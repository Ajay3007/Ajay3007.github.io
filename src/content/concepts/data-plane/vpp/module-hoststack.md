---
title: "VPP Host Stack - TCP and Session Layers"
description: "VPP MASTERY · HOST STACK · BONUS MODULE 🌐 VPP Host Stack TCP Session Layers - Userspace networking, SVM FIFOs, VCL, Cut-through connections src/vnet/session/ src/vnet/tcp/…"
domain: data-plane
track: vpp
order: 99
url: /learning/data-plane/vpp/module-hoststack/
---

<style>
/* ── VPP Module Base ─────────────────────────────── */
.mod-header {
  background: linear-gradient(135deg, #0d1b2a 0%, #1a3a5c 55%, #1a7a6e 100%);
  border-radius: 12px 12px 0 0;
  padding: 1.8rem 2rem 1.4rem;
  color: #fff;
  margin-bottom: 0;
}
.mod-eyebrow {
  font-size: .7rem; font-family: monospace; letter-spacing: .12em;
  color: #7ab8d8; text-transform: uppercase; margin-bottom: .5rem;
}
.mod-title {
  font-size: 2rem; font-weight: 800; color: #fff;
  margin: .2rem 0 .6rem; letter-spacing: -.02em; border: none;
}
.mod-subtitle { color: #a8cce0; font-size: .95rem; margin-bottom: 1rem; }
.mod-pills { display: flex; flex-wrap: wrap; gap: .5rem; margin-top: .8rem; }
.mod-pill {
  background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.18);
  border-radius: 20px; padding: 3px 12px; font-size: .72rem;
  font-family: monospace; color: #c8e4f4;
}

/* Tabs */
.tab-bar {
  display: flex; flex-wrap: wrap; background: #0d1b2a;
  border-radius: 0 0 8px 8px; overflow-x: auto; margin-bottom: 2rem;
}
.tab-btn {
  padding: .65rem 1.1rem; font-size: .8rem; font-weight: 600;
  font-family: monospace; color: #7ab8d8; background: transparent;
  border: none; cursor: pointer; border-bottom: 2px solid transparent;
  white-space: nowrap; transition: color .15s, border-color .15s;
}
.tab-btn:hover { color: #fff; }
.tab-btn.active { color: #5dd6c8; border-bottom-color: #5dd6c8; }
.tab-pane { display: none; }
.tab-pane.active { display: block; }

/* Concept panels */
.cp {
  border-radius: 10px; border: 1.5px solid var(--border-color, #e4e4e4);
  background: var(--card-bg, #fff); margin: 1.2rem 0; overflow: hidden;
}
.cp-hdr {
  padding: .8rem 1.2rem; display: flex; align-items: center; gap: .7rem;
  border-bottom: 1px solid var(--border-color, #eee);
}
.cp-hdr .ico { font-size: 1.2rem; }
.cp-hdr h3 { margin: 0; font-size: 1rem; font-weight: 700; border: none; color: var(--text-color, #111); }
.cp-hdr .tag {
  margin-left: auto; font-size: .68rem; font-family: monospace;
  padding: 2px 8px; border-radius: 4px; font-weight: 700; letter-spacing: .04em;
}
.cp-body { padding: 1.1rem 1.2rem; }
.cp-body p, .cp-body li { font-size: .9rem; line-height: 1.7; color: var(--text-color, #222); }
.cp-body ul { margin: .4rem 0; padding-left: 1.4rem; }
.cp-body li { margin-bottom: .3rem; }

/* Panel colour variants */
.p-blue  .cp-hdr { background: #e8f1f9; } [data-theme=dark] .p-blue  .cp-hdr { background: #0d2030; }
.p-teal  .cp-hdr { background: #e0f0ee; } [data-theme=dark] .p-teal  .cp-hdr { background: #0a2420; }
.p-orange .cp-hdr { background: #faeee4; } [data-theme=dark] .p-orange .cp-hdr { background: #2a1808; }
.p-purple .cp-hdr { background: #ede8f5; } [data-theme=dark] .p-purple .cp-hdr { background: #1e1028; }
.p-green  .cp-hdr { background: #e2f0e8; } [data-theme=dark] .p-green  .cp-hdr { background: #0a2018; }
.p-red    .cp-hdr { background: #faeaea; } [data-theme=dark] .p-red    .cp-hdr { background: #2a0808; }

.tag-blue   { background: #d0e8f8; color: #1a4a7c; }
.tag-teal   { background: #c8e8e4; color: #0e5248; }
.tag-orange { background: #fad8c0; color: #8c3a0a; }
.tag-purple { background: #e0d4f4; color: #3a1a6c; }
.tag-green  { background: #c8e8d4; color: #0e4a28; }
.tag-red    { background: #f4d0d0; color: #6c1a1a; }

/* Code blocks */
.cb {
  background: #0d1b2a; border-radius: 8px; padding: 1rem 1.2rem;
  margin: .8rem 0; overflow-x: auto; border-left: 3px solid #1a7a6e;
}
.cb pre {
  margin: 0; font-family: 'Courier New', monospace; font-size: .82rem;
  line-height: 1.65; color: #c8e0d0; white-space: pre;
}
.cm { color: #4a7a5a; } .ck { color: #7ab8d8; }
.cv { color: #f0c080; } .cs { color: #f0a060; }

/* Insight & warning boxes */
.ins {
  background: #e8f5f0; border: 1.5px solid #1a7a6e; border-radius: 8px;
  padding: .9rem 1.1rem; margin: 1rem 0;
}
[data-theme=dark] .ins { background: #0a2420; border-color: #2a9a8e; }
.ins p { margin: 0; font-size: .88rem; line-height: 1.65; color: var(--text-color, #222); }
.ins strong { color: #0e5248; }
[data-theme=dark] .ins strong { color: #5dd6c8; }

.warn {
  background: #fef6e4; border: 1.5px solid #e0a820;
  border-left: 4px solid #c07800; border-radius: 8px;
  padding: .9rem 1.1rem; margin: 1rem 0;
}
[data-theme=dark] .warn { background: #2a1e00; border-color: #a07000; border-left-color: #d09000; }
.warn p { margin: 0; font-size: .88rem; line-height: 1.65; color: var(--text-color, #222); }

/* Tables */
.t-table { width: 100%; border-collapse: collapse; margin: .8rem 0; font-size: .86rem; }
.t-table th {
  background: #1a3a5c; color: #fff; padding: .5rem .9rem;
  text-align: left; font-size: .77rem; font-weight: 700;
  font-family: monospace; letter-spacing: .04em;
}
.t-table td { padding: .5rem .9rem; border-bottom: 1px solid var(--border-color, #eee); color: var(--text-color, #222); vertical-align: top; }
.t-table tr:nth-child(even) td { background: var(--bg-color, #f8f8f8); }
.t-table code { font-size: .79rem; background: rgba(0,0,0,.06); padding: 1px 5px; border-radius: 3px; color: #1a7a6e; }

/* Term glossary */
.term-grid { display: flex; flex-direction: column; gap: 8px; margin: .5rem 0; }
.term-row {
  border-radius: 8px; border: 0.5px solid var(--border-color, #e0e0e0);
  background: var(--card-bg, #fff); padding: 12px 14px;
  display: grid; grid-template-columns: 150px 1fr; gap: 12px; align-items: start;
}
@media (max-width: 540px) { .term-row { grid-template-columns: 1fr; } }
.term-name {
  font-size: .75rem; font-weight: 700; font-family: monospace;
  color: #1a3a5c; background: #e8f1f9; padding: 3px 8px;
  border-radius: 4px; align-self: start;
}
[data-theme=dark] .term-name { background: #0d2030; color: #7ab8d8; }
.term-def { font-size: .87rem; color: var(--text-color, #333); line-height: 1.65; }

/* Architecture stack diagram */
.arch-stack { display: flex; flex-direction: column; gap: 0; max-width: 560px; margin: 1rem auto; }
.arch-layer {
  padding: 13px 20px; cursor: default; border-left: 4px solid transparent;
  border-bottom: 1px solid rgba(0,0,0,.05);
}
.arch-layer:first-child { border-radius: 10px 10px 0 0; }
.arch-layer:last-child  { border-radius: 0 0 10px 10px; border-bottom: none; }
.arch-layer-name { font-size: .9rem; font-weight: 700; margin-bottom: .15rem; }
.arch-layer-sub  { font-size: .8rem; opacity: .8; }
.arch-sep {
  text-align: center; font-size: .75rem; font-family: monospace;
  color: var(--light-text, #888); padding: 3px 0; letter-spacing: .04em;
}
.al-app    { background: #ede8f5; border-left-color: #5b3a8c; }
.al-app .arch-layer-name { color: #3a1a6c; }
.al-vcl    { background: #faeee4; border-left-color: #c05e1b; }
.al-vcl .arch-layer-name { color: #8c3a0a; }
.al-binapi { background: #fafafa; border-left-color: #aaa; border-top: 2px dashed #ccc; }
.al-binapi .arch-layer-name { color: #555; }
.al-session { background: #e8f1f9; border-left-color: #1a3a5c; }
.al-session .arch-layer-name { color: #1a3a5c; }
.al-tcp    { background: #e0f0ee; border-left-color: #1a7a6e; }
.al-tcp .arch-layer-name { color: #0e5248; }
.al-ip     { background: #e2f0e8; border-left-color: #1e6b3c; }
.al-ip .arch-layer-name { color: #0e4a28; }
.al-dpdk   { background: #faeee4; border-left-color: #c05e1b; }
.al-dpdk .arch-layer-name { color: #8c3a0a; }
[data-theme=dark] .al-app    { background: #1e1028; }
[data-theme=dark] .al-vcl    { background: #2a1808; }
[data-theme=dark] .al-binapi { background: #181818; border-top-color: #444; }
[data-theme=dark] .al-session { background: #0d2030; }
[data-theme=dark] .al-tcp    { background: #0a2420; }
[data-theme=dark] .al-ip     { background: #0a2018; }
[data-theme=dark] .al-dpdk   { background: #2a1808; }

/* Data flow steps */
.flow-list { display: flex; flex-direction: column; gap: 0; margin: 1rem 0; }
.flow-step {
  display: flex; gap: 14px; align-items: flex-start;
  padding: 12px 14px; border-left: 2px solid var(--border-color, #e0e0e0);
  margin-left: 14px; position: relative;
}
.flow-step::before {
  content: attr(data-n);
  position: absolute; left: -14px; top: 14px;
  width: 26px; height: 26px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: .75rem; font-weight: 700; color: #fff;
  background: var(--step-color, #1a3a5c);
}
.flow-step:last-child { border-left-color: transparent; }
.flow-step-body { flex: 1; padding-left: 4px; }
.flow-step-title { font-size: .9rem; font-weight: 700; color: var(--text-color, #111); margin-bottom: .3rem; }
.flow-step-detail { font-size: .87rem; color: var(--text-color, #333); line-height: 1.65; }
.flow-step-code {
  font-family: monospace; font-size: .8rem; display: inline-block;
  background: #0d1b2a; color: #7ab8d8; padding: 2px 8px;
  border-radius: 4px; margin-top: .35rem;
}

/* FIFO diagram */
.fifo-wrap { border-radius: 10px; overflow: hidden; border: 1.5px solid var(--border-color, #e0e0e0); margin: 1rem 0; }
.fifo-hdr { background: #1a3a5c; color: #fff; font-size: .78rem; font-weight: 700; font-family: monospace; padding: 8px 14px; letter-spacing: .04em; }
.fifo-ring { display: flex; gap: 3px; padding: 12px; background: var(--card-bg, #fff); }
.fifo-slot {
  flex: 1; height: 40px; border-radius: 6px; display: flex;
  align-items: center; justify-content: center; font-size: .75rem;
  font-weight: 600; border: 1.5px solid transparent;
}
.fs-data  { background: #d0e8f8; color: #1a3a5c; border-color: #b5d4f4; }
.fs-empty { background: var(--bg-color, #f5f5f5); color: var(--light-text, #aaa); border-color: var(--border-color, #e0e0e0); }
.fs-head  { outline: 2.5px solid #1a7a6e; }
.fs-tail  { outline: 2.5px solid #c05e1b; }
.fifo-legend { display: flex; gap: 16px; padding: 4px 12px 10px; font-size: .75rem; flex-wrap: wrap; }
.fifo-legend-item { display: flex; align-items: center; gap: 5px; color: var(--text-color, #333); }
.fifo-legend-dot { width: 12px; height: 12px; border-radius: 3px; }

/* Performance badges */
.perf-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 1rem 0; }
@media (max-width: 500px) { .perf-grid { grid-template-columns: 1fr; } }
.perf-card { border-radius: 10px; border: 1.5px solid var(--border-color, #e0e0e0); background: var(--card-bg, #fff); padding: 14px; text-align: center; }
.perf-num { font-size: 2rem; font-weight: 800; line-height: 1; margin-bottom: 4px; }
.perf-label { font-size: .78rem; color: var(--light-text, #666); font-family: monospace; }
.perf-sub { font-size: .75rem; color: var(--light-text, #888); margin-top: 4px; }

/* Checklist */
.cl { list-style: none; padding: 0; margin: .5rem 0; }
.cl li {
  display: flex; align-items: flex-start; gap: .6rem;
  padding: .45rem .6rem; font-size: .87rem; color: var(--text-color, #222);
  line-height: 1.5; border-bottom: 1px solid var(--border-color, #f0f0f0);
}
.cl li:last-child { border-bottom: none; }
.cl li::before { content: '☐'; font-size: 1rem; flex-shrink: 0; color: #1a7a6e; margin-top: -.05rem; }

/* Nav */
.mod-nav {
  display: flex; justify-content: space-between; align-items: center;
  flex-wrap: wrap; gap: .8rem; margin-top: 2.5rem;
  padding-top: 1.2rem; border-top: 1px solid var(--border-color, #eee);
}
.mod-nav a {
  display: inline-flex; align-items: center; gap: .4rem;
  padding: .5rem 1rem; border-radius: 7px;
  background: var(--card-bg, #f5f5f5); border: 1px solid var(--border-color, #ddd);
  font-size: .85rem; font-weight: 600; color: var(--text-color, #333) !important;
  text-decoration: none !important; transition: background .15s;
}
.mod-nav a:hover { background: var(--bg-color, #ebebeb); }
.mod-nav .nb { background: #1a3a5c; color: #fff !important; border-color: #1a3a5c; }
.mod-nav .nb:hover { background: #245280; }

/* Section divider */
.sep {
  font-size: .7rem; font-family: monospace; font-weight: 700; letter-spacing: .1em;
  text-transform: uppercase; color: var(--light-text, #888);
  margin: 2rem 0 .8rem; padding-bottom: .35rem;
  border-bottom: 1px solid var(--border-color, #eee);
}

/* two-col grid */
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0; }
@media (max-width: 540px) { .two-col { grid-template-columns: 1fr; } }

/* sequence diagram (handmade) */
.seq-wrap { overflow-x: auto; margin: 1rem 0; }
.seq-table { border-collapse: collapse; min-width: 560px; width: 100%; font-size: .82rem; }
.seq-table th { background: #1a3a5c; color: #fff; padding: .5rem 1rem; text-align: center; font-weight: 700; font-family: monospace; }
.seq-table td { padding: .45rem .8rem; border-bottom: 1px solid var(--border-color, #eee); color: var(--text-color, #222); vertical-align: middle; }
.seq-table tr:nth-child(even) td { background: var(--bg-color, #f8f8f8); }
.seq-dir { text-align: center; font-family: monospace; font-size: .85rem; color: #1a7a6e; font-weight: 700; }
.seq-msg { font-size: .82rem; color: var(--text-color, #333); }
.seq-note { font-size: .75rem; color: var(--light-text, #888); font-style: italic; }
</style>

<!-- ── HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">VPP MASTERY · HOST STACK · BONUS MODULE</div>
  <div class="mod-title">🌐 VPP Host Stack</div>
  <div class="mod-subtitle">TCP &amp; Session Layers - Userspace networking, SVM FIFOs, VCL, Cut-through connections</div>
  <div class="mod-pills">
    <span class="mod-pill">src/vnet/session/</span>
    <span class="mod-pill">src/vnet/tcp/</span>
    <span class="mod-pill">src/svm/</span>
    <span class="mod-pill">src/vcl/</span>
    <span class="mod-pill">200K CPS · 8 Gbps/core</span>
  </div>
</div>

<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">What &amp; Why</button>
  <button class="tab-btn" onclick="vt(event,'t1')">Key Terms</button>
  <button class="tab-btn" onclick="vt(event,'t2')">Architecture</button>
  <button class="tab-btn" onclick="vt(event,'t3')">Session Layer</button>
  <button class="tab-btn" onclick="vt(event,'t4')">SVM FIFOs</button>
  <button class="tab-btn" onclick="vt(event,'t5')">TCP</button>
  <button class="tab-btn" onclick="vt(event,'t6')">VCL</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Connection Flow</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Cut-through</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Multi-threading</button>
  <button class="tab-btn" onclick="vt(event,'ta')">Checklist</button>
</div>


<!-- ════════════ TAB 0 - WHAT & WHY ════════════ -->
<div id="t0" class="tab-pane active">
<p class="sep">THE PROBLEM IT SOLVES</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Why Traditional Networking is Slow for High-Performance Apps</h3><span class="tag tag-blue">MOTIVATION</span></div>
  <div class="cp-body">
    <p>In the standard Linux model, every network operation - <code>send()</code>, <code>recv()</code>, <code>connect()</code> - crosses the <strong>kernel boundary</strong>. This means:</p>
    <ul>
      <li><strong>System call overhead:</strong> Each <code>send()</code> traps into the kernel, switches CPU context, runs kernel TCP code, copies data to a kernel socket buffer, then returns. At 10 Gbps line rate this becomes the bottleneck.</li>
      <li><strong>Data copies:</strong> Data moves from your app buffer → kernel socket buffer → NIC DMA buffer. Multiple copies per packet.</li>
      <li><strong>Cache pollution:</strong> Kernel code runs on the same CPU cores, evicting your application's data from L1/L2 cache.</li>
      <li><strong>Scheduling jitter:</strong> The kernel may deschedule your process at any moment, adding microseconds of latency.</li>
    </ul>
    <p>VPP's host stack eliminates all of this. The <strong>entire TCP/IP stack runs inside VPP's userspace process</strong>. Applications communicate with it via shared memory FIFOs - no syscalls, no copies, no kernel crossing on the data path.</p>
  </div>
</div>

<div class="two-col">
  <div class="cp p-red" style="margin:0">
    <div class="cp-hdr"><span class="ico">🐢</span><h3>Traditional Model</h3><span class="tag tag-red">SLOW PATH</span></div>
    <div class="cp-body">
      <p><strong>App calls send()</strong> → syscall trap → kernel TCP → kernel socket buffer → NIC driver → DMA → wire</p>
      <p><strong>Data path crosses:</strong> user/kernel boundary × 2, 2–3 memory copies, context switches, scheduler jitter</p>
      <p><strong>Ceiling:</strong> ~1–5 Gbps per core with significant CPU load</p>
    </div>
  </div>
  <div class="cp p-green" style="margin:0">
    <div class="cp-hdr"><span class="ico">⚡</span><h3>VPP Host Stack</h3><span class="tag tag-green">FAST PATH</span></div>
    <div class="cp-body">
      <p><strong>App writes to TX FIFO</strong> → VPP reads shared memory → TCP → IP → DPDK → DMA → wire</p>
      <p><strong>Data path crosses:</strong> shared memory write only, zero copies, no kernel, no syscalls</p>
      <p><strong>Demonstrated:</strong> 8 Gbps/core, 200K connections/sec (2017 numbers - much higher on modern HW)</p>
    </div>
  </div>
</div>

<div class="perf-grid">
  <div class="perf-card">
    <div class="perf-num" style="color:#1a7a6e">200K</div>
    <div class="perf-label">connections/sec</div>
    <div class="perf-sub">on a single Intel Xeon E2690</div>
  </div>
  <div class="perf-card">
    <div class="perf-num" style="color:#1a3a5c">8 Gbps</div>
    <div class="perf-label">throughput per core</div>
    <div class="perf-sub">normal TCP sessions</div>
  </div>
  <div class="perf-card">
    <div class="perf-num" style="color:#c05e1b">~120 Gbps</div>
    <div class="perf-label">cut-through mode</div>
    <div class="perf-sub">memory bandwidth limit</div>
  </div>
  <div class="perf-card">
    <div class="perf-num" style="color:#5b3a8c">0</div>
    <div class="perf-label">syscalls on data path</div>
    <div class="perf-sub">pure shared memory</div>
  </div>
</div>

</div>


<!-- ════════════ TAB 1 - KEY TERMS ════════════ -->
<div id="t1" class="tab-pane">
<p class="sep">BEGINNER VOCABULARY - KNOW THESE BEFORE GOING DEEPER</p>

<div class="term-grid">

  <div class="term-row">
    <span class="term-name">userspace TCP stack</span>
    <span class="term-def">Normally TCP/IP lives inside the Linux kernel. A "userspace stack" means VPP implements its own complete TCP state machine as a regular process - no kernel involvement in packet processing. Your application doesn't use kernel sockets at all.</span>
  </div>

  <div class="term-row">
    <span class="term-name">shared memory</span>
    <span class="term-def">Two processes map the same physical RAM pages into their own virtual address spaces. Process A writes bytes at address 0x7f000000; Process B reads those same bytes at whatever address it mapped them to. Zero copies, zero kernel involvement - just memory reads and writes.</span>
  </div>

  <div class="term-row">
    <span class="term-name">SVM</span>
    <span class="term-def">Shared Virtual Memory. VPP's allocator for shared memory regions. An SVM segment is a named, fixed-size chunk of shared memory. Multiple SVM segments can exist simultaneously - one per application namespace, or one per application. Source: <code>src/svm/</code></span>
  </div>

  <div class="term-row">
    <span class="term-name">FIFO</span>
    <span class="term-def">First In First Out. A ring buffer - bytes written at the head are read from the tail in order. In VPP host stack, every TCP session has two FIFOs allocated inside a shared memory segment: one for data flowing VPP→App (RX FIFO) and one for App→VPP (TX FIFO).</span>
  </div>

  <div class="term-row">
    <span class="term-name">lock-free</span>
    <span class="term-def">The FIFO can be written and read simultaneously by two threads (VPP worker and app) without mutex locks. This works because each FIFO has exactly one writer and one reader - SPSC (single producer single consumer). Atomic operations on head/tail pointers ensure consistency without blocking.</span>
  </div>

  <div class="term-row">
    <span class="term-name">Binary API</span>
    <span class="term-def">VPP's control-plane message protocol. Structured binary messages sent over a Unix socket or shared memory queue. Used for control operations: create a session, bind a port, connect, set options. NOT used for packet data - that goes through SVM FIFOs. Like the difference between a REST API (control) and a database file (data).</span>
  </div>

  <div class="term-row">
    <span class="term-name">session (vs connection)</span>
    <span class="term-def">VPP uses "session" as the generic term for an endpoint-to-endpoint communication channel, regardless of transport protocol (TCP, UDP, TLS, QUIC). A TCP session wraps a TCP connection. The session layer manages all sessions uniformly; the transport layer (TCP) handles the specific protocol.</span>
  </div>

  <div class="term-row">
    <span class="term-name">5-tuple</span>
    <span class="term-def">The 5 fields that uniquely identify a TCP/UDP flow: source IP, source port, destination IP, destination port, protocol. VPP's session lookup table maps 5-tuple → session object in O(1) using a bihash. Every arriving packet is looked up by its 5-tuple to find the right session and FIFO.</span>
  </div>

  <div class="term-row">
    <span class="term-name">VCL</span>
    <span class="term-def">VPP Communications Library. A C library that applications link against. It provides POSIX-socket-like functions (vcl_connect, vcl_read, vcl_write, vcl_epoll_wait) that talk to VPP's session layer via Binary API and SVM FIFOs instead of calling into the kernel.</span>
  </div>

  <div class="term-row">
    <span class="term-name">LD_PRELOAD</span>
    <span class="term-def">A Linux environment variable that forces the dynamic linker to load a specified shared library before all others. VCL provides an LD_PRELOAD library (<code>libvcl_ldpreload.so</code>) that intercepts standard POSIX socket calls (connect, send, recv, epoll_wait) and redirects them to VPP - without modifying or recompiling the application. nginx can use VPP's stack with just <code>LD_PRELOAD=libvcl_ldpreload.so nginx</code>.</span>
  </div>

  <div class="term-row">
    <span class="term-name">namespace</span>
    <span class="term-def">VPP session namespaces isolate network resources between applications. Each namespace has its own local session lookup table and can be associated with a specific VRF (routing table). App A in namespace 1 cannot see App B's sessions in namespace 2, even though they share the same VPP instance. Think of it like Linux network namespaces, but inside VPP.</span>
  </div>

  <div class="term-row">
    <span class="term-name">cut-through (redirect)</span>
    <span class="term-def">When a server application advertises itself as a cut-through target, VPP can redirect a new client connection directly to the server's shared memory segment - bypassing TCP entirely for the data path. The client writes to what it thinks is a TCP socket; the bytes appear directly in the server's RX FIFO. Throughput is limited only by memory bandwidth (~120 Gbps).</span>
  </div>

  <div class="term-row">
    <span class="term-name">NewReno</span>
    <span class="term-def">A TCP congestion control algorithm. When packet loss is detected, NewReno reduces the sending window size and slowly increases it again. VPP implements NewReno as its baseline congestion control, plus SACK-based fast recovery. You don't need to tune this for most use cases, but knowing it exists matters for latency-sensitive workloads.</span>
  </div>

  <div class="term-row">
    <span class="term-name">SACK</span>
    <span class="term-def">Selective Acknowledgement. A TCP extension where the receiver tells the sender exactly which segments it has received (not just the highest in-order byte). This allows the sender to retransmit only the missing segments rather than everything after a loss. VPP's TCP implementation supports SACK for efficient loss recovery.</span>
  </div>

</div>
</div>


<!-- ════════════ TAB 2 - ARCHITECTURE ════════════ -->
<div id="t2" class="tab-pane">
<p class="sep">FULL STACK ARCHITECTURE</p>

<div class="arch-stack">
  <div class="arch-layer al-app">
    <div class="arch-layer-name">Application</div>
    <div class="arch-layer-sub">Your process (nginx, iperf, custom app). Links against VCL or uses LD_PRELOAD.</div>
  </div>
  <div class="arch-sep">↕ &nbsp;vcl_connect / vcl_read / vcl_write &nbsp;↕</div>
  <div class="arch-layer al-vcl">
    <div class="arch-layer-name">VCL - VPP Communications Library</div>
    <div class="arch-layer-sub">src/vcl/ · POSIX-like API · LD_PRELOAD intercept · epoll shim</div>
  </div>
  <div class="arch-sep">↕ &nbsp;Binary API messages (control only) &nbsp;↕</div>
  <div class="arch-layer al-binapi" style="background:var(--bg-color,#f5f5f5)">
    <div class="arch-layer-name" style="color:var(--light-text,#666);font-size:.8rem">- VPP process boundary - shared memory segment allocated here —</div>
  </div>
  <div class="arch-layer al-session">
    <div class="arch-layer-name">Session Layer</div>
    <div class="arch-layer-sub">src/vnet/session/ · App state · SVM FIFO alloc · 5-tuple lookup · namespaces · pluggable transport</div>
  </div>
  <div class="arch-sep">↕ &nbsp;session_tx_fifo / session_rx_fifo &nbsp;↕</div>
  <div class="arch-layer al-tcp">
    <div class="arch-layer-name">TCP (clean-slate userspace)</div>
    <div class="arch-layer-sub">src/vnet/tcp/ · Full state machine · NewReno · SACK · retransmit timers · checksum offload</div>
  </div>
  <div class="arch-sep">↕ &nbsp;ip4-lookup / ip4-rewrite graph nodes &nbsp;↕</div>
  <div class="arch-layer al-ip">
    <div class="arch-layer-name">IP / vnet</div>
    <div class="arch-layer-sub">FIB lookup · routing · adjacency rewrite</div>
  </div>
  <div class="arch-sep">↕ &nbsp;dpdk-input / dpdk-output &nbsp;↕</div>
  <div class="arch-layer al-dpdk">
    <div class="arch-layer-name">DPDK / NIC driver</div>
    <div class="arch-layer-sub">Physical NIC · hugepages · zero-copy mbuf RX/TX</div>
  </div>
</div>

<div class="ins">
  <p>💡 <strong>Key insight - two independent paths:</strong> The Binary API (control plane) and the SVM FIFOs (data plane) are completely separate. The Binary API is used only for setup: creating sessions, binding ports, setting options - think of it like the control socket. The SVM FIFOs are the actual data highway - once a session is established, the app and VPP only talk through shared memory reads/writes. No Binary API messages on the hot path.</p>
</div>

<p class="sep">SOURCE DIRECTORY MAP</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📁</span><h3>Where the Code Lives</h3><span class="tag tag-blue">SOURCE</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cs">src/vnet/session/</span>   <span class="cm"># Session layer: session.c, session_api.c, application.c</span>
<span class="cs">src/vnet/tcp/</span>       <span class="cm"># TCP implementation: tcp.c, tcp_input.c, tcp_output.c</span>
                    <span class="cm">#   tcp_cc.c (congestion control), tcp_timer.c</span>
<span class="cs">src/svm/</span>            <span class="cm"># Shared Virtual Memory: svm_fifo.c, fifo_segment.c</span>
<span class="cs">src/vcl/</span>            <span class="cm"># VCL library: vcl_private.c, vppcom.c, ldp.c (LD_PRELOAD)</span>
<span class="cs">src/vnet/session/</span>   <span class="cm"># Binary API: session.api</span></pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 3 - SESSION LAYER ════════════ -->
<div id="t3" class="tab-pane">
<p class="sep">SESSION LAYER - src/vnet/session/</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🗂️</span><h3>What the Session Layer Manages</h3><span class="tag tag-blue">OVERVIEW</span></div>
  <div class="cp-body">
    <p>The session layer sits between transport protocols (TCP, UDP, TLS, QUIC) and applications. It is the broker that connects "application wants to receive data on port 8080" with "TCP received bytes for the flow matching (srcIP:srcPort → dstIP:8080)".</p>
    <p>It owns five responsibilities:</p>
    <ul>
      <li><strong>Application registration:</strong> When an app attaches via Binary API, the session layer creates an <code>application_t</code> object and maps it to a namespace and set of permissions.</li>
      <li><strong>Session allocation:</strong> For every accepted TCP connection, one <code>session_t</code> object is allocated (from a pool), and two SVM FIFOs are allocated (RX and TX) inside the app's shared memory segment.</li>
      <li><strong>Lookup tables:</strong> Two bihash tables - a global table (keyed by 5-tuple) for ingress matching, and a local table (keyed by local endpoint) for bind/accept matching.</li>
      <li><strong>Namespace isolation:</strong> Each namespace has its own local session table and can be pinned to a VRF. Apps in different namespaces cannot see each other's sessions.</li>
      <li><strong>Transport abstraction:</strong> The session layer defines a transport protocol interface (<code>session_transport_vft_t</code>) - TCP, UDP, TLS, QUIC all register themselves. New transport protocols can be added as plugins.</li>
    </ul>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Session Lookup Tables - Two-Table Design</h3><span class="tag tag-teal">INTERNALS</span></div>
  <div class="cp-body">

<div class="cb"><pre><span class="cm">/* Two lookup tables - different key spaces */</span>

<span class="cm">/* Global session table: ingress packet → active session */</span>
<span class="cm">/* Key: full 5-tuple (src_ip, src_port, dst_ip, dst_port, proto) */</span>
<span class="cm">/* Value: session index */</span>
<span class="cm">/* Used by: ip4-lookup → session-queue node (data path) */</span>
session_table_t *global_table = &session_main.session_tables[fib_index];

<span class="cm">/* Local session table: per-namespace, for listen/bind */</span>
<span class="cm">/* Key: local endpoint (dst_ip, dst_port, proto) */</span>
<span class="cm">/* Value: listen session index (which app is listening here?) */</span>
<span class="cm">/* Used by: TCP SYN processing - find who owns this port */</span>
session_table_t *local_table = &ns->local_session_table;

<span class="cm">/* Fast-path lookup (called per packet in session-queue node) */</span>
session_t *s = session_lookup_connection_wt4(fib_index,
    &ip4_hdr->src_address, &ip4_hdr->dst_address,
    tcp_hdr->src_port, tcp_hdr->dst_port,
    TRANSPORT_PROTO_TCP);

<span class="cm">/* Both tables are backed by bihash_48_8 */</span>
<span class="cm">/* 48-byte key: 4+4 byte IPs + 2+2 ports + 1 proto + padding */</span></pre></div>

    <p>The two-table design also supports <strong>session rules</strong> - filter rules attached to either table:</p>
    <ul>
      <li><strong>Local table rules</strong> - namespace-specific, used for egress filtering (which apps can connect out)</li>
      <li><strong>Global table rules</strong> - VRF-specific, used for ingress filtering (which connections are accepted into a namespace)</li>
    </ul>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔌</span><h3>Transport Protocol Plugin Interface</h3><span class="tag tag-orange">EXTENSIBILITY</span></div>
  <div class="cp-body">
    <p>Any transport protocol registers itself with the session layer by implementing <code>session_transport_vft_t</code>. This is a vtable of function pointers - the session layer calls these without knowing which protocol it's talking to.</p>
<div class="cb"><pre><span class="ck">typedef struct</span> {
    <span class="cm">/* Connection management */</span>
    <span class="ck">u32</span>  (*open)  (transport_endpoint_cfg_t *tep);
    void (*close) (u32 conn_index, u32 thread_index);
    void (*reset) (u32 conn_index, u32 thread_index);

    <span class="cm">/* Data transfer */</span>
    u32  (*push_header) (transport_connection_t *tc, vlib_buffer_t **b, u32 n);
    u16  (*send_mss)    (transport_connection_t *tc);

    <span class="cm">/* Introspection */</span>
    transport_connection_t *(*get_connection)(u32 idx, u32 thread);
    u8  *(*format_connection)(u8 *s, va_list *args);
} transport_proto_vft_t;

<span class="cm">/* Registration (in TCP plugin init) */</span>
transport_register_protocol(TRANSPORT_PROTO_TCP, &tcp_proto, FIB_PROTOCOL_IP4, ~0);
transport_register_protocol(TRANSPORT_PROTO_TCP, &tcp_proto, FIB_PROTOCOL_IP6, ~0);</pre></div>
    <p>This is why VPP can support TCP, UDP, TLS (via OpenSSL/mbedTLS plugins), QUIC (via quicly), and custom protocols - they all plug into the same session layer infrastructure.</p>
  </div>
</div>
</div>


<!-- ════════════ TAB 4 - SVM FIFOs ════════════ -->
<div id="t4" class="tab-pane">
<p class="sep">SVM FIFOs - src/svm/svm_fifo.c</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>What a FIFO Looks Like in Memory</h3><span class="tag tag-teal">INTERNALS</span></div>
  <div class="cp-body">
    <p>An SVM FIFO is a ring buffer allocated inside a shared memory segment. Two processes - VPP's dataplane worker and the application - access it simultaneously, with no locks. Safety comes from the SPSC (Single Producer Single Consumer) guarantee: exactly one writer advances the head, exactly one reader advances the tail.</p>

    <!-- VISUAL FIFO DIAGRAM -->
    <div class="fifo-wrap">
      <div class="fifo-hdr">RX FIFO - session 42 - 64 KB - VPP writes (head) · App reads (tail)</div>
      <div class="fifo-ring">
        <div class="fifo-slot fs-empty">—</div>
        <div class="fifo-slot fs-empty">—</div>
        <div class="fifo-slot fs-data fs-tail">data</div>
        <div class="fifo-slot fs-data">data</div>
        <div class="fifo-slot fs-data">data</div>
        <div class="fifo-slot fs-data">data</div>
        <div class="fifo-slot fs-data fs-head">data</div>
        <div class="fifo-slot fs-empty">—</div>
      </div>
      <div class="fifo-legend">
        <div class="fifo-legend-item"><div class="fifo-legend-dot" style="background:#d0e8f8;border:1.5px solid #b5d4f4"></div> Data (5 segments)</div>
        <div class="fifo-legend-item"><div class="fifo-legend-dot" style="background:var(--bg-color,#f5f5f5);border:1px solid var(--border-color,#ddd)"></div> Empty</div>
        <div class="fifo-legend-item"><div class="fifo-legend-dot" style="outline:2.5px solid #1a7a6e;background:transparent"></div> Head (VPP writes here next)</div>
        <div class="fifo-legend-item"><div class="fifo-legend-dot" style="outline:2.5px solid #c05e1b;background:transparent"></div> Tail (App reads from here)</div>
      </div>
    </div>

<div class="cb"><pre><span class="ck">typedef struct</span> svm_fifo {
    CLIB_CACHE_LINE_ALIGN_MARK(cacheline0);
    <span class="ck">atomic_u32</span> head;          <span class="cm">/* consumer (app) advances this */</span>
    <span class="ck">atomic_u32</span> tail;          <span class="cm">/* producer (VPP) advances this */</span>
    <span class="ck">u32</span>  size;                <span class="cm">/* ring capacity in bytes */</span>
    <span class="ck">u32</span>  nitems;              <span class="cm">/* number of items (size / chunk) */</span>
    <span class="ck">u8</span>  *data;                <span class="cm">/* pointer into shared memory region */</span>
    <span class="ck">u32</span>  master_session_index;<span class="cm">/* which session owns this FIFO */</span>
    <span class="ck">u8</span>   master_thread_index; <span class="cm">/* worker thread that manages it */</span>
    svm_fifo_chunk_t *ooo_enqueues; <span class="cm">/* out-of-order data list */</span>
} svm_fifo_t;</pre></div>

    <p><strong>Important design properties:</strong></p>
    <ul>
      <li><strong>Fixed position in shared memory:</strong> Once allocated, a FIFO never moves. The app holds a pointer to it from the moment the session is established.</li>
      <li><strong>Out-of-order support:</strong> TCP can receive segments out of order. The FIFO supports enqueueing OOO data directly - VPP enqueues each TCP segment at its byte-offset position. When the gap fills, the FIFO contiguous range advances.</li>
      <li><strong>Lock-free dequeue with option to peek:</strong> The app can peek at data without consuming it - useful for protocols where you need to inspect a header before deciding how much to read.</li>
      <li><strong>Atomic size increment:</strong> While head/tail are advanced with plain writes (safe due to SPSC), the total available bytes counter uses an atomic increment to allow safe multi-threaded introspection.</li>
    </ul>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📦</span><h3>SVM Segment - The Shared Memory Container</h3><span class="tag tag-purple">MEMORY MODEL</span></div>
  <div class="cp-body">
    <p>FIFOs are allocated inside an <strong>SVM segment</strong> - a named, fixed-size region of shared memory created with <code>shm_open</code> + <code>mmap</code>. The segment is created by VPP and mapped into both the VPP process and the application process at session establishment time.</p>

<div class="cb"><pre><span class="cm">/* Segment creation (VPP side, triggered by app attach) */</span>
fifo_segment_create_args_t a = {
    .segment_name = <span class="cs">"app-42-segment"</span>,
    .segment_size = 64 << 20,   <span class="cm">/* 64 MB */</span>
    .segment_type = SSVM_SEGMENT_SHM,
};
fifo_segment_create(sm, &a);

<span class="cm">/* App maps the segment (VCL side) */</span>
ssvm_slave_init_shm(sh);  <span class="cm">/* mmap's the segment into the app's VA space */</span>

<span class="cm">/* After mmap: both sides hold pointers to the same physical pages */</span>
svm_fifo_t *rx_fifo = session->rx_fifo;   <span class="cm">/* VPP's pointer */</span>
svm_fifo_t *rx_fifo = vcl_session->rx_fifo; <span class="cm">/* App's pointer - same memory */</span>

<span class="cm">/* Write (VPP, on packet receive): */</span>
svm_fifo_enqueue(s->rx_fifo, b->current_length,
                 vlib_buffer_get_current(b));

<span class="cm">/* Read (app, via VCL): */</span>
n = svm_fifo_dequeue(vcl_s->rx_fifo, buf_len, buf);</pre></div>

    <div class="warn">
      <p>⚠️ <strong>Segment size tuning:</strong> The segment is allocated at app attach time and its size is fixed. If your app's sessions have large buffers (e.g., 1 MB RX FIFO per connection) and you have many concurrent connections, segment exhaustion is a common issue. Tune via: <code>session { evt-q-length 64  segment-size 256m  add-segment-size 128m }</code> in startup.conf.</p>
    </div>
  </div>
</div>
</div>


<!-- ════════════ TAB 5 - TCP ════════════ -->
<div id="t5" class="tab-pane">
<p class="sep">VPP TCP - src/vnet/tcp/</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📡</span><h3>Clean-Slate TCP Implementation</h3><span class="tag tag-teal">OVERVIEW</span></div>
  <div class="cp-body">
    <p>VPP implements TCP from scratch - it does not use any Linux kernel TCP code. This was a deliberate choice: the kernel's TCP is optimised for general-purpose use across millions of different scenarios. VPP's TCP is optimised for high throughput with many concurrent connections in a polling dataplane.</p>
    <p><strong>What it implements:</strong></p>
    <ul>
      <li><strong>Full state machine:</strong> CLOSED → SYN_SENT → SYN_RCVD → ESTABLISHED → FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT → CLOSED (and all error transitions)</li>
      <li><strong>Flow control:</strong> Sliding window, window scaling (RFC 7323), receive window advertisement</li>
      <li><strong>Congestion control:</strong> NewReno (default), with a pluggable congestion control interface for cubic, BBR, etc.</li>
      <li><strong>Loss recovery:</strong> Fast retransmit, fast recovery, RTO-based retransmission, SACK-based selective retransmit</li>
      <li><strong>Timers:</strong> RTO (retransmission timeout), persist, keepalive, TIME_WAIT - all implemented on VPP's timer wheel infrastructure (<code>tw_timer_*</code>)</li>
      <li><strong>Checksum offloading:</strong> Delegates to DPDK TX offload when hardware supports it</li>
      <li><strong>PMTU discovery:</strong> Path MTU discovery via ICMP unreachable handling</li>
      <li><strong>TSO:</strong> TCP Segmentation Offload on supporting NICs</li>
    </ul>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📊</span><h3>TCP in the VPP Graph - Node Chain</h3><span class="tag tag-blue">GRAPH NODES</span></div>
  <div class="cp-body">
    <p>TCP processing is decomposed into graph nodes like everything else in VPP. The RX and TX paths are separate node chains:</p>

<div class="cb"><pre><span class="cm">/* RX path (incoming segment) */</span>
dpdk-input
  → ethernet-input
    → ip4-input
      → ip4-lookup            <span class="cm">/* FIB lookup → local delivery */</span>
        → ip4-local           <span class="cm">/* dst is local → demux by proto */</span>
          → tcp4-input        <span class="cm">/* TCP header validation */</span>
            → tcp4-established <span class="cm">/* ESTABLISHED state: enqueue to rx_fifo */</span>
            → tcp4-syn-sent    <span class="cm">/* SYN_SENT state: process SYN-ACK */</span>
            → tcp4-rcv-process <span class="cm">/* other states: FIN, RST processing */</span>
              → session-queue  <span class="cm">/* notify app: data available on rx_fifo */</span>

<span class="cm">/* TX path (app writes to tx_fifo) */</span>
session-queue                  <span class="cm">/* reads from tx_fifo */</span>
  → tcp4-output                <span class="cm">/* build TCP segment, set headers */</span>
    → ip4-rewrite              <span class="cm">/* L3 rewrite */</span>
      → dpdk-output</pre></div>

    <p>The <strong>session-queue</strong> node is the bridge between the session layer and the graph. On the RX side it notifies the application of new data. On the TX side it reads from the TX FIFO and passes data to TCP for segmentation and transmission.</p>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">⏱️</span><h3>TCP Timers - Timer Wheel Integration</h3><span class="tag tag-orange">INTERNALS</span></div>
  <div class="cp-body">
    <p>VPP's TCP uses the <code>tw_timer</code> wheel infrastructure from vppinfra. Each TCP connection can have multiple concurrent timers (RTO, persist, keepalive, TIME_WAIT). The timer wheel fires callbacks at O(1) per tick regardless of how many active timers exist.</p>
<div class="cb"><pre><span class="cm">/* Timer types per connection */</span>
<span class="ck">typedef enum</span> {
    TCP_TIMER_RETRANSMIT = 0,  <span class="cm">/* RTO: retransmit if no ACK received */</span>
    TCP_TIMER_DELACK,          <span class="cm">/* delayed ACK: batch ACKs for efficiency */</span>
    TCP_TIMER_PERSIST,         <span class="cm">/* zero-window probe */</span>
    TCP_TIMER_KEEPALIVE,       <span class="cm">/* detect dead connections */</span>
    TCP_TIMER_WAITCLOSE,       <span class="cm">/* TIME_WAIT expiry */</span>
    TCP_TIMER_RETRANSMIT_SYN,  <span class="cm">/* SYN retransmit before connection est. */</span>
    TCP_N_TIMERS,
} tcp_timers_e;

<span class="cm">/* Starting a timer (inside TCP processing) */</span>
tcp_timer_set(tc, TCP_TIMER_RETRANSMIT,
              clib_max(tc->rto * TCP_TO_TIMER_TICK, 1));
<span class="cm">/* tc->rto is in ms; TCP_TO_TIMER_TICK converts to wheel ticks */</span>

<span class="cm">/* Timer callback (fires on expiry) */</span>
<span class="ck">static void</span> tcp_timer_retransmit_handler(u32 conn_index) {
    tcp_connection_t *tc = tcp_connection_get(conn_index, vlib_get_thread_index());
    <span class="cm">/* double RTO (exponential backoff), retransmit */</span>
    tc->rto = clib_min(tc->rto << 1, TCP_RTO_MAX);
    tcp_retransmit_first_unacked(tc);
}</pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 6 - VCL ════════════ -->
<div id="t6" class="tab-pane">
<p class="sep">VCL - VPP COMMUNICATIONS LIBRARY - src/vcl/</p>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔌</span><h3>What VCL Is and Why It Exists</h3><span class="tag tag-purple">OVERVIEW</span></div>
  <div class="cp-body">
    <p>VCL is the application-side library that hides all VPP host stack complexity behind a clean API. Without VCL, an application would need to: implement the Binary API wire format, manage its own shared memory segment mappings, handle FIFO enqueue/dequeue directly, and implement epoll on top of FIFO state. VCL does all of this.</p>
    <p>VCL provides two integration modes:</p>
    <ul>
      <li><strong>Native VCL API:</strong> Application calls <code>vppcom_*</code> functions directly. Maximum control and performance. Requires modifying the application.</li>
      <li><strong>LD_PRELOAD (ldpreload.c):</strong> VCL intercepts POSIX socket calls at the dynamic linker level. Zero code changes needed - but some advanced socket features (like <code>SO_REUSEPORT</code>) may not be supported.</li>
    </ul>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📋</span><h3>Native VCL API Reference</h3><span class="tag tag-blue">API</span></div>
  <div class="cp-body">

<table class="t-table">
  <thead><tr><th>VCL Function</th><th>POSIX Equivalent</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td><code>vppcom_app_create()</code></td><td>—</td><td>Attach to VPP via Binary API. Must be called first.</td></tr>
    <tr><td><code>vppcom_session_create()</code></td><td><code>socket()</code></td><td>Allocate a VCL session object. Returns session handle (integer).</td></tr>
    <tr><td><code>vppcom_session_bind()</code></td><td><code>bind()</code></td><td>Register local endpoint with session layer.</td></tr>
    <tr><td><code>vppcom_session_listen()</code></td><td><code>listen()</code></td><td>Register listen session in local session table.</td></tr>
    <tr><td><code>vppcom_session_accept()</code></td><td><code>accept()</code></td><td>Dequeue next accepted connection. Blocks until one arrives (or non-blocking).</td></tr>
    <tr><td><code>vppcom_session_connect()</code></td><td><code>connect()</code></td><td>Trigger TCP SYN via Binary API; waits for session established event.</td></tr>
    <tr><td><code>vppcom_session_read()</code></td><td><code>read()</code></td><td>Dequeue bytes from RX FIFO. Zero-copy if using peek + advance.</td></tr>
    <tr><td><code>vppcom_session_write()</code></td><td><code>write()</code></td><td>Enqueue bytes into TX FIFO. Returns bytes written.</td></tr>
    <tr><td><code>vppcom_epoll_create()</code></td><td><code>epoll_create()</code></td><td>Create an epoll handle backed by VPP session events.</td></tr>
    <tr><td><code>vppcom_epoll_ctl()</code></td><td><code>epoll_ctl()</code></td><td>Add/remove/modify session monitoring.</td></tr>
    <tr><td><code>vppcom_epoll_wait()</code></td><td><code>epoll_wait()</code></td><td>Block until events (EPOLLIN, EPOLLOUT) on any monitored session.</td></tr>
    <tr><td><code>vppcom_session_close()</code></td><td><code>close()</code></td><td>Close session; sends TCP FIN if established.</td></tr>
  </tbody>
</table>

<div class="cb"><pre><span class="cm">/* Minimal VCL server skeleton */</span>
vppcom_app_create(<span class="cs">"my-server"</span>);

<span class="ck">int</span> ls = vppcom_session_create(VPPCOM_PROTO_TCP, 0 <span class="cm">/* is_nonblocking */</span>);
vppcom_session_bind(ls, &ep);     <span class="cm">/* ep = { .is_ip4=1, .ip=..., .port=8080 } */</span>
vppcom_session_listen(ls, 10);

<span class="ck">while</span> (1) {
    <span class="ck">int</span> cs = vppcom_session_accept(ls, &client_ep, 0);
    <span class="cm">/* cs is the connected session handle */</span>

    <span class="ck">char</span> buf[4096];
    <span class="ck">int</span> n = vppcom_session_read(cs, buf, <span class="ck">sizeof</span>(buf));
    <span class="cm">/* buf now contains TCP payload - read directly from RX FIFO */</span>
    
    vppcom_session_write(cs, response, resp_len);
    vppcom_session_close(cs);
}</pre></div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🎭</span><h3>LD_PRELOAD - Zero-Code-Change Integration</h3><span class="tag tag-orange">LD_PRELOAD</span></div>
  <div class="cp-body">
    <p>The LD_PRELOAD library (<code>src/vcl/ldp.c</code>) wraps every relevant POSIX socket function. When the dynamic linker loads a program, it loads this library first, so calls to <code>connect()</code>, <code>send()</code>, <code>recv()</code> etc. hit the VCL wrapper, not libc.</p>

<div class="cb"><pre><span class="cm"># Run nginx against VPP's stack - no code changes to nginx</span>
export VCL_CONFIG=/etc/vpp/vcl.conf
LD_PRELOAD=/usr/lib/libvcl_ldpreload.so nginx -g "daemon off;"

<span class="cm"># Run iperf3 as server against VPP's stack</span>
LD_PRELOAD=/usr/lib/libvcl_ldpreload.so iperf3 -s -p 5201

<span class="cm"># Run iperf3 as client, connecting to a VPP host-stack server</span>
LD_PRELOAD=/usr/lib/libvcl_ldpreload.so iperf3 -c 10.0.0.1 -p 5201 -t 10</pre></div>

<div class="cb"><pre><span class="cm">/* How the interception works (ldp.c) */</span>
<span class="cm">/* The shim re-defines connect() with the same signature as libc */</span>
<span class="ck">int</span> connect(<span class="ck">int</span> fd, <span class="ck">const struct</span> sockaddr *addr, socklen_t len) {
    ldp_worker_ctx_t *ldpw = ldp_worker_get_current();

    <span class="ck">if</span> (ldp_is_vcl_session(fd)) {
        <span class="cm">/* fd belongs to VCL - use VPP's stack */</span>
        <span class="ck">return</span> vppcom_session_connect(fd - LDP_SID_BIT, &ep);
    } else {
        <span class="cm">/* Regular fd - fall through to libc */</span>
        <span class="ck">return</span> libc_connect(fd, addr, len);
    }
}</pre></div>

    <div class="ins">
      <p>💡 <strong>Hybrid mode:</strong> LD_PRELOAD supports a hybrid model - sockets created for non-network purposes (local Unix sockets, pipes, files) continue to use the kernel. Only sockets on the configured IP address/port ranges are redirected to VPP. This allows apps that mix network I/O and file I/O to work without modification.</p>
    </div>
  </div>
</div>
</div>


<!-- ════════════ TAB 7 - CONNECTION FLOW ════════════ -->
<div id="t7" class="tab-pane">
<p class="sep">STEP-BY-STEP: SESSION ESTABLISHMENT &amp; DATA TRANSFER</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🤝</span><h3>Phase 1 - App Attachment</h3><span class="tag tag-blue">SETUP</span></div>
  <div class="cp-body">
    <p>Before any session can be created, both client and server must attach to VPP:</p>
    <div class="flow-list">
      <div class="flow-step" data-n="1" style="--step-color:#1a3a5c">
        <div class="flow-step-body">
          <div class="flow-step-title">App calls vppcom_app_create()</div>
          <div class="flow-step-detail">VCL sends an <code>app_attach</code> Binary API message to VPP. VPP creates an <code>application_t</code> object, assigns a namespace, and allocates a shared memory segment for this app's sessions.</div>
          <div class="flow-step-code">Binary API → app_attach_reply</div>
        </div>
      </div>
      <div class="flow-step" data-n="2" style="--step-color:#1a3a5c">
        <div class="flow-step-body">
          <div class="flow-step-title">VPP returns segment fd</div>
          <div class="flow-step-detail">VPP replies with the shared memory segment descriptor. VCL calls <code>ssvm_slave_init_shm()</code> to mmap the segment into the app's address space. Now both processes share the same physical pages.</div>
          <div class="flow-step-code">mmap(segment_fd) → shared memory mapped</div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📞</span><h3>Phase 2 - Session Establishment (TCP Handshake)</h3><span class="tag tag-teal">CONNECT</span></div>
  <div class="cp-body">

    <div class="seq-wrap">
    <table class="seq-table">
      <thead><tr><th>Server App</th><th>VPP (server side)</th><th>Network</th><th>VPP (client side)</th><th>Client App</th></tr></thead>
      <tbody>
        <tr><td class="seq-msg">bind + listen</td><td class="seq-msg">registers local table entry</td><td></td><td></td><td></td></tr>
        <tr><td></td><td></td><td></td><td></td><td class="seq-msg">connect()</td></tr>
        <tr><td></td><td></td><td></td><td class="seq-msg">allocate TCP conn, SYN</td><td></td></tr>
        <tr><td></td><td></td><td class="seq-dir">──── SYN ────→</td><td></td><td></td></tr>
        <tr><td></td><td class="seq-msg">SYN_RCVD, send SYN-ACK</td><td></td><td></td><td></td></tr>
        <tr><td></td><td></td><td class="seq-dir">←── SYN-ACK ──</td><td></td><td></td></tr>
        <tr><td></td><td></td><td class="seq-dir">──── ACK ────→</td><td class="seq-msg">ESTABLISHED</td><td></td></tr>
        <tr><td></td><td class="seq-msg">ESTABLISHED → alloc FIFOs</td><td></td><td class="seq-msg">alloc FIFOs</td><td></td></tr>
        <tr><td></td><td class="seq-msg">notify app: new session</td><td></td><td></td><td></td></tr>
        <tr><td class="seq-msg">accept() returns</td><td></td><td></td><td></td><td class="seq-msg">connect() returns</td></tr>
        <tr><td class="seq-note" colspan="5" style="text-align:center;padding:.6rem">Both apps now hold a session handle. Two FIFOs (RX + TX) are live in shared memory for each side.</td></tr>
      </tbody>
    </table>
    </div>

    <p>Key point: the TCP handshake (SYN/SYN-ACK/ACK) is handled entirely inside VPP's graph nodes. The <strong>application is not involved</strong> until the handshake completes. Only then does VPP allocate the FIFOs and notify the app via an event message on the Binary API channel.</p>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📦</span><h3>Phase 3 - Data Transfer</h3><span class="tag tag-green">DATA PATH</span></div>
  <div class="cp-body">

    <div class="flow-list">
      <div class="flow-step" data-n="1" style="--step-color:#1e6b3c">
        <div class="flow-step-body">
          <div class="flow-step-title">App writes to TX FIFO</div>
          <div class="flow-step-detail">App calls <code>vppcom_session_write(cs, buf, len)</code>. VCL calls <code>svm_fifo_enqueue(tx_fifo, len, buf)</code> - a pure memory copy into the shared region. No syscall, no kernel crossing.</div>
          <div class="flow-step-code">svm_fifo_enqueue(tx_fifo)</div>
        </div>
      </div>
      <div class="flow-step" data-n="2" style="--step-color:#1e6b3c">
        <div class="flow-step-body">
          <div class="flow-step-title">App sends TX write event</div>
          <div class="flow-step-detail">VCL sends a <code>SESSION_IO_EVT_TX</code> event to VPP's worker thread via the session event queue (a shared memory MPSC queue). This wakes up the <code>session-queue</code> node to process the TX FIFO.</div>
          <div class="flow-step-code">session_event_queue → SESSION_IO_EVT_TX</div>
        </div>
      </div>
      <div class="flow-step" data-n="3" style="--step-color:#1e6b3c">
        <div class="flow-step-body">
          <div class="flow-step-title">VPP reads TX FIFO, builds TCP segments</div>
          <div class="flow-step-detail">The <code>session-queue</code> node dequeues the TX event, reads bytes from the TX FIFO, passes them to TCP output, which builds TCP segments respecting MSS, window size, and congestion window. Segments enter the graph at <code>tcp4-output</code>.</div>
          <div class="flow-step-code">svm_fifo_dequeue(tx_fifo) → tcp4-output → dpdk-output</div>
        </div>
      </div>
      <div class="flow-step" data-n="4" style="--step-color:#1e6b3c">
        <div class="flow-step-body">
          <div class="flow-step-title">Remote VPP receives, enqueues to RX FIFO</div>
          <div class="flow-step-detail">On the receiving side, <code>tcp4-established</code> processes the segment, enqueues the payload directly into the session's RX FIFO, and sends a <code>SESSION_IO_EVT_RX</code> event to the app.</div>
          <div class="flow-step-code">svm_fifo_enqueue(rx_fifo) → SESSION_IO_EVT_RX</div>
        </div>
      </div>
      <div class="flow-step" data-n="5" style="--step-color:#1e6b3c">
        <div class="flow-step-body">
          <div class="flow-step-title">Remote app reads from RX FIFO</div>
          <div class="flow-step-detail">App's <code>epoll_wait</code> wakes on the RX event. App calls <code>vppcom_session_read()</code> → <code>svm_fifo_dequeue(rx_fifo)</code>. Data is now in the app's buffer. Total copies: 1 (FIFO → app buffer). Zero kernel crossings.</div>
          <div class="flow-step-code">svm_fifo_dequeue(rx_fifo) → app buffer</div>
        </div>
      </div>
    </div>
  </div>
</div>
</div>


<!-- ════════════ TAB 8 - CUT-THROUGH ════════════ -->
<div id="t8" class="tab-pane">
<p class="sep">CUT-THROUGH (REDIRECTED) CONNECTIONS</p>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>What is a Cut-Through Connection?</h3><span class="tag tag-orange">CONCEPT</span></div>
  <div class="cp-body">
    <p>A cut-through connection (also called "redirect" in the VPP source) takes the host stack to its logical extreme. When both the client and server are applications talking to the <em>same VPP instance</em>, VPP can skip TCP entirely for the data path and connect the two apps' shared memory FIFOs directly.</p>
    <p>The flow works like this:</p>
    <ul>
      <li><strong>Server app</strong> calls <code>bind + listen</code> but also sends a <code>redirect</code> message indicating it wants cut-through connections.</li>
      <li><strong>Client app</strong> calls <code>connect</code>. VPP's session layer sees that both endpoints are local applications.</li>
      <li>VPP <strong>redirects</strong> the connection: the client's TX FIFO becomes the server's RX FIFO. They share the same memory region.</li>
      <li>Data written by the client appears in the server's buffer with <strong>zero copies and zero TCP overhead</strong>.</li>
    </ul>
    <p>The throughput ceiling is no longer CPU or NIC speed - it is <strong>memory bandwidth</strong> (typically 80–150 GB/s on modern systems), which gives the ~120 Gbps figure quoted in the presentation.</p>
  </div>
</div>

<div class="two-col">
  <div class="cp p-blue" style="margin:0">
    <div class="cp-hdr"><span class="ico">🔵</span><h3>Normal TCP Session</h3><span class="tag tag-blue">COMPARISON</span></div>
    <div class="cp-body">
      <p>App → TX FIFO → <strong>TCP segment</strong> → IP → NIC TX → wire → NIC RX → IP → <strong>TCP reassembly</strong> → RX FIFO → App</p>
      <p>Each direction: 1 copy + TCP processing (header parsing, ACK, window management, congestion control)</p>
      <p style="margin-top:.8rem;font-size:.85rem"><strong>Performance: ~8 Gbps/core</strong></p>
    </div>
  </div>
  <div class="cp p-green" style="margin:0">
    <div class="cp-hdr"><span class="ico">🟢</span><h3>Cut-Through Connection</h3><span class="tag tag-green">COMPARISON</span></div>
    <div class="cp-body">
      <p>App → <strong>shared FIFO</strong> → App</p>
      <p>No TCP headers. No IP routing. No NIC. No ACK. No congestion control. Pure shared memory reads and writes.</p>
      <p style="margin-top:.8rem;font-size:.85rem"><strong>Performance: ~120 Gbps (memory BW limited)</strong></p>
    </div>
  </div>
</div>

<div class="ins" style="margin-top:1rem">
  <p>💡 <strong>When is cut-through useful?</strong> Any time two services on the same host need to pass large volumes of data between each other: a proxy and an origin server, a load balancer and an application, two stages of a data processing pipeline. In container/pod deployments where both ends run on the same physical node, cut-through gives you essentially in-process performance over a network-like API.</p>
</div>
</div>


<!-- ════════════ TAB 9 - MULTI-THREADING ════════════ -->
<div id="t9" class="tab-pane">
<p class="sep">MULTI-THREADING MODEL</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🧵</span><h3>Session Layer with Multiple Worker Threads</h3><span class="tag tag-teal">THREADING</span></div>
  <div class="cp-body">
    <p>VPP's session layer follows the same per-worker model as the rest of VPP. Each worker thread owns a set of sessions - the sessions whose TCP connections are RSS-hashed to that worker's NIC RX queue. A session's FIFOs are only accessed by its owning worker on the VPP side, and by the application on the app side.</p>

<div class="cb"><pre><span class="cm">/* Session ownership - pinned to worker by RSS hash */</span>
<span class="cm">/* Worker 0 owns sessions hashed to NIC queue 0 */</span>
<span class="cm">/* Worker 1 owns sessions hashed to NIC queue 1 */</span>
<span class="cm">/* etc. */</span>

<span class="cm">/* Per-thread session pools */</span>
session_t **sessions_by_thread;    <span class="cm">/* sessions_by_thread[thread_idx] = pool */</span>
tcp_connection_t **connections;    <span class="cm">/* per-thread TCP connection pool */</span>

<span class="cm">/* Per-worker timer wheels - no shared state */</span>
tw_timer_wheel_2t_1w_2048sl_t *timer_wheels; <span class="cm">/* one per worker */</span>

<span class="cm">/* App event queues - one per app per thread */</span>
<span class="cm">/* VPP workers post RX/TX events here; app polls them */</span>
svm_msg_q_t *app_event_queue[MAX_THREADS];</pre></div>

    <p><strong>The multi-app, multi-thread picture (from the slide deck):</strong></p>
    <ul>
      <li><strong>Core 0:</strong> App1 process + VPP TCP/IP/Session for App1's sessions</li>
      <li><strong>Core 1:</strong> Additional VPP worker handling different sessions (different NIC queue)</li>
      <li>App1 and its VPP sessions may span both cores if RSS distributes its flows to both queues</li>
      <li>Each core has its own FIFO pairs - no locking between cores on the data path</li>
    </ul>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📬</span><h3>App Event Queue - Cross-Boundary Notification</h3><span class="tag tag-blue">EVENTS</span></div>
  <div class="cp-body">
    <p>The app event queue (also in shared memory) is the notification channel from VPP workers to the application. It is an <strong>MPSC queue</strong> (multiple VPP workers can post, one app reads) - so it requires atomic operations, unlike the SPSC FIFOs.</p>

<div class="cb"><pre><span class="ck">typedef struct</span> {
    <span class="ck">u32</span>  session_index;
    <span class="ck">u8</span>   event_type;   <span class="cm">/* SESSION_IO_EVT_RX / TX / CLOSE / etc. */</span>
} session_event_t;

<span class="cm">/* VPP worker posts event when rx_fifo has new data */</span>
session_event_t evt = {
    .session_index = s->session_index,
    .event_type    = SESSION_IO_EVT_RX,
};
svm_msg_q_add(app->event_queue, &evt, SVM_Q_NOWAIT);

<span class="cm">/* App (VCL) polls for events */</span>
<span class="ck">while</span> (1) {
    svm_msg_q_msg_t msg;
    <span class="ck">if</span> (svm_msg_q_sub(eq, &msg, SVM_Q_NOWAIT, 0) == 0) {
        session_event_t *e = svm_msg_q_msg_data(eq, &msg);
        <span class="ck">if</span> (e->event_type == SESSION_IO_EVT_RX)
            notify_app_readable(e->session_index);
        svm_msg_q_free_msg(eq, &msg);
    }
}</pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB A - CHECKLIST ════════════ -->
<div id="ta" class="tab-pane">
<p class="sep">HOST STACK MASTERY CHECKLIST</p>

<ul class="cl">
  <li>Can explain why userspace TCP outperforms kernel TCP for high-connection-count workloads</li>
  <li>Know the two planes: Binary API (control) vs SVM FIFO (data) - and which is used on the hot path</li>
  <li>Understand the layered architecture: App → VCL → [Binary API] → Session → TCP → IP → DPDK</li>
  <li>Know what an SVM segment is and how it is mapped into both VPP and the app process</li>
  <li>Understand the SVM FIFO memory layout: head/tail pointers, ring buffer, out-of-order support</li>
  <li>Know why the FIFO is lock-free: SPSC guarantee - one writer (VPP), one reader (app)</li>
  <li>Understand the session layer's 5 responsibilities: app reg, session alloc, lookup, namespaces, transport abstraction</li>
  <li>Know the two lookup tables: global (5-tuple → active session) and local (endpoint → listen session)</li>
  <li>Understand TCP graph node chain: dpdk-input → ip4-local → tcp4-input → tcp4-established → session-queue</li>
  <li>Know VPP's TCP features: full state machine, NewReno, SACK, tw_timer wheel, checksum offload</li>
  <li>Can list the VCL native API functions and their POSIX equivalents</li>
  <li>Understand how LD_PRELOAD interception works: shim re-defines connect/send/recv, checks fd type</li>
  <li>Can trace a complete session establishment: vppcom_app_create → bind → listen → TCP handshake → FIFO alloc → accept</li>
  <li>Can trace a complete data transfer: write → svm_fifo_enqueue → TX event → tcp4-output → dpdk-output → wire → dpdk-input → tcp4-established → svm_fifo_enqueue → RX event → read</li>
  <li>Understand cut-through connections: direct FIFO sharing, no TCP overhead, ~120 Gbps ceiling</li>
  <li>Know the multi-threading model: per-worker session pools, SPSC FIFOs, MPSC app event queue</li>
  <li>Know startup.conf session stanza: segment-size, evt-q-length, add-segment-size</li>
  <li>Know key source directories: src/vnet/session, src/vnet/tcp, src/svm, src/vcl</li>
</ul>

<div class="ins" style="margin-top:1.2rem;">
  <p>✅ Host Stack module complete. Suggested next steps: run VCL iperf3 against a VPP instance (<code>LD_PRELOAD=libvcl_ldpreload.so iperf3</code>), inspect <code>show session verbose</code> and <code>show tcp statistics</code> while traffic is flowing, then explore <code>src/vnet/tcp/tcp_input.c</code> to trace a SYN through the state machine.</p>
</div>
</div>


<!-- MODULE NAV -->
<div class="mod-nav">
  <a href="/learning/data-plane/vpp/module-p5-controlplane/">← Control Plane</a>
  <a href="/learning/data-plane/vpp/vpp-roadmap/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/data-plane/vpp/">↑ VPP Hub</a>
</div>

<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
</script>
