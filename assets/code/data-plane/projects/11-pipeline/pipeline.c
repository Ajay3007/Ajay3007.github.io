/**
 * pipeline.c — Module 11: Multi-lcore RX/TX Pipeline
 *
 * This module wires together Modules 08–10 into the actual packet
 * processing skeleton — the structure that runs at line rate in the DP application.
 *
 * Pipeline topology:
 *
 *   NIC port 0
 *     │  (DMA fills mbufs from pool — Module 09)
 *     ↓
 *   RX lcore  ──── rte_eth_rx_burst() ────────────────────────────────┐
 *                                                                      │
 *              Distributes round-robin across worker rx_rings          │
 *              (or: RSS routes directly to per-worker NIC queues)      │
 *                                                                      │
 *   rx_ring[0]  rx_ring[1]  rx_ring[2]  rx_ring[3]  (rte_ring)       │
 *       │           │           │           │                          │
 *   Worker 0    Worker 1    Worker 2    Worker 3                      │
 *   lcore 3     lcore 4     lcore 5     lcore 6                       │
 *       │           │           │           │                          │
 *   Parse ETH/IP/UDP-TCP  (Module 05)                                 │
 *   DNS port 53 → dns_parse() → policy  (Modules 06, 22)              │
 *   TLS port 443 → tls_extract_sni() → policy  (Modules 07, 22)       │
 *   Decision: ALLOW → tx_ring  |  DROP → rte_pktmbuf_free()           │
 *             SINKHOLE → modify in-place → tx_ring  (Module 23)       │
 *       │           │           │           │                          │
 *   ────┴───────────┴───────────┴───────────┴──── tx_ring ────────────┘
 *                                                      │
 *                                                  TX lcore
 *                                              rte_eth_tx_burst()
 *                                                      │
 *                                                  NIC port 0
 *
 * In the real DP project:
 *   - This structure is in pkt_proc.h / app_main.c
 *   - The rx_ring equivalent uses rte_distributor for worker dispatch
 *   - Worker function is process_dns_for_group() + related
 *   - Sinkhole is dns_build_sinkhole_v4/v6()
 *
 * REFERENCE CODE: requires DPDK installed.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <signal.h>
#include <stdatomic.h>

#include <rte_eal.h>
#include <rte_ethdev.h>
#include <rte_mempool.h>
#include <rte_mbuf.h>
#include <rte_ring.h>
#include <rte_lcore.h>
#include <rte_cycles.h>
#include <rte_errno.h>
#include <rte_ip.h>
#include <rte_udp.h>
#include <rte_tcp.h>
#include <rte_ether.h>

/* ───────────────────────────────────────────────────────────
 * Pipeline constants
 * ─────────────────────────────────────────────────────────── */
#define MAX_WORKERS     8
#define BURST_SIZE      32      /* packets per rte_eth_rx_burst call */
#define RING_SIZE       4096    /* must be power of 2 */
#define PORT_ID         0
#define RX_QUEUE_ID     0
#define TX_QUEUE_ID     0

#define PORT_DNS        53
#define PORT_HTTPS      443

/* ───────────────────────────────────────────────────────────
 * Policy decision codes
 * Mirrors ALLOW_PACKET / DROP_PACKET / PROCESS_WORKFLOW in policy_cache.h
 * ─────────────────────────────────────────────────────────── */
#define DECISION_ALLOW    0
#define DECISION_DROP     1
#define DECISION_SINKHOLE 2

/* ───────────────────────────────────────────────────────────
 * Per-lcore context
 *
 * Each lcore gets its own context struct, aligned to a cache line so
 * adjacent lcore contexts don't share a cache line (false sharing).
 * The main lcore reads stats (atomic_load) without any lock.
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    unsigned int     lcore_id;
    uint16_t         port_id;
    uint16_t         queue_id;

    struct rte_ring *rx_ring;    /* this worker's input ring */
    struct rte_ring *tx_ring;    /* shared output ring → TX lcore */

    volatile int     running;    /* set to 0 to stop this lcore */

    /* per-lcore stats — atomic so main lcore can read lock-free */
    atomic_ulong  pkt_rx;
    atomic_ulong  pkt_tx;
    atomic_ulong  pkt_drop;
    atomic_ulong  pkt_dns;
    atomic_ulong  pkt_tls;
} __rte_cache_aligned lcore_ctx_t;

/* ───────────────────────────────────────────────────────────
 * Global pipeline state
 * ─────────────────────────────────────────────────────────── */
static struct {
    struct rte_ring   *rx_rings[MAX_WORKERS]; /* one per worker */
    struct rte_ring   *tx_ring;               /* shared workers → TX */
    struct rte_mempool *pool;
    lcore_ctx_t        ctx[RTE_MAX_LCORE];
    unsigned int       worker_lcores[MAX_WORKERS];
    unsigned int       worker_count;
    unsigned int       rx_lcore;
    unsigned int       tx_lcore;
} g_pipeline;

static volatile int g_quit = 0;

/* ───────────────────────────────────────────────────────────
 * policy_stub — placeholder for the real policy engine
 *
 * In the real app, this is replaced by:
 *   process_dns_for_group()  — for DNS packets
 *   url_policy_for_tls()  — for TLS/IP packets
 *
 * Those functions:
 *   1. rte_hash_lookup_data(domain_details_table, domain, &fd) — Module 16
 *   2. hs_scan_domain_group(domain, ...) if hash miss         — Module 22
 *   3. Return ALLOW / DROP / SINKHOLE based on filter_details
 * ─────────────────────────────────────────────────────────── */
static inline int policy_stub(struct rte_mbuf *mbuf,
                               int is_dns, int is_tls,
                               const char *domain)
{
    (void)mbuf;
    (void)is_tls;

    /*
     * Stub: block domains ending in ".blocked" for demo purposes.
     * In the real app, this check is replaced by the two-tier lookup:
     *   hash table exact match → Hyperscan regex fallback
     */
    if (is_dns && domain && strstr(domain, ".blocked"))
        return DECISION_SINKHOLE;

    return DECISION_ALLOW;
}

/* ───────────────────────────────────────────────────────────
 * parse_and_decide — per-packet parse + policy stub
 *
 * This is the skeleton of the real worker lcore inner loop.
 * Modules 05-07 implement the parsers; Module 22 replaces policy_stub.
 *
 * Returns: DECISION_ALLOW / DROP / SINKHOLE
 * ─────────────────────────────────────────────────────────── */
static inline int parse_and_decide(struct rte_mbuf *mbuf,
                                    int *is_dns_out, int *is_tls_out)
{
    *is_dns_out = 0;
    *is_tls_out = 0;

    /*
     * Guard: reject multi-segment mbufs.
     * Jumbo frames (>2176 bytes) arrive as chained mbufs.
     * At MTU=1500 this is rare, but must be handled.
     * The DP application drops them rather than paying linearise cost.
     */
    if (unlikely(mbuf->nb_segs > 1))
        return DECISION_DROP;

    uint32_t pkt_len = rte_pktmbuf_pkt_len(mbuf);
    if (unlikely(pkt_len < sizeof(struct rte_ether_hdr)))
        return DECISION_DROP;

    /* ── Layer 2: Ethernet ── */
    struct rte_ether_hdr *eth = rte_pktmbuf_mtod(mbuf, struct rte_ether_hdr *);
    uint16_t ether_type       = rte_be_to_cpu_16(eth->ether_type);

    /*
     * VLAN handling: if ether_type == 0x8100, the real VLAN tag follows.
     * Skip it to get to the inner EtherType.
     * The DP application enterprise variant handles 802.1Q-tagged traffic.
     */
    struct rte_vlan_hdr *vlan = NULL;
    if (ether_type == RTE_ETHER_TYPE_VLAN) {
        vlan       = (struct rte_vlan_hdr *)(eth + 1);
        ether_type = rte_be_to_cpu_16(vlan->eth_proto);
    }

    /* ── Layer 3: IPv4 or IPv6 ── */
    uint8_t l4_proto = 0;
    void   *l4_hdr   = NULL;

    if (ether_type == RTE_ETHER_TYPE_IPV4) {
        struct rte_ipv4_hdr *ip4 = (struct rte_ipv4_hdr *)
            ((uint8_t *)eth + sizeof(*eth) + (vlan ? 4 : 0));

        if (unlikely(pkt_len < sizeof(*eth) + rte_ipv4_hdr_len(ip4)))
            return DECISION_DROP;

        l4_proto = ip4->next_proto_id;
        l4_hdr   = (uint8_t *)ip4 + rte_ipv4_hdr_len(ip4);

    } else if (ether_type == RTE_ETHER_TYPE_IPV6) {
        struct rte_ipv6_hdr *ip6 = (struct rte_ipv6_hdr *)
            ((uint8_t *)eth + sizeof(*eth) + (vlan ? 4 : 0));

        if (unlikely(pkt_len < sizeof(*eth) + sizeof(*ip6)))
            return DECISION_DROP;

        l4_proto = ip6->proto;
        l4_hdr   = ip6 + 1;

    } else {
        /* ARP, LLDP, etc. — forward without policy */
        return DECISION_ALLOW;
    }

    /* ── Layer 4: UDP or TCP ── */
    char domain[256] = {0};

    if (l4_proto == IPPROTO_UDP) {
        struct rte_udp_hdr *udp = (struct rte_udp_hdr *)l4_hdr;
        uint16_t dst_port       = rte_be_to_cpu_16(udp->dst_port);
        uint16_t src_port       = rte_be_to_cpu_16(udp->src_port);

        if (dst_port == PORT_DNS || src_port == PORT_DNS) {
            *is_dns_out = 1;

            /*
             * Real app calls:
             *   parse_dns_ipv4_request_packet_over_udp(mbuf, worker_info, ...)
             * which extracts qname into worker_info->domain and calls
             * url_policy_for_dns().
             *
             * Here: stub domain extraction from raw DNS question.
             * dns_parse_message() from Module 06 would go here.
             */
            uint8_t *dns_payload = (uint8_t *)(udp + 1);
            int      dns_len     = rte_be_to_cpu_16(udp->dgram_len) - 8;

            if (dns_len > 12) {
                /* Skip DNS header (12B), walk qname label encoding */
                uint8_t *qname_ptr = dns_payload + 12;
                int      pos = 0;
                while (pos < dns_len - 12 && qname_ptr[pos] != 0) {
                    uint8_t label_len = qname_ptr[pos++];
                    if (label_len >= 64 || pos + label_len > dns_len - 12)
                        break;
                    if (domain[0]) strncat(domain, ".", sizeof(domain)-strlen(domain)-1);
                    strncat(domain, (char *)qname_ptr + pos,
                            label_len < (int)(sizeof(domain)-strlen(domain)-1)
                                ? label_len : sizeof(domain)-strlen(domain)-1);
                    pos += label_len;
                }
            }
        }

    } else if (l4_proto == IPPROTO_TCP) {
        struct rte_tcp_hdr *tcp = (struct rte_tcp_hdr *)l4_hdr;
        uint16_t dst_port       = rte_be_to_cpu_16(tcp->dst_port);

        if (dst_port == PORT_HTTPS) {
            *is_tls_out = 1;

            /*
             * Real app:
             *   hs_scan_payload(tcp_payload, payload_len, worker_info, &matchCtx)
             * Hyperscan matches HS_PATTERN_ID_TLS=1 → on_hs_match extracts SNI.
             * tls_extract_sni_from_match() from Module 07 is what on_hs_match calls.
             *
             * Here: stub — SNI extraction from Module 07 would plug in here.
             */
            uint8_t *tcp_payload = (uint8_t *)tcp +
                                   ((tcp->data_off >> 4) << 2);
            if (*tcp_payload == 0x16) {  /* TLS Handshake record */
                strncpy(domain, "tls-sni-stub.example", sizeof(domain)-1);
            }
        }
    }

    return policy_stub(mbuf, *is_dns_out, *is_tls_out, domain);
}

/* ───────────────────────────────────────────────────────────
 * rx_lcore_func — receive packets from NIC, distribute to workers
 *
 * This lcore does ONE thing: call rte_eth_rx_burst() in a tight loop
 * and distribute packets to worker rings. It must NOT do any parsing
 * or policy work — that would slow down the RX loop and cause NIC
 * queue overflow (stats.imissed).
 * ─────────────────────────────────────────────────────────── */
static int rx_lcore_func(void *arg)
{
    lcore_ctx_t    *ctx   = (lcore_ctx_t *)arg;
    struct rte_mbuf *mbufs[BURST_SIZE];
    uint32_t         worker_rr = 0;   /* round-robin index */

    printf("[lcore %u] RX started: port=%u queue=%u → %u workers\n",
           ctx->lcore_id, ctx->port_id, ctx->queue_id,
           g_pipeline.worker_count);

    while (ctx->running && !g_quit) {
        /*
         * rte_eth_rx_burst: the hot path entry point.
         * Polls the NIC RX descriptor ring. Returns 0 if no packets.
         * Never blocks — if empty, returns immediately with nb_rx=0.
         *
         * BURST_SIZE=32: process up to 32 packets per call.
         * Larger bursts amortize per-call overhead but increase latency.
         * 32 is the standard sweet spot for most NIC drivers.
         */
        uint16_t nb_rx = rte_eth_rx_burst(ctx->port_id, ctx->queue_id,
                                           mbufs, BURST_SIZE);
        if (nb_rx == 0) {
            rte_pause();  /* x86 PAUSE: tells CPU we're in a spin loop */
            continue;
        }

        atomic_fetch_add(&ctx->pkt_rx, nb_rx);

        /*
         * Distribute packets round-robin across worker rx_rings.
         * Alternative: RSS with dedicated NIC queues per worker —
         * then each worker calls rte_eth_rx_burst() on its own queue
         * and this RX lcore is not needed.
         *
         * Round-robin keeps flows from the same src IP on different workers
         * (no per-flow stickiness). For the DP application this is acceptable since
         * each DNS query is stateless from the policy perspective.
         * TLS SNI extraction uses the tls_session_table to
         * maintain per-connection state across packets.
         */
        for (uint16_t i = 0; i < nb_rx; i++) {
            uint32_t wid  = worker_rr % g_pipeline.worker_count;
            worker_rr++;

            if (unlikely(rte_ring_enqueue(g_pipeline.rx_rings[wid],
                                           mbufs[i]) != 0)) {
                /* Worker ring full: drop and free */
                rte_pktmbuf_free(mbufs[i]);
                atomic_fetch_add(&ctx->pkt_drop, 1);
            }
        }
    }

    printf("[lcore %u] RX stopped: rx=%lu drop=%lu\n",
           ctx->lcore_id,
           atomic_load(&ctx->pkt_rx),
           atomic_load(&ctx->pkt_drop));
    return 0;
}

/* ───────────────────────────────────────────────────────────
 * worker_lcore_func — parse + policy + forward/drop
 *
 * The core of the DP application. This lcore:
 *   1. Dequeues packets from its rx_ring
 *   2. Parses Ethernet / IP / UDP-TCP headers
 *   3. For DNS: parses query, looks up policy
 *   4. For TLS: extracts SNI, looks up policy
 *   5. ALLOW → enqueue to tx_ring
 *      DROP  → rte_pktmbuf_free()
 *      SINKHOLE → modify in-place, enqueue to tx_ring
 * ─────────────────────────────────────────────────────────── */
static int worker_lcore_func(void *arg)
{
    lcore_ctx_t    *ctx = (lcore_ctx_t *)arg;
    struct rte_mbuf *mbufs[BURST_SIZE];
    struct rte_mbuf *fwd[BURST_SIZE];
    uint16_t         nb_fwd;

    printf("[lcore %u] Worker started\n", ctx->lcore_id);

    while (ctx->running && !g_quit) {
        uint16_t nb = rte_ring_dequeue_burst(ctx->rx_ring,
                                              (void **)mbufs,
                                              BURST_SIZE, NULL);
        if (nb == 0) {
            rte_pause();
            continue;
        }

        nb_fwd = 0;

        for (uint16_t i = 0; i < nb; i++) {
            int is_dns = 0, is_tls = 0;
            int decision = parse_and_decide(mbufs[i], &is_dns, &is_tls);

            if (is_dns) atomic_fetch_add(&ctx->pkt_dns, 1);
            if (is_tls) atomic_fetch_add(&ctx->pkt_tls, 1);

            switch (decision) {

            case DECISION_ALLOW:
                fwd[nb_fwd++] = mbufs[i];
                break;

            case DECISION_DROP:
                rte_pktmbuf_free(mbufs[i]);
                atomic_fetch_add(&ctx->pkt_drop, 1);
                break;

            case DECISION_SINKHOLE:
                /*
                 * Real app calls:
                 *   dns_build_sinkhole_v4(mbuf, walled_garden_ip)
                 * which rewrites the packet in-place (Module 23).
                 * For now: just forward unmodified as a stub.
                 */
                fwd[nb_fwd++] = mbufs[i];
                atomic_fetch_add(&ctx->pkt_drop, 1); /* count as "enforced" */
                break;
            }
        }

        /* Enqueue forwarded packets to the TX ring */
        if (nb_fwd == 0)
            continue;

        uint16_t nb_enq = rte_ring_enqueue_burst(ctx->tx_ring,
                                                   (void **)fwd,
                                                   nb_fwd, NULL);
        atomic_fetch_add(&ctx->pkt_tx, nb_enq);

        /* Free packets that couldn't be enqueued (tx_ring full) */
        for (uint16_t i = nb_enq; i < nb_fwd; i++) {
            rte_pktmbuf_free(fwd[i]);
            atomic_fetch_add(&ctx->pkt_drop, 1);
        }
    }

    printf("[lcore %u] Worker stopped: dns=%lu tls=%lu tx=%lu drop=%lu\n",
           ctx->lcore_id,
           atomic_load(&ctx->pkt_dns),
           atomic_load(&ctx->pkt_tls),
           atomic_load(&ctx->pkt_tx),
           atomic_load(&ctx->pkt_drop));
    return 0;
}

/* ───────────────────────────────────────────────────────────
 * tx_lcore_func — dequeue from tx_ring, call rte_eth_tx_burst
 *
 * Separating TX into its own lcore prevents worker lcores from ever
 * blocking on NIC backpressure. If the NIC TX ring is temporarily full,
 * only this lcore stalls — workers keep processing.
 * ─────────────────────────────────────────────────────────── */
static int tx_lcore_func(void *arg)
{
    lcore_ctx_t    *ctx = (lcore_ctx_t *)arg;
    struct rte_mbuf *mbufs[BURST_SIZE];

    printf("[lcore %u] TX started: port=%u queue=%u\n",
           ctx->lcore_id, ctx->port_id, ctx->queue_id);

    while (ctx->running && !g_quit) {
        uint16_t nb = rte_ring_dequeue_burst(ctx->tx_ring,
                                              (void **)mbufs,
                                              BURST_SIZE, NULL);
        if (nb == 0) {
            rte_pause();
            continue;
        }

        /*
         * rte_eth_tx_burst: sends up to nb packets.
         * May return < nb if the NIC TX ring is full.
         * Unsent packets MUST be freed — otherwise the pool drains.
         *
         * The NIC frees the mbufs back to the pool after DMA completes
         * (for sent packets). The application must free unsent ones.
         */
        uint16_t nb_tx = rte_eth_tx_burst(ctx->port_id, ctx->queue_id,
                                           mbufs, nb);
        atomic_fetch_add(&ctx->pkt_tx, nb_tx);

        /* Free unsent: NIC TX ring was full */
        for (uint16_t i = nb_tx; i < nb; i++) {
            rte_pktmbuf_free(mbufs[i]);
            atomic_fetch_add(&ctx->pkt_drop, 1);
        }
    }

    /*
     * Drain remaining packets after stop signal.
     * Workers may have enqueued a final burst to tx_ring after
     * TX lcore got the stop signal. Drain before exiting.
     */
    uint16_t nb;
    do {
        nb = rte_ring_dequeue_burst(ctx->tx_ring,
                                     (void **)mbufs, BURST_SIZE, NULL);
        if (nb > 0) {
            uint16_t nb_tx = rte_eth_tx_burst(ctx->port_id, ctx->queue_id,
                                               mbufs, nb);
            for (uint16_t i = nb_tx; i < nb; i++)
                rte_pktmbuf_free(mbufs[i]);
        }
    } while (nb > 0);

    printf("[lcore %u] TX stopped: tx=%lu drop=%lu\n",
           ctx->lcore_id,
           atomic_load(&ctx->pkt_tx),
           atomic_load(&ctx->pkt_drop));
    return 0;
}

/* ───────────────────────────────────────────────────────────
 * print_pipeline_stats — main lcore prints aggregate stats
 * ─────────────────────────────────────────────────────────── */
static void print_pipeline_stats(void)
{
    unsigned long total_rx   = 0;
    unsigned long total_tx   = 0;
    unsigned long total_drop = 0;
    unsigned long total_dns  = 0;
    unsigned long total_tls  = 0;

    for (uint32_t i = 0; i < g_pipeline.worker_count; i++) {
        lcore_ctx_t *ctx = &g_pipeline.ctx[g_pipeline.worker_lcores[i]];
        total_dns  += atomic_load(&ctx->pkt_dns);
        total_tls  += atomic_load(&ctx->pkt_tls);
        total_tx   += atomic_load(&ctx->pkt_tx);
        total_drop += atomic_load(&ctx->pkt_drop);
    }
    total_rx = atomic_load(&g_pipeline.ctx[g_pipeline.rx_lcore].pkt_rx);

    printf("[Stats] rx=%-8lu  tx=%-8lu  drop=%-6lu  dns=%-6lu  tls=%-6lu"
           "  rings: rx=%u/%u tx=%u/%u\n",
           total_rx, total_tx, total_drop, total_dns, total_tls,
           rte_ring_count(g_pipeline.rx_rings[0]), RING_SIZE,
           rte_ring_count(g_pipeline.tx_ring),     RING_SIZE);
}

/* ───────────────────────────────────────────────────────────
 * pipeline_setup — create rings and assign lcore contexts
 * ─────────────────────────────────────────────────────────── */
static int pipeline_setup(struct rte_mempool *pool,
                            unsigned int rx_lcore,
                            unsigned int tx_lcore,
                            unsigned int *worker_lcores,
                            unsigned int nb_workers)
{
    char ring_name[64];

    g_pipeline.pool         = pool;
    g_pipeline.rx_lcore     = rx_lcore;
    g_pipeline.tx_lcore     = tx_lcore;
    g_pipeline.worker_count = nb_workers;

    /* Create one rx_ring per worker */
    for (uint32_t i = 0; i < nb_workers; i++) {
        snprintf(ring_name, sizeof(ring_name), "rx_ring_%u", i);
        /*
         * SPSC flags: Single Producer (RX lcore) + Single Consumer (worker i).
         * SPSC is faster than MPMC — no CAS needed.
         * If RSS is used instead of RX lcore distribution, each worker
         * calls rx_burst directly and no rx_ring is needed.
         */
        g_pipeline.rx_rings[i] = rte_ring_create(ring_name, RING_SIZE,
                                                   rte_socket_id(),
                                                   RING_F_SP_ENQ | RING_F_SC_DEQ);
        if (!g_pipeline.rx_rings[i]) {
            fprintf(stderr, "Cannot create rx_ring_%u\n", i);
            return -1;
        }
        g_pipeline.worker_lcores[i] = worker_lcores[i];
    }

    /* One shared tx_ring: multiple producers (workers) → one consumer (TX lcore) */
    g_pipeline.tx_ring = rte_ring_create("tx_ring", RING_SIZE,
                                          rte_socket_id(), 0); /* MPSC */
    if (!g_pipeline.tx_ring) {
        fprintf(stderr, "Cannot create tx_ring\n");
        return -1;
    }

    /* Initialise RX lcore context */
    lcore_ctx_t *rx_ctx      = &g_pipeline.ctx[rx_lcore];
    rx_ctx->lcore_id         = rx_lcore;
    rx_ctx->port_id          = PORT_ID;
    rx_ctx->queue_id         = RX_QUEUE_ID;
    rx_ctx->running          = 1;

    /* Initialise TX lcore context */
    lcore_ctx_t *tx_ctx      = &g_pipeline.ctx[tx_lcore];
    tx_ctx->lcore_id         = tx_lcore;
    tx_ctx->port_id          = PORT_ID;
    tx_ctx->queue_id         = TX_QUEUE_ID;
    tx_ctx->tx_ring          = g_pipeline.tx_ring;
    tx_ctx->running          = 1;

    /* Initialise worker lcore contexts */
    for (uint32_t i = 0; i < nb_workers; i++) {
        lcore_ctx_t *w   = &g_pipeline.ctx[worker_lcores[i]];
        w->lcore_id      = worker_lcores[i];
        w->port_id       = PORT_ID;
        w->queue_id      = 0;
        w->rx_ring       = g_pipeline.rx_rings[i];
        w->tx_ring       = g_pipeline.tx_ring;
        w->running       = 1;
    }

    printf("[Pipeline] Created %u rx_rings + 1 tx_ring (%u slots each)\n",
           nb_workers, RING_SIZE);
    return 0;
}

/* ─── Signal handler ────────────────────────────────────── */
static void sig_handler(int sig)
{
    (void)sig;
    g_quit = 1;
}

/* ─── Minimal EAL args ───────────────────────────────────── */
static const char *eal_args[] = {
    "pipeline", "-l", "0-5", "--socket-mem", "512",
    "-n", "4", "--proc-type", "auto",
};

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    signal(SIGINT,  sig_handler);
    signal(SIGTERM, sig_handler);

    printf("=== Module 11: Multi-lcore RX/TX Pipeline ===\n\n");

    /* EAL init */
    int ret = rte_eal_init(
        (int)(sizeof(eal_args) / sizeof(eal_args[0])),
        (char **)(uintptr_t)eal_args);
    if (ret < 0)
        rte_exit(EXIT_FAILURE, "rte_eal_init: %s\n", rte_strerror(rte_errno));

    /* Mempool */
    struct rte_mempool *pool = rte_pktmbuf_pool_create(
        "pipeline_pool", 8191, 256, 0,
        RTE_MBUF_DEFAULT_BUF_SIZE, rte_socket_id());
    if (!pool)
        rte_exit(EXIT_FAILURE, "pool create failed\n");

    /*
     * Port init would go here (Module 10):
     *   port_init(PORT_ID, pool);
     * Omitted to keep this module self-contained without a NIC.
     */

    /* Setup pipeline rings and contexts */
    unsigned int worker_lcores[] = {2, 3, 4, 5};
    unsigned int nb_workers = 4;

    if (pipeline_setup(pool, 1, /* rx_lcore */
                               1, /* tx_lcore (same as rx for demo) */
                               worker_lcores, nb_workers) < 0)
        rte_exit(EXIT_FAILURE, "pipeline_setup failed\n");

    /* ── Launch worker lcores ── */
    printf("[Launch] Starting pipeline lcores...\n");

    /* TX lcore */
    rte_eal_remote_launch(tx_lcore_func,
                           &g_pipeline.ctx[g_pipeline.tx_lcore],
                           g_pipeline.tx_lcore);

    /* Worker lcores */
    for (uint32_t i = 0; i < nb_workers; i++) {
        rte_eal_remote_launch(worker_lcore_func,
                               &g_pipeline.ctx[worker_lcores[i]],
                               worker_lcores[i]);
    }

    /*
     * Note: RX lcore is NOT launched here because we have no physical NIC.
     * In a real app with a NIC:
     *   rte_eal_remote_launch(rx_lcore_func,
     *                          &g_pipeline.ctx[g_pipeline.rx_lcore],
     *                          g_pipeline.rx_lcore);
     *
     * Instead, the main lcore injects fake packets to demonstrate the
     * worker and TX path.
     */

    /* ── Main lcore: inject test packets ── */
    printf("[Main] Injecting test packets into worker rings...\n");
    uint64_t injected = 0;

    for (int round = 0; round < 10 && !g_quit; round++) {
        for (uint32_t w = 0; w < nb_workers && !g_quit; w++) {
            struct rte_mbuf *m = rte_pktmbuf_alloc(pool);
            if (!m) continue;

            /* Build a minimal Ethernet frame */
            struct rte_ether_hdr *eth =
                (struct rte_ether_hdr *)rte_pktmbuf_append(m, 60);
            if (eth) {
                memset(eth, 0, 60);
                eth->ether_type = rte_cpu_to_be_16(RTE_ETHER_TYPE_IPV4);
            }

            if (rte_ring_enqueue(g_pipeline.rx_rings[w], m) != 0)
                rte_pktmbuf_free(m);
            else
                injected++;
        }
        rte_delay_ms(50);
        print_pipeline_stats();
    }

    /* ── Graceful shutdown ── */
    printf("\n[Shutdown] Stopping all lcores...\n");
    g_quit = 1;

    /* Stop workers first, then TX (so TX can drain the ring) */
    for (uint32_t i = 0; i < nb_workers; i++)
        g_pipeline.ctx[worker_lcores[i]].running = 0;
    for (uint32_t i = 0; i < nb_workers; i++)
        rte_eal_wait_lcore(worker_lcores[i]);

    g_pipeline.ctx[g_pipeline.tx_lcore].running = 0;
    rte_eal_wait_lcore(g_pipeline.tx_lcore);

    printf("[Main] injected=%lu packets\n", injected);
    print_pipeline_stats();

    rte_eal_cleanup();
    printf("\n=== Pipeline demo complete ===\n");
    return 0;
}
