/**
 * full_pipeline.c — Module 21: Full Pipeline (Annotated Assembly)
 *
 * This file assembles all 20 prior modules into one complete dataplane
 * application. Every significant call is annotated with the module it
 * came from. Read this file top-to-bottom to understand how a production
 * DPDK-based URL filtering engine is structured.
 *
 * ══════════════════════════════════════════════════════════════════
 * SYSTEM ARCHITECTURE
 * ══════════════════════════════════════════════════════════════════
 *
 *  ┌─────────────────────────────────────────────────────────┐
 *  │                      the DP application Process                    │
 *  │                                                         │
 *  │  lcore 0 (main)   lcore 1 (RX)   lcore 2 (TX)         │
 *  │  ┌──────────┐     ┌──────────┐   ┌──────────┐          │
 *  │  │  Kafka   │     │ rx_burst │   │ tx_burst │          │
 *  │  │  consumer│     │    ↓     │   │    ↑     │          │
 *  │  │  policy  │     │  rings   │   │  rings   │          │
 *  │  │  update  │     └──────────┘   └──────────┘          │
 *  │  │  CDR     │                                           │
 *  │  │  flush   │   lcores 3-6 (workers)                   │
 *  │  │  stats   │   ┌──────────────────────────┐           │
 *  │  └──────────┘   │ parse ETH/IP/UDP-TCP      │           │
 *  │                  │ DNS: dns_parse → policy   │           │
 *  │                  │ TLS: hs_scan → SNI        │           │
 *  │                  │ ALLOW→tx / DROP→free      │           │
 *  │                  │ SINKHOLE→rewrite→tx       │           │
 *  │                  │ CDR batch add             │           │
 *  │                  └──────────────────────────┘           │
 *  └─────────────────────────────────────────────────────────┘
 *           │  Kafka CDR         │  Kafka policy
 *           ▼                    ▼
 *     ┌──────────┐        ┌──────────────┐
 *     │  Kafka   │        │  PM          │
 *     │  Broker  │        │ (Provisioning│
 *     └──────────┘        │  Module)     │
 *                         └──────────────┘
 *
 * ══════════════════════════════════════════════════════════════════
 * TWO BUILD MODES
 * ══════════════════════════════════════════════════════════════════
 *
 *   make simulate   → pure C, runs anywhere, synthetic packets
 *                     Uses: Module 03 rings, Module 04/17 policy
 *
 *   make production → DPDK + Hyperscan + rdkafka (real hardware)
 *                     Uses: all module APIs as documented below
 *
 * ══════════════════════════════════════════════════════════════════
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdatomic.h>
#include <signal.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>
#include <ctype.h>
#include <arpa/inet.h>

/* ─── Module 05: packet structs ──────────────────────────── */
#include "../05-packet-structs/packet_structs.h"

/* ─── Module 03: ring buffer (replaces rte_ring in simulate) */
#include "../03-ring-buffer/ring.h"

/* ─── Module 17: policy lookup decision codes ───────────── */
#define ALLOW_PACKET      0
#define DROP_PACKET       1
#define PROCESS_WORKFLOW  2    /* sinkhole */

/* ─── Module 15: Hyperscan (optional) ───────────────────── */
#ifdef WITH_HYPERSCAN
#include <hs.h>
#endif

/* ─── Module 19/20: Kafka (optional) ────────────────────── */
#ifdef WITH_KAFKA
#include <librdkafka/rdkafka.h>
#endif

/* ═══════════════════════════════════════════════════════════
 * SECTION 1: CONSTANTS + CONFIGURATION
 *
 * In production (app_main.c): read from config file via Module 01.
 * Here: hardcoded for the simulation demo.
 * ═══════════════════════════════════════════════════════════ */

#define NUM_WORKERS       2        /* worker lcore count (Module 08) */
#define RING_SZ           512      /* inter-lcore ring depth (Module 03) */
#define BURST_SIZE        16       /* packets per burst (Module 11) */
#define WALLED_GARDEN_IP  0x0A010101  /* 10.1.1.1 (Module 18) */
#define CDR_BATCH_MAX     64       /* CDR batch size (Module 19) */
#define SIMULATION_PKTS   1000     /* total packets to simulate */

/* ═══════════════════════════════════════════════════════════
 * SECTION 2: PER-LCORE CONTEXT
 *
 * In production: worker_lcore_info_t (Module 08) contains:
 *   hs_scratch_t *worker_scratch   ← Module 16
 *   cdr_batch_t   cdr_batch        ← Module 19
 *   rte_ring     *rx_ring          ← Module 11
 *   rte_ring     *tx_ring          ← Module 11
 *   atomic stats                   ← Module 13
 * ═══════════════════════════════════════════════════════════ */
typedef struct {
    int          lcore_id;
    ring_t      *rx_ring;          /* ← Module 03/11: inbound packets       */
    ring_t      *tx_ring;          /* ← Module 03/11: outbound packets       */
    volatile int running;

    /* Stats (Module 13: atomic counters) */
    atomic_ulong pkt_rx;
    atomic_ulong pkt_tx;
    atomic_ulong pkt_drop;
    atomic_ulong pkt_dns;
    atomic_ulong pkt_tls;
    atomic_ulong pkt_sinkholes;
    atomic_ulong cdr_produced;
} __attribute__((aligned(64))) worker_ctx_t;

/* ═══════════════════════════════════════════════════════════
 * SECTION 3: POLICY STATE
 *
 * In production:
 *   group_struct (policy_cache.h) has:
 *     rte_hash *domain_details_table   ← Module 12
 *     hs_database_t *database          ← Module 15
 *     dp_hyperscan_details *hyperscan_details ← Module 15
 *   ip_vs_subscriber_table                   ← Module 12 (500K entries)
 *   malicious_domain_table   ← Module 12 + Module 20
 * ═══════════════════════════════════════════════════════════ */
typedef struct {
    char    domain[256];
    int     is_whitelisted;
    int     is_blacklisted;
    uint32_t category;
} policy_entry_t;

/* Simplified in-memory policy store (replaces rte_hash, Module 12) */
#define MAX_POLICY_ENTRIES  128
static policy_entry_t  g_policy[MAX_POLICY_ENTRIES];
static int             g_policy_count = 0;
static pthread_rwlock_t g_policy_lock = PTHREAD_RWLOCK_INITIALIZER;

/* Malicious domain list (Module 20: populated from IDPS feed via Kafka) */
static char   g_malicious[64][256];
static int    g_malicious_count = 0;

/* ═══════════════════════════════════════════════════════════
 * SECTION 4: GLOBAL PIPELINE STATE
 * ═══════════════════════════════════════════════════════════ */
#define MAX_LCORES  8

static ring_t      *g_rx_rings[NUM_WORKERS];  /* RX → each worker (Module 11) */
static ring_t      *g_tx_ring;                 /* workers → TX (Module 11)     */
static worker_ctx_t g_ctx[MAX_LCORES];
static volatile int g_shutdown = 0;

/* ═══════════════════════════════════════════════════════════
 * SECTION 5: SIMULATED PACKET POOL
 *
 * In production: rte_pktmbuf_pool_create() → Module 09
 * Here: fixed-size byte arrays simulate mbufs.
 * ═══════════════════════════════════════════════════════════ */
#define PKT_BUF_SIZE  256
typedef struct {
    uint8_t data[PKT_BUF_SIZE];
    int     data_len;
    int     is_dns;       /* pre-parsed flag for simulation */
    int     is_tls;
    char    domain[256];  /* pre-extracted for simulation */
    int     qtype;
} sim_mbuf_t;

/* Pool of pre-allocated mbufs (circular) */
#define POOL_SIZE  256
static sim_mbuf_t  g_pool[POOL_SIZE];
static int         g_pool_head = 0;
static pthread_mutex_t g_pool_mutex = PTHREAD_MUTEX_INITIALIZER;

static sim_mbuf_t *pool_alloc(void)
{
    pthread_mutex_lock(&g_pool_mutex);
    sim_mbuf_t *m = &g_pool[g_pool_head % POOL_SIZE];
    g_pool_head++;
    pthread_mutex_unlock(&g_pool_mutex);
    return m;
}
/* pool_free: in simulation just mark as available; in DPDK: rte_pktmbuf_free() */
static void pool_free(sim_mbuf_t *m) { (void)m; }

/* ═══════════════════════════════════════════════════════════
 * SECTION 6: POLICY LOOKUP
 *
 * In production (Module 17):
 *   url_policy_for_dns(domain, qtype, groups, n)
 *     → check_malicious()          rte_hash_lookup(malicious_table, domain)
 *     → fetch_group_url_details()
 *         Tier 1: rte_hash_lookup_data(domain_details_table, domain, &fd)
 *         Tier 2: hs_scan_domain_group(domain, group->database, scratch)
 *     → apply_filter_details(fd, group, port)
 * ═══════════════════════════════════════════════════════════ */
static int policy_lookup(const char *domain)
{
    /* ── Malicious check (Module 17, 20) ── */
    for (int i = 0; i < g_malicious_count; i++) {
        if (strcasecmp(g_malicious[i], domain) == 0)
            return PROCESS_WORKFLOW;   /* malicious → sinkhole */
    }

    /* ── Tier 1: exact match (Module 12: rte_hash_lookup_data) ── */
    pthread_rwlock_rdlock(&g_policy_lock);
    for (int i = 0; i < g_policy_count; i++) {
        if (strcasecmp(g_policy[i].domain, domain) == 0) {
            int r;
            if      (g_policy[i].is_whitelisted) r = ALLOW_PACKET;
            else if (g_policy[i].is_blacklisted)  r = PROCESS_WORKFLOW;
            else                                   r = ALLOW_PACKET;
            pthread_rwlock_unlock(&g_policy_lock);
            return r;
        }
    }
    pthread_rwlock_unlock(&g_policy_lock);

    /*
     * Tier 2: Hyperscan fallback (Module 16: hs_scan_domain_group)
     * In production:
     *   hs_scan(group->database, domain, strlen(domain), 0,
     *           worker_scratch, on_hs_match_group, &matchCtx)
     * Simulation: treat unknown domains as ALLOW (default policy)
     */
    return ALLOW_PACKET;
}

/* ═══════════════════════════════════════════════════════════
 * SECTION 7: DNS SINKHOLE
 *
 * In production (Module 18):
 *   dns_build_sinkhole_v4(mbuf, wg_ipv4)
 *   → swap ETH/IP/UDP headers in-place
 *   → append DNS answer section (A or AAAA record)
 *   → set TX hardware checksum offload flags on mbuf
 *
 * Simulation: mark the mbuf as a sinkhole response.
 * ═══════════════════════════════════════════════════════════ */
static void apply_sinkhole(sim_mbuf_t *m)
{
    /*
     * Production code (pkt_proc.h):
     *   if (qtype == DNS_TYPE_A)
     *       dns_build_sinkhole_v4(
     *           mbuf, walled_garden_ipv4);
     *   else
     *       dns_build_sinkhole_v4(
     *           mbuf, walled_garden_ipv4);  // AAAA answer injected inside
     *
     *   m->ol_flags |= RTE_MBUF_F_TX_IPV4 | RTE_MBUF_F_TX_IP_CKSUM
     *               |  RTE_MBUF_F_TX_UDP_CKSUM;
     */
    m->data[0] = 0xSINKHOLE_MARKER;   /* simulation flag */
    (void)m; /* suppress unused variable warning in simulation */
}

/* ═══════════════════════════════════════════════════════════
 * SECTION 8: CDR BATCH
 *
 * In production (Module 19):
 *   cdr_batch_add(&worker_info->cdr_batch, &rec)
 *   → batch accumulates; when full: rd_kafka_produce() per CDR
 *   → main lcore: rd_kafka_poll() + cdr_batch_flush_if_timeout()
 * ═══════════════════════════════════════════════════════════ */
typedef struct {
    char   domain[256];
    int    action;
    uint64_t ts;
} cdr_rec_t;

typedef struct {
    cdr_rec_t records[CDR_BATCH_MAX];
    int       count;
} cdr_batch_t;

static void cdr_add(cdr_batch_t *batch, const char *domain, int action,
                    atomic_ulong *produced_counter)
{
    if (batch->count >= CDR_BATCH_MAX) {
        /*
         * Production (Module 19):
         *   for (i=0; i<count; i++)
         *       rd_kafka_produce(cdr_topic, partition,
         *                        RD_KAFKA_MSG_F_COPY,
         *                        json_buf, json_len, &subscriber_ip, 4, NULL)
         *   rd_kafka_poll(producer, 0)
         */
        batch->count = 0;   /* simulation: just reset */
    }

    struct timespec ts;
    clock_gettime(CLOCK_REALTIME, &ts);

    batch->records[batch->count].action  = action;
    batch->records[batch->count].ts      = (uint64_t)ts.tv_sec * 1000 +
                                            ts.tv_nsec / 1000000;
    strncpy(batch->records[batch->count].domain, domain, 255);
    batch->count++;
    atomic_fetch_add_explicit(produced_counter, 1, memory_order_relaxed);
}

/* ═══════════════════════════════════════════════════════════
 * SECTION 9: RX LCORE
 *
 * In production (Module 11):
 *   while (running) {
 *       nb_rx = rte_eth_rx_burst(port, queue, mbufs, BURST_SIZE);  ← Module 10
 *       if (nb_rx == 0) { rte_pause(); continue; }
 *       distribute round-robin to worker rx_rings via rte_ring_enqueue_burst
 *   }
 * ═══════════════════════════════════════════════════════════ */

/* Synthetic packet generator — simulates NIC delivering DNS/TLS packets */
static sim_mbuf_t *generate_synthetic_packet(int seq)
{
    static const char *dns_domains[] = {
        "google.com",             /* will be whitelisted */
        "facebook.com",           /* will be blacklisted */
        "github.com",             /* unknown → allow */
        "malware-download.ru",    /* malicious table → sinkhole */
        "ads.doubleclick.net",    /* policy blocked */
        "internal.corp.local",    /* unknown → allow */
        "youtube.com",            /* unknown → allow */
        "phishing-bank.xyz",      /* malicious */
    };
    int n_dns = 8;
    const char *tls_domains[] = { "blocked-https.example.com", "allowed-cdn.net" };

    sim_mbuf_t *m = pool_alloc();
    memset(m, 0, sizeof(*m));
    m->data_len = PKT_BUF_SIZE;

    if (seq % 5 == 0) {
        /* TLS packet (Module 07) */
        m->is_tls = 1;
        strncpy(m->domain, tls_domains[seq % 2], 255);
        m->qtype  = 0;

        /*
         * Production: TCP payload begins with TLS record (0x16).
         * hs_scan_payload(payload, len, worker_scratch, &matchCtx)
         * → on_hs_match callback with id=HS_PATTERN_ID_TLS=1
         * → read SNI at from+7 / from+9 (Module 07, Module 16)
         */
        m->data[0] = 0x16;  /* TLS Handshake content type */

    } else {
        /* DNS packet (Module 06) */
        m->is_dns = 1;
        strncpy(m->domain, dns_domains[seq % n_dns], 255);
        m->qtype  = (seq % 3 == 0) ? 28 : 1;  /* mix A and AAAA */

        /*
         * Production: UDP dst_port==53 detected.
         * dns_parse_message(udp_payload, udp_len, &msg)  ← Module 06
         * → msg.qname = domain, msg.qtype, msg.question_wire_end
         */
        eth_hdr_t *eth = (eth_hdr_t *)m->data;
        eth->ether_type = htons(ETHER_TYPE_IPV4);
        ipv4_hdr_t *ip4 = (ipv4_hdr_t *)(m->data + ETH_HDR_LEN);
        ip4->proto    = IP_PROTO_UDP;
        ip4->src_ip   = htonl(0xC0A80100 + (seq % 200));
        ip4->dst_ip   = htonl(0x08080808);
        ip4->version_ihl = 0x45;
        udp_hdr_t *udp = (udp_hdr_t *)(m->data + ETH_HDR_LEN + IPV4_HDR_MIN);
        udp->dst_port = htons(PORT_DNS);
        udp->src_port = htons(10000 + (seq % 50000));
    }

    return m;
}

static void *rx_lcore_func(void *arg)
{
    worker_ctx_t *ctx = (worker_ctx_t *)arg;
    int           seq = 0;
    int           worker_rr = 0;

    printf("[lcore %d] RX started\n", ctx->lcore_id);

    while (ctx->running && !g_shutdown && seq < SIMULATION_PKTS) {

        /* ── Generate/receive a burst ──
         * Production: nb_rx = rte_eth_rx_burst(port, queue, mbufs, BURST_SIZE)
         * Simulation: generate synthetic packets
         */
        sim_mbuf_t *burst[BURST_SIZE];
        int nb_rx = 0;

        for (int i = 0; i < BURST_SIZE && seq < SIMULATION_PKTS; i++, seq++) {
            burst[nb_rx++] = generate_synthetic_packet(seq);
        }

        if (nb_rx == 0) { usleep(100); continue; }

        atomic_fetch_add_explicit(&ctx->pkt_rx, nb_rx, memory_order_relaxed);

        /* ── Distribute round-robin to worker rings ──
         * Production: rte_ring_enqueue() per packet into g_rx_rings[worker_rr]
         */
        for (int i = 0; i < nb_rx; i++) {
            int wid = worker_rr % NUM_WORKERS;
            worker_rr++;
            if (ring_enqueue(g_rx_rings[wid], burst[i]) != RING_OK) {
                pool_free(burst[i]);
                atomic_fetch_add_explicit(&ctx->pkt_drop, 1, memory_order_relaxed);
            }
        }
    }

    printf("[lcore %d] RX done: rx=%lu drop=%lu\n",
           ctx->lcore_id,
           atomic_load(&ctx->pkt_rx), atomic_load(&ctx->pkt_drop));
    return NULL;
}

/* ═══════════════════════════════════════════════════════════
 * SECTION 10: WORKER LCORE (THE HOT PATH)
 *
 * This is the core of the DP application. Every packet flows through here.
 * In production: runs on a dedicated physical CPU core pinned by DPDK EAL.
 * ═══════════════════════════════════════════════════════════ */
static void *worker_lcore_func(void *arg)
{
    worker_ctx_t *ctx    = (worker_ctx_t *)arg;
    cdr_batch_t   cdr    = {0};
    void         *burst[BURST_SIZE];
    int           nb;

    printf("[lcore %d] Worker started\n", ctx->lcore_id);

    /*
     * Production startup (called before launch, Module 16):
     *   hs_clone_scratch_for_lcore(&worker_info->worker_scratch, lcore_id)
     *   hs_alloc_scratch(group->database, &worker_info->worker_scratch)
     */

    while (ctx->running && !g_shutdown) {

        /* ── Dequeue from RX ring ──
         * Production: rte_ring_dequeue_burst(ctx->rx_ring, mbufs, BURST_SIZE, NULL)
         */
        nb = (int)ring_dequeue_burst(ctx->rx_ring, burst, BURST_SIZE);
        if (nb == 0) { usleep(10); continue; }

        for (int i = 0; i < nb; i++) {
            sim_mbuf_t *m = (sim_mbuf_t *)burst[i];
            int decision  = ALLOW_PACKET;
            const char *domain = m->domain;

            /* ════════ HOT PATH START ════════ */

            /* ── Guard: multi-segment mbuf (Module 09/11) ──
             * Production: if (unlikely(m->nb_segs > 1)) { drop; continue; }
             */

            /* ── Layer 2/3/4 parse (Module 05) ──
             * Production:
             *   eth  = rte_pktmbuf_mtod(m, struct rte_ether_hdr *)
             *   ip4  = (ipv4_hdr_t *)(eth + 1)
             *   udp  = (udp_hdr_t *)((uint8_t *)ip4 + rte_ipv4_hdr_len(ip4))
             *   tcp  = same offset for TCP
             */

            if (m->is_dns) {
                /* ── DNS packet path ──────────────────────────── */
                atomic_fetch_add_explicit(&ctx->pkt_dns, 1, memory_order_relaxed);

                /* ── DNS parse (Module 06) ──
                 * Production:
                 *   parse_dns_ipv4_request_packet_over_udp(mbuf, worker_info, ...)
                 *     → dns_parse_message(udp_payload, udp_len, &msg)
                 *     → domain = msg.qname  (normalised to lowercase)
                 *     → qtype  = msg.qtype  (A=1 or AAAA=28)
                 *     → question_wire_end = msg.question_wire_end
                 */

                /* ── Subscriber lookup (Module 12: ip_vs_subscriber_table) ──
                 * Production:
                 *   rte_hash_lookup_data(ip_vs_subscriber_table, &src_ip, &sub)
                 *   group_id = sub->group_id
                 */

                /* ── Two-tier policy lookup (Module 17) ──
                 * Production:
                 *   url_policy_for_dns(
                 *       domain, qtype, groups, n_groups)
                 *     → check_malicious_domain()
                 *     → fetch_url_policy_for_domain()
                 *         Tier 1: rte_hash_lookup_data(domain_details_table,...)
                 *         Tier 2: hs_scan_domain_group(domain, db, scratch)
                 *     → apply_filter_details(fd, group, port)
                 */
                decision = policy_lookup(domain);

                if (decision == PROCESS_WORKFLOW) {
                    /* ── DNS Sinkhole (Module 18) ──
                     * Production:
                     *   dns_build_sinkhole_v4(mbuf, wg_ip)
                     *     → swap ETH/IP/UDP src↔dst
                     *     → set DNS QR=1, ancount=1
                     *     → rte_pktmbuf_append(mbuf, answer_len)
                     *     → build A/AAAA answer (walled garden IP)
                     *     → update total_len, dgram_len
                     *     → m->ol_flags |= TX_IPV4|TX_IP_CKSUM|TX_UDP_CKSUM
                     */
                    apply_sinkhole(m);
                    atomic_fetch_add_explicit(&ctx->pkt_sinkholes, 1,
                                              memory_order_relaxed);
                }

            } else if (m->is_tls) {
                /* ── TLS/HTTPS packet path ─────────────────────── */
                atomic_fetch_add_explicit(&ctx->pkt_tls, 1, memory_order_relaxed);

                /* ── TLS SNI extraction (Module 07, Module 16) ──
                 * Production:
                 *   hs_scan_payload(payload, len, worker_scratch, &matchCtx)
                 *     → Hyperscan fires id=HS_PATTERN_ID_TLS=1
                 *     → on_hs_match:
                 *         sni_len = read_u16_be(payload + from + 7)
                 *         memcpy(domain, payload + from + 9, sni_len)
                 */

                /* ── TLS policy lookup (Module 17) ──
                 * Production:
                 *   url_policy_for_tls(domain, worker_info, ...)
                 */
                decision = policy_lookup(domain);

                if (decision == DROP_PACKET || decision == PROCESS_WORKFLOW) {
                    /* ── TCP RST injection for blocked TLS ──
                     * Production: inject_tcp_rst(mbuf)
                     *   → build RST packet in-place
                     *   → similar to DNS sinkhole but TCP RST not DNS answer
                     */
                }
            }

            /* ════════ POLICY DECISION APPLIED ════════ */

            /* ── CDR record (Module 19) ──
             * Production: cdr_batch_add(&worker_info->cdr_batch, &rec)
             * Every decision generates a CDR (allow, drop, sinkhole).
             */
            cdr_add(&cdr, domain, decision, &ctx->cdr_produced);

            /* ── Route packet ── */
            if (decision == DROP_PACKET) {
                pool_free(m);
                atomic_fetch_add_explicit(&ctx->pkt_drop, 1, memory_order_relaxed);

            } else {
                /* ALLOW or SINKHOLE — forward to TX ring */
                if (ring_enqueue(g_tx_ring, m) != RING_OK) {
                    pool_free(m);
                    atomic_fetch_add_explicit(&ctx->pkt_drop, 1, memory_order_relaxed);
                } else {
                    atomic_fetch_add_explicit(&ctx->pkt_tx, 1, memory_order_relaxed);
                }
            }

            /* ════════ HOT PATH END ════════ */
        }
    }

    /* Flush remaining CDR batch on exit */
    /*
     * Production: for (i=0; i<cdr.count; i++)
     *   rd_kafka_produce(cdr_topic, ..., json_cdr, ...)
     */

    printf("[lcore %d] Worker done: dns=%lu tls=%lu sinkhole=%lu "
           "drop=%lu cdr=%lu\n",
           ctx->lcore_id,
           atomic_load(&ctx->pkt_dns),
           atomic_load(&ctx->pkt_tls),
           atomic_load(&ctx->pkt_sinkholes),
           atomic_load(&ctx->pkt_drop),
           atomic_load(&ctx->cdr_produced));
    return NULL;
}

/* ═══════════════════════════════════════════════════════════
 * SECTION 11: TX LCORE (Module 11)
 * ═══════════════════════════════════════════════════════════ */
static void *tx_lcore_func(void *arg)
{
    worker_ctx_t *ctx = (worker_ctx_t *)arg;
    void         *burst[BURST_SIZE];
    int           nb;

    printf("[lcore %d] TX started\n", ctx->lcore_id);

    while (ctx->running && !g_shutdown) {
        /* Production: rte_ring_dequeue_burst(tx_ring, mbufs, BURST) */
        nb = (int)ring_dequeue_burst(g_tx_ring, burst, BURST_SIZE);
        if (nb == 0) { usleep(10); continue; }

        /*
         * Production:
         *   nb_tx = rte_eth_tx_burst(port, queue, mbufs, nb)  ← Module 10
         *   for (i=nb_tx; i<nb; i++) rte_pktmbuf_free(mbufs[i])  ← Module 09
         *   NIC hardware computes checksums (TX_IP_CKSUM, TX_UDP_CKSUM flags)
         */
        for (int i = 0; i < nb; i++) pool_free((sim_mbuf_t *)burst[i]);
        atomic_fetch_add_explicit(&ctx->pkt_tx, nb, memory_order_relaxed);
    }

    /* Drain remaining packets */
    while (ring_dequeue(g_tx_ring, (void **)burst) == RING_OK)
        pool_free((sim_mbuf_t *)burst[0]);

    printf("[lcore %d] TX done: tx=%lu\n",
           ctx->lcore_id, atomic_load(&ctx->pkt_tx));
    return NULL;
}

/* ═══════════════════════════════════════════════════════════
 * SECTION 12: MAIN LCORE CONTROL LOOP
 *
 * In production, the main lcore (lcore 0) handles:
 *   1. Kafka consumer poll — receive policy updates (Module 20)
 *   2. CDR producer poll   — trigger delivery callbacks (Module 19)
 *   3. CDR batch flush     — timer-based flush (Module 19)
 *   4. Stats printing      — aggregate per-lcore counters (Module 13)
 *   5. SIGTERM handling    — initiate graceful shutdown
 * ═══════════════════════════════════════════════════════════ */
static void main_control_loop(void)
{
    /*
     * Production Kafka consumer init (Module 20):
     *   rk_consumer = kafka_consumer_init(broker, "dp_consumer")
     *   rd_kafka_subscribe(rk_consumer, {"policy_updates"})
     */

    int ticks = 0;

    while (!g_shutdown) {
        usleep(100000);  /* 100ms (production: non-blocking rd_kafka_consumer_poll) */
        ticks++;

        /* ── Kafka consumer poll (Module 20) ──
         * Production:
         *   msg = rd_kafka_consumer_poll(rk_consumer, 0)
         *   if (msg) {
         *     pmsg = parse_policy_message(msg->payload, msg->len)
         *     apply_policy_message(&pmsg)
         *     if (pmsg.type == SYNC_COMPLETE)
         *       rd_kafka_commit_message(rk_consumer, msg, 0)
         *   }
         */

        /* Simulate a policy update at tick 5 */
        if (ticks == 5) {
            printf("\n[Main] Simulating Kafka policy update (SYNC_COMPLETE)...\n");

            /*
             * Production sequence (Module 20):
             *   BEGIN_SYNC:    build pending domain table
             *   ADD_DOMAIN × N: fill pending table
             *   SYNC_COMPLETE:
             *     atomic_swap(group->domain_details_table ← pending)
             *     rte_rcu_qsbr_synchronize(qsbr) ← wait for workers to quiesce
             *     rte_hash_free(old_table)
             *     hs_db_compile_for_groups(group)
             */
            pthread_rwlock_wrlock(&g_policy_lock);
            if (g_policy_count < MAX_POLICY_ENTRIES) {
                strncpy(g_policy[g_policy_count].domain, "new-blocked.com", 255);
                g_policy[g_policy_count].is_blacklisted = 1;
                g_policy_count++;
                printf("[Main] Policy updated: new-blocked.com → blacklist\n");
            }
            pthread_rwlock_unlock(&g_policy_lock);
        }

        /* ── CDR producer poll (Module 19) ──
         * Production: rd_kafka_poll(rk_producer, 0)
         */

        /* ── Stats (Module 13) ──
         * Aggregate per-lcore atomic counters.
         */
        if (ticks % 10 == 0) {
            unsigned long tot_dns = 0, tot_sinkhole = 0, tot_drop = 0;
            for (int i = 0; i < MAX_LCORES; i++) {
                tot_dns      += atomic_load(&g_ctx[i].pkt_dns);
                tot_sinkhole += atomic_load(&g_ctx[i].pkt_sinkholes);
                tot_drop     += atomic_load(&g_ctx[i].pkt_drop);
            }
            printf("[Stats] dns=%lu  sinkhole=%lu  drop=%lu\n",
                   tot_dns, tot_sinkhole, tot_drop);
        }
    }

    /*
     * Production shutdown (Module 19/20):
     *   rd_kafka_flush(rk_producer, 5000)
     *   rd_kafka_consumer_close(rk_consumer)
     *   rd_kafka_destroy(rk_producer)
     *   rd_kafka_destroy(rk_consumer)
     */
}

/* ─── Signal handler ────────────────────────────────────── */
static void sig_handler(int sig) { (void)sig; g_shutdown = 1; }

/* ═══════════════════════════════════════════════════════════
 * SECTION 13: STARTUP SEQUENCE
 *
 * Order matters. Each step depends on the one before.
 * ═══════════════════════════════════════════════════════════ */
int main(void)
{
    signal(SIGINT,  sig_handler);
    signal(SIGTERM, sig_handler);

    printf("=== Module 21: Full Pipeline ===\n");
    printf("Simulating %d packets across %d workers\n\n",
           SIMULATION_PKTS, NUM_WORKERS);

    /* ══ Step 1: Config (Module 01) ══
     * Production: config_load(&cfg, "/etc/dp_app/dp_app.conf")
     * Reads: eal.cores, port.num_rx_queues, kafka.broker,
     *        policy.pattern_file, logging.level, ...
     */
    printf("[1] Config loaded\n");

    /* ══ Step 2: Logger (Module 02) ══
     * Production: logger_init(level_str, log_file_path)
     * Must be before ALL other subsystems — they log during init.
     */
    printf("[2] Logger initialized\n");

    /* ══ Step 3: EAL init (Module 08) ══
     * Production:
     *   build_eal_args(cores, socket_mem, mem_channels, log_level)
     *   ret = rte_eal_init(eal_argc, eal_argv)
     *   if (ret < 0) rte_exit(EXIT_FAILURE, "EAL init failed")
     *
     *   After this: hugepages locked, lcores pinned, NICs probed.
     */
    printf("[3] EAL initialized (simulation: using pthreads)\n");

    /* ══ Step 4: Mempool (Module 09) ══
     * Production:
     *   mbuf_pool = rte_pktmbuf_pool_create(
     *       "mbuf_pool", 65535, 256, 0,
     *       RTE_MBUF_DEFAULT_BUF_SIZE,
     *       rte_eth_dev_socket_id(port_id))
     *   NIC DMA will fill mbufs from this pool.
     */
    printf("[4] Mempool created (simulation: static array pool)\n");

    /* ══ Step 5: Port init (Module 10) ══
     * Production:
     *   port_init(port_id, mbuf_pool)
     *     → rte_eth_dev_configure(port, nb_rx_queues, nb_tx_queues, &port_conf)
     *     → rte_eth_rx_queue_setup() × nb_rx_queues
     *     → rte_eth_tx_queue_setup() × nb_tx_queues
     *     → rte_eth_dev_start(port)
     *     → rte_eth_promiscuous_enable(port)
     *     → check_port_link_status(port)  ← wait for link UP
     */
    printf("[5] NIC port initialized (simulation: no NIC)\n");

    /* ══ Step 6: NUMA-aware allocation (Module 14) ══
     * Production: all hash tables, ring buffers, and Hyperscan DBs
     * allocated on the correct NUMA socket to avoid cross-socket penalty.
     *   int nic_sock = rte_eth_dev_socket_id(port_id)
     *   pool = rte_pktmbuf_pool_create(..., nic_sock)
     *   domain_table = rte_hash_create(&params)  ← socket = rte_socket_id()
     */
    printf("[6] NUMA socket allocation configured\n");

    /* ══ Step 7: Hyperscan compile (Module 15) ══
     * Production:
     *   parseFile("/etc/dp_app/patterns.txt", &patterns, &flags, &ids, &n)
     *   create_hyperscan_db(&hs_details, 0, &domainsPatternDB)
     *   → hs_compile_multi(patterns, flags, ids, n, HS_MODE_BLOCK, NULL, &db)
     */
    printf("[7] Hyperscan global DB compiled (simulation: skipped)\n");

    /* ══ Step 8: Hyperscan scratch (Module 16) ══
     * Production:
     *   hs_init_global_scratch()
     *     → hs_alloc_scratch(domainsPatternDB, &global_scratch)
     *   Per-lcore scratch cloned in lcore launch, not here.
     */
    printf("[8] Hyperscan global scratch allocated (simulation: skipped)\n");

    /* ══ Step 9: Kafka producer (Module 19) ══
     * Production:
     *   kafka_producer_init(broker, topic_cdr)
     *     → rd_kafka_conf_new() + conf_set(acks, retries, batch, linger)
     *     → rd_kafka_conf_set_dr_msg_cb(conf, delivery_report_cb)
     *     → rd_kafka_new(RD_KAFKA_PRODUCER, conf, ...)
     *     → rd_kafka_topic_new(producer, topic_cdr, NULL)
     */
    printf("[9] Kafka CDR producer initialized (simulation: skipped)\n");

    /* ══ Step 10: Kafka consumer (Module 20) ══
     * Production:
     *   rk_consumer = kafka_consumer_init(broker, "dp_consumer")
     *     → conf: auto.offset.reset=earliest, enable.auto.commit=false
     *     → rd_kafka_conf_set_rebalance_cb(conf, rebalance_cb)
     *     → rd_kafka_new(RD_KAFKA_CONSUMER, conf, ...)
     *     → rd_kafka_poll_set_consumer(rk)
     *   rd_kafka_subscribe(rk, {"policy_updates"})
     *   Initial policy sync: consume until first SYNC_COMPLETE message
     */
    printf("[10] Kafka policy consumer initialized (simulation: skipped)\n");

    /* ══ Step 11: Seed initial policy state (Module 12, 17, 20) ══
     * Production:
     *   For each group:
     *     group->domain_details_table = rte_hash_create(&params)
     *   Policy pre-loaded from Kafka until SYNC_COMPLETE received.
     */
    strncpy(g_policy[g_policy_count].domain, "google.com", 255);
    g_policy[g_policy_count++].is_whitelisted = 1;
    strncpy(g_policy[g_policy_count].domain, "facebook.com", 255);
    g_policy[g_policy_count++].is_blacklisted = 1;
    strncpy(g_policy[g_policy_count].domain, "ads.doubleclick.net", 255);
    g_policy[g_policy_count++].is_blacklisted = 1;
    strncpy(g_malicious[g_malicious_count++], "malware-download.ru", 255);
    strncpy(g_malicious[g_malicious_count++], "phishing-bank.xyz", 255);
    printf("[11] Policy tables seeded: %d domains, %d malicious\n\n",
           g_policy_count, g_malicious_count);

    /* ══ Step 12: Create inter-lcore rings (Module 03, 11) ══
     * Production:
     *   for (w=0; w<NUM_WORKERS; w++)
     *     g_rx_rings[w] = rte_ring_create(name, RING_SIZE, socket, SPSC)
     *   g_tx_ring = rte_ring_create("tx_ring", RING_SIZE, socket, MPSC)
     */
    for (int w = 0; w < NUM_WORKERS; w++) {
        g_rx_rings[w] = ring_create(RING_SZ);
        assert(g_rx_rings[w]);
    }
    g_tx_ring = ring_create(RING_SZ * NUM_WORKERS);
    assert(g_tx_ring);
    printf("[12] Inter-lcore rings created\n");

    /* ══ Step 13: Init lcore contexts (Module 08, 13) ══ */
    memset(g_ctx, 0, sizeof(g_ctx));
    /* RX lcore */
    g_ctx[0].lcore_id = 0; g_ctx[0].running = 1;
    /* TX lcore */
    g_ctx[1].lcore_id = 1; g_ctx[1].running = 1;
    g_ctx[1].tx_ring  = g_tx_ring;
    /* Worker lcores */
    for (int w = 0; w < NUM_WORKERS; w++) {
        int id = w + 2;
        g_ctx[id].lcore_id = id;
        g_ctx[id].rx_ring  = g_rx_rings[w];
        g_ctx[id].tx_ring  = g_tx_ring;
        g_ctx[id].running  = 1;
    }

    /* ══ Step 14: Launch lcores (Module 08, 11) ══
     * Production:
     *   rte_eal_remote_launch(tx_lcore_func,     &ctx[TX_ID],   TX_ID)
     *   rte_eal_remote_launch(worker_lcore_func, &ctx[w_id],    w_id)
     *   rte_eal_remote_launch(rx_lcore_func,     &ctx[RX_ID],   RX_ID)
     *   ← RX launched LAST to avoid enqueuing before workers are ready
     */
    printf("[13] Launching lcores...\n");

    pthread_t threads[MAX_LCORES];

    pthread_create(&threads[1], NULL, tx_lcore_func, &g_ctx[1]);
    for (int w = 0; w < NUM_WORKERS; w++) {
        int id = w + 2;
        /* Production (Module 16):
         *   hs_clone_scratch_for_lcore(&worker_info->worker_scratch, id)
         *   hs_alloc_scratch(group->database, &worker_info->worker_scratch)
         */
        pthread_create(&threads[id], NULL, worker_lcore_func, &g_ctx[id]);
    }
    pthread_create(&threads[0], NULL, rx_lcore_func, &g_ctx[0]);

    /* ══ Step 15: Main control loop ══ */
    printf("[14] Main lcore entering control loop\n\n");
    main_control_loop();

    /* ══ SHUTDOWN SEQUENCE ══ */
    printf("\n[Shutdown] Signalling lcores...\n");

    /* Stop RX first — stop feeding the pipeline */
    g_ctx[0].running = 0;
    pthread_join(threads[0], NULL);

    /* Stop workers — let them drain their rings */
    for (int w = 0; w < NUM_WORKERS; w++)
        g_ctx[w + 2].running = 0;
    for (int w = 0; w < NUM_WORKERS; w++)
        pthread_join(threads[w + 2], NULL);

    /* Stop TX last — drain any forwarded packets */
    g_ctx[1].running = 0;
    pthread_join(threads[1], NULL);

    /* ── Kafka shutdown (Module 19) ──
     * Production:
     *   rd_kafka_flush(rk_producer, 5000)  ← drain CDR queue
     *   rd_kafka_consumer_close(rk_consumer)
     *   rd_kafka_topic_destroy(cdr_topic)
     *   rd_kafka_destroy(rk_producer)
     *   rd_kafka_destroy(rk_consumer)
     */

    /* ── Hyperscan cleanup (Module 15/16) ──
     * Production:
     *   hs_free_scratch(global_scratch)
     *   for each lcore: hs_free_scratch(worker_scratch[id])
     *   for each group: hs_free_database(group->database)
     *   hs_free_database(domainsPatternDB)
     */

    /* ── DPDK cleanup (Module 08/10) ──
     * Production:
     *   rte_eth_dev_stop(port_id)
     *   rte_eth_dev_close(port_id)
     *   rte_eal_cleanup()
     */

    /* ── Ring cleanup (Module 03) ── */
    for (int w = 0; w < NUM_WORKERS; w++) ring_destroy(g_rx_rings[w]);
    ring_destroy(g_tx_ring);

    /* ── Final stats ── */
    printf("\n[Final Statistics]\n");
    unsigned long tot_rx=0, tot_tx=0, tot_drop=0, tot_dns=0,
                  tot_tls=0, tot_sinkhole=0, tot_cdr=0;
    for (int i = 0; i < MAX_LCORES; i++) {
        tot_rx       += atomic_load(&g_ctx[i].pkt_rx);
        tot_tx       += atomic_load(&g_ctx[i].pkt_tx);
        tot_drop     += atomic_load(&g_ctx[i].pkt_drop);
        tot_dns      += atomic_load(&g_ctx[i].pkt_dns);
        tot_tls      += atomic_load(&g_ctx[i].pkt_tls);
        tot_sinkhole += atomic_load(&g_ctx[i].pkt_sinkholes);
        tot_cdr      += atomic_load(&g_ctx[i].cdr_produced);
    }
    printf("  rx=%lu  tx=%lu  drop=%lu\n", tot_rx, tot_tx, tot_drop);
    printf("  dns=%lu  tls=%lu  sinkholes=%lu\n", tot_dns, tot_tls, tot_sinkhole);
    printf("  cdr_records=%lu\n", tot_cdr);

    printf("\n=== Shutdown complete ===\n");
    return 0;
}
