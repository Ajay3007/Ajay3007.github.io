---
layout: learning
title: "DPDK P2 — Poll Mode Drivers & Port Config"
permalink: /learning/data-plane/dpdk/module-p2-pmd/
---
<style>
.mod-header{background:linear-gradient(135deg,#041a14 0%,#0b3028 60%,#1a6058 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#5adbc8;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#a8e0d8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#c8f4ee}
.tab-bar{display:flex;flex-wrap:wrap;gap:0;background:#0b3028;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#5adbc8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#40f0d8;border-bottom-color:#40f0d8}
.tab-pane{display:none}
.tab-pane.active{display:block}
.p-teal{background:#e8f6f4;border-left:4px solid #1a7a6e;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-blue{background:#eaf2fc;border-left:4px solid #2e6da4;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-orange{background:#fdf0e8;border-left:4px solid #c05e1b;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-slate{background:#f4f6f8;border-left:4px solid #64748b;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
[data-theme=dark] .p-teal{background:#0d2020;border-color:#2a9a8e}
[data-theme=dark] .p-blue{background:#0d1e34;border-color:#4a90d9}
[data-theme=dark] .p-orange{background:#1e0d00;border-color:#e07830}
[data-theme=dark] .p-slate{background:#1a1e24;border-color:#8898aa}
.p-teal h4,.p-blue h4,.p-orange h4,.p-slate h4{margin:0 0 .5rem;font-size:.9rem;font-weight:700}
.ins{background:#e8f5e9;border:1px solid #66bb6a;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.warn{background:#fff8e1;border:1px solid #ffca28;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.note{background:#e3f2fd;border:1px solid #42a5f5;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
[data-theme=dark] .ins{background:#0d2010;border-color:#388e3c}
[data-theme=dark] .warn{background:#1e1800;border-color:#f9a825}
[data-theme=dark] .note{background:#0d1e2e;border-color:#1976d2}
.cb{background:#0d1117;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;font-family:monospace;font-size:.82rem;line-height:1.7;color:#e6edf3;white-space:pre-wrap}
.cb .cm{color:#8b949e}.cb .ck{color:#ff7b72}.cb .cv{color:#79c0ff}.cb .cs{color:#a5d6ff}.cb .cn{color:#f2cc60}.cb .cf{color:#d2a8ff}.cb .co{color:#ffa657}.cb .cg{color:#3fb950}
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.8rem 0}
.t-table th{background:#0b3028;color:#5adbc8;font-family:monospace;font-size:.75rem;font-weight:700;padding:.5rem .7rem;text-align:left;border-bottom:2px solid #1a6040}
.t-table td{padding:.45rem .7rem;border-bottom:1px solid var(--border-color,#e8e8e8);vertical-align:top}
.t-table tr:last-child td{border-bottom:none}
.t-table tr:hover td{background:var(--bg-color,#f8f9fa)}
.flow-list{list-style:none;padding:0;margin:.8rem 0}
.fl-step{display:flex;gap:.8rem;margin-bottom:.5rem;font-size:.88rem;line-height:1.6}
.fl-num{width:24px;height:24px;border-radius:50%;background:#1a7a6e;color:#fff;font-size:.72rem;font-weight:800;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:.15rem}
.diagram-box{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;font-family:monospace;font-size:.78rem;line-height:1.8;color:#c9d1d9;overflow-x:auto;white-space:pre}
.lab-box{background:var(--card-bg,#fff);border:2px solid #1a7a6e;border-radius:10px;overflow:hidden;margin:1rem 0}
.lab-hdr{background:#0b3028;color:#fff;padding:.7rem 1.2rem;font-weight:700;font-family:monospace;font-size:.9rem}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.5rem;font-size:.87rem}
.sn{background:#1a7a6e;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:800;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{padding:.3rem 0;font-size:.87rem;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐ ";font-size:1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#0b3028;color:#fff !important;border-color:#0b3028}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">DPDK MASTERY · PHASE 2 OF 3 · MODULE A</div>
  <div class="mod-title">Poll Mode Drivers &amp; Port Config</div>
  <div class="mod-subtitle">PMD internals · NIC descriptor rings · rx_burst / tx_burst hot path · RSS · Port configuration sequence</div>
  <div class="mod-pills">
    <span class="mod-pill">Ch 7 — PMD Deep Dive</span>
    <span class="mod-pill">Ch 8 — Port Configuration</span>
    <span class="mod-pill">Ch 9 — RSS Deep Dive</span>
    <span class="mod-pill">C · ixgbe · mlx5 · Toeplitz</span>
    <span class="mod-pill">Weeks 6–8</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t-pmd')">PMD Types</button>
  <button class="tab-btn" onclick="vt(event,'t-ring')">Descriptor Rings</button>
  <button class="tab-btn" onclick="vt(event,'t-burst')">rx/tx_burst</button>
  <button class="tab-btn" onclick="vt(event,'t-portcfg')">Port Config</button>
  <button class="tab-btn" onclick="vt(event,'t-offload')">Offloads &amp; Stats</button>
  <button class="tab-btn" onclick="vt(event,'t-rss')">RSS &amp; RETA</button>
  <button class="tab-btn" onclick="vt(event,'t-qa')">Interview Q&amp;A</button>
  <button class="tab-btn" onclick="vt(event,'t-lab')">Lab</button>
</div>

<!-- TAB: PMD Types -->
<div id="t-pmd" class="tab-pane active">

<div class="p-teal">
<h4>What a PMD Is</h4>
A Poll Mode Driver (PMD) is a <strong>user-space NIC driver</strong> that replaces the kernel driver for a specific NIC model. It maps NIC BAR (Base Address Register) memory into user-space via VFIO/UIO and programs the NIC's hardware descriptor rings directly. It provides <code>rte_eth_rx_burst()</code> and <code>rte_eth_tx_burst()</code> implementations — called millions of times per second with zero system calls.
</div>

<table class="t-table">
<thead><tr><th>PMD Type</th><th>Examples</th><th>Description</th><th>Notes</th></tr></thead>
<tbody>
<tr><td><strong>Physical NIC</strong></td><td><code>ixgbe</code> (X520), <code>i40e</code> (XL710), <code>ice</code> (E810), <code>mlx5</code> (ConnectX)</td><td>Direct hardware driver — maximum performance</td><td>Requires device binding (except mlx5 bifurcated)</td></tr>
<tr><td><strong>Virtual NIC</strong></td><td><code>virtio</code> (KVM), <code>vmxnet3</code> (VMware), <code>vhost-user</code></td><td>VM-facing PMD — communicates via shared memory</td><td>Lower performance than physical — no DMA bypass</td></tr>
<tr><td><strong>Software (vdev)</strong></td><td><code>net_ring</code>, <code>net_tap</code>, <code>net_pcap</code>, <code>net_null</code></td><td>Software-only — testing, kernel bridging, dev</td><td>No real NIC needed — great for unit testing</td></tr>
<tr><td><strong>Bonding</strong></td><td><code>net_bonding</code></td><td>Aggregates multiple physical PMDs into one logical port</td><td>LAG/LACP support; active-backup or LACP mode</td></tr>
</tbody>
</table>

<div class="note">&#128204; <strong>PMD as function pointer table:</strong> Each PMD registers a set of function pointers (<code>eth_rx_burst_t</code>, <code>eth_tx_burst_t</code>, etc.) at probe time. When you call <code>rte_eth_rx_burst()</code>, it's an indirect function call through this table — PMD-specific code runs directly, fully inlined per NIC type. This is why different NICs can coexist in one DPDK application.</div>

</div><!-- /t-pmd -->

<!-- TAB: Descriptor Rings -->
<div id="t-ring" class="tab-pane">

<div class="p-teal">
<h4>NIC Hardware Descriptor Rings</h4>
The descriptor ring is a circular array in hugepage memory shared between the NIC hardware and the PMD software. It is the fundamental data transfer mechanism — no pipes, no queues, no kernel — just two pointers (NIC's and PMD's) into a shared ring.
</div>

<div class="diagram-box">Rx Descriptor Ring (in hugepage memory, DMA-accessible by NIC)

 ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
 │desc0│desc1│desc2│desc3│desc4│desc5│desc6│desc7│  ← ring[nb_rx_desc]
 └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
            ↑ NIC write ptr                ↑ CPU read ptr

Each descriptor contains:
  buf_addr (IOVA of pre-allocated mbuf)
  buf_len  (size of the buffer)
  status   (including DD = Descriptor Done bit)

Flow:
  CPU fills ring[i].buf_addr = IOVA of empty mbuf (pre-loaded at setup)
  NIC DMA writes packet data into that IOVA
  NIC sets ring[i].status |= DD bit  ← handshake signal
  PMD polls: if DD bit set → packet is ready → read mbuf</div>

<p class="sep">RX DESCRIPTOR LIFECYCLE</p>

<ul class="flow-list">
<li class="fl-step"><span class="fl-num">1</span><div><strong>Setup:</strong> <code>rte_eth_rx_queue_setup()</code> pre-fills all ring slots with empty mbuf IOVAs from the mempool</div></li>
<li class="fl-step"><span class="fl-num">2</span><div><strong>Packet arrives:</strong> NIC DMA engine writes packet bytes into the mbuf at that IOVA — zero CPU involvement</div></li>
<li class="fl-step"><span class="fl-num">3</span><div><strong>NIC signals done:</strong> NIC sets DD bit in descriptor + writes pkt_len, ol_flags, RSS hash</div></li>
<li class="fl-step"><span class="fl-num">4</span><div><strong>PMD polls:</strong> <code>rte_eth_rx_burst()</code> checks DD bit → mbuf is ready → copies metadata into mbuf fields</div></li>
<li class="fl-step"><span class="fl-num">5</span><div><strong>Refill:</strong> PMD allocates fresh mbuf from pool → puts its IOVA into the now-empty ring slot → NIC can reuse</div></li>
<li class="fl-step"><span class="fl-num">6</span><div><strong>Returns:</strong> PMD returns received mbuf to application — total latency: ~20–50 ns from DD bit set</div></li>
</ul>

<p class="sep">TX DESCRIPTOR LIFECYCLE</p>

<ul class="flow-list">
<li class="fl-step"><span class="fl-num">1</span><div><strong>App calls:</strong> <code>rte_eth_tx_burst(port, queue, mbufs[], n)</code></div></li>
<li class="fl-step"><span class="fl-num">2</span><div><strong>PMD fills Tx descriptor:</strong> writes mbuf's IOVA + length + offload flags, updates Tx tail pointer</div></li>
<li class="fl-step"><span class="fl-num">3</span><div><strong>NIC DMA:</strong> reads packet from mbuf buffer → sends on wire</div></li>
<li class="fl-step"><span class="fl-num">4</span><div><strong>NIC sets DD:</strong> on completed descriptor (async — NIC is busy sending next packets)</div></li>
<li class="fl-step"><span class="fl-num">5</span><div><strong>Lazy free:</strong> PMD frees completed Tx mbufs on the <em>next</em> tx_burst call or when tx_free_thresh crossed</div></li>
</ul>

<div class="warn">&#9888;&#65039; <strong>Critical:</strong> <code>rte_eth_tx_burst()</code> returns the count of packets actually queued (may be less than <code>n</code> if Tx ring is full). Caller MUST free any unsent packets: <code>pkts[nb_tx..n-1]</code>. Failing to do so causes mbuf leaks → mempool exhaustion → rx_burst returns 0 mbufs → application appears to stop receiving packets.</div>

</div><!-- /t-ring -->

<!-- TAB: rx/tx_burst -->
<div id="t-burst" class="tab-pane">

<p class="sep">RX_BURST — THE HOT PATH FUNCTION</p>

<div class="cb"><span class="cm">// rte_eth_rx_burst signature</span>
<span class="co">uint16_t</span> <span class="cf">rte_eth_rx_burst</span>(
    <span class="co">uint16_t</span>          port_id,    <span class="cm">// which NIC port</span>
    <span class="co">uint16_t</span>          queue_id,   <span class="cm">// which Rx queue on that port</span>
    <span class="ck">struct</span> rte_mbuf **rx_pkts,    <span class="cm">// output: array of received mbufs</span>
    <span class="co">uint16_t</span>          nb_pkts     <span class="cm">// max mbufs to receive (burst size)</span>
);
<span class="cm">// Returns: actual number of mbufs received (0 to nb_pkts)</span>

<span class="cm">// Canonical polling loop</span>
<span class="ck">struct</span> rte_mbuf *pkts[<span class="cn">BURST_SIZE</span>];
<span class="ck">while</span> (<span class="cn">1</span>) {
    <span class="co">uint16_t</span> nb_rx = <span class="cf">rte_eth_rx_burst</span>(port, queue, pkts, <span class="cn">BURST_SIZE</span>);
    <span class="ck">for</span> (<span class="co">uint16_t</span> i = <span class="cn">0</span>; i &lt; nb_rx; i++)
        <span class="cf">process_packet</span>(pkts[i]);
}</div>

<p class="sep">TX_BURST — SAFE TRANSMIT PATTERN</p>

<div class="cb"><span class="cm">// rte_eth_tx_burst — ALWAYS check return value</span>
<span class="co">uint16_t</span> nb_tx = <span class="cf">rte_eth_tx_burst</span>(port, queue, pkts, nb_pkts);

<span class="cm">// Free unsent packets (Tx ring was full)</span>
<span class="ck">if</span> (<span class="cf">unlikely</span>(nb_tx &lt; nb_pkts)) {
    <span class="ck">for</span> (<span class="co">uint16_t</span> i = nb_tx; i &lt; nb_pkts; i++)
        <span class="cf">rte_pktmbuf_free</span>(pkts[i]);
}</div>

<p class="sep">BURST SIZE TUNING</p>

<table class="t-table">
<thead><tr><th>Burst Size</th><th>Throughput</th><th>Latency</th><th>Cache Usage</th><th>Recommendation</th></tr></thead>
<tbody>
<tr><td>8</td><td>Good for low load</td><td>Lowest</td><td>Minimal</td><td>Low-latency SLAs</td></tr>
<tr><td>32</td><td>Good balance</td><td>Moderate</td><td>Good I-cache reuse</td><td>Blaze/SASE-DP default</td></tr>
<tr><td>64</td><td>High throughput</td><td>Higher</td><td>Excellent</td><td>DPDK example default</td></tr>
<tr><td>128+</td><td>Marginal improvement</td><td>Higher</td><td>Diminishing returns</td><td>May exceed L1 cache</td></tr>
</tbody>
</table>

<div class="ins">&#127381; <strong>Blaze/SASE-DP Real-World Finding:</strong> With 100G NIC and 8 workers, burst size 32 gave the best latency/throughput balance. At burst=64 throughput was ~3% higher but p99 latency increased ~15%. At burst=16, throughput dropped ~8%. Start with 32 — tune based on your latency SLA vs throughput target.</div>

</div><!-- /t-burst -->

<!-- TAB: Port Config -->
<div id="t-portcfg" class="tab-pane">

<p class="sep">PORT CONFIGURATION — MANDATORY ORDER</p>

<ul class="flow-list">
<li class="fl-step"><span class="fl-num">1</span><div><strong>rte_eal_init()</strong> — initialize EAL (hugepages, lcores, PCI probe)</div></li>
<li class="fl-step"><span class="fl-num">2</span><div><strong>rte_eth_dev_count_avail()</strong> — how many NIC ports are available?</div></li>
<li class="fl-step"><span class="fl-num">3</span><div><strong>rte_eth_dev_info_get()</strong> — query NIC capabilities (max queues, offload flags, desc limits)</div></li>
<li class="fl-step"><span class="fl-num">4</span><div><strong>rte_pktmbuf_pool_create()</strong> — create mbuf pool on NIC's NUMA socket</div></li>
<li class="fl-step"><span class="fl-num">5</span><div><strong>rte_eth_dev_configure()</strong> — configure port: number of queues, offloads, RSS</div></li>
<li class="fl-step"><span class="fl-num">6</span><div><strong>rte_eth_rx_queue_setup()</strong> — setup each Rx queue (descriptor count, socket, pool)</div></li>
<li class="fl-step"><span class="fl-num">7</span><div><strong>rte_eth_tx_queue_setup()</strong> — setup each Tx queue (descriptor count, socket)</div></li>
<li class="fl-step"><span class="fl-num">8</span><div><strong>rte_eth_dev_start()</strong> — start the device (enables DMA, activates queues)</div></li>
<li class="fl-step"><span class="fl-num">9</span><div><strong>rte_eth_promiscuous_enable()</strong> — optional: receive all traffic regardless of dst MAC</div></li>
<li class="fl-step"><span class="fl-num">10</span><div><strong>rte_eth_link_get_nowait()</strong> — poll until link is UP</div></li>
</ul>

<div class="cb"><span class="cm">// Full port configuration example</span>
<span class="ck">struct</span> rte_eth_conf port_conf = {
    .rxmode = {
        .mtu     = <span class="cn">RTE_ETHER_MAX_LEN</span>,
        .offloads = <span class="cn">RTE_ETH_RX_OFFLOAD_CHECKSUM</span> |
                    <span class="cn">RTE_ETH_RX_OFFLOAD_RSS_HASH</span>,
    },
    .txmode = {
        .mq_mode  = <span class="cn">RTE_ETH_MQ_TX_NONE</span>,
        .offloads = <span class="cn">RTE_ETH_TX_OFFLOAD_IPV4_CKSUM</span> |
                    <span class="cn">RTE_ETH_TX_OFFLOAD_TCP_CKSUM</span>,
    },
    .rx_adv_conf.rss_conf = {
        .rss_key = NULL,   <span class="cm">// use default 40-byte RSS key</span>
        .rss_hf  = <span class="cn">RTE_ETH_RSS_IP</span> | <span class="cn">RTE_ETH_RSS_TCP</span> | <span class="cn">RTE_ETH_RSS_UDP</span>,
    },
};

<span class="cf">rte_eth_dev_configure</span>(port_id, nb_rx_queues, nb_tx_queues, &amp;port_conf);

<span class="ck">for</span> (<span class="co">uint16_t</span> q = <span class="cn">0</span>; q &lt; nb_rx_queues; q++)
    <span class="cf">rte_eth_rx_queue_setup</span>(port_id, q, <span class="cn">512</span>,   <span class="cm">// nb_rx_desc</span>
        <span class="cf">rte_eth_dev_socket_id</span>(port_id), NULL, mbuf_pool);

<span class="ck">for</span> (<span class="co">uint16_t</span> q = <span class="cn">0</span>; q &lt; nb_tx_queues; q++)
    <span class="cf">rte_eth_tx_queue_setup</span>(port_id, q, <span class="cn">512</span>,
        <span class="cf">rte_eth_dev_socket_id</span>(port_id), NULL);

<span class="cf">rte_eth_dev_start</span>(port_id);
<span class="cf">rte_eth_promiscuous_enable</span>(port_id);</div>

<table class="t-table">
<thead><tr><th>nb_rx_desc</th><th>Use Case</th><th>Trade-off</th></tr></thead>
<tbody>
<tr><td>256</td><td>Low latency, light load</td><td>Small ring → NIC drops more under burst → imissed increments</td></tr>
<tr><td>512</td><td>Balanced — common default</td><td>Good balance of memory vs burst tolerance</td></tr>
<tr><td>1024</td><td>High throughput, bursty traffic</td><td>More memory, better burst handling</td></tr>
<tr><td>4096</td><td>Line-rate 100G with large bursts</td><td>Maximum burst tolerance — highest memory use</td></tr>
</tbody>
</table>

</div><!-- /t-portcfg -->

<!-- TAB: Offloads & Stats -->
<div id="t-offload" class="tab-pane">

<table class="t-table">
<thead><tr><th>Offload Flag</th><th>Direction</th><th>Effect</th></tr></thead>
<tbody>
<tr><td><code>RTE_ETH_RX_OFFLOAD_CHECKSUM</code></td><td>Rx</td><td>NIC verifies IP/TCP/UDP checksums. Sets <code>RTE_MBUF_F_RX_*_CKSUM_GOOD/BAD</code> flags.</td></tr>
<tr><td><code>RTE_ETH_RX_OFFLOAD_RSS_HASH</code></td><td>Rx</td><td>NIC computes RSS hash. Sets <code>mbuf->hash.rss</code> and <code>RTE_MBUF_F_RX_RSS_HASH</code>.</td></tr>
<tr><td><code>RTE_ETH_RX_OFFLOAD_VLAN_STRIP</code></td><td>Rx</td><td>NIC strips VLAN tag from frame. Tag stored in <code>mbuf->vlan_tci</code>.</td></tr>
<tr><td><code>RTE_ETH_RX_OFFLOAD_SCATTER</code></td><td>Rx</td><td>Allow multi-segment mbufs (required for jumbo frames &gt; buf_size).</td></tr>
<tr><td><code>RTE_ETH_TX_OFFLOAD_IPV4_CKSUM</code></td><td>Tx</td><td>NIC computes and inserts IPv4 header checksum.</td></tr>
<tr><td><code>RTE_ETH_TX_OFFLOAD_TCP_CKSUM</code></td><td>Tx</td><td>NIC computes and inserts TCP checksum.</td></tr>
<tr><td><code>RTE_ETH_TX_OFFLOAD_VLAN_INSERT</code></td><td>Tx</td><td>NIC inserts VLAN tag from <code>mbuf->vlan_tci</code>.</td></tr>
<tr><td><code>RTE_ETH_TX_OFFLOAD_TCP_TSO</code></td><td>Tx</td><td>TCP Segmentation Offload — NIC segments large TCP to MTU-sized frames.</td></tr>
</tbody>
</table>

<p class="sep">PORT STATISTICS</p>

<div class="cb"><span class="cm">// Read port statistics</span>
<span class="ck">struct</span> rte_eth_stats stats;
<span class="cf">rte_eth_stats_get</span>(port_id, &amp;stats);
<span class="cf">printf</span>(<span class="cs">"Rx: %lu pkts, %lu bytes, %lu missed, %lu errors\n"</span>,
    stats.ipackets, stats.ibytes, stats.imissed, stats.ierrors);
<span class="cf">printf</span>(<span class="cs">"Tx: %lu pkts, %lu bytes, %lu errors\n"</span>,
    stats.opackets, stats.obytes, stats.oerrors);</div>

<table class="t-table">
<thead><tr><th>Stat Field</th><th>Meaning</th><th>Action if Non-Zero</th></tr></thead>
<tbody>
<tr><td><code>stats.imissed</code></td><td>Packets dropped by NIC hardware — Rx ring was full</td><td>Increase nb_rx_desc; increase burst_size; reduce processing latency; add more worker lcores</td></tr>
<tr><td><code>stats.ierrors</code></td><td>Receive errors (bad FCS, oversized frames)</td><td>Check cable/NIC health; check MTU configuration</td></tr>
<tr><td><code>stats.rx_nombuf</code></td><td>Packets dropped — no free mbufs in pool</td><td>Increase mempool size; check for mbuf leaks</td></tr>
<tr><td><code>stats.oerrors</code></td><td>Transmit errors</td><td>Check Tx configuration and offload flags</td></tr>
</tbody>
</table>

<div class="warn">&#9888;&#65039; <strong>imissed vs rx_nombuf:</strong> These are different failure modes. <code>imissed</code> = NIC couldn't write packet because the Rx ring had no empty descriptors (ring was full — software too slow to drain it). <code>rx_nombuf</code> = PMD tried to refill the ring but the mempool had no free mbufs (mbuf leak). Both result in dropped packets but have different root causes and fixes.</div>

</div><!-- /t-offload -->

<!-- TAB: RSS & RETA -->
<div id="t-rss" class="tab-pane">

<div class="p-teal">
<h4>RSS — Hardware Multi-Core Distribution</h4>
RSS (Receive Side Scaling) distributes incoming packets across multiple Rx queues using a hardware hash of the packet's 5-tuple. Each queue is serviced by one lcore. Because the same 5-tuple always maps to the same queue, all packets of a TCP connection always land on the same core — enabling <strong>lock-free per-flow state</strong>.
</div>

<p class="sep">RSS MECHANISM</p>

<div class="diagram-box">RSS — Packet to Queue Assignment (hardware path)

Packet arrives at NIC
  ↓
NIC parser extracts 5-tuple from fixed byte offsets:
  Src IP  @ bytes 26–29    Dst IP   @ bytes 30–33
  Src Port @ bytes 34–35   Dst Port @ bytes 36–37
  Protocol @ byte 23
  ↓
Toeplitz Hash Unit (silicon logic — runs at wire speed):
  Algorithm: for each input bit → if bit=1: hash XOR= key[i:i+32]
  Same 5-tuple always → same 32-bit hash (deterministic)
  Same 5-tuple → same hash → same queue → same lcore
  hash = 0x3A7F1C
  ↓
RETA (Redirection Table) lookup:
  queue = RETA[hash & (reta_size - 1)]
  RETA[0x1C] = queue 3
  ↓
Packet DMA'd into Rx Queue 3 → lcore 3 picks it up

All packets of one TCP connection always land on the same lcore.
Per-flow state on one lcore — no locking needed on hot path.</div>

<p class="sep">SYMMETRIC RSS KEY</p>

<div class="p-blue">
<h4>The Symmetric RSS Problem</h4>
By default, RSS is asymmetric: <code>hash(src=A, dst=B) ≠ hash(src=B, dst=A)</code>. For stateful NFs that process both directions of a flow, this means forward and return packets land on different cores — requiring cross-core state access. The symmetric Toeplitz key (Microsoft key) fixes this: <code>hash(A→B) == hash(B→A)</code>.
</div>

<div class="cb"><span class="cm">// Symmetric RSS key (Microsoft Toeplitz key)</span>
<span class="ck">static</span> <span class="co">uint8_t</span> sym_rss_key[] = {
    <span class="cn">0x6D</span>, <span class="cn">0x5A</span>, <span class="cn">0x56</span>, <span class="cn">0xDA</span>, <span class="cn">0x25</span>, <span class="cn">0x5B</span>, <span class="cn">0x0E</span>, <span class="cn">0xC2</span>,
    <span class="cn">0x41</span>, <span class="cn">0x67</span>, <span class="cn">0x25</span>, <span class="cn">0x3D</span>, <span class="cn">0x43</span>, <span class="cn">0xA3</span>, <span class="cn">0x8F</span>, <span class="cn">0xB0</span>,
    <span class="cn">0xD0</span>, <span class="cn">0xCA</span>, <span class="cn">0x2B</span>, <span class="cn">0xCB</span>, <span class="cn">0xAE</span>, <span class="cn">0x7B</span>, <span class="cn">0x30</span>, <span class="cn">0xB4</span>,
    <span class="cn">0x77</span>, <span class="cn">0xCB</span>, <span class="cn">0x2D</span>, <span class="cn">0xA3</span>, <span class="cn">0x80</span>, <span class="cn">0x30</span>, <span class="cn">0xF2</span>, <span class="cn">0x0C</span>,
    <span class="cn">0x6A</span>, <span class="cn">0x42</span>, <span class="cn">0xB7</span>, <span class="cn">0x3B</span>, <span class="cn">0xBE</span>, <span class="cn">0xAC</span>, <span class="cn">0x01</span>, <span class="cn">0xFA</span>,
};
<span class="cm">// Use in rss_conf.rss_key — guarantees forward/return on same lcore</span></div>

<p class="sep">RETA IMBALANCE — THE POWER-OF-2 REQUIREMENT</p>

<div class="warn">&#9888;&#65039; <strong>Blaze/SASE-DP Real-World Finding:</strong> With 6 workers (non-power-of-2) and RETA size=128: 128/6=21.33 → uneven. Queues 0-3 got 22 entries, queues 4-5 got 21 entries → cores 0-3 received ~5% more traffic. Under high load, cores 0-3 saturated first → throughput ceiling. Switching to 8 workers: all at ~91% utilization, throughput +12%. <strong>Rule: always use power-of-2 worker counts.</strong></div>

<div class="cb"><span class="cm">// Update RETA programmatically for even distribution</span>
<span class="co">uint16_t</span> reta_size;
<span class="cf">rte_eth_dev_info_get</span>(port_id, &amp;dev_info);
reta_size = dev_info.reta_size;   <span class="cm">// typically 128 or 512</span>

<span class="ck">struct</span> rte_eth_rss_reta_entry64 reta_conf[reta_size / <span class="cn">RTE_ETH_RETA_GROUP_SIZE</span>];
<span class="cf">memset</span>(reta_conf, <span class="cn">0</span>, <span class="ck">sizeof</span>(reta_conf));

<span class="ck">for</span> (<span class="co">uint16_t</span> i = <span class="cn">0</span>; i &lt; reta_size; i++) {
    <span class="co">uint16_t</span> grp = i / <span class="cn">RTE_ETH_RETA_GROUP_SIZE</span>;
    <span class="co">uint16_t</span> idx = i % <span class="cn">RTE_ETH_RETA_GROUP_SIZE</span>;
    reta_conf[grp].mask         = <span class="cn">UINT64_MAX</span>;
    reta_conf[grp].reta[idx]    = i % nb_workers;   <span class="cm">// nb_workers must be power-of-2</span>
}
<span class="cf">rte_eth_dev_rss_reta_update</span>(port_id, reta_conf, reta_size);</div>

</div><!-- /t-rss -->

<!-- TAB: Interview Q&A -->
<div id="t-qa" class="tab-pane">

<div class="p-slate">
<h4>Q: What is the DD bit and why does DPDK use it instead of interrupts?</h4>
The DD (Descriptor Done) bit is a status bit set by NIC hardware in a descriptor after it finishes with it — for Rx: after DMA'ing the packet; for Tx: after sending it. The PMD polls this bit in a tight loop instead of sleeping and waiting for an interrupt. At 100G/64B, ~148 Mpps would require 148M interrupts/sec — impossible. Polling eliminates interrupt latency and context switches entirely.
</div>

<div class="p-slate">
<h4>Q: What happens if rte_eth_tx_burst() returns less than nb_pkts?</h4>
The Tx ring was full — not all packets could be queued. The caller must free the unsent packets (<code>pkts[nb_tx..nb_pkts-1]</code>). Failing to do so causes a mbuf leak → mempool exhaustion → <code>rx_burst</code> can no longer refill Rx ring → <code>rx_nombuf</code> stat increments → application crashes or stops receiving.
</div>

<div class="p-slate">
<h4>Q: When are Tx mbufs actually freed?</h4>
NOT immediately after tx_burst. The NIC needs time to DMA the data. The PMD frees completed Tx mbufs lazily: either when the next tx_burst is called and the PMD reclaims descriptors, or when a configurable <code>tx_free_thresh</code> is crossed. Never access an mbuf after passing it to tx_burst — the mbuf may be freed by the PMD asynchronously.
</div>

<div class="p-slate">
<h4>Q: What is the order of port configuration API calls and why does it matter?</h4>
Order: dev_info_get → dev_configure → rx_queue_setup (each queue) → tx_queue_setup (each queue) → dev_start. This order is mandatory: <code>dev_configure</code> allocates internal resources; <code>queue_setup</code> allocates descriptor rings using those resources; <code>dev_start</code> enables DMA. Calling out of order returns EINVAL or silently fails.
</div>

<div class="p-slate">
<h4>Q: What does stats.imissed mean and how do you fix it?</h4>
<code>imissed</code> counts packets the NIC hardware dropped because the Rx ring had no empty descriptor slots — the application wasn't consuming packets fast enough. Fixes: (1) Increase <code>nb_rx_desc</code>; (2) Increase burst_size to drain more per call; (3) Reduce per-packet processing time; (4) Add more worker lcores.
</div>

<div class="p-slate">
<h4>Q: Why must worker count be a power of 2 for RSS?</h4>
RETA has a fixed size (typically 128 or 512). DPDK maps RETA entries evenly to queues: RETA[i] = i % nb_workers. If nb_workers is not a power of 2, the division is uneven — some queues get more RETA entries (more traffic) than others. Under load, the heavier queues saturate first, creating a throughput bottleneck. Power-of-2 counts guarantee exact even distribution.
</div>

</div><!-- /t-qa -->

<!-- TAB: Lab -->
<div id="t-lab" class="tab-pane">

<div class="lab-box">
<div class="lab-hdr">&#128293; Lab 5: L2 Forwarder with RSS Verification</div>
<div class="lab-body">
<p style="font-size:.87rem;margin:.3rem 0 .8rem">Build the classic DPDK L2 forwarder (MAC swap + forward) and add RSS verification to confirm packets are landing on the expected lcore.</p>

<div class="lab-step"><span class="sn">1</span><div>Configure port with 4 Rx queues (power-of-2) and enable RSS on IP+TCP+UDP</div></div>
<div class="lab-step"><span class="sn">2</span><div>Launch 4 worker lcores — each polls its own queue: <code>rte_eth_rx_burst(port, lcore_id % 4, ...)</code></div></div>
<div class="lab-step"><span class="sn">3</span><div>In the Rx loop: print <code>mbuf->hash.rss</code> and verify it's set (<code>RTE_MBUF_F_RX_RSS_HASH</code> in ol_flags)</div></div>
<div class="lab-step"><span class="sn">4</span><div>MAC swap: swap src ↔ dst Ethernet addresses using <code>rte_ether_addr_copy()</code></div></div>
<div class="lab-step"><span class="sn">5</span><div>Transmit back on the same port/queue: <code>rte_eth_tx_burst(port, queue, pkts, nb_rx)</code></div></div>
<div class="lab-step"><span class="sn">6</span><div>Monitor stats: verify <code>imissed == 0</code> and <code>rx_nombuf == 0</code> under load</div></div>
<div class="lab-step"><span class="sn">7</span><div><strong>Extension:</strong> try 3 workers (non-power-of-2) — observe CPU imbalance in <code>top -H</code></div></div>
</div>
</div>

<p class="sep">MASTERY CHECKLIST</p>
<ul class="cl">
<li>Can explain what the DD bit is and why DPDK polls it instead of using interrupts</li>
<li>Can draw the full Rx descriptor lifecycle (6 steps from setup to application)</li>
<li>Can write the canonical polling loop with correct Tx free pattern</li>
<li>Can list the 10-step port configuration sequence in order and explain why order matters</li>
<li>Can explain imissed vs rx_nombuf and what causes each</li>
<li>Can explain RSS: Toeplitz hash, RETA, why same 5-tuple always lands on same lcore</li>
<li>Can explain why worker count must be power-of-2 for even RSS distribution</li>
<li>Can write RETA update code to manually control traffic distribution</li>
</ul>

</div><!-- /t-lab -->

<div class="mod-nav">
  <a href="{{ '/learning/data-plane/dpdk/module-p1-memory/' | relative_url }}">&#8592; P1B: Hugepages, mempool &amp; mbuf</a>
  <a href="{{ '/learning/data-plane/dpdk/dpdk-roadmap/' | relative_url }}">&#8593; Roadmap</a>
  <a class="nb" href="{{ '/learning/data-plane/dpdk/module-p2-rings/' | relative_url }}">P2B: rte_ring &amp; App Models &#8594;</a>
</div>

<script>
function vt(e,id){
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  e.target.classList.add('active');
}
</script>
