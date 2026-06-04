/**
 * ring.h — Module 03: Ring Buffer (SPSC, lock-free)
 *
 * A ring buffer (circular queue) is the primary inter-lcore communication
 * mechanism in a DPDK application. In the DP application it is used to hand packets
 * from the RX lcore to worker lcores, and from worker lcores to the TX lcore.
 *
 * DPDK's rte_ring is a production-grade MPMC (Multi-Producer Multi-Consumer)
 * ring. This module implements the simpler SPSC (Single-Producer Single-Consumer)
 * variant first — same idea, no CAS atomics needed, easier to understand.
 *
 * Once you understand this, rte_ring's enqueue/dequeue source is immediately
 * readable. The core insight — power-of-2 size + head/tail indices +
 * acquire/release memory ordering — is identical.
 *
 * SPSC contract:
 *   - Exactly ONE thread calls ring_enqueue()  (the producer)
 *   - Exactly ONE thread calls ring_dequeue()  (the consumer)
 *   - No mutex needed — only memory barriers
 */

#ifndef RING_H
#define RING_H

#include <stdint.h>
#include <stddef.h>

/* ───────────────────────────────────────────────────────────
 * Cache line size.
 *
 * On x86_64 a cache line is 64 bytes. Putting head and tail on
 * the SAME cache line causes "false sharing": when the producer
 * writes head, the CPU invalidates the cache line on the consumer's
 * core even though the consumer only reads tail — and vice versa.
 * This serialises the two cores and destroys throughput.
 *
 * Solution: align each to its own cache line (see ring_t below).
 * rte_ring does exactly this with __rte_cache_aligned.
 * ─────────────────────────────────────────────────────────── */
#define RING_CACHE_LINE_SIZE  64

/* ───────────────────────────────────────────────────────────
 * Return codes
 * ─────────────────────────────────────────────────────────── */
#define RING_OK       0
#define RING_FULL    -1
#define RING_EMPTY   -2
#define RING_EINVAL  -3

/* ───────────────────────────────────────────────────────────
 * ring_t — the ring buffer structure.
 *
 * Layout mirrors rte_ring: prod and cons each on their own cache
 * line so producer and consumer cores never share a cache line.
 *
 * entries[] is an array of void* — just like rte_ring stores
 * pointers to rte_mbuf objects. The ring owns the slot array
 * but NOT the objects pointed to.
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    /* --- producer state: only the producer core writes here --- */
    uint32_t  head        __attribute__((aligned(RING_CACHE_LINE_SIZE)));

    /* --- consumer state: only the consumer core writes here --- */
    uint32_t  tail        __attribute__((aligned(RING_CACHE_LINE_SIZE)));

    /* --- read-only after init: shared safely without barriers --- */
    uint32_t  size;       /* total capacity, must be power of 2   */
    uint32_t  mask;       /* size - 1, used instead of % operator */
    void    **entries;    /* pointer array of length 'size'        */
} ring_t;

/* ─── Public API ─────────────────────────────────────────── */

/**
 * ring_create — allocate a ring buffer of 'size' slots.
 *
 * 'size' MUST be a power of 2 (64, 128, 256, 512, 1024, ...).
 * Power-of-2 allows replacing the expensive `% size` with `& mask`
 * — same trick rte_ring uses.
 *
 * In the real app, ring sizes come from config:
 *   uint32_t ring_size = config_get_int(&cfg, "worker", "ring_size", 1024);
 *   ring_t *r = ring_create(ring_size);
 *
 * Returns pointer on success, NULL on failure.
 */
ring_t *ring_create(uint32_t size);

/**
 * ring_destroy — free the ring buffer.
 * Does NOT free the objects pointed to by entries[].
 */
void ring_destroy(ring_t *r);

/**
 * ring_enqueue — add one pointer to the ring (producer side).
 *
 * Called ONLY from the producer thread/lcore.
 * In the real app this is called on the RX lcore after
 * rte_eth_rx_burst() fills an array of rte_mbuf pointers.
 *
 * Returns RING_OK on success, RING_FULL if no space.
 */
int ring_enqueue(ring_t *r, void *obj);

/**
 * ring_dequeue — remove one pointer from the ring (consumer side).
 *
 * Called ONLY from the consumer thread/lcore.
 * In the real app this is called at the top of the worker lcore's
 * main loop to fetch the next mbuf to process.
 *
 * Returns RING_OK and sets *obj on success, RING_EMPTY if nothing
 * available.
 */
int ring_dequeue(ring_t *r, void **obj);

/**
 * ring_enqueue_burst — enqueue up to 'count' pointers from array[].
 *
 * Mirrors rte_ring_enqueue_burst(). Returns the number of objects
 * actually enqueued (may be less than count if ring fills up).
 *
 * In the real app the RX lcore does:
 *   nb_rx = rte_eth_rx_burst(port, queue, mbufs, BURST_SIZE);
 *   nb_sent = ring_enqueue_burst(ring, (void**)mbufs, nb_rx);
 *   // drop mbufs[nb_sent .. nb_rx-1] if ring was full
 */
uint32_t ring_enqueue_burst(ring_t *r, void **objs, uint32_t count);

/**
 * ring_dequeue_burst — dequeue up to 'count' pointers into array[].
 *
 * Mirrors rte_ring_dequeue_burst(). Returns actual count dequeued.
 *
 * In the real app the worker lcore does:
 *   nb = ring_dequeue_burst(ring, (void**)mbufs, BURST_SIZE);
 *   for (i = 0; i < nb; i++) process_packet(mbufs[i]);
 */
uint32_t ring_dequeue_burst(ring_t *r, void **objs, uint32_t count);

/* ─── Inline status helpers ─────────────────────────────── */

static inline uint32_t ring_count(const ring_t *r)
{
    /* acquire load: see the latest head/tail written by the other core */
    uint32_t h = __atomic_load_n(&r->head, __ATOMIC_ACQUIRE);
    uint32_t t = __atomic_load_n(&r->tail, __ATOMIC_ACQUIRE);
    return (h - t) & r->mask;
}

static inline uint32_t ring_free_count(const ring_t *r)
{
    return r->size - 1 - ring_count(r);
}

static inline int ring_is_empty(const ring_t *r)
{
    return __atomic_load_n(&r->head, __ATOMIC_ACQUIRE) ==
           __atomic_load_n(&r->tail, __ATOMIC_ACQUIRE);
}

static inline int ring_is_full(const ring_t *r)
{
    uint32_t h = __atomic_load_n(&r->head, __ATOMIC_ACQUIRE);
    uint32_t t = __atomic_load_n(&r->tail, __ATOMIC_ACQUIRE);
    /* ring is full when head is exactly (size-1) ahead of tail */
    return ((h - t) & r->mask) == (r->size - 1);
}

#endif /* RING_H */
