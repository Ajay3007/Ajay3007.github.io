---
title: "DPDK P3 — Multi-Process, rte_flow & NUMA"
description: "DPDK MASTERY · PHASE 3 OF 3 · MODULE A Multi-Process, rte flow NUMA Primary/secondary model · shared resources · hardware flow classification · NUMA-aware allocation Ch 13 —…"
domain: data-plane
track: dpdk
order: 3
ownHeader: true
url: /learning/data-plane/dpdk/module-p3-advanced/
---

<style>
.mod-header{background:linear-gradient(135deg,#1a0800 0%,#3a1200 60%,#6a2800 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#f0a060;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#f0c8a0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#fce0c0}
.tab-bar{display:flex;flex-wrap:wrap;gap:0;background:#3a1200;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#f0a060;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#ffcc80;border-bottom-color:#ffcc80}
.tab-pane{display:none}
.tab-pane.active{display:block}
.p-orange{background:#fdf0e8;border-left:4px solid #c05e1b;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-blue{background:#eaf2fc;border-left:4px solid #2e6da4;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-teal{background:#e8f6f4;border-left:4px solid #1a7a6e;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-slate{background:#f4f6f8;border-left:4px solid #64748b;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-violet{background:#f3f0fc;border-left:4px solid #7c3aed;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
[data-theme=dark] .p-orange{background:#1e0d00;border-color:#e07830}
[data-theme=dark] .p-blue{background:#0d1e34;border-color:#4a90d9}
[data-theme=dark] .p-teal{background:#0d2020;border-color:#2a9a8e}
[data-theme=dark] .p-slate{background:#1a1e24;border-color:#8898aa}
[data-theme=dark] .p-violet{background:#180d30;border-color:#9d6bf0}
.p-orange h4,.p-blue h4,.p-teal h4,.p-slate h4,.p-violet h4{margin:0 0 .5rem;font-size:.9rem;font-weight:700}
.ins{background:#e8f5e9;border:1px solid #66bb6a;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.warn{background:#fff8e1;border:1px solid #ffca28;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.note{background:#e3f2fd;border:1px solid #42a5f5;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
[data-theme=dark] .ins{background:#0d2010;border-color:#388e3c}
[data-theme=dark] .warn{background:#1e1800;border-color:#f9a825}
[data-theme=dark] .note{background:#0d1e2e;border-color:#1976d2}
.cb{background:#0d1117;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;font-family:monospace;font-size:.82rem;line-height:1.7;color:#e6edf3;white-space:pre-wrap}
.cb .cm{color:#8b949e}.cb .ck{color:#ff7b72}.cb .cv{color:#79c0ff}.cb .cs{color:#a5d6ff}.cb .cn{color:#f2cc60}.cb .cf{color:#d2a8ff}.cb .co{color:#ffa657}.cb .cg{color:#3fb950}
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.8rem 0}
.t-table th{background:#3a1200;color:#f0a060;font-family:monospace;font-size:.75rem;font-weight:700;padding:.5rem .7rem;text-align:left;border-bottom:2px solid #6a2800}
.t-table td{padding:.45rem .7rem;border-bottom:1px solid var(--border-color,#e8e8e8);vertical-align:top}
.t-table tr:last-child td{border-bottom:none}
.t-table tr:hover td{background:var(--bg-color,#f8f9fa)}
.diagram-box{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;font-family:monospace;font-size:.78rem;line-height:1.8;color:#c9d1d9;overflow-x:auto;white-space:pre}
.lab-box{background:var(--card-bg,#fff);border:2px solid #c05e1b;border-radius:10px;overflow:hidden;margin:1rem 0}
.lab-hdr{background:#3a1200;color:#fff;padding:.7rem 1.2rem;font-weight:700;font-family:monospace;font-size:.9rem}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.5rem;font-size:.87rem}
.sn{background:#c05e1b;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:800;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{padding:.3rem 0;font-size:.87rem;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐ ";font-size:1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#3a1200;color:#fff !important;border-color:#3a1200}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">DPDK MASTERY · PHASE 3 OF 3 · MODULE A</div>
  <div class="mod-title">Multi-Process, rte_flow &amp; NUMA</div>
  <div class="mod-subtitle">Primary/secondary model · shared resources · hardware flow classification · NUMA-aware allocation</div>
  <div class="mod-pills">
    <span class="mod-pill">Ch 13 — Multi-Process</span>
    <span class="mod-pill">Ch 14 — rte_flow</span>
    <span class="mod-pill">Ch 15 — Multi-Core &amp; NUMA</span>
    <span class="mod-pill">C · VFIO · FDIR · Cache-Line</span>
    <span class="mod-pill">Weeks 11–13</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t-mp')">Multi-Process</button>
  <button class="tab-btn" onclick="vt(event,'t-shared')">Shared Resources</button>
  <button class="tab-btn" onclick="vt(event,'t-flow')">rte_flow API</button>
  <button class="tab-btn" onclick="vt(event,'t-flowex')">Flow Examples</button>
  <button class="tab-btn" onclick="vt(event,'t-numa')">NUMA &amp; Cache</button>
  <button class="tab-btn" onclick="vt(event,'t-qa')">Interview Q&amp;A</button>
  <button class="tab-btn" onclick="vt(event,'t-lab')">Lab</button>
</div>
<!-- TAB: Multi-Process -->
<div id="t-mp" class="tab-pane active">
<div class="p-orange">
<h4>Primary / Secondary Process Model</h4>
DPDK supports multiple OS processes sharing the same NIC and hugepage memory. The <strong>primary</strong> process owns all resources; <strong>secondary</strong> processes attach and use them. This enables hot-restartable components, traffic class isolation, and separation of control and data planes.
</div>
<div class="diagram-box">Multi-Process Architecture

Primary Process                      Secondary Processes
┌──────────────────────┐             ┌─────────────────────┐
│ rte_eal_init()       │             │ rte_eal_init()       │
│ (creates resources)  │             │ --proc-type=secondary│
│                      │  hugepage   │ (attaches)           │
│ hugepage memory      │◄──shared───►│ hugepage memory      │
│ rte_mempool (named)  │             │ rte_mempool_lookup() │
│ rte_ring (named)     │             │ rte_ring_lookup()    │
│ NIC: dev_configure   │             │ NIC: rx_burst only   │
│ NIC: dev_start       │             │ (cannot reconfigure) │
│                      │             └─────────────────────┘
│ Queues 0-3 →         │             Secondary-Enterprise
│ Queues 4-7 →         │             ┌─────────────────────┐
└──────────────────────┘             │ Secondary-Mobility   │
                                     └─────────────────────┘
Jio SASE-DP production pattern: primary owns both 100G ports.
Enterprise secondary handles queues 0-3 (URL filter).
Mobility secondary handles queues 4-7 (5G/SCEF policy).</div>
<p class="sep">EAL ARGUMENTS FOR MULTI-PROCESS</p>
<div class="cb"><span class="cm"># Primary process — creates all shared resources</span>
./my_primary -l 0-3 -n 4 --proc-type=primary --file-prefix=sase \
             -a 0000:03:00.0 -- [app args]

<span class="cm"># Secondary process — attaches to primary's shared memory</span>
./my_secondary -l 4-7 -n 4 --proc-type=secondary --file-prefix=sase \
               -- [app args]

<span class="cm"># auto: becomes primary if none exists, secondary otherwise</span>
./my_app -l 0-3 -n 4 --proc-type=auto --file-prefix=sase</div>
<div class="warn">&#9888;&#65039; <strong>Rules:</strong> Secondary does NOT need <code>-a</code> (device allowlist) — it inherits device info from primary. Secondary CAN specify <code>-l</code> (lcores) — must NOT overlap with primary's lcores. Both must use the same <code>--file-prefix</code> to share the same <code>/dev/shm/</code> files.</div>
</div><!-- /t-mp -->
<!-- TAB: Shared Resources -->
<div id="t-shared" class="tab-pane">
<table class="t-table">
<thead><tr><th>Resource</th><th>Shared?</th><th>Access from Secondary</th></tr></thead>
<tbody>
<tr><td>Hugepage memory segments</td><td>YES — read/write</td><td>All processes map same physical hugepages</td></tr>
<tr><td><code>rte_mempool</code> (named)</td><td>YES — shared pool</td><td><code>rte_mempool_lookup("MBUF_POOL")</code></td></tr>
<tr><td><code>rte_ring</code> (named)</td><td>YES — shared ring</td><td><code>rte_ring_lookup("WORK_RING")</code></td></tr>
<tr><td><code>rte_hash</code> / <code>rte_lpm</code> / <code>rte_acl</code></td><td>YES — if in named memzone</td><td><code>rte_memzone_lookup("FLOW_TABLE")</code></td></tr>
<tr><td>NIC port state</td><td>YES — read-only for secondary</td><td>Can rx_burst/tx_burst but NOT reconfigure</td></tr>
<tr><td>Per-process heap (<code>rte_malloc</code>)</td><td>NO — per-process</td><td>Each process has own heap allocation</td></tr>
<tr><td>lcores / thread pool</td><td>NO — per-process</td><td>Each process runs its own lcore threads</td></tr>
</tbody>
</table>
<div class="cb"><span class="cm">// Secondary process — find shared pool created by primary</span>
<span class="ck">struct</span> rte_mempool *pool = <span class="cf">rte_mempool_lookup</span>(<span class="cs">"MBUF_POOL"</span>);
<span class="ck">if</span> (!pool)
    <span class="cf">rte_exit</span>(<span class="cn">EXIT_FAILURE</span>, <span class="cs">"Cannot find mempool — is primary running?\n"</span>);

<span class="ck">struct</span> rte_ring *ring = <span class="cf">rte_ring_lookup</span>(<span class="cs">"WORK_RING"</span>);
<span class="ck">if</span> (!ring)
    <span class="cf">rte_exit</span>(<span class="cn">EXIT_FAILURE</span>, <span class="cs">"Cannot find ring\n"</span>);

<span class="cm">// Find a custom data structure placed in a named memzone by primary</span>
<span class="ck">const</span> <span class="ck">struct</span> rte_memzone *mz = <span class="cf">rte_memzone_lookup</span>(<span class="cs">"FLOW_TABLE"</span>);
<span class="ck">struct</span> my_flow_table *ftbl = (<span class="ck">struct</span> my_flow_table *)mz-&gt;addr;

<span class="cm">// Receive packets using NIC queue assigned to this secondary</span>
<span class="ck">struct</span> rte_mbuf *pkts[<span class="cn">32</span>];
<span class="co">uint16_t</span> nb = <span class="cf">rte_eth_rx_burst</span>(port_id, my_queue_id, pkts, <span class="cn">32</span>);</div>
<div class="p-orange">
<h4>Limitations and Gotchas</h4>
<ul style="margin:.3rem 0 0;font-size:.87rem;line-height:1.8">
<li>Secondary cannot call <code>rte_eth_dev_configure()</code> or <code>rte_eth_dev_start()</code> — NIC already owned by primary</li>
<li>All processes must use the same <code>--socket-mem</code> — mismatch causes attach failure</li>
<li><strong>Pointer sharing:</strong> raw pointers in shared memory are only valid in the process that set them. Use IOVA offsets or named memzones, not raw pointers.</li>
<li>Primary exit kills shared memory — all secondaries lose access to pools and rings immediately → segfault</li>
<li>Cannot mix DPDK versions between primary and secondary — ABI must match exactly</li>
</ul>
</div>
<div class="ins">&#127381; <strong>Common mistake:</strong> Secondary calls <code>rte_pktmbuf_pool_create()</code> instead of <code>rte_mempool_lookup()</code>. This fails with EEXIST (name already taken by primary's pool). Always use <code>_lookup()</code> in secondary processes for resources created by primary.</div>
</div><!-- /t-shared -->
<!-- TAB: rte_flow API -->
<div id="t-flow" class="tab-pane">
<div class="p-orange">
<h4>rte_flow — Hardware Flow Classification</h4>
<code>rte_flow</code> allows applications to program the NIC's hardware to perform packet classification and queue steering <strong>in silicon — with zero CPU involvement for matched flows</strong>. Matched packets bypass RSS entirely and are sent directly to a specific queue. Non-matching packets continue through normal RSS.
</div>
<p class="sep">HOW rte_flow WORKS</p>
<div class="diagram-box">rte_flow Architecture

Application defines flow rule (generic DPDK format)
  ↓
rte_flow_create() — PMD validates rule
  PMD translates to NIC-specific hardware instructions
  ↓
NIC FDIR / Flow Table programmed (in NIC silicon)
  ↓
Packet arrives:
  Matching packets → NIC classifies in hardware → steered to specific Rx queue
  Non-matching packets → go through normal RSS pipeline

Key benefit: matched flows bypass RSS entirely — zero CPU for classification
Use case: steer specific traffic class to dedicated queue/lcore
Example: steer all traffic from enterprise VPN subnet → queue 0 (enterprise secondary)
         steer all 5G/GTP traffic → queue 4 (mobility secondary)</div>
<p class="sep">FLOW RULE STRUCTURE</p>
<div class="p-blue">
<h4>Three Building Blocks</h4>
<ol style="margin:.3rem 0 0;font-size:.87rem;line-height:1.8">
<li><strong>Attributes</strong>: ingress/egress, priority, group number</li>
<li><strong>Pattern (match criteria)</strong>: chain of item types — ETH, IPV4, TCP, UDP, VXLAN, GTP, etc. Each item specifies field values and masks.</li>
<li><strong>Actions (what to do with matched packets)</strong>: QUEUE (steer to specific Rx queue), DROP, COUNT, MARK (tag mbuf), RSS (apply RSS to matched subset), JUMP (goto another group)</li>
</ol>
</div>
<div class="cb"><span class="cm">// Complete rte_flow example: steer all TCP port 443 traffic → queue 0</span>
<span class="ck">struct</span> rte_flow_attr attr = {
    .ingress  = <span class="cn">1</span>,   <span class="cm">// match incoming packets</span>
    .priority = <span class="cn">0</span>,   <span class="cm">// highest priority</span>
};

<span class="cm">// Pattern: ETH / IPV4 / TCP(dport=443) / END</span>
<span class="ck">struct</span> rte_flow_item_tcp tcp_spec = { .hdr.dst_port = <span class="cf">rte_cpu_to_be_16</span>(<span class="cn">443</span>) };
<span class="ck">struct</span> rte_flow_item_tcp tcp_mask = { .hdr.dst_port = <span class="cn">0xFFFF</span> };

<span class="ck">struct</span> rte_flow_item pattern[] = {
    { .type = <span class="cn">RTE_FLOW_ITEM_TYPE_ETH  </span>},
    { .type = <span class="cn">RTE_FLOW_ITEM_TYPE_IPV4 </span>},
    { .type = <span class="cn">RTE_FLOW_ITEM_TYPE_TCP  </span>, .spec = &amp;tcp_spec, .mask = &amp;tcp_mask },
    { .type = <span class="cn">RTE_FLOW_ITEM_TYPE_END  </span>},
};

<span class="cm">// Action: steer to queue 0</span>
<span class="ck">struct</span> rte_flow_action_queue queue_action = { .index = <span class="cn">0</span> };
<span class="ck">struct</span> rte_flow_action actions[] = {
    { .type = <span class="cn">RTE_FLOW_ACTION_TYPE_QUEUE</span>, .conf = &amp;queue_action },
    { .type = <span class="cn">RTE_FLOW_ACTION_TYPE_END  </span>},
};

<span class="cm">// Validate (check NIC supports this rule — no changes to HW)</span>
<span class="ck">struct</span> rte_flow_error err;
<span class="co">int</span> ret = <span class="cf">rte_flow_validate</span>(port_id, &amp;attr, pattern, actions, &amp;err);

<span class="cm">// Create (programs the NIC hardware)</span>
<span class="ck">struct</span> rte_flow *flow = <span class="cf">rte_flow_create</span>(port_id, &amp;attr, pattern, actions, &amp;err);
<span class="ck">if</span> (!flow)
    <span class="cf">rte_exit</span>(<span class="cn">EXIT_FAILURE</span>, <span class="cs">"Flow create failed: %s\n"</span>, err.message);

<span class="cm">// Destroy when no longer needed</span>
<span class="cf">rte_flow_destroy</span>(port_id, flow, &amp;err);</div>
</div><!-- /t-flow -->
<!-- TAB: Flow Examples -->
<div id="t-flowex" class="tab-pane active">
<p class="sep">COMMON FLOW RULE PATTERNS</p>
<table class="t-table">
<thead><tr><th>Use Case</th><th>Pattern Items</th><th>Action</th></tr></thead>
<tbody>
<tr><td>Drop all traffic from IP</td><td>ETH / IPV4(src=1.2.3.4/32)</td><td>DROP</td></tr>
<tr><td>Steer VoIP (UDP 5060) to dedicated queue</td><td>ETH / IPV4 / UDP(dport=5060)</td><td>QUEUE(index=2)</td></tr>
<tr><td>Count ARP packets</td><td>ETH(type=0x0806)</td><td>COUNT + QUEUE(index=0)</td></tr>
<tr><td>VXLAN tunnel traffic to specific queue</td><td>ETH / IPV4 / UDP(4789) / VXLAN(vni=100)</td><td>QUEUE(index=3)</td></tr>
<tr><td>GTP-U (5G traffic) to mobility queue</td><td>ETH / IPV4 / UDP(2152) / GTP(teid=X)</td><td>QUEUE(index=4)</td></tr>
<tr><td>Mark HTTPS packets (apply DPI only to marked)</td><td>ETH / IPV4 / TCP(dport=443)</td><td>MARK(id=1) + RSS</td></tr>
</tbody>
</table>
<div class="p-teal">
<h4>rte_flow Groups and Priority</h4>
<ul style="margin:.3rem 0 0;font-size:.87rem;line-height:1.8">
<li><strong>Priority</strong>: lower number = higher priority. If two rules match the same packet, the higher priority (lower number) wins.</li>
<li><strong>Group</strong>: rules in group 0 are evaluated first. A JUMP action sends matching packets to another group for further classification — enabling multi-level classification trees.</li>
<li>Always call <code>rte_flow_validate()</code> before <code>rte_flow_create()</code> — different NICs support different item/action combinations. Validation catches unsupported combos before touching hardware.</li>
</ul>
</div>
<div class="warn">&#9888;&#65039; <strong>NIC capability check:</strong> Not all NICs support all flow item/action combinations. Intel i40e supports 5-tuple exact match (FDIR). mlx5 supports a much richer flow API including VXLAN, GTP inner headers. Always call <code>rte_flow_validate()</code> first — it returns an error with a descriptive message if the NIC cannot implement the rule.</div>
</div><!-- /t-flowex -->
<!-- TAB: NUMA & Cache -->
<div id="t-numa" class="tab-pane">
<div class="p-orange">
<h4>NUMA — Non-Uniform Memory Access</h4>
In multi-socket servers, each CPU socket has local RAM. Accessing memory on the <em>same</em> socket (local) takes ~60 ns; accessing the <em>other</em> socket (remote) takes ~120 ns — 2× slower. DPDK makes NUMA awareness explicit throughout: every allocation API takes a <code>socket_id</code> parameter.
</div>
<p class="sep">NUMA ALLOCATION RULES</p>
<table class="t-table">
<thead><tr><th>Resource</th><th>Correct Socket</th><th>Why</th></tr></thead>
<tbody>
<tr><td>mbuf pool</td><td><code>rte_eth_dev_socket_id(port)</code></td><td>NIC DMA writes to local socket RAM — remote access doubles latency</td></tr>
<tr><td>rte_ring</td><td><code>rte_socket_id()</code> of the producer/consumer lcore</td><td>Ring data read/written by lcores on that socket</td></tr>
<tr><td>rte_hash / rte_lpm</td><td><code>rte_socket_id()</code> of the lookup lcore</td><td>Hash table entries accessed at line rate — remote access unacceptable</td></tr>
<tr><td>Rx/Tx queues</td><td><code>rte_eth_dev_socket_id(port)</code></td><td>Queue descriptors DMA'd between NIC and RAM — must be local</td></tr>
</tbody>
</table>
<div class="cb"><span class="cm">// NUMA-correct mempool creation</span>
<span class="co">int</span> nic_socket = <span class="cf">rte_eth_dev_socket_id</span>(port_id);
<span class="ck">struct</span> rte_mempool *pool = <span class="cf">rte_pktmbuf_pool_create</span>(
    <span class="cs">"MBUF_POOL"</span>, N_MBUFS, CACHE_SZ, <span class="cn">0</span>, <span class="cn">RTE_MBUF_DEFAULT_BUF_SIZE</span>,
    nic_socket   <span class="cm">// MUST match NIC's socket</span>
);

<span class="cm">// Check lcore-to-socket alignment</span>
<span class="co">unsigned</span> lcore_id;
<span class="cf">RTE_LCORE_FOREACH_WORKER</span>(lcore_id) {
    <span class="co">unsigned</span> lcore_socket = <span class="cf">rte_lcore_to_socket_id</span>(lcore_id);
    <span class="ck">if</span> (lcore_socket != nic_socket)
        <span class="cf">printf</span>(<span class="cs">"WARNING: lcore %u on socket %u, NIC on socket %u — cross-NUMA!\n"</span>,
               lcore_id, lcore_socket, nic_socket);
}</div>
<p class="sep">CACHE-LINE ALIGNMENT & FALSE SHARING</p>
<div class="p-teal">
<h4>False Sharing — The Hidden Serializer</h4>
When two different variables on the <strong>same cache line (64 bytes)</strong> are written by different cores, every write invalidates the other core's cached copy — causing cache coherency traffic even though the cores access different variables. This can reduce throughput by 10–100×.
</div>
<div class="cb"><span class="cm">// WRONG — counter and flag on same cache line → false sharing</span>
<span class="ck">struct</span> per_core_data {
    <span class="co">uint64_t</span> rx_count;    <span class="cm">// 8 bytes</span>
    <span class="co">uint64_t</span> tx_count;    <span class="cm">// 8 bytes</span>
    <span class="co">int</span>      running;     <span class="cm">// 4 bytes — on same 64-byte line!</span>
} cores[RTE_MAX_LCORE];   <span class="cm">// core 0 and core 1 share a cache line</span>
<span class="cm">// CORRECT — pad each entry to a full cache line</span>
<span class="ck">struct</span> per_core_data {
    <span class="co">uint64_t</span> rx_count;
    <span class="co">uint64_t</span> tx_count;
    <span class="co">int</span>      running;
    <span class="co">uint8_t</span>  _pad[<span class="cn">64</span> - <span class="ck">sizeof</span>(<span class="co">uint64_t</span>)*<span class="cn">2</span> - <span class="ck">sizeof</span>(<span class="co">int</span>)];  <span class="cm">// pad to 64 bytes</span>
} __rte_cache_aligned cores[RTE_MAX_LCORE];  <span class="cm">// each core gets its own cache line</span></div>
<div class="note">&#128204; <strong>__rte_cache_aligned</strong> is a DPDK macro that expands to <code>__attribute__((aligned(RTE_CACHE_LINE_SIZE)))</code>. Always use it for per-lcore data structures to prevent false sharing.</div>
</div><!-- /t-numa -->
<!-- TAB: Interview Q&A -->
<div id="t-qa" class="tab-pane">
<div class="p-slate">
<h4>Q: What is the difference between primary and secondary DPDK processes?</h4>
Primary creates and owns all shared resources: hugepage memory, named mempools, rings, and NIC configuration. Secondary attaches to existing primary memory via <code>--proc-type=secondary</code> and <code>--file-prefix</code> matching, finds named objects via lookup APIs, and can use NIC queues but cannot reconfigure the NIC. Primary must be started first.
</div>
<div class="p-slate">
<h4>Q: What happens to secondary processes if the primary exits?</h4>
The shared hugepage memory is unmapped by the OS when the primary exits. Secondary processes lose access to all shared mempools, rings, and hash tables. Any access to those objects causes segfault. Production systems should monitor primary health and gracefully shut down secondaries before primary exits.
</div>
<div class="p-slate">
<h4>Q: Why must --file-prefix match between primary and secondary?</h4>
DPDK uses the file prefix to name shared memory files in <code>/dev/shm/</code> (e.g., <code>/dev/shm/sase_config</code>). Primary creates these files; secondary maps them. If prefixes differ, secondary maps a different (empty) shared memory file — it finds no mempools or rings and fails to start.
</div>
<div class="p-slate">
<h4>Q: What is rte_flow and how does it differ from RSS?</h4>
RSS distributes packets across queues by hashing the 5-tuple — the NIC computes a hash and uses a lookup table (RETA) to pick the queue. rte_flow programs the NIC to match specific packet fields (exact values + masks) and steer matching packets directly to a specific queue — bypassing RSS entirely. rte_flow is more precise (5-tuple, VLAN, VXLAN VNI, GTP TEID…) but consumes NIC hardware resources (FDIR table entries). RSS is always-on and handles all traffic; rte_flow handles specific classified flows.
</div>
<div class="p-slate">
<h4>Q: What is false sharing and how does DPDK prevent it?</h4>
False sharing occurs when two cores write to different variables that happen to reside on the same 64-byte cache line. Each write forces the cache line to be transferred between cores via the coherency protocol — causing serialization even though the cores are touching different data. DPDK prevents this by padding per-lcore data structures to 64 bytes using <code>__rte_cache_aligned</code>, ensuring each core's data occupies its own cache line.
</div>
<div class="p-slate">
<h4>Q: Why must mempool be allocated on the NIC's NUMA socket?</h4>
NIC DMA writes packet data into mbuf buffers. If those buffers are on the remote NUMA socket, every DMA write crosses the QPI/UPI interconnect — ~120 ns instead of ~60 ns. At 100G/64B (148 Mpps), the interconnect bandwidth becomes the bottleneck. NUMA-local allocation keeps DMA writes on the same socket as the NIC → no interconnect crossing → maximum throughput.
</div>
</div><!-- /t-qa -->
<!-- TAB: Lab -->
<div id="t-lab" class="tab-pane">
<div class="lab-box">
<div class="lab-hdr">&#128293; Lab 8: Multi-Process SASE-DP Skeleton</div>
<div class="lab-body">
<p style="font-size:.87rem;margin:.3rem 0 .8rem">Build a minimal primary/secondary DPDK application that mirrors the Jio SASE-DP architecture: primary owns the NIC, enterprise secondary handles traffic on queues 0-1.</p>
<div class="lab-step"><span class="sn">1</span><div><strong>Primary:</strong> <code>rte_eal_init()</code> with <code>--proc-type=primary --file-prefix=sase</code>. Configure NIC with 4 queues. Create named mempool <code>"MBUF_POOL"</code> and ring <code>"RX_TO_ENTERPRISE"</code>.</div></div>
<div class="lab-step"><span class="sn">2</span><div><strong>Primary RX loop:</strong> rx_burst on queues 0-1 → enqueue to <code>"RX_TO_ENTERPRISE"</code> ring</div></div>
<div class="lab-step"><span class="sn">3</span><div><strong>Secondary:</strong> <code>rte_eal_init()</code> with <code>--proc-type=secondary --file-prefix=sase</code>. Lookup <code>"MBUF_POOL"</code> and <code>"RX_TO_ENTERPRISE"</code>.</div></div>
<div class="lab-step"><span class="sn">4</span><div><strong>Secondary process loop:</strong> dequeue from ring → process (print src IP) → free mbuf</div></div>
<div class="lab-step"><span class="sn">5</span><div>Run primary and secondary in separate terminals — verify packets flow through</div></div>
<div class="lab-step"><span class="sn">6</span><div>Kill secondary — verify primary keeps running. Kill primary — observe secondary behavior (segfault or graceful exit)</div></div>
</div>
</div>
<div class="lab-box">
<div class="lab-hdr">&#128293; Lab 9: rte_flow Hardware Classifier</div>
<div class="lab-body">
<p style="font-size:.87rem;margin:.3rem 0 .8rem">Program the NIC to steer specific traffic to queue 0 and observe zero-CPU classification.</p>
<div class="lab-step"><span class="sn">1</span><div>Configure port with 4 queues and start device</div></div>
<div class="lab-step"><span class="sn">2</span><div>Call <code>rte_flow_validate()</code> for a TCP/443 rule — check NIC supports it</div></div>
<div class="lab-step"><span class="sn">3</span><div>Create flow rule: ETH / IPV4 / TCP(dport=443) → QUEUE(0)</div></div>
<div class="lab-step"><span class="sn">4</span><div>Send mixed traffic: HTTPS (443), HTTP (80), DNS (53)</div></div>
<div class="lab-step"><span class="sn">5</span><div>Verify only HTTPS packets appear on queue 0; HTTP/DNS go through RSS to other queues</div></div>
<div class="lab-step"><span class="sn">6</span><div>Add a second rule: DROP all traffic from 10.0.0.0/8 (test with spoofed packets)</div></div>
<div class="lab-step"><span class="sn">7</span><div>Destroy rules and verify traffic reverts to pure RSS distribution</div></div>
</div>
</div>
<p class="sep">MASTERY CHECKLIST</p>
<ul class="cl">
<li>Can explain primary vs secondary: who creates, who looks up, who can't reconfigure NIC</li>
<li>Can explain what --file-prefix does and what happens if primaries/secondaries use different prefixes</li>
<li>Can write a secondary process that finds a named mempool and ring created by a primary</li>
<li>Can explain what rte_flow does that RSS cannot</li>
<li>Can write a complete rte_flow rule with pattern + action + validate + create + destroy</li>
<li>Can explain NUMA remote memory access penalty and how to avoid it</li>
<li>Can explain false sharing and demonstrate the __rte_cache_aligned fix</li>
<li>Can identify the NUMA socket for a given NIC port and allocate resources on it</li>
</ul>
</div><!-- /t-lab -->
<div class="mod-nav">
  <a href="/learning/data-plane/dpdk/module-p2-rings/">&#8592; P2B: rte_ring &amp; App Models</a>
  <a href="/learning/data-plane/dpdk/dpdk-roadmap/">&#8593; Roadmap</a>
  <a class="nb" href="/learning/data-plane/dpdk/module-p3-perf/">P3B: Patterns, Tuning &amp; Debug &#8594;</a>
</div>
<script>
function vt(e,id){
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  e.target.classList.add('active');
}
</script>
