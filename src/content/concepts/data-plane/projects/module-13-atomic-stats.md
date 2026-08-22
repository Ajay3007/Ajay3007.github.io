---
title: "Module 13 — Atomic Counters + Per-lcore Stats"
description: "Module 13 — Atomic Counters + Per-lcore Stats Pure C — fully runnable without DPDK."
domain: data-plane
track: dataplane-projects
order: 99
url: /learning/data-plane/projects/module-13-atomic-stats/
---

# Module 13 — Atomic Counters + Per-lcore Stats

> **Pure C** — fully runnable without DPDK. Build with `make`, run with `./atomic_stats`.

## What you learn

How to implement lock-free per-lcore statistics in C using `_Atomic` /
`stdatomic.h` — the exact pattern used for every counter in the DP application.
Includes a measured demo of false sharing (why cache-line alignment matters),
atomic vs mutex performance (why atomics are mandatory in the hot path),
memory ordering choices, and a live rate calculation from concurrent workers.

---

## Atomic variables in the real DP application project

From `domain_scan.h`:

```c
extern atomic_ullong hs_db_compile_count;
extern atomic_ullong hs_scratch_alloc_count;
extern atomic_ulong  match_count;
extern atomic_ulong  dns_rx_count;
extern atomic_ulong  dns_proc_count;
```

From `policy_cache.c`:

```c
atomic_ulong malicious_domain_count;
```

---

## Build and run

```bash
make
./atomic_stats
```

Expected output (abbreviated):
```
=== Module 13: Atomic Counters + Per-lcore Stats ===

sizeof(lcore_stats_t) = 128 bytes  (must be multiple of 64)
Alignment check passed.

Demo 2: False sharing
  Bad  layout (shared cache line): 1.247 sec
  Good layout (aligned, separate): 0.312 sec
  Speedup: 4.0x

Demo 3: atomic vs mutex
  4 threads × 10M increments each:
  mutex:  2.841 sec  (71 ns/op)
  atomic: 0.624 sec  (16 ns/op)
  Speedup: 4.6x
```

---

## Key concepts

### 1. `memory_order_relaxed` for stats counters

```c
/* In the hot path — worker lcore increments its own counter */
atomic_fetch_add_explicit(&stats->pkt_rx, 1, memory_order_relaxed);

/* Main lcore reads for aggregation */
unsigned long rx = atomic_load_explicit(&stats->pkt_rx, memory_order_relaxed);
```

`memory_order_relaxed` guarantees **atomicity** (no torn reads/writes)
but no **ordering** (no fence instruction emitted on x86). For a stat
counter this is always sufficient. Using the default `memory_order_seq_cst`
emits an `MFENCE` instruction — ~20 cycles overhead per increment in the hot path.

| Ordering | Fence | Use for |
|---|---|---|
| `relaxed` | none | stats counters, ref counts |
| `release`/`acquire` | store/load fence | publishing data (flag after write) |
| `seq_cst` | full fence (MFENCE) | global ordering — almost never needed |

### 2. `__attribute__((aligned(64)))` on `lcore_stats_t`

Without alignment:

```text
lcore_stats_t stats[4]:
  stats[0]: bytes 0–47   → cache line 0 (bytes 0–63)   ← lcore 3 writes
  stats[1]: bytes 48–95  → spans lines 0–1             ← lcore 4 writes
                                                           SAME cache line as lcore 3!
```

Every time lcore 4 writes `stats[1].pkt_rx`, the CPU sends a cache
invalidation to lcore 3's core. This is **false sharing**.

With `aligned(64)`:
```text
  stats[0]: bytes 0–63    → cache line 0 (lcore 3 only)
  stats[1]: bytes 64–127  → cache line 1 (lcore 4 only)
```

Zero cross-core invalidations. The measured 4× speedup in the demo shows
the real cost at 50M increments/sec.

### 3. Per-lcore vs global atomics

```c
/* Per-lcore: only THIS lcore writes — zero contention */
atomic_fetch_add_explicit(&stats->pkt_rx, 1, memory_order_relaxed);
/* Cost: ~3–5 ns (just the atomic instruction, no cache miss) */

/* Global (cross-lcore): ALL lcores write — contention */
atomic_fetch_add_explicit(&dns_rx_count, 1, memory_order_relaxed);
/* Cost: ~10–20 ns (CAS loop if contended, cache line bounces between cores) */
```

Keep global atomics for infrequent events: DB compiled, scratch allocated,
malicious domain loaded. Use per-lcore atomics for per-packet counters.

### 4. Stats aggregation pattern (main lcore)

```c
while (running) {
    sleep_ms(1000);
    stats_aggregate(all_lcore_stats, NUM_WORKERS, &curr);

    double dt = (curr.timestamp_ns - prev.timestamp_ns) / 1e9;
    double rx_pps = (curr.pkt_rx - prev.pkt_rx) / dt;

    LOG_INFO("rx=%.0f/s  dns=%.0f/s", rx_pps, (curr.pkt_dns - prev.pkt_dns) / dt);
    prev = curr;
}
```

No lock needed: stats_aggregate reads atomics with `relaxed` ordering.

### 5. `aligned_alloc` for arrays

```c
/* Array of N cache-aligned stats structs */
lcore_stats_t *all = aligned_alloc(CACHE_LINE_SIZE,
                                    N * sizeof(lcore_stats_t));
```

`malloc()` only guarantees 16-byte alignment. Without `aligned_alloc`,
even if the struct has `aligned(64)`, the first element of a heap-allocated
array might start at an unaligned address — breaking the false-sharing protection.

---

## Connection to DPDK's atomic API

DPDK has its own atomic types (`rte_atomic64_t`, `rte_atomic32_t`) which
predate C11 atomics. Modern DPDK (>= 21.x) recommends using C11 `_Atomic`
directly — which is what the DP application uses.

```c
/* Old DPDK style (deprecated): */
rte_atomic64_t counter;
rte_atomic64_add(&counter, 1);

/* Modern C11 (the DP application / this module): */
atomic_ulong counter;
atomic_fetch_add_explicit(&counter, 1, memory_order_relaxed);
```

---

## Next module

**Module 14 — NUMA-aware Memory Allocation**: `rte_malloc_socket`,
`rte_zmalloc_socket`, `rte_memzone_reserve` — allocating memory on the
correct NUMA socket for NIC queues, hash tables, and Hyperscan databases.

---

## Source files

| File | Download |
|---|---|
| `atomic_stats.c` | [atomic_stats.c](https://github.com/Ajay3007/dataplane-learning/blob/main/13-atomic-stats/atomic_stats.c){:target="_blank" rel="noopener noreferrer"} |
| `Makefile` | [Makefile](https://github.com/Ajay3007/dataplane-learning/blob/main/13-atomic-stats/Makefile){:target="_blank" rel="noopener noreferrer"} |
