/**
 * packet_structs.h — Module 05: Network Packet Header Structures
 *
 * Every packet that enters the the DP application pipeline is parsed by overlaying
 * these structs onto raw packet bytes. In DPDK, the equivalent structs live
 * in rte_ether.h, rte_ip.h, rte_tcp.h, rte_udp.h. This module defines
 * the same structs without any DPDK dependency so you can compile and run
 * the parser on any Linux box.
 *
 * Critical rule: ALL multi-byte fields in network headers are BIG-ENDIAN.
 * x86 CPUs are little-endian. Always convert with ntohs() / ntohl() before
 * arithmetic, and htons() / htonl() before writing back into a packet.
 *
 * Forgetting this is one of the most common bugs in new dataplane code —
 * a port 53 check that tests (udp->dst_port == 53) instead of
 * (ntohs(udp->dst_port) == 53) silently passes for port 13568 (0x3500).
 *
 * In the real project, pkt_proc.h includes rte_ether.h / rte_ip.h
 * for these structs, plus a custom dns_hdr struct defined inline.
 */

#ifndef PACKET_STRUCTS_H
#define PACKET_STRUCTS_H

#include <stdint.h>
#include <string.h>
#include <arpa/inet.h>    /* ntohs, ntohl, htons, htonl */

/* ───────────────────────────────────────────────────────────
 * EtherType values (ether_hdr.ether_type, network byte order)
 * ─────────────────────────────────────────────────────────── */
#define ETHER_TYPE_IPV4   0x0800
#define ETHER_TYPE_IPV6   0x86DD
#define ETHER_TYPE_ARP    0x0806
#define ETHER_TYPE_VLAN   0x8100   /* 802.1Q VLAN tag */
#define ETHER_TYPE_QINQ   0x88A8   /* 802.1ad double tagging */

/* ───────────────────────────────────────────────────────────
 * IP protocol numbers (ipv4_hdr.proto / ipv6_hdr.proto)
 * ─────────────────────────────────────────────────────────── */
#define IP_PROTO_ICMP     1
#define IP_PROTO_TCP      6
#define IP_PROTO_UDP      17
#define IP_PROTO_ICMPV6   58

/* ───────────────────────────────────────────────────────────
 * TCP flag bits (tcp_hdr.flags)
 * ─────────────────────────────────────────────────────────── */
#define TCP_FLAG_FIN  0x01
#define TCP_FLAG_SYN  0x02
#define TCP_FLAG_RST  0x04
#define TCP_FLAG_PSH  0x08
#define TCP_FLAG_ACK  0x10
#define TCP_FLAG_URG  0x20

/* ───────────────────────────────────────────────────────────
 * DNS flag bits (dns_hdr.flags, network byte order)
 * ─────────────────────────────────────────────────────────── */
#define DNS_FLAG_QR       0x8000   /* 0=query 1=response */
#define DNS_FLAG_AA       0x0400   /* authoritative answer */
#define DNS_FLAG_TC       0x0200   /* truncated */
#define DNS_FLAG_RD       0x0100   /* recursion desired */
#define DNS_FLAG_RA       0x0080   /* recursion available */
#define DNS_OPCODE_QUERY  0x0000
#define DNS_RCODE_MASK    0x000F
#define DNS_RCODE_OK      0
#define DNS_RCODE_NXDOMAIN 3
#define DNS_RCODE_REFUSED 5

#define DNS_TYPE_A        1
#define DNS_TYPE_AAAA     28
#define DNS_TYPE_CNAME    5
#define DNS_TYPE_MX       15
#define DNS_CLASS_IN      1

/* ───────────────────────────────────────────────────────────
 * Well-known ports
 * ─────────────────────────────────────────────────────────── */
#define PORT_DNS    53
#define PORT_HTTP   80
#define PORT_HTTPS  443
#define PORT_DNS_TLS 853   /* DNS over TLS */

/* ───────────────────────────────────────────────────────────
 * Header size constants
 * ─────────────────────────────────────────────────────────── */
#define ETH_HDR_LEN    14
#define VLAN_HDR_LEN    4
#define IPV4_HDR_MIN   20
#define IPV6_HDR_LEN   40
#define UDP_HDR_LEN     8
#define TCP_HDR_MIN    20
#define DNS_HDR_LEN    12

/* Extract IPv4 header length in bytes from the IHL field */
#define IPV4_IHL_BYTES(hdr)   (((hdr)->version_ihl & 0x0F) << 2)

/* Extract TCP header length in bytes from the data_offset field */
#define TCP_HDR_LEN(hdr)      (((hdr)->data_offset >> 4) << 2)

/* ───────────────────────────────────────────────────────────
 * Ethernet header — 14 bytes
 *
 * __attribute__((packed)) prevents the compiler from inserting
 * padding bytes between fields to satisfy alignment constraints.
 * Without it, sizeof(eth_hdr_t) might be 16 instead of 14 and
 * the struct would not overlay correctly onto raw packet bytes.
 *
 * rte_ether.h equivalent: struct rte_ether_hdr
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    uint8_t  dst_mac[6];
    uint8_t  src_mac[6];
    uint16_t ether_type;    /* use ntohs() to compare; 0x0800=IPv4 */
} __attribute__((packed)) eth_hdr_t;

/* ───────────────────────────────────────────────────────────
 * 802.1Q VLAN tag — 4 bytes, follows eth_hdr when ether_type == 0x8100
 *
 * In enterprise environments all packets may be VLAN-tagged.
 * The real app checks for this in the initial parsing step and
 * adjusts the IP header pointer accordingly.
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    uint16_t tci;           /* tag control info: PCP(3) + DEI(1) + VID(12) */
    uint16_t ether_type;    /* inner ether type (e.g., 0x0800 for IPv4)     */
} __attribute__((packed)) vlan_hdr_t;

/* ───────────────────────────────────────────────────────────
 * IPv4 header — 20 bytes minimum (no options)
 *
 * rte_ip.h equivalent: struct rte_ipv4_hdr
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    uint8_t  version_ihl;   /* version(4b) | IHL(4b): IHL*4 = header bytes */
    uint8_t  tos;           /* type of service / DSCP + ECN                */
    uint16_t total_len;     /* total packet length including header         */
    uint16_t packet_id;     /* identification (for reassembly)              */
    uint16_t frag_offset;   /* flags(3b) | fragment offset(13b)             */
    uint8_t  ttl;           /* time to live; decremented at each hop        */
    uint8_t  proto;         /* next layer: IP_PROTO_TCP=6, IP_PROTO_UDP=17  */
    uint16_t checksum;
    uint32_t src_ip;        /* source address, big-endian                   */
    uint32_t dst_ip;        /* destination address, big-endian              */
} __attribute__((packed)) ipv4_hdr_t;

/* ───────────────────────────────────────────────────────────
 * IPv6 header — 40 bytes fixed (no options)
 *
 * rte_ip.h equivalent: struct rte_ipv6_hdr
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    uint32_t vtc_flow;      /* version(4b) | traffic class(8b) | flow(20b) */
    uint16_t payload_len;   /* length after this header (not including it)  */
    uint8_t  proto;         /* next header (same values as IPv4 proto)      */
    uint8_t  hop_limit;     /* equivalent of IPv4 TTL                       */
    uint8_t  src_ip[16];    /* 128-bit source address                       */
    uint8_t  dst_ip[16];    /* 128-bit destination address                  */
} __attribute__((packed)) ipv6_hdr_t;

/* ───────────────────────────────────────────────────────────
 * UDP header — 8 bytes
 *
 * rte_udp.h equivalent: struct rte_udp_hdr
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    uint16_t src_port;
    uint16_t dst_port;
    uint16_t dgram_len;     /* UDP header + payload length                  */
    uint16_t checksum;
} __attribute__((packed)) udp_hdr_t;

/* ───────────────────────────────────────────────────────────
 * TCP header — 20 bytes minimum
 *
 * rte_tcp.h equivalent: struct rte_tcp_hdr
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    uint16_t src_port;
    uint16_t dst_port;
    uint32_t seq_num;       /* sequence number                              */
    uint32_t ack_num;       /* acknowledgement number                       */
    uint8_t  data_offset;   /* upper 4 bits: header length in 32-bit words  */
    uint8_t  flags;         /* TCP_FLAG_SYN / ACK / FIN / RST / PSH        */
    uint16_t window;        /* receive window size                          */
    uint16_t checksum;
    uint16_t urgent_ptr;
} __attribute__((packed)) tcp_hdr_t;

/* ───────────────────────────────────────────────────────────
 * DNS header — 12 bytes
 *
 * Defined directly in pkt_proc.h in the real the DP application project.
 * Used for both DNS query parsing and DNS sinkhole response building
 * (Module 23).
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    uint16_t id;            /* transaction ID — echoed in the response      */
    uint16_t flags;         /* QR|OPCODE|AA|TC|RD|RA|Z|AD|CD|RCODE         */
    uint16_t qdcount;       /* number of questions                          */
    uint16_t ancount;       /* number of answer RRs                         */
    uint16_t nscount;       /* number of authority RRs                      */
    uint16_t arcount;       /* number of additional RRs                     */
} __attribute__((packed)) dns_hdr_t;

/* ───────────────────────────────────────────────────────────
 * Unaligned big-endian read helpers
 *
 * Packet bytes are NOT guaranteed to be naturally aligned. For example,
 * a uint16_t field inside the DNS payload might start at an odd address.
 * On x86 a misaligned read works silently, but on ARM it triggers a fault.
 * DPDK uses these helpers throughout. In pkt_proc.h read_u16_be is
 * defined for TLS SNI extraction (Module 07).
 * ─────────────────────────────────────────────────────────── */
static inline uint16_t read_u16_be(const uint8_t *p)
{
    return (uint16_t)((p[0] << 8) | p[1]);
}

static inline uint32_t read_u32_be(const uint8_t *p)
{
    return ((uint32_t)p[0] << 24) |
           ((uint32_t)p[1] << 16) |
           ((uint32_t)p[2] <<  8) |
            (uint32_t)p[3];
}

static inline void write_u16_be(uint8_t *p, uint16_t v)
{
    p[0] = (v >> 8) & 0xFF;
    p[1] =  v       & 0xFF;
}

static inline void write_u32_be(uint8_t *p, uint32_t v)
{
    p[0] = (v >> 24) & 0xFF;
    p[1] = (v >> 16) & 0xFF;
    p[2] = (v >>  8) & 0xFF;
    p[3] =  v        & 0xFF;
}

/* ─── Function declarations ──────────────────────────────── */

/* Parse a DNS qname from wire format (label encoding) into a dot-separated
 * string.  e.g., "\x03www\x07example\x03com\x00" → "www.example.com"
 * Returns number of bytes consumed from the wire, or -1 on error. */
int dns_parse_qname(const uint8_t *wire, int wire_len,
                    int offset, char *out, int out_len);

/* Pretty-print helpers */
void print_eth_hdr(const eth_hdr_t *hdr);
void print_ipv4_hdr(const ipv4_hdr_t *hdr);
void print_ipv6_hdr(const ipv6_hdr_t *hdr);
void print_udp_hdr(const udp_hdr_t *hdr);
void print_tcp_hdr(const tcp_hdr_t *hdr);
void print_dns_hdr(const dns_hdr_t *hdr);
void print_hex_dump(const uint8_t *buf, int len);

#endif /* PACKET_STRUCTS_H */
