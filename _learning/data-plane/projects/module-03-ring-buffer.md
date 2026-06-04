---
layout: default
title: "Module 03 — Ring Buffer (SPSC, lock-free)"
permalink: /learning/data-plane/projects/module-03-ring-buffer/
---

# Module 03 — Ring Buffer (SPSC, lock-free)

## What you learn

How to implement a lock-free Single-Producer Single-Consumer (SPSC) ring
buffer in C — the manual equivalent of DPDK's `rte_ring`.

A ring buffer is the primary inter-lcore communication channel in a DPDK
application. In the DP application:

- **RX lcore** enqueues received `rte_mbuf*` pointers into a ring
- **Worker lcores** dequeue from the ring and run policy decisions
- **Worker lcores** enqueue processed packets into a TX ring
- **TX lcore** dequeues and calls `rte_eth_tx_burst()`

Understanding this module makes `rte_ring`'s source code immediately
readable — the same three ideas appear in both:
1. Power-of-2 size with bitmask indexing
2. Separate head (producer) and tail (consumer) on separate cache lines
3. Acquire/release memory barriers

---

## Where this fits in the real application

```text
RX lcore
  │
  │  rte_eth_rx_burst() → mbufs[]
  │  rte_ring_enqueue_burst(rx_ring, mbufs, nb_rx)
  │
  ▼
[  rx_ring  ]    ← rte_ring, created with ring_create() equivalent
  │
  │  rte_ring_dequeue_burst(rx_ring, mbufs, BURST_SIZE)
  ▼
Worker lcore
  │  process_dns_for_group()
  │  policy decision → DROP / ALLOW / SINKHOLE
  │  rte_ring_enqueue_burst(tx_ring, fwd_mbufs, nb_fwd)
  │
  ▼
[  tx_ring  ]
  │
  ▼
TX lcore
  │  rte_eth_tx_burst()
```

---

## Files

| File | Purpose |
|---|---|
| `ring.h` | Struct, API declarations, inline status helpers |
| `ring.c` | Implementation, functional tests, concurrent producer/consumer demo |
| `Makefile` | Build rules (`-lpthread` required for demo threads) |

---

## Build and run

```bash
make
./ring
```

Expected output:
```
=== Module 03: Ring Buffer (SPSC) ===
ring_t size: 128 bytes

--- Test 1: basic enqueue/dequeue ---
  PASS: FIFO order preserved
--- Test 2: ring full behaviour ---
  PASS: RING_FULL returned correctly
--- Test 3: ring empty behaviour ---
  PASS: RING_EMPTY returned on empty ring
--- Test 4: index wraparound ---
  PASS: head/tail wrapped around correctly
--- Test 5: concurrent producer/consumer ---
[producer] Starting: will enqueue 1000 items in bursts of 16
[consumer] Starting: waiting for items
[producer] Done: enqueued 1000 items
[consumer] Done: received 1000 items
  consumed_sum = 499500  expected = 499500
  PASS: all items delivered, no drops, no corruption

All tests passed.
```

---

## Key concepts in the code

### 1. Power-of-2 size + bitmask (instead of modulo)

```c
r->mask = size - 1;
// instead of:  index % size        (division, ~20 cycles)
// we use:      index & r->mask     (AND,      ~1 cycle)
```

This is one of the most common DPDK micro-optimisations. Every index
access in the inner loop benefits from it. `rte_ring` uses the same trick.

### 2. Sentinel slot — why capacity is `size - 1`

The ring uses one slot as a sentinel so `head == tail` unambiguously means
**empty**. If we allowed `head == tail` to also mean full, we'd need a
separate `count` field — which requires atomic updates from both producer
and consumer (contention). The sentinel avoids that.

```text
size = 4, mask = 3
head=0 tail=0 → empty   (head == tail)
head=1 tail=0 → 1 item
head=2 tail=0 → 2 items
head=3 tail=0 → FULL    ((head-tail) & mask == size-1 == 3)
```

### 3. Memory barriers — why they matter

```c
/* producer: write data THEN advance head */
r->entries[head & r->mask] = obj;
__atomic_store_n(&r->head, next, __ATOMIC_RELEASE);  // barrier here

/* consumer: read head THEN read data */
head = __atomic_load_n(&r->head, __ATOMIC_ACQUIRE);  // barrier here
*obj = r->entries[tail & r->mask];
```

Without `RELEASE`/`ACQUIRE`:
- The CPU or compiler can reorder the store to `entries[]` to happen
  **after** the store to `head`.
- The consumer sees the new `head` and reads a slot that hasn't been
  written yet → **silent data corruption**.

`RELEASE` ensures all stores before it are visible before the store itself.
`ACQUIRE` ensures all loads after it see everything that happened before
the paired `RELEASE`.

In DPDK this is expressed as `rte_smp_wmb()` / `rte_smp_rmb()`.

### 4. False sharing prevention

`head` and `tail` are aligned to separate cache lines (64 bytes each):

```c
uint32_t head  __attribute__((aligned(RING_CACHE_LINE_SIZE)));
uint32_t tail  __attribute__((aligned(RING_CACHE_LINE_SIZE)));
```

Without this: every time the producer writes `head`, the CPU broadcasts
a cache line invalidation to the consumer's core (which holds `tail` in
the **same** cache line). The consumer stalls waiting for the line.
With separate cache lines: each core owns its index without interference.

`rte_ring` uses `__rte_cache_aligned` for the same reason.

### 5. DPDK mapping

| This module | DPDK equivalent |
|---|---|
| `ring_create(size)` | `rte_ring_create(name, size, socket_id, flags)` |
| `ring_enqueue(r, obj)` | `rte_ring_enqueue(r, obj)` |
| `ring_dequeue(r, &obj)` | `rte_ring_dequeue(r, &obj)` |
| `ring_enqueue_burst(...)` | `rte_ring_enqueue_burst(...)` |
| `ring_dequeue_burst(...)` | `rte_ring_dequeue_burst(...)` |
| `mask = size - 1` | identical in rte_ring source |
| `__ATOMIC_RELEASE` | `rte_smp_wmb()` |
| `__ATOMIC_ACQUIRE` | `rte_smp_rmb()` |

The main differences in `rte_ring`:
- MPMC support via CAS (`__atomic_compare_exchange`) for multi-producer safety
- NUMA-aware allocation (`rte_malloc_socket` on the correct socket)
- Named rings registered in a global table for cross-process access

---

## Next module

**Module 04 — Hash Map**: A fixed-size open-addressing hash map in pure C —
the manual equivalent of DPDK's `rte_hash`.

---

## Source files

| File | Download |
|---|---|
| `ring.h` | [ring.h]({{ '/assets/code/data-plane/projects/03-ring-buffer/ring.h' | relative_url }}) |
| `ring.c` | [ring.c]({{ '/assets/code/data-plane/projects/03-ring-buffer/ring.c' | relative_url }}) |
| `Makefile` | [Makefile]({{ '/assets/code/data-plane/projects/03-ring-buffer/Makefile' | relative_url }}) |
