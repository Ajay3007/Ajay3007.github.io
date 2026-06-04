/**
 * numa_alloc.c — Module 14: NUMA-aware Memory Allocation
 *
 * Non-Uniform Memory Access (NUMA): on multi-socket servers, each CPU
 * socket has its own memory controller and DRAM banks. A lcore on socket 0
 * accessing memory allocated on socket 1 crosses the QPI/UPI interconnect:
 *
 *   Local access:  socket 0 lcore → socket 0 DRAM  ≈  80 ns
 *   Remote access: socket 0 lcore → socket 1 DRAM  ≈ 170 ns  (2× penalty)
 *
 * At 2M DNS lookups/sec, if the domain_details_table is on the wrong socket:
 *   2M × (170 - 80) ns = 180 ms of extra stall per second per worker lcore
 *   With 4 worker lcores: 720 ms/sec wasted on NUMA penalty alone.
 *
 * Rule: ALWAYS allocate memory on the same socket as the lcore(s) that
 * will access it. In the DP application this applies to:
 *   - rte_hash tables (domain_details_table, ip_vs_subscriber_table, ...)
 *   - rte_mempool (mbuf pool — must match NIC port's socket)
 *   - Hyperscan database (compiled on the socket of scanning lcores)
 *   - Per-lcore Hyperscan scratch (on each lcore's socket)
 *   - rte_ring rx_rings / tx_ring
 *
 * This file has two parts:
 *   Part A: NUMA topology reader — pure C, runs on any Linux box
 *   Part B: DPDK NUMA allocation APIs — reference code, needs DPDK
 *
 * REFERENCE CODE (Part B): requires DPDK installed.
 * Part A compiles standalone: gcc -Wall -O2 -o numa_topo numa_alloc.c
 */

/* ═══════════════════════════════════════════════════════════
 * PART A — NUMA Topology Reader (pure C, no DPDK)
 *
 * Before writing any DPDK app, understand your hardware topology.
 * This section reads it from the Linux sysfs — the same source that
 * DPDK's EAL uses to assign lcores to sockets.
 * ═══════════════════════════════════════════════════════════ */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <assert.h>
#include <dirent.h>
#include <ctype.h>

/* ───────────────────────────────────────────────────────────
 * print_cpu_topology — read /sys/devices/system/cpu/cpu*/topology/
 *
 * Shows which physical core and NUMA socket each logical CPU belongs to.
 * This is the first thing to run on a new server before writing DPDK config.
 * ─────────────────────────────────────────────────────────── */
static void print_cpu_topology(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Part A: NUMA / CPU Topology (from /sys)\n");
    printf("══════════════════════════════════════════════\n\n");

    printf("  %-8s %-12s %-12s %-8s\n",
           "cpu", "physical_id", "core_id", "socket");
    printf("  %-8s %-12s %-12s %-8s\n",
           "---", "-----------", "-------", "------");

    char path[256];
    char val[64];
    int  cpu;
    int  found_any = 0;

    for (cpu = 0; cpu < 512; cpu++) {
        snprintf(path, sizeof(path),
                 "/sys/devices/system/cpu/cpu%d/topology/physical_package_id",
                 cpu);
        FILE *fp = fopen(path, "r");
        if (!fp) break;   /* no more CPUs */

        int socket_id = -1, core_id = -1;
        if (fgets(val, sizeof(val), fp))
            socket_id = atoi(val);
        fclose(fp);

        snprintf(path, sizeof(path),
                 "/sys/devices/system/cpu/cpu%d/topology/core_id", cpu);
        fp = fopen(path, "r");
        if (fp) {
            if (fgets(val, sizeof(val), fp))
                core_id = atoi(val);
            fclose(fp);
        }

        printf("  cpu%-5d %-12d %-12d %-8d\n",
               cpu, socket_id, core_id, socket_id);
        found_any = 1;
    }

    if (!found_any)
        printf("  Could not read /sys/devices/system/cpu/ (not Linux?)\n");
    printf("\n");
}

/* ───────────────────────────────────────────────────────────
 * print_numa_memory — show hugepage memory per NUMA node
 *
 * DPDK allocates hugepages from /dev/hugepages (or hugetlbfs).
 * The --socket-mem EAL argument specifies how many MB to allocate
 * per socket. This function shows the current allocation.
 * ─────────────────────────────────────────────────────────── */
static void print_numa_memory(void)
{
    printf("  NUMA node memory (hugepages):\n");

    char path[256];
    char val[64];
    int  node;
    int  found_any = 0;

    for (node = 0; node < 8; node++) {
        snprintf(path, sizeof(path),
                 "/sys/devices/system/node/node%d/hugepages/"
                 "hugepages-2048kB/nr_hugepages", node);
        FILE *fp = fopen(path, "r");
        if (!fp) continue;

        int nr = 0;
        if (fgets(val, sizeof(val), fp))
            nr = atoi(val);
        fclose(fp);

        snprintf(path, sizeof(path),
                 "/sys/devices/system/node/node%d/hugepages/"
                 "hugepages-2048kB/free_hugepages", node);
        fp = fopen(path, "r");
        int free_nr = 0;
        if (fp) {
            if (fgets(val, sizeof(val), fp))
                free_nr = atoi(val);
            fclose(fp);
        }

        if (nr > 0 || free_nr > 0) {
            printf("    node%d: %d total × 2MB = %d MB  "
                   "(%d MB free)\n",
                   node, nr, nr * 2, free_nr * 2);
            found_any = 1;
        }
    }

    if (!found_any)
        printf("    No hugepages allocated. Allocate with:\n"
               "    echo 512 > /sys/kernel/mm/hugepages/"
               "hugepages-2048kB/nr_hugepages\n");
    printf("\n");
}

/* ───────────────────────────────────────────────────────────
 * recommend_eal_args — suggest EAL args based on topology
 *
 * DPDK EAL needs to know which socket to take memory from.
 * Wrong: --socket-mem 2048,0 on a single-socket machine → error
 * Wrong: --socket-mem 0,2048 when all lcores are on socket 0 → NUMA miss
 * Right: match socket-mem to the sockets hosting your lcores + NIC
 * ─────────────────────────────────────────────────────────── */
static void recommend_eal_args(void)
{
    printf("  Typical EAL args for a dual-socket server:\n\n");
    printf("  Single socket 0 (all lcores on socket 0, NIC on socket 0):\n");
    printf("    -l 2-7 --socket-mem 2048,0\n");
    printf("    → 2048 MB from socket 0 only\n\n");
    printf("  Dual socket (lcores on both, 2 NICs):\n");
    printf("    -l 2-7,10-15 --socket-mem 1024,1024\n");
    printf("    → 1024 MB per socket, NIC queues allocated on their socket\n\n");
    printf("  Check NIC NUMA socket:\n");
    printf("    cat /sys/bus/pci/devices/<PCI_ADDR>/numa_node\n");
    printf("    dpdk-devbind --status  (shows 'socket X' column)\n\n");
}

/* ═══════════════════════════════════════════════════════════
 * PART B — DPDK NUMA Allocation APIs (reference code)
 * ═══════════════════════════════════════════════════════════ */

#ifdef WITH_DPDK  /* compile Part B only when DPDK is available */

#include <rte_eal.h>
#include <rte_malloc.h>
#include <rte_memzone.h>
#include <rte_lcore.h>
#include <rte_ethdev.h>
#include <rte_cycles.h>
#include <rte_errno.h>

/* ───────────────────────────────────────────────────────────
 * demo_rte_malloc — rte_malloc vs rte_malloc_socket
 * ─────────────────────────────────────────────────────────── */
static void demo_rte_malloc(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Part B Demo 1: rte_malloc vs rte_malloc_socket\n");
    printf("══════════════════════════════════════════════\n\n");

    int socket = (int)rte_socket_id();
    printf("  Current lcore socket: %d\n\n", socket);

    /* ── rte_malloc_socket: explicit socket ──
     *
     * Used throughout the DP application for all per-group and per-lcore allocations.
     * The "type" string is a tag for rte_malloc_stats() diagnostics.
     * alignment=0 → use RTE_CACHE_LINE_SIZE (64 bytes).
     */
    size_t filter_details_size = 1024;   /* sizeof(filter_details) per domain */

    void *fd = rte_malloc_socket(
        "filter_details",       /* type tag for stats */
        filter_details_size,    /* bytes */
        0,                      /* alignment (0 = RTE_CACHE_LINE_SIZE) */
        socket                  /* NUMA socket */
    );
    if (!fd) {
        fprintf(stderr, "rte_malloc_socket failed: %s\n",
                rte_strerror(rte_errno));
        return;
    }
    printf("  rte_malloc_socket(\"filter_details\", 1024, 0, socket=%d) → %p\n",
           socket, fd);

    /* ── rte_zmalloc_socket: zeroed allocation ──
     *
     * Like rte_malloc_socket but zero-initialises the memory.
     * Always prefer this for structs — avoids uninitialised field bugs.
     * Used for group_struct, filter_details, lcore_info allocations.
     */
    void *group = rte_zmalloc_socket(
        "group_struct",
        4096,
        RTE_CACHE_LINE_SIZE,    /* explicit cache-line alignment */
        socket
    );
    if (!group) {
        fprintf(stderr, "rte_zmalloc_socket failed\n");
        rte_free(fd);
        return;
    }
    printf("  rte_zmalloc_socket(\"group_struct\", 4096, 64, socket=%d) → %p\n",
           socket, group);

    /* ── rte_malloc (no socket): uses SOCKET_ID_ANY ──
     *
     * DO NOT use for hot-path data structures.
     * SOCKET_ID_ANY means "allocate from any socket" — if called from
     * the main lcore (which may be on socket 0) during init, and the
     * worker lcores are on socket 1, you get cross-NUMA access.
     *
     * Only acceptable for control-plane allocations that are rarely accessed.
     */
    void *log_buf = rte_malloc("log_buffer", 8192, 0);
    printf("  rte_malloc(\"log_buffer\", 8192) [SOCKET_ID_ANY] → %p\n\n", log_buf);
    printf("  WARNING: rte_malloc without socket_id is risky.\n");
    printf("           Use rte_malloc_socket() for all hot-path data.\n\n");

    rte_free(fd);
    rte_free(group);
    rte_free(log_buf);
}

/* ───────────────────────────────────────────────────────────
 * demo_memzone — rte_memzone for named, persistent allocations
 *
 * A memzone is a named region in hugepage memory that persists until
 * rte_eal_cleanup(). Unlike rte_malloc, memzones can be looked up by
 * name from any part of the code — or from a secondary DPDK process.
 *
 * In the DP application, memzones are not heavily used (single-process app), but
 * they are useful for sharing state between the main process and a
 * monitoring secondary process.
 * ─────────────────────────────────────────────────────────── */
static void demo_memzone(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Part B Demo 2: rte_memzone (named hugepage memory)\n");
    printf("══════════════════════════════════════════════\n\n");

    int socket = (int)rte_socket_id();

    /*
     * Reserve a named memzone on the correct socket.
     * Names must be unique within the DPDK process.
     * Size is rounded up to the hugepage alignment (2MB).
     *
     * Use cases:
     *   - Global config struct shared across modules
     *   - Lookup tables that secondary processes need to read
     *   - Persistent counters that survive module reload
     */
    const struct rte_memzone *mz = rte_memzone_reserve(
        "dp_app_global_config",   /* unique name */
        4096,                       /* bytes needed */
        socket,                     /* NUMA socket */
        0                           /* flags (0 = default) */
    );

    if (!mz) {
        fprintf(stderr, "rte_memzone_reserve failed: %s\n",
                rte_strerror(rte_errno));
        return;
    }

    printf("  Reserved memzone 'dp_app_global_config':\n");
    printf("    addr      = %p\n", mz->addr);
    printf("    iova      = 0x%016" PRIx64 " (physical/IOVA for DMA)\n",
           mz->iova);
    printf("    len       = %zu bytes\n", mz->len);
    printf("    socket_id = %d\n", mz->socket_id);
    printf("    hugepage  = %zu KB pages\n\n", mz->hugepage_sz / 1024);

    /* Write some data into the memzone */
    snprintf((char *)mz->addr, 64,
             "DP App config - socket %d", socket);

    /* Look up the memzone by name from another part of the code */
    const struct rte_memzone *mz2 = rte_memzone_lookup("dp_app_global_config");
    assert(mz2 != NULL);
    assert(mz2->addr == mz->addr);
    printf("  Lookup by name: mz2->addr = %p → \"%s\"\n\n",
           mz2->addr, (char *)mz2->addr);

    /* Memzones are NOT freed with rte_free — they persist until EAL cleanup */
    /* rte_memzone_free(mz); */   /* exists but rarely used */
}

/* ───────────────────────────────────────────────────────────
 * demo_socket_queries — show socket ID APIs
 * ─────────────────────────────────────────────────────────── */
static void demo_socket_queries(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Part B Demo 3: DPDK socket query APIs\n");
    printf("══════════════════════════════════════════════\n\n");

    printf("  rte_socket_count()       = %u  (total NUMA sockets)\n",
           rte_socket_count());
    printf("  rte_get_main_lcore()     = %u\n", rte_get_main_lcore());
    printf("  rte_socket_id()          = %u  (main lcore's socket)\n",
           rte_socket_id());

    unsigned int lcore_id;
    printf("\n  Per-lcore socket IDs:\n");
    RTE_LCORE_FOREACH(lcore_id) {
        printf("    lcore %-3u → socket %u\n",
               lcore_id, rte_lcore_to_socket_id(lcore_id));
    }

    /*
     * NIC socket ID:
     * The NIC is physically plugged into one socket's PCIe slot.
     * mbufs for this NIC should be allocated on the same socket.
     * rte_eth_rx_queue_setup() already uses rte_eth_dev_socket_id()
     * internally — but rte_pktmbuf_pool_create() does not.
     *
     * In the DP application:
     *   int nic_socket = rte_eth_dev_socket_id(port_id);
     *   pool = rte_pktmbuf_pool_create("pool", n, cache, 0,
     *                                   RTE_MBUF_DEFAULT_BUF_SIZE,
     *                                   nic_socket);
     */
    if (rte_eth_dev_count_avail() > 0) {
        printf("\n  NIC port sockets:\n");
        uint16_t port_id;
        RTE_ETH_FOREACH_DEV(port_id) {
            int sock = rte_eth_dev_socket_id(port_id);
            printf("    port %-3u → socket %d%s\n",
                   port_id, sock,
                   sock == (int)rte_socket_id() ? " (same as main — good)" :
                                                   " (DIFFERENT — risk NUMA miss)");
        }
    }
    printf("\n");
}

/* ───────────────────────────────────────────────────────────
 * demo_numa_miss_cost — benchmark local vs remote access
 * ─────────────────────────────────────────────────────────── */
#define BENCH_ITERS   10000000
#define BENCH_BUF_SZ  (4 * 1024 * 1024)  /* 4 MB — too big for L3 */

static void demo_numa_miss_cost(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Part B Demo 4: NUMA local vs remote access cost\n");
    printf("══════════════════════════════════════════════\n\n");

    int local_socket  = (int)rte_socket_id();
    int remote_socket = (local_socket == 0) ? 1 : 0;

    if (rte_socket_count() < 2) {
        printf("  Single-socket machine — cannot measure cross-NUMA penalty.\n");
        printf("  On a dual-socket machine:\n");
        printf("    local  (same socket):   ~80 ns per random access\n");
        printf("    remote (cross socket):  ~170 ns per random access\n");
        printf("    Penalty: 2× — critical at 2M lookups/sec\n\n");
        return;
    }

    /* Allocate on local socket */
    uint8_t *local_buf = (uint8_t *)rte_malloc_socket(
        "bench_local", BENCH_BUF_SZ, RTE_CACHE_LINE_SIZE, local_socket);
    /* Allocate on remote socket */
    uint8_t *remote_buf = (uint8_t *)rte_malloc_socket(
        "bench_remote", BENCH_BUF_SZ, RTE_CACHE_LINE_SIZE, remote_socket);

    if (!local_buf || !remote_buf) {
        printf("  Cannot allocate benchmark buffers (not enough hugepages?)\n\n");
        rte_free(local_buf);
        rte_free(remote_buf);
        return;
    }

    memset(local_buf,  0xAA, BENCH_BUF_SZ);
    memset(remote_buf, 0xBB, BENCH_BUF_SZ);

    /* Benchmark random reads (simulates hash table lookup pattern) */
    volatile uint64_t sink = 0;
    uint64_t t0, t1;
    uint32_t stride = 4096;   /* stride larger than cache line → every access is a miss */

    /* Local */
    t0 = rte_rdtsc();
    for (int i = 0; i < BENCH_ITERS; i++)
        sink += local_buf[((uint64_t)i * stride) % BENCH_BUF_SZ];
    t1 = rte_rdtsc();
    double local_ns = (double)(t1 - t0) / rte_get_tsc_hz() * 1e9 / BENCH_ITERS;

    /* Remote */
    t0 = rte_rdtsc();
    for (int i = 0; i < BENCH_ITERS; i++)
        sink += remote_buf[((uint64_t)i * stride) % BENCH_BUF_SZ];
    t1 = rte_rdtsc();
    double remote_ns = (double)(t1 - t0) / rte_get_tsc_hz() * 1e9 / BENCH_ITERS;

    printf("  Buffer size: %d MB (larger than L3 → forced cache misses)\n",
           BENCH_BUF_SZ / 1024 / 1024);
    printf("  Local  socket %d access: %.1f ns/read\n", local_socket, local_ns);
    printf("  Remote socket %d access: %.1f ns/read\n", remote_socket, remote_ns);
    printf("  NUMA penalty: %.1fx  (%.1f ns overhead per access)\n\n",
           remote_ns / local_ns, remote_ns - local_ns);

    printf("  At 2M lookups/sec with wrong NUMA:\n");
    printf("    Extra latency = %.0f ms/sec per worker lcore\n\n",
           (remote_ns - local_ns) * 2e6 / 1e6);

    rte_free(local_buf);
    rte_free(remote_buf);
    (void)sink;
}

/* ───────────────────────────────────────────────────────────
 * demo_hyperscan_alloc — the real the DP application allocation pattern
 *
 * Hyperscan (Module 19-22) allocates databases and scratch spaces
 * internally via malloc(). To make them NUMA-local, the DP application uses
 * Hyperscan's custom allocator API to redirect allocations to
 * rte_malloc_socket().
 * ─────────────────────────────────────────────────────────── */
static void demo_hyperscan_alloc_pattern(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Part B Demo 5: Hyperscan NUMA allocation pattern\n");
    printf("══════════════════════════════════════════════\n\n");

    int socket = (int)rte_socket_id();

    printf("  In the real the DP application app (hs_db_compile_for_groups):\n\n");
    printf("  /* Redirect Hyperscan allocations to NUMA-local hugepages */\n");
    printf("  hs_set_allocator(\n");
    printf("      rte_malloc_hs,          /* custom alloc wrapper */\n");
    printf("      rte_free_hs             /* custom free wrapper */\n");
    printf("  );\n\n");
    printf("  /* Now hs_compile_multi() allocates on the correct socket */\n");
    printf("  hs_compile_multi(patterns, flags, ids, count,\n");
    printf("                   HS_MODE_BLOCK, NULL, &db, &err);\n\n");
    printf("  /* Per-lcore scratch: allocated on each lcore's socket */\n");
    printf("  RTE_LCORE_FOREACH_WORKER(lcore_id) {\n");
    printf("      int lsock = rte_lcore_to_socket_id(lcore_id);\n");
    printf("      /* hs_clone_scratch uses current allocator for the new scratch */\n");
    printf("      hs_clone_scratch(global_scratch, &per_lcore_scratch[lcore_id]);\n");
    printf("  }\n\n");

    printf("  /* Simulated: allocate a 'database' buffer on socket %d */\n", socket);
    size_t db_size = 512 * 1024;   /* 512 KB simulated Hyperscan DB */
    void  *db_buf  = rte_zmalloc_socket("hs_database", db_size,
                                         RTE_CACHE_LINE_SIZE, socket);
    if (db_buf) {
        printf("  hs_database buffer: %zu KB on socket %d at %p\n",
               db_size / 1024, socket, db_buf);
        rte_free(db_buf);
    }

    printf("\n  Key rule: Hyperscan DB must be on the SAME socket as worker lcores.\n");
    printf("  A 200MB DB on the wrong socket = 2M × 90ns = 180ms/sec of NUMA penalty.\n\n");
}

/* ─── Minimal EAL args ──────────────────────────────────── */
static const char *eal_args[] = {
    "numa_alloc", "-l", "0-3", "--socket-mem", "512,0",
    "-n", "4", "--proc-type", "auto", "--no-pci",
};

static void run_dpdk_demos(void)
{
    int ret = rte_eal_init(
        (int)(sizeof(eal_args) / sizeof(eal_args[0])),
        (char **)(uintptr_t)eal_args);
    if (ret < 0) {
        fprintf(stderr, "rte_eal_init failed: %s\n", rte_strerror(rte_errno));
        return;
    }

    demo_rte_malloc();
    demo_memzone();
    demo_socket_queries();
    demo_numa_miss_cost();
    demo_hyperscan_alloc_pattern();

    rte_eal_cleanup();
}

#endif  /* WITH_DPDK */

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    printf("=== Module 14: NUMA-aware Memory Allocation ===\n\n");

    /* Part A: always runs (no DPDK required) */
    print_cpu_topology();
    print_numa_memory();
    recommend_eal_args();

#ifdef WITH_DPDK
    printf("══════════════════════════════════════════════\n");
    printf("Part B: DPDK allocation demos\n");
    printf("══════════════════════════════════════════════\n\n");
    run_dpdk_demos();
#else
    printf("═══════════════════════════════════════════════════════\n");
    printf("Part B (DPDK) skipped — compile with make dpdk to enable\n");
    printf("═══════════════════════════════════════════════════════\n\n");
    printf("DPDK allocation API summary:\n\n");
    printf("  rte_malloc_socket(type, size, align, socket)\n");
    printf("    → NUMA-local alloc, hugepage-backed\n");
    printf("    → Use for: hash tables, group structs, filter_details\n\n");
    printf("  rte_zmalloc_socket(type, size, align, socket)\n");
    printf("    → Same + zero-initialised\n");
    printf("    → Prefer this for all structs\n\n");
    printf("  rte_free(ptr)\n");
    printf("    → Returns to hugepage pool\n\n");
    printf("  rte_memzone_reserve(name, size, socket, flags)\n");
    printf("    → Named, persistent, survives module reload\n");
    printf("    → Lookable by name: rte_memzone_lookup(name)\n\n");
    printf("  rte_socket_id()                  → current lcore's socket\n");
    printf("  rte_lcore_to_socket_id(lcore_id) → specific lcore's socket\n");
    printf("  rte_eth_dev_socket_id(port_id)   → NIC port's socket\n\n");
    printf("  SOCKET_ID_ANY = -1 (any socket — avoid for hot data)\n");
#endif

    printf("Key rules:\n");
    printf("  1. Always use rte_malloc_socket() for hot-path data\n");
    printf("  2. socket = rte_socket_id() if called from a worker lcore\n");
    printf("  3. socket = rte_eth_dev_socket_id(port) for mbuf pools\n");
    printf("  4. socket = rte_lcore_to_socket_id(id) for per-lcore scratch\n");
    printf("  5. Never rte_malloc() (SOCKET_ID_ANY) for hash tables or DB\n");

    return 0;
}
