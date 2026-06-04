---
layout: default
title: "Module 09 — Mempool + mbuf"
permalink: /learning/data-plane/projects/module-09-mempool-mbuf/
---

# Module 09 — Mempool + mbuf

> **Reference code** — requires DPDK installed.

## What you learn

How DPDK manages packet memory via pre-allocated mempools and `rte_mbuf`
structures — why mempools exist, how the mbuf memory layout works, the
full alloc/fill/process/free lifecycle, in-place packet modification
(the pattern used by the DNS sinkhole), hardware checksum offload flags,
and multi-segment (chained) mbufs.

---

## Why mempools — the core insight

```text
Without mempools (naive approach):
  Packet arrives → malloc(1500) → process → free()
  At 2M pkts/sec: 2M malloc() calls/sec
  malloc has locks + may call brk() → becomes the bottleneck

With mempools (DPDK approach):
  Startup: pre-allocate 65535 mbufs in hugepage memory
  Runtime: "alloc" = pop pointer from lockless ring  (~10 ns)
           "free"  = push pointer back to ring        (~10 ns)
  No syscalls, no locks in the fast path
```

The mempool object ring uses the same design as Module 03 (rte_ring).

---

## mbuf memory layout

```text
One mbuf object in the pool:

  ┌─────────────────────────────┐  ← buf_addr (hugepage address)
  │  struct rte_mbuf  (~128B)   │  metadata: data_off, data_len, pkt_len,
  │                             │  nb_segs, port, ol_flags, hash.rss, ...
  ├─────────────────────────────┤
  │  private area  (0B default) │  app-specific metadata per mbuf
  ├─────────────────────────────┤
  │  headroom      (128B)       │  reserved for prepending headers
  ├─────────────────────────────┤  ← buf_addr + data_off
  │                             │  ← rte_pktmbuf_mtod(m, T*)
  │  packet data                │
  │  (data_len bytes)           │
  │                             │
  ├─────────────────────────────┤
  │  tailroom                   │  available for appending (answer section!)
  └─────────────────────────────┘  ← buf_addr + buf_len
```

---

## Where this fits in the real application

```text
Startup:
  mbuf_pool = rte_pktmbuf_pool_create("pktmbuf_pool_s0",
                  65535, 256, 0, RTE_MBUF_DEFAULT_BUF_SIZE,
                  rte_socket_id())
  rte_eth_rx_queue_setup(port, queue, nb_desc, socket, &cfg, mbuf_pool)

RX lcore:
  nb_rx = rte_eth_rx_burst(port, queue, mbufs, BURST_SIZE)

Worker lcore:
  eth = rte_pktmbuf_mtod(mbufs[i], eth_hdr_t *)  ← zero-copy header access

DNS sinkhole (Module 18):
  → rewrite packet in-place via rte_pktmbuf_mtod()
  → rte_pktmbuf_append() for answer section bytes
  → m->ol_flags |= TX_IPV4 | TX_IP_CKSUM | TX_UDP_CKSUM

TX lcore:
  nb_tx = rte_eth_tx_burst(port, queue, mbufs, nb_fwd)
  for dropped mbufs: rte_pktmbuf_free(m)
```

---

## Key concepts in the code

### 1. Pool size: must be 2^k − 1

```c
#define POOL_NUM_MBUFS  8191   /* 2^13 - 1: correct */
#define POOL_NUM_MBUFS  8192   /* 2^13:     WRONG — rte_ring adds 1, wastes a slot */
```

### 2. Per-lcore cache — reducing ring contention

```text
Without cache: every alloc/free touches the pool's central ring
               → ring lock contention between lcores

With cache_size=256: each lcore keeps 256 mbufs locally
               → alloc/free from local cache (no ring) until cache empties/fills
               → ring only touched when cache needs replenishment
               → typical alloc is ~3 ns instead of ~10 ns
```

### 3. `rte_pktmbuf_mtod` — the most-used macro

```c
/* Get typed pointer to packet start */
eth_hdr_t *eth = rte_pktmbuf_mtod(m, eth_hdr_t *);

/* Expands to: */
eth_hdr_t *eth = (eth_hdr_t *)((char *)(m)->buf_addr + (m)->data_off);
```

### 4. `rte_pktmbuf_append` — used in DNS sinkhole

```c
/* Reserve space at the tail and return pointer to it */
char *answer_section = rte_pktmbuf_append(m, dns_answer_len);
if (!answer_section) { /* tailroom exhausted */ }
memcpy(answer_section, answer_bytes, dns_answer_len);
/* Update IP total_len and UDP dgram_len to include the new bytes */
ip4->total_len = htons(ntohs(ip4->total_len) + dns_answer_len);
```

### 5. Hardware checksum offload

```c
m->ol_flags |= RTE_MBUF_F_TX_IPV4 | RTE_MBUF_F_TX_IP_CKSUM
             | RTE_MBUF_F_TX_UDP_CKSUM;
ip4->checksum = 0;
udp->checksum = rte_ipv4_phdr_cksum(ip4, m->ol_flags);
```

Software checksum would cost ~50 ns per packet — HW offload costs ~0.

### 6. Multi-segment guard in the real app

```c
nb_rx = rte_eth_rx_burst(port, queue, mbufs, BURST_SIZE);
for (int i = 0; i < nb_rx; i++) {
    if (unlikely(mbufs[i]->nb_segs > 1)) {
        /* Jumbo frame — the DP application drops it rather than paying linearise cost */
        rte_pktmbuf_free(mbufs[i]);
        continue;
    }
    eth = rte_pktmbuf_mtod(mbufs[i], eth_hdr_t *);
}
```

---

## Pool sizing reference

| Deployment | num_mbufs | Rationale |
|---|---|---|
| Dev/test (VM) | 4095 (2^12-1) | Small hugepage allocation |
| Single port, 4 queues | 16383 (2^14-1) | 4×1024 descriptors + 3× headroom |
| 4 ports, 4 queues each | 65535 (2^16-1) | 16×1024 + 3× headroom |
| the DP application production | 65535 | Used in app_main.c |

---

## Next module

**Module 10 — Port Init**: Configure a DPDK NIC port — set up RX/TX queues,
descriptor rings, link speed, promiscuous mode, and RSS.

---

## Source files

| File | Download |
|---|---|
| `mempool_mbuf.c` | [mempool_mbuf.c]({{ '/assets/code/data-plane/projects/09-mempool-mbuf/mempool_mbuf.c' | relative_url }}) |
| `Makefile` | [Makefile]({{ '/assets/code/data-plane/projects/09-mempool-mbuf/Makefile' | relative_url }}) |
