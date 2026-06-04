/**
 * atomic_stats.c — Module 13: Atomic Counters + Per-lcore Stats
 *
 * At line rate, every packet that passes through the pipeline increments
 * one or more counters: received, transmitted, dropped, DNS, TLS, blocked,
 * sinkholes, Hyperscan scans. These counters must be updated without locks —
 * a mutex around a counter in the hot path would serialize all worker lcores
 * onto a single point of contention and destroy throughput.
 *
 * Solution: C11 atomic types (_Atomic) with per-lcore structs.
 *
 * In the real DP application project (domain_scan.h):
 *
 *   extern atomic_ullong hs_db_compile_count;
 *   extern atomic_ullong hs_scratch_alloc_count;
 *   extern atomic_ulong  match_count;
 *   extern atomic_ulong  dns_rx_count;
 *   extern atomic_ulong  dns_proc_count;
 *
 * In policy_cache.c:
 *
 *   atomic_ulong malicious_domain_count;
 *
 * These are globals incremented by any lcore. Per-lcore stats in the worker
 * context (pkt_rx, pkt_tx, pkt_drop) use the same pattern but are only
 * written by their own lcore — no contention, faster still.
 *
 * This module is PURE C — compiles and runs without DPDK.
 * Build: make
 * Run:   ./atomic_stats
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdatomic.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>
#include <assert.h>
#include <inttypes.h>

/* ───────────────────────────────────────────────────────────
 * Cache line size — same value as RTE_CACHE_LINE_SIZE in DPDK
 * ─────────────────────────────────────────────────────────── */
#define CACHE_LINE_SIZE   64

/* ───────────────────────────────────────────────────────────
 * lcore_stats_t — per-lcore statistics struct
 *
 * CRITICAL DESIGN RULE: each lcore's stats struct must be aligned
 * to its own cache line. Without this, two adjacent lcore stats
 * share a cache line — when lcore 3 writes pkt_rx, the CPU
 * invalidates the line on lcore 4's core, causing lcore 4 to stall
 * on its next write even though it's writing a completely different counter.
 *
 * This is false sharing — Module 03 introduced the concept for ring
 * head/tail; here it applies to the entire stats struct array.
 *
 * __attribute__((aligned(64))) ensures each array element starts at
 * a 64-byte boundary. DPDK uses __rte_cache_aligned for the same purpose.
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    /* ── Packet flow counters ── */
    atomic_ulong pkt_rx;         /* received from NIC                      */
    atomic_ulong pkt_tx;         /* forwarded to NIC TX                    */
    atomic_ulong pkt_drop;       /* dropped (policy, ring full, malformed) */

    /* ── Protocol counters ── */
    atomic_ulong pkt_ipv4;
    atomic_ulong pkt_ipv6;
    atomic_ulong pkt_dns;        /* UDP dst_port==53                       */
    atomic_ulong pkt_tls;        /* TCP dst_port==443 with ClientHello     */

    /* ── Policy counters ── */
    atomic_ulong policy_allow;
    atomic_ulong policy_block;
    atomic_ulong policy_sinkhole;

    /* ── Hyperscan counters (mirrors domain_scan.h globals per-lcore) ── */
    atomic_ulong hs_scans;       /* total hs_scan_payload() calls          */
    atomic_ulong hs_matches;     /* total Hyperscan pattern matches        */

    /* ── byte counters ── */
    atomic_ulong bytes_rx;
    atomic_ulong bytes_tx;

    /*
     * Pad to fill the cache line. sizeof all atomics above:
     * 14 × sizeof(atomic_ulong) = 14 × 8 = 112 bytes on 64-bit.
     * Next multiple of 64 = 128 bytes. Pad 16 bytes.
     *
     * In DPDK this is done automatically by __rte_cache_aligned on
     * the struct + RTE_CACHE_LINE_ROUNDUP on the size.
     */
    uint8_t _pad[16];

} __attribute__((aligned(CACHE_LINE_SIZE))) lcore_stats_t;

/* ───────────────────────────────────────────────────────────
 * Global stats — incremented from any lcore
 *
 * These mirror the globals in domain_scan.h / policy_cache.c.
 * Unlike per-lcore stats, these have contention between all lcores.
 * Keep the number of globals small and increment them only on
 * infrequent events (DB compilation, scratch allocation, etc.)
 * ─────────────────────────────────────────────────────────── */
atomic_ullong hs_db_compile_count;      /* incremented when a Hyperscan DB is compiled */
atomic_ullong hs_scratch_alloc_count;   /* incremented per scratch alloc per lcore     */
atomic_ulong  dns_rx_count;     /* DNS packets that entered Hyperscan scan     */
atomic_ulong  dns_proc_count;    /* DNS packets where Hyperscan returned result */
atomic_ulong  malicious_domain_count; /* domains loaded from threat feed      */

/* ───────────────────────────────────────────────────────────
 * Aggregated stats snapshot (plain, non-atomic, point-in-time)
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    unsigned long pkt_rx;
    unsigned long pkt_tx;
    unsigned long pkt_drop;
    unsigned long pkt_dns;
    unsigned long pkt_tls;
    unsigned long policy_allow;
    unsigned long policy_block;
    unsigned long policy_sinkhole;
    unsigned long hs_scans;
    unsigned long hs_matches;
    unsigned long bytes_rx;
    unsigned long bytes_tx;
    uint64_t      timestamp_ns;
} stats_snapshot_t;

/* ───────────────────────────────────────────────────────────
 * stats_aggregate — sum all per-lcore stats into a snapshot
 *
 * Called from the main lcore control loop, typically every second.
 * Uses memory_order_relaxed for reads: we don't need strict ordering
 * here — a stats read that sees a value 1 microsecond stale is fine.
 * ─────────────────────────────────────────────────────────── */
static void stats_aggregate(const lcore_stats_t *all, int n,
                             stats_snapshot_t *out)
{
    memset(out, 0, sizeof(*out));

    for (int i = 0; i < n; i++) {
        const lcore_stats_t *s = &all[i];

        /*
         * memory_order_relaxed: no synchronisation or ordering guarantee.
         * Just atomicity — the load sees a complete write, not a torn value.
         * This is sufficient for stats: we don't need to see the LATEST value,
         * just a coherent value. Using memory_order_seq_cst here would add
         * a full memory fence on every read — unnecessary overhead.
         */
        out->pkt_rx        += atomic_load_explicit(&s->pkt_rx,       memory_order_relaxed);
        out->pkt_tx        += atomic_load_explicit(&s->pkt_tx,       memory_order_relaxed);
        out->pkt_drop      += atomic_load_explicit(&s->pkt_drop,     memory_order_relaxed);
        out->pkt_dns       += atomic_load_explicit(&s->pkt_dns,      memory_order_relaxed);
        out->pkt_tls       += atomic_load_explicit(&s->pkt_tls,      memory_order_relaxed);
        out->policy_allow  += atomic_load_explicit(&s->policy_allow, memory_order_relaxed);
        out->policy_block  += atomic_load_explicit(&s->policy_block, memory_order_relaxed);
        out->policy_sinkhole += atomic_load_explicit(&s->policy_sinkhole, memory_order_relaxed);
        out->hs_scans      += atomic_load_explicit(&s->hs_scans,     memory_order_relaxed);
        out->hs_matches    += atomic_load_explicit(&s->hs_matches,   memory_order_relaxed);
        out->bytes_rx      += atomic_load_explicit(&s->bytes_rx,     memory_order_relaxed);
        out->bytes_tx      += atomic_load_explicit(&s->bytes_tx,     memory_order_relaxed);
    }

    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    out->timestamp_ns = (uint64_t)ts.tv_sec * 1000000000ULL + ts.tv_nsec;
}

/* ───────────────────────────────────────────────────────────
 * stats_print_rates — calculate per-second rates from two snapshots
 *
 * Called every second from the main lcore. The delta between two
 * snapshots divided by the interval gives the rate.
 * ─────────────────────────────────────────────────────────── */
static void stats_print_rates(const stats_snapshot_t *prev,
                               const stats_snapshot_t *curr)
{
    double dt_sec = (double)(curr->timestamp_ns - prev->timestamp_ns) / 1e9;
    if (dt_sec < 0.001) return;

    double rx_pps    = (curr->pkt_rx   - prev->pkt_rx)   / dt_sec;
    double tx_pps    = (curr->pkt_tx   - prev->pkt_tx)   / dt_sec;
    double drop_pps  = (curr->pkt_drop - prev->pkt_drop) / dt_sec;
    double dns_pps   = (curr->pkt_dns  - prev->pkt_dns)  / dt_sec;
    double mbps_rx   = (double)(curr->bytes_rx - prev->bytes_rx) * 8 / dt_sec / 1e6;

    printf("[Stats] rx=%-8.0f/s  tx=%-8.0f/s  drop=%-6.0f/s  "
           "dns=%-6.0f/s  %.1f Mbps\n",
           rx_pps, tx_pps, drop_pps, dns_pps, mbps_rx);
}

static void stats_print_totals(const stats_snapshot_t *s)
{
    printf("\n[Totals]\n");
    printf("  rx          : %lu  tx: %lu  drop: %lu\n",
           s->pkt_rx, s->pkt_tx, s->pkt_drop);
    printf("  dns         : %lu  tls: %lu\n", s->pkt_dns, s->pkt_tls);
    printf("  allow       : %lu  block: %lu  sinkhole: %lu\n",
           s->policy_allow, s->policy_block, s->policy_sinkhole);
    printf("  hs_scans    : %lu  hs_matches: %lu\n",
           s->hs_scans, s->hs_matches);
    printf("  bytes_rx    : %lu  bytes_tx: %lu\n",
           s->bytes_rx, s->bytes_tx);
    printf("  hs_db_compile_count    : %llu\n",
           atomic_load(&hs_db_compile_count));
    printf("  hs_scratch_alloc_count : %llu\n",
           atomic_load(&hs_scratch_alloc_count));
    printf("  dns_rx_count   : %lu\n",
           atomic_load(&dns_rx_count));
    printf("  malicious_domain_count  : %lu\n",
           atomic_load(&malicious_domain_count));
}

/* ═══════════════════════════════════════════════════════════
 * Simulation: worker threads increment stats
 *
 * Each thread simulates one worker lcore.
 * Runs for WORKER_DURATION_MS milliseconds then exits.
 * ═══════════════════════════════════════════════════════════ */
#define NUM_WORKERS         4
#define WORKER_DURATION_MS  2000
#define SIMULATED_PKT_SIZE  512   /* bytes per simulated packet */

typedef struct {
    lcore_stats_t *my_stats;   /* pointer to this worker's stats entry */
    int            worker_id;
} worker_arg_t;

static void *worker_thread(void *arg)
{
    worker_arg_t  *wa    = (worker_arg_t *)arg;
    lcore_stats_t *stats = wa->my_stats;
    int            id    = wa->worker_id;

    struct timespec stop;
    clock_gettime(CLOCK_MONOTONIC, &stop);
    stop.tv_nsec += WORKER_DURATION_MS * 1000000LL;
    if (stop.tv_nsec >= 1000000000LL) {
        stop.tv_sec++;
        stop.tv_nsec -= 1000000000LL;
    }

    unsigned long iterations = 0;

    while (1) {
        /* Check time */
        struct timespec now;
        clock_gettime(CLOCK_MONOTONIC, &now);
        if (now.tv_sec > stop.tv_sec ||
            (now.tv_sec == stop.tv_sec && now.tv_nsec >= stop.tv_nsec))
            break;

        /* Simulate processing a burst of 32 packets */
        for (int i = 0; i < 32; i++) {
            /*
             * memory_order_relaxed for per-lcore counters:
             * Only THIS thread writes these counters (no contention).
             * We just need the increment to be atomic to prevent torn
             * writes visible to the main thread's stats_aggregate().
             *
             * In DPDK, single-writer counters sometimes use plain
             * non-atomic increments with an explicit fence before
             * the main lcore reads — but C11 atomics are cleaner.
             */
            atomic_fetch_add_explicit(&stats->pkt_rx, 1, memory_order_relaxed);
            atomic_fetch_add_explicit(&stats->bytes_rx, SIMULATED_PKT_SIZE,
                                      memory_order_relaxed);

            /* Simulate 70% DNS, 20% TLS, 10% other */
            int r = (iterations * 17 + i * 7 + id * 3) % 10;
            if (r < 7) {
                atomic_fetch_add_explicit(&stats->pkt_dns, 1, memory_order_relaxed);
                atomic_fetch_add_explicit(&stats->hs_scans, 1, memory_order_relaxed);

                /* Also increment global counter (all workers write this) */
                atomic_fetch_add_explicit(&dns_rx_count, 1,
                                          memory_order_relaxed);

                /* Simulate 5% block rate */
                if (r == 0) {
                    atomic_fetch_add_explicit(&stats->policy_block, 1,
                                              memory_order_relaxed);
                    atomic_fetch_add_explicit(&stats->pkt_drop, 1,
                                              memory_order_relaxed);
                } else if (r == 1) {
                    atomic_fetch_add_explicit(&stats->policy_sinkhole, 1,
                                              memory_order_relaxed);
                    atomic_fetch_add_explicit(&stats->pkt_tx, 1,
                                              memory_order_relaxed);
                    atomic_fetch_add_explicit(&stats->bytes_tx,
                                              SIMULATED_PKT_SIZE,
                                              memory_order_relaxed);
                } else {
                    atomic_fetch_add_explicit(&stats->policy_allow, 1,
                                              memory_order_relaxed);
                    atomic_fetch_add_explicit(&stats->pkt_tx, 1,
                                              memory_order_relaxed);
                    atomic_fetch_add_explicit(&stats->bytes_tx,
                                              SIMULATED_PKT_SIZE,
                                              memory_order_relaxed);
                }

                atomic_fetch_add_explicit(&dns_proc_count, 1,
                                          memory_order_relaxed);
            } else if (r < 9) {
                atomic_fetch_add_explicit(&stats->pkt_tls, 1,
                                          memory_order_relaxed);
                atomic_fetch_add_explicit(&stats->hs_scans, 1,
                                          memory_order_relaxed);
                atomic_fetch_add_explicit(&stats->policy_allow, 1,
                                          memory_order_relaxed);
                atomic_fetch_add_explicit(&stats->pkt_tx, 1,
                                          memory_order_relaxed);
                atomic_fetch_add_explicit(&stats->bytes_tx,
                                          SIMULATED_PKT_SIZE * 10,
                                          memory_order_relaxed);
            } else {
                /* other IP traffic */
                atomic_fetch_add_explicit(&stats->policy_allow, 1,
                                          memory_order_relaxed);
                atomic_fetch_add_explicit(&stats->pkt_tx, 1,
                                          memory_order_relaxed);
            }
        }
        iterations++;
    }

    return NULL;
}

/* ═══════════════════════════════════════════════════════════
 * Demo 1: memory ordering — show the difference between orderings
 * ═══════════════════════════════════════════════════════════ */
static void demo_memory_ordering(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 1: Memory ordering for counters\n");
    printf("══════════════════════════════════════════════\n\n");

    atomic_ulong counter = 0;

    /*
     * memory_order_relaxed: atomicity guaranteed, no ordering constraints.
     * Use for: stats counters, reference counts (increment side).
     * Fastest — no fence instruction emitted on x86.
     */
    atomic_fetch_add_explicit(&counter, 1, memory_order_relaxed);
    printf("  relaxed add (stats hot path):    counter = %lu\n",
           atomic_load_explicit(&counter, memory_order_relaxed));

    /*
     * memory_order_release / memory_order_acquire: pair.
     * Use for: publishing data to another thread.
     *   Producer: writes data, then stores flag with RELEASE.
     *   Consumer: loads flag with ACQUIRE, then reads data.
     * Guarantees consumer sees all writes before the RELEASE store.
     *
     * In the DP application this pattern is used in the ring buffer (Module 03)
     * and when signalling workers to stop:
     *   lcore_info->running = 0;  // needs RELEASE semantics
     */
    atomic_ulong flag = 0;
    atomic_store_explicit(&flag, 1, memory_order_release);
    unsigned long seen = atomic_load_explicit(&flag, memory_order_acquire);
    printf("  release/acquire (stop flag):     flag = %lu\n", seen);

    /*
     * memory_order_seq_cst: strongest ordering, full fence.
     * Use for: when you need a globally consistent view across threads.
     * Slowest — emits MFENCE on x86. Avoid in the hot path.
     * Never needed for simple stats counters.
     */
    atomic_ulong sc = 0;
    atomic_fetch_add(&sc, 1);   /* default is seq_cst */
    printf("  seq_cst (default, avoid in hot path): sc = %lu\n\n", atomic_load(&sc));

    printf("  Rule: use relaxed for all stats counters.\n");
    printf("        use release/acquire only for signalling flags.\n\n");
}

/* ═══════════════════════════════════════════════════════════
 * Demo 2: false sharing — measure the cost
 * ═══════════════════════════════════════════════════════════ */
#define FALSE_SHARING_ITERS  50000000

typedef struct {
    atomic_ulong a;
    atomic_ulong b;   /* SHARES a cache line with a — false sharing */
} bad_counters_t;

typedef struct {
    atomic_ulong a __attribute__((aligned(CACHE_LINE_SIZE)));
    atomic_ulong b __attribute__((aligned(CACHE_LINE_SIZE)));
} good_counters_t;

typedef struct {
    void *counters;
    int   which;      /* 0=a, 1=b */
    int   good;       /* 0=bad layout, 1=good layout */
} fs_arg_t;

static void *fs_worker(void *arg)
{
    fs_arg_t *fa = (fs_arg_t *)arg;
    if (fa->good) {
        good_counters_t *c = (good_counters_t *)fa->counters;
        for (int i = 0; i < FALSE_SHARING_ITERS; i++)
            atomic_fetch_add_explicit(fa->which == 0 ? &c->a : &c->b,
                                      1, memory_order_relaxed);
    } else {
        bad_counters_t *c = (bad_counters_t *)fa->counters;
        for (int i = 0; i < FALSE_SHARING_ITERS; i++)
            atomic_fetch_add_explicit(fa->which == 0 ? &c->a : &c->b,
                                      1, memory_order_relaxed);
    }
    return NULL;
}

static double run_false_sharing_test(int good)
{
    pthread_t t1, t2;
    struct timespec t_start, t_end;

    if (good) {
        good_counters_t c = {0, 0};
        fs_arg_t a1 = {&c, 0, 1}, a2 = {&c, 1, 1};
        clock_gettime(CLOCK_MONOTONIC, &t_start);
        pthread_create(&t1, NULL, fs_worker, &a1);
        pthread_create(&t2, NULL, fs_worker, &a2);
        pthread_join(t1, NULL);
        pthread_join(t2, NULL);
        clock_gettime(CLOCK_MONOTONIC, &t_end);
    } else {
        bad_counters_t c = {0, 0};
        fs_arg_t a1 = {&c, 0, 0}, a2 = {&c, 1, 0};
        clock_gettime(CLOCK_MONOTONIC, &t_start);
        pthread_create(&t1, NULL, fs_worker, &a1);
        pthread_create(&t2, NULL, fs_worker, &a2);
        pthread_join(t1, NULL);
        pthread_join(t2, NULL);
        clock_gettime(CLOCK_MONOTONIC, &t_end);
    }

    return ((t_end.tv_sec  - t_start.tv_sec)  * 1e9 +
            (t_end.tv_nsec - t_start.tv_nsec)) / 1e9;
}

static void demo_false_sharing(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 2: False sharing — cache line contention\n");
    printf("══════════════════════════════════════════════\n\n");

    printf("  sizeof(bad_counters_t)  = %zu (fits in 1 cache line = contention)\n",
           sizeof(bad_counters_t));
    printf("  sizeof(good_counters_t) = %zu (each on its own cache line)\n\n",
           sizeof(good_counters_t));

    printf("  Running %d increments per thread, 2 threads...\n",
           FALSE_SHARING_ITERS);

    double bad_time  = run_false_sharing_test(0);
    double good_time = run_false_sharing_test(1);

    printf("  Bad  layout (shared cache line): %.3f sec\n", bad_time);
    printf("  Good layout (aligned, separate): %.3f sec\n", good_time);
    printf("  Speedup: %.1fx\n\n", bad_time / good_time);
    printf("  This is why lcore_stats_t is __attribute__((aligned(64)))\n");
    printf("  and why DPDK uses __rte_cache_aligned on all hot structs.\n\n");
}

/* ═══════════════════════════════════════════════════════════
 * Demo 3: multi-worker simulation + rate stats
 * ═══════════════════════════════════════════════════════════ */
static void demo_live_stats(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 3: live stats from %d simulated workers\n", NUM_WORKERS);
    printf("══════════════════════════════════════════════\n\n");

    /*
     * Allocate per-worker stats as an array.
     * aligned_alloc ensures the array starts at a 64-byte boundary.
     * Since each element is also 64-byte aligned (struct attribute),
     * stats[0], stats[1], ... all land on separate cache lines.
     */
    lcore_stats_t *all_stats = (lcore_stats_t *)aligned_alloc(
        CACHE_LINE_SIZE,
        NUM_WORKERS * sizeof(lcore_stats_t));
    assert(all_stats != NULL);
    memset(all_stats, 0, NUM_WORKERS * sizeof(lcore_stats_t));

    /* Simulate startup: Hyperscan DB compiled and scratch allocated */
    for (int i = 0; i < NUM_WORKERS; i++) {
        atomic_fetch_add(&hs_scratch_alloc_count, 1);
    }
    atomic_fetch_add(&hs_db_compile_count, 1);   /* one global DB compiled */

    /* Load malicious domains from threat feed */
    atomic_store(&malicious_domain_count, 48729);

    /* Launch worker threads */
    pthread_t       threads[NUM_WORKERS];
    worker_arg_t    args[NUM_WORKERS];

    for (int i = 0; i < NUM_WORKERS; i++) {
        args[i].my_stats  = &all_stats[i];
        args[i].worker_id = i;
        pthread_create(&threads[i], NULL, worker_thread, &args[i]);
    }

    /* Main thread: read and print stats every 500ms */
    stats_snapshot_t prev_snap = {0}, curr_snap = {0};
    stats_aggregate(all_stats, NUM_WORKERS, &prev_snap);

    printf("  %-6s  %-12s  %-12s  %-10s  %-10s  %s\n",
           "time", "rx/s", "tx/s", "drop/s", "dns/s", "Mbps");
    printf("  %-6s  %-12s  %-12s  %-10s  %-10s  %s\n",
           "------","------------","------------","----------","----------","----");

    struct timespec t_start, now;
    clock_gettime(CLOCK_MONOTONIC, &t_start);

    for (int tick = 0; tick < 4; tick++) {
        usleep(500000);  /* 500ms */
        stats_aggregate(all_stats, NUM_WORKERS, &curr_snap);

        double dt = (double)(curr_snap.timestamp_ns - prev_snap.timestamp_ns) / 1e9;
        double rx_pps   = (curr_snap.pkt_rx   - prev_snap.pkt_rx)   / dt;
        double tx_pps   = (curr_snap.pkt_tx   - prev_snap.pkt_tx)   / dt;
        double drop_pps = (curr_snap.pkt_drop - prev_snap.pkt_drop) / dt;
        double dns_pps  = (curr_snap.pkt_dns  - prev_snap.pkt_dns)  / dt;
        double mbps     = (double)(curr_snap.bytes_rx - prev_snap.bytes_rx) * 8 / dt / 1e6;

        clock_gettime(CLOCK_MONOTONIC, &now);
        double elapsed = (now.tv_sec - t_start.tv_sec) +
                         (now.tv_nsec - t_start.tv_nsec) / 1e9;

        printf("  %5.1fs  %12.0f  %12.0f  %10.0f  %10.0f  %.1f\n",
               elapsed, rx_pps, tx_pps, drop_pps, dns_pps, mbps);

        prev_snap = curr_snap;
    }

    /* Wait for workers to finish */
    for (int i = 0; i < NUM_WORKERS; i++)
        pthread_join(threads[i], NULL);

    stats_aggregate(all_stats, NUM_WORKERS, &curr_snap);
    stats_print_totals(&curr_snap);

    free(all_stats);
}

/* ═══════════════════════════════════════════════════════════
 * Demo 4: atomic_fetch_add vs mutex — why atomics win
 * ═══════════════════════════════════════════════════════════ */
#define CONTENTION_ITERS  10000000
#define CONTENTION_THREADS 4

typedef struct {
    int             use_mutex;
    pthread_mutex_t *mu;
    unsigned long   *plain_counter;
    atomic_ulong    *atomic_counter;
} contention_arg_t;

static void *contention_worker(void *arg)
{
    contention_arg_t *ca = (contention_arg_t *)arg;
    for (int i = 0; i < CONTENTION_ITERS; i++) {
        if (ca->use_mutex) {
            pthread_mutex_lock(ca->mu);
            (*ca->plain_counter)++;
            pthread_mutex_unlock(ca->mu);
        } else {
            atomic_fetch_add_explicit(ca->atomic_counter, 1,
                                      memory_order_relaxed);
        }
    }
    return NULL;
}

static void demo_atomic_vs_mutex(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 4: atomic vs mutex for shared counter\n");
    printf("══════════════════════════════════════════════\n\n");

    pthread_t        threads[CONTENTION_THREADS];
    contention_arg_t args[CONTENTION_THREADS];
    struct timespec  t0, t1;

    /* ── Mutex version ── */
    pthread_mutex_t mu = PTHREAD_MUTEX_INITIALIZER;
    unsigned long plain = 0;
    for (int i = 0; i < CONTENTION_THREADS; i++) {
        args[i] = (contention_arg_t){1, &mu, &plain, NULL};
    }
    clock_gettime(CLOCK_MONOTONIC, &t0);
    for (int i = 0; i < CONTENTION_THREADS; i++)
        pthread_create(&threads[i], NULL, contention_worker, &args[i]);
    for (int i = 0; i < CONTENTION_THREADS; i++)
        pthread_join(threads[i], NULL);
    clock_gettime(CLOCK_MONOTONIC, &t1);
    double mutex_sec = (t1.tv_sec - t0.tv_sec) +
                       (t1.tv_nsec - t0.tv_nsec) / 1e9;

    /* ── Atomic version ── */
    atomic_ulong ac = 0;
    for (int i = 0; i < CONTENTION_THREADS; i++) {
        args[i] = (contention_arg_t){0, NULL, NULL, &ac};
    }
    clock_gettime(CLOCK_MONOTONIC, &t0);
    for (int i = 0; i < CONTENTION_THREADS; i++)
        pthread_create(&threads[i], NULL, contention_worker, &args[i]);
    for (int i = 0; i < CONTENTION_THREADS; i++)
        pthread_join(threads[i], NULL);
    clock_gettime(CLOCK_MONOTONIC, &t1);
    double atomic_sec = (t1.tv_sec - t0.tv_sec) +
                        (t1.tv_nsec - t0.tv_nsec) / 1e9;

    assert(plain == (unsigned long)CONTENTION_THREADS * CONTENTION_ITERS);
    assert(atomic_load(&ac) == (unsigned long)CONTENTION_THREADS * CONTENTION_ITERS);

    printf("  %d threads × %d increments each:\n",
           CONTENTION_THREADS, CONTENTION_ITERS);
    printf("  mutex:  %.3f sec  (%.0f ns/op)\n",
           mutex_sec, mutex_sec * 1e9 / (CONTENTION_THREADS * CONTENTION_ITERS));
    printf("  atomic: %.3f sec  (%.0f ns/op)\n",
           atomic_sec, atomic_sec * 1e9 / (CONTENTION_THREADS * CONTENTION_ITERS));
    printf("  Speedup: %.1fx\n\n", mutex_sec / atomic_sec);
    printf("  At 2M packets/sec: mutex overhead = %.0f ms/sec,  atomic = %.0f ms/sec\n",
           mutex_sec / (CONTENTION_THREADS * CONTENTION_ITERS) * 2e6 * 1e3,
           atomic_sec / (CONTENTION_THREADS * CONTENTION_ITERS) * 2e6 * 1e3);
    printf("  Mutex makes stats collection a bottleneck; atomic does not.\n\n");
}

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    printf("=== Module 13: Atomic Counters + Per-lcore Stats ===\n\n");
    printf("sizeof(lcore_stats_t) = %zu bytes  "
           "(must be a multiple of %d for alignment)\n\n",
           sizeof(lcore_stats_t), CACHE_LINE_SIZE);

    assert(sizeof(lcore_stats_t) % CACHE_LINE_SIZE == 0);
    printf("Alignment check passed: no two lcore_stats_t share a cache line.\n\n");

    demo_memory_ordering();
    demo_false_sharing();
    demo_atomic_vs_mutex();
    demo_live_stats();

    printf("\n=== All demos complete ===\n");
    printf("\nKey rules for dataplane stats:\n");
    printf("  1. Always use memory_order_relaxed for counters\n");
    printf("  2. Align per-lcore structs to CACHE_LINE_SIZE (64 bytes)\n");
    printf("  3. Never use mutex in the hot path — use atomics\n");
    printf("  4. Global counters (cross-lcore) have contention — keep them rare\n");
    printf("  5. Per-lcore counters (one writer) have zero contention\n");
    return 0;
}
