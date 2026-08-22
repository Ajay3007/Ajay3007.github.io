---
title: "DPDK P1 — Foundation, Architecture & EAL"
description: "DPDK MASTERY · PHASE 1 OF 3 · MODULE A Foundation, Architecture EAL Why DPDK exists · Full software stack · Environment Abstraction Layer · PCIe device binding Ch 1 — Why DPDK…"
domain: data-plane
track: dpdk
order: 1
ownHeader: true
url: /learning/data-plane/dpdk/module-p1-foundation/
---

<style>
:root{--dpdk-blue:#1a3a5c;--dpdk-teal:#1a7a6e;--dpdk-orange:#c05e1b}
.mod-header{background:linear-gradient(135deg,#030d1a 0%,#0a2040 60%,#1a4a70 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#5ab0d0;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#a8cce0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#c8e4f4}
.tab-bar{display:flex;flex-wrap:wrap;gap:0;background:#0a2040;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#5dd0f0;border-bottom-color:#5dd0f0}
.tab-pane{display:none}
.tab-pane.active{display:block}
.p-blue{background:#eaf2fc;border-left:4px solid #2e6da4;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-teal{background:#e8f6f4;border-left:4px solid #1a7a6e;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-orange{background:#fdf0e8;border-left:4px solid #c05e1b;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-slate{background:#f4f6f8;border-left:4px solid #64748b;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-violet{background:#f3f0fc;border-left:4px solid #7c3aed;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
[data-theme=dark] .p-blue{background:#0d1e34;border-color:#4a90d9}
[data-theme=dark] .p-teal{background:#0d2020;border-color:#2a9a8e}
[data-theme=dark] .p-orange{background:#1e0d00;border-color:#e07830}
[data-theme=dark] .p-slate{background:#1a1e24;border-color:#8898aa}
[data-theme=dark] .p-violet{background:#180d30;border-color:#9d6bf0}
.p-blue h4,.p-teal h4,.p-orange h4,.p-slate h4,.p-violet h4{margin:.0 0 .5rem;font-size:.9rem;font-weight:700}
.ins{background:#e8f5e9;border:1px solid #66bb6a;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.warn{background:#fff8e1;border:1px solid #ffca28;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.note{background:#e3f2fd;border:1px solid #42a5f5;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.analogy{background:#fce4ec;border:1px solid #ef9a9a;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
[data-theme=dark] .ins{background:#0d2010;border-color:#388e3c}
[data-theme=dark] .warn{background:#1e1800;border-color:#f9a825}
[data-theme=dark] .note{background:#0d1e2e;border-color:#1976d2}
[data-theme=dark] .analogy{background:#2a0d14;border-color:#c62828}
.cb{background:#0d1117;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;font-family:monospace;font-size:.82rem;line-height:1.7;color:#e6edf3;white-space:pre-wrap}
.cb .cm{color:#8b949e}.cb .ck{color:#ff7b72}.cb .cv{color:#79c0ff}.cb .cs{color:#a5d6ff}.cb .cn{color:#f2cc60}.cb .cf{color:#d2a8ff}.cb .co{color:#ffa657}.cb .cg{color:#3fb950}
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.8rem 0}
.t-table th{background:#0a2040;color:#7ab8d8;font-family:monospace;font-size:.75rem;font-weight:700;padding:.5rem .7rem;text-align:left;border-bottom:2px solid #1a4070}
.t-table td{padding:.45rem .7rem;border-bottom:1px solid var(--border-color,#e8e8e8);vertical-align:top}
.t-table tr:last-child td{border-bottom:none}
.t-table tr:hover td{background:var(--bg-color,#f8f9fa)}
.flow-list{list-style:none;padding:0;margin:.8rem 0}
.fl-step{display:flex;gap:.8rem;margin-bottom:.5rem;font-size:.88rem;line-height:1.6}
.fl-num{width:24px;height:24px;border-radius:50%;background:#2e6da4;color:#fff;font-size:.72rem;font-weight:800;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:.15rem}
.diagram-box{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;font-family:monospace;font-size:.78rem;line-height:1.8;color:#c9d1d9;overflow-x:auto;white-space:pre}
.lab-box{background:var(--card-bg,#fff);border:2px solid #2e6da4;border-radius:10px;overflow:hidden;margin:1rem 0}
.lab-hdr{background:#0a2040;color:#fff;padding:.7rem 1.2rem;font-weight:700;font-family:monospace;font-size:.9rem}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.5rem;font-size:.87rem}
.sn{background:#2e6da4;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:800;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{padding:.3rem 0;font-size:.87rem;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐ ";font-size:1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#0a2040;color:#fff !important;border-color:#0a2040}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">DPDK MASTERY · PHASE 1 OF 3 · MODULE A</div>
  <div class="mod-title">Foundation, Architecture &amp; EAL</div>
  <div class="mod-subtitle">Why DPDK exists · Full software stack · Environment Abstraction Layer · PCIe device binding</div>
  <div class="mod-pills">
    <span class="mod-pill">Ch 1 — Why DPDK</span>
    <span class="mod-pill">Ch 2 — Architecture</span>
    <span class="mod-pill">Ch 3 — EAL Deep Dive</span>
    <span class="mod-pill">C · Linux · PCIe · VFIO</span>
    <span class="mod-pill">Weeks 1–2</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t-why')">Why DPDK</button>
  <button class="tab-btn" onclick="vt(event,'t-kpath')">Kernel Path</button>
  <button class="tab-btn" onclick="vt(event,'t-fastpath')">DPDK Fast Path</button>
  <button class="tab-btn" onclick="vt(event,'t-arch')">Architecture</button>
  <button class="tab-btn" onclick="vt(event,'t-eal')">EAL Deep Dive</button>
  <button class="tab-btn" onclick="vt(event,'t-pcie')">PCIe &amp; Binding</button>
  <button class="tab-btn" onclick="vt(event,'t-qa')">Interview Q&amp;A</button>
  <button class="tab-btn" onclick="vt(event,'t-lab')">Lab</button>
</div>
<!-- TAB: Why DPDK -->
<div id="t-why" class="tab-pane active">
<div class="p-blue">
<h4>&#9889; The Core Problem</h4>
DPDK (Data Plane Development Kit) exists because the Linux kernel packet processing path — perfectly adequate for general-purpose computing — is <strong>fundamentally too slow for line-rate NF processing at 10G, 25G, 100G speeds</strong>. It eliminates five categories of overhead: interrupts, allocation, copies, context switches, and protocol stack traversal.
</div>
<div class="note">&#128204; <strong>Packet budget at 100Gbps / 64-byte frames:</strong> ~148 million packets per second → <strong>6.7 nanoseconds per packet</strong>. A single L3 cache miss (~40 cycles @ 3 GHz = ~13 ns) already exceeds this budget. Every design choice in DPDK is shaped by this constraint.</div>
<p class="sep">OVERHEAD BREAKDOWN</p>
<table class="t-table">
<thead><tr><th>Overhead</th><th>Description</th><th>Cost</th><th>DPDK Solution</th></tr></thead>
<tbody>
<tr><td><code>Hardware interrupt</code></td><td>CPU suspends task, saves state, runs ISR</td><td>~1–5 µs + cache pollution</td><td>Interrupts disabled — CPU polls NIC (PMD)</td></tr>
<tr><td><code>softirq scheduling</code></td><td>ISR → NET_RX_SOFTIRQ deferred</td><td>Unpredictable latency</td><td>No softirq — polling loop runs constantly</td></tr>
<tr><td><code>sk_buff allocation</code></td><td>Per-packet kmalloc from slab allocator</td><td>~100–200 ns / packet</td><td>Pre-allocated mbuf pool — zero runtime alloc</td></tr>
<tr><td><code>Protocol stack traversal</code></td><td>Full IP/TCP even if NF doesn't need it</td><td>Many cache misses</td><td>App implements only what it needs</td></tr>
<tr><td><code>Memory copies</code></td><td>DMA ring → sk_buff → user buffer</td><td>2–4 memcpy / packet</td><td>NIC DMA writes directly to user-space hugepage mbuf</td></tr>
<tr><td><code>Context switch</code></td><td>Kernel → user-space on recv()</td><td>~1–10 µs</td><td>No syscalls in data path — pure user-space</td></tr>
<tr><td><code>TLB pressure</code></td><td>4KB pages → many TLB entries → frequent misses</td><td>10–100s cycles / miss</td><td>2MB/1GB hugepages — far fewer TLB entries</td></tr>
</tbody>
</table>
<div class="p-teal">
<h4>NAPI — Good but Not Enough</h4>
NAPI (New API) switches from interrupt-driven to polling mode under high load, reducing interrupt rate. But it still requires: sk_buff allocation per packet, full protocol stack traversal, memory copies to user space, and context switches on recv(). DPDK eliminates <em>all</em> of these — NAPI only eliminates one.
</div>
</div><!-- /t-why -->
<!-- TAB: Kernel Path -->
<div id="t-kpath" class="tab-pane">
<p class="sep">LINUX KERNEL PACKET PATH — 9 STAGES</p>
<div class="diagram-box">Linux Kernel Packet Path — Full Chain

① Packet arrives on wire
  → NIC DMA writes it to ring buffer in kernel memory

② NIC raises hardware interrupt
  → CPU suspends current task

③ CPU runs ISR (Interrupt Service Routine)
  → Quick acknowledgement, schedules softirq

④ NET_RX_SOFTIRQ scheduled
  → Deferred processing (unpredictable latency)

⑤ NAPI poll loop runs
  → Pulls packets from NIC ring into sk_buff structures

⑥ sk_buff travels up the protocol stack
  → Ethernet → IP → TCP/UDP (many function calls, cache misses)

⑦ Packet data copied into socket receive buffer
  → First memory copy

⑧ Application calls recv() / read()
  → Context switch to user space (~1–10 µs)

⑨ Packet data copied from socket buffer into application buffer
  → Second memory copy

Total: 2+ memory copies · 1+ context switch · 1 interrupt · 1 softirq per packet</div>
<div class="p-slate">
<h4>sk_buff — The Kernel Packet Structure</h4>
The <code>sk_buff</code> is the Linux kernel's equivalent of DPDK's <code>rte_mbuf</code>. Every packet is wrapped in an sk_buff.
<ul style="margin:.5rem 0 0;font-size:.87rem;line-height:1.8">
<li>Allocated <strong>per packet at interrupt time</strong> — per-packet malloc</li>
<li>Contains: head/data/tail/end pointers, network/transport header pointers, protocol info, device pointer, checksum fields</li>
<li>Supports cloning and reference counting — complex lifecycle with overhead</li>
<li>Size: <strong>200+ bytes of metadata overhead per packet</strong></li>
</ul>
</div>
<table class="t-table">
<thead><tr><th>Comparison Point</th><th>Linux sk_buff</th><th>DPDK rte_mbuf</th></tr></thead>
<tbody>
<tr><td>Allocation</td><td>Per-packet kmalloc at interrupt time</td><td>Pre-allocated in pool at startup — zero runtime alloc</td></tr>
<tr><td>Memory location</td><td>Kernel heap (4KB pages, swappable)</td><td>Hugepage RAM (2MB/1GB, pinned, NUMA-local)</td></tr>
<tr><td>NIC DMA target</td><td>Kernel ring buffer → copied to sk_buff</td><td>Directly into mbuf data buffer — zero copy</td></tr>
<tr><td>User-space access</td><td>Requires syscall + copy</td><td>Direct pointer — no syscall, no copy</td></tr>
<tr><td>Metadata size</td><td>200+ bytes</td><td>~128 bytes (rte_mbuf header)</td></tr>
</tbody>
</table>
</div><!-- /t-kpath -->
<!-- TAB: DPDK Fast Path -->
<div id="t-fastpath" class="tab-pane">
<p class="sep">DPDK PACKET PATH — ZERO OVERHEAD</p>
<div class="diagram-box">DPDK Fast Path — The Canonical Loop

NIC Rx Queue (hardware ring in hugepage memory)
  ↓
NIC DMA writes packet directly into pre-allocated mbuf
  → ZERO CPU involvement · ZERO kernel involvement

PMD polls ring — no interrupt, no softirq, no context switch
  rte_eth_rx_burst(port, queue, mbufs[], burst_size)
  → returns batch of received mbufs
  ↓
Application processes packets (modify headers, lookup, forward)
  ↓
  rte_eth_tx_burst(port, queue, mbufs[], n)
  → NIC DMA reads from mbuf and sends on wire
  ↓
  rte_pktmbuf_free(mbuf)
  → return mbuf to pool (no free — just reset head pointer)

0 interrupts · 0 copies · 0 malloc/free · 0 context switches</div>
<div class="ins">&#9989; <strong>The canonical DPDK main loop in C:</strong></div>
<div class="cb"><span class="cm">// Minimal DPDK fast-path polling loop</span>
<span class="ck">struct</span> rte_mbuf *pkts[<span class="cn">BURST_SZ</span>];

<span class="ck">while</span> (<span class="cn">1</span>) {
    <span class="co">uint16_t</span> nb_rx = <span class="cf">rte_eth_rx_burst</span>(port, queue, pkts, <span class="cn">BURST_SZ</span>);

    <span class="ck">for</span> (<span class="co">uint16_t</span> i = <span class="cn">0</span>; i &lt; nb_rx; i++) {
        <span class="cf">process_packet</span>(pkts[i]);   <span class="cm">// modify, forward, drop</span>
    }

    <span class="co">uint16_t</span> nb_tx = <span class="cf">rte_eth_tx_burst</span>(port, queue, pkts, nb_rx);

    <span class="cm">// Free any packets the Tx ring couldn't accept</span>
    <span class="ck">for</span> (<span class="co">uint16_t</span> i = nb_tx; i &lt; nb_rx; i++)
        <span class="cf">rte_pktmbuf_free</span>(pkts[i]);
}</div>
<div class="p-blue">
<h4>When NOT to Use DPDK</h4>
<ul style="margin:.3rem 0 0;font-size:.87rem;line-height:1.8">
<li><strong>Low packet rate applications</strong> — the dedicated polling CPU is wasted</li>
<li><strong>Need full TCP/IP stack</strong> — DPDK has no kernel TCP (VPP or mTCP fill this gap)</li>
<li><strong>Hardware without PMD support</strong> — older or obscure NICs</li>
<li><strong>Rapid prototyping</strong> — DPDK has significant setup complexity</li>
</ul>
</div>
</div><!-- /t-fastpath -->
<!-- TAB: Architecture -->
<div id="t-arch" class="tab-pane">
<p class="sep">DPDK SOFTWARE STACK</p>
<div class="diagram-box">DPDK Software Stack

┌─────────────────────────────────────────────────────────────────┐
│              USER APPLICATION (NF / SASE-DP)                    │
│  SASE URL Filter  │  Blaze Broker  │  MRI Resolver  │  NGFW    │
├──────────────┬────────────┬──────────────┬───────────────────────┤
│  rte_flow    │  rte_acl   │  rte_hash    │  rte_lpm              │
│  rte_timer   │  rte_meter │  rte_sched   │  rte_distributor      │
├──────────────┴────────────┴──────────────┴───────────────────────┤
│        rte_mbuf  │  rte_mempool  │  rte_ring                     │
├─────────────────────────────────────────────────────────────────┤
│              ethdev API  (rte_ethdev.h)                          │
├─────────────────────────────────────────────────────────────────┤
│    Poll Mode Drivers (PMD):  ixgbe │ i40e │ mlx5 │ tap │ ring   │
├─────────────────────────────────────────────────────────────────┤
│          EAL — Environment Abstraction Layer                     │
│    hugepages │ lcore mgmt │ PCI init │ memory │ log │ timer     │
└─────────────────────────────────────────────────────────────────┘
   KERNEL: UIO/VFIO driver (tiny — only device init/interrupt)
   NIC HARDWARE: Rx/Tx descriptor rings</div>
<table class="t-table">
<thead><tr><th>Component</th><th>Responsibility</th><th>Key API</th></tr></thead>
<tbody>
<tr><td><code>EAL</code></td><td>Hardware init, hugepage setup, lcore management, PCI device binding</td><td><code>rte_eal_init()</code></td></tr>
<tr><td><code>PMD</code></td><td>NIC-specific driver — polls hardware Rx/Tx queues directly</td><td><code>rte_eth_rx_burst()</code> / <code>rte_eth_tx_burst()</code></td></tr>
<tr><td><code>ethdev API</code></td><td>Hardware-agnostic interface to PMD — port configure, queue setup</td><td><code>rte_eth_dev_configure()</code></td></tr>
<tr><td><code>rte_mempool</code></td><td>Pre-allocated object pool — eliminates runtime malloc</td><td><code>rte_pktmbuf_pool_create()</code></td></tr>
<tr><td><code>rte_mbuf</code></td><td>Packet buffer structure — wraps packet data + metadata</td><td><code>rte_pktmbuf_mtod()</code></td></tr>
<tr><td><code>rte_ring</code></td><td>Lock-free FIFO circular buffer — inter-core packet passing</td><td><code>rte_ring_enqueue_bulk()</code></td></tr>
<tr><td><code>rte_flow</code></td><td>Hardware flow classification and steering (Flow API)</td><td><code>rte_flow_create()</code></td></tr>
<tr><td><code>rte_hash</code></td><td>Exact-match hash table — flow table lookups</td><td><code>rte_hash_lookup_bulk()</code></td></tr>
<tr><td><code>rte_lpm</code></td><td>Longest-prefix match — routing table</td><td><code>rte_lpm_lookup_bulk()</code></td></tr>
<tr><td><code>rte_acl</code></td><td>Multi-field ACL classification</td><td><code>rte_acl_classify()</code></td></tr>
<tr><td><code>rte_distributor</code></td><td>Work distributor — one RX core fans out to N worker cores</td><td><code>rte_distributor_process()</code></td></tr>
</tbody>
</table>
</div><!-- /t-arch -->
<!-- TAB: EAL Deep Dive -->
<div id="t-eal" class="tab-pane">
<div class="p-blue">
<h4>EAL — Environment Abstraction Layer</h4>
EAL is the foundation of every DPDK application. It must be the <strong>first call</strong> in main(). It initializes hugepages, discovers and probes NIC devices, pins lcores to CPUs, and provides all the primitives the rest of DPDK builds on.
</div>
<div class="cb"><span class="cm">// Minimal EAL initialization</span>
<span class="ck">int</span> <span class="cf">main</span>(<span class="ck">int</span> argc, <span class="ck">char</span> *argv[]) {
    <span class="ck">int</span> ret = <span class="cf">rte_eal_init</span>(argc, argv);
    <span class="ck">if</span> (ret &lt; <span class="cn">0</span>)
        <span class="cf">rte_exit</span>(<span class="cn">EXIT_FAILURE</span>, <span class="cs">"EAL init failed\n"</span>);

    argc -= ret;   <span class="cm">// EAL consumes its own args; remaining go to app</span>
    argv += ret;

    <span class="co">unsigned</span> nb_ports = <span class="cf">rte_eth_dev_count_avail</span>();
    <span class="cf">printf</span>(<span class="cs">"Available NIC ports: %u\n"</span>, nb_ports);

    <span class="co">unsigned</span> nb_lcores = <span class="cf">rte_lcore_count</span>();
    <span class="cf">printf</span>(<span class="cs">"Configured lcores: %u\n"</span>, nb_lcores);

    <span class="cm">// ... rest of application</span>
    <span class="cf">rte_eal_cleanup</span>();
    <span class="ck">return</span> <span class="cn">0</span>;
}</div>
<p class="sep">KEY EAL COMMAND-LINE FLAGS</p>
<table class="t-table">
<thead><tr><th>Flag</th><th>Meaning</th><th>Example</th></tr></thead>
<tbody>
<tr><td><code>-l</code></td><td>List of lcores to use (CPU threads)</td><td><code>-l 0-3</code> or <code>-l 0,2,4,6</code></td></tr>
<tr><td><code>-n</code></td><td>Number of memory channels</td><td><code>-n 4</code></td></tr>
<tr><td><code>-a</code></td><td>Allowlist: bind only these PCI devices</td><td><code>-a 0000:03:00.0</code></td></tr>
<tr><td><code>--socket-mem</code></td><td>Hugepage memory per NUMA socket (MB)</td><td><code>--socket-mem 1024,1024</code></td></tr>
<tr><td><code>--huge-dir</code></td><td>Path where hugepages are mounted</td><td><code>--huge-dir /dev/hugepages</code></td></tr>
<tr><td><code>--proc-type</code></td><td>Process type for multi-process DPDK</td><td><code>--proc-type=primary</code></td></tr>
<tr><td><code>--file-prefix</code></td><td>Shared memory prefix (multi-process)</td><td><code>--file-prefix=myapp</code></td></tr>
<tr><td><code>--log-level</code></td><td>Component log verbosity</td><td><code>--log-level=pmd:8</code></td></tr>
</tbody>
</table>
<p class="sep">LCORE CONCEPTS</p>
<div class="p-teal">
<h4>lcores vs Physical CPUs</h4>
An <strong>lcore</strong> is DPDK's logical core — maps 1:1 to a hardware CPU thread (including hyperthreads). EAL pins each lcore to a CPU using <code>pthread_setaffinity_np()</code> at startup, preventing OS scheduler migration. The <strong>main lcore</strong> (lcore 0 by default) runs after rte_eal_init() returns. Worker lcores are launched with <code>rte_eal_remote_launch()</code>.
</div>
<div class="cb"><span class="cm">// Enumerate and query lcores</span>
<span class="co">unsigned</span> lcore_id;
<span class="cf">RTE_LCORE_FOREACH_WORKER</span>(lcore_id) {
    <span class="co">unsigned</span> socket = <span class="cf">rte_lcore_to_socket_id</span>(lcore_id);
    <span class="co">unsigned</span> cpu    = <span class="cf">rte_lcore_to_cpu_id</span>(lcore_id);
    <span class="cf">printf</span>(<span class="cs">"lcore %u → CPU %u on socket %u\n"</span>, lcore_id, cpu, socket);
}

<span class="cm">// Launch worker function on each lcore</span>
<span class="cf">RTE_LCORE_FOREACH_WORKER</span>(lcore_id) {
    <span class="cf">rte_eal_remote_launch</span>(worker_loop, NULL, lcore_id);
}
<span class="cf">rte_eal_mp_wait_lcore</span>();  <span class="cm">// wait for all workers to finish</span></div>
</div><!-- /t-eal -->
<!-- TAB: PCIe & Binding -->
<div id="t-pcie" class="tab-pane">
<div class="p-orange">
<h4>PCIe Device Binding — Taking NIC from Kernel</h4>
Before DPDK can use a NIC, that NIC must be <strong>unbound from its kernel driver</strong> and bound to a DPDK-compatible driver. This is how DPDK takes ownership of the NIC away from the kernel.
</div>
<p class="sep">BINDING WORKFLOW</p>
<ul class="flow-list">
<li class="fl-step"><span class="fl-num">1</span><div><strong>Default state:</strong> NIC bound to kernel driver (<code>ixgbe</code>, <code>ice</code>, <code>mlx5_core</code>) → Kernel uses NIC for <code>eth0</code>, visible to <code>ip link</code></div></li>
<li class="fl-step"><span class="fl-num">2</span><div><strong>Unbind from kernel:</strong> <code>dpdk-devbind.py --unbind 0000:03:00.0</code></div></li>
<li class="fl-step"><span class="fl-num">3</span><div><strong>Bind to VFIO-PCI:</strong> <code>dpdk-devbind.py --bind=vfio-pci 0000:03:00.0</code></div></li>
<li class="fl-step"><span class="fl-num">4</span><div><strong>DPDK state:</strong> NIC invisible to <code>ip link</code> / <code>ifconfig</code>. PMD accesses NIC registers via mmap. DPDK owns all queues.</div></li>
</ul>
<table class="t-table">
<thead><tr><th>Driver</th><th>Mode</th><th>Security</th><th>Requirement</th><th>Use Case</th></tr></thead>
<tbody>
<tr><td><code>vfio-pci</code></td><td>IOMMU-protected DMA</td><td>Safe — IOMMU blocks unauthorized DMA</td><td>IOMMU enabled in BIOS + kernel (<code>intel_iommu=on</code>)</td><td>Production — recommended</td></tr>
<tr><td><code>uio_pci_generic</code></td><td>No IOMMU</td><td>Unsafe — NIC can DMA anywhere</td><td>No IOMMU required</td><td>Dev/test only</td></tr>
<tr><td><code>igb_uio</code></td><td>No IOMMU</td><td>Unsafe</td><td>Out-of-tree kernel module</td><td>Legacy — avoid</td></tr>
</tbody>
</table>
<div class="ins">&#127381; <strong>Mellanox/NVIDIA mlx4/mlx5 Exception:</strong> These NICs do <em>not</em> require unbinding from the kernel driver. They use a <strong>bifurcated driver model</strong> — the kernel driver (<code>mlx5_core</code>) handles management traffic and control operations, while the DPDK PMD gets dedicated hardware queues for fast-path traffic. Both coexist on the same NIC simultaneously. This is what the Jio SASE-DP deployment uses.</div>
<p class="sep">IOMMU & IOVA</p>
<div class="diagram-box">IOVA — How NIC DMA Addresses Host Memory

CPU Virtual Address  0x7F3A00001080   ← what your C code uses
Physical Address     0x200001080      ← actual silicon location
IOVA                 0x200001080      ← what NIC DMA engine uses

VFIO mode: IOMMU sits between PCIe bus and RAM
  DPDK registers allowed DMA regions with IOMMU at startup
  Unregistered DMA attempts → BLOCKED by IOMMU
  Kernel memory is safe even if NIC has a bug

How DPDK manages IOVA:
  ① EAL allocs hugepages  (physically contiguous 2MB frames)
  ② mmap() maps hugepages into process virtual address space
  ③ rte_mem_virt2iova()  converts virtual ↔ IOVA for any hugepage addr
  ④ Rx descriptor pre-filled: desc[i].buf_addr = IOVA of empty mbuf
  ⑤ NIC DMA reads descriptor → writes packet to that IOVA
  ⑥ PMD converts: mbuf ptr = rte_mem_iova2virt(desc[i].buf_addr)</div>
<div class="warn">&#9888;&#65039; <strong>Why IOVAs must be physically contiguous:</strong> NIC DMA writes a packet as one contiguous PCIe burst. 2MB hugepages guarantee physical contiguity within each page — safe for DMA. Normal 4KB pages may not be contiguous in physical RAM — <strong>never use for DMA buffers</strong>.</div>
</div><!-- /t-pcie -->
<!-- TAB: Interview Q&A -->
<div id="t-qa" class="tab-pane">
<div class="p-slate">
<h4>Q: What is the main overhead DPDK eliminates?</h4>
The interrupt per packet and associated context switch. At 100Gbps/64B there are ~148 Mpps — one interrupt per packet would saturate the CPU just handling interrupts. DPDK disables interrupts and uses polling (PMD), so the CPU spends 100% of its time processing packets, not handling interrupts.
</div>
<div class="p-slate">
<h4>Q: What is NAPI and why isn't it enough?</h4>
NAPI (New API) switches from interrupt-driven to polling mode under high load, reducing interrupt overhead. But it still requires sk_buff allocation per packet, full protocol stack traversal, memory copies to user space, and context switches on recv(). DPDK eliminates all of these — NAPI only eliminates one.
</div>
<div class="p-slate">
<h4>Q: How many memory copies does Linux do vs DPDK?</h4>
Linux: DMA → kernel ring buffer → sk_buff → user-space buffer = 2–3 copies.<br>
DPDK: NIC DMA writes directly into user-space hugepage mbuf = <strong>0 copies</strong> (zero copy).
</div>
<div class="p-slate">
<h4>Q: What is the packet budget at 100Gbps with 64-byte packets?</h4>
~148 million packets per second → ~6.7 nanoseconds per packet. A single L3 cache miss (~40 cycles @ 3 GHz = ~13 ns) already exceeds this. This is why hugepages, NUMA alignment, and cache-conscious programming are mandatory in DPDK — not optional.
</div>
<div class="p-slate">
<h4>Q: What is a bifurcated driver model and which NIC uses it?</h4>
Mellanox/NVIDIA ConnectX NICs (mlx4/mlx5) support bifurcation: the NIC is bound to both the kernel driver (mlx5_core) and the DPDK PMD simultaneously. The kernel driver handles management traffic (ARP, ICMP, control). The DPDK PMD gets dedicated hardware queues for fast-path traffic. This allows DPDK and kernel networking on the same NIC without rebinding — a key operational advantage in production deployments.
</div>
<div class="p-slate">
<h4>Q: What does rte_eal_init() do?</h4>
It: (1) parses EAL command-line arguments, (2) mounts and allocates hugepages on configured NUMA sockets, (3) probes PCI devices and initializes PMD drivers, (4) pins lcores to physical CPUs via <code>pthread_setaffinity_np()</code>, (5) initializes the memory allocator, log system, and timer subsystem. It must be the first call in main(). Returns the number of args consumed — the rest belong to the application.
</div>
<div class="p-slate">
<h4>Q: Why does DPDK require hugepages?</h4>
Two reasons: (1) <strong>TLB efficiency</strong> — 2MB pages mean far fewer TLB entries, dramatically reducing TLB misses on the hot path. (2) <strong>DMA stability</strong> — hugepages are pinned (mlock'd) so they cannot be swapped out. NIC DMA needs fixed physical addresses (IOVAs). If a page is swapped out, its IOVA is stale — the NIC would write to wrong/freed memory. Hugepages guarantee the IOVA is always valid.
</div>
</div><!-- /t-qa -->
<!-- TAB: Lab -->
<div id="t-lab" class="tab-pane">
<div class="lab-box">
<div class="lab-hdr">&#128293; Lab 1: DPDK Hello World + EAL Probe</div>
<div class="lab-body">
<p style="font-size:.87rem;margin:.3rem 0 .8rem">Build the standard DPDK helloworld sample and instrument it to probe every EAL primitive.</p>
<div class="lab-step"><span class="sn">1</span><div><strong>Setup hugepages:</strong> <code>echo 1024 &gt; /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages</code></div></div>
<div class="lab-step"><span class="sn">2</span><div><strong>Mount hugetlbfs:</strong> <code>mount -t hugetlbfs none /dev/hugepages</code></div></div>
<div class="lab-step"><span class="sn">3</span><div><strong>Bind NIC to VFIO:</strong> <code>dpdk-devbind.py --bind=vfio-pci 0000:03:00.0</code></div></div>
<div class="lab-step"><span class="sn">4</span><div><strong>Build helloworld:</strong> <code>cd $DPDK_BUILD/examples/helloworld &amp;&amp; make</code></div></div>
<div class="lab-step"><span class="sn">5</span><div><strong>Run with 4 lcores:</strong> <code>./helloworld -l 0-3 -n 4</code></div></div>
<div class="lab-step"><span class="sn">6</span><div><strong>Add probe code:</strong> print lcore count, NUMA socket per lcore, available port count, hugepage memory per socket</div></div>
<div class="lab-step"><span class="sn">7</span><div><strong>Verify IOVA:</strong> Call <code>rte_mem_virt2iova()</code> on a stack variable — expect <code>RTE_BAD_IOVA</code> (stack is not a hugepage). Call on a hugepage-allocated buffer — expect valid IOVA.</div></div>
</div>
</div>
<div class="lab-box">
<div class="lab-hdr">&#128293; Lab 2: Skeleton NIC Receiver (no mbuf pool yet)</div>
<div class="lab-body">
<p style="font-size:.87rem;margin:.3rem 0 .8rem">Before setting up full rx/tx queues: use dpdk-devbind.py to cycle bind/unbind a NIC and observe how it disappears from <code>ip link</code>. Then probe the NIC capabilities.</p>
<div class="lab-step"><span class="sn">1</span><div>Run <code>ip link</code> — note the NIC interface name (e.g. <code>eth1</code>)</div></div>
<div class="lab-step"><span class="sn">2</span><div>Bind to vfio-pci: <code>dpdk-devbind.py --bind=vfio-pci 0000:03:00.0</code></div></div>
<div class="lab-step"><span class="sn">3</span><div>Run <code>ip link</code> again — <code>eth1</code> is gone from the OS view</div></div>
<div class="lab-step"><span class="sn">4</span><div>In C: call <code>rte_eth_dev_info_get(0, &amp;info)</code> and print <code>driver_name</code>, <code>max_rx_queues</code>, <code>max_tx_queues</code>, <code>rx_desc_lim.nb_max</code></div></div>
<div class="lab-step"><span class="sn">5</span><div>Restore: <code>dpdk-devbind.py --bind=ixgbe 0000:03:00.0</code> — <code>eth1</code> reappears</div></div>
</div>
</div>
<p class="sep">MASTERY CHECKLIST</p>
<ul class="cl">
<li>Can state the 6 categories of Linux kernel packet path overhead and DPDK's solution for each</li>
<li>Can explain why NAPI is not enough</li>
<li>Can draw the DPDK software stack from EAL to user application</li>
<li>Can explain what rte_eal_init() does and why it must be first</li>
<li>Can bind a NIC to vfio-pci and explain what changes in the kernel view</li>
<li>Can explain IOVA, why hugepages must be used for DMA, and what happens if a page is swapped out</li>
<li>Can explain the bifurcated driver model and which NICs use it</li>
<li>Can enumerate lcores, query their NUMA socket, and launch a worker function</li>
</ul>
</div><!-- /t-lab -->
<div class="mod-nav">
  <a href="/learning/data-plane/dpdk/dpdk-roadmap/">&#8593; Roadmap</a>
  <a class="nb" href="/learning/data-plane/dpdk/module-p1-memory/">P1B: Hugepages, mempool &amp; mbuf &#8594;</a>
</div>
<script>
function vt(e,id){
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  e.target.classList.add('active');
}
</script>
