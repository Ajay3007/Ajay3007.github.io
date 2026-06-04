/**
 * dns_parser.c — Module 06: DNS Parser
 *
 * Parses DNS messages from raw wire bytes. Covers:
 *   - Query parsing (question section: qname, qtype, qclass)
 *   - Response parsing (answer section: A, AAAA, CNAME records)
 *   - DNS over UDP (direct DNS message)
 *   - DNS over TCP (2-byte length prefix stripped before calling parser)
 *   - Pointer compression (RFC 1035 §4.1.4)
 *   - Name normalisation (lowercase)
 *
 * The flow in the real DP application for a DNS packet:
 *
 *   1. Ethernet/IP/UDP headers parsed (Module 05)
 *   2. UDP dst_port == 53 detected
 *   3. dns_parse_message() called on UDP payload
 *   4. msg.qname + msg.qtype passed to url_policy_for_dns()
 *   5. Hash table lookup: exact domain match → filter_details
 *   6. If no exact match → Hyperscan regex scan (Module 22)
 *   7. Policy decision → ALLOW / DROP / SINKHOLE
 *   8. If SINKHOLE → build DNS response in-place (Module 23)
 */

#include "dns_parser.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>
#include <arpa/inet.h>

/* ───────────────────────────────────────────────────────────
 * dns_type_str / dns_rcode_str
 * ─────────────────────────────────────────────────────────── */
const char *dns_type_str(uint16_t type)
{
    switch (type) {
    case DNS_TYPE_A:     return "A";
    case DNS_TYPE_AAAA:  return "AAAA";
    case DNS_TYPE_CNAME: return "CNAME";
    case DNS_TYPE_MX:    return "MX";
    case 2:              return "NS";
    case 6:              return "SOA";
    case 12:             return "PTR";
    case 33:             return "SRV";
    default:             return "?";
    }
}

const char *dns_rcode_str(uint16_t rcode)
{
    switch (rcode) {
    case 0:  return "NOERROR";
    case 1:  return "FORMERR";
    case 2:  return "SERVFAIL";
    case 3:  return "NXDOMAIN";
    case 4:  return "NOTIMP";
    case 5:  return "REFUSED";
    default: return "?";
    }
}

/* ───────────────────────────────────────────────────────────
 * dns_normalize_name — lowercase in place
 *
 * In the real DP application, TLD normalisation also strips trailing
 * dots and handles punycode, but those are separate modules.
 * Lowercasing alone covers 99% of the case sensitivity issue.
 * ─────────────────────────────────────────────────────────── */
void dns_normalize_name(char *name)
{
    while (*name) {
        *name = (char)tolower((unsigned char)*name);
        name++;
    }
}

/* ───────────────────────────────────────────────────────────
 * dns_parse_qname — decode DNS label-encoded name
 *
 * DNS wire format name encoding (RFC 1035 §3.1):
 *
 *   "www.example.com" encoded as:
 *     03 77 77 77        ← length 3, then "www"
 *     07 65 78 61 6d 70 6c 65  ← length 7, then "example"
 *     03 63 6f 6d        ← length 3, then "com"
 *     00                 ← root label (end of name)
 *
 * Pointer compression (§4.1.4):
 *   When top 2 bits of a length byte are 11, the next byte forms a
 *   14-bit offset pointing to a name elsewhere in the message.
 *   This saves space in responses by back-referencing the question.
 *
 *   0xC0 0x0C = pointer to offset 12 (the start of the question name)
 *
 * Returns bytes consumed at start offset (not counting pointer jumps).
 * ─────────────────────────────────────────────────────────── */
int dns_parse_qname(const uint8_t *wire, int wire_len,
                    int offset, char *out, int out_len)
{
    int out_pos  = 0;
    int start    = offset;
    int jumped   = 0;      /* 1 once we've followed a pointer */
    int jump_ret = -1;     /* bytes consumed before the pointer */
    int loops    = 0;      /* guard against infinite compression loops */

    while (offset < wire_len && loops++ < 128) {
        uint8_t label_len = wire[offset];

        /* End of name */
        if (label_len == 0) {
            if (out_pos > 0)
                out[out_pos - 1] = '\0';  /* overwrite trailing '.' */
            else
                out[0] = '\0';
            return jumped ? jump_ret : (offset - start + 1);
        }

        /* Pointer compression: top 2 bits = 11 */
        if ((label_len & 0xC0) == 0xC0) {
            if (offset + 1 >= wire_len) return -1;
            int ptr = ((label_len & 0x3F) << 8) | wire[offset + 1];
            if (!jumped)
                jump_ret = offset - start + 2;
            jumped = 1;
            offset = ptr;
            continue;
        }

        /* Label too long — malformed packet */
        if (label_len > 63) return -1;

        offset++;
        if (offset + label_len > wire_len) return -1;
        if (out_pos + label_len + 1 >= out_len) return -1;

        memcpy(out + out_pos, wire + offset, label_len);
        out_pos += label_len;
        out[out_pos++] = '.';
        offset += label_len;
    }

    return -1;  /* no root label found */
}

/* ───────────────────────────────────────────────────────────
 * dns_parse_message — full DNS message parser
 * ─────────────────────────────────────────────────────────── */
int dns_parse_message(const uint8_t *wire, int wire_len, dns_message_t *msg)
{
    int offset;
    int i;

    if (!wire || !msg || wire_len < DNS_HDR_LEN)
        return -1;

    memset(msg, 0, sizeof(*msg));

    /* ── Parse header (12 bytes) ── */
    const dns_hdr_t *hdr = (const dns_hdr_t *)wire;
    uint16_t flags = ntohs(hdr->flags);

    msg->id                = ntohs(hdr->id);
    msg->is_response       = (flags & DNS_FLAG_QR) ? 1 : 0;
    msg->recursion_desired = (flags & DNS_FLAG_RD) ? 1 : 0;
    msg->recursion_avail   = (flags & DNS_FLAG_RA) ? 1 : 0;
    msg->authoritative     = (flags & DNS_FLAG_AA) ? 1 : 0;
    msg->rcode             = flags & DNS_RCODE_MASK;
    msg->qdcount           = ntohs(hdr->qdcount);
    msg->ancount           = ntohs(hdr->ancount);
    msg->num_answers       = 0;

    offset = DNS_HDR_LEN;

    /* ── Parse question section ──
     *
     * We only parse the first question. DNS allows multiple questions
     * but virtually no real implementation sends more than one, and
     * the RFC says resolvers MAY return FORMERR for multiple questions.
     */
    if (msg->qdcount == 0) {
        msg->question_wire_end = offset;
        return 0;   /* valid but empty query */
    }

    /* qname */
    int consumed = dns_parse_qname(wire, wire_len, offset,
                                    msg->qname, MAX_DNS_NAME_LEN);
    if (consumed < 0) return -1;

    dns_normalize_name(msg->qname);

    offset += consumed;

    /* qtype + qclass (4 bytes) */
    if (offset + 4 > wire_len) return -1;
    msg->qtype  = read_u16_be(wire + offset);
    msg->qclass = read_u16_be(wire + offset + 2);
    offset += 4;

    msg->question_wire_end = offset;  /* save for sinkhole (Module 23) */

    /* Skip additional questions if any */
    for (i = 1; i < msg->qdcount && offset < wire_len; i++) {
        consumed = dns_parse_qname(wire, wire_len, offset,
                                    msg->qname, MAX_DNS_NAME_LEN);
        if (consumed < 0) break;
        offset += consumed + 4;   /* skip qtype + qclass */
    }

    /* ── Parse answer section (responses only) ── */
    if (!msg->is_response || msg->ancount == 0)
        return 0;

    int max_ans = msg->ancount < MAX_DNS_ANSWERS
                      ? msg->ancount : MAX_DNS_ANSWERS;

    for (i = 0; i < max_ans && offset < wire_len; i++) {
        dns_answer_t *ans = &msg->answers[i];

        /* name (may be a pointer to the question) */
        consumed = dns_parse_qname(wire, wire_len, offset,
                                    ans->name, MAX_DNS_NAME_LEN);
        if (consumed < 0) break;
        offset += consumed;

        /* type + class + ttl + rdlength = 10 bytes */
        if (offset + 10 > wire_len) break;
        ans->type     = read_u16_be(wire + offset);
        ans->cls      = read_u16_be(wire + offset + 2);
        ans->ttl      = read_u32_be(wire + offset + 4);
        ans->rdlength = read_u16_be(wire + offset + 8);
        offset += 10;

        if (offset + ans->rdlength > wire_len) break;

        /* rdata: decode based on type */
        switch (ans->type) {

        case DNS_TYPE_A:
            /* 4 bytes: IPv4 address */
            if (ans->rdlength == 4) {
                memcpy(ans->rdata, wire + offset, 4);
            }
            break;

        case DNS_TYPE_AAAA:
            /* 16 bytes: IPv6 address */
            if (ans->rdlength == 16) {
                memcpy(ans->rdata, wire + offset, 16);
            }
            break;

        case DNS_TYPE_CNAME:
            /*
             * CNAME rdata is another label-encoded name.
             * Pointer compression often appears here:
             *   "cdn.example.com" → pointer back to "example.com" in question.
             */
            dns_parse_qname(wire, wire_len, offset,
                             ans->cname, MAX_DNS_NAME_LEN);
            dns_normalize_name(ans->cname);
            break;

        default:
            /* copy raw rdata for other types */
            if (ans->rdlength <= (uint16_t)sizeof(ans->rdata))
                memcpy(ans->rdata, wire + offset, ans->rdlength);
            break;
        }

        offset += ans->rdlength;
        msg->num_answers++;
    }

    return 0;
}

/* ───────────────────────────────────────────────────────────
 * dns_dump — pretty-print a parsed message
 * ─────────────────────────────────────────────────────────── */
void dns_dump(const dns_message_t *msg)
{
    char ip_buf[INET6_ADDRSTRLEN];
    int  i;

    printf("  ID      : 0x%04x\n", msg->id);
    printf("  Type    : %s\n", msg->is_response ? "RESPONSE" : "QUERY");
    printf("  RD/RA   : %d/%d\n", msg->recursion_desired, msg->recursion_avail);
    if (msg->is_response)
        printf("  RCODE   : %s (%u)\n", dns_rcode_str(msg->rcode), msg->rcode);

    printf("  [Question]\n");
    printf("    qname : %s\n", msg->qname[0] ? msg->qname : "(empty)");
    printf("    qtype : %s (%u)\n", dns_type_str(msg->qtype), msg->qtype);
    printf("    qclass: %u\n", msg->qclass);

    if (msg->num_answers > 0) {
        printf("  [Answers: %d]\n", msg->num_answers);
        for (i = 0; i < msg->num_answers; i++) {
            const dns_answer_t *a = &msg->answers[i];
            printf("    [%d] name=%s  type=%s  ttl=%u",
                   i, a->name, dns_type_str(a->type), a->ttl);
            switch (a->type) {
            case DNS_TYPE_A:
                inet_ntop(AF_INET, a->rdata, ip_buf, sizeof(ip_buf));
                printf("  ip=%s", ip_buf);
                break;
            case DNS_TYPE_AAAA:
                inet_ntop(AF_INET6, a->rdata, ip_buf, sizeof(ip_buf));
                printf("  ip=%s", ip_buf);
                break;
            case DNS_TYPE_CNAME:
                printf("  cname=%s", a->cname);
                break;
            }
            printf("\n");
        }
    }
}

/* ═══════════════════════════════════════════════════════════
 * Demo
 *
 * Simulates the exact DNS parsing flow in the DP application:
 *   packet in → parse headers (Module 05) → parse DNS (this module)
 *   → domain extracted → policy lookup (Module 22)
 * ═══════════════════════════════════════════════════════════ */

/* ─── Sample packets ─────────────────────────────────────── */

/*
 * DNS query: A record for "blocked-malware.example.com"
 * This is the kind of query the DP application would receive for a domain
 * in its blocked list. UDP payload starts after the UDP header.
 */
static const uint8_t query_a[] = {
    0xca,0xfe,                               /* ID: 0xcafe */
    0x01,0x00,                               /* flags: RD=1 */
    0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00, /* qdcount=1 */
    /* qname: blocked-malware.example.com */
    0x0f,                                    /* 15: "blocked-malware" */
    0x62,0x6c,0x6f,0x63,0x6b,0x65,0x64,
    0x2d,0x6d,0x61,0x6c,0x77,0x61,0x72,0x65,
    0x07,0x65,0x78,0x61,0x6d,0x70,0x6c,0x65, /* 7: "example" */
    0x03,0x63,0x6f,0x6d,                     /* 3: "com" */
    0x00,                                    /* root */
    0x00,0x01,                               /* QTYPE: A */
    0x00,0x01,                               /* QCLASS: IN */
};

/*
 * DNS query: AAAA record for "GOOGLE.COM"
 * uppercase to demonstrate normalization
 */
static const uint8_t query_aaaa[] = {
    0xbe,0xef,                               /* ID: 0xbeef */
    0x01,0x00,
    0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,
    /* qname: GOOGLE.COM  (uppercase — should normalize to google.com) */
    0x06,0x47,0x4f,0x4f,0x47,0x4c,0x45,     /* 6: "GOOGLE" */
    0x03,0x43,0x4f,0x4d,                     /* 3: "COM" */
    0x00,
    0x00,0x1c,                               /* QTYPE: AAAA */
    0x00,0x01,
};

/*
 * DNS response: A record for "www.example.com" → 93.184.216.34
 * Includes pointer compression in the answer (0xc00c points back to qname).
 */
static const uint8_t response_a[] = {
    0x12,0x34,                               /* ID: 0x1234 */
    0x81,0x80,                               /* flags: QR=1, RD=1, RA=1 */
    0x00,0x01,                               /* qdcount=1 */
    0x00,0x01,                               /* ancount=1 */
    0x00,0x00,0x00,0x00,                     /* nscount=0, arcount=0 */
    /* question: www.example.com A IN */
    0x03,0x77,0x77,0x77,                     /* "www" */
    0x07,0x65,0x78,0x61,0x6d,0x70,0x6c,0x65,/* "example" */
    0x03,0x63,0x6f,0x6d,0x00,               /* "com" + root */
    0x00,0x01,0x00,0x01,                     /* QTYPE A, QCLASS IN */
    /* answer: name=ptr(0x0c), A, IN, ttl=300, rdlen=4, ip=93.184.216.34 */
    0xc0,0x0c,                               /* name pointer to offset 12 */
    0x00,0x01,                               /* type: A */
    0x00,0x01,                               /* class: IN */
    0x00,0x00,0x01,0x2c,                     /* TTL: 300 */
    0x00,0x04,                               /* rdlength: 4 */
    0x5d,0xb8,0xd8,0x22,                     /* 93.184.216.34 */
};

/*
 * DNS response: CNAME + AAAA chain
 * cdn.example.com → CNAME origin.example.com → AAAA 2606:2800:220:1:248:1893:25c8:1946
 *
 * This is common for CDN-hosted domains. The policy engine checks
 * BOTH the original qname (cdn.example.com) AND follows CNAMEs.
 */
static const uint8_t response_cname_aaaa[] = {
    0xab,0xcd,                               /* ID */
    0x81,0x80,                               /* QR=1, RD=1, RA=1 */
    0x00,0x01,                               /* qdcount=1 */
    0x00,0x02,                               /* ancount=2 */
    0x00,0x00,0x00,0x00,
    /* question: cdn.example.com AAAA IN */
    0x03,0x63,0x64,0x6e,                     /* "cdn" */
    0x07,0x65,0x78,0x61,0x6d,0x70,0x6c,0x65,/* "example" */
    0x03,0x63,0x6f,0x6d,0x00,               /* "com" + root */
    0x00,0x1c,0x00,0x01,                     /* QTYPE AAAA, QCLASS IN */
    /* answer 1: cdn.example.com CNAME origin.example.com (ptr back + new label) */
    0xc0,0x0c,                               /* name = ptr to offset 12 (cdn.example.com) */
    0x00,0x05,                               /* type: CNAME */
    0x00,0x01,                               /* class: IN */
    0x00,0x00,0x00,0x3c,                     /* TTL: 60 */
    0x00,0x0e,                               /* rdlength: 14 */
    0x06,0x6f,0x72,0x69,0x67,0x69,0x6e,     /* "origin" */
    0xc0,0x10,                               /* ptr to offset 16 = "example.com" */
    /* answer 2: origin.example.com AAAA 2606:2800:220:1:248:1893:25c8:1946 */
    0xc0,0x31,                               /* name ptr to answer1 rdata "origin.example.com" */
    0x00,0x1c,                               /* type: AAAA */
    0x00,0x01,                               /* class: IN */
    0x00,0x00,0x01,0x2c,                     /* TTL: 300 */
    0x00,0x10,                               /* rdlength: 16 */
    0x26,0x06,0x28,0x00,0x02,0x20,0x00,0x01, /* 2606:2800:220:1 */
    0x02,0x48,0x18,0x93,0x25,0xc8,0x19,0x46, /* :248:1893:25c8:1946 */
};

/*
 * DNS over TCP: A query for "ads.tracker.io"
 * Same DNS message as UDP but prefixed with a 2-byte length field.
 * In the real app, parse_dns_ipv4_request_packet_over_tcp() strips
 * the 2-byte prefix before calling the DNS parser.
 */
static const uint8_t dns_over_tcp[] = {
    /* 2-byte TCP length prefix (RFC 1035 §4.2.2) */
    0x00, 0x26,                              /* DNS message length = 38 bytes */
    /* DNS message starts here */
    0x11,0x11,                               /* ID: 0x1111 */
    0x01,0x00,                               /* RD=1 */
    0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,
    /* qname: ads.tracker.io */
    0x03,0x61,0x64,0x73,                     /* "ads" */
    0x07,0x74,0x72,0x61,0x63,0x6b,0x65,0x72,/* "tracker" */
    0x02,0x69,0x6f,                          /* "io" */
    0x00,
    0x00,0x01,0x00,0x01,                     /* A IN */
};

/* ─── Tests ──────────────────────────────────────────────── */

static void test_query_a(void)
{
    dns_message_t msg;
    printf("\n--- Test 1: A query for blocked-malware.example.com ---\n");
    assert(dns_parse_message(query_a, sizeof(query_a), &msg) == 0);
    dns_dump(&msg);

    assert(msg.is_response       == 0);
    assert(msg.qtype             == DNS_TYPE_A);
    assert(strcmp(msg.qname, "blocked-malware.example.com") == 0);
    assert(msg.question_wire_end == (int)sizeof(query_a));

    /*
     * In the real app, after this parse:
     *   url_policy_for_dns(msg.qname, msg.qtype, ...)
     *   → rte_hash_lookup_data(group->domain_details_table, msg.qname, &fd)
     *   → if blocked: build sinkhole response (Module 23)
     */
    printf("  → policy engine would look up: \"%s\" (type %s)\n",
           msg.qname, dns_type_str(msg.qtype));
    printf("  PASS\n");
}

static void test_query_aaaa_normalize(void)
{
    dns_message_t msg;
    printf("\n--- Test 2: AAAA query — uppercase normalization ---\n");
    assert(dns_parse_message(query_aaaa, sizeof(query_aaaa), &msg) == 0);
    dns_dump(&msg);

    assert(msg.qtype == DNS_TYPE_AAAA);
    assert(strcmp(msg.qname, "google.com") == 0);  /* was "GOOGLE.COM" in wire */
    printf("  'GOOGLE.COM' normalized to '%s'\n", msg.qname);
    printf("  PASS\n");
}

static void test_response_a(void)
{
    dns_message_t msg;
    printf("\n--- Test 3: A response with pointer compression ---\n");
    assert(dns_parse_message(response_a, sizeof(response_a), &msg) == 0);
    dns_dump(&msg);

    assert(msg.is_response   == 1);
    assert(msg.num_answers   == 1);
    assert(msg.answers[0].type == DNS_TYPE_A);

    /* Verify decoded IP: 93.184.216.34 */
    char ip[16];
    inet_ntop(AF_INET, msg.answers[0].rdata, ip, sizeof(ip));
    assert(strcmp(ip, "93.184.216.34") == 0);
    printf("  Pointer compression decoded correctly: %s → %s\n",
           msg.qname, ip);
    printf("  PASS\n");
}

static void test_response_cname_aaaa(void)
{
    dns_message_t msg;
    printf("\n--- Test 4: CNAME + AAAA chain response ---\n");
    assert(dns_parse_message(response_cname_aaaa, sizeof(response_cname_aaaa),
                              &msg) == 0);
    dns_dump(&msg);

    assert(msg.num_answers >= 2);
    assert(msg.answers[0].type == DNS_TYPE_CNAME);
    assert(msg.answers[1].type == DNS_TYPE_AAAA);
    printf("  CNAME decoded: cdn.example.com → %s\n", msg.answers[0].cname);
    printf("  PASS\n");
}

static void test_dns_over_tcp(void)
{
    dns_message_t msg;
    printf("\n--- Test 5: DNS over TCP (strip 2-byte length prefix) ---\n");

    /*
     * In the real app, parse_dns_ipv4_request_packet_over_tcp() does:
     *   uint16_t dns_len = read_u16_be(tcp_payload);
     *   uint8_t *dns_msg = tcp_payload + DNS_TCP_LEN_PREFIX;
     *   dns_parse_message(dns_msg, dns_len, &msg);
     */
    uint16_t dns_len = read_u16_be(dns_over_tcp);
    const uint8_t *dns_msg = dns_over_tcp + DNS_TCP_LEN_PREFIX;

    printf("  TCP length prefix: %u bytes\n", dns_len);
    assert((int)dns_len == (int)sizeof(dns_over_tcp) - DNS_TCP_LEN_PREFIX);

    assert(dns_parse_message(dns_msg, dns_len, &msg) == 0);
    dns_dump(&msg);

    assert(strcmp(msg.qname, "ads.tracker.io") == 0);
    printf("  Extracted domain: \"%s\"\n", msg.qname);
    printf("  PASS\n");
}

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    printf("=== Module 06: DNS Parser ===\n");

    test_query_a();
    test_query_aaaa_normalize();
    test_response_a();
    test_response_cname_aaaa();
    test_dns_over_tcp();

    printf("\n--- DNS parsing → policy lookup flow ---\n");
    printf("  1. UDP dst_port == 53 detected\n");
    printf("  2. dns_parse_message(udp_payload, udp_payload_len, &msg)\n");
    printf("  3. domain = msg.qname     e.g. \"ads.tracker.io\"\n");
    printf("  4. qtype  = msg.qtype     DNS_TYPE_A or DNS_TYPE_AAAA\n");
    printf("  5. rte_hash_lookup_data(group->domain_details_table, domain, &fd)\n");
    printf("  6. if hit  → apply filter_details policy\n");
    printf("  7. if miss → hs_scan_domain_group(domain, ...) [Module 22]\n");
    printf("  8. if blocked → build sinkhole response [Module 23]\n");
    printf("     qtype A    → inject A  answer with walled-garden IPv4\n");
    printf("     qtype AAAA → inject AAAA answer with walled-garden IPv6\n");

    printf("\nAll tests passed.\n");
    return 0;
}
