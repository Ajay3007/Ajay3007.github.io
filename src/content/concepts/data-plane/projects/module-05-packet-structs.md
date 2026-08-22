---
title: "Module 05 — Packet Header Structs & Parser"
description: "Module 05 — Packet Header Structs & Parser What you learn How to define network packet header structs in C and parse raw bytes into them — layer by layer: Ethernet → IPv4/IPv6…"
domain: data-plane
track: dataplane-projects
order: 99
ownHeader: true
url: /learning/data-plane/projects/module-05-packet-structs/
---

# Module 05 — Packet Header Structs & Parser

## What you learn

How to define network packet header structs in C and parse raw bytes into
them — layer by layer: Ethernet → IPv4/IPv6 → UDP/TCP → DNS.

This is the entry point of every packet in the DP application pipeline. Before
any policy decision can be made, the packet headers must be parsed to
extract the source/destination IP, protocol, port, and ultimately the
domain name (DNS) or SNI (TLS).

---

## Where this fits in the real application

```text
rte_eth_rx_burst(port, queue, mbufs, BURST_SIZE)
  │
  │  mbuf → raw bytes
  │  pkt = rte_pktmbuf_mtod(mbuf, uint8_t *)
  │
  ├─► eth  = (eth_hdr_t *) pkt
  │
  ├─► ip4  = (ipv4_hdr_t *)(pkt + ETH_HDR_LEN)            [if IPv4]
  │   ip6  = (ipv6_hdr_t *)(pkt + ETH_HDR_LEN)            [if IPv6]
  │
  ├─► udp  = (udp_hdr_t *)((uint8_t *)ip4 + IPV4_IHL_BYTES(ip4))
  │   tcp  = (tcp_hdr_t *)((uint8_t *)ip4 + IPV4_IHL_BYTES(ip4))
  │
  ├─► DNS port 53 → dns_hdr + qname parsing    → Module 06
  │   TCP port 443 → TLS ClientHello parsing   → Module 07
  │
  └─► policy decision (Module 22)
```

---

## Files

| File | Purpose |
|---|---|
| `packet_structs.h` | All header structs, constants, inline helpers |
| `packet_parser.c` | Layer-by-layer parser + 3 sample packets + demo |
| `Makefile` | Build rules |

---

## Build and run

```bash
make
./packet_parser
```

Expected output (abbreviated):
```
=== Module 05: Packet Structs ===

--- Struct sizes (must match protocol spec) ---
  eth_hdr_t  : 14 bytes (expected 14)
  ipv4_hdr_t : 20 bytes (expected 20)
  ...
  All sizes correct.

══════════════════════════════════════════
Packet: DNS A query (UDP/IPv4) — www.example.com  (75 bytes)
══════════════════════════════════════════
[Ethernet]
  dst_mac    : ff:ff:ff:ff:ff:ff
  src_mac    : 00:11:22:33:44:55
  ether_type : 0x0800  (IPv4)
[IPv4]
  src_ip     : 198.51.100.5
  dst_ip     : 8.8.8.8
  protocol   : 17  (UDP)
[UDP]
  dst_port   : 53  (DNS)
[DNS]
  id         : 0x1234
  type       : QUERY
[DNS Question]
  qname      : www.example.com
  qtype      : 1 (A)
  qclass     : 1 (IN)
```

---

## Key concepts in the code

### 1. `__attribute__((packed))` — the most critical attribute

Without it the compiler inserts padding to align fields:

```c
/* Without packed — compiler might add padding: */
struct bad {
    uint8_t  a;      /* offset 0 */
    /* 3 bytes padding inserted! */
    uint32_t b;      /* offset 4, not 1 */
};  /* sizeof = 8, not 5 */

/* With packed — no padding: */
struct good {
    uint8_t  a;      /* offset 0 */
    uint32_t b;      /* offset 1 */
} __attribute__((packed));  /* sizeof = 5 */
```

If you forget `packed` on `ipv4_hdr_t`, `ip4->src_ip` points to the
wrong offset in the packet and you read garbage IP addresses.

### 2. Network byte order (big-endian)

x86 CPUs store multi-byte integers least-significant byte first (little-endian).
Network protocols store them most-significant byte first (big-endian).

```c
/* Port 53 in memory, as it appears in the packet: */
uint8_t bytes[] = { 0x00, 0x35 };   /* 0x0035 = 53 in big-endian */

/* On x86, reading this as uint16_t directly: */
uint16_t raw = *(uint16_t *)bytes;   /* reads as 0x3500 = 13568 — WRONG */

/* Correct way: */
uint16_t port = ntohs(*(uint16_t *)bytes);  /* converts to 53 — RIGHT */
```

**Every** port number, IP address, length field, and DNS field must be
converted with `ntohs()` or `ntohl()` before comparison or arithmetic.

### 3. Zero-copy pointer overlay

"Parsing" in a dataplane means casting, not copying:

```c
/* DPDK real app: */
uint8_t *pkt = rte_pktmbuf_mtod(mbuf, uint8_t *);

/* Overlay structs — no data copied, just pointer arithmetic: */
eth_hdr_t  *eth = (eth_hdr_t *)pkt;
ipv4_hdr_t *ip4 = (ipv4_hdr_t *)(pkt + ETH_HDR_LEN);
udp_hdr_t  *udp = (udp_hdr_t *)((uint8_t *)ip4 + IPV4_IHL_BYTES(ip4));
dns_hdr_t  *dns = (dns_hdr_t *)((uint8_t *)udp + UDP_HDR_LEN);
```

This is why DPDK is fast — no `memcpy` per packet. The packet stays in
the NIC-allocated hugepage buffer from receive to transmit.

### 4. Variable-length IPv4 header

IPv4 has an options field that makes the header variable-length (20–60 bytes).
Always use `IPV4_IHL_BYTES(ip4)` — never hardcode 20.

```c
#define IPV4_IHL_BYTES(hdr)  (((hdr)->version_ihl & 0x0F) << 2)
/* IHL field is count of 32-bit words; multiply by 4 to get bytes */
```

### 5. `read_u16_be` — safe unaligned reads

```c
static inline uint16_t read_u16_be(const uint8_t *p) {
    return (uint16_t)((p[0] << 8) | p[1]);
}
```

Used in `pkt_proc.h` for TLS SNI length extraction — identical pattern.

### 6. DNS qname wire format

DNS does NOT use null-terminated strings. It uses length-prefixed labels:

```text
"www.example.com" in DNS wire format:
  \x03 w w w \x07 e x a m p l e \x03 c o m \x00
   ^3          ^7                  ^3        ^end
```

---

## rte_pktmbuf header access (what you'll see in real code)

```c
/* In the real DP application app (pkt_proc.h): */
struct rte_mbuf  *mbuf = mbufs[i];
struct rte_ether_hdr *eth;
struct rte_ipv4_hdr  *ip4;
struct rte_udp_hdr   *udp;

eth = rte_pktmbuf_mtod(mbuf, struct rte_ether_hdr *);

if (ntohs(eth->ether_type) == RTE_ETHER_TYPE_IPV4) {
    ip4 = (struct rte_ipv4_hdr *)((uint8_t *)eth + sizeof(*eth));

    if (ip4->next_proto_id == IPPROTO_UDP) {
        udp = (struct rte_udp_hdr *)((uint8_t *)ip4 +
               rte_ipv4_hdr_len(ip4));

        if (ntohs(udp->dst_port) == 53) {
            /* DNS packet — parse qname, lookup policy */
        }
    }
}
```

---

## Next module

**Module 06 — DNS Parser**: Build a complete DNS query parser — extract
transaction ID, query type (A/AAAA), and the full domain name from the
wire format.

---

## Source files

| File | Download |
|---|---|
| `packet_structs.h` | [packet_structs.h](https://github.com/Ajay3007/dataplane-learning/blob/main/05-packet-structs/packet_structs.h){:target="_blank" rel="noopener noreferrer"} |
| `packet_parser.c` | [packet_parser.c](https://github.com/Ajay3007/dataplane-learning/blob/main/05-packet-structs/packet_parser.c){:target="_blank" rel="noopener noreferrer"} |
| `Makefile` | [Makefile](https://github.com/Ajay3007/dataplane-learning/blob/main/05-packet-structs/Makefile){:target="_blank" rel="noopener noreferrer"} |
