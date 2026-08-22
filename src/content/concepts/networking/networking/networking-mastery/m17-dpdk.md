---
title: "M17 - High-Performance Networking with DPDK"
description: "NETWORKING MASTERY · PHASE 4 · MODULE 17 · WEEK 15 🚀 High-Performance Networking with DPDK Poll mode drivers · mbuf and mempool · RX/TX burst API · hugepages · NUMA · RSS ·…"
domain: networking
track: networking-mastery
order: 17
ownHeader: true
url: /learning/networking-mastery/m17-dpdk/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#2a0a08 40%,#6a1a08 75%,#4a0a00 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#f08860;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#f8c8a8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#fce0c8}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#f08860;border-bottom-color:#f08860}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee)}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700;letter-spacing:.04em}
.cp-body{padding:1.1rem 1.2rem}
.cp-body p,.cp-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.cp-body ul,.cp-body ol{margin:.4rem 0;padding-left:1.4rem}
.cp-body li{margin-bottom:.3rem}
.cp-body h4{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin:.9rem 0 .3rem}
.p-blue .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue .cp-hdr{background:#0d2030}
.p-teal .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.p-red .cp-hdr{background:#faeaea}[data-theme=dark] .p-red .cp-hdr{background:#2a0808}
.p-amber .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber .cp-hdr{background:#2a1e00}
.tag-blue{background:#d0e8f8;color:#1a4a7c}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}.tag-red{background:#f4d0d0;color:#6c1a1a}
.tag-amber{background:#fae8a0;color:#5a3800}
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #8a3010}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#f0c8a0;white-space:pre}
.cm{color:#806040}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#fff8f0;border:1.5px solid #c06020;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#280800;border-color:#d07030}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#7a3000}[data-theme=dark] .ins strong{color:#f08860}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#7a3000;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#8a3010}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #8a3010;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#8a3010;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#8a3010;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#8a3010;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 4 · MODULE 17 · WEEK 15</div>
  <div class="mod-title">🚀 High-Performance Networking with DPDK</div>
  <div class="mod-subtitle">Poll mode drivers · mbuf and mempool · RX/TX burst API · hugepages · NUMA · RSS · DPDK pipelines</div>
  <div class="mod-pills">
    <span class="mod-pill">Advanced</span>
    <span class="mod-pill">Prerequisite: M14 Linux Stack</span>
    <span class="mod-pill">DPDK 23.x</span>
    <span class="mod-pill">Your Core Work Domain</span>
    <span class="mod-pill">3 Labs</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">Why DPDK</button>
  <button class="tab-btn" onclick="vt(event,'t1')">EAL and Setup</button>
  <button class="tab-btn" onclick="vt(event,'t2')">mbuf and Mempool</button>
  <button class="tab-btn" onclick="vt(event,'t3')">PMD and Burst API</button>
  <button class="tab-btn" onclick="vt(event,'t4')">RSS and Flow Director</button>
  <button class="tab-btn" onclick="vt(event,'t5')">Pipelines</button>
  <button class="tab-btn" onclick="vt(event,'t6')">Performance Tuning</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Checklist</button>
</div>

<!-- TAB 0 -->
<div id="t0" class="tab-pane active">
<p class="sep">WHY DPDK — THE KERNEL IS NOT FAST ENOUGH</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🚀</span><h3>The Performance Problem DPDK Solves</h3><span class="tag tag-orange">MOTIVATION</span></div>
  <div class="cp-body">
    <p>You already have 2.5 years of DPDK experience — this module deepens that foundation with the theoretical underpinning of each performance technique, connecting your practical knowledge to the "why".</p>
<div class="cb"><pre><span class="cm">/* Why kernel forwarding is slow — root causes */</span>
 
1. Interrupt overhead (eliminated by PMD polling):
   10G at 64B = 14.8M packets/s = 14.8M IRQs/s
   Each IRQ: context switch + cache invalidation ≈ 1000 cycles = 14.8T cycles/s wasted
 
2. Memory allocation (eliminated by mempool):
   kmalloc()/kfree() per sk_buff → fragmentation, lock contention
   DPDK mempool: pre-allocated, lock-free, O(1)
 
3. Memory copies (eliminated by zero-copy design):
   NIC → DMA buffer → sk_buff → socket rcvbuf → userspace
   DPDK: NIC DMA → mbuf in hugepage → application (1 copy from NIC)
 
4. Cache misses (eliminated by hugepages + NUMA pinning):
   4KB pages: 1GB of packet buffers = 262,144 TLB entries → TLB thrash
   2MB hugepages: same 1GB = 512 TLB entries → fits in TLB
 
5. Lock contention (eliminated by per-core design):
   Kernel routing: locks on ARP cache, routing table, socket buffers
   DPDK: each core owns its own queues and mempools → no locks
 
<span class="cm">/* Performance numbers */</span>
Kernel stack:   ~1-3 Mpps per core (64B packets)
DPDK (Intel):   ~30-80 Mpps per core
DPDK (Mellanox/ConnectX): up to 100+ Mpps per core
Your servers: AMD EPYC + Mellanox — which PMD are you using?</pre></div>
  </div>
</div>
</div>

<!-- TAB 1 -->
<div id="t1" class="tab-pane">
<p class="sep">EAL — ENVIRONMENT ABSTRACTION LAYER</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚙️</span><h3>EAL Initialization and Configuration</h3><span class="tag tag-blue">EAL</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* DPDK EAL — abstracts OS and hardware */</span>
<span class="cm">/* Manages: hugepages, NUMA, CPU affinity, PCI devices, logging */</span>
 
<span class="cm">/* Minimal DPDK application skeleton */</span>
<span class="cs">#include &lt;rte_eal.h&gt;
#include &lt;rte_ethdev.h&gt;
#include &lt;rte_mbuf.h&gt;</span>
 
<span class="ck">int</span> main(<span class="ck">int</span> argc, <span class="ck">char</span> **argv) {
    <span class="cm">/* EAL init: parses EAL args, sets up hugepages, maps devices */</span>
    <span class="ck">int</span> ret = rte_eal_init(argc, argv);
    <span class="ck">if</span> (ret < 0) rte_exit(EXIT_FAILURE, <span class="cs">"EAL init failed\n"</span>);
    argc -= ret; argv += ret;  <span class="cm">/* remaining args are app-specific */</span>
 
    <span class="cm">/* Check available ports */</span>
    uint16_t nb_ports = rte_eth_dev_count_avail();
    printf(<span class="cs">"Available ports: %u\n"</span>, nb_ports);
 
    <span class="cm">/* Create mempool (see Tab 2) */</span>
    <span class="ck">struct</span> rte_mempool *mp = rte_pktmbuf_pool_create(
        <span class="cs">"MBUF_POOL"</span>,          <span class="cm">/* name */</span>
        8192 * nb_ports,      <span class="cm">/* n: total mbufs */</span>
        256,                  <span class="cm">/* cache_size: per-core cache */</span>
        0,                    <span class="cm">/* priv_size */</span>
        RTE_MBUF_DEFAULT_BUF_SIZE,
        rte_socket_id());     <span class="cm">/* NUMA socket */</span>
 
    <span class="cm">/* Configure each port */</span>
    uint16_t port_id;
    RTE_ETH_FOREACH_DEV(port_id) {
        port_init(port_id, mp);
    }
 
    <span class="cm">/* Launch worker on each lcore */</span>
    rte_eal_mp_remote_launch(lcore_main, NULL, CALL_MAIN);
 
    rte_eal_cleanup();
    return 0;
}
 
<span class="cm">/* Key EAL command-line arguments */</span>
-l 0-3          <span class="cm"># use lcores 0,1,2,3 (logical CPU cores)</span>
-n 4            <span class="cm"># 4 memory channels</span>
--socket-mem 2048  <span class="cm"># 2GB hugepage memory on socket 0</span>
--vdev eth_pcap0,iface=eth0  <span class="cm"># use pcap driver (for testing without real NIC)</span>
-a 0000:01:00.0 <span class="cm"># allow only this PCI device</span>
 
<span class="cm">/* Hugepage setup (required before DPDK runs) */</span>
echo 2048 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages
mkdir -p /mnt/huge
mount -t hugetlbfs nodev /mnt/huge</pre></div>
  </div>
</div>
</div>

<!-- TAB 2 -->
<div id="t2" class="tab-pane">
<p class="sep">mbuf AND MEMPOOL — PACKET BUFFER MANAGEMENT</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📦</span><h3>rte_mbuf and rte_mempool</h3><span class="tag tag-green">MBUF</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* rte_mbuf — DPDK's packet buffer (analogous to sk_buff) */</span>
<span class="ck">struct</span> rte_mbuf {
    <span class="cm">/* Buffer addresses */</span>
    void            *buf_addr;       <span class="cm">/* virtual address of buffer start */</span>
    rte_iova_t       buf_iova;       <span class="cm">/* IO/DMA address */</span>
    uint16_t         buf_len;        <span class="cm">/* total buffer length */</span>
    uint16_t         data_off;       <span class="cm">/* offset to first byte of data (headroom) */</span>
    uint16_t         data_len;       <span class="cm">/* data length in THIS mbuf segment */</span>
    uint32_t         pkt_len;        <span class="cm">/* total packet length (all segments) */</span>
 
    <span class="cm">/* Segmentation (chained mbufs for large packets) */</span>
    struct rte_mbuf *next;           <span class="cm">/* next segment in chain (NULL if only one) */</span>
    uint8_t          nb_segs;        <span class="cm">/* number of segments */</span>
 
    <span class="cm">/* Offload flags */</span>
    uint64_t         ol_flags;       <span class="cm">/* PKT_TX_IP_CKSUM, PKT_RX_RSS_HASH, etc. */</span>
    uint32_t         packet_type;    <span class="cm">/* RTE_PTYPE_L3_IPV4, L4_TCP, etc. */</span>
    uint32_t         hash.rss;       <span class="cm">/* RSS hash computed by NIC */</span>
 
    <span class="cm">/* Port and queue */</span>
    uint16_t         port;
    uint32_t         seqn;
};
 
<span class="cm">/* Accessing packet data */</span>
<span class="ck">struct</span> rte_ipv4_hdr *ip = rte_pktmbuf_mtod_offset(m,
    <span class="ck">struct</span> rte_ipv4_hdr *, sizeof(<span class="ck">struct</span> rte_ether_hdr));
uint32_t src_ip = rte_be_to_cpu_32(ip->src_addr);
uint32_t dst_ip = rte_be_to_cpu_32(ip->dst_addr);
 
<span class="cm">/* Prepend header (like skb_push) */</span>
<span class="ck">struct</span> rte_ether_hdr *eth = (<span class="ck">struct</span> rte_ether_hdr *)
    rte_pktmbuf_prepend(m, sizeof(<span class="ck">struct</span> rte_ether_hdr));
 
<span class="cm">/* rte_mempool — pre-allocated, lock-free pool */</span>
<span class="cm">/* Pool has: global ring + per-lcore cache (avoids lock on common case) */</span>
 
<span class="cm">/* Allocate mbuf from pool */</span>
<span class="ck">struct</span> rte_mbuf *m = rte_pktmbuf_alloc(mp);
<span class="ck">if</span> (!m) { <span class="cm">/* pool exhausted — back-pressure or drop */</span> }
 
<span class="cm">/* Free mbuf back to pool */</span>
rte_pktmbuf_free(m);  <span class="cm">/* returns to per-lcore cache, then global ring */</span>
 
<span class="cm">/* Bulk allocate/free (amortizes pool overhead) */</span>
<span class="ck">struct</span> rte_mbuf *mbufs[32];
rte_pktmbuf_alloc_bulk(mp, mbufs, 32);
rte_mempool_put_bulk(mp, (<span class="ck">void</span> **)mbufs, 32);</pre></div>
  </div>
</div>
</div>

<!-- TAB 3 -->
<div id="t3" class="tab-pane">
<p class="sep">PMD AND BURST API — THE CORE FORWARDING LOOP</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Poll Mode Driver and rte_eth_rx/tx_burst</h3><span class="tag tag-teal">PMD</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Port initialization */</span>
<span class="ck">static int</span> port_init(uint16_t port, <span class="ck">struct</span> rte_mempool *mp) {
    <span class="ck">struct</span> rte_eth_conf port_conf = {
        .rxmode = { .max_lro_pkt_size = RTE_ETHER_MAX_LEN },
        .txmode = { .mq_mode = RTE_ETH_MQ_TX_NONE },
    };
    <span class="ck">const int</span> rx_rings = 1, tx_rings = 1;
    uint16_t nb_rxd = 1024, nb_txd = 1024;
 
    rte_eth_dev_configure(port, rx_rings, tx_rings, &port_conf);
    rte_eth_dev_adjust_nb_rx_tx_desc(port, &nb_rxd, &nb_txd);
 
    <span class="cm">/* Setup RX queue on NUMA-local socket */</span>
    rte_eth_rx_queue_setup(port, 0, nb_rxd,
        rte_eth_dev_socket_id(port), NULL, mp);
    <span class="cm">/* Setup TX queue */</span>
    rte_eth_tx_queue_setup(port, 0, nb_txd,
        rte_eth_dev_socket_id(port), NULL);
 
    rte_eth_dev_start(port);
    rte_eth_promiscuous_enable(port);
    return 0;
}
 
<span class="cm">/* Core forwarding loop — the main performance-critical loop */</span>
<span class="ck">static int</span> lcore_main(void *arg) {
    uint16_t port;
    <span class="ck">struct</span> rte_mbuf *bufs[BURST_SIZE];  <span class="cm">/* BURST_SIZE = 32 */</span>
 
    RTE_ETH_FOREACH_DEV(port) {
        <span class="ck">if</span> (rte_eth_dev_socket_id(port) > 0 &&
            rte_eth_dev_socket_id(port) != (<span class="ck">int</span>)rte_socket_id())
            printf(<span class="cs">"WARNING: port %u is on remote NUMA\n"</span>, port);
    }
 
    printf(<span class="cs">"Core %u forwarding. [Ctrl+C to quit]\n"</span>, rte_lcore_id());
 
    <span class="ck">while</span> (1) {
        RTE_ETH_FOREACH_DEV(port) {
            <span class="cm">/* POLL: pull up to BURST_SIZE packets from NIC RX queue */</span>
            uint16_t nb_rx = rte_eth_rx_burst(port, 0, bufs, BURST_SIZE);
            <span class="ck">if</span> (nb_rx == 0) <span class="ck">continue</span>;  <span class="cm">/* nothing received */</span>
 
            <span class="cm">/* Process each packet */</span>
            <span class="ck">for</span> (uint16_t i = 0; i < nb_rx; i++) {
                process_packet(bufs[i]);  <span class="cm">/* L3 lookup, NAT, filter... */</span>
            }
 
            <span class="cm">/* Burst transmit — send all processed packets */</span>
            uint16_t nb_tx = rte_eth_tx_burst(port ^ 1, 0, bufs, nb_rx);
            <span class="cm">/* Free any packets that failed to transmit */</span>
            <span class="ck">if</span> (nb_tx < nb_rx)
                rte_pktmbuf_free_bulk(&bufs[nb_tx], nb_rx - nb_tx);
        }
    }
}
 
<span class="cm">/* Why burst size matters for performance */</span>
<span class="cm"># Burst=1:  function call overhead dominates → low throughput</span>
<span class="cm"># Burst=32: amortize call overhead, fill cache with packet data → optimal</span>
<span class="cm"># Burst=128: diminishing returns, prefetch distance too large</span>
<span class="cm"># Empirically: 32 is optimal for most workloads</span></pre></div>
  </div>
</div>
</div>

<!-- TAB 4 -->
<div id="t4" class="tab-pane">
<p class="sep">RSS AND FLOW DIRECTOR — HARDWARE PACKET STEERING</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>RSS Configuration and Flow Director</h3><span class="tag tag-purple">RSS</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* RSS — Receive Side Scaling */</span>
<span class="cm">/* NIC hashes packet 5-tuple → assigns to RX queue → specific lcore */</span>
<span class="cm">/* Ensures packets of same flow always go to same core (session affinity) */</span>
 
<span class="ck">struct</span> rte_eth_conf port_conf = {
    .rxmode = {
        .mq_mode = RTE_ETH_MQ_RX_RSS,
    },
    .rx_adv_conf = {
        .rss_conf = {
            .rss_key = NULL,     <span class="cm">/* NULL = use default 40-byte key */</span>
            .rss_hf  = RTE_ETH_RSS_IP | RTE_ETH_RSS_TCP | RTE_ETH_RSS_UDP,
        },
    },
};
 
<span class="cm">/* Per-packet RSS hash (computed by NIC hardware) */</span>
<span class="ck">if</span> (m->ol_flags & RTE_MBUF_F_RX_RSS_HASH)
    uint32_t hash = m->hash.rss;  <span class="cm">/* use for flow table lookup */</span>
 
<span class="cm">/* Symmetric RSS — ensure fwd and return packets land on same core */</span>
<span class="cm">/* Standard RSS: hash(sIP,dIP,sPort,dPort) — fwd and return differ! */</span>
<span class="cm">/* Symmetric: hash(sIP^dIP, sPort^dPort) — XOR makes it symmetric */</span>
<span class="cm">/* Implemented by using a special Toeplitz key: */</span>
<span class="ck">static uint8_t sym_rss_key[] = {
    0x6d, 0x5a, 0x56, 0xda, 0x25, 0x5b, 0x0e, 0xc2,
    0x41, 0x67, 0x25, 0x3d, 0x43, 0xa3, 0x8f, 0xb0,
    0xd0, 0xca, 0x2b, 0xcb, 0xae, 0x7b, 0x30, 0xb4,
    0x77, 0xcb, 0x2d, 0xa3, 0x80, 0x30, 0xf2, 0x0c,
    0x6a, 0x42, 0xb7, 0x3b, 0xbe, 0xac, 0x01, 0xfa,
};</span>
 
<span class="cm">/* Flow Director — exact-match steering beyond RSS */</span>
<span class="cm">/* Program specific 5-tuples → specific queue */</span>
<span class="ck">struct</span> rte_flow_attr attr = { .ingress = 1 };
<span class="ck">struct</span> rte_flow_item pattern[4];
<span class="ck">struct</span> rte_flow_action action[2];
 
<span class="cm">/* Match IPv4 + TCP dst port 80 */</span>
<span class="ck">struct</span> rte_flow_item_ipv4 ipv4_spec = { .hdr.dst_addr = htonl(0xc0a80001) };
<span class="ck">struct</span> rte_flow_item_tcp  tcp_spec  = { .hdr.dst_port = htons(80) };
<span class="cm">/* → send to queue 3 */</span>
<span class="ck">struct</span> rte_flow_action_queue queue_action = { .index = 3 };
 
<span class="cm">/* Create the flow rule */</span>
<span class="ck">struct</span> rte_flow_error error;
<span class="ck">struct</span> rte_flow *flow = rte_flow_create(port_id, &attr,
    pattern, action, &error);</pre></div>
  </div>
</div>
</div>

<!-- TAB 5 -->
<div id="t5" class="tab-pane">
<p class="sep">DPDK PIPELINES — STRUCTURING COMPLEX DATA PLANES</p>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">🏭</span><h3>Run-to-Completion vs Pipeline Models</h3><span class="tag tag-amber">PIPELINES</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Model 1: Run-to-Completion (RTC) */</span>
<span class="cm">/* Each lcore processes packets end-to-end: RX → all processing → TX */</span>
<span class="cm">/* Pros: no inter-core communication, lowest latency */</span>
<span class="cm">/* Cons: all processing must fit in one core's budget */</span>
 
lcore 0: RX port 0 → classify → ACL → NAT → TX port 1
lcore 1: RX port 1 → classify → ACL → NAT → TX port 0
lcore 2: RX port 2 → classify → ACL → NAT → TX port 3
 
<span class="cm">/* Model 2: Pipeline (assembly line) */</span>
<span class="cm">/* Different cores handle different stages; communicate via ring queues */</span>
<span class="cm">/* Pros: each stage specialised, cache-friendly per stage */</span>
<span class="cm">/* Cons: ring enqueue/dequeue latency, pipeline stalls */</span>
 
lcore 0 (RX):      NIC → mbuf → enqueue to classify_ring
lcore 1 (Classify): dequeue → L3 parse → enqueue to acl_ring
lcore 2 (ACL):     dequeue → policy check → enqueue to nat_ring
lcore 3 (NAT+TX):  dequeue → NAT → NIC TX
 
<span class="cm">/* rte_ring — lock-free SPSC/MPSC/SPMC/MPMC ring queue */</span>
<span class="ck">struct</span> rte_ring *ring = rte_ring_create(<span class="cs">"MY_RING"</span>, 4096,
    rte_socket_id(), RING_F_SP_ENQ | RING_F_SC_DEQ);
 
<span class="cm">/* Enqueue (producer side) */</span>
rte_ring_enqueue_burst(ring, (<span class="ck">void</span> **)mbufs, nb_mbufs, NULL);
 
<span class="cm">/* Dequeue (consumer side) */</span>
uint16_t n = rte_ring_dequeue_burst(ring, (<span class="ck">void</span> **)mbufs,
    BURST_SIZE, NULL);
 
<span class="cm">/* DPDK Graph framework (DPDK 20.11+) */</span>
<span class="cm">/* Modern way to build pipelines: graph of nodes, edges are rte_rings */</span>
<span class="cm">/* Nodes: ip4_lookup, ip4_rewrite, acl_classify, etc. */</span>
<span class="cm">/* Automatic vectorisation: processes batch of packets per node */</span></pre></div>
  </div>
</div>
</div>

<!-- TAB 6 -->
<div id="t6" class="tab-pane">
<p class="sep">DPDK PERFORMANCE TUNING</p>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Systematic Performance Optimisation</h3><span class="tag tag-red">TUNING</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* 1. CPU isolation — dedicate cores to DPDK */</span>
<span class="cm"># Kernel boot: isolcpus=4-7,nohz_full=4-7,rcu_nocbs=4-7</span>
<span class="cm"># DPDK EAL: -l 4-7  (use cores 4-7)</span>
<span class="cm"># These cores will spin 100% polling — don't share with OS</span>
 
<span class="cm">/* 2. NUMA awareness — memory on same socket as NIC */</span>
<span class="ck">if</span> (rte_eth_dev_socket_id(port) != (<span class="ck">int</span>)rte_socket_id()) {
    printf(<span class="cs">"NUMA mismatch: NIC on socket %d, core on socket %d\n"</span>,
           rte_eth_dev_socket_id(port), rte_socket_id());
    <span class="cm">/* Cross-NUMA memory access: +60ns latency per access */</span>
    <span class="cm">/* Fix: pin workers to same NUMA node as their NIC */</span>
}
<span class="cm">/* Mempool MUST be on same NUMA as NIC: */</span>
rte_pktmbuf_pool_create(<span class="cs">"MP"</span>, N, 256, 0, BUF_SIZE,
    rte_eth_dev_socket_id(port));  <span class="cm">/* NOT rte_socket_id() */</span>
 
<span class="cm">/* 3. Prefetching — hide memory latency */</span>
<span class="ck">for</span> (i = 0; i < nb_rx; i++) {
    <span class="ck">if</span> (i + 4 < nb_rx)
        rte_prefetch0(rte_pktmbuf_mtod(bufs[i + 4], void *));
    process_packet(bufs[i]);  <span class="cm">/* by the time we process [i], [i+4] is in L1 */</span>
}
 
<span class="cm">/* 4. TX descriptor writeback — reduce PCIe round trips */</span>
<span class="ck">struct</span> rte_eth_txconf txconf = {
    .tx_thresh = { .pthresh = 32, .hthresh = 0, .wthresh = 0 },
    .tx_free_thresh = 32,        <span class="cm">/* free 32 at once, not 1 by 1 */</span>
};
 
<span class="cm">/* 5. Offloads — hardware helps software */</span>
<span class="ck">struct</span> rte_eth_conf port_conf = {
    .rxmode.offloads = RTE_ETH_RX_OFFLOAD_CHECKSUM |  <span class="cm">/* HW validates cksum */</span>
                       RTE_ETH_RX_OFFLOAD_RSS_HASH,    <span class="cm">/* HW computes RSS */</span>
    .txmode.offloads = RTE_ETH_TX_OFFLOAD_IPV4_CKSUM | <span class="cm">/* HW fills IP cksum */</span>
                       RTE_ETH_TX_OFFLOAD_TCP_CKSUM,   <span class="cm">/* HW fills TCP cksum */</span>
};
 
<span class="cm">/* 6. Measuring performance */</span>
uint64_t hz = rte_get_timer_hz();
uint64_t start = rte_get_timer_cycles();
<span class="cm">/* ... process N packets ... */</span>
uint64_t elapsed = rte_get_timer_cycles() - start;
double mpps = (double)N / ((double)elapsed / hz) / 1e6;
printf(<span class="cs">"%.2f Mpps (%.1f ns/packet)\n"</span>, mpps, 1e9 * elapsed / hz / N);</pre></div>
  </div>
</div>
</div>

<!-- TAB 7 -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>DPDK Packet Counter and L3 Forwarder</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build the classic DPDK "basicfwd" — receive packets, swap MAC addresses, transmit back. Add per-flow counters.</p>
    <div class="lab-step"><div class="sn">1</div><div>Set up hugepages and bind a test NIC (or use vdev): <code>dpdk-devbind.py --bind=vfio-pci 0000:01:00.0</code>. Build and run the DPDK skeleton from the EAL tab. Verify you can receive packets.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Implement L2 forwarding: for each received packet, swap src/dst MAC (rte_ether_addr_copy), update checksums if needed, transmit on the other port. This is the DPDK equivalent of a wire — measure throughput with pktgen-dpdk.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Add an rte_hash table (BPF-style hash map for DPDK): key = 5-tuple, value = packet count. For each received packet, parse IP+TCP/UDP headers, lookup/create entry, increment count. Print top-10 flows by packet count every 5 seconds.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Benchmark: measure Mpps with different burst sizes (1, 4, 8, 16, 32, 64). Plot throughput vs burst size. Identify the optimal burst size for your hardware. Document what limits throughput (PCIe bandwidth? CPU cycles? Memory bandwidth?).</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Multi-Core DPDK with RSS</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Scale DPDK forwarding to multiple cores using RSS for flow distribution.</p>
    <div class="lab-step"><div class="sn">1</div><div>Configure 4 RX queues and 4 TX queues on your test NIC. Set RSS to distribute based on IP+TCP 5-tuple. Launch 4 worker threads, one per queue: lcore 4 handles queue 0, lcore 5 handles queue 1, etc.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Generate flows from a traffic generator with varying 5-tuples. Verify RSS distribution: read per-queue packet counters from <code>rte_eth_stats_get()</code>. Distribution should be roughly even (within 10%).</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Compare symmetric vs asymmetric RSS: try the standard Toeplitz key, then the symmetric key. Verify that with symmetric RSS, forward and reverse flows of the same connection land on the same queue.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Performance Profiling Deep-Dive</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Profile your DPDK application at the cycle level and identify bottlenecks.</p>
    <div class="lab-step"><div class="sn">1</div><div>Enable Intel PMU counters in your forwarding loop: measure cycles per packet, LLC cache misses per packet, DRAM accesses per packet using perf on the isolated cores: <code>perf stat -e cycles,cache-misses,dTLB-misses -C 4 sleep 5</code>.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Profile memory access patterns: add artificial 5-tuple lookups against a 10K-entry rte_hash table. Measure performance with table in L3 cache (small table) vs DRAM (large table). Quantify the cost of a single cache miss in ns.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Test NUMA effects: move your mempool to the remote NUMA node (use socket_id = 1 - rte_eth_dev_socket_id(port)). Measure the throughput degradation. Verify the ~60ns cross-NUMA penalty empirically.</div></div>
  </div>
</div>
</div>

<!-- TAB 8 -->
<div id="t8" class="tab-pane">
<p class="sep">M17 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know the 5 root causes of kernel networking overhead and how DPDK eliminates each</li>
  <li>Know DPDK performance numbers: ~30-80 Mpps/core vs kernel ~1-3 Mpps/core</li>
  <li>Know EAL responsibilities: hugepage management, CPU affinity, PCI device mapping, NUMA awareness</li>
  <li>Know EAL CLI options: -l (cores), -n (memory channels), --socket-mem, -a (PCI allowlist)</li>
  <li>Know hugepage requirement and why: 2MB pages reduce TLB pressure (512 vs 262,144 entries for 1GB)</li>
  <li>Know rte_mbuf key fields: buf_addr/buf_iova, data_off, data_len, pkt_len, next, ol_flags, hash.rss</li>
  <li>Know rte_mempool design: global ring + per-lcore cache, lock-free on common path</li>
  <li>Know the PMD polling model: spin loop calling rte_eth_rx_burst, no interrupts ever</li>
  <li>Know why burst size matters: amortizes function call overhead; optimal typically 32</li>
  <li>Know NUMA mismatch penalty: ~60ns latency per cross-NUMA memory access</li>
  <li>Know RSS configuration: mq_mode=RSS, rss_hf for hash fields (IP, TCP, UDP)</li>
  <li>Know symmetric RSS problem and solution: XOR-based Toeplitz key ensures fwd/return on same core</li>
  <li>Know Flow Director: exact-match 5-tuple → specific queue steering (harder than RSS, more precise)</li>
  <li>Know run-to-completion vs pipeline models; when to choose each</li>
  <li>Know rte_ring: lock-free SPSC/MPSC/SPMC/MPMC; used to connect pipeline stages</li>
  <li>Know TX offloads: RTE_ETH_TX_OFFLOAD_IPV4_CKSUM, TCP_CKSUM — hardware fills checksums</li>
  <li>Know prefetching pattern: prefetch N+4 while processing N to hide memory latency</li>
  <li>Completed Lab 1: built DPDK L2 forwarder with per-flow hash table counters, benchmarked burst sizes</li>
  <li>Completed Lab 2: configured multi-core with RSS, verified symmetric flow distribution</li>
  <li>Completed Lab 3: profiled with PMU counters, quantified NUMA penalty and cache miss cost</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M18 - VPP and Data Plane Development</strong> — the final Phase 4 module, covering the vector packet processor your team actively uses for R&D.</p>
</div>
</div>

<div class="mod-nav">
  <a href="/learning/networking-mastery/m16-ebpf-xdp/">← M16 eBPF/XDP</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m18-vpp/">Next: M18 - VPP →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
