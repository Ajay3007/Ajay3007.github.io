/**
 * dns_sinkhole.c — Module 18: DNS Sinkhole (In-place Packet Rewrite)
 *
 * When url_policy_for_dns() returns PROCESS_WORKFLOW (Module 17),
 * the DNS query must be turned into a sinkhole response in-place — without
 * allocating a new packet buffer.
 *
 * What "in-place" means:
 *   The original query mbuf is reused. We modify its bytes directly:
 *     1. Swap Ethernet src/dst MAC
 *     2. Swap IPv4/IPv6 src/dst addresses
 *     3. Swap UDP src/dst ports (or update TCP length)
 *     4. Set DNS QR=1 (response), ancount=1
 *     5. Append DNS answer section (A or AAAA record pointing to walled garden)
 *     6. Update IP total_len and UDP dgram_len
 *     7. (DPDK only) Set TX hardware checksum offload flags on mbuf
 *
 * Why in-place?
 *   Allocating a new mbuf for each blocked DNS packet costs a pool dequeue
 *   (~10 ns) + memcpy (~200 ns for 100 bytes) + pool enqueue for the old mbuf.
 *   At 200K blocked DNS/sec that's 42 ms/sec of extra overhead.
 *   In-place rewrite: just pointer arithmetic and a few memcpy/memset calls.
 *
 * In the real the DP application project (pkt_proc.h):
 *   dns_build_sinkhole_v4()    — UDP/IPv4
 *   dns_build_sinkhole_v6()    — UDP/IPv6
 *   dns_build_sinkhole_v4_tcp()— TCP/IPv4
 *   dns_build_sinkhole_v6_tcp()— TCP/IPv6
 *
 * This module is PURE C — runs without DPDK or Hyperscan.
 * Build: make
 * Run:   ./dns_sinkhole
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <assert.h>
#include <arpa/inet.h>   /* htons, htonl, ntohs, ntohl */

#include "../05-packet-structs/packet_structs.h"

/* ───────────────────────────────────────────────────────────
 * Walled garden addresses
 *
 * When a blocked DNS query arrives, the sinkhole response redirects
 * the client to these IPs. The walled garden server at these IPs
 * serves an HTTP "blocked" page for web traffic.
 *
 * In the DP application, these are configured values read from config at startup.
 * ─────────────────────────────────────────────────────────── */
#define WALLED_GARDEN_IPV4   0x0A010101   /* 10.1.1.1 */
#define WALLED_GARDEN_IPV6   {0xfd,0x00,0x00,0x00,0x00,0x00,0x00,0x00,\
                               0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01}
#define DNS_SINKHOLE_TTL     60           /* seconds — short so client retries */

/* ───────────────────────────────────────────────────────────
 * DNS answer section sizes
 *
 *  Field            Bytes
 *  ---------------  -----
 *  Name (ptr)       2       0xC0 0x0C (pointer to question name at offset 12)
 *  Type             2       0x0001 (A) or 0x001C (AAAA)
 *  Class            2       0x0001 (IN)
 *  TTL              4
 *  RDLENGTH         2       4 (IPv4) or 16 (IPv6)
 *  RDATA            4/16
 *  ---------------  -----
 *  Total (A):       16
 *  Total (AAAA):    28
 * ─────────────────────────────────────────────────────────── */
#define DNS_ANSWER_A_LEN     16
#define DNS_ANSWER_AAAA_LEN  28

/* Maximum packet buffer size for our tests */
#define MAX_PKT_BUF   2048

/* ───────────────────────────────────────────────────────────
 * build_dns_answer — construct the DNS answer section bytes
 *
 * @buf     : output buffer to write answer into
 * @qtype   : DNS_TYPE_A (1) or DNS_TYPE_AAAA (28)
 * @wg_ipv4 : walled garden IPv4 (network byte order), used for A
 * @wg_ipv6 : walled garden IPv6 (16 bytes), used for AAAA
 *
 * Returns the number of bytes written.
 * ─────────────────────────────────────────────────────────── */
static int build_dns_answer(uint8_t *buf, uint16_t qtype,
                              uint32_t wg_ipv4, const uint8_t *wg_ipv6)
{
    int off = 0;

    /* Name: pointer to the question name (offset 12 in the DNS message) */
    buf[off++] = 0xC0;
    buf[off++] = 0x0C;   /* 0xC00C = "pointer to offset 12" */

    /* Type */
    write_u16_be(buf + off, qtype);
    off += 2;

    /* Class: IN */
    write_u16_be(buf + off, DNS_CLASS_IN);
    off += 2;

    /* TTL */
    write_u32_be(buf + off, DNS_SINKHOLE_TTL);
    off += 4;

    if (qtype == DNS_TYPE_A) {
        /* RDLENGTH: 4 bytes (IPv4) */
        write_u16_be(buf + off, 4);
        off += 2;
        /* RDATA: walled garden IPv4 in network byte order */
        write_u32_be(buf + off, ntohl(wg_ipv4));
        off += 4;
    } else {
        /* RDLENGTH: 16 bytes (IPv6) */
        write_u16_be(buf + off, 16);
        off += 2;
        /* RDATA: walled garden IPv6 */
        memcpy(buf + off, wg_ipv6, 16);
        off += 16;
    }

    return off;
}

/* ───────────────────────────────────────────────────────────
 * dns_sinkhole_udp_ipv4 — in-place rewrite for UDP/IPv4
 *
 * Mirrors dns_build_sinkhole_v4() in pkt_proc.h.
 *
 * @pkt         : raw packet buffer (Ethernet + IPv4 + UDP + DNS)
 * @pkt_len     : current packet length
 * @buf_capacity: total buffer capacity (must have room for answer)
 * @qtype       : DNS_TYPE_A or DNS_TYPE_AAAA (from DNS query)
 * @question_end: byte offset where the DNS question section ends
 *                (from dns_parse_message().question_wire_end + DNS header offset)
 *
 * Returns new packet length, or -1 on error.
 *
 * In DPDK: pkt = rte_pktmbuf_mtod(mbuf, uint8_t *)
 *          extend tail: rte_pktmbuf_append(mbuf, answer_len)
 *          then set: m->ol_flags |= TX_IPV4|TX_IP_CKSUM|TX_UDP_CKSUM
 * ─────────────────────────────────────────────────────────── */
int dns_sinkhole_udp_ipv4(uint8_t *pkt, int pkt_len, int buf_capacity,
                            uint16_t qtype, int question_end)
{
    if (pkt_len < ETH_HDR_LEN + IPV4_HDR_MIN + UDP_HDR_LEN + DNS_HDR_LEN)
        return -1;

    int answer_len = (qtype == DNS_TYPE_A) ? DNS_ANSWER_A_LEN : DNS_ANSWER_AAAA_LEN;
    int new_pkt_len = pkt_len + answer_len;

    if (new_pkt_len > buf_capacity)
        return -1;  /* no room to append answer section */

    /* ── Pointers to each header layer ── */
    eth_hdr_t  *eth = (eth_hdr_t *)pkt;
    ipv4_hdr_t *ip4 = (ipv4_hdr_t *)(pkt + ETH_HDR_LEN);
    udp_hdr_t  *udp = (udp_hdr_t *)(pkt + ETH_HDR_LEN + IPV4_HDR_MIN);
    dns_hdr_t  *dns = (dns_hdr_t *) (pkt + ETH_HDR_LEN + IPV4_HDR_MIN + UDP_HDR_LEN);

    /* ── Step 1: Swap Ethernet src ↔ dst ──
     *
     * The response must go back to the client who sent the query.
     * Swapping src/dst MAC turns "client → server" into "server → client".
     */
    uint8_t tmp_mac[6];
    memcpy(tmp_mac,       eth->dst_mac, 6);
    memcpy(eth->dst_mac,  eth->src_mac, 6);
    memcpy(eth->src_mac,  tmp_mac,      6);

    /* ── Step 2: Swap IPv4 src ↔ dst ── */
    uint32_t tmp_ip = ip4->src_ip;
    ip4->src_ip     = ip4->dst_ip;
    ip4->dst_ip     = tmp_ip;

    /* ── Step 3: Swap UDP src ↔ dst port ──
     *
     * Query:    client_port → 53
     * Response: 53 → client_port
     */
    uint16_t tmp_port = udp->src_port;
    udp->src_port     = udp->dst_port;
    udp->dst_port     = tmp_port;

    /* ── Step 4: Build DNS answer section ──
     *
     * Append at the end of the packet (after the question section).
     * question_end is the absolute offset from start of DNS message
     * (i.e., relative to dns header).
     * We write starting after the full question section in the raw packet.
     */
    int dns_offset = ETH_HDR_LEN + IPV4_HDR_MIN + UDP_HDR_LEN;
    uint8_t answer_buf[DNS_ANSWER_AAAA_LEN];
    uint8_t wg_ipv6[] = WALLED_GARDEN_IPV6;

    int written = build_dns_answer(answer_buf, qtype,
                                    htonl(WALLED_GARDEN_IPV4), wg_ipv6);
    assert(written == answer_len);

    /* Append answer bytes at the tail of the packet */
    memcpy(pkt + dns_offset + question_end, answer_buf, answer_len);

    /* ── Step 5: Update DNS header ── */
    uint16_t flags = ntohs(dns->flags);
    flags |= DNS_FLAG_QR;      /* set QR bit: 0=query → 1=response */
    flags |= DNS_FLAG_RA;      /* recursion available */
    flags &= ~DNS_FLAG_AA;     /* not authoritative */
    dns->flags   = htons(flags);
    dns->ancount = htons(1);   /* 1 answer record */
    /* qdcount stays the same (1 question echoed back) */

    /* ── Step 6: Update UDP length ── */
    uint16_t new_udp_len = ntohs(udp->dgram_len) + (uint16_t)answer_len;
    udp->dgram_len = htons(new_udp_len);

    /*
     * UDP checksum:
     * Option A: set to 0 (UDP checksum is optional for IPv4).
     *           Receivers must accept this per RFC 768.
     * Option B: set TX_UDP_CKSUM offload flag (DPDK handles it in HW).
     *
     * the DP application uses Option B (hardware offload) for efficiency.
     * Here (pure C, no NIC) we use Option A.
     */
    udp->checksum = 0;

    /* ── Step 7: Update IPv4 total_len ── */
    uint16_t new_ip_len = ntohs(ip4->total_len) + (uint16_t)answer_len;
    ip4->total_len = htons(new_ip_len);

    /*
     * IPv4 checksum:
     * In DPDK: ip4->checksum = 0; m->ol_flags |= TX_IP_CKSUM;
     * Here (pure C): compute software checksum.
     */
    ip4->checksum = 0;
    /* Software IP checksum (not done here — set 0 for demo) */

    return new_pkt_len;
}

/* ───────────────────────────────────────────────────────────
 * dns_sinkhole_udp_ipv6 — in-place rewrite for UDP/IPv6
 *
 * Mirrors dns_build_sinkhole_v6() in pkt_proc.h.
 * IPv6 header layout is different: fixed 40 bytes, payload_len field
 * instead of total_len.
 * ─────────────────────────────────────────────────────────── */
int dns_sinkhole_udp_ipv6(uint8_t *pkt, int pkt_len, int buf_capacity,
                            uint16_t qtype, int question_end)
{
    if (pkt_len < ETH_HDR_LEN + IPV6_HDR_LEN + UDP_HDR_LEN + DNS_HDR_LEN)
        return -1;

    int answer_len  = (qtype == DNS_TYPE_A) ? DNS_ANSWER_A_LEN : DNS_ANSWER_AAAA_LEN;
    int new_pkt_len = pkt_len + answer_len;
    if (new_pkt_len > buf_capacity) return -1;

    eth_hdr_t  *eth = (eth_hdr_t *)pkt;
    ipv6_hdr_t *ip6 = (ipv6_hdr_t *)(pkt + ETH_HDR_LEN);
    udp_hdr_t  *udp = (udp_hdr_t *) (pkt + ETH_HDR_LEN + IPV6_HDR_LEN);
    dns_hdr_t  *dns = (dns_hdr_t *)  (pkt + ETH_HDR_LEN + IPV6_HDR_LEN + UDP_HDR_LEN);

    /* Swap Ethernet */
    uint8_t tmp_mac[6];
    memcpy(tmp_mac, eth->dst_mac, 6);
    memcpy(eth->dst_mac, eth->src_mac, 6);
    memcpy(eth->src_mac, tmp_mac, 6);

    /* Swap IPv6 src ↔ dst (16 bytes each) */
    uint8_t tmp_ip6[16];
    memcpy(tmp_ip6,       ip6->src_ip, 16);
    memcpy(ip6->src_ip,   ip6->dst_ip, 16);
    memcpy(ip6->dst_ip,   tmp_ip6,     16);

    /* Swap UDP ports */
    uint16_t tmp_port = udp->src_port;
    udp->src_port     = udp->dst_port;
    udp->dst_port     = tmp_port;

    /* Append answer */
    int dns_offset = ETH_HDR_LEN + IPV6_HDR_LEN + UDP_HDR_LEN;
    uint8_t answer_buf[DNS_ANSWER_AAAA_LEN];
    uint8_t wg_ipv6[] = WALLED_GARDEN_IPV6;
    int written = build_dns_answer(answer_buf, qtype,
                                    htonl(WALLED_GARDEN_IPV4), wg_ipv6);
    memcpy(pkt + dns_offset + question_end, answer_buf, written);

    /* Update DNS header */
    uint16_t flags = ntohs(dns->flags);
    flags |= (DNS_FLAG_QR | DNS_FLAG_RA);
    dns->flags   = htons(flags);
    dns->ancount = htons(1);

    /* Update UDP length */
    udp->dgram_len = htons(ntohs(udp->dgram_len) + (uint16_t)answer_len);
    udp->checksum  = 0;

    /* Update IPv6 payload_len (does NOT include IPv6 header itself) */
    ip6->payload_len = htons(ntohs(ip6->payload_len) + (uint16_t)answer_len);

    return new_pkt_len;
}

/* ───────────────────────────────────────────────────────────
 * dns_sinkhole_tcp_ipv4 — in-place rewrite for TCP/IPv4 DNS
 *
 * Mirrors dns_build_sinkhole_v4_tcp() in pkt_proc.h.
 *
 * DNS over TCP has a 2-byte length prefix before the DNS message.
 * The rewrite must update this length field too.
 * ─────────────────────────────────────────────────────────── */
int dns_sinkhole_tcp_ipv4(uint8_t *pkt, int pkt_len, int buf_capacity,
                            uint16_t qtype, int question_end,
                            int tcp_hdr_len)
{
    /* Minimum: ETH + IPv4 + TCP + DNS_TCP_LEN + DNS_HDR */
    int min_len = ETH_HDR_LEN + IPV4_HDR_MIN + tcp_hdr_len
                  + DNS_TCP_LEN_PREFIX + DNS_HDR_LEN;
    if (pkt_len < min_len) return -1;

    int answer_len  = (qtype == DNS_TYPE_A) ? DNS_ANSWER_A_LEN : DNS_ANSWER_AAAA_LEN;
    int new_pkt_len = pkt_len + answer_len;
    if (new_pkt_len > buf_capacity) return -1;

    eth_hdr_t  *eth = (eth_hdr_t *)pkt;
    ipv4_hdr_t *ip4 = (ipv4_hdr_t *)(pkt + ETH_HDR_LEN);
    tcp_hdr_t  *tcp = (tcp_hdr_t *) (pkt + ETH_HDR_LEN + IPV4_HDR_MIN);

    /* TCP payload starts after TCP header */
    uint8_t *tcp_payload = (uint8_t *)tcp + tcp_hdr_len;

    /* DNS TCP length prefix (2 bytes) + DNS message */
    uint16_t dns_msg_len = read_u16_be(tcp_payload);
    dns_hdr_t *dns = (dns_hdr_t *)(tcp_payload + DNS_TCP_LEN_PREFIX);

    /* Swap Ethernet */
    uint8_t tmp_mac[6];
    memcpy(tmp_mac, eth->dst_mac, 6);
    memcpy(eth->dst_mac, eth->src_mac, 6);
    memcpy(eth->src_mac, tmp_mac, 6);

    /* Swap IPv4 src ↔ dst */
    uint32_t tmp_ip = ip4->src_ip;
    ip4->src_ip = ip4->dst_ip;
    ip4->dst_ip = tmp_ip;

    /* Swap TCP src ↔ dst port */
    uint16_t tmp_port = tcp->src_port;
    tcp->src_port = tcp->dst_port;
    tcp->dst_port = tmp_port;

    /*
     * For TCP, we must also swap seq/ack numbers and set ACK flag.
     * In the real the DP application app, this is handled by maintaining TCP state
     * (connection_track_table). Here we do a minimal swap for demo purposes.
     */
    uint32_t tmp_seq = tcp->seq_num;
    tcp->seq_num = tcp->ack_num;
    tcp->ack_num = htonl(ntohl(tmp_seq) + (uint32_t)pkt_len);
    tcp->flags   = TCP_FLAG_ACK | TCP_FLAG_PSH;

    /* Append answer in DNS message */
    int dns_abs_offset = (int)((uint8_t *)dns - pkt);
    uint8_t answer_buf[DNS_ANSWER_AAAA_LEN];
    uint8_t wg_ipv6[] = WALLED_GARDEN_IPV6;
    int written = build_dns_answer(answer_buf, qtype,
                                    htonl(WALLED_GARDEN_IPV4), wg_ipv6);
    memcpy(pkt + dns_abs_offset + question_end, answer_buf, written);

    /* Update DNS header */
    uint16_t flags = ntohs(dns->flags);
    flags |= (DNS_FLAG_QR | DNS_FLAG_RA);
    dns->flags   = htons(flags);
    dns->ancount = htons(1);

    /* Update DNS TCP length prefix */
    uint16_t new_dns_msg_len = dns_msg_len + (uint16_t)answer_len;
    write_u16_be(tcp_payload, new_dns_msg_len);

    /* Update IPv4 total_len */
    ip4->total_len = htons(ntohs(ip4->total_len) + (uint16_t)answer_len);
    ip4->checksum  = 0;

    /* TCP checksum: set 0 (or use hardware offload in DPDK) */
    tcp->checksum = 0;

    return new_pkt_len;
}

/* ───────────────────────────────────────────────────────────
 * Verification helpers
 * ─────────────────────────────────────────────────────────── */
static void print_ipv4(uint32_t ip_be)
{
    uint32_t ip = ntohl(ip_be);
    printf("%u.%u.%u.%u",
           (ip>>24)&0xFF, (ip>>16)&0xFF, (ip>>8)&0xFF, ip&0xFF);
}

static void verify_sinkhole_response(const uint8_t *pkt, int pkt_len,
                                      int is_ipv6, int is_tcp, int tcp_hdr_len)
{
    int l3_off = ETH_HDR_LEN;
    int l4_off = l3_off + (is_ipv6 ? IPV6_HDR_LEN : IPV4_HDR_MIN);
    int dns_off;

    if (is_tcp)
        dns_off = l4_off + tcp_hdr_len + DNS_TCP_LEN_PREFIX;
    else
        dns_off = l4_off + UDP_HDR_LEN;

    if (pkt_len < dns_off + (int)DNS_HDR_LEN) {
        printf("    Packet too short\n");
        return;
    }

    const dns_hdr_t *dns = (const dns_hdr_t *)(pkt + dns_off);
    uint16_t flags = ntohs(dns->flags);

    printf("    QR=%d  (1=response)  ", (flags & DNS_FLAG_QR) ? 1 : 0);
    printf("RA=%d  RCODE=%u\n",
           (flags & DNS_FLAG_RA) ? 1 : 0, flags & DNS_RCODE_MASK);
    printf("    qdcount=%u  ancount=%u\n",
           ntohs(dns->qdcount), ntohs(dns->ancount));

    /* Parse answer section — it starts after the question */
    /* Simplified: just check the pointer and type */
    const uint8_t *answer = pkt + dns_off;  /* start of DNS message */
    /* Walk past header + question to find answer */
    int q_off = DNS_HDR_LEN;
    /* skip qname */
    while (q_off < pkt_len - dns_off && answer[q_off] != 0) {
        uint8_t len = answer[q_off];
        if ((len & 0xC0) == 0xC0) { q_off += 2; break; }
        q_off += 1 + len;
    }
    if (answer[q_off] != 0) {
        /* pointer compression already handled */
    } else {
        q_off++;  /* null label */
    }
    q_off += 4;  /* qtype + qclass */

    const uint8_t *ans_sec = answer + q_off;
    if (ans_sec + 12 > pkt + pkt_len) {
        printf("    Answer section truncated\n");
        return;
    }

    /* Name pointer */
    uint16_t name_ptr = read_u16_be(ans_sec);
    uint16_t rr_type  = read_u16_be(ans_sec + 2);
    uint32_t ttl      = read_u32_be(ans_sec + 6);
    uint16_t rdlen    = read_u16_be(ans_sec + 10);

    printf("    Answer RR: name_ptr=0x%04x  type=%u (%s)  "
           "ttl=%u  rdlen=%u\n",
           name_ptr, rr_type,
           rr_type == DNS_TYPE_A ? "A" : rr_type == DNS_TYPE_AAAA ? "AAAA" : "?",
           ttl, rdlen);

    if (rr_type == DNS_TYPE_A && rdlen == 4) {
        uint32_t rdata = read_u32_be(ans_sec + 12);
        printf("    RDATA (A): ");
        print_ipv4(htonl(rdata));
        printf("\n");
        assert(rdata == WALLED_GARDEN_IPV4);
    } else if (rr_type == DNS_TYPE_AAAA && rdlen == 16) {
        char ipv6_str[INET6_ADDRSTRLEN];
        inet_ntop(AF_INET6, ans_sec + 12, ipv6_str, sizeof(ipv6_str));
        printf("    RDATA (AAAA): %s\n", ipv6_str);
    }
}

/* ═══════════════════════════════════════════════════════════
 * Tests
 * ═══════════════════════════════════════════════════════════ */

/* ─── Test 1: UDP/IPv4, A query ───────────────────────────── */
static void test_udp_ipv4_a(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Test 1: Sinkhole UDP/IPv4 A query\n");
    printf("══════════════════════════════════════════════\n\n");

    /*
     * Original query: client 198.51.100.5:54321 → 8.8.8.8:53
     * DNS: A query for "blocked.example.com"
     *
     * After sinkhole:
     *   8.8.8.8:53 → 198.51.100.5:54321
     *   DNS response: A record pointing to 10.1.1.1
     */
    static uint8_t pkt[MAX_PKT_BUF] = {
        /* Ethernet */
        0x00,0x01,0x02,0x03,0x04,0x05,    /* dst MAC */
        0xAA,0xBB,0xCC,0xDD,0xEE,0xFF,    /* src MAC */
        0x08,0x00,                          /* IPv4 */
        /* IPv4: src=198.51.100.5, dst=8.8.8.8 */
        0x45,0x00,
        0x00,0x4f,                          /* total_len = 79 */
        0x00,0x01,0x00,0x00,
        0x40,0x11,0x00,0x00,               /* TTL=64, UDP */
        0xC0,0xA8,0x01,0x64,               /* src: 198.51.100.5 */
        0x08,0x08,0x08,0x08,               /* dst: 8.8.8.8 */
        /* UDP: src=54321, dst=53 */
        0xD4,0x31, 0x00,0x35,
        0x00,0x3b, 0x00,0x00,              /* dgram_len=59, cksum=0 */
        /* DNS header */
        0xCA,0xFE,                          /* ID */
        0x01,0x00,                          /* flags: RD=1 */
        0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,
        /* DNS question: blocked.example.com A IN */
        0x07,'b','l','o','c','k','e','d',
        0x07,'e','x','a','m','p','l','e',
        0x03,'c','o','m',0x00,
        0x00,0x01,                          /* QTYPE: A */
        0x00,0x01,                          /* QCLASS: IN */
    };
    int pkt_len = ETH_HDR_LEN + IPV4_HDR_MIN + UDP_HDR_LEN + DNS_HDR_LEN + 27;
    /* question_end: DNS_HDR_LEN(12) + qname(21) + qtype+qclass(4) = 37 */
    int question_end = 37;

    printf("  Before: src=198.51.100.5:54321 → dst=8.8.8.8:53\n");
    printf("  pkt_len=%d  question_end=%d\n\n", pkt_len, question_end);

    int new_len = dns_sinkhole_udp_ipv4(pkt, pkt_len, MAX_PKT_BUF,
                                          DNS_TYPE_A, question_end);
    assert(new_len == pkt_len + DNS_ANSWER_A_LEN);

    ipv4_hdr_t *ip4 = (ipv4_hdr_t *)(pkt + ETH_HDR_LEN);
    udp_hdr_t  *udp = (udp_hdr_t *) (pkt + ETH_HDR_LEN + IPV4_HDR_MIN);

    printf("  After:\n");
    printf("    src="); print_ipv4(ip4->src_ip);
    printf(":%u", ntohs(udp->src_port));
    printf(" → dst="); print_ipv4(ip4->dst_ip);
    printf(":%u\n", ntohs(udp->dst_port));
    printf("    new pkt_len=%d (+%d bytes for A answer)\n\n",
           new_len, DNS_ANSWER_A_LEN);

    /* Verify src/dst swap */
    assert(ntohl(ip4->src_ip) == 0x08080808);   /* was dst, now src */
    assert(ntohl(ip4->dst_ip) == 0xC0A80164);   /* was src, now dst */
    assert(ntohs(udp->src_port) == 53);
    assert(ntohs(udp->dst_port) == 54321);

    verify_sinkhole_response(pkt, new_len, 0, 0, 0);
    printf("\n  PASS ✓\n\n");
}

/* ─── Test 2: UDP/IPv4, AAAA query ─────────────────────────── */
static void test_udp_ipv4_aaaa(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Test 2: Sinkhole UDP/IPv4 AAAA query\n");
    printf("══════════════════════════════════════════════\n\n");

    /* Same packet structure as test 1, but QTYPE=AAAA */
    static uint8_t pkt[MAX_PKT_BUF] = {
        /* Ethernet */
        0x00,0x01,0x02,0x03,0x04,0x05,
        0xAA,0xBB,0xCC,0xDD,0xEE,0xFF,
        0x08,0x00,
        /* IPv4 */
        0x45,0x00, 0x00,0x4f,
        0x00,0x01,0x00,0x00, 0x40,0x11,0x00,0x00,
        0xC0,0xA8,0x01,0x64,
        0x08,0x08,0x08,0x08,
        /* UDP */
        0xD4,0x31, 0x00,0x35, 0x00,0x3b,0x00,0x00,
        /* DNS */
        0xBE,0xEF, 0x01,0x00,
        0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,
        /* Question: blocked.example.com AAAA IN */
        0x07,'b','l','o','c','k','e','d',
        0x07,'e','x','a','m','p','l','e',
        0x03,'c','o','m',0x00,
        0x00,0x1c,   /* QTYPE: AAAA */
        0x00,0x01,
    };
    int pkt_len      = ETH_HDR_LEN + IPV4_HDR_MIN + UDP_HDR_LEN + DNS_HDR_LEN + 27;
    int question_end = 37;

    int new_len = dns_sinkhole_udp_ipv4(pkt, pkt_len, MAX_PKT_BUF,
                                          DNS_TYPE_AAAA, question_end);
    assert(new_len == pkt_len + DNS_ANSWER_AAAA_LEN);

    printf("  AAAA answer section: %d bytes (+%d over A)\n\n",
           DNS_ANSWER_AAAA_LEN, DNS_ANSWER_AAAA_LEN - DNS_ANSWER_A_LEN);
    verify_sinkhole_response(pkt, new_len, 0, 0, 0);
    printf("\n  PASS ✓\n\n");
}

/* ─── Test 3: UDP/IPv6, AAAA query ─────────────────────────── */
static void test_udp_ipv6_aaaa(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Test 3: Sinkhole UDP/IPv6 AAAA query\n");
    printf("══════════════════════════════════════════════\n\n");

    static uint8_t pkt[MAX_PKT_BUF] = {
        /* Ethernet */
        0x33,0x33,0x00,0x00,0x00,0x01,
        0xAA,0xBB,0xCC,0xDD,0xEE,0xFF,
        0x86,0xDD,                          /* IPv6 */
        /* IPv6: src=2001:db8::100, dst=2001:db8::53 */
        0x60,0x00,0x00,0x00,
        0x00,0x33,                          /* payload_len=51 */
        0x11, 0x40,                          /* next=UDP, hop=64 */
        0x20,0x01,0x0d,0xb8,0x00,0x00,0x00,0x00,
        0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x00,  /* src */
        0x20,0x01,0x0d,0xb8,0x00,0x00,0x00,0x00,
        0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x35,  /* dst */
        /* UDP */
        0xC0,0x01, 0x00,0x35, 0x00,0x33,0x00,0x00,
        /* DNS */
        0xDE,0xAD, 0x01,0x00,
        0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,
        /* Question: secure.corp AAAA IN */
        0x06,'s','e','c','u','r','e',
        0x04,'c','o','r','p',0x00,
        0x00,0x1c, 0x00,0x01,
    };
    int pkt_len      = ETH_HDR_LEN + IPV6_HDR_LEN + UDP_HDR_LEN + DNS_HDR_LEN + 19;
    int question_end = DNS_HDR_LEN + 19;

    int new_len = dns_sinkhole_udp_ipv6(pkt, pkt_len, MAX_PKT_BUF,
                                          DNS_TYPE_AAAA, question_end);
    assert(new_len == pkt_len + DNS_ANSWER_AAAA_LEN);

    verify_sinkhole_response(pkt, new_len, 1, 0, 0);
    printf("\n  PASS ✓\n\n");
}

/* ─── Test 4: TCP/IPv4, A query ─────────────────────────────── */
static void test_tcp_ipv4_a(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Test 4: Sinkhole TCP/IPv4 A query\n");
    printf("══════════════════════════════════════════════\n\n");

    static uint8_t pkt[MAX_PKT_BUF] = {
        /* Ethernet */
        0x00,0x01,0x02,0x03,0x04,0x05,
        0xAA,0xBB,0xCC,0xDD,0xEE,0xFF,
        0x08,0x00,
        /* IPv4 */
        0x45,0x00, 0x00,0x59,              /* total_len=89 */
        0x00,0x02,0x40,0x00, 0x40,0x06,0x00,0x00,
        0xC0,0xA8,0x01,0x64,
        0x08,0x08,0x08,0x08,
        /* TCP: src=12345, dst=53, data_off=5 (20 byte header) */
        0x30,0x39, 0x00,0x35,
        0x00,0x00,0x00,0x01,               /* seq */
        0x00,0x00,0x00,0x00,               /* ack */
        0x50,                               /* data_offset=5 */
        TCP_FLAG_PSH|TCP_FLAG_ACK,
        0xFF,0xFF, 0x00,0x00, 0x00,0x00,   /* window, cksum, urgptr */
        /* DNS TCP length prefix (2 bytes) + DNS message */
        0x00,0x29,                          /* DNS msg length = 41 */
        /* DNS header */
        0x11,0x11, 0x01,0x00,
        0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,
        /* Question: ads.example.com A IN */
        0x03,'a','d','s',
        0x07,'e','x','a','m','p','l','e',
        0x03,'c','o','m',0x00,
        0x00,0x01, 0x00,0x01,
    };
    int pkt_len      = ETH_HDR_LEN + IPV4_HDR_MIN + 20 + DNS_TCP_LEN_PREFIX + DNS_HDR_LEN + 21;
    int question_end = DNS_HDR_LEN + 21;
    int tcp_hdr_len  = 20;

    printf("  Before: TCP DNS query (with 2-byte length prefix)\n");
    printf("  DNS TCP length prefix = 0x0029 (%d bytes)\n\n",
           0x29);

    int new_len = dns_sinkhole_tcp_ipv4(pkt, pkt_len, MAX_PKT_BUF,
                                         DNS_TYPE_A, question_end, tcp_hdr_len);
    assert(new_len == pkt_len + DNS_ANSWER_A_LEN);

    /* Verify the TCP length prefix was updated */
    int tcp_payload_off = ETH_HDR_LEN + IPV4_HDR_MIN + tcp_hdr_len;
    uint16_t new_dns_len = read_u16_be(pkt + tcp_payload_off);
    printf("  Updated DNS TCP length prefix = %u (was 41, +%d = %u)\n\n",
           new_dns_len, DNS_ANSWER_A_LEN, 41 + DNS_ANSWER_A_LEN);
    assert(new_dns_len == 41 + DNS_ANSWER_A_LEN);

    verify_sinkhole_response(pkt, new_len, 0, 1, tcp_hdr_len);
    printf("\n  PASS ✓\n\n");
}

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    printf("=== Module 18: DNS Sinkhole ===\n\n");
    printf("Walled garden IPv4: 10.1.1.1 (0x%08X)\n", WALLED_GARDEN_IPV4);
    printf("Sinkhole TTL: %d seconds\n\n", DNS_SINKHOLE_TTL);

    test_udp_ipv4_a();
    test_udp_ipv4_aaaa();
    test_udp_ipv6_aaaa();
    test_tcp_ipv4_a();

    printf("=== All tests passed ===\n\n");
    printf("In-place rewrite steps:\n");
    printf("  1. Swap ETH src ↔ dst (memcpy via tmp)\n");
    printf("  2. Swap IP  src ↔ dst (uint32/uint8[16])\n");
    printf("  3. Swap UDP src ↔ dst port\n");
    printf("  4. Set DNS QR=1, ancount=1\n");
    printf("  5. Append answer: 0xC00C | type | IN | TTL=60 | rdlen | IP\n");
    printf("  6. Update UDP dgram_len / IPv4 total_len / TCP dns_len\n");
    printf("  7. (DPDK) m->ol_flags |= TX_IPV4|TX_IP_CKSUM|TX_UDP_CKSUM\n\n");
    printf("DPDK equivalent of step 5:\n");
    printf("  char *ans = rte_pktmbuf_append(mbuf, answer_len);\n");
    printf("  memcpy(ans, answer_buf, answer_len);\n");
    printf("  /* mbuf data_len + pkt_len updated automatically */\n");
    return 0;
}
