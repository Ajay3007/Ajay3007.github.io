---
layout: default
title: "Module 14 — NUMA-aware Memory Allocation"
permalink: /learning/data-plane/projects/module-14-numa-alloc/
---

# Module 14 — NUMA-aware Memory Allocation

**Part A** (NUMA topology reader) — pure C, runs on any Linux box.  
**Part B** (DPDK allocation APIs) — reference code, requires DPDK.

## What you learn

Why NUMA placement matters in a dataplane application (2× memory latency
penalty for cross-socket access), how to detect your server's NUMA topology,
and which DPDK allocation API to use for every type of dataplane object —
hash tables, mempools, Hyperscan databases, per-lcore scratch spaces.

---

## The NUMA penalty — why it matters at line rate

```text
Single-socket server (all RAM local):
  Any lcore reads any address → ~80 ns

Dual-socket server (cross-NUMA access):
  Socket 0 lcore reads socket 1 memory → ~170 ns  (2× slower)
  Socket 0 lcore reads socket 0 memory → ~80 ns   (baseline)

At 2M DNS lookups/sec with domain_details_table on wrong socket:
  Extra latency = 2,000,000 × (170 - 80) ns = 180 ms/sec per worker lcore
  4 worker lcores: 720 ms/sec wasted — almost 1 full CPU core consumed
  by memory bus latency alone
```

This is why every hash table, pool, and database in SASE DP specifies
`socket_id = rte_socket_id()` or `rte_eth_dev_socket_id(port_id)`.

---

## Build and run

```bash
# Part A only — reads /sys topology, no DPDK needed
make
./numa_alloc
```

---

## Key concepts

### 1. DPDK allocation hierarchy

```text
hugepage memory (pre-allocated, pinned, physically contiguous)
  │
  ├─ rte_memzone: named regions, persistent, shareable across processes
  │
  └─ rte_malloc heap: anonymous, per-socket pools
       ├─ rte_malloc_socket()   → explicit socket, not zero-initialised
       └─ rte_zmalloc_socket()  → explicit socket, zero-initialised (use this)
```

### 2. Which API for each SASE DP object

| Object | API | Socket |
|---|---|---|
| `group_struct` | `rte_zmalloc_socket` | worker lcore's socket |
| `rte_hash` (domain table) | `rte_hash_create` → `.socket_id` | worker lcore's socket |
| `rte_mempool` (mbufs) | `rte_pktmbuf_pool_create` → `socket_id` | NIC port's socket |
| Hyperscan DB | `hs_set_allocator` → `rte_malloc_socket` | worker lcores' socket |
| Hyperscan scratch | `hs_clone_scratch` | each lcore's own socket |
| `rte_ring` (rx/tx rings) | `rte_ring_create` → `socket_id` | worker lcores' socket |

### 3. Socket ID query APIs

```c
rte_socket_id()                    /* socket of the calling lcore */
rte_lcore_to_socket_id(lcore_id)   /* socket of a specific lcore */
rte_eth_dev_socket_id(port_id)     /* socket of a NIC port */
```

**The NIC's socket is the most important one.** If the mbuf pool is on the
wrong socket, every packet receive and transmit crosses the QPI/UPI.

```c
/* CORRECT: pool on the same socket as the NIC */
int nic_sock = rte_eth_dev_socket_id(port_id);
pool = rte_pktmbuf_pool_create("pool", n, cache, 0,
                                RTE_MBUF_DEFAULT_BUF_SIZE,
                                nic_sock);               /* ← matches NIC */
```

### 4. Hyperscan NUMA allocation in SASE DP

```c
/* Custom allocator wrappers — redirect Hyperscan's internal malloc to DPDK */
static void *hs_rte_malloc(size_t size) {
    return rte_malloc_socket("hs_internal", size, 0, rte_socket_id());
}
static void hs_rte_free(void *ptr) { rte_free(ptr); }

/* Set before any hs_compile call */
hs_set_allocator(hs_rte_malloc, hs_rte_free);
```

Without this, Hyperscan uses `malloc()` (system allocator), which allocates
from normal 4KB pages on the process's default NUMA node.

### 5. Detecting the NUMA topology of your server

```bash
# Show NUMA nodes and their CPUs
numactl --hardware

# Show which NUMA node a PCI device (NIC) is on
cat /sys/bus/pci/devices/0000:01:00.0/numa_node

# Show hugepage allocation per node
cat /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages
```

---

## Common NUMA mistakes in DPDK code

| Mistake | Symptom | Fix |
|---|---|---|
| `rte_malloc()` instead of `rte_malloc_socket()` | 2× lookup latency on dual-socket | Use `rte_malloc_socket(..., rte_socket_id())` |
| mbuf pool on wrong socket from NIC | High imissed, NIC DMA stalls | `rte_pktmbuf_pool_create(..., rte_eth_dev_socket_id(port))` |
| Hyperscan DB on socket 0, workers on socket 1 | hs_scan takes 2× longer | Use `hs_set_allocator` to redirect to NUMA-local hugepages |

---

## Next module

**Module 15 — Hyperscan: Compile Patterns**: The first Hyperscan module.
Compile single and multi-pattern databases (`hs_compile` / `hs_compile_multi`),
understand the difference between regex and literal.

---

## Source files

| File | Download |
|---|---|
| `numa_alloc.c` | [numa_alloc.c]({{ '/assets/code/data-plane/projects/14-numa-alloc/numa_alloc.c' | relative_url }}) |
| `Makefile` | [Makefile]({{ '/assets/code/data-plane/projects/14-numa-alloc/Makefile' | relative_url }}) |
