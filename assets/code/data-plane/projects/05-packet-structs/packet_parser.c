/**
 * packet_parser.c — Module 05: Network Packet Header Parsing
 *
 * Demonstrates parsing raw packet bytes layer by layer:
 *   Ethernet → IPv4/IPv6 → UDP/TCP → DNS
 *
 * This is exactly what happens at the entry point of the DP application
 * packet processing pipeline in pkt_proc.h. Every packet received
 * via rte_eth_rx_burst() goes through this same sequence of header
 * pointer calculations before any policy decision is made.
 *
 * Key insight: "parsing" a packet in a dataplane means casting a pointer
 * to a struct — not copying data. The packet stays in the mbuf, we just
 * overlay our struct definition on top of the bytes.
 *
 *   uint8_t *pkt = rte_pktmbuf_mtod(mbuf, uint8_t *);
 *   eth_hdr_t  *eth = (eth_hdr_t *)pkt;
 *   ipv4_hdr_t *ip4 = (ipv4_hdr_t *)(pkt + ETH_HDR_LEN);
 *   udp_hdr_t  *udp = (udp_hdr_t *)((uint8_t *)ip4 + IPV4_IHL_BYTES(ip4));
 */

#include "packet_structs.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <assert.h>

/* ───────────────────────────────────────────────────────────
 * Utility: hex dump (used to show raw bytes alongside parsed output)
 * ─────────────────────────────────────────────────────────── */
void print_hex_dump(const uint8_t *buf, int len)
{
    int i;
    for (i = 0; i < len; i++) {
        if (i % 16 == 0) printf("\n  %04x: ", i);
        printf("%02x ", buf[i]);
        if (i % 16 == 7) printf(" ");
    }
    printf("\n");
}

/* ───────────────────────────────────────────────────────────
 * MAC address to "xx:xx:xx:xx:xx:xx" string
 * ─────────────────────────────────────────────────────────── */
static void mac_to_str(const uint8_t *mac, char *buf, int len)
{
    snprintf(buf, len, "%02x:%02x:%02x:%02x:%02x:%02x",
             mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
}

/* ───────────────────────────────────────────────────────────
 * IPv4 address to "a.b.c.d" string
 * ip is in network byte order (big-endian)
 * ─────────────────────────────────────────────────────────── */
static void ipv4_to_str(uint32_t ip_be, char *buf, int len)
{
    uint32_t ip = ntohl(ip_be);
    snprintf(buf, len, "%u.%u.%u.%u",
             (ip >> 24) & 0xFF, (ip >> 16) & 0xFF,
             (ip >>  8) & 0xFF,  ip        & 0xFF);
}

/* ───────────────────────────────────────────────────────────
 * IPv6 address to compressed colon-hex string
 * ─────────────────────────────────────────────────────────── */
static void ipv6_to_str(const uint8_t *addr, char *buf, int len)
{
    inet_ntop(AF_INET6, addr, buf, len);
}

/* ───────────────────────────────────────────────────────────
 * Pretty-print functions
 * ─────────────────────────────────────────────────────────── */

void print_eth_hdr(const eth_hdr_t *hdr)
{
    char src[18], dst[18];
    mac_to_str(hdr->src_mac, src, sizeof(src));
    mac_to_str(hdr->dst_mac, dst, sizeof(dst));

    printf("[Ethernet]\n");
    printf("  dst_mac    : %s\n", dst);
    printf("  src_mac    : %s\n", src);
    printf("  ether_type : 0x%04x", ntohs(hdr->ether_type));

    switch (ntohs(hdr->ether_type)) {
    case ETHER_TYPE_IPV4: printf("  (IPv4)\n");   break;
    case ETHER_TYPE_IPV6: printf("  (IPv6)\n");   break;
    case ETHER_TYPE_ARP:  printf("  (ARP)\n");    break;
    case ETHER_TYPE_VLAN: printf("  (VLAN 802.1Q)\n"); break;
    default:              printf("  (unknown)\n"); break;
    }
}

void print_ipv4_hdr(const ipv4_hdr_t *hdr)
{
    char src[16], dst[16];
    ipv4_to_str(hdr->src_ip, src, sizeof(src));
    ipv4_to_str(hdr->dst_ip, dst, sizeof(dst));

    printf("[IPv4]\n");
    printf("  version    : %u\n",  (hdr->version_ihl >> 4) & 0xF);
    printf("  IHL        : %u bytes\n", IPV4_IHL_BYTES(hdr));
    printf("  total_len  : %u\n",  ntohs(hdr->total_len));
    printf("  TTL        : %u\n",  hdr->ttl);
    printf("  protocol   : %u",    hdr->proto);
    switch (hdr->proto) {
    case IP_PROTO_TCP:  printf("  (TCP)\n");  break;
    case IP_PROTO_UDP:  printf("  (UDP)\n");  break;
    case IP_PROTO_ICMP: printf("  (ICMP)\n"); break;
    default:            printf("\n");         break;
    }
    printf("  src_ip     : %s\n", src);
    printf("  dst_ip     : %s\n", dst);
}

void print_ipv6_hdr(const ipv6_hdr_t *hdr)
{
    char src[INET6_ADDRSTRLEN], dst[INET6_ADDRSTRLEN];
    ipv6_to_str(hdr->src_ip, src, sizeof(src));
    ipv6_to_str(hdr->dst_ip, dst, sizeof(dst));

    printf("[IPv6]\n");
    printf("  version    : %u\n", (ntohl(hdr->vtc_flow) >> 28) & 0xF);
    printf("  payload_len: %u\n", ntohs(hdr->payload_len));
    printf("  next_hdr   : %u", hdr->proto);
    switch (hdr->proto) {
    case IP_PROTO_TCP:    printf("  (TCP)\n");    break;
    case IP_PROTO_UDP:    printf("  (UDP)\n");    break;
    case IP_PROTO_ICMPV6: printf("  (ICMPv6)\n"); break;
    default:              printf("\n");            break;
    }
    printf("  hop_limit  : %u\n", hdr->hop_limit);
    printf("  src_ip     : %s\n", src);
    printf("  dst_ip     : %s\n", dst);
}

void print_udp_hdr(const udp_hdr_t *hdr)
{
    printf("[UDP]\n");
    printf("  src_port   : %u\n", ntohs(hdr->src_port));
    printf("  dst_port   : %u",   ntohs(hdr->dst_port));
    if (ntohs(hdr->dst_port) == PORT_DNS ||
        ntohs(hdr->src_port) == PORT_DNS)
        printf("  (DNS)\n");
    else
        printf("\n");
    printf("  length     : %u\n", ntohs(hdr->dgram_len));
}

void print_tcp_hdr(const tcp_hdr_t *hdr)
{
    printf("[TCP]\n");
    printf("  src_port   : %u\n",  ntohs(hdr->src_port));
    printf("  dst_port   : %u",    ntohs(hdr->dst_port));
    if (ntohs(hdr->dst_port) == PORT_HTTPS ||
        ntohs(hdr->src_port) == PORT_HTTPS)
        printf("  (HTTPS/TLS)\n");
    else if (ntohs(hdr->dst_port) == PORT_HTTP ||
             ntohs(hdr->src_port) == PORT_HTTP)
        printf("  (HTTP)\n");
    else
        printf("\n");
    printf("  seq_num    : 0x%08x\n", ntohl(hdr->seq_num));
    printf("  ack_num    : 0x%08x\n", ntohl(hdr->ack_num));
    printf("  hdr_len    : %u bytes\n", TCP_HDR_LEN(hdr));
    printf("  flags      : 0x%02x [", hdr->flags);
    if (hdr->flags & TCP_FLAG_SYN) printf("SYN ");
    if (hdr->flags & TCP_FLAG_ACK) printf("ACK ");
    if (hdr->flags & TCP_FLAG_FIN) printf("FIN ");
    if (hdr->flags & TCP_FLAG_RST) printf("RST ");
    if (hdr->flags & TCP_FLAG_PSH) printf("PSH ");
    printf("]\n");
    printf("  window     : %u\n", ntohs(hdr->window));
}

void print_dns_hdr(const dns_hdr_t *hdr)
{
    uint16_t flags = ntohs(hdr->flags);
    printf("[DNS]\n");
    printf("  id         : 0x%04x\n", ntohs(hdr->id));
    printf("  type       : %s\n", (flags & DNS_FLAG_QR) ? "RESPONSE" : "QUERY");
    printf("  RD         : %s\n", (flags & DNS_FLAG_RD) ? "yes" : "no");
    printf("  RA         : %s\n", (flags & DNS_FLAG_RA) ? "yes" : "no");
    printf("  rcode      : %u\n", flags & DNS_RCODE_MASK);
    printf("  questions  : %u\n", ntohs(hdr->qdcount));
    printf("  answers    : %u\n", ntohs(hdr->ancount));
}

/* ───────────────────────────────────────────────────────────
 * dns_parse_qname — decode DNS wire-format label encoding
 *
 * DNS names are encoded as length-prefixed labels:
 *   "www.example.com" → 03 77 77 77  07 65 78 61 6d 70 6c 65  03 63 6f 6d  00
 *                        3  w  w  w   7  e  x  a  m  p  l  e   3  c  o  m  (end)
 *
 * This is the first thing parsed in the DNS payload after the 12-byte header.
 * The real app's parse_dns_ipv4_request_packet_over_udp() does this same walk.
 *
 * Returns the number of wire bytes consumed, or -1 on error.
 * ─────────────────────────────────────────────────────────── */
int dns_parse_qname(const uint8_t *wire, int wire_len,
                    int offset, char *out, int out_len)
{
    int  out_pos  = 0;
    int  start    = offset;
    int  jumped   = 0;
    int  jump_ret = -1;

    while (offset < wire_len) {
        uint8_t label_len = wire[offset];

        /* End of name */
        if (label_len == 0) {
            if (out_pos > 0) out[out_pos - 1] = '\0';  /* overwrite last '.' */
            else out[0] = '\0';
            return jumped ? jump_ret : offset - start + 1;
        }

        /* DNS pointer compression: top 2 bits set = pointer to elsewhere */
        if ((label_len & 0xC0) == 0xC0) {
            if (offset + 1 >= wire_len) return -1;
            int ptr = ((label_len & 0x3F) << 8) | wire[offset + 1];
            if (!jumped) jump_ret = offset - start + 2;
            jumped = 1;
            offset = ptr;
            continue;
        }

        /* Regular label */
        offset++;
        if (offset + label_len > wire_len) return -1;
        if (out_pos + label_len + 1 >= out_len) return -1;

        memcpy(out + out_pos, wire + offset, label_len);
        out_pos += label_len;
        out[out_pos++] = '.';
        offset += label_len;
    }
    return -1;
}

/* ───────────────────────────────────────────────────────────
 * Layer-by-layer packet parser
 *
 * In the real DP application this is spread across multiple functions
 * in pkt_proc.h. The pointer arithmetic is identical — we just
 * don't have an rte_mbuf here.
 * ─────────────────────────────────────────────────────────── */
static void parse_and_print_packet(const char *label,
                                    const uint8_t *pkt, int pkt_len)
{
    int offset = 0;

    printf("\n══════════════════════════════════════════\n");
    printf("Packet: %s  (%d bytes)\n", label, pkt_len);
    printf("══════════════════════════════════════════\n");

    printf("\nHex dump:");
    print_hex_dump(pkt, pkt_len);
    printf("\n");

    /* ── Layer 2: Ethernet ── */
    if (pkt_len < ETH_HDR_LEN) { printf("Packet too short for Ethernet\n"); return; }
    const eth_hdr_t *eth = (const eth_hdr_t *)pkt;
    print_eth_hdr(eth);
    offset += ETH_HDR_LEN;

    uint16_t eth_type = ntohs(eth->ether_type);

    /* Handle 802.1Q VLAN tag */
    if (eth_type == ETHER_TYPE_VLAN) {
        if (pkt_len < offset + VLAN_HDR_LEN) return;
        const vlan_hdr_t *vlan = (const vlan_hdr_t *)(pkt + offset);
        printf("[VLAN] vid=%u  inner_type=0x%04x\n",
               ntohs(vlan->tci) & 0x0FFF, ntohs(vlan->ether_type));
        eth_type = ntohs(vlan->ether_type);
        offset  += VLAN_HDR_LEN;
    }

    /* ── Layer 3: IP ── */
    uint8_t l4_proto = 0;
    int     l4_offset = 0;

    if (eth_type == ETHER_TYPE_IPV4) {
        if (pkt_len < offset + IPV4_HDR_MIN) return;
        const ipv4_hdr_t *ip4 = (const ipv4_hdr_t *)(pkt + offset);
        print_ipv4_hdr(ip4);
        l4_proto  = ip4->proto;
        l4_offset = offset + IPV4_IHL_BYTES(ip4);
        offset    = l4_offset;

    } else if (eth_type == ETHER_TYPE_IPV6) {
        if (pkt_len < offset + IPV6_HDR_LEN) return;
        const ipv6_hdr_t *ip6 = (const ipv6_hdr_t *)(pkt + offset);
        print_ipv6_hdr(ip6);
        l4_proto  = ip6->proto;
        l4_offset = offset + IPV6_HDR_LEN;
        offset    = l4_offset;

    } else {
        printf("Not an IP packet (ether_type=0x%04x)\n", eth_type);
        return;
    }

    /* ── Layer 4: UDP or TCP ── */
    if (l4_proto == IP_PROTO_UDP) {
        if (pkt_len < offset + UDP_HDR_LEN) return;
        const udp_hdr_t *udp = (const udp_hdr_t *)(pkt + offset);
        print_udp_hdr(udp);

        /* ── Application layer: DNS over UDP ── */
        int dns_offset = offset + UDP_HDR_LEN;
        if (ntohs(udp->dst_port) == PORT_DNS ||
            ntohs(udp->src_port) == PORT_DNS) {

            if (pkt_len < dns_offset + DNS_HDR_LEN) return;
            const dns_hdr_t *dns = (const dns_hdr_t *)(pkt + dns_offset);
            print_dns_hdr(dns);

            /* Parse question section */
            if (ntohs(dns->qdcount) > 0) {
                char qname[256];
                int qname_offset = dns_offset + DNS_HDR_LEN;
                int consumed = dns_parse_qname(pkt, pkt_len,
                                               qname_offset, qname, sizeof(qname));
                if (consumed > 0) {
                    int type_off = qname_offset + consumed;
                    uint16_t qtype  = read_u16_be(pkt + type_off);
                    uint16_t qclass = read_u16_be(pkt + type_off + 2);
                    printf("[DNS Question]\n");
                    printf("  qname      : %s\n", qname);
                    printf("  qtype      : %u (%s)\n", qtype,
                           qtype == DNS_TYPE_A    ? "A"    :
                           qtype == DNS_TYPE_AAAA ? "AAAA" :
                           qtype == DNS_TYPE_CNAME? "CNAME": "other");
                    printf("  qclass     : %u (%s)\n", qclass,
                           qclass == DNS_CLASS_IN ? "IN" : "other");
                }
            }
        }

    } else if (l4_proto == IP_PROTO_TCP) {
        if (pkt_len < offset + TCP_HDR_MIN) return;
        const tcp_hdr_t *tcp = (const tcp_hdr_t *)(pkt + offset);
        print_tcp_hdr(tcp);

        /* Show payload length */
        int tcp_payload_off = offset + TCP_HDR_LEN(tcp);
        int tcp_payload_len = pkt_len - tcp_payload_off;
        if (tcp_payload_len > 0)
            printf("[TCP Payload] %d bytes (Module 07 parses TLS SNI here)\n",
                   tcp_payload_len);
        else
            printf("[TCP Payload] 0 bytes (SYN/ACK handshake packet)\n");
    }
}

/* ─── Sample packets ─────────────────────────────────────── */

/*
 * Sample 1: DNS A query over UDP/IPv4 for "www.example.com"
 * src: 198.51.100.5:12345  dst: 8.8.8.8:53
 */
static const uint8_t dns_query_ipv4[] = {
    /* Ethernet */
    0xff,0xff,0xff,0xff,0xff,0xff,          /* dst MAC */
    0x00,0x11,0x22,0x33,0x44,0x55,          /* src MAC */
    0x08,0x00,                               /* EtherType: IPv4 */
    /* IPv4 */
    0x45,0x00,0x00,0x3d,                     /* version/IHL, DSCP, total_len=61 */
    0xab,0xcd,0x00,0x00,                     /* id, flags+frag */
    0x40,0x11,0x00,0x00,                     /* TTL=64, proto=UDP, cksum */
    0xc6,0x33,0x64,0x05,                     /* src: 198.51.100.5 */
    0x08,0x08,0x08,0x08,                     /* dst: 8.8.8.8 */
    /* UDP */
    0x30,0x39,                               /* src_port: 12345 */
    0x00,0x35,                               /* dst_port: 53 */
    0x00,0x29,0x00,0x00,                     /* length=41, checksum */
    /* DNS header */
    0x12,0x34,                               /* ID: 0x1234 */
    0x01,0x00,                               /* flags: RD=1 */
    0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00, /* qdcount=1 */
    /* DNS question: www.example.com A IN */
    0x03,0x77,0x77,0x77,                     /* 3 "www" */
    0x07,0x65,0x78,0x61,0x6d,0x70,0x6c,0x65,/* 7 "example" */
    0x03,0x63,0x6f,0x6d,0x00,               /* 3 "com" + root */
    0x00,0x01,                               /* QTYPE: A */
    0x00,0x01,                               /* QCLASS: IN */
};

/*
 * Sample 2: DNS AAAA query over UDP/IPv6 for "secure.corp.internal"
 * src: 2001:db8::1  dst: 2001:db8::53
 */
static const uint8_t dns_query_ipv6[] = {
    /* Ethernet */
    0x33,0x33,0x00,0x00,0x00,0x01,          /* dst MAC (IPv6 multicast) */
    0xaa,0xbb,0xcc,0xdd,0xee,0xff,          /* src MAC */
    0x86,0xdd,                               /* EtherType: IPv6 */
    /* IPv6 */
    0x60,0x00,0x00,0x00,                     /* version=6, TC=0, flow=0 */
    0x00,0x2e,                               /* payload_len=46 */
    0x11,                                    /* next_hdr: UDP */
    0x40,                                    /* hop_limit=64 */
    0x20,0x01,0x0d,0xb8,0x00,0x00,0x00,0x00,/* src: 2001:db8::1 */
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,
    0x20,0x01,0x0d,0xb8,0x00,0x00,0x00,0x00,/* dst: 2001:db8::53 */
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x35,
    /* UDP */
    0xc0,0x01,                               /* src_port: 49153 */
    0x00,0x35,                               /* dst_port: 53 */
    0x00,0x2e,0x00,0x00,                     /* length=46, checksum */
    /* DNS header */
    0xde,0xad,                               /* ID: 0xdead */
    0x01,0x00,                               /* flags: RD=1 */
    0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,/* qdcount=1 */
    /* DNS question: secure.corp.internal AAAA IN */
    0x06,0x73,0x65,0x63,0x75,0x72,0x65,     /* 6 "secure" */
    0x04,0x63,0x6f,0x72,0x70,               /* 4 "corp" */
    0x08,0x69,0x6e,0x74,0x65,0x72,0x6e,0x61,0x6c, /* 8 "internal" */
    0x00,                                    /* root */
    0x00,0x1c,                               /* QTYPE: AAAA (28) */
    0x00,0x01,                               /* QCLASS: IN */
};

/*
 * Sample 3: TCP SYN packet (HTTPS connection to 93.184.216.34:443)
 * This is the kind of packet that triggers TLS SNI extraction (Module 07)
 * once the handshake ClientHello arrives.
 */
static const uint8_t tcp_syn_ipv4[] = {
    /* Ethernet */
    0x00,0x50,0x56,0x01,0x02,0x03,          /* dst MAC */
    0x00,0x0c,0x29,0xaa,0xbb,0xcc,          /* src MAC */
    0x08,0x00,                               /* EtherType: IPv4 */
    /* IPv4 */
    0x45,0x00,0x00,0x3c,                     /* version/IHL, total_len=60 */
    0x12,0x34,0x40,0x00,                     /* id, DF flag set */
    0x40,0x06,0x00,0x00,                     /* TTL=64, proto=TCP, cksum */
    0xc6,0x33,0x64,0x0a,                     /* src: 198.51.100.10 */
    0x5d,0xb8,0xd8,0x22,                     /* dst: 93.184.216.34 */
    /* TCP: SYN to port 443 */
    0xd4,0x31,                               /* src_port: 54321 */
    0x01,0xbb,                               /* dst_port: 443 */
    0x00,0x00,0x00,0x01,                     /* seq_num */
    0x00,0x00,0x00,0x00,                     /* ack_num */
    0x60,                                    /* data_offset=6 (24 bytes hdr) */
    TCP_FLAG_SYN,                            /* flags: SYN */
    0xff,0xff,                               /* window */
    0x00,0x00,0x00,0x00,                     /* checksum, urgent_ptr */
    /* TCP options: MSS=1460 (4 bytes) */
    0x02,0x04,0x05,0xb4,
};

/* ─── Struct size verification ──────────────────────────── */
static void print_struct_sizes(void)
{
    printf("=== Module 05: Packet Structs ===\n\n");
    printf("--- Struct sizes (must match protocol spec) ---\n");
    printf("  eth_hdr_t  : %2zu bytes (expected 14)\n", sizeof(eth_hdr_t));
    printf("  vlan_hdr_t : %2zu bytes (expected  4)\n", sizeof(vlan_hdr_t));
    printf("  ipv4_hdr_t : %2zu bytes (expected 20)\n", sizeof(ipv4_hdr_t));
    printf("  ipv6_hdr_t : %2zu bytes (expected 40)\n", sizeof(ipv6_hdr_t));
    printf("  udp_hdr_t  : %2zu bytes (expected  8)\n", sizeof(udp_hdr_t));
    printf("  tcp_hdr_t  : %2zu bytes (expected 20)\n", sizeof(tcp_hdr_t));
    printf("  dns_hdr_t  : %2zu bytes (expected 12)\n", sizeof(dns_hdr_t));

    /* These asserts catch accidental removal of __attribute__((packed)) */
    assert(sizeof(eth_hdr_t)  == 14);
    assert(sizeof(vlan_hdr_t) ==  4);
    assert(sizeof(ipv4_hdr_t) == 20);
    assert(sizeof(ipv6_hdr_t) == 40);
    assert(sizeof(udp_hdr_t)  ==  8);
    assert(sizeof(tcp_hdr_t)  == 20);
    assert(sizeof(dns_hdr_t)  == 12);
    printf("  All sizes correct.\n");
}

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    print_struct_sizes();

    parse_and_print_packet("DNS A query (UDP/IPv4) — www.example.com",
                            dns_query_ipv4, sizeof(dns_query_ipv4));

    parse_and_print_packet("DNS AAAA query (UDP/IPv6) — secure.corp.internal",
                            dns_query_ipv6, sizeof(dns_query_ipv6));

    parse_and_print_packet("TCP SYN (IPv4) — HTTPS to 93.184.216.34:443",
                            tcp_syn_ipv4,   sizeof(tcp_syn_ipv4));

    printf("\n--- byte order demo ---\n");
    printf("Port 53 in network byte order : 0x%04x\n", htons(53));
    printf("Port 53 read raw from packet  : 0x%02x 0x%02x\n",
           dns_query_ipv4[36], dns_query_ipv4[37]);
    printf("ntohs(0x0035)                 : %u\n", ntohs(0x0035));
    printf("Checking port: ntohs(udp->dst_port) == 53  ← CORRECT\n");
    printf("Checking port: udp->dst_port == 53          ← WRONG! (compares to 0x3500 = 13568)\n");

    return 0;
}
