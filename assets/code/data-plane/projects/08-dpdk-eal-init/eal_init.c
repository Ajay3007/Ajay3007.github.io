/**
 * eal_init.c — Module 08: DPDK EAL Initialization
 *
 * The Environment Abstraction Layer (EAL) is the foundation of every
 * DPDK application. Calling rte_eal_init() does several things at once:
 *
 *   1. Locks hugepage memory (pre-allocated by the OS via dpdk-devbind /
 *      nr_hugepages sysctl). DPDK packet buffers live here — never in
 *      normal heap — so the OS cannot page them out during line-rate RX.
 *
 *   2. Pins lcores (logical CPU cores) to physical CPUs via CPU affinity.
 *      From this point on, the OS scheduler does NOT run anything else on
 *      the cores you handed to DPDK. They spin in tight poll loops.
 *
 *   3. Initialises the per-lcore memory allocator (rte_malloc zone per socket).
 *
 *   4. Probes PCI devices (NIC drivers). If a NIC was bound with
 *      dpdk-devbind --bind=vfio-pci, DPDK takes exclusive control of it.
 *
 *   5. Sets up the service core framework for background tasks.
 *
 * In the real DP project (app_main.c), EAL init is the very first
 * substantial call after config_load(). Everything else — port init,
 * mempool creation, Hyperscan compilation, Kafka init, lcore launch —
 * happens AFTER rte_eal_init() returns.
 *
 * REFERENCE CODE: requires DPDK installed.
 * Build with: make  (see Makefile)
 * Run with:   sudo ./eal_init   (must be root or CAP_NET_ADMIN for hugepages)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <stdatomic.h>

#include <rte_eal.h>
#include <rte_lcore.h>
#include <rte_memory.h>
#include <rte_memzone.h>
#include <rte_launch.h>
#include <rte_cycles.h>
#include <rte_log.h>
#include <rte_errno.h>
#include <rte_ring.h>
#include <rte_version.h>

/* ───────────────────────────────────────────────────────────
 * Lcore role assignment
 *
 * In the DP application each lcore has a fixed role assigned at startup.
 * Mixing roles destroys throughput: if the RX lcore stops polling
 * to run policy logic, the NIC RX ring fills and packets are dropped.
 *
 * Roles come from config (Module 01):
 *   rx_lcore  = 1   (one dedicated RX core per port)
 *   tx_lcore  = 2   (one dedicated TX core per port)
 *   worker_lcores = 3,4,5,6
 * ─────────────────────────────────────────────────────────── */
typedef enum {
    LCORE_ROLE_MAIN    = 0,   /* main thread: init, control, signal handling */
    LCORE_ROLE_RX      = 1,   /* rte_eth_rx_burst loop → enqueue to ring */
    LCORE_ROLE_TX      = 2,   /* dequeue from ring → rte_eth_tx_burst */
    LCORE_ROLE_WORKER  = 3,   /* policy engine: DNS/TLS parsing, Hyperscan */
    LCORE_ROLE_UNUSED  = 4,
} lcore_role_t;

static const char *lcore_role_str(lcore_role_t r) {
    switch (r) {
    case LCORE_ROLE_MAIN:   return "MAIN";
    case LCORE_ROLE_RX:     return "RX";
    case LCORE_ROLE_TX:     return "TX";
    case LCORE_ROLE_WORKER: return "WORKER";
    default:                return "UNUSED";
    }
}

/* ───────────────────────────────────────────────────────────
 * worker_lcore_info — per-lcore state (simplified)
 *
 * In the real DP project this struct is much larger:
 *   - hs_scratch_t *scratch (Hyperscan, Module 21)
 *   - rte_hash *connection_table (per-lcore connection tracking)
 *   - CDR batch buffer
 *   - per-lcore stats counters
 *
 * Every worker function receives a pointer to its own lcore_info.
 * The struct is __rte_cache_aligned so adjacent instances don't
 * share a cache line (false sharing — see Module 03).
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    unsigned int   lcore_id;
    uint16_t       port_id;
    uint16_t       queue_id;     /* NIC queue assigned to this lcore */
    lcore_role_t   role;

    struct rte_ring *rx_ring;    /* RX lcore enqueues here; worker dequeues */
    struct rte_ring *tx_ring;    /* worker enqueues here; TX lcore dequeues */

    /* stats — atomic so main lcore can read without locking */
    atomic_ulong   pkt_rx;
    atomic_ulong   pkt_tx;
    atomic_ulong   pkt_drop;

    volatile int   running;      /* set to 0 to stop this lcore gracefully */
} __rte_cache_aligned worker_lcore_info_t;

#define MAX_LCORES  RTE_MAX_LCORE

static worker_lcore_info_t lcore_info[MAX_LCORES];
static volatile int        force_quit = 0;

/* ───────────────────────────────────────────────────────────
 * Signal handler — graceful shutdown
 *
 * In the real app, SIGTERM / SIGINT stops all worker lcores,
 * flushes CDR batches to Kafka, then calls rte_eal_cleanup().
 * Never call rte_eal_cleanup() from a signal handler directly —
 * set a flag and let main() do it.
 * ─────────────────────────────────────────────────────────── */
static void signal_handler(int signum)
{
    if (signum == SIGINT || signum == SIGTERM) {
        printf("\nSignal %d received, initiating shutdown...\n", signum);
        force_quit = 1;
    }
}

/* ───────────────────────────────────────────────────────────
 * Build EAL argument vector from config values
 *
 * rte_eal_init() takes a traditional (argc, argv) pair — the same
 * format as a command-line invocation. In the real app, app_main.c builds
 * this vector from config values rather than passing them on the shell
 * command line. This gives the application control over EAL options
 * without requiring operators to know DPDK flags.
 *
 * Typical EAL args built here:
 *   ./dp_app
 *     -l 0-7              core list (or -c for hex mask)
 *     --socket-mem 2048   hugepage MB per NUMA socket
 *     -n 4                memory channels (match CPU/board spec)
 *     --proc-type auto    primary or secondary process
 *     --log-level 7       DPDK internal log verbosity
 *     --                  separator before app-specific args
 * ─────────────────────────────────────────────────────────── */
#define MAX_EAL_ARGS  32
#define MAX_ARG_LEN   64

static char   eal_argv_storage[MAX_EAL_ARGS][MAX_ARG_LEN];
static char  *eal_argv[MAX_EAL_ARGS];
static int    eal_argc = 0;

static void eal_add_arg(const char *arg)
{
    if (eal_argc >= MAX_EAL_ARGS) {
        fprintf(stderr, "Too many EAL args\n");
        return;
    }
    strncpy(eal_argv_storage[eal_argc], arg, MAX_ARG_LEN - 1);
    eal_argv[eal_argc] = eal_argv_storage[eal_argc];
    eal_argc++;
}

static int build_eal_args(const char *cores,
                            int         socket_mem_mb,
                            int         mem_channels,
                            int         log_level)
{
    char tmp[64];

    eal_argc = 0;

    eal_add_arg("dp_app");           /* argv[0]: program name */

    eal_add_arg("-l");               /* lcore list */
    eal_add_arg(cores);

    eal_add_arg("--socket-mem");
    snprintf(tmp, sizeof(tmp), "%d", socket_mem_mb);
    eal_add_arg(tmp);

    eal_add_arg("-n");               /* memory channels */
    snprintf(tmp, sizeof(tmp), "%d", mem_channels);
    eal_add_arg(tmp);

    eal_add_arg("--proc-type");
    eal_add_arg("auto");

    eal_add_arg("--log-level");
    snprintf(tmp, sizeof(tmp), "%d", log_level);
    eal_add_arg(tmp);

    /*
     * In production we also add:
     *   --vdev net_pcap0,...  (for virtual NIC in container testing)
     *   --huge-dir /dev/hugepages
     *   --file-prefix dp_app  (for multiple DPDK processes on same host)
     */

    printf("[EAL] Built arg vector (%d args):", eal_argc);
    for (int i = 0; i < eal_argc; i++)
        printf(" %s", eal_argv[i]);
    printf("\n");

    return eal_argc;
}

/* ───────────────────────────────────────────────────────────
 * Lcore role assignment
 *
 * After rte_eal_init(), query which lcores are available and assign
 * roles based on config. In the real app, config specifies:
 *   rx_lcore      = 1
 *   tx_lcore      = 2
 *   worker_lcores = 3,4,5,6
 *
 * Any lcore not assigned to an explicit role should NOT be launched —
 * let it stay idle. Launching an unneeded lcore wastes a core and
 * can cause unexpected behaviour in the ring topology.
 * ─────────────────────────────────────────────────────────── */
static void assign_lcore_roles(unsigned int rx_lcore,
                                 unsigned int tx_lcore)
{
    unsigned int lcore_id;

    /* initialise all to UNUSED */
    RTE_LCORE_FOREACH(lcore_id) {
        lcore_info[lcore_id].lcore_id = lcore_id;
        lcore_info[lcore_id].role     = LCORE_ROLE_UNUSED;
        lcore_info[lcore_id].running  = 0;
    }

    /* main lcore */
    unsigned int main_lcore = rte_get_main_lcore();
    lcore_info[main_lcore].role = LCORE_ROLE_MAIN;

    /* RX lcore */
    if (rte_lcore_is_enabled(rx_lcore)) {
        lcore_info[rx_lcore].role     = LCORE_ROLE_RX;
        lcore_info[rx_lcore].port_id  = 0;
        lcore_info[rx_lcore].queue_id = 0;
        lcore_info[rx_lcore].running  = 1;
    }

    /* TX lcore */
    if (rte_lcore_is_enabled(tx_lcore)) {
        lcore_info[tx_lcore].role     = LCORE_ROLE_TX;
        lcore_info[tx_lcore].port_id  = 0;
        lcore_info[tx_lcore].queue_id = 0;
        lcore_info[tx_lcore].running  = 1;
    }

    /* remaining enabled lcores (not main, RX, TX) → WORKER */
    RTE_LCORE_FOREACH_WORKER(lcore_id) {
        if (lcore_id == rx_lcore || lcore_id == tx_lcore)
            continue;
        lcore_info[lcore_id].role    = LCORE_ROLE_WORKER;
        lcore_info[lcore_id].running = 1;
    }
}

/* ───────────────────────────────────────────────────────────
 * Print lcore topology summary
 *
 * In the real app, this is logged at INFO level right after EAL init
 * so operators can confirm the core assignment before packet processing
 * begins. Seeing the wrong assignment here (e.g., TX lcore unassigned)
 * saves hours of debugging a zero-throughput startup.
 * ─────────────────────────────────────────────────────────── */
static void print_lcore_topology(void)
{
    unsigned int lcore_id;
    unsigned int main_lcore = rte_get_main_lcore();

    printf("\n[Lcore Topology]\n");
    printf("  DPDK version   : %s\n", rte_version());
    printf("  Total lcores   : %u\n", rte_lcore_count());
    printf("  Main lcore     : %u\n", main_lcore);
    printf("  NUMA sockets   : %u\n", rte_socket_count());
    printf("\n");
    printf("  %-8s %-10s %-8s %-6s\n", "lcore", "role", "socket", "enabled");
    printf("  %-8s %-10s %-8s %-6s\n", "-----", "----", "------", "-------");

    RTE_LCORE_FOREACH(lcore_id) {
        printf("  %-8u %-10s %-8u %-6s\n",
               lcore_id,
               lcore_role_str(lcore_info[lcore_id].role),
               rte_lcore_to_socket_id(lcore_id),
               rte_lcore_is_enabled(lcore_id) ? "yes" : "no");
    }
    printf("\n");
}

/* ───────────────────────────────────────────────────────────
 * Print hugepage memory summary
 *
 * This verifies that hugepages are available and correctly allocated
 * across NUMA sockets. If socket 0 has memory but socket 1 has zero,
 * any allocation on socket 1 (e.g., a mempool for a NIC on socket 1)
 * will silently fall back to socket 0, causing cross-NUMA memory
 * accesses — a ~100 ns penalty per packet on high-end servers.
 * ─────────────────────────────────────────────────────────── */
static void print_memory_info(void)
{
    printf("[Memory]\n");

    const struct rte_memseg_list *msl;
    uint32_t i;
    RTE_MEMSEG_LIST_FOREACH(msl) {
        if (!msl->memseg_arr.count)
            continue;
        printf("  socket %d: %zu MB hugepages (%zu-byte pages)\n",
               msl->socket_id,
               (size_t)msl->len / (1024 * 1024),
               (size_t)msl->page_sz);
    }
    printf("\n");
}

/* ───────────────────────────────────────────────────────────
 * Worker lcore function — the skeleton of every worker loop
 *
 * In the real app this is the main loop in pkt_proc.h.
 * The actual function is much larger (policy decisions, CDR, sinkholing)
 * but the outer structure is identical to what's shown here.
 *
 * Critical design rules for lcore functions:
 *   1. NEVER block (no mutexes, no sleep, no syscalls in the hot path)
 *   2. NEVER allocate or free memory in the fast path
 *   3. All inter-lcore communication through rte_ring
 *   4. Check 'running' flag at the top of each iteration for graceful stop
 * ─────────────────────────────────────────────────────────── */
static int lcore_worker_func(void *arg)
{
    worker_lcore_info_t *info = (worker_lcore_info_t *)arg;
    unsigned int         my_lcore = rte_lcore_id();

    printf("[lcore %u] %s started on socket %u\n",
           my_lcore, lcore_role_str(info->role),
           rte_lcore_to_socket_id(my_lcore));

    /*
     * Main processing loop.
     *
     * In the real app, depending on the role:
     *
     *   RX lcore:
     *     nb_rx = rte_eth_rx_burst(port, queue, mbufs, BURST_SIZE);
     *     rte_ring_enqueue_burst(info->rx_ring, (void **)mbufs, nb_rx, NULL);
     *
     *   Worker lcore:
     *     nb = rte_ring_dequeue_burst(info->rx_ring, (void **)mbufs, BURST_SIZE, NULL);
     *     for each mbuf: parse DNS/TLS → policy → sinkhole/forward
     *     rte_ring_enqueue_burst(info->tx_ring, (void **)fwd_mbufs, nb_fwd, NULL);
     *
     *   TX lcore:
     *     nb = rte_ring_dequeue_burst(info->tx_ring, (void **)mbufs, BURST_SIZE, NULL);
     *     rte_eth_tx_burst(port, queue, mbufs, nb);
     */
    uint64_t iterations = 0;

    while (info->running && !force_quit) {
        /* simulated work: real work replaces this */
        iterations++;

        /*
         * rte_pause() is a DPDK wrapper around the x86 PAUSE instruction.
         * It hints the CPU that we're in a spin loop, reducing power
         * consumption slightly and improving hyper-threading performance.
         * Do NOT use sleep() — that yields the core to the OS scheduler.
         */
        rte_pause();

        /* stop after a short demo run */
        if (iterations >= 1000)
            break;
    }

    printf("[lcore %u] %s stopping after %lu iterations\n",
           my_lcore, lcore_role_str(info->role), iterations);
    return 0;
}

/* ───────────────────────────────────────────────────────────
 * main — EAL init + lcore launch sequence
 * ─────────────────────────────────────────────────────────── */
int main(int argc, char *argv[])
{
    int ret;

    signal(SIGINT,  signal_handler);
    signal(SIGTERM, signal_handler);

    printf("=== Module 08: DPDK EAL Init ===\n\n");

    /* ── Step 1: Build EAL args from config ──
     *
     * In app_main.c these values come from config_load() (Module 01).
     * Here we hardcode them for demonstration.
     *
     * "--" separates EAL args from application args.
     * rte_eal_init() returns the index of "--" in argv so the
     * application can parse its own args after it.
     */
    build_eal_args(
        "0-3",   /* cores: 0,1,2,3 */
        1024,    /* socket_mem: 1024 MB (use less for VMs / dev machines) */
        4,       /* memory channels */
        7        /* log level */
    );

    /* ── Step 2: Initialize EAL ──
     *
     * This is the single most important call in the application.
     * On success: hugepages are locked, lcores are pinned, NICs are probed.
     * On failure: rte_exit() is typical (abort + print) — no recovery.
     *
     * rte_eal_init() returns the number of EAL args consumed, so
     * any remaining args (argc - ret, argv + ret) are app-specific.
     */
    ret = rte_eal_init(eal_argc, eal_argv);
    if (ret < 0) {
        rte_exit(EXIT_FAILURE,
                 "rte_eal_init failed: %s\n", rte_strerror(rte_errno));
    }
    printf("[EAL] Initialized. %d EAL args consumed.\n\n", ret);

    /* ── Step 3: Print system topology ── */
    print_lcore_topology();
    print_memory_info();

    /* ── Step 4: Assign roles from config ──
     *
     * In app_main.c:
     *   int rx_lcore = config_get_int(&cfg, "worker", "rx_lcore", 1);
     *   int tx_lcore = config_get_int(&cfg, "worker", "tx_lcore", 2);
     */
    unsigned int rx_lcore = 1;
    unsigned int tx_lcore = 2;
    assign_lcore_roles(rx_lcore, tx_lcore);

    /*
     * Verify role assignment.
     * In the real app, a missing or wrong assignment here means packets
     * will be dropped silently. Always print and validate before launch.
     */
    printf("[Roles assigned]\n");
    printf("  Main   lcore : %u\n", rte_get_main_lcore());
    printf("  RX     lcore : %u\n", rx_lcore);
    printf("  TX     lcore : %u\n", tx_lcore);
    printf("\n");

    /*
     * NOTE: In the real app, between Step 4 and Step 5 you would:
     *   - Create mempools (Module 09)
     *   - Initialize NIC ports (Module 10)
     *   - Compile Hyperscan pattern DB (Module 11)
     *   - Initialize Kafka producer/consumer (Module 12)
     *   - Set up per-lcore rx_ring / tx_ring
     * All of this must happen BEFORE launching worker lcores.
     */

    /* ── Step 5: Launch worker lcores ──
     *
     * rte_eal_remote_launch(func, arg, lcore_id) starts 'func(arg)'
     * on the specified lcore. The lcore must not already be running.
     *
     * The main lcore does NOT call rte_eal_remote_launch on itself —
     * it runs its own loop after launching workers.
     *
     * In app_main.c, after all workers are launched, the main lcore
     * enters a control loop: printing stats, handling Kafka policy
     * updates, responding to OAM commands.
     */
    printf("[Launch] Starting worker lcores...\n");

    unsigned int lcore_id;
    RTE_LCORE_FOREACH_WORKER(lcore_id) {
        if (lcore_info[lcore_id].role == LCORE_ROLE_UNUSED)
            continue;

        ret = rte_eal_remote_launch(lcore_worker_func,
                                     &lcore_info[lcore_id],
                                     lcore_id);
        if (ret != 0) {
            fprintf(stderr, "Failed to launch lcore %u: %s\n",
                    lcore_id, rte_strerror(ret));
        }
    }

    /* ── Step 6: Main lcore control loop ──
     *
     * In the real app, the main lcore handles:
     *   - Kafka consumer poll for policy updates (every 100ms)
     *   - Periodic stats printing
     *   - OAM command processing
     *   - Watching for force_quit (set by SIGTERM handler)
     *
     * It must NOT do any packet processing — that's the worker lcores' job.
     */
    printf("[Main lcore %u] Entering control loop...\n",
           rte_get_main_lcore());

    while (!force_quit) {
        /* In the real app: poll Kafka, update policy, print stats */
        rte_delay_ms(100);

        /* Print running stats every second */
        static int ticks = 0;
        if (++ticks % 10 == 0) {
            unsigned long total_rx = 0;
            RTE_LCORE_FOREACH_WORKER(lcore_id) {
                total_rx += atomic_load(&lcore_info[lcore_id].pkt_rx);
            }
            printf("[Stats] total_rx=%lu\n", total_rx);
        }

        /* Exit after a short demo */
        if (ticks >= 5) {
            force_quit = 1;
        }
    }

    /* ── Step 7: Wait for all workers to stop ──
     *
     * rte_eal_wait_lcore() blocks until the lcore function returns.
     * Must be called for every lcore that was rte_eal_remote_launch()ed,
     * or rte_eal_cleanup() will error.
     *
     * In the real app, before waiting, signal each lcore to stop:
     *   lcore_info[id].running = 0;
     */
    printf("[Shutdown] Signalling workers to stop...\n");
    RTE_LCORE_FOREACH_WORKER(lcore_id) {
        if (lcore_info[lcore_id].role != LCORE_ROLE_UNUSED) {
            lcore_info[lcore_id].running = 0;
        }
    }

    RTE_LCORE_FOREACH_WORKER(lcore_id) {
        if (lcore_info[lcore_id].role != LCORE_ROLE_UNUSED) {
            rte_eal_wait_lcore(lcore_id);
            printf("[lcore %u] joined\n", lcore_id);
        }
    }

    /* ── Step 8: Cleanup ──
     *
     * rte_eal_cleanup() releases hugepages, unbinds NIC drivers,
     * and destroys shared memory objects. Must be called before exit
     * for clean resource release, especially in multi-process setups.
     *
     * In the real app, before this:
     *   - Flush all CDR batches to Kafka
     *   - rd_kafka_flush() and rd_kafka_destroy()
     *   - Free Hyperscan databases and scratches
     */
    printf("[Cleanup] rte_eal_cleanup()\n");
    rte_eal_cleanup();

    printf("\n=== Shutdown complete ===\n");
    printf("\nStartup sequence for a full application:\n");
    printf("  1. config_load()                     (Module 01)\n");
    printf("  2. logger_init()                     (Module 02)\n");
    printf("  3. build_eal_args() + rte_eal_init() (THIS MODULE)\n");
    printf("  4. rte_pktmbuf_pool_create()         (Module 09)\n");
    printf("  5. port_init()                       (Module 10)\n");
    printf("  6. hs_init_global_scratch()           (Module 11)\n");
    printf("  7. kafka_init()                      (Module 12)\n");
    printf("  8. rte_ring_create() per lcore        (Module 03)\n");
    printf("  9. rte_eal_remote_launch() workers    (THIS MODULE)\n");
    printf(" 10. main lcore control loop\n");

    return 0;
}
