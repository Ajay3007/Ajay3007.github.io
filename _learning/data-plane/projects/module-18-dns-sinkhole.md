---
layout: default
title: "Module 18 — DNS Sinkhole"
permalink: /learning/data-plane/projects/module-18-dns-sinkhole/
---

# Module 18 — DNS Sinkhole

> **Pure C** — fully runnable. No DPDK, no Hyperscan.

## What you learn

How to rewrite a DNS query packet into a sinkhole response **in-place** —
the exact technique used in SASE DP to redirect blocked DNS queries to a
walled-garden IP without allocating a new packet buffer.

Covers all four variants:
- `dns_sinkhole_udp_ipv4()` — UDP/IPv4, A or AAAA query
- `dns_sinkhole_udp_ipv6()` — UDP/IPv6, A or AAAA query
- `dns_sinkhole_tcp_ipv4()` — TCP/IPv4 (with 2-byte length prefix update)

---

## What the sinkhole does

```text
Client sends DNS A query:
  ETH[client→gateway]  IPv4[192.168.1.100→8.8.8.8]  UDP[54321→53]
  DNS: QUERY blocked.example.com A

SASE DP rewrites the mbuf in-place:
  ETH[gateway→client]  IPv4[8.8.8.8→192.168.1.100]  UDP[53→54321]
  DNS: RESPONSE  ancount=1
       ANSWER: blocked.example.com A 60 10.1.1.1  ← walled garden
```

The client never reaches the blocked domain. From their perspective, the
DNS query got a response — just not the IP they expected.

---

## Where this fits in the real application

```text
Worker lcore:
  │
  ├─► dns_parse_message()         → domain, qtype, question_wire_end
  ├─► group_and_url_processing_for_dns()  → PROCESS_WORKFLOW
  │
  └─► if PROCESS_WORKFLOW:
        if qtype == A:
          dns_reuse_request_as_redirect_response_ip4(mbuf, wg_ipv4)
        │
        ├─ Swap ETH/IP/UDP headers
        ├─ Set DNS QR=1, ancount=1
        ├─ rte_pktmbuf_append(mbuf, answer_len)  ← extend tail
        ├─ Build answer section (0xC00C | type | TTL | wg_ip)
        ├─ Update IP total_len, UDP dgram_len
        └─ m->ol_flags |= TX_IPV4 | TX_IP_CKSUM | TX_UDP_CKSUM
```

---

## Build and run

```bash
make
./dns_sinkhole
```

Expected output:
```
=== Module 18: DNS Sinkhole ===
Walled garden IPv4: 10.1.1.1

Test 1: Sinkhole UDP/IPv4 A query
  Before: src=192.168.1.100:54321 → dst=8.8.8.8:53
  After:
    src=8.8.8.8:53 → dst=192.168.1.100:54321
    QR=1  RA=1  RCODE=0
    Answer RR: type=1 (A)  ttl=60
    RDATA (A): 10.1.1.1
  PASS ✓

=== All tests passed ===
```

---

## Key concepts

### 1. Why in-place rewrite (no new allocation)

```text
Option A (naive): alloc new mbuf → build response → free query mbuf
  Cost: rte_pktmbuf_alloc(~10ns) + memcpy(~200ns) + rte_pktmbuf_free(~10ns)
  At 200K blocked DNS/sec: 200,000 × 220ns = 44ms/sec CPU overhead

Option B (in-place): modify the query mbuf directly
  Cost: ~30ns (a few memcpy + pointer arithmetic)
  At 200K blocked DNS/sec: 200,000 × 30ns = 6ms/sec — 7× less overhead
```

### 2. Header swap — the correct way

```c
/* WRONG: overwrites src before you can read it */
memcpy(eth->dst_mac, eth->src_mac, 6);
memcpy(eth->src_mac, eth->dst_mac, 6);  /* dst_mac is already gone! */

/* CORRECT: save one side first */
uint8_t tmp[6];
memcpy(tmp,          eth->dst_mac, 6);
memcpy(eth->dst_mac, eth->src_mac, 6);
memcpy(eth->src_mac, tmp,          6);
```

### 3. DNS answer section layout

```text
Offset  Size  Value           Meaning
------  ----  -----           -------
0       2     0xC0 0x0C       Name: pointer to offset 12 (question name)
2       2     0x00 0x01       Type: A (or 0x001C for AAAA)
4       2     0x00 0x01       Class: IN
6       4     0x00 0x00 0x00 0x3C  TTL: 60 seconds
10      2     0x00 0x04       RDLENGTH: 4 (or 16 for AAAA)
12      4     10.1.1.1        RDATA: walled garden IPv4
```

The pointer `0xC00C` means "the name for this answer record is the same
as the name at offset 12 in the DNS message (the question qname)".

### 4. `question_wire_end` — where to append

```text
DNS message structure:
  [DNS header 12B] [question section ...] [← answer appended here]
                                          ^
                                   question_wire_end
```

Getting this offset wrong corrupts the DNS question section or appends
the answer to the wrong location.

### 5. Length field cascade

After appending the answer, three length fields must be updated:

```c
udp->dgram_len  += answer_len;   /* UDP header + payload */
ip4->total_len  += answer_len;   /* entire IP packet */
/* For TCP: dns_tcp_prefix += answer_len  (2-byte DNS length prefix) */
```

Missing any one causes the receiver to parse the wrong number of bytes,
producing a malformed response that the client DNS resolver discards.

### 6. Hardware checksum offload (DPDK only)

```c
/* After in-place rewrite in DPDK: */
ip4->checksum  = 0;    /* NIC will compute */
udp->checksum  = rte_ipv4_phdr_cksum(ip4, m->ol_flags);
m->ol_flags   |= RTE_MBUF_F_TX_IPV4 | RTE_MBUF_F_TX_IP_CKSUM
               | RTE_MBUF_F_TX_UDP_CKSUM;
```

Without this (or correct software checksum), the client's network stack
discards the response as a bad checksum. This was one of the trickiest
bugs to diagnose in the real SASE DP sinkhole implementation.

---

## DPDK mbuf append (what replaces memcpy in real app)

```c
/* Step 1: extend the mbuf tail */
char *answer_ptr = rte_pktmbuf_append(mbuf, answer_len);
if (!answer_ptr) {
    LOG_ERROR("Cannot append DNS answer: tailroom exhausted");
    rte_pktmbuf_free(mbuf);
    return;
}

/* Step 2: write answer bytes */
build_dns_answer((uint8_t *)answer_ptr, qtype, wg_ipv4, wg_ipv6);

/* mbuf->data_len and mbuf->pkt_len are updated automatically by append */
```

---

## Next module

**Module 19 — Kafka Producer (CDR Export)**: Every policy decision
generates a Charging Data Record that is exported to Kafka.

---

## Source files

| File | Download |
|---|---|
| `dns_sinkhole.c` | [dns_sinkhole.c]({{ '/assets/code/data-plane/projects/18-dns-sinkhole/dns_sinkhole.c' | relative_url }}) |
| `Makefile` | [Makefile]({{ '/assets/code/data-plane/projects/18-dns-sinkhole/Makefile' | relative_url }}) |
