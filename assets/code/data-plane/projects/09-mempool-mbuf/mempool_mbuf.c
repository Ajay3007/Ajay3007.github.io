/**
 * mempool_mbuf.c — Module 09: Mempool + mbuf
 *
 * Every packet in a DPDK application lives in an rte_mbuf, which lives in
 * an rte_mempool. Understanding this is essential before touching any packet
 * processing code.
 *
 * WHY MEMPOOLS EXIST:
 *   At 25 Gbps with 1500-byte packets, the NIC delivers ~2 million packets
 *   per second. If each packet required a malloc() / free() call, the memory
 *   allocator would become the bottleneck — malloc has locks and syscalls.
 *
 *   The mempool pre-allocates a fixed number of mbufs at startup. At runtime,
 *   "allocation" is just popping a pointer off a lock-free ring — ~10 ns.
 *   "Free" is pushing it back — ~10 ns. No syscalls, no locks in the fast path.
 *
 * IN THE REAL DP APPLICATION PROJECT:
 *   - One pool per NUMA socket (socket-local memory avoids cross-NUMA latency)
 *   - Pool created once in port_init() before rte_eth_rx_queue_setup()
 *   - NIC DMA engine writes received packets directly into pool mbufs
 *   - Workers access packet data via rte_pktmbuf_mtod()
 *   - DNS sinkhole (Module 23) rewrites packet data in-place through mtod
 *   - rte_pktmbuf_free() called after TX or on DROP — never on received mbufs
 *     that are forwarded (TX burst will free them)
 *
 * REFERENCE CODE: requires DPDK installed.
 * Build: make
 * Run:   sudo ./mempool_mbuf
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdint.h>

#include <rte_eal.h>
#include <rte_mempool.h>
#include <rte_mbuf.h>
#include <rte_mbuf_pool_ops.h>
#include <rte_errno.h>
#include <rte_lcore.h>

/* Include our packet structs for realistic packet manipulation */
#include "../05-packet-structs/packet_structs.h"

/* ───────────────────────────────────────────────────────────
 * Pool sizing constants
 *
 * n MUST be 2^k - 1 (e.g. 255, 511, 1023, 8191, 65535).
 * The underlying rte_ring requires power-of-2 capacity, so the pool
 * adds 1 internally: pool of 8191 needs a ring of 8192 = 2^13.
 *
 * Rule of thumb: n >= (nb_rx_desc * nb_rx_queues * nb_ports) * 2
 * For our demo: 255 is plenty.
 *
 * In DP production config:
 *   n = 65535  (2^16 - 1)
 *   This supports 4 ports × 4 queues × 1024 descriptors = 16384 mbufs
 *   "in flight", with 49151 spares in the pool.
 * ─────────────────────────────────────────────────────────── */
#define POOL_NAME         "pktmbuf_pool"
#define POOL_NUM_MBUFS    8191          /* 2^13 - 1 */
#define POOL_CACHE_SIZE   256           /* per-lcore cache: reduces ring lock contention */
#define POOL_PRIV_SIZE    0             /* no private per-mbuf metadata in this demo */
#define POOL_DATA_ROOM    RTE_MBUF_DEFAULT_BUF_SIZE  /* 2176 bytes: 1500 MTU + headroom + overhead */

/*
 * RTE_MBUF_DEFAULT_BUF_SIZE = RTE_MBUF_DEFAULT_DATAROOM + RTE_PKTMBUF_HEADROOM
 *                           = 2048 + 128 = 2176 bytes
 *
 * The 128-byte headroom is reserved in front of the packet data area.
 * It allows prepending headers without reallocating (used in tunneling,
 * and by DNS sinkhole when adjusting the packet size).
 */

/* ───────────────────────────────────────────────────────────
 * print_mbuf_layout — show the memory layout of one mbuf
 *
 * Understanding this diagram is key to working with mbufs.
 * ─────────────────────────────────────────────────────────── */
static void print_mbuf_layout(struct rte_mbuf *m, const char *label)
{
    printf("\n[mbuf layout: %s]\n", label);
    printf("  buf_addr        = %p   (start of raw buffer in hugepage)\n",
           m->buf_addr);
    printf("  buf_iova        = 0x%016" PRIx64 " (physical/IOVA address for DMA)\n",
           m->buf_iova);
    printf("  buf_len         = %u  (total buffer size)\n", m->buf_len);
    printf("  data_off        = %u  (offset from buf_addr to packet start)\n",
           m->data_off);
    printf("  data_len        = %u  (bytes of valid data in this segment)\n",
           m->data_len);
    printf("  pkt_len         = %u  (total packet length, all segments)\n",
           m->pkt_len);
    printf("  nb_segs         = %u  (number of chained segments)\n",
           m->nb_segs);
    printf("  port            = %u  (RX port)\n", m->port);
    printf("  refcnt          = %u  (reference count)\n",
           rte_mbuf_refcnt_read(m));
    printf("  headroom        = %u  (space before data: buf_addr+data_off - buf_addr)\n",
           rte_pktmbuf_headroom(m));
    printf("  tailroom        = %u  (space after data)\n",
           rte_pktmbuf_tailroom(m));
    printf("  rte_pktmbuf_mtod = %p  (pointer to packet data start)\n",
           rte_pktmbuf_mtod(m, void *));
    printf("\n");
    printf("  Memory layout:\n");
    printf("  [mbuf struct %zuB][priv %uB][headroom %uB][<-- data %uB -->][tailroom %uB]\n",
           sizeof(struct rte_mbuf),
           rte_pktmbuf_priv_size(m->pool),
           rte_pktmbuf_headroom(m),
           m->data_len,
           rte_pktmbuf_tailroom(m));
}

/* ───────────────────────────────────────────────────────────
 * print_pool_stats — check pool health
 *
 * In the real app, call this periodically from the main lcore.
 * If avail_count keeps dropping toward zero, mbufs are leaking
 * (alloc without free somewhere in the pipeline).
 * ─────────────────────────────────────────────────────────── */
static void print_pool_stats(struct rte_mempool *pool)
{
    printf("[pool: %s]\n", pool->name);
    printf("  size          = %u  (total mbufs)\n",   pool->size);
    printf("  populated     = %u\n", pool->populated_size);
    printf("  available     = %u  (in pool, ready to alloc)\n",
           rte_mempool_avail_count(pool));
    printf("  in_use        = %u  (allocated, not yet freed)\n",
           rte_mempool_in_use_count(pool));
    printf("  cache_size    = %u  (per-lcore cache depth)\n", pool->cache_size);
    printf("  elt_size      = %u  (sizeof mbuf + priv + data room)\n",
           pool->elt_size);
    printf("\n");
}

/* ───────────────────────────────────────────────────────────
 * Demo 1: alloc, inspect, free
 * ─────────────────────────────────────────────────────────── */
static void demo_alloc_inspect_free(struct rte_mempool *pool)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 1: alloc → inspect → free\n");
    printf("══════════════════════════════════════════════\n");

    struct rte_mbuf *m = rte_pktmbuf_alloc(pool);
    if (!m)
        rte_exit(EXIT_FAILURE, "rte_pktmbuf_alloc failed\n");

    print_mbuf_layout(m, "freshly allocated (empty)");

    /*
     * Simulate what happens when the NIC receives a packet:
     * rte_eth_rx_burst() fills the mbuf with received bytes and sets
     * data_len / pkt_len. Here we manually fill it with a fake DNS packet.
     */
    const uint8_t fake_dns_pkt[] = {
        /* Ethernet + IPv4 + UDP + DNS (abbreviated) */
        0xff,0xff,0xff,0xff,0xff,0xff, 0x00,0x11,0x22,0x33,0x44,0x55, 0x08,0x00,
        0x45,0x00,0x00,0x28, 0x00,0x01, 0x00,0x00, 0x40,0x11,0x00,0x00,
        0xc0,0xa8,0x01,0x01, 0x08,0x08,0x08,0x08,
        0xd4,0x31, 0x00,0x35, 0x00,0x14, 0x00,0x00,
        0x00,0x01, 0x00,0x00, 0x00,0x01, 0x00,0x00, 0x00,0x00, 0x00,0x00,
    };
    size_t pkt_len = sizeof(fake_dns_pkt);

    /* Append space at the tail and copy packet bytes into it */
    char *data = rte_pktmbuf_append(m, pkt_len);
    if (!data)
        rte_exit(EXIT_FAILURE, "rte_pktmbuf_append failed (packet too large?)\n");
    memcpy(data, fake_dns_pkt, pkt_len);

    print_mbuf_layout(m, "after rte_pktmbuf_append (packet filled)");

    /* Access packet headers — zero-copy overlay */
    eth_hdr_t  *eth = rte_pktmbuf_mtod(m, eth_hdr_t *);
    ipv4_hdr_t *ip4 = (ipv4_hdr_t *)((uint8_t *)eth + ETH_HDR_LEN);
    udp_hdr_t  *udp = (udp_hdr_t *)((uint8_t *)ip4 + IPV4_IHL_BYTES(ip4));

    printf("  Parsed from mbuf (zero-copy):\n");
    printf("    src_ip  = 0x%08x  dst_ip = 0x%08x\n",
           ntohl(ip4->src_ip), ntohl(ip4->dst_ip));
    printf("    src_port= %u  dst_port= %u\n",
           ntohs(udp->src_port), ntohs(udp->dst_port));
    printf("    proto   = %u (%s)\n", ip4->proto,
           ip4->proto == IP_PROTO_UDP ? "UDP" : "other");

    rte_pktmbuf_free(m);
    printf("  mbuf freed (returned to pool)\n");
    printf("  pool available after free: %u\n\n",
           rte_mempool_avail_count(pool));
}

/* ───────────────────────────────────────────────────────────
 * Demo 2: in-place packet modification (DNS sinkhole preview)
 *
 * In Module 23, dns_build_sinkhole_v4() does this:
 *   1. rte_pktmbuf_mtod() to get a pointer to the packet bytes
 *   2. Swap src/dst MAC, IP, ports in-place
 *   3. Set the DNS QR bit
 *   4. Append the answer section (A record with walled-garden IP)
 *   5. Adjust IP total_len and UDP dgram_len fields
 *   6. Set TX checksum offload flags on the mbuf
 *
 * This demo shows step 1 and 2 — the in-place modification pattern.
 * ─────────────────────────────────────────────────────────── */
static void demo_inplace_modify(struct rte_mempool *pool)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 2: in-place packet modification (DNS sinkhole pattern)\n");
    printf("══════════════════════════════════════════════\n");

    struct rte_mbuf *m = rte_pktmbuf_alloc(pool);
    assert(m != NULL);

    /* Fill with an Ethernet + IPv4 + UDP frame */
    uint8_t frame[42];
    memset(frame, 0, sizeof(frame));

    eth_hdr_t  *eth = (eth_hdr_t *)frame;
    ipv4_hdr_t *ip4 = (ipv4_hdr_t *)(frame + ETH_HDR_LEN);
    udp_hdr_t  *udp = (udp_hdr_t *)(frame + ETH_HDR_LEN + IPV4_HDR_MIN);

    /* src: client MAC + IP */
    memset(eth->src_mac, 0xAA, 6);
    memset(eth->dst_mac, 0xFF, 6);
    eth->ether_type = htons(ETHER_TYPE_IPV4);

    ip4->version_ihl = 0x45;
    ip4->proto       = IP_PROTO_UDP;
    ip4->src_ip      = htonl(0xC6336405);  /* 198.51.100.5 */
    ip4->dst_ip      = htonl(0x08080808);  /* 8.8.8.8 */
    ip4->total_len   = htons(28);

    udp->src_port    = htons(54321);
    udp->dst_port    = htons(53);          /* DNS */
    udp->dgram_len   = htons(8);

    char *pkt_data = rte_pktmbuf_append(m, sizeof(frame));
    assert(pkt_data != NULL);
    memcpy(pkt_data, frame, sizeof(frame));

    printf("  Before (DNS query from client to 8.8.8.8):\n");
    eth_hdr_t  *meth = rte_pktmbuf_mtod(m, eth_hdr_t *);
    ipv4_hdr_t *mip4 = (ipv4_hdr_t *)((uint8_t *)meth + ETH_HDR_LEN);
    udp_hdr_t  *mudp = (udp_hdr_t *)((uint8_t *)mip4 + IPV4_HDR_MIN);
    printf("    src=%u.%u.%u.%u:%u → dst=%u.%u.%u.%u:%u\n",
           (ntohl(mip4->src_ip) >> 24) & 0xFF, (ntohl(mip4->src_ip) >> 16) & 0xFF,
           (ntohl(mip4->src_ip) >>  8) & 0xFF,  ntohl(mip4->src_ip)        & 0xFF,
           ntohs(mudp->src_port),
           (ntohl(mip4->dst_ip) >> 24) & 0xFF, (ntohl(mip4->dst_ip) >> 16) & 0xFF,
           (ntohl(mip4->dst_ip) >>  8) & 0xFF,  ntohl(mip4->dst_ip)        & 0xFF,
           ntohs(mudp->dst_port));

    /*
     * In-place rewrite: turn the DNS query into a sinkhole response.
     * Module 23 does a much more complete version: swaps all headers,
     * builds the DNS answer section, sets checksum offload flags.
     * Here we just show the pattern: mtod + modify.
     */
    uint32_t orig_src = mip4->src_ip;
    uint32_t orig_dst = mip4->dst_ip;
    uint16_t orig_sport = mudp->src_port;
    uint16_t orig_dport = mudp->dst_port;

    /* Swap src ↔ dst (packet is now going back to the client) */
    mip4->src_ip = orig_dst;
    mip4->dst_ip = orig_src;
    mudp->src_port = orig_dport;
    mudp->dst_port = orig_sport;

    /*
     * Set hardware checksum offload flags.
     * Instead of computing IP/UDP checksums in software (slow),
     * we set these flags and the NIC TX engine computes them in hardware.
     * This is one of the biggest per-packet CPU savings in DPDK.
     */
    m->ol_flags |= RTE_MBUF_F_TX_IPV4 |
                   RTE_MBUF_F_TX_IP_CKSUM |
                   RTE_MBUF_F_TX_UDP_CKSUM;
    mip4->checksum = 0;   /* NIC will fill this */
    mudp->checksum = rte_ipv4_phdr_cksum(mip4, m->ol_flags); /* pseudo-header */

    printf("  After in-place rewrite (sinkhole response back to client):\n");
    printf("    src=%u.%u.%u.%u:%u → dst=%u.%u.%u.%u:%u\n",
           (ntohl(mip4->src_ip) >> 24) & 0xFF, (ntohl(mip4->src_ip) >> 16) & 0xFF,
           (ntohl(mip4->src_ip) >>  8) & 0xFF,  ntohl(mip4->src_ip)        & 0xFF,
           ntohs(mudp->src_port),
           (ntohl(mip4->dst_ip) >> 24) & 0xFF, (ntohl(mip4->dst_ip) >> 16) & 0xFF,
           (ntohl(mip4->dst_ip) >>  8) & 0xFF,  ntohl(mip4->dst_ip)        & 0xFF,
           ntohs(mudp->dst_port));
    printf("  ol_flags TX_IPV4|TX_IP_CKSUM|TX_UDP_CKSUM set\n");
    printf("  → rte_eth_tx_burst() will HW-compute checksums\n\n");

    rte_pktmbuf_free(m);
}

/* ───────────────────────────────────────────────────────────
 * Demo 3: burst alloc / free (the real RX/TX pattern)
 *
 * In the real app, the RX lcore does:
 *   nb_rx = rte_eth_rx_burst(port, queue, mbufs, BURST_SIZE);
 * This fills mbufs[] from the pool. The worker then processes them
 * and the TX lcore calls:
 *   nb_tx = rte_eth_tx_burst(port, queue, mbufs, nb_fwd);
 * TX burst frees the mbufs back to the pool after transmission.
 * ─────────────────────────────────────────────────────────── */
#define BURST_SIZE  32

static void demo_burst_alloc(struct rte_mempool *pool)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 3: burst alloc/free (RX/TX pattern)\n");
    printf("══════════════════════════════════════════════\n");

    struct rte_mbuf *mbufs[BURST_SIZE];

    printf("  pool available before burst alloc: %u\n",
           rte_mempool_avail_count(pool));

    /*
     * rte_pktmbuf_alloc_bulk() allocates multiple mbufs in one call.
     * More efficient than calling rte_pktmbuf_alloc() in a loop because
     * it takes the pool lock once (or uses the per-lcore cache once).
     *
     * The real RX path: mbufs are pre-allocated and queued to the NIC
     * RX descriptor ring. When a packet arrives, the NIC DMA fills the
     * pre-queued mbuf and returns it via rte_eth_rx_burst().
     */
    int ret = rte_pktmbuf_alloc_bulk(pool, mbufs, BURST_SIZE);
    if (ret != 0)
        rte_exit(EXIT_FAILURE, "rte_pktmbuf_alloc_bulk failed\n");

    printf("  allocated burst of %d mbufs\n", BURST_SIZE);
    printf("  pool available after  burst alloc: %u\n",
           rte_mempool_avail_count(pool));

    /* Simulate worker processing: fill each mbuf with a fake payload */
    for (int i = 0; i < BURST_SIZE; i++) {
        char *data = rte_pktmbuf_append(mbufs[i], 60);
        if (data)
            memset(data, (uint8_t)i, 60);   /* fill with pattern */
    }

    /* Simulate TX: free the burst back to pool */
    for (int i = 0; i < BURST_SIZE; i++)
        rte_pktmbuf_free(mbufs[i]);

    printf("  freed burst of %d mbufs\n", BURST_SIZE);
    printf("  pool available after  burst free:  %u\n\n",
           rte_mempool_avail_count(pool));
}

/* ───────────────────────────────────────────────────────────
 * Demo 4: headroom — prepend a header
 *
 * When a packet needs a new outer header added (e.g., GRE tunnel,
 * or adding a VLAN tag), use rte_pktmbuf_prepend() to extend data
 * into the pre-reserved headroom without any copy.
 *
 * In the DP application this isn't used directly, but the headroom is important
 * for the DNS sinkhole: the answer section is appended (rte_pktmbuf_append),
 * and the IP/UDP length fields are adjusted to match.
 * ─────────────────────────────────────────────────────────── */
static void demo_headroom(struct rte_mempool *pool)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 4: headroom — prepend a header\n");
    printf("══════════════════════════════════════════════\n");

    struct rte_mbuf *m = rte_pktmbuf_alloc(pool);
    assert(m != NULL);

    /* Start with just an IP payload (no Ethernet header yet) */
    char *ip_data = rte_pktmbuf_append(m, 20);
    assert(ip_data != NULL);
    memset(ip_data, 0x45, 20);
    printf("  headroom before prepend: %u bytes\n", rte_pktmbuf_headroom(m));

    /*
     * Prepend a 14-byte Ethernet header using the headroom.
     * This returns a pointer to the newly prepended area.
     * No data is copied — data_off is simply decremented by 14.
     */
    eth_hdr_t *eth = (eth_hdr_t *)rte_pktmbuf_prepend(m, ETH_HDR_LEN);
    if (!eth)
        rte_exit(EXIT_FAILURE, "rte_pktmbuf_prepend failed: not enough headroom\n");

    eth->ether_type = htons(ETHER_TYPE_IPV4);
    printf("  headroom after  prepend: %u bytes\n", rte_pktmbuf_headroom(m));
    printf("  data_len after  prepend: %u bytes\n", m->data_len);
    printf("  mtod now points to Ethernet header: ether_type=0x%04x\n",
           ntohs(rte_pktmbuf_mtod(m, eth_hdr_t *)->ether_type));

    rte_pktmbuf_free(m);
    printf("\n");
}

/* ───────────────────────────────────────────────────────────
 * Demo 5: mbuf chain (multi-segment for jumbo frames)
 *
 * For packets larger than data_room (2176 bytes), DPDK chains multiple
 * mbufs. nb_segs > 1, and m->next points to the next segment.
 *
 * In the DP application, jumbo frames are uncommon (MTU is 1500), but the code
 * must guard against nb_segs > 1 (linearise or handle the chain) to
 * avoid parsing only the first segment and missing the DNS payload.
 * ─────────────────────────────────────────────────────────── */
static void demo_mbuf_chain(struct rte_mempool *pool)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 5: mbuf chain (multi-segment)\n");
    printf("══════════════════════════════════════════════\n");

    struct rte_mbuf *m1 = rte_pktmbuf_alloc(pool);
    struct rte_mbuf *m2 = rte_pktmbuf_alloc(pool);
    assert(m1 && m2);

    char *d1 = rte_pktmbuf_append(m1, 100);
    char *d2 = rte_pktmbuf_append(m2, 100);
    assert(d1 && d2);
    memset(d1, 0xAA, 100);
    memset(d2, 0xBB, 100);

    /* Chain m2 onto m1 */
    rte_pktmbuf_chain(m1, m2);

    printf("  m1: data_len=%u  nb_segs=%u  pkt_len=%u\n",
           m1->data_len, m1->nb_segs, m1->pkt_len);
    printf("  m1->next = %p (m2)\n", (void *)m1->next);

    /*
     * The real app checks nb_segs before parsing:
     *
     *   if (m->nb_segs > 1) {
     *       // Option A: linearise (expensive — one memcpy per packet)
     *       //           rte_pktmbuf_linearize(m)
     *       // Option B: only handle single-segment (drop multi-seg)
     *       //           rte_pktmbuf_free(m); continue;
     *   }
     *   eth = rte_pktmbuf_mtod(m, eth_hdr_t *);
     *
     * The DP application drops multi-segment packets (rare at 1500 MTU) rather than
     * paying the linearise copy cost on every packet.
     */
    printf("  real app: if (m->nb_segs > 1) → drop or linearise\n");

    /* Free head — chain is freed automatically */
    rte_pktmbuf_free(m1);
    printf("  rte_pktmbuf_free(m1) frees entire chain\n\n");
}

/* ─── main ──────────────────────────────────────────────── */

/* Minimal EAL args for demo (no NIC needed) */
static const char *eal_args[] = {
    "mempool_mbuf",
    "-l", "0",               /* use lcore 0 only */
    "--socket-mem", "256",
    "-n", "4",
    "--proc-type", "auto",
    "--no-pci",              /* skip PCI probe — no NIC needed for this demo */
};

int main(void)
{
    printf("=== Module 09: Mempool + mbuf ===\n\n");

    /* Initialise EAL (same as Module 08, minimal args) */
    int ret = rte_eal_init(
        (int)(sizeof(eal_args) / sizeof(eal_args[0])),
        (char **)(uintptr_t)eal_args);
    if (ret < 0)
        rte_exit(EXIT_FAILURE, "rte_eal_init failed: %s\n",
                 rte_strerror(rte_errno));

    printf("[EAL] Initialized.\n");
    printf("sizeof(struct rte_mbuf) = %zu bytes\n\n", sizeof(struct rte_mbuf));

    /* ── Create the mempool ──
     *
     * In the real app (port_init in app_main.c):
     *
     *   mbuf_pool = rte_pktmbuf_pool_create(
     *       "mbuf_pool_s0",           // name (unique per socket)
     *       65535,                    // num mbufs (2^16 - 1)
     *       256,                      // cache size (per-lcore)
     *       0,                        // priv size (0 = no private area)
     *       RTE_MBUF_DEFAULT_BUF_SIZE,// data room size
     *       rte_socket_id()           // NUMA socket for allocation
     *   );
     *   if (!mbuf_pool)
     *       rte_exit(EXIT_FAILURE, "Cannot create mbuf pool\n");
     *
     *   // Then hand the pool to the NIC RX queue:
     *   rte_eth_rx_queue_setup(port, queue, nb_desc, socket,
     *                           &rx_conf, mbuf_pool);
     */
    struct rte_mempool *pool = rte_pktmbuf_pool_create(
        POOL_NAME,
        POOL_NUM_MBUFS,
        POOL_CACHE_SIZE,
        POOL_PRIV_SIZE,
        POOL_DATA_ROOM,
        rte_socket_id()
    );
    if (!pool)
        rte_exit(EXIT_FAILURE,
                 "rte_pktmbuf_pool_create failed: %s\n",
                 rte_strerror(rte_errno));

    printf("[Pool created]\n");
    print_pool_stats(pool);

    /* Run demos */
    demo_alloc_inspect_free(pool);
    demo_inplace_modify(pool);
    demo_burst_alloc(pool);
    demo_headroom(pool);
    demo_mbuf_chain(pool);

    printf("[Final pool state]\n");
    print_pool_stats(pool);

    printf("--- mbuf API quick-reference ---\n");
    printf("  rte_pktmbuf_pool_create(...)      → create pool at startup\n");
    printf("  rte_pktmbuf_alloc(pool)            → get one mbuf\n");
    printf("  rte_pktmbuf_alloc_bulk(pool,m,n)   → get n mbufs at once\n");
    printf("  rte_pktmbuf_free(m)                → return to pool\n");
    printf("  rte_pktmbuf_mtod(m, T*)            → pointer to packet data\n");
    printf("  rte_pktmbuf_append(m, len)         → extend into tailroom\n");
    printf("  rte_pktmbuf_prepend(m, len)        → extend into headroom\n");
    printf("  rte_pktmbuf_adj(m, len)            → strip from front\n");
    printf("  rte_pktmbuf_trim(m, len)           → strip from back\n");
    printf("  rte_pktmbuf_data_len(m)            → bytes in this segment\n");
    printf("  rte_pktmbuf_pkt_len(m)             → total bytes all segments\n");
    printf("  rte_pktmbuf_headroom(m)            → space before data\n");
    printf("  rte_pktmbuf_tailroom(m)            → space after data\n");
    printf("  rte_pktmbuf_chain(head, tail)      → link segments\n");
    printf("  rte_pktmbuf_linearize(m)           → collapse chain to 1 seg\n");
    printf("  m->ol_flags |= RTE_MBUF_F_TX_*    → HW offload flags\n");

    rte_eal_cleanup();
    return 0;
}
