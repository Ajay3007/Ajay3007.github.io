/**
 * port_init.c — Module 10: NIC Port Initialization
 *
 * After EAL init (Module 08) and mempool creation (Module 09), the next
 * step is configuring the NIC port. This tells the NIC:
 *   - How many RX queues to create (one per worker lcore for RSS)
 *   - How many TX queues to create
 *   - What hardware offloads to enable (checksum, RSS, VLAN strip)
 *   - The descriptor ring depth per queue
 *   - Which mempool to pull packet buffers from (for RX)
 *
 * In the real the DP application project, port initialization in app_main.c does:
 *   - One port, 4 RX queues (one per worker lcore), 1 TX queue
 *   - RSS configured to hash on IP + UDP + TCP (so DNS traffic spreads
 *     evenly across worker lcores by src IP)
 *   - TX hardware checksum offload enabled (avoids software checksum in
 *     DNS sinkhole response — Module 23)
 *   - Promiscuous mode for capturing all traffic
 *
 * REFERENCE CODE: requires DPDK and a DPDK-bound NIC.
 * For testing without a NIC: add --vdev net_null0 to EAL args
 * (Module 08 shows how to add EAL args programmatically).
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#include <rte_eal.h>
#include <rte_ethdev.h>
#include <rte_mempool.h>
#include <rte_mbuf.h>
#include <rte_errno.h>
#include <rte_lcore.h>
#include <rte_cycles.h>

/* ───────────────────────────────────────────────────────────
 * Port configuration constants
 *
 * RX_DESC and TX_DESC must be powers of 2.
 * In the DP application:  RX_DESC=1024, TX_DESC=1024
 * A larger ring reduces drops under burst but uses more memory.
 * ─────────────────────────────────────────────────────────── */
#define NUM_RX_QUEUES   4       /* one per worker lcore (from config) */
#define NUM_TX_QUEUES   1       /* single TX lcore services one queue */
#define RX_DESC         1024    /* RX descriptor ring depth per queue */
#define TX_DESC         1024    /* TX descriptor ring depth per queue */

#define LINK_POLL_INTERVAL_MS  100
#define LINK_POLL_MAX_TRIES    90  /* 9 seconds total wait for link up */

/* ───────────────────────────────────────────────────────────
 * rte_eth_conf — the central port config struct
 *
 * This struct controls everything about how the NIC behaves.
 * Wrong settings here are silent: the NIC initialises successfully
 * but drops packets, mis-hashes RSS, or skips checksum offload.
 * ─────────────────────────────────────────────────────────── */
static struct rte_eth_conf port_conf = {
    .rxmode = {
        /*
         * RSS (Receive Side Scaling): distributes incoming packets across
         * multiple RX queues based on a hash of src/dst IP + port.
         *
         * Without RSS, all packets go to queue 0. With NUM_RX_QUEUES=4,
         * RSS spreads load evenly — each worker lcore polls its own queue
         * and never contends with another.
         *
         * Alternative: RTE_ETH_MQ_RX_NONE (single queue, no RSS)
         */
        .mq_mode  = RTE_ETH_MQ_RX_RSS,

        /*
         * RX offload flags:
         * CHECKSUM — NIC verifies IP/TCP/UDP checksums in hardware.
         *            If checksum is bad, RTE_MBUF_F_RX_IP_CKSUM_BAD is set
         *            on the mbuf. The real app checks this and drops the
         *            packet before parsing to avoid acting on corrupted data.
         */
        .offloads = RTE_ETH_RX_OFFLOAD_CHECKSUM,
    },

    .rx_adv_conf = {
        .rss_conf = {
            /*
             * RSS hash key: NULL = use the NIC's default (40-byte Toeplitz key).
             * In the DP application the default key is fine — we want DNS (UDP) and
             * HTTPS (TCP) traffic distributed by src IP across workers.
             *
             * rss_hf: which packet types to hash.
             * We hash IP + TCP + UDP so that:
             *   - DNS (UDP/53) flows spread across workers by client IP
             *   - HTTPS (TCP/443) flows spread across workers by client IP
             * If a packet type is NOT in rss_hf, it goes to queue 0.
             */
            .rss_key = NULL,
            .rss_hf  = RTE_ETH_RSS_IP  |
                       RTE_ETH_RSS_TCP |
                       RTE_ETH_RSS_UDP,
        },
    },

    .txmode = {
        .mq_mode = RTE_ETH_MQ_TX_NONE,  /* no TX multi-queue (one TX lcore) */

        /*
         * TX offload flags — hardware checksum insertion.
         *
         * When the DNS sinkhole (Module 23) rewrites a packet, it sets
         * RTE_MBUF_F_TX_IP_CKSUM and RTE_MBUF_F_TX_UDP_CKSUM on the mbuf,
         * zeroes ip->checksum, and sets udp->checksum to the pseudo-header
         * sum. The NIC TX engine then fills in the real checksums.
         *
         * Without these offload flags here, the NIC ignores the mbuf flags
         * and transmits with checksum=0 — the receiver drops the packet.
         */
        .offloads = RTE_ETH_TX_OFFLOAD_IPV4_CKSUM |
                    RTE_ETH_TX_OFFLOAD_UDP_CKSUM   |
                    RTE_ETH_TX_OFFLOAD_TCP_CKSUM,
    },
};

/* ───────────────────────────────────────────────────────────
 * print_port_info — dump NIC capabilities
 *
 * Always call this before configuring a port in development.
 * Some NICs don't support certain offloads — if you request an
 * offload the NIC doesn't support, rte_eth_dev_configure() fails
 * with EINVAL. Checking capabilities avoids this surprise.
 * ─────────────────────────────────────────────────────────── */
static void print_port_info(uint16_t port_id)
{
    struct rte_eth_dev_info info;

    rte_eth_dev_info_get(port_id, &info);

    printf("[Port %u capabilities]\n", port_id);
    printf("  driver          : %s\n", info.driver_name);
    printf("  if_index        : %u\n", info.if_index);
    printf("  max_rx_queues   : %u\n", info.max_rx_queues);
    printf("  max_tx_queues   : %u\n", info.max_tx_queues);
    printf("  max_rx_desc     : %u  (per queue)\n", info.rx_desc_lim.nb_max);
    printf("  max_tx_desc     : %u  (per queue)\n", info.tx_desc_lim.nb_max);

    /* Check which RX offloads this NIC supports */
    printf("  rx_offloads     : ");
    if (info.rx_offload_capa & RTE_ETH_RX_OFFLOAD_CHECKSUM)
        printf("CHECKSUM ");
    if (info.rx_offload_capa & RTE_ETH_RX_OFFLOAD_VLAN_STRIP)
        printf("VLAN_STRIP ");
    if (info.rx_offload_capa & RTE_ETH_RX_OFFLOAD_RSS_HASH)
        printf("RSS_HASH ");
    if (info.rx_offload_capa & RTE_ETH_RX_OFFLOAD_SCATTER)
        printf("SCATTER ");
    printf("\n");

    /* Check which TX offloads this NIC supports */
    printf("  tx_offloads     : ");
    if (info.tx_offload_capa & RTE_ETH_TX_OFFLOAD_IPV4_CKSUM)
        printf("IPV4_CKSUM ");
    if (info.tx_offload_capa & RTE_ETH_TX_OFFLOAD_UDP_CKSUM)
        printf("UDP_CKSUM ");
    if (info.tx_offload_capa & RTE_ETH_TX_OFFLOAD_TCP_CKSUM)
        printf("TCP_CKSUM ");
    if (info.tx_offload_capa & RTE_ETH_TX_OFFLOAD_MULTI_SEGS)
        printf("MULTI_SEGS ");
    printf("\n");

    /* Check which RSS hash types this NIC supports */
    printf("  rss_hf_capa     : ");
    if (info.flow_type_rss_offloads & RTE_ETH_RSS_IP)  printf("IP ");
    if (info.flow_type_rss_offloads & RTE_ETH_RSS_TCP) printf("TCP ");
    if (info.flow_type_rss_offloads & RTE_ETH_RSS_UDP) printf("UDP ");
    printf("\n\n");
}

/* ───────────────────────────────────────────────────────────
 * check_port_link_status — wait for physical link to come up
 *
 * After rte_eth_dev_start(), the NIC negotiates link with the switch.
 * This takes 0–3 seconds. We poll rather than blocking so we can
 * timeout and print a useful error message.
 *
 * In the real the DP application app, a timeout here means the fibre/cable is
 * disconnected or the switch port is down — a hard startup failure.
 * ─────────────────────────────────────────────────────────── */
static int check_port_link_status(uint16_t port_id)
{
    struct rte_eth_link link;
    int tries = 0;

    printf("[Port %u] Waiting for link...", port_id);
    fflush(stdout);

    while (tries < LINK_POLL_MAX_TRIES) {
        memset(&link, 0, sizeof(link));
        rte_eth_link_get_nowait(port_id, &link);

        if (link.link_status == RTE_ETH_LINK_UP) {
            printf("\n[Port %u] Link UP  %u Gbps  %s-duplex  %s\n",
                   port_id,
                   link.link_speed / 1000,
                   link.link_duplex == RTE_ETH_LINK_FULL_DUPLEX
                       ? "full" : "half",
                   link.link_autoneg ? "autoneg" : "fixed");
            return 0;
        }

        printf(".");
        fflush(stdout);
        rte_delay_ms(LINK_POLL_INTERVAL_MS);
        tries++;
    }

    printf("\n[Port %u] Link DOWN after %d ms — check cable/switch\n",
           port_id, LINK_POLL_MAX_TRIES * LINK_POLL_INTERVAL_MS);
    return -1;
}

/* ───────────────────────────────────────────────────────────
 * port_init — the main initialization function
 *
 * This is what app_main.c calls once per port after EAL init.
 * Returns 0 on success, -1 on any failure.
 *
 * @port_id   : NIC port index (0-based)
 * @mbuf_pool : pool from Module 09 (rte_pktmbuf_pool_create)
 * ─────────────────────────────────────────────────────────── */
int port_init(uint16_t port_id, struct rte_mempool *mbuf_pool)
{
    struct rte_eth_dev_info dev_info;
    struct rte_eth_rxconf   rxq_conf;
    struct rte_eth_txconf   txq_conf;
    uint16_t                nb_rxd = RX_DESC;
    uint16_t                nb_txd = TX_DESC;
    int                     ret;
    uint16_t                q;

    if (!rte_eth_dev_is_valid_port(port_id)) {
        fprintf(stderr, "[port_init] Port %u is not valid\n", port_id);
        return -1;
    }

    print_port_info(port_id);

    rte_eth_dev_info_get(port_id, &dev_info);

    /*
     * Intersect requested offloads with what the NIC actually supports.
     * Requesting an unsupported offload causes rte_eth_dev_configure() to
     * fail with -EINVAL. Always mask against dev_info capabilities.
     */
    port_conf.rxmode.offloads &= dev_info.rx_offload_capa;
    port_conf.txmode.offloads &= dev_info.tx_offload_capa;

    /*
     * Also intersect the RSS hash types.
     * A NIC that doesn't support RSS_UDP would silently never hash
     * DNS (UDP/53) — all DNS would pile onto queue 0.
     */
    port_conf.rx_adv_conf.rss_conf.rss_hf &= dev_info.flow_type_rss_offloads;

    if (NUM_RX_QUEUES > dev_info.max_rx_queues) {
        fprintf(stderr, "[port_init] Requested %u RX queues but NIC max is %u\n",
                NUM_RX_QUEUES, dev_info.max_rx_queues);
        return -1;
    }

    /* ── Step 1: Configure the port ── */
    ret = rte_eth_dev_configure(port_id,
                                 NUM_RX_QUEUES,
                                 NUM_TX_QUEUES,
                                 &port_conf);
    if (ret < 0) {
        fprintf(stderr, "[port_init] rte_eth_dev_configure failed: %s\n",
                rte_strerror(-ret));
        return -1;
    }
    printf("[Port %u] Configured: %u RX queues, %u TX queues\n",
           port_id, NUM_RX_QUEUES, NUM_TX_QUEUES);

    /* ── Step 2: Adjust descriptor counts ──
     *
     * rte_eth_dev_adjust_nb_rx_tx_desc() rounds nb_rxd / nb_txd to the
     * nearest valid value for this NIC (must be a power of 2 within the
     * NIC's min/max range). Always call this after configure.
     */
    ret = rte_eth_dev_adjust_nb_rx_tx_desc(port_id, &nb_rxd, &nb_txd);
    if (ret < 0) {
        fprintf(stderr, "[port_init] adjust_nb_rx_tx_desc failed: %s\n",
                rte_strerror(-ret));
        return -1;
    }
    printf("[Port %u] Descriptors: RX=%u  TX=%u (after NIC alignment)\n",
           port_id, nb_rxd, nb_txd);

    /* ── Step 3: Set up RX queues ──
     *
     * One queue per worker lcore. Each queue gets its own slice of the
     * mbuf pool — RSS hash routes incoming packets to specific queues,
     * each polled by exactly one lcore (no contention).
     *
     * socket_id: allocate the RX queue descriptor ring on the same NUMA
     * socket as the NIC. Cross-NUMA descriptor ring access adds ~100 ns
     * per packet on a dual-socket server.
     */
    rxq_conf           = dev_info.default_rxconf;
    rxq_conf.offloads  = port_conf.rxmode.offloads;

    for (q = 0; q < NUM_RX_QUEUES; q++) {
        ret = rte_eth_rx_queue_setup(
            port_id,
            q,                          /* queue index */
            nb_rxd,                     /* descriptor ring depth */
            rte_eth_dev_socket_id(port_id),  /* NUMA socket */
            &rxq_conf,
            mbuf_pool                   /* pool for received packet buffers */
        );
        if (ret < 0) {
            fprintf(stderr, "[port_init] rx_queue_setup q=%u failed: %s\n",
                    q, rte_strerror(-ret));
            return -1;
        }
    }
    printf("[Port %u] RX queues set up (pool: %s)\n",
           port_id, mbuf_pool->name);

    /* ── Step 4: Set up TX queues ── */
    txq_conf          = dev_info.default_txconf;
    txq_conf.offloads = port_conf.txmode.offloads;

    for (q = 0; q < NUM_TX_QUEUES; q++) {
        ret = rte_eth_tx_queue_setup(
            port_id,
            q,
            nb_txd,
            rte_eth_dev_socket_id(port_id),
            &txq_conf
        );
        if (ret < 0) {
            fprintf(stderr, "[port_init] tx_queue_setup q=%u failed: %s\n",
                    q, rte_strerror(-ret));
            return -1;
        }
    }
    printf("[Port %u] TX queues set up\n", port_id);

    /* ── Step 5: Start the port ──
     *
     * This triggers the NIC to begin link negotiation and DMA setup.
     * No packets flow until this call returns successfully.
     */
    ret = rte_eth_dev_start(port_id);
    if (ret < 0) {
        fprintf(stderr, "[port_init] rte_eth_dev_start failed: %s\n",
                rte_strerror(-ret));
        return -1;
    }
    printf("[Port %u] Started\n", port_id);

    /* ── Step 6: Enable promiscuous mode ──
     *
     * In promiscuous mode the NIC accepts ALL frames, not just those
     * addressed to its own MAC. Required for an inline security appliance
     * that intercepts traffic between clients and the internet.
     *
     * Without promiscuous mode, the NIC silently drops packets destined
     * for other MACs — subscribers' DNS queries would never reach the DP application.
     */
    ret = rte_eth_promiscuous_enable(port_id);
    if (ret < 0)
        fprintf(stderr, "[port_init] promiscuous_enable warning: %s\n",
                rte_strerror(-ret));
    else
        printf("[Port %u] Promiscuous mode enabled\n", port_id);

    /* ── Step 7: Wait for link ── */
    return check_port_link_status(port_id);
}

/* ───────────────────────────────────────────────────────────
 * print_port_stats — per-queue RX/TX counters
 *
 * In the real app the main lcore prints these every second.
 * A TX drop count > 0 means the TX ring is full — the TX lcore
 * can't keep up with the worker lcores.
 * ─────────────────────────────────────────────────────────── */
static void print_port_stats(uint16_t port_id)
{
    struct rte_eth_stats stats;
    rte_eth_stats_get(port_id, &stats);

    printf("\n[Port %u statistics]\n", port_id);
    printf("  rx_packets  : %" PRIu64 "\n", stats.ipackets);
    printf("  rx_bytes    : %" PRIu64 "\n", stats.ibytes);
    printf("  rx_missed   : %" PRIu64 "  (NIC RX ring full → dropped)\n",
           stats.imissed);
    printf("  rx_errors   : %" PRIu64 "\n", stats.ierrors);
    printf("  tx_packets  : %" PRIu64 "\n", stats.opackets);
    printf("  tx_bytes    : %" PRIu64 "\n", stats.obytes);
    printf("  tx_errors   : %" PRIu64 "\n", stats.oerrors);

    /*
     * imissed > 0: the RX ring filled up because the software (RX lcore)
     * didn't call rte_eth_rx_burst() fast enough. Causes:
     *   - RX lcore doing work it shouldn't (policy, Hyperscan)
     *   - Worker lcores too slow (ring between RX and workers is full)
     *   - Insufficient NIC RX descriptors (increase RX_DESC)
     *
     * In the DP application, imissed is the first stat checked when investigating
     * packet loss complaints.
     */
}

/* ───────────────────────────────────────────────────────────
 * print_rss_reta — RSS redirect table
 *
 * The RSS RETA (Redirection Table) maps each hash bucket (0–127 typically)
 * to an RX queue. By default, DPDK distributes evenly: bucket i → queue i % nb_queues.
 *
 * In the real app, after port_init you can read the RETA to verify that
 * traffic will actually spread across your worker queues.
 * ─────────────────────────────────────────────────────────── */
static void print_rss_reta(uint16_t port_id, uint16_t nb_queues)
{
    struct rte_eth_dev_info info;
    rte_eth_dev_info_get(port_id, &info);

    uint16_t reta_size = info.reta_size;   /* typically 128 or 512 entries */
    if (reta_size == 0) {
        printf("[Port %u] No RSS RETA (RSS not supported)\n", port_id);
        return;
    }

    struct rte_eth_rss_reta_entry64 reta_conf[reta_size / RTE_ETH_RETA_GROUP_SIZE + 1];
    uint16_t nb_groups = (reta_size + RTE_ETH_RETA_GROUP_SIZE - 1)
                         / RTE_ETH_RETA_GROUP_SIZE;

    for (uint16_t g = 0; g < nb_groups; g++)
        reta_conf[g].mask = UINT64_MAX;   /* read all entries */

    if (rte_eth_dev_rss_reta_query(port_id, reta_conf, reta_size) != 0) {
        printf("[Port %u] Could not read RSS RETA\n", port_id);
        return;
    }

    printf("[Port %u] RSS RETA (%u entries → %u queues):\n",
           port_id, reta_size, nb_queues);

    /* Show the first 16 entries */
    uint16_t show = reta_size < 16 ? reta_size : 16;
    for (uint16_t i = 0; i < show; i++) {
        uint16_t grp = i / RTE_ETH_RETA_GROUP_SIZE;
        uint16_t idx = i % RTE_ETH_RETA_GROUP_SIZE;
        printf("  bucket[%3u] → queue %u\n", i, reta_conf[grp].reta[idx]);
    }
    if (reta_size > 16)
        printf("  ... (%u more entries)\n", reta_size - 16);
    printf("\n");
}

/* ─── Minimal EAL args (use net_null if no physical NIC) ─── */
static const char *eal_args[] = {
    "port_init",
    "-l", "0-1",
    "--socket-mem", "256",
    "-n", "4",
    "--proc-type", "auto",
    /*
     * For testing without a real NIC, use a null PMD:
     *   "--vdev", "net_null0,copy=1"
     * This creates a virtual port that accepts and silently drops all packets.
     * Copy=1 makes TX actually copy data (useful for correctness testing).
     *
     * In CI/CD environments where no NIC is available, replace the
     * real port with net_null and the code structure stays identical.
     */
};

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    printf("=== Module 10: NIC Port Init ===\n\n");

    int ret = rte_eal_init(
        (int)(sizeof(eal_args) / sizeof(eal_args[0])),
        (char **)(uintptr_t)eal_args);
    if (ret < 0)
        rte_exit(EXIT_FAILURE, "rte_eal_init failed: %s\n",
                 rte_strerror(rte_errno));

    /* Check available ports */
    uint16_t nb_ports = rte_eth_dev_count_avail();
    printf("[EAL] %u NIC port(s) available\n\n", nb_ports);

    if (nb_ports == 0) {
        printf("No NIC ports found.\n"
               "Hint: bind a NIC with:\n"
               "  dpdk-devbind --bind=vfio-pci <PCI_addr>\n"
               "Or add --vdev net_null0 to EAL args for testing.\n");
        rte_eal_cleanup();
        return 0;
    }

    /* Create mbuf pool (same as Module 09) */
    struct rte_mempool *pool = rte_pktmbuf_pool_create(
        "mbuf_pool",
        8191,
        256,
        0,
        RTE_MBUF_DEFAULT_BUF_SIZE,
        rte_socket_id()
    );
    if (!pool)
        rte_exit(EXIT_FAILURE, "Cannot create mempool: %s\n",
                 rte_strerror(rte_errno));

    /* Initialize each available port */
    uint16_t port_id;
    RTE_ETH_FOREACH_DEV(port_id) {
        printf("────────────────────────────────────────\n");
        printf("Initializing port %u...\n", port_id);
        if (port_init(port_id, pool) < 0)
            rte_exit(EXIT_FAILURE, "Port %u init failed\n", port_id);

        print_port_stats(port_id);
        print_rss_reta(port_id, NUM_RX_QUEUES);
    }

    printf("════════════════════════════════════════\n");
    printf("All ports initialized. System ready for packet I/O.\n\n");

    printf("Next step in the real app:\n");
    printf("  rte_eal_remote_launch(rx_lcore_func, &lcore_info[rx], rx_lcore)\n");
    printf("  rte_eal_remote_launch(tx_lcore_func, &lcore_info[tx], tx_lcore)\n");
    printf("  RTE_LCORE_FOREACH_WORKER(id) → launch worker_func\n\n");

    printf("RX loop (inside rx_lcore_func):\n");
    printf("  nb_rx = rte_eth_rx_burst(port, queue, mbufs, BURST_SIZE)\n");
    printf("  rte_ring_enqueue_burst(rx_ring, (void**)mbufs, nb_rx, NULL)\n\n");

    printf("TX loop (inside tx_lcore_func):\n");
    printf("  nb    = rte_ring_dequeue_burst(tx_ring, (void**)mbufs, BURST_SIZE, NULL)\n");
    printf("  nb_tx = rte_eth_tx_burst(port, queue, mbufs, nb)\n");
    printf("  for dropped: rte_pktmbuf_free(mbufs[nb_tx + i])\n");

    /* Graceful port shutdown */
    RTE_ETH_FOREACH_DEV(port_id) {
        printf("\n[Shutdown] Stopping port %u...\n", port_id);
        rte_eth_dev_stop(port_id);
        rte_eth_dev_close(port_id);
    }

    rte_eal_cleanup();
    return 0;
}
