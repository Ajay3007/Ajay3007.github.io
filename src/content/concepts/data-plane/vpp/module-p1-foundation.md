---
title: "VPP P1 - Foundation and Environment"
description: "VPP MASTERY · PHASE 1 · WEEKS 1–3 ⚡ Foundation Environment Scalar vs Vector · VPP Layers · Build · Docker + Mellanox · startup.conf · CLI · First Packet Docker AMD + Mellanox…"
domain: data-plane
track: vpp
order: 1
ownHeader: true
url: /learning/data-plane/vpp/module-p1-foundation/
---

<style>
/* ── Shared VPP Module Styles ───────────────────────────────── */
:root {
  --vpp-blue: #1a3a5c;
  --vpp-teal: #1a7a6e;
  --vpp-orange: #c05e1b;
  --vpp-purple: #5b3a8c;
  --vpp-green: #1e6b3c;
}
.mod-header {
  background: linear-gradient(135deg, #0d1b2a 0%, #1a3a5c 100%);
  border-radius: 12px 12px 0 0;
  padding: 1.8rem 2rem 1.4rem;
  color: #fff;
  margin-bottom: 0;
}
.mod-eyebrow {
  font-size: .7rem;
  font-family: monospace;
  letter-spacing: .12em;
  color: #7ab8d8;
  text-transform: uppercase;
  margin-bottom: .5rem;
}
.mod-title {
  font-size: 2rem;
  font-weight: 800;
  color: #fff;
  margin: .2rem 0 .6rem;
  letter-spacing: -.02em;
  border: none;
}
.mod-subtitle { color: #a8cce0; font-size: .95rem; margin-bottom: 1rem; }
.mod-pills { display: flex; flex-wrap: wrap; gap: .5rem; margin-top: .8rem; }
.mod-pill {
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.18);
  border-radius: 20px;
  padding: 3px 12px;
  font-size: .72rem;
  font-family: monospace;
  color: #c8e4f4;
}

/* Tabs */
.tab-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 0;
  background: #0d1b2a;
  border-radius: 0 0 8px 8px;
  overflow-x: auto;
  margin-bottom: 2rem;
}
.tab-btn {
  padding: .65rem 1.1rem;
  font-size: .8rem;
  font-weight: 600;
  font-family: monospace;
  color: #7ab8d8;
  background: transparent;
  border: none;
  cursor: pointer;
  border-bottom: 2px solid transparent;
  white-space: nowrap;
  transition: color .15s, border-color .15s;
}
.tab-btn:hover { color: #fff; }
.tab-btn.active { color: #5dd6c8; border-bottom-color: #5dd6c8; }
.tab-pane { display: none; }
.tab-pane.active { display: block; }

/* Concept panels */
.concept-panel {
  border-radius: 10px;
  border: 1.5px solid var(--border-color, #e4e4e4);
  background: var(--card-bg, #fff);
  margin: 1.2rem 0;
  overflow: hidden;
}
.concept-panel-hdr {
  padding: .8rem 1.2rem;
  display: flex;
  align-items: center;
  gap: .7rem;
  border-bottom: 1px solid var(--border-color, #eee);
}
.concept-panel-hdr .icon { font-size: 1.2rem; }
.concept-panel-hdr h3 {
  margin: 0;
  font-size: 1rem;
  font-weight: 700;
  border: none;
  color: var(--text-color, #111);
}
.concept-panel-hdr .tag {
  margin-left: auto;
  font-size: .68rem;
  font-family: monospace;
  padding: 2px 8px;
  border-radius: 4px;
  font-weight: 700;
  letter-spacing: .04em;
}
.concept-panel-body { padding: 1.1rem 1.2rem; }
.concept-panel-body p, .concept-panel-body li {
  font-size: .9rem;
  line-height: 1.7;
  color: var(--text-color, #222);
}
.concept-panel-body ul { margin: .4rem 0; padding-left: 1.4rem; }
.concept-panel-body li { margin-bottom: .3rem; }

/* Color variants */
.panel-blue .concept-panel-hdr { background: #e8f1f9; }
.panel-teal .concept-panel-hdr { background: #e0f0ee; }
.panel-orange .concept-panel-hdr { background: #faeee4; }
.panel-purple .concept-panel-hdr { background: #ede8f5; }
.panel-green .concept-panel-hdr { background: #e2f0e8; }
[data-theme="dark"] .panel-blue .concept-panel-hdr { background: #0d2030; }
[data-theme="dark"] .panel-teal .concept-panel-hdr { background: #0a2420; }
[data-theme="dark"] .panel-orange .concept-panel-hdr { background: #2a1808; }
[data-theme="dark"] .panel-purple .concept-panel-hdr { background: #1e1028; }
[data-theme="dark"] .panel-green .concept-panel-hdr { background: #0a2018; }

.tag-blue { background: #d0e8f8; color: #1a4a7c; }
.tag-teal { background: #c8e8e4; color: #0e5248; }
.tag-orange { background: #fad8c0; color: #8c3a0a; }
.tag-purple { background: #e0d4f4; color: #3a1a6c; }
.tag-green { background: #c8e8d4; color: #0e4a28; }

/* Code blocks */
.code-block {
  background: #0d1b2a;
  border-radius: 8px;
  padding: 1rem 1.2rem;
  margin: .8rem 0;
  overflow-x: auto;
  border-left: 3px solid #1a7a6e;
}
.code-block pre {
  margin: 0;
  font-family: 'Courier New', monospace;
  font-size: .82rem;
  line-height: 1.6;
  color: #a8d8c0;
  white-space: pre;
}
.code-block .c-comment { color: #5d8a70; }
.code-block .c-key { color: #7ab8d8; }
.code-block .c-val { color: #f0c080; }
.code-block .c-str { color: #f0a060; }

/* DPDK callout */
.dpdk-box {
  background: #f0ecf8;
  border: 1.5px solid #9b7bd0;
  border-left: 4px solid #5b3a8c;
  border-radius: 8px;
  padding: 1rem 1.2rem;
  margin: 1rem 0;
}
[data-theme="dark"] .dpdk-box { background: #1a1028; border-color: #7060a8; border-left-color: #9b7bd0; }
.dpdk-box .dpdk-hdr {
  font-size: .72rem;
  font-family: monospace;
  font-weight: 700;
  letter-spacing: .08em;
  color: #5b3a8c;
  margin-bottom: .5rem;
  text-transform: uppercase;
}
[data-theme="dark"] .dpdk-box .dpdk-hdr { color: #b090e8; }
.dpdk-box ul { margin: 0; padding-left: 1.2rem; }
.dpdk-box li { font-size: .87rem; line-height: 1.65; color: var(--text-color,#222); margin-bottom: .25rem; }

/* Key insight box */
.insight-box {
  background: #e8f5f0;
  border: 1.5px solid #1a7a6e;
  border-radius: 8px;
  padding: .9rem 1.1rem;
  margin: 1rem 0;
}
[data-theme="dark"] .insight-box { background: #0a2420; border-color: #2a9a8e; }
.insight-box p { margin: 0; font-size: .88rem; line-height: 1.65; color: var(--text-color,#222); }
.insight-box strong { color: #0e5248; }
[data-theme="dark"] .insight-box strong { color: #5dd6c8; }

/* Layer boxes */
.layer-stack { display: flex; flex-direction: column; gap: .5rem; margin: 1rem 0; }
.layer-box {
  border-radius: 8px;
  padding: .8rem 1.2rem;
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}
.layer-label {
  font-family: monospace;
  font-weight: 800;
  font-size: .9rem;
  min-width: 80px;
  padding-top: .05rem;
}
.layer-box p { margin: 0; font-size: .88rem; line-height: 1.6; color: var(--text-color,#222); }
.layer-box code { font-size: .8rem; background: rgba(0,0,0,.06); padding: 1px 5px; border-radius: 3px; }

/* Config file block */
.conf-block {
  background: #111;
  border-radius: 8px;
  padding: 1rem 1.2rem;
  margin: .8rem 0;
  overflow-x: auto;
}
.conf-block pre {
  margin: 0;
  font-family: monospace;
  font-size: .82rem;
  line-height: 1.65;
  color: #e0e0e0;
}
.conf-key { color: #7ab8d8; }
.conf-val { color: #f0c080; }
.conf-comment { color: #5a7a5a; }
.conf-section { color: #5dd6c8; font-weight: 700; }

/* CLI table */
.cli-table { width: 100%; border-collapse: collapse; margin: .8rem 0; font-size: .87rem; }
.cli-table th {
  background: #1a3a5c;
  color: #fff;
  padding: .55rem .9rem;
  text-align: left;
  font-size: .78rem;
  font-weight: 700;
  font-family: monospace;
  letter-spacing: .04em;
}
.cli-table td { padding: .5rem .9rem; border-bottom: 1px solid var(--border-color,#eee); color: var(--text-color,#222); vertical-align: top; }
.cli-table tr:nth-child(even) td { background: var(--bg-color,#f8f8f8); }
.cli-table code { font-size: .8rem; background: rgba(0,0,0,.06); padding: 1px 5px; border-radius: 3px; color: #1a7a6e; }

/* Mini project box */
.project-box {
  border: 2px solid var(--vpp-orange,#c05e1b);
  border-radius: 10px;
  overflow: hidden;
  margin: 1.5rem 0;
  background: var(--card-bg,#fff);
}
.project-box-hdr {
  background: #c05e1b;
  padding: .75rem 1.2rem;
  display: flex;
  align-items: center;
  gap: .8rem;
}
.project-box-hdr .pnum {
  background: rgba(255,255,255,.2);
  border-radius: 6px;
  padding: 2px 10px;
  font-family: monospace;
  font-size: .8rem;
  font-weight: 700;
  color: #fff;
}
.project-box-hdr h4 { margin: 0; color: #fff; font-size: 1rem; font-weight: 700; }
.project-box-body { padding: 1.1rem 1.2rem; }
.project-box-body p { font-size: .88rem; line-height: 1.65; color: var(--text-color,#333); margin-bottom: .5rem; }
.project-step {
  display: flex;
  gap: .7rem;
  align-items: flex-start;
  padding: .4rem 0;
  border-bottom: 1px dashed var(--border-color,#eee);
  font-size: .87rem;
  color: var(--text-color,#333);
  line-height: 1.55;
}
.project-step:last-of-type { border-bottom: none; }
.project-step .step-n {
  background: #c05e1b;
  color: #fff;
  border-radius: 50%;
  width: 22px; height: 22px;
  display: flex; align-items: center; justify-content: center;
  font-size: .72rem;
  font-weight: 700;
  flex-shrink: 0;
  margin-top: .05rem;
}
.project-meta {
  display: flex; flex-wrap: wrap; gap: .5rem; margin-top: .8rem;
}
.project-meta-item {
  font-size: .77rem;
  font-family: monospace;
  padding: 3px 10px;
  border-radius: 5px;
  font-weight: 600;
}
.pm-docker { background: #e0f0f8; color: #0d4060; }
.pm-code { background: #e0f0e8; color: #0d4030; }
[data-theme="dark"] .pm-docker { background: #0a2030; color: #60c0e8; }
[data-theme="dark"] .pm-code { background: #0a2018; color: #60d890; }

/* Checklist */
.checklist { list-style: none; padding: 0; margin: .5rem 0; }
.checklist li {
  display: flex; align-items: flex-start; gap: .6rem;
  padding: .45rem .6rem;
  border-radius: 6px;
  font-size: .87rem;
  color: var(--text-color,#222);
  line-height: 1.5;
  border-bottom: 1px solid var(--border-color,#f0f0f0);
}
.checklist li:last-child { border-bottom: none; }
.checklist li::before {
  content: '☐';
  font-size: 1rem;
  flex-shrink: 0;
  color: #1a7a6e;
  margin-top: -.05rem;
}

/* Nav */
.mod-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: .8rem;
  margin-top: 2.5rem;
  padding-top: 1.2rem;
  border-top: 1px solid var(--border-color,#eee);
}
.mod-nav a {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  padding: .5rem 1rem;
  border-radius: 7px;
  background: var(--card-bg,#f5f5f5);
  border: 1px solid var(--border-color,#ddd);
  font-size: .85rem;
  font-weight: 600;
  color: var(--text-color,#333) !important;
  text-decoration: none !important;
  transition: background .15s;
}
.mod-nav a:hover { background: var(--bg-color,#ebebeb); }
.mod-nav .next-btn { background: #1a3a5c; color: #fff !important; border-color: #1a3a5c; }
.mod-nav .next-btn:hover { background: #245280; }

/* Section title */
.section-sep {
  font-size: .7rem; font-family: monospace; font-weight: 700;
  letter-spacing: .1em; text-transform: uppercase;
  color: var(--light-text,#888);
  margin: 2rem 0 .8rem;
  padding-bottom: .35rem;
  border-bottom: 1px solid var(--border-color,#eee);
}
</style>
<!-- HEADER -->
<div class="mod-header">
  <div class="mod-eyebrow">VPP MASTERY · PHASE 1 · WEEKS 1–3</div>
  <div class="mod-title">⚡ Foundation &amp; Environment</div>
  <div class="mod-subtitle">Scalar vs Vector · VPP Layers · Build · Docker + Mellanox · startup.conf · CLI · First Packet</div>
  <div class="mod-pills">
<span class="mod-pill">Docker</span>
<span class="mod-pill">AMD + Mellanox</span>
<span class="mod-pill">DPDK Background</span>
<span class="mod-pill">vppctl</span>
<span class="mod-pill">1 Mini-Project</span>
  </div>
</div>
<!-- TAB BAR -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="switchTab(event,'t-mental')">Mental Model</button>
  <button class="tab-btn" onclick="switchTab(event,'t-layers')">VPP Layers</button>
  <button class="tab-btn" onclick="switchTab(event,'t-build')">Build &amp; Docker</button>
  <button class="tab-btn" onclick="switchTab(event,'t-conf')">startup.conf</button>
  <button class="tab-btn" onclick="switchTab(event,'t-cli')">vppctl CLI</button>
  <button class="tab-btn" onclick="switchTab(event,'t-proj')">Mini-Project</button>
  <button class="tab-btn" onclick="switchTab(event,'t-check')">Checklist</button>
</div>
<!-- ══════════ TAB: MENTAL MODEL ══════════ -->
<div id="t-mental" class="tab-pane active">
<p class="section-sep">THE FUNDAMENTAL SHIFT</p>
<div class="concept-panel panel-blue">
  <div class="concept-panel-hdr">
<span class="icon">🧠</span>
<h3>Scalar vs Vector Packet Processing</h3>
<span class="tag tag-blue">CORE CONCEPT</span>
  </div>
  <div class="concept-panel-body">
<p><strong>Scalar (traditional stacks):</strong> One packet enters the stack, traverses all processing stages, exits. Then the next packet starts. Every packet re-warms the CPU instruction cache from scratch.</p>
<p><strong>Vector (VPP's model):</strong> A <em>batch</em> of packets - the vector - enters a single graph node together. That node processes all N packets before any packet moves to the next node. The first packet in the batch warms the I-cache; every subsequent packet in the batch benefits at zero cost.</p>
<div class="code-block">

```python
// Scalar processing - per-packet cache thrash
for each packet:
  ip4_lookup(pkt)     // I-cache warm
  ip4_rewrite(pkt)    // I-cache cold again
  ethernet_output(pkt)

// Vector processing - VPP's model
ip4_lookup(pkt[0..255])     // warm once, amortised over 256 pkts
ip4_rewrite(pkt[0..255])    // warm once, amortised over 256 pkts
ethernet_output(pkt[0..255]) // warm once, amortised over 256 pkts
```



<p>This single architectural decision - processing a vector of packets per node invocation - gives VPP its performance edge. It enables prefetching, SIMD vectorisation, and cache-efficient branch prediction that simply cannot happen one packet at a time.</p>
  </div>
</div>
<div class="dpdk-box">
  <div class="dpdk-hdr">⚙️ DPDK PARALLEL - What You Already Know</div>
  <ul>
<li><strong>rte_eth_rx_burst()</strong> is VPP's equivalent of "get a vector of packets" - you already use burst RX for the same reason</li>
<li><strong>PMD poll loop</strong> maps to VPP's INPUT node polling: both spin on hardware without interrupts</li>
<li><strong>rte_mbuf** array from rx_burst</strong> ≈ VPP's <code>vlib_frame_t</code> of buffer indices - a batch of packet references processed together</li>
<li>VPP generalises the single DPDK burst loop into a <em>chain</em> of N graph nodes, each processing the same batch</li>
  </ul>
</div>
<div class="concept-panel panel-teal">
  <div class="concept-panel-hdr">
<span class="icon">📊</span>
<h3>The Packet Processing Graph - Core Mental Model</h3>
<span class="tag tag-teal">ARCHITECTURE</span>
  </div>
  <div class="concept-panel-body">
<p>VPP's dataplane is a <strong>directed graph</strong> of processing nodes. Each node is a C function. Packets (as buffer indices) flow along graph edges. A single packet traversal from RX to TX typically looks like:</p>
<div class="code-block"><pre><span class="c-key">dpdk-input</span>
  → <span class="c-key">ethernet-input</span>
    → <span class="c-key">ip4-input</span>
      → <span class="c-key">ip4-lookup</span>       <span class="c-comment">(FIB lookup → next-hop)</span>
        → <span class="c-key">ip4-rewrite</span>    <span class="c-comment">(rewrite L2 header)</span>
          → <span class="c-key">dpdk-output</span>  <span class="c-comment">(TX to NIC)</span></pre></div>
<p>The graph is <strong>not acyclic</strong> - a packet can re-visit ip4-lookup multiple times (e.g., MPLS label push/pop). Each node's output is a <em>next index</em> that selects the outgoing edge.</p>
<ul>
<li>Nodes communicate via <code>vlib_frame_t</code>: arrays of <strong>u32 buffer indices</strong>, not pointers</li>
<li>All nodes for a given phase run to completion before the next phase begins</li>
<li>The graph dispatcher (<code>vlib_main_loop</code>) drives everything - you never write a main loop</li>
</ul>
  </div>
</div>
<div class="insight-box">
  <p>💡 <strong>Key insight - why u32 indices, not pointers?</strong> A u32 is 4 bytes; a pointer is 8. A frame of 256 packet references is 1 KB with indices vs 2 KB with pointers. This matters: the entire frame fits in a cache line set. Buffer pool base address + index = pointer at any time - zero overhead to dereference.</p>
</div>
</div>
<!-- ══════════ TAB: VPP LAYERS ══════════ -->
<div id="t-layers" class="tab-pane">
<p class="section-sep">IMPLEMENTATION TAXONOMY</p>
<div class="layer-stack">
  <div class="layer-box" style="background:#e8f1f9; border: 1.5px solid #b0ccec;">
<div class="layer-label" style="color:#1a3a5c;">VPP</div>
<div>
<p><strong>Container application</strong> - the <code>vpp</code> binary itself. Ties all layers together, runs the main loop, loads plugins. Source: <code>src/vpp/</code></p>
</div>
  </div>
  <div class="layer-box" style="background:#faeee4; border: 1.5px solid #e8b890;">
<div class="layer-label" style="color:#c05e1b;">Plugins</div>
<div>
<p><strong>Shared libraries loaded at startup.</strong> DPDK, memif, NAT, ACL, GTP, QUIC - all plugins. Your own features go here. Source: <code>src/plugins/</code></p>
<p>Key plugins: <code>dpdk_plugin.so</code>, <code>memif_plugin.so</code>, <code>nat_plugin.so</code>, <code>acl_plugin.so</code>, <code>af_xdp_plugin.so</code></p>
</div>
  </div>
  <div class="layer-box" style="background:#e2f0e8; border: 1.5px solid #8ec8a8;">
<div class="layer-label" style="color:#1e6b3c;">VNET</div>
<div>
<p><strong>Networking layer.</strong> L2/L3/L4 graph nodes, interface abstraction (sw_if_index), FIB, ARP, neighbour tables, session layer. Source: <code>src/vnet/</code></p>
<p>Key subdirs: <code>src/vnet/ip/</code>, <code>src/vnet/ethernet/</code>, <code>src/vnet/fib/</code>, <code>src/vnet/devices/</code></p>
</div>
  </div>
  <div class="layer-box" style="background:#e0f0ee; border: 1.5px solid #80c0b8;">
<div class="layer-label" style="color:#1a7a6e;">VLIB</div>
<div>
<p><strong>Vector processing library.</strong> Graph node scheduler, buffer management, cooperative threads (process nodes), CLI, packet tracing, counters. Source: <code>src/vlib/</code></p>
<p>Key files: <code>src/vlib/main.c</code> (dispatch loop), <code>src/vlib/node.h</code>, <code>src/vlib/buffer.h</code></p>
</div>
  </div>
  <div class="layer-box" style="background:#ede8f5; border: 1.5px solid #c0a8e8;">
<div class="layer-label" style="color:#5b3a8c;">VPPInfra</div>
<div>
<p><strong>Core library - VPP's libc.</strong> Memory allocators, vectors, pools, hash tables, ring buffers, format/unformat, timers. Everything is built on top of this. Source: <code>src/vppinfra/</code></p>
<p>Key files: <code>pool.h</code>, <code>vec.h</code>, <code>hash.h</code>, <code>bihash_8_8.h</code>, <code>clib.h</code>, <code>format.h</code></p>
</div>
  </div>
</div>
<div class="concept-panel panel-blue">
  <div class="concept-panel-hdr">
<span class="icon">📁</span>
<h3>Source Repository Layout</h3>
<span class="tag tag-blue">CODEBASE MAP</span>
  </div>
  <div class="concept-panel-body">
<div class="code-block"><pre>github.com/FDio/vpp
├── <span class="c-key">src/vppinfra/</span>     <span class="c-comment"># Core library: vec.h, pool.h, hash.h, bihash_*.h</span>
├── <span class="c-key">src/vlib/</span>         <span class="c-comment"># Graph dispatcher: main.c, node.h, buffer.h, threads.c</span>
├── <span class="c-key">src/vnet/</span>         <span class="c-comment"># Networking: ip/, ethernet/, fib/, devices/, feature/</span>
├── <span class="c-key">src/plugins/</span>      <span class="c-comment"># Plugins: dpdk/, memif/, nat/, acl/, af_xdp/, linux-cp/</span>
├── <span class="c-key">src/vpp/</span>          <span class="c-comment"># Container binary: app/vpe_cli.c</span>
├── <span class="c-key">src/vpp-api/</span>      <span class="c-comment"># API bindings: python/vpp_papi/, .api.json files</span>
├── <span class="c-key">src/svm/</span>          <span class="c-comment"># Shared virtual memory</span>
├── <span class="c-key">src/examples/</span>    <span class="c-comment"># Sample plugin, handoff demo</span>
└── <span class="c-key">test/</span>             <span class="c-comment"># Python test framework: test_*.py</span></pre></div>
<p>When you explore a new VPP subsystem, start by reading the <code>.h</code> file - it contains the data structures and macro definitions. The <code>.c</code> file contains the implementations. API definitions live in <code>.api</code> files alongside each plugin.</p>
  </div>
</div>
</div>
<!-- ══════════ TAB: BUILD & DOCKER ══════════ -->
<div id="t-build" class="tab-pane">
<p class="section-sep">BUILD FROM SOURCE</p>
<div class="concept-panel panel-teal">
  <div class="concept-panel-hdr">
<span class="icon">🔨</span>
<h3>Building VPP</h3>
<span class="tag tag-teal">HANDS-ON</span>
  </div>
  <div class="concept-panel-body">
<p>Always build from source for development. Binary packages hide important details. The VPP build system is CMake-based with a convenience Makefile wrapper.</p>
<div class="code-block">

```bash
# Clone the repo
git clone https://github.com/FDio/vpp.git && cd vpp

# Install build dependencies (Ubuntu 22.04)
make install-dep

# Debug build - has symbols, ASAN-compatible, slower
make build

# Release/optimised build - production performance
make build-release

# Run debug VPP interactively (reads /etc/vpp/startup.conf)
make run

# Run under GDB for debugging
make run-gdb

# Run full test suite
make test

# Run a specific test
make test TEST=test_nat
```



<ul>
<li>Debug binary lives at: <code>build-root/install-vpp_debug-native/vpp/bin/vpp</code></li>
<li>Release binary: <code>build-root/install-vpp-native/vpp/bin/vpp</code></li>
<li>Plugins: compiled as <code>.so</code> files, loaded from the plugin directory at startup</li>
</ul>
  </div>
</div>
<p class="section-sep">DOCKER + AMD + MELLANOX SETUP</p>
<div class="concept-panel panel-orange">
  <div class="concept-panel-hdr">
<span class="icon">🐳</span>
<h3>Container Setup for Mellanox Ports</h3>
<span class="tag tag-orange">YOUR ENV</span>
  </div>
  <div class="concept-panel-body">
<p>Your environment: Docker containers on AMD server with Mellanox Ethernet ports. VPP needs privileged access to hugepages, VFIO devices, and the PCI bus. The following setup gives VPP everything it needs.</p>
<div class="code-block">

```bash
# Step 1: Allocate hugepages on the host (2MB pages)
echo 2048 | sudo tee /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages
sudo mkdir -p /dev/hugepages
sudo mount -t hugetlbfs nodev /dev/hugepages

# Step 2: Bind Mellanox port to vfio-pci (use PCI address from lspci)
sudo dpdk-devbind.py --status                     # find PCI address
sudo dpdk-devbind.py --bind vfio-pci 0000:03:00.0
sudo dpdk-devbind.py --bind vfio-pci 0000:03:00.1

# Step 3: Run VPP container with all required resources
docker run --privileged --network host \
  -v /dev/hugepages:/dev/hugepages \
  -v /sys/bus/pci:/sys/bus/pci \
  -v /run/vpp:/run/vpp \
  -v /dev/vfio:/dev/vfio \
  -v /dev/vfio/vfio:/dev/vfio/vfio \
  -v /etc/vpp:/etc/vpp \
  -it ubuntu:22.04 /bin/bash
```



<div class="dpdk-box">
<div class="dpdk-hdr">⚙️ DPDK KNOWLEDGE - Mellanox + VFIO</div>
<ul>
<li><strong>mlx5 PMD</strong>: Mellanox ConnectX-4/5/6 use the mlx5 poll-mode driver. VPP's DPDK plugin includes mlx5 support. No separate binding needed for mlx5 - it works through the kernel <code>mlx5_core</code> + VFIO</li>
<li><strong>IOVA mode</strong>: For Mellanox with DPDK, use <code>--iova-mode va</code> (VA mode). Set in VPP via <code>dpdk { iova-mode va }</code> in startup.conf</li>
<li><strong>SR-IOV VFs</strong>: For multi-container setups, create VFs on the PF and pass one VF per container - same as standard DPDK SR-IOV workflow</li>
<li><strong>No KNI</strong>: VPP does not use DPDK KNI. Use TAP v2 or linux-cp for Linux kernel access</li>
</ul>
</div>
  </div>
</div>
</div>
<!-- ══════════ TAB: STARTUP.CONF ══════════ -->
<div id="t-conf" class="tab-pane">
<p class="section-sep">STARTUP CONFIGURATION</p>
<div class="concept-panel panel-blue">
  <div class="concept-panel-hdr">
<span class="icon">⚙️</span>
<h3>startup.conf - Every Stanza Explained</h3>
<span class="tag tag-blue">CONFIGURATION</span>
  </div>
  <div class="concept-panel-body">
<p><code>startup.conf</code> is VPP's single configuration file, read at launch. It controls process behaviour, CPU pinning, DPDK ports, buffer pools, and plugin loading. Here is a production-annotated example for your environment:</p>
<div class="conf-block"><pre><span class="conf-section">unix</span> {
  <span class="conf-key">nodaemon</span>                          <span class="conf-comment"># run in foreground (good for containers)</span>
  <span class="conf-key">log</span> <span class="conf-val">/var/log/vpp/vpp.log</span>
  <span class="conf-key">full-coredump</span>                     <span class="conf-comment"># core dumps on crash</span>
  <span class="conf-key">cli-listen</span> <span class="conf-val">/run/vpp/cli.sock</span>     <span class="conf-comment"># vppctl connects here</span>
  <span class="conf-key">startup-config</span> <span class="conf-val">/etc/vpp/setup.gate</span> <span class="conf-comment"># CLI commands run at startup</span>
}
 
<span class="conf-section">api-trace</span> {
  <span class="conf-key">on</span>                                <span class="conf-comment"># record API calls (for replay debugging)</span>
}
 
<span class="conf-section">cpu</span> {
  <span class="conf-key">main-core</span> <span class="conf-val">0</span>                       <span class="conf-comment"># pin main thread to core 0</span>
  <span class="conf-key">corelist-workers</span> <span class="conf-val">2-5</span>             <span class="conf-comment"># 4 workers on cores 2-5</span>
  <span class="conf-comment"># corelist-workers 2,4,6,8        # non-contiguous cores also OK</span>
}
 
<span class="conf-section">dpdk</span> {
  <span class="conf-key">dev</span> <span class="conf-val">0000:03:00.0</span> {               <span class="conf-comment"># Mellanox port 0</span>
    <span class="conf-key">num-rx-queues</span> <span class="conf-val">4</span>                <span class="conf-comment"># 1 queue per worker thread</span>
    <span class="conf-key">num-tx-queues</span> <span class="conf-val">4</span>
    <span class="conf-key">num-rx-desc</span> <span class="conf-val">1024</span>
    <span class="conf-key">num-tx-desc</span> <span class="conf-val">1024</span>
  }
  <span class="conf-key">dev</span> <span class="conf-val">0000:03:00.1</span> {               <span class="conf-comment"># Mellanox port 1</span>
    <span class="conf-key">num-rx-queues</span> <span class="conf-val">4</span>
    <span class="conf-key">num-tx-queues</span> <span class="conf-val">4</span>
  }
  <span class="conf-key">uio-driver</span> <span class="conf-val">vfio-pci</span>
  <span class="conf-key">iova-mode</span> <span class="conf-val">va</span>                      <span class="conf-comment"># required for Mellanox mlx5</span>
  <span class="conf-key">socket-mem</span> <span class="conf-val">1024,1024</span>             <span class="conf-comment"># 1 GB per NUMA socket</span>
  <span class="conf-key">no-multi-seg</span>                      <span class="conf-comment"># disable jumbo unless needed</span>
  <span class="conf-key">log-level</span> <span class="conf-val">notice</span>
}
 
<span class="conf-section">buffers</span> {
  <span class="conf-key">buffers-per-numa</span> <span class="conf-val">128000</span>          <span class="conf-comment"># buffer pool size per NUMA node</span>
  <span class="conf-key">default-data-size</span> <span class="conf-val">2048</span>           <span class="conf-comment"># buffer data area in bytes</span>
  <span class="conf-comment"># use 10240 for jumbo/MTU 9000</span>
}
 
<span class="conf-section">plugins</span> {
  <span class="conf-key">path</span> <span class="conf-val">/usr/lib/x86_64-linux-gnu/vpp_plugins</span>
  <span class="conf-key">plugin</span> <span class="conf-val">dpdk_plugin.so</span>  { <span class="conf-key">enable</span> }
  <span class="conf-key">plugin</span> <span class="conf-val">memif_plugin.so</span> { <span class="conf-key">enable</span> }
  <span class="conf-comment"># plugin some_plugin.so { disable }</span>
}
 
<span class="conf-section">statseg</span> {
  <span class="conf-key">size</span> <span class="conf-val">128m</span>                         <span class="conf-comment"># stats segment size</span>
  <span class="conf-key">per-node-counters</span> <span class="conf-val">on</span>
}</pre></div>
<p><strong>Key rules:</strong></p>
<ul>
<li><code>corelist-workers</code> count must equal total RX queues across all interfaces for full utilisation</li>
<li><code>socket-mem</code> uses hugepages - must be pre-allocated on host before container starts</li>
<li><code>buffers-per-numa</code> - if you see buffer allocation failures in logs, increase this</li>
<li><code>startup-config</code> - put CLI commands here (set interface state, add routes) for auto-config at boot</li>
</ul>
  </div>
</div>
</div>
<!-- ══════════ TAB: VPPCTL CLI ══════════ -->
<div id="t-cli" class="tab-pane">
<p class="section-sep">ESSENTIAL CLI COMMANDS</p>
<div class="concept-panel panel-teal">
  <div class="concept-panel-hdr">
<span class="icon">💻</span>
<h3>vppctl - Your Primary Interface</h3>
<span class="tag tag-teal">CLI REFERENCE</span>
  </div>
  <div class="concept-panel-body">
<p><code>vppctl</code> connects to VPP's Unix socket (<code>/run/vpp/cli.sock</code>) and sends CLI commands. You can use it interactively or pipe commands:</p>
<div class="code-block"><pre>vppctl                      <span class="c-comment"># interactive shell</span>
vppctl show version         <span class="c-comment"># single command</span>
echo "show run" | vppctl    <span class="c-comment"># pipe</span></pre></div>
  </div>
</div>
<table class="cli-table">
  <thead><tr><th>Command</th><th>What It Shows / Does</th><th>Use When</th></tr></thead>
  <tbody>
<tr><td><code>show version</code></td><td>VPP version, build date, plugins loaded</td><td>First thing after starting VPP</td></tr>
<tr><td><code>show plugins</code></td><td>All loaded plugins with versions</td><td>Verify dpdk_plugin, memif_plugin loaded</td></tr>
<tr><td><code>show interface</code></td><td>All interfaces: state, RX/TX packet+byte counters, error counts</td><td>Check interface is up, count packets</td></tr>
<tr><td><code>show run</code></td><td>Per-node stats: calls, vectors processed, suspends, <strong>clocks/vector</strong></td><td>Most important perf view - check vectors/call</td></tr>
<tr><td><code>show buffers</code></td><td>Buffer pool utilisation per NUMA node</td><td>Check for buffer starvation (free &lt; 20%)</td></tr>
<tr><td><code>show error</code></td><td>Error counter table: which nodes are dropping and why</td><td>Debug drops - e.g. "ip4 source lookup miss"</td></tr>
<tr><td><code>show ip fib</code></td><td>FIB routing table: all prefixes and their DPO chains</td><td>Verify routes are programmed correctly</td></tr>
<tr><td><code>show ip neighbors</code></td><td>ARP/ND neighbour table</td><td>Check ARP resolution</td></tr>
<tr><td><code>trace add dpdk-input 100</code></td><td>Capture next 100 packets entering from DPDK input</td><td>Start trace before sending test traffic</td></tr>
<tr><td><code>show trace</code></td><td>Full per-packet trace: every node the packet visited with timestamps</td><td>After trace capture - shows complete packet path</td></tr>
<tr><td><code>clear trace</code></td><td>Clear the trace buffer</td><td>Before new capture</td></tr>
<tr><td><code>show interface rx-placement</code></td><td>Which worker thread handles which interface RX queue</td><td>Verify NUMA-local queue assignments</td></tr>
<tr><td><code>set interface rx-placement &lt;if&gt; queue 0 worker 0</code></td><td>Assign interface queue to specific worker</td><td>Manual NUMA-aware pinning</td></tr>
<tr><td><code>set interface state &lt;if&gt; up</code></td><td>Bring interface up</td><td>After creating interface</td></tr>
<tr><td><code>set interface ip address &lt;if&gt; 10.0.0.1/24</code></td><td>Assign IP address</td><td>Configure L3 interface</td></tr>
<tr><td><code>show dpdk interface</code></td><td>DPDK-specific interface info: queues, link speed, driver</td><td>Verify mlx5 link is up at correct speed</td></tr>
<tr><td><code>show dpdk interface xstats &lt;if&gt;</code></td><td>Extended NIC statistics from the DPDK ethdev layer</td><td>Deep NIC-level counters</td></tr>
<tr><td><code>show log</code></td><td>VPP internal log messages</td><td>Troubleshoot startup and plugin errors</td></tr>
<tr><td><code>event-logger on</code></td><td>Enable high-resolution event logger</td><td>Timing analysis - use with g2 viewer</td></tr>
  </tbody>
</table>
<div class="insight-box">
  <p>💡 <strong>The most important command: <code>show run</code></strong> - look at <em>vectors/call</em> for your input node. A value of 32–256 means VPP is batching well. A value of 1–4 means the system is lightly loaded or misconfigured. <em>Clocks/vector</em> is your per-packet CPU cost - lower is better.</p>
</div>
</div>
<!-- ══════════ TAB: MINI-PROJECT ══════════ -->
<div id="t-proj" class="tab-pane">
<div class="project-box">
  <div class="project-box-hdr">
<span class="pnum">PROJECT 1</span>
<h4>VPP Container Lab - First Packet</h4>
  </div>
  <div class="project-box-body">
<p><strong>Objective:</strong> Spin up a VPP instance inside Docker with Mellanox ports, configure two interfaces, send traffic, and fully trace the packet path through the graph.</p>
<div class="project-step"><div class="step-n">1</div><div>Pull or build a VPP Docker image with DPDK support for Mellanox mlx5. Verify with <code>show plugins</code> that <code>dpdk_plugin.so</code> is loaded.</div></div>
<div class="project-step"><div class="step-n">2</div><div>Write a <code>startup.conf</code> with your Mellanox PCI addresses, 1 GB hugepages per socket, and 2 worker threads pinned to non-overlapping cores.</div></div>
<div class="project-step"><div class="step-n">3</div><div>Start VPP and run <code>show interface</code>. Both Mellanox ports should appear as <code>GigabitEthernet</code> or <code>Ethernet</code> devices. Bring them up: <code>set interface state &lt;if&gt; up</code>.</div></div>
<div class="project-step"><div class="step-n">4</div><div>Assign IP addresses to both DPDK interfaces. Add a static route between them: <code>ip route add 192.168.2.0/24 via 192.168.1.2</code>.</div></div>
<div class="project-step"><div class="step-n">5</div><div>From a peer container or host, start a trace: <code>trace add dpdk-input 100</code>. Then send 10 ICMP pings to VPP's interface IP.</div></div>
<div class="project-step"><div class="step-n">6</div><div>Run <code>show trace</code>. For each captured packet, identify every graph node it visited and the time spent (in clock ticks) at each node.</div></div>
<div class="project-step"><div class="step-n">7</div><div>Run <code>show run</code>. Record: vectors/call for dpdk-input, clocks/vector for ip4-lookup and ip4-rewrite. This is your baseline performance fingerprint.</div></div>
<div class="project-step"><div class="step-n">8</div><div>Experiment: change worker threads from 2 to 4 in startup.conf, restart, and compare <code>show run</code> output. Does throughput scale linearly?</div></div>
<div class="project-step"><div class="step-n">9</div><div>Run <code>show error</code> and verify there are no unexpected drops. If there are, trace a dropped packet and identify the error node.</div></div>
<div class="project-meta">
<span class="project-meta-item pm-docker">🐳 Docker --privileged + /dev/hugepages + /dev/vfio bind-mounted</span>
<span class="project-meta-item pm-code">📂 src/plugins/dpdk/device/node.c · src/vnet/ip/ip4_forward.c</span>
</div>
  </div>
</div>
</div>
<!-- ══════════ TAB: CHECKLIST ══════════ -->
<div id="t-check" class="tab-pane">
<p class="section-sep">PHASE 1 COMPLETION CHECKLIST</p>
<ul class="checklist">
  <li>Can explain scalar vs vector processing and why vector processing improves I-cache utilisation</li>
  <li>Know the 5 VPP layers (VPPInfra, vlib, vnet, plugins, VPP binary) and what each is responsible for</li>
  <li>Can build VPP from source (<code>make build</code> and <code>make build-release</code>) and know where the binaries are</li>
  <li>Can run a VPP container on the AMD/Mellanox environment with correct hugepage and VFIO setup</li>
  <li>Can write a complete <code>startup.conf</code> from scratch with DPDK stanza, CPU pinning, and buffer sizing</li>
  <li>Know the difference between <code>main-core</code> and <code>corelist-workers</code> and how to size them for NIC queues</li>
  <li>Can use <code>vppctl</code> to bring up interfaces, assign IPs, add routes</li>
  <li>Can capture and interpret a packet trace - identify each graph node in the trace output</li>
  <li>Understand what <code>show run</code> shows: vectors/call, clocks/vector, and what good values look like</li>
  <li>Completed Mini-Project 1: first packet traced end-to-end through the VPP graph</li>
</ul>
<div class="insight-box" style="margin-top:1.2rem;">
  <p>✅ When complete: ready for <strong>Phase 2 - Core VPP Internals</strong>. Start with <strong>vppinfra</strong> - every data structure you'll use in plugins is defined there.</p>
</div>
</div>
<!-- MODULE NAV -->
<div class="mod-nav">
  <a href="/learning/data-plane/vpp/">← VPP Hub</a>
  <a href="/learning/data-plane/vpp/vpp-roadmap/">🗺️ Roadmap</a>
  <a class="next-btn" href="/learning/data-plane/vpp/module-p2-vppinfra/">Next: vppinfra →</a>
</div>
<script>
function switchTab(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
</script>
