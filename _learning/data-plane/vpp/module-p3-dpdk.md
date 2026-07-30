---
layout: learning
title: "VPP P3A - DPDK Plugin Deep Dive"
permalink: /learning/data-plane/vpp/module-p3-dpdk/
---
<style>
.mod-header{background:linear-gradient(135deg,#0d1b2a 0%,#3a1a08 60%,#c05e1b 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#f0c080;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#f0d0a0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#f8e0c0}
.tab-bar{display:flex;flex-wrap:wrap;background:#0d1b2a;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}.tab-btn.active{color:#f0c080;border-bottom-color:#f0c080}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee)}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700}
.cp-body{padding:1.1rem 1.2rem}
.cp-body p,.cp-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.cp-body ul{margin:.4rem 0;padding-left:1.4rem}
.cp-body li{margin-bottom:.3rem}
.p-blue .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue .cp-hdr{background:#0d2030}
.p-teal .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.tag-blue{background:#d0e8f8;color:#1a4a7c}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-green{background:#c8e8d4;color:#0e4a28}
.tag-purple{background:#e0d4f4;color:#3a1a6c}
.cb{background:#0d1b2a;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #c05e1b}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#f0d4a0;white-space:pre}
.cm{color:#7a5a30}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.dpdk-box{background:#f0ecf8;border:1.5px solid #9b7bd0;border-left:4px solid #5b3a8c;border-radius:8px;padding:1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .dpdk-box{background:#1a1028;border-color:#7060a8;border-left-color:#9b7bd0}
.dpdk-box .dh{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.08em;color:#5b3a8c;margin-bottom:.5rem;text-transform:uppercase}
[data-theme=dark] .dpdk-box .dh{color:#b090e8}
.dpdk-box ul{margin:0;padding-left:1.2rem}
.dpdk-box li{font-size:.87rem;line-height:1.65;color:var(--text-color,#222);margin-bottom:.25rem}
.ins{background:#e8f5f0;border:1.5px solid #1a7a6e;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0a2420;border-color:#2a9a8e}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#0e5248}[data-theme=dark] .ins strong{color:#5dd6c8}
.api-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.86rem}
.api-table th{background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.api-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.api-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.api-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a7a6e}
.proj-box{border:2px solid #c05e1b;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.proj-hdr{background:#c05e1b;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.proj-hdr .pn{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.proj-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.proj-body{padding:1.1rem 1.2rem}
.proj-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.ps{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.ps:last-of-type{border-bottom:none}
.ps .sn{background:#c05e1b;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#1a7a6e;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">VPP MASTERY · PHASE 3A · WEEKS 9–10</div>
  <div class="mod-title">🔌 DPDK Plugin Deep Dive</div>
  <div class="mod-subtitle">dpdk-input · zero-copy mbuf bridge · startup.conf DPDK stanza · Mellanox mlx5 · xstats</div>
  <div class="mod-pills">
    <span class="mod-pill">src/plugins/dpdk/</span>
    <span class="mod-pill">device/node.c</span>
    <span class="mod-pill">init.c</span>
    <span class="mod-pill">dpdk.h</span>
    <span class="mod-pill">Mellanox mlx5</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'ta')">Architecture</button>
  <button class="tab-btn" onclick="vt(event,'tb')">dpdk-input Node</button>
  <button class="tab-btn" onclick="vt(event,'tc')">mbuf ↔ vlib_buffer Bridge</button>
  <button class="tab-btn" onclick="vt(event,'td')">Mellanox mlx5</button>
  <button class="tab-btn" onclick="vt(event,'te')">Configuration</button>
  <button class="tab-btn" onclick="vt(event,'tf')">Projects</button>
  <button class="tab-btn" onclick="vt(event,'tg')">Checklist</button>
</div>

<div id="ta" class="tab-pane active">
<p class="sep">DPDK PLUGIN ARCHITECTURE</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🏗️</span><h3>How the DPDK Plugin Integrates</h3><span class="tag tag-orange">ARCHITECTURE</span></div>
  <div class="cp-body">
    <p>The DPDK plugin (<code>dpdk_plugin.so</code>) bridges DPDK's poll-mode driver (PMD) model and VPP's graph-node model. It is responsible for: initialising DPDK EAL, binding physical ports, polling RX queues, converting mbufs to vlib buffers, and transmitting vlib buffers back through DPDK's TX burst API.</p>
<div class="cb"><pre><span class="cm">/* Plugin source layout: src/plugins/dpdk/ */</span>
dpdk/
├── device/
│   ├── node.c       <span class="cm"># dpdk-input node function - the RX hot path</span>
│   ├── tx_func.c    <span class="cm"># dpdk-output / dpdk-tx - the TX hot path</span>
│   ├── init.c       <span class="cm"># EAL init, port setup, queue allocation</span>
│   └── format.c     <span class="cm"># CLI formatting: show dpdk interface</span>
├── dpdk.h           <span class="cm"># dpdk_main_t, dpdk_device_t - master structs</span>
└── api/
    └── dpdk.api     <span class="cm"># Binary API: set DPDK interface config etc</span>

<span class="cm">/* Key structs */</span>
dpdk_main_t   - singleton: EAL args, device pool, per-worker tx queues
dpdk_device_t - per-port: port_id, n_rx_queues, rx/tx descriptors, stats</pre></div>
    <ul>
      <li>The DPDK plugin calls <code>rte_eal_init()</code> during VPP startup - before any graph nodes run</li>
      <li>One <code>dpdk_device_t</code> exists per physical port; stored in a vec indexed by <code>xd_index</code></li>
      <li>Each RX queue is polled by exactly one worker thread - the assignment is in <code>dpdk_device_t.rx_queues[q].thread_index</code></li>
      <li>TX uses per-worker tx queue buffers to avoid locking: worker N uses tx queue N exclusively</li>
    </ul>
  </div>
</div>
</div>

<div id="tb" class="tab-pane">
<p class="sep">dpdk-input - THE RX HOT PATH</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>dpdk-input Node Internals</h3><span class="tag tag-teal">INTERNALS</span></div>
  <div class="cp-body">
    <p><code>dpdk-input</code> is a <code>VLIB_NODE_TYPE_INPUT</code> node that polls DPDK RX queues. It is the entry point for all physical network traffic in VPP. The key performance insight is that it processes <em>burst of up to DPDK_NB_RX_DESC mbufs</em> per call and converts them all to vlib buffer indices before dispatching to the next graph node.</p>
<div class="cb"><pre><span class="cm">/* Simplified dpdk-input hot path (src/plugins/dpdk/device/node.c) */</span>
VLIB_NODE_FN(dpdk_input_node)(vlib_main_t *vm, vlib_node_runtime_t *node,
                              vlib_frame_t *frame)
{
    dpdk_main_t *dm = &dpdk_main;
    dpdk_per_thread_data_t *ptd = vec_elt_at_index(dm->per_thread_data,
                                                    vm->thread_index);
    <span class="ck">u32</span> n_rx_packets = 0;

    <span class="cm">/* Poll each queue assigned to this worker */</span>
    dpdk_device_and_queue_t *dq;
    vec_foreach(dq, dm->devices_by_cpu[vm->thread_index]) {
        dpdk_device_t *xd = vec_elt_at_index(dm->devices, dq->device_index);

        <span class="cm">/* DPDK burst receive - fills ptd->mbufs[] */</span>
        <span class="ck">u32</span> n_rx = rte_eth_rx_burst(xd->port_id, dq->queue_id,
                                   ptd->mbufs, DPDK_RX_BURST_SZ);
        <span class="ck">if</span> (n_rx == 0) continue;

        <span class="cm">/* Convert mbufs to vlib buffer indices + dispatch to ethernet-input */</span>
        n_rx_packets += dpdk_process_rx_burst(vm, node, xd, dq->queue_id,
                                             ptd, n_rx);
    }
    return n_rx_packets;
}

<span class="cm">/* What dpdk_process_rx_burst does: */</span>
<span class="cm">/* 1. For each mbuf: derive vlib_buffer_t pointer (they share memory) */</span>
<span class="cm">/* 2. Set vlib_buffer fields: current_data, current_length, sw_if_index */</span>
<span class="cm">/* 3. Copy DPDK offload flags to vlib_buffer flags (RSS hash, checksum) */</span>
<span class="cm">/* 4. Enqueue u32 buffer indices to ethernet-input frame */</span></pre></div>
    <div class="ins">
      <p>💡 <strong>Key performance detail:</strong> <code>dpdk-input</code> does NOT call <code>vlib_buffer_alloc()</code>. Instead, vlib buffers and DPDK mbufs share the same memory pool - the vlib buffer header IS the mbuf's private data area. This zero-copy design means RX never allocates memory; the conversion from mbuf to vlib_buffer is a pointer offset calculation.</p>
    </div>
  </div>
</div>
</div>

<div id="tc" class="tab-pane">
<p class="sep">MBUF ↔ VLIB_BUFFER MEMORY BRIDGE</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Shared Memory Layout</h3><span class="tag tag-blue">ZERO-COPY</span></div>
  <div class="cp-body">
    <p>The DPDK plugin pre-allocates a single <code>rte_mempool</code> with a custom private data size large enough to hold a <code>vlib_buffer_t</code>. Each <code>rte_mbuf</code> in this pool has its <code>rte_mbuf_priv_data</code> area occupied by the <code>vlib_buffer_t</code> header. They overlap in memory.</p>
<div class="cb"><pre><span class="cm">/* Memory layout of a DPDK+VPP buffer */</span>

+──────────────────────────────────────────────────────────────────+
|  rte_mbuf (128 bytes)  |  vlib_buffer_t (128 bytes)  |  data[]  |
|  (DPDK header)         |  (VPP header = mbuf priv)   |          |
+──────────────────────────────────────────────────────────────────+
                         ↑                              ↑
                   vlib_buffer ptr               packet data

<span class="cm">/* Converting between the two */</span>
<span class="cm">/* mbuf → vlib_buffer */</span>
vlib_buffer_t *b = vlib_buffer_from_rte_mbuf(mb);
<span class="cm">/* equivalent to: (vlib_buffer_t *)RTE_PTR_ADD(mb, sizeof(struct rte_mbuf)) */</span>

<span class="cm">/* vlib_buffer → mbuf */</span>
struct rte_mbuf *mb = rte_mbuf_from_vlib_buffer(b);
<span class="cm">/* equivalent to: (struct rte_mbuf *)RTE_PTR_SUB(b, sizeof(struct rte_mbuf)) */</span>

<span class="cm">/* Fields are synced at RX entry and TX exit */</span>
<span class="cm">/* RX: DPDK fills mbuf, plugin copies to vlib_buffer fields */</span>
b->current_data   = mb->data_off - RTE_PKTMBUF_HEADROOM;
b->current_length = mb->data_len;
b->flags |= (mb->ol_flags & PKT_RX_RSS_HASH) ? VLIB_BUFFER_TOTAL_LENGTH_VALID : 0;
vnet_buffer(b)->sw_if_index[VLIB_RX] = xd->sw_if_index;
vnet_buffer(b)->sw_if_index[VLIB_TX] = ~0;  <span class="cm">/* unknown at RX */</span>

<span class="cm">/* TX: vlib_buffer → mbuf */</span>
mb->data_off = b->current_data + RTE_PKTMBUF_HEADROOM;
mb->data_len = b->current_length;
mb->pkt_len  = b->current_length;</pre></div>
    <div class="dpdk-box">
      <div class="dh">⚙️ DPDK KNOWLEDGE APPLIED</div>
      <ul>
        <li>You know <code>rte_mempool</code> with custom private size - VPP uses exactly this to embed vlib_buffer_t in each mbuf's private data region</li>
        <li>You know <code>rte_mbuf.data_off</code> is the offset from the mbuf start to packet data - VPP's <code>current_data</code> is the equivalent from the vlib_buffer start</li>
        <li>RSS hash in <code>mb->hash.rss</code> is copied to <code>b->flow_id</code> - used for per-flow worker assignment in some configurations</li>
        <li>DPDK scatter-gather (multi-segment mbufs) maps to VPP chained buffers via <code>b->next_buffer</code> - the DPDK plugin chains them during RX conversion</li>
      </ul>
    </div>
  </div>
</div>
</div>

<div id="td" class="tab-pane">
<p class="sep">MELLANOX mlx5 - YOUR NIC</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔬</span><h3>mlx5 PMD Specifics for VPP</h3><span class="tag tag-purple">MELLANOX</span></div>
  <div class="cp-body">
    <p>Mellanox ConnectX-4/5/6 (mlx5 PMD) in VPP behaves differently from Intel NICs. Understanding the mlx5-specific behaviour prevents the most common VPP + Mellanox configuration issues.</p>
    <table class="api-table">
      <thead><tr><th>Topic</th><th>mlx5 Behaviour</th><th>Action Required</th></tr></thead>
      <tbody>
        <tr><td>Driver binding</td><td>mlx5 does NOT use vfio-pci as primary. Uses kernel mlx5_core + mlx5_ib alongside DPDK</td><td>Do NOT unbind from mlx5_core. DPDK mlx5 PMD works on top of it via rdma</td></tr>
        <tr><td>IOVA mode</td><td>Requires Virtual Address (VA) IOVA mode</td><td>Set <code>iova-mode va</code> in startup.conf dpdk stanza</td></tr>
        <tr><td>Hugepages</td><td>mlx5 uses DMA mapping - works with 2MB and 1GB pages</td><td>Both work; 1GB pages give fewer TLB misses at high load</td></tr>
        <tr><td>Multi-queue RSS</td><td>Full RSS support: Toeplitz hash on IPv4/IPv6/TCP/UDP</td><td>Set num-rx-queues = num worker threads for full parallelism</td></tr>
        <tr><td>Checksum offload</td><td>Full IPv4/TCP/UDP TX and RX checksum offload</td><td>Enable in dpdk stanza: <code>enable-tcp-udp-checksum</code></td></tr>
        <tr><td>TSO (TCP Segmentation)</td><td>Supported on ConnectX-5 and later</td><td>Enable per-port in startup.conf if using TCP session layer</td></tr>
        <tr><td>Multi-seg mbufs</td><td>mlx5 handles scatter-gather natively</td><td>Enable <code>multi-seg</code> in dpdk stanza for jumbo frames</td></tr>
        <tr><td>VF / SR-IOV</td><td>Create VFs on the PF, each VF gets its own PMD instance</td><td>One VF per container - standard SR-IOV workflow you know from DPDK</td></tr>
      </tbody>
    </table>
<div class="cb"><pre><span class="cm"># Correct startup.conf for Mellanox ConnectX-5 with VPP</span>
dpdk {
  dev 0000:03:00.0 {
    name eth0                       <span class="cm"># human-readable name in VPP</span>
    num-rx-queues 4                 <span class="cm"># = number of worker threads</span>
    num-tx-queues 4
    num-rx-desc 2048
    num-tx-desc 2048
    rss-fn 0x3c8                    <span class="cm"># RSS on IPv4+IPv6+TCP+UDP</span>
    enable-tcp-udp-checksum         <span class="cm"># TX checksum offload</span>
  }
  uio-driver none                   <span class="cm"># mlx5: no vfio-pci binding needed</span>
  iova-mode va                      <span class="cm"># REQUIRED for mlx5</span>
  socket-mem 2048,0                 <span class="cm"># 2GB on NUMA 0, 0 on NUMA 1</span>
  log-level notice
}

<span class="cm"># Verify mlx5 detection</span>
<span class="cm"># vppctl: show dpdk interface</span>
<span class="cm"># Should show: driver mlx5_pmd, link state up</span></pre></div>
  </div>
</div>
</div>

<div id="te" class="tab-pane">
<p class="sep">DPDK STANZA REFERENCE</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">⚙️</span><h3>Complete startup.conf DPDK Options</h3><span class="tag tag-teal">CONFIGURATION</span></div>
  <div class="cp-body">
    <table class="api-table">
      <thead><tr><th>Option</th><th>Scope</th><th>Description</th><th>Recommended for AMD+mlx5</th></tr></thead>
      <tbody>
        <tr><td><code>dev &lt;PCI&gt; { ... }</code></td><td>Per-port</td><td>Configure a specific DPDK device by PCI address</td><td>Required for each Mellanox port</td></tr>
        <tr><td><code>num-rx-queues N</code></td><td>Per-port</td><td>Number of RX queues. Must ≤ number of worker threads</td><td>Set equal to workers</td></tr>
        <tr><td><code>num-tx-queues N</code></td><td>Per-port</td><td>Number of TX queues. One per worker</td><td>Set equal to workers</td></tr>
        <tr><td><code>num-rx-desc N</code></td><td>Per-port</td><td>RX ring size. Power of 2. 1024–4096</td><td>2048 for high-throughput</td></tr>
        <tr><td><code>num-tx-desc N</code></td><td>Per-port</td><td>TX ring size. Power of 2</td><td>2048</td></tr>
        <tr><td><code>uio-driver vfio-pci</code></td><td>Global</td><td>Use vfio-pci for Intel/virtio. For mlx5: use <code>none</code></td><td><code>uio-driver none</code></td></tr>
        <tr><td><code>iova-mode va</code></td><td>Global</td><td>Virtual address IOVA mode. Required for mlx5</td><td>Always set for mlx5</td></tr>
        <tr><td><code>socket-mem N,N</code></td><td>Global</td><td>Hugepage memory per NUMA socket in MB</td><td>Match to your topology</td></tr>
        <tr><td><code>no-multi-seg</code></td><td>Global</td><td>Disable multi-segment mbufs (faster for small packets)</td><td>Set unless using jumbo frames</td></tr>
        <tr><td><code>enable-tcp-udp-checksum</code></td><td>Per-port</td><td>Enable HW TX checksum offload for TCP/UDP</td><td>Enable on mlx5 ConnectX-5+</td></tr>
        <tr><td><code>log-level &lt;level&gt;</code></td><td>Global</td><td>DPDK log verbosity: debug/info/notice/warning/error</td><td><code>notice</code> in production</td></tr>
        <tr><td><code>dev default { ... }</code></td><td>Global</td><td>Default settings applied to all DPDK devices</td><td>Use to avoid repeating per-port config</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>

<div id="tf" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr"><span class="pn">PROJECT 4</span><h4>Interface Technology Comparison Lab</h4></div>
  <div class="proj-body">
    <p><strong>Objective:</strong> Quantitatively compare DPDK, memif, and TAP throughput using identical test traffic. Understand the performance cost of each interface type.</p>
    <div class="ps"><div class="sn">1</div><div>Set up three VPP containers: Container A (testpmd sending 64B frames), Container B (VPP with all three interface types), Container C (testpmd receiving). Create: one DPDK-to-DPDK path, one memif path, one TAP path between the same endpoints.</div></div>
    <div class="ps"><div class="sn">2</div><div>Use testpmd's <code>txonly</code> mode to send at line rate (10 Gbps) on each path. Record: throughput (Mpps), latency (p50/p99 from dpdk-testpmd <code>rxonly</code> with timestamps), and CPU usage per worker thread.</div></div>
    <div class="ps"><div class="sn">3</div><div>Examine <code>show run</code> on each VPP instance. Compare vectors/call and clocks/vector for dpdk-input vs memif-input vs af-packet-input. Build a table of results.</div></div>
    <div class="ps"><div class="sn">4</div><div>Check <code>show dpdk interface xstats GigabitEthernet0/8/0</code> for hardware-level counters: rx_missed_errors, rx_no_mbuf_errors, tx_errors. These indicate buffer exhaustion or descriptor ring underflow.</div></div>
    <div class="ps"><div class="sn">5</div><div>Identify the bottleneck in each path using the data collected. Write a 1-page analysis: when would you choose each interface type in a production deployment?</div></div>
  </div>
</div>
</div>

<div id="tg" class="tab-pane">
<p class="sep">P3A COMPLETION CHECKLIST</p>
<ul class="cl">
  <li>Know dpdk_plugin.so source layout: node.c (RX), tx_func.c (TX), init.c (setup), dpdk.h</li>
  <li>Understand dpdk-input's poll loop: rte_eth_rx_burst → convert → enqueue to ethernet-input</li>
  <li>Can explain the mbuf/vlib_buffer shared memory layout and the zero-copy design</li>
  <li>Know the offset conversion macros: vlib_buffer_from_rte_mbuf / rte_mbuf_from_vlib_buffer</li>
  <li>Know which mbuf fields are synced to vlib_buffer fields at RX (data_off, data_len, ol_flags)</li>
  <li>Understand mlx5 PMD specifics: no vfio-pci unbind, iova-mode va required, RSS configuration</li>
  <li>Can write a complete dpdk stanza for Mellanox ConnectX-5 with multi-queue, checksum offload</li>
  <li>Know the key dpdk stanza options and their effects (num-rx-queues, socket-mem, no-multi-seg)</li>
  <li>Can interpret show dpdk interface xstats: know what rx_missed_errors and rx_no_mbuf_errors mean</li>
  <li>Completed Project 4: interface technology comparison with quantitative results</li>
</ul>
<div class="ins" style="margin-top:1.2rem;">
  <p>✅ Next: <strong>P3B - memif and shared-memory interfaces</strong>. This is where VPP shines for container-to-container connectivity.</p>
</div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/data-plane/vpp/module-p2-vnet/' | relative_url }}">← vnet</a>
  <a href="{{ '/learning/data-plane/vpp/vpp-roadmap/' | relative_url }}">🗺️ Roadmap</a>
  <a class="nb" href="{{ '/learning/data-plane/vpp/module-p3-memif/' | relative_url }}">Next: memif →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active');}
</script>
