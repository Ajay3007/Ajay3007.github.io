/**
 * ring.c — Module 03: Ring Buffer (SPSC, lock-free)
 *
 * Implements a lock-free Single-Producer Single-Consumer ring buffer —
 * the manual equivalent of DPDK's rte_ring.
 *
 * In the DP application:
 *   - RX lcore  → ring → worker lcores  (distribute received packets)
 *   - worker    → ring → TX lcore       (forward processed packets)
 *
 * rte_ring handles MPMC (multiple producers/consumers) with CAS atomics.
 * The SPSC case here is simpler: no CAS needed. Just a producer index
 * (head) and a consumer index (tail) with acquire/release barriers to
 * prevent the CPU from reordering reads and writes across cores.
 *
 * Why memory barriers matter (even on x86):
 *   Without barriers, the CPU or compiler can reorder:
 *   1. Producer writes data to entries[head & mask]
 *   2. Producer increments head
 *   If step 2 is visible to the consumer before step 1, the consumer
 *   reads a slot that hasn't been filled yet — silent data corruption.
 *   __ATOMIC_RELEASE on the head store and __ATOMIC_ACQUIRE on the
 *   head load prevent exactly this reordering.
 */

#include "ring.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <stdint.h>
#include <inttypes.h>
#include <assert.h>
#include <unistd.h>    /* usleep */

/* ───────────────────────────────────────────────────────────
 * Internal helpers
 * ─────────────────────────────────────────────────────────── */

/* Check if n is a non-zero power of 2 */
static int is_power_of_two(uint32_t n)
{
    return (n != 0) && ((n & (n - 1)) == 0);
}

/* ───────────────────────────────────────────────────────────
 * ring_create
 * ─────────────────────────────────────────────────────────── */
ring_t *ring_create(uint32_t size)
{
    ring_t *r;

    if (!is_power_of_two(size)) {
        fprintf(stderr, "[ring] size %u is not a power of 2\n", size);
        return NULL;
    }

    r = calloc(1, sizeof(ring_t));
    if (!r)
        return NULL;

    r->entries = calloc(size, sizeof(void *));
    if (!r->entries) {
        free(r);
        return NULL;
    }

    r->size = size;
    r->mask = size - 1;   /* e.g. size=1024 → mask=0x3FF */
    r->head = 0;
    r->tail = 0;

    return r;
}

/* ───────────────────────────────────────────────────────────
 * ring_destroy
 * ─────────────────────────────────────────────────────────── */
void ring_destroy(ring_t *r)
{
    if (!r)
        return;
    free(r->entries);
    free(r);
}

/* ───────────────────────────────────────────────────────────
 * ring_enqueue — producer side
 *
 * Step-by-step:
 *  1. Load tail with ACQUIRE to get latest consumer position.
 *  2. Check if ring is full: full when (head - tail) == size - 1.
 *     We reserve one slot as a sentinel so head == tail means EMPTY,
 *     not ambiguous full-or-empty.
 *  3. Write obj into entries[head & mask].
 *  4. Store incremented head with RELEASE so the consumer sees
 *     the entry write (step 3) before it sees the new head.
 * ─────────────────────────────────────────────────────────── */
int ring_enqueue(ring_t *r, void *obj)
{
    uint32_t head, tail, next;

    head = r->head;   /* only producer touches head — no atomic load needed */
    tail = __atomic_load_n(&r->tail, __ATOMIC_ACQUIRE);

    /* full: head is (size-1) ahead of tail */
    if (((head - tail) & r->mask) == (r->size - 1))
        return RING_FULL;

    next = (head + 1) & r->mask;  /* wraps around via mask */
    r->entries[head & r->mask] = obj;

    /*
     * RELEASE barrier: ensures the entry write above is globally
     * visible to other cores BEFORE the head update below.
     * Without this, the consumer might see head advanced but read
     * a stale (unwritten) entry.
     */
    __atomic_store_n(&r->head, next, __ATOMIC_RELEASE);
    return RING_OK;
}

/* ───────────────────────────────────────────────────────────
 * ring_dequeue — consumer side
 *
 * Step-by-step:
 *  1. Load head with ACQUIRE to see any new entries from producer.
 *  2. Check empty: head == tail means nothing to read.
 *  3. Read entry from entries[tail & mask].
 *  4. Store incremented tail with RELEASE so the producer sees
 *     the slot is free before reusing it.
 * ─────────────────────────────────────────────────────────── */
int ring_dequeue(ring_t *r, void **obj)
{
    uint32_t head, tail, next;

    tail = r->tail;   /* only consumer touches tail */
    head = __atomic_load_n(&r->head, __ATOMIC_ACQUIRE);

    if (head == tail)
        return RING_EMPTY;

    *obj = r->entries[tail & r->mask];

    next = (tail + 1) & r->mask;
    __atomic_store_n(&r->tail, next, __ATOMIC_RELEASE);
    return RING_OK;
}

/* ───────────────────────────────────────────────────────────
 * ring_enqueue_burst — enqueue up to 'count' items
 * Returns number actually enqueued (stops when ring is full).
 * ─────────────────────────────────────────────────────────── */
uint32_t ring_enqueue_burst(ring_t *r, void **objs, uint32_t count)
{
    uint32_t i;
    for (i = 0; i < count; i++) {
        if (ring_enqueue(r, objs[i]) != RING_OK)
            break;
    }
    return i;
}

/* ───────────────────────────────────────────────────────────
 * ring_dequeue_burst — dequeue up to 'count' items
 * Returns number actually dequeued (stops when ring is empty).
 * ─────────────────────────────────────────────────────────── */
uint32_t ring_dequeue_burst(ring_t *r, void **objs, uint32_t count)
{
    uint32_t i;
    for (i = 0; i < count; i++) {
        if (ring_dequeue(r, &objs[i]) != RING_OK)
            break;
    }
    return i;
}

/* ═══════════════════════════════════════════════════════════
 * Demo — simulates the RX lcore → worker lcore pipeline
 *
 * Two pthreads share a ring:
 *   producer: simulates RX lcore enqueuing "packet pointers"
 *   consumer: simulates worker lcore dequeuing and processing
 *
 * In the real DPDK app:
 *   - The ring holds rte_mbuf* pointers, not int*
 *   - The "threads" are DPDK lcores pinned to physical CPU cores
 *   - The ring is created with rte_ring_create() instead of ring_create()
 *   - The producer calls rte_eth_rx_burst() to fill packets
 * ═══════════════════════════════════════════════════════════ */

#define DEMO_RING_SIZE    256     /* must be power of 2            */
#define DEMO_TOTAL_PKTS   1000   /* total "packets" to pass through */
#define DEMO_BURST_SIZE   16     /* match DPDK's typical burst size */

/* Shared state between producer and consumer threads */
typedef struct {
    ring_t   *ring;
    uint32_t  total;           /* total items to produce/consume */
    uint64_t  consumed_sum;    /* checksum to verify no drops/corruption */
} demo_state_t;

/* Producer thread — simulates RX lcore */
static void *producer_thread(void *arg)
{
    demo_state_t *s = (demo_state_t *)arg;
    uint32_t i;

    printf("[producer] Starting: will enqueue %u items in bursts of %d\n",
           s->total, DEMO_BURST_SIZE);

    for (i = 0; i < s->total; ) {
        /*
         * In a real RX lcore, here we'd call:
         *   nb_rx = rte_eth_rx_burst(port_id, queue_id, mbufs, BURST_SIZE);
         * and then enqueue the mbufs. We simulate packet pointers with
         * heap-allocated ints.
         */
        void *burst[DEMO_BURST_SIZE];
        uint32_t burst_sz = 0;
        uint32_t j;

        /* Build a burst of "packets" */
        for (j = 0; j < DEMO_BURST_SIZE && i < s->total; j++, i++) {
            int *pkt = malloc(sizeof(int));
            *pkt = i;   /* packet "sequence number" */
            burst[burst_sz++] = pkt;
        }

        /* Enqueue burst — busy-retry if ring is full */
        uint32_t sent = 0;
        while (sent < burst_sz) {
            uint32_t n = ring_enqueue_burst(s->ring,
                                             burst + sent,
                                             burst_sz - sent);
            sent += n;
            if (n == 0)
                /* Ring full — in DPDK you'd free the dropped mbufs here */
                usleep(1);
        }
    }

    printf("[producer] Done: enqueued %u items\n", s->total);
    return NULL;
}

/* Consumer thread — simulates worker lcore */
static void *consumer_thread(void *arg)
{
    demo_state_t *s = (demo_state_t *)arg;
    uint32_t received = 0;
    void    *burst[DEMO_BURST_SIZE];

    printf("[consumer] Starting: waiting for items\n");

    while (received < s->total) {
        /*
         * In a real worker lcore, here we'd call:
         *   nb = rte_ring_dequeue_burst(ring, (void**)mbufs, BURST_SIZE, NULL);
         * and then run each mbuf through the policy engine:
         *   process_dns_for_group(mbufs[i], worker_info, ...)
         */
        uint32_t nb = ring_dequeue_burst(s->ring, burst, DEMO_BURST_SIZE);

        uint32_t i;
        for (i = 0; i < nb; i++) {
            int *pkt = (int *)burst[i];
            s->consumed_sum += *pkt;   /* checksum verification */
            free(pkt);
            received++;
        }

        if (nb == 0)
            usleep(1);   /* ring empty — yield (DPDK polls without sleep) */
    }

    printf("[consumer] Done: received %u items\n", received);
    return NULL;
}

/* ─── Functional tests ──────────────────────────────────── */

static void test_basic(void)
{
    printf("\n--- Test 1: basic enqueue/dequeue ---\n");

    ring_t *r = ring_create(8);
    assert(r != NULL);
    assert(ring_is_empty(r));

    /* enqueue 3 items */
    int a = 10, b = 20, c = 30;
    assert(ring_enqueue(r, &a) == RING_OK);
    assert(ring_enqueue(r, &b) == RING_OK);
    assert(ring_enqueue(r, &c) == RING_OK);
    assert(ring_count(r) == 3);

    /* dequeue and verify order (FIFO) */
    void *out;
    assert(ring_dequeue(r, &out) == RING_OK); assert(*(int*)out == 10);
    assert(ring_dequeue(r, &out) == RING_OK); assert(*(int*)out == 20);
    assert(ring_dequeue(r, &out) == RING_OK); assert(*(int*)out == 30);
    assert(ring_is_empty(r));

    printf("  PASS: FIFO order preserved\n");
    ring_destroy(r);
}

static void test_full(void)
{
    printf("--- Test 2: ring full behaviour ---\n");

    /* size=4 → max 3 entries (1 slot reserved as sentinel) */
    ring_t *r = ring_create(4);
    assert(r != NULL);

    int vals[4] = {1, 2, 3, 4};
    assert(ring_enqueue(r, &vals[0]) == RING_OK);
    assert(ring_enqueue(r, &vals[1]) == RING_OK);
    assert(ring_enqueue(r, &vals[2]) == RING_OK);
    assert(ring_is_full(r));
    assert(ring_enqueue(r, &vals[3]) == RING_FULL);  /* must reject */

    printf("  PASS: RING_FULL returned correctly\n");
    ring_destroy(r);
}

static void test_empty(void)
{
    printf("--- Test 3: ring empty behaviour ---\n");

    ring_t *r = ring_create(4);
    void *out;
    assert(ring_dequeue(r, &out) == RING_EMPTY);
    printf("  PASS: RING_EMPTY returned on empty ring\n");
    ring_destroy(r);
}

static void test_wrap(void)
{
    printf("--- Test 4: index wraparound ---\n");

    ring_t *r = ring_create(4);
    int vals[8];
    int i;

    /* Fill and drain multiple times to force index wraparound */
    for (i = 0; i < 8; i++) {
        vals[i] = i * 100;
        assert(ring_enqueue(r, &vals[i]) == RING_OK);
        void *out;
        assert(ring_dequeue(r, &out) == RING_OK);
        assert(*(int*)out == i * 100);
    }

    printf("  PASS: head/tail wrapped around correctly\n");
    ring_destroy(r);
}

static void test_concurrent(void)
{
    printf("--- Test 5: concurrent producer/consumer ---\n");

    demo_state_t state = {
        .ring         = ring_create(DEMO_RING_SIZE),
        .total        = DEMO_TOTAL_PKTS,
        .consumed_sum = 0,
    };
    assert(state.ring != NULL);

    pthread_t prod, cons;
    pthread_create(&prod, NULL, producer_thread, &state);
    pthread_create(&cons, NULL, consumer_thread, &state);
    pthread_join(prod, NULL);
    pthread_join(cons, NULL);

    /* Verify no items were dropped or corrupted:
     * sum(0..999) = 999*1000/2 = 499500 */
    uint64_t expected = (uint64_t)(DEMO_TOTAL_PKTS - 1) * DEMO_TOTAL_PKTS / 2;
    printf("  consumed_sum = %" PRIu64 "  expected = %" PRIu64 "\n",
           state.consumed_sum, expected);
    assert(state.consumed_sum == expected);

    printf("  PASS: all items delivered, no drops, no corruption\n");
    ring_destroy(state.ring);
}

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    printf("=== Module 03: Ring Buffer (SPSC) ===\n");
    printf("ring_t size: %zu bytes\n\n", sizeof(ring_t));

    test_basic();
    test_full();
    test_empty();
    test_wrap();
    test_concurrent();

    printf("\nAll tests passed.\n");
    printf("\n--- How this maps to DPDK rte_ring ---\n");
    printf("  ring_create(size)         →  rte_ring_create(name, size, socket, flags)\n");
    printf("  ring_enqueue(r, obj)      →  rte_ring_enqueue(r, obj)\n");
    printf("  ring_dequeue(r, &obj)     →  rte_ring_dequeue(r, &obj)\n");
    printf("  ring_enqueue_burst(...)   →  rte_ring_enqueue_burst(...)\n");
    printf("  ring_dequeue_burst(...)   →  rte_ring_dequeue_burst(...)\n");
    printf("  mask = size-1 trick       →  identical in rte_ring source\n");
    printf("  __ATOMIC_RELEASE/ACQUIRE  →  rte_smp_wmb()/rte_smp_rmb()\n");

    return 0;
}
