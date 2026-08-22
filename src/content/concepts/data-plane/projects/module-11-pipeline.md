---
title: "Module 11 — Multi-lcore RX/TX Pipeline"
description: "Module 11 — Multi-lcore RX/TX Pipeline Reference code — requires DPDK installed."
domain: data-plane
track: dataplane-projects
order: 99
ownHeader: true
url: /learning/data-plane/projects/module-11-pipeline/
---

# Module 11 — Multi-lcore RX/TX Pipeline

> **Reference code** — requires DPDK installed.

## What you learn

How to wire together EAL (Module 08), mempool (Module 09), and port init
(Module 10) into a complete multi-lcore packet processing pipeline — the
skeleton of the DP application at runtime.

This is the structural blueprint: RX lcore polls the NIC, distributes
packets to worker lcores via `rte_ring`, workers parse + apply policy,
forward packets to a shared TX ring, and the TX lcore drains it to the NIC.

---

## Pipeline topology

```text
NIC port 0
  │  (DMA fills mbufs from pool — Module 09)
  ↓
RX lcore (lcore 1)
  rte_eth_rx_burst(port=0, queue=0, mbufs, BURST_SIZE=32)
  │
  │  Round-robin distribute across worker rx_rings
  │
  ├── rx_ring[0] ──► Worker lcore 2
  ├── rx_ring[1] ──► Worker lcore 3
  ├── rx_ring[2] ──► Worker lcore 4
  └── rx_ring[3] ──► Worker lcore 5
                          │
           For each mbuf: │
             parse ETH/IP/UDP-TCP          (Module 05)
             DNS: dns_parse_message()       (Module 06)
             TLS: tls_extract_sni()         (Module 07)
             policy lookup                  (Module 17)
               ALLOW    → tx_ring
               DROP     → rte_pktmbuf_free()
               SINKHOLE → modify in-place → tx_ring  (Module 18)
                          │
                       tx_ring (shared MPSC)
                          │
TX lcore (lcore 1)
  rte_ring_dequeue_burst(tx_ring, mbufs, BURST_SIZE)
  rte_eth_tx_burst(port=0, queue=0, mbufs, nb)
  free unsent mbufs
  │
  ↓
NIC port 0 → wire
```

---

## Files

| File | Purpose |
|---|---|
| `pipeline.c` | Full pipeline: RX/worker/TX lcore functions, ring setup, stats, shutdown |
| `Makefile` | DPDK build |

---

## Key concepts in the code

### 1. Each lcore has exactly one job

```text
RX lcore:     ONLY calls rte_eth_rx_burst() + rte_ring_enqueue()
Worker lcore: ONLY does parse + policy + ring enqueue/dequeue
TX lcore:     ONLY calls rte_ring_dequeue() + rte_eth_tx_burst()
```

If the RX lcore also runs policy logic, it slows down and the NIC RX
descriptor ring fills → `stats.imissed` increments → silent packet loss.

### 2. `rte_pause()` — never `sleep()`

```c
if (nb_rx == 0) {
    rte_pause();   /* x86 PAUSE: hints CPU it's in a spin loop */
    continue;
}
```

`sleep()` or `usleep()` yield the thread to the OS scheduler. The lcore
may not resume for milliseconds — all in-flight NIC descriptors fill up.

### 3. SPSC ring for RX→worker, MPSC for worker→TX

```c
/* rx_ring: single producer (RX lcore), single consumer (one worker) */
rx_rings[i] = rte_ring_create(name, RING_SIZE, socket,
                               RING_F_SP_ENQ | RING_F_SC_DEQ);

/* tx_ring: multiple producers (all workers), single consumer (TX lcore) */
tx_ring = rte_ring_create("tx_ring", RING_SIZE, socket, 0); /* MPSC default */
```

SPSC is faster than MPMC (no CAS atomic needed — just head/tail with
memory barriers). Use the most restrictive type you can justify.

### 4. `unlikely()` — branch prediction hints

```c
if (unlikely(mbuf->nb_segs > 1))    /* rarely true at MTU=1500 */
    return DECISION_DROP;

if (unlikely(rte_ring_enqueue(...) != 0))  /* rarely true if ring sized correctly */
    rte_pktmbuf_free(m);
```

`unlikely(x)` expands to `__builtin_expect((x), 0)`. On the hot path
(millions of packets/sec), branch mispredictions cost ~15 cycles each.

### 5. Free unsent TX mbufs — the leak you'll hit

```c
uint16_t nb_tx = rte_eth_tx_burst(port, queue, mbufs, nb);

/* MANDATORY: free what the NIC didn't send */
for (uint16_t i = nb_tx; i < nb; i++)
    rte_pktmbuf_free(mbufs[i]);
```

`rte_eth_tx_burst()` may return `nb_tx < nb` when the NIC TX descriptor
ring is full. The NIC only frees mbufs it actually DMA'd. If you don't
free the unsent ones, the pool slowly drains to zero — silent stall.

This is one of the most common bugs in new DPDK code.

### 6. Shutdown ordering — drain the rings

```text
Stop workers → wait for workers to exit →
Stop TX lcore (TX drains tx_ring before exiting) →
wait for TX →
rte_eth_dev_stop() → rte_eal_cleanup()
```

Never stop the TX lcore before workers. Workers may enqueue a final burst
to tx_ring after the stop signal. If TX exits first, those packets are
stuck in the ring — the client's sinkhole response is never delivered.

---

## Next module

**Module 12 — rte_hash CRUD**: Deep dive into DPDK's `rte_hash` table
operations — the exact API used for `domain_details_table` in each
`group_struct`.

---

## Source files

| File | Download |
|---|---|
| `pipeline.c` | [pipeline.c](https://github.com/Ajay3007/dataplane-learning/blob/main/11-pipeline/pipeline.c){:target="_blank" rel="noopener noreferrer"} |
| `Makefile` | [Makefile](https://github.com/Ajay3007/dataplane-learning/blob/main/11-pipeline/Makefile){:target="_blank" rel="noopener noreferrer"} |
