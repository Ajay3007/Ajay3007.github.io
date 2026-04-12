---
layout: default
title: "DPDK P2 — rte_ring, Distributor & App Models"
permalink: /learning/data-plane/dpdk/module-p2-rings/
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
.p-violet{background:#f3f0fc;border-left:4px solid #7c3aed;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
[data-theme=dark] .p-teal{background:#0d2020;border-color:#2a9a8e}
[data-theme=dark] .p-blue{background:#0d1e34;border-color:#4a90d9}
[data-theme=dark] .p-orange{background:#1e0d00;border-color:#e07830}
[data-theme=dark] .p-slate{background:#1a1e24;border-color:#8898aa}
[data-theme=dark] .p-violet{background:#180d30;border-color:#9d6bf0}
.p-teal h4,.p-blue h4,.p-orange h4,.p-slate h4,.p-violet h4{margin:0 0 .5rem;font-size:.9rem;font-weight:700}
.ins{background:#e8f5e9;border:1px solid #66bb6a;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.warn{background:#fff8e1;border:1px solid #ffca28;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.note{background:#e3f2fd;border:1px solid #42a5f5;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
[data-theme=dark] .ins{background:#0d2010;border-color:#388e3c}
[data-theme=dark] .warn{background:#1e1800;border-color:#f9a825}
[data-theme=dark] .note{background:#0d1e2e;border-color:#1976d2}
.cb{background:#0d1117;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;font-family:monospace;font-size:.82rem;line-height:1.7;color:#e6edf3}
.cb .cm{color:#8b949e}.cb .ck{color:#ff7b72}.cb .cv{color:#79c0ff}.cb .cs{color:#a5d6ff}.cb .cn{color:#f2cc60}.cb .cf{color:#d2a8ff}.cb .co{color:#ffa657}.cb .cg{color:#3fb950}
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.8rem 0}
.t-table th{background:#0b3028;color:#5adbc8;font-family:monospace;font-size:.75rem;font-weight:700;padding:.5rem .7rem;text-align:left;border-bottom:2px solid #1a6040}
.t-table td{padding:.45rem .7rem;border-bottom:1px solid var(--border-color,#e8e8e8);vertical-align:top}
.t-table tr:last-child td{border-bottom:none}
.t-table tr:hover td{background:var(--bg-color,#f8f9fa)}
.diagram-box{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;font-family:monospace;font-size:.78rem;line-height:1.8;color:#c9d1d9;overflow-x:auto;white-space:pre}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.8rem 0}
@media(max-width:640px){.two-col{grid-template-columns:1fr}}
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
  <div class="mod-eyebrow">DPDK MASTERY · PHASE 2 OF 3 · MODULE B</div>
  <div class="mod-title">rte_ring, Distributor &amp; App Models</div>
  <div class="mod-subtitle">Lock-free ring internals · CAS mechanics · rte_distributor · Run-to-completion vs Pipeline</div>
  <div class="mod-pills">
    <span class="mod-pill">Ch 10 — rte_ring</span>
    <span class="mod-pill">Ch 11 — rte_distributor</span>
    <span class="mod-pill">Ch 12 — App Models</span>
    <span class="mod-pill">C · Lock-Free · MPMC</span>
    <span class="mod-pill">Weeks 8–10</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t-ring')">Ring Internals</button>
  <button class="tab-btn" onclick="vt(event,'t-cas')">CAS Mechanics</button>
  <button class="tab-btn" onclick="vt(event,'t-modes')">Ring Modes</button>
  <button class="tab-btn" onclick="vt(event,'t-api')">Ring API</button>
  <button class="tab-btn" onclick="vt(event,'t-dist')">rte_distributor</button>
  <button class="tab-btn" onclick="vt(event,'t-appmodel')">App Models</button>
  <button class="tab-btn" onclick="vt(event,'t-qa')">Interview Q&amp;A</button>
  <button class="tab-btn" onclick="vt(event,'t-lab')">Lab</button>
</div>

<!-- TAB: Ring Internals -->
<div id="t-ring" class="tab-pane active">

<div class="p-teal">
<h4>rte_ring — The Inter-Core Packet Bus</h4>
<code>rte_ring</code> is DPDK's lock-free, fixed-size circular buffer. It passes object pointers (typically mbuf pointers) between cores with minimal overhead — no mutexes, no condition variables, no syscalls. It is the primitive that connects Rx cores, worker cores, and Tx cores in a pipeline architecture.
</div>

<div class="diagram-box">rte_ring Internal Layout (in hugepage memory, power-of-2 sized)

┌─────────────────────────────────────────────────────────────────┐
│   ring metadata: name, size (power-of-2), mask, flags           │
│   prod.head  prod.tail  (producer / enqueue side)               │
│   cons.head  cons.tail  (consumer / dequeue side)               │
├─────────────────────────────────────────────────────────────────┤
│  ring[0] │ ring[1] │ ring[2] │ ... │ ring[size-1]              │
│  (void* pointer slots — contain mbuf pointers or other objects)  │
└─────────────────────────────────────────────────────────────────┘

free  slots = (cons.tail - prod.head) & mask
used  slots = (prod.tail - cons.head) & mask

Invariant: prod.tail always ≤ prod.head (producers fill between head and tail)
           cons.tail always ≤ prod.tail (consumers can only see committed data)</div>

<div class="note">&#128204; <strong>Power-of-2 size requirement:</strong> rte_ring uses <code>mask = size - 1</code> for modulo via bitwise AND — <code>idx & mask</code> instead of <code>idx % size</code>. Bitwise AND is a single instruction vs division which can be 20–80 cycles. This is why ring size must always be a power of 2.</div>

</div><!-- /t-ring -->

<!-- TAB: CAS Mechanics -->
<div id="t-cas" class="tab-pane">

<div class="p-teal">
<h4>Lock-Free MPMC via CAS (Compare-And-Swap)</h4>
rte_ring achieves multi-producer multi-consumer safety without mutexes using atomic CAS operations. CAS atomically checks if a memory location holds an expected value and swaps it with a new value — if another thread modified it concurrently, CAS fails and the operation retries.
</div>

<p class="sep">MULTI-PRODUCER ENQUEUE — CAS PROTOCOL</p>

<div class="diagram-box">Multi-Producer Enqueue (simplified — showing CAS retry)

Producer A and Producer B both want to enqueue simultaneously:

Step ①: Both read current prod.head = 10
Step ②: Both compute new_head = 10 + 1 = 11
Step ③: CAS(prod.head, old=10, new=11) — atomic operation
  → Producer A wins CAS: prod.head = 11, A owns slot[10]
  → Producer B loses CAS: prod.head already 11 → retry from ①

Step ④: Producer A writes object pointer into ring[10]
Step ⑤: Producer A waits for prod.tail to reach 10
         (if another producer owns an earlier slot, A must wait for it to commit)
Step ⑥: Producer A sets prod.tail = 11
         → Consumer can now see slot[10]

Key insight: CAS failure is not an error — it's the retry signal.
Under low contention: CAS succeeds first try → near-zero overhead.
Under high contention: retries add latency → prefer SPSC when possible.</div>

<div class="p-blue">
<h4>Why Wait-Free is Not the Same as Lock-Free</h4>
rte_ring is <strong>lock-free</strong> (no thread can block indefinitely holding a lock) but not <em>wait-free</em> (individual threads may retry). In practice, under typical DPDK workloads with one producer and one consumer per ring (SPSC mode), there is no CAS at all — just atomic load/store, which is near-zero cost.
</div>

</div><!-- /t-cas -->

<!-- TAB: Ring Modes -->
<div id="t-modes" class="tab-pane">

<table class="t-table">
<thead><tr><th>Mode</th><th>Enqueue</th><th>Dequeue</th><th>Overhead</th><th>Use Case</th></tr></thead>
<tbody>
<tr><td><strong>SPSC</strong><br>Single Producer, Single Consumer</td><td>No CAS — direct index</td><td>No CAS — direct index</td><td>Minimum — just atomic load/store</td><td>One Rx core → one worker; fastest possible ring</td></tr>
<tr><td><strong>MPSC</strong><br>Multi Producer, Single Consumer</td><td>CAS on producer</td><td>No CAS on consumer</td><td>Low on consumer side</td><td>Multiple cores feeding one consumer (fan-in)</td></tr>
<tr><td><strong>SPMC</strong><br>Single Producer, Multi Consumer</td><td>No CAS on producer</td><td>CAS on consumer</td><td>Low on producer side</td><td>One source, multiple workers (rare)</td></tr>
<tr><td><strong>MPMC</strong><br>Multi Producer, Multi Consumer</td><td>CAS on both sides</td><td>CAS on both sides</td><td>Highest — most general</td><td>Default mode; needed when both sides have multiple cores</td></tr>
</tbody>
</table>

<div class="cb"><span class="cm">// Create ring with explicit mode flags</span>
<span class="ck">struct</span> rte_ring *ring;

<span class="cm">// SPSC — fastest (dedicate one producer and one consumer core)</span>
ring = <span class="cf">rte_ring_create</span>(<span class="cs">"FAST_RING"</span>, <span class="cn">1024</span>, <span class="cf">rte_socket_id</span>(),
                      <span class="cn">RING_F_SP_ENQ</span> | <span class="cn">RING_F_SC_DEQ</span>);

<span class="cm">// MPMC — default (most general)</span>
ring = <span class="cf">rte_ring_create</span>(<span class="cs">"WORK_RING"</span>, <span class="cn">4096</span>, <span class="cf">rte_socket_id</span>(),
                      <span class="cn">0</span>);   <span class="cm">// 0 = MPMC</span>

<span class="cm">// Check if creation succeeded</span>
<span class="ck">if</span> (!ring)
    <span class="cf">rte_exit</span>(<span class="cn">EXIT_FAILURE</span>, <span class="cs">"Ring create failed: %s\n"</span>, <span class="cf">rte_strerror</span>(<span class="cf">rte_errno</span>));</div>

<div class="warn">&#9888;&#65039; <strong>Ring size must be a power of 2.</strong> If you pass a non-power-of-2 size, <code>rte_ring_create()</code> returns NULL. The actual usable capacity is <code>size - 1</code> (one slot is always kept empty to distinguish full from empty). So a ring of size 1024 holds at most 1023 objects.</div>

</div><!-- /t-modes -->

<!-- TAB: Ring API -->
<div id="t-api" class="tab-pane">

<p class="sep">CORE ENQUEUE / DEQUEUE APIs</p>

<div class="cb"><span class="cm">// Single object</span>
<span class="co">int</span> ret = <span class="cf">rte_ring_enqueue</span>(ring, obj_ptr);  <span class="cm">// 0 = success, -ENOBUFS = full</span>
<span class="co">int</span> ret = <span class="cf">rte_ring_dequeue</span>(ring, &amp;obj_ptr); <span class="cm">// 0 = success, -ENOENT = empty</span>

<span class="cm">// Bulk — preferred: reduces CAS contention + better cache efficiency</span>
<span class="co">unsigned</span> enqueued = <span class="cf">rte_ring_enqueue_bulk</span>(ring, objs, n, &amp;free_space);
<span class="cm">// Returns n on success, 0 on failure (ring doesn't have n free slots)</span>

<span class="co">unsigned</span> dequeued = <span class="cf">rte_ring_dequeue_bulk</span>(ring, objs, n, &amp;avail);
<span class="cm">// Returns n on success, 0 on failure (ring doesn't have n objects)</span>

<span class="cm">// Burst — partial success (unlike bulk which is all-or-nothing)</span>
<span class="co">unsigned</span> enqueued = <span class="cf">rte_ring_enqueue_burst</span>(ring, objs, n, &amp;free_space);
<span class="cm">// Returns 0..n: enqueued as many as possible</span>

<span class="co">unsigned</span> dequeued = <span class="cf">rte_ring_dequeue_burst</span>(ring, objs, n, &amp;avail);
<span class="cm">// Returns 0..n: dequeued as many as available</span></div>

<div class="p-teal">
<h4>bulk vs burst — Which to Use?</h4>
<ul style="margin:.3rem 0 0;font-size:.87rem;line-height:1.8">
<li><strong>bulk</strong>: all-or-nothing. Enqueues exactly <code>n</code> objects or fails. Use when you need atomic batch operations — e.g., pass a full burst of 32 packets to a worker core atomically.</li>
<li><strong>burst</strong>: enqueues as many as possible (0 to n). Use for drain loops where partial success is acceptable — e.g., forwarding loop that drains whatever is available.</li>
</ul>
</div>

<p class="sep">RING INSPECTION APIs</p>

<div class="cb"><span class="co">unsigned</span> count    = <span class="cf">rte_ring_count</span>(ring);      <span class="cm">// objects currently in ring</span>
<span class="co">unsigned</span> free_cnt = <span class="cf">rte_ring_free_count</span>(ring);  <span class="cm">// empty slots available</span>
<span class="co">int</span>      full      = <span class="cf">rte_ring_full</span>(ring);        <span class="cm">// 1 if no free slots</span>
<span class="co">int</span>      empty     = <span class="cf">rte_ring_empty</span>(ring);       <span class="cm">// 1 if no objects</span>

<span class="cm">// Named ring lookup (for multi-process — secondary finds ring created by primary)</span>
<span class="ck">struct</span> rte_ring *ring = <span class="cf">rte_ring_lookup</span>(<span class="cs">"WORK_RING"</span>);
<span class="ck">if</span> (!ring) <span class="cm">/* ring not yet created by primary */</span>;</div>

</div><!-- /t-api -->

<!-- TAB: rte_distributor -->
<div id="t-dist" class="tab-pane">

<div class="p-teal">
<h4>rte_distributor — One RX Core → N Workers</h4>
<code>rte_distributor</code> implements the <strong>fan-out pattern</strong>: one RX/coordinator lcore receives packets from the NIC and distributes them to a pool of worker lcores based on a flow tag. The key property: all packets with the same tag (e.g., RSS hash) are guaranteed to go to the same worker — enabling per-flow state without locking.
</div>

<div class="diagram-box">rte_distributor Architecture

              ┌─────────────────┐
              │  RX / Coordinator│  lcore 0
              │  rte_eth_rx_burst│
              │  rte_distributor_│
              │  process()       │
              └────────┬────────┘
                       │ distributes by mbuf->hash.rss
          ┌────────────┼────────────┐
          ▼            ▼            ▼
   ┌──────────┐  ┌──────────┐  ┌──────────┐
   │ Worker 1 │  │ Worker 2 │  │ Worker 3 │   lcores 1, 2, 3
   │ rte_dist_│  │ rte_dist_│  │ rte_dist_│
   │ get_pkt()│  │ get_pkt()│  │ get_pkt()│
   └──────────┘  └──────────┘  └──────────┘
   All packets with same hash → same worker → per-flow state, no locks</div>

<div class="cb"><span class="cm">// Coordinator lcore (lcore 0)</span>
<span class="ck">struct</span> rte_distributor *dist = <span class="cf">rte_distributor_create</span>(
    <span class="cs">"SASE_DIST"</span>,         <span class="cm">// name</span>
    <span class="cf">rte_socket_id</span>(),     <span class="cm">// NUMA socket</span>
    nb_workers,          <span class="cm">// number of worker lcores</span>
    <span class="cn">RTE_DIST_ALG_BURST</span>   <span class="cm">// burst mode (preferred over single)</span>
);

<span class="ck">struct</span> rte_mbuf *pkts[<span class="cn">BURST_SIZE</span>];
<span class="ck">while</span> (<span class="cn">1</span>) {
    <span class="co">uint16_t</span> nb_rx = <span class="cf">rte_eth_rx_burst</span>(port, <span class="cn">0</span>, pkts, <span class="cn">BURST_SIZE</span>);
    <span class="cm">// Set flow tag for each packet — distributor uses this for affinity</span>
    <span class="ck">for</span> (<span class="co">uint16_t</span> i = <span class="cn">0</span>; i &lt; nb_rx; i++)
        pkts[i]-&gt;hash.usr = pkts[i]-&gt;hash.rss;  <span class="cm">// use RSS hash as tag</span>
    <span class="cf">rte_distributor_process</span>(dist, pkts, nb_rx);
}

<span class="cm">// Worker lcore (each runs this function)</span>
<span class="ck">static</span> <span class="co">int</span> <span class="cf">worker_loop</span>(<span class="ck">void</span> *arg) {
    <span class="ck">struct</span> rte_distributor *dist = arg;
    <span class="ck">struct</span> rte_mbuf *pkts[<span class="cn">BURST_SIZE</span>];
    <span class="co">uint16_t</span> nb;
    <span class="ck">while</span> (<span class="cn">1</span>) {
        nb = <span class="cf">rte_distributor_get_pkt</span>(dist, <span class="cf">rte_lcore_id</span>(), pkts, NULL, <span class="cn">0</span>);
        <span class="ck">for</span> (<span class="co">uint16_t</span> i = <span class="cn">0</span>; i &lt; nb; i++) {
            <span class="cf">process_packet</span>(pkts[i]);
            <span class="cf">rte_pktmbuf_free</span>(pkts[i]);
        }
    }
    <span class="ck">return</span> <span class="cn">0</span>;
}</div>

<div class="ins">&#127381; <strong>Blaze/SASE-DP Context:</strong> The SASE-DP URL filter uses a distributor-based architecture: the RX core receives packets from a 100G NIC and distributes by RSS hash (= 5-tuple hash) to 8 worker cores. Each worker owns its portion of the flow table — no cross-core lookups, no locking on the hot path. Enterprise and mobility traffic classes separated by RETA programming.</div>

</div><!-- /t-dist -->

<!-- TAB: App Models -->
<div id="t-appmodel" class="tab-pane">

<p class="sep">TWO FUNDAMENTAL DPDK APPLICATION ARCHITECTURES</p>

<div class="two-col">
<div class="p-blue">
<h4>Run-to-Completion (RTC)</h4>
Each lcore handles the <em>entire</em> processing pipeline for its packets: RX → process → TX. All processing for a packet happens on one core before the next packet is touched.
<br><br>
<strong>Pros:</strong> Simplest. No inter-core communication. Best cache locality — packet data stays in one core's cache throughout processing. Lowest latency for simple NFs.
<br><br>
<strong>Cons:</strong> Processing time per packet must fit within one core's budget. Hard to balance load when packets have variable processing time. One slow packet blocks the whole pipeline.
<br><br>
<strong>Best for:</strong> Simple forwarding, L2/L3 routing, stateless NFs.
</div>
<div class="p-teal">
<h4>Pipeline Model</h4>
Different lcores handle different stages: lcore 0 → RX, lcore 1 → classify, lcore 2 → policy, lcore 3 → TX. Packets flow through stages via rte_ring queues.
<br><br>
<strong>Pros:</strong> Each stage runs at its own speed. Easier to scale specific bottleneck stages by adding more cores. Stages can be optimized independently.
<br><br>
<strong>Cons:</strong> Each ring hand-off adds ~50–100 ns latency. Higher total latency. More complex. Ring backpressure must be handled explicitly.
<br><br>
<strong>Best for:</strong> Complex NFs with multiple distinct processing stages (DPI, URL filter, stateful firewalls). SASE-DP uses a hybrid.
</div>
</div>

<div class="diagram-box">Run-to-Completion (RTC)

lcore 0: RX → process → TX (all ports, all stages)
lcore 1: RX → process → TX (different queue)
lcore 2: RX → process → TX (different queue)
lcore 3: RX → process → TX (different queue)

Ring traffic: NONE — no inter-core packets

Pipeline Model

lcore 0:  NIC RX → ring_rx[]  ──────────────────────────────►
lcore 1:  ring_rx[] → classify → ring_classify[] ──────────►
lcore 2:  ring_classify[] → policy → ring_policy[] ────────►
lcore 3:  ring_policy[] → TX NIC

Hybrid (SASE-DP): RTC within each stage, distributor between RX and workers</div>

<table class="t-table">
<thead><tr><th>Criterion</th><th>Run-to-Completion</th><th>Pipeline</th></tr></thead>
<tbody>
<tr><td>Latency</td><td>Lower (no ring hand-off)</td><td>Higher (50–100 ns per ring)</td></tr>
<tr><td>Throughput</td><td>Equal if compute-bound</td><td>Better if stages can parallelize</td></tr>
<tr><td>Complexity</td><td>Simple</td><td>Complex (backpressure, stage tuning)</td></tr>
<tr><td>Load balancing</td><td>Harder with variable per-packet cost</td><td>Easier — tune per stage</td></tr>
<tr><td>Cache behavior</td><td>Excellent (packet stays in one cache)</td><td>Cold cache per stage</td></tr>
<tr><td>Use case</td><td>Simple forwarding, routing</td><td>DPI, URL filter, stateful NFs</td></tr>
</tbody>
</table>

</div><!-- /t-appmodel -->

<!-- TAB: Interview Q&A -->
<div id="t-qa" class="tab-pane">

<div class="p-slate">
<h4>Q: How does rte_ring achieve lock-free MPMC operation?</h4>
Using CAS (Compare-And-Swap) atomic operations. Each producer atomically claims a slot by CAS'ing the producer head pointer. If the CAS fails (another producer claimed the slot concurrently), it retries. Once a producer owns a slot, it writes the object and then waits for the producer tail to reach its slot (to maintain order), then advances the tail. Consumers similarly CAS the consumer head. Under low contention, CAS succeeds on first try with near-zero overhead.
</div>

<div class="p-slate">
<h4>Q: Why must rte_ring size be a power of 2?</h4>
rte_ring uses bitwise AND for modulo: <code>idx & (size-1)</code> instead of <code>idx % size</code>. Bitwise AND is a single-cycle instruction; division can take 20–80 cycles. At millions of enqueue/dequeue operations per second, this difference matters. Power-of-2 also means the mask is simply <code>size - 1</code> — computed once at creation time.
</div>

<div class="p-slate">
<h4>Q: What is the difference between rte_ring_enqueue_bulk and enqueue_burst?</h4>
<strong>bulk</strong>: all-or-nothing. Enqueues exactly <em>n</em> objects or fails entirely (returns 0). The ring must have at least <em>n</em> free slots. Use when atomicity is required — e.g., passing a full burst to a stage.<br>
<strong>burst</strong>: partial success. Enqueues 0 to <em>n</em> objects — as many as the ring can accept. Returns the actual count. Use in drain loops where you want maximum throughput regardless of how many succeed.
</div>

<div class="p-slate">
<h4>Q: What is rte_distributor and when would you use it over rte_ring?</h4>
<code>rte_distributor</code> is a higher-level fan-out primitive: one coordinator distributes packets to N workers by flow tag (hash), guaranteeing all packets of the same flow go to the same worker. Use it when you need <em>flow affinity</em> — per-flow state on workers without cross-core locks. Use rte_ring directly when you have simpler FIFO queuing needs or want more control over the distribution logic.
</div>

<div class="p-slate">
<h4>Q: When should you choose pipeline over run-to-completion?</h4>
Pipeline is better when: (1) Processing stages have very different compute costs — pipeline lets you add more cores to the bottleneck stage. (2) Stages can be developed and optimized independently. (3) You need different security/isolation boundaries between stages (separate processes via shared rings). RTC is better when: latency is paramount, processing is simple and uniform, or the NF fits cleanly within a single lcore's budget.
</div>

</div><!-- /t-qa -->

<!-- TAB: Lab -->
<div id="t-lab" class="tab-pane">

<div class="lab-box">
<div class="lab-hdr">&#128293; Lab 6: Ring-Based Worker Pipeline</div>
<div class="lab-body">
<p style="font-size:.87rem;margin:.3rem 0 .8rem">Implement a two-stage pipeline: RX lcore → rte_ring → Worker lcore → TX. Measure the latency added by the ring hand-off.</p>

<div class="lab-step"><span class="sn">1</span><div>Create two SPSC rings: <code>rte_ring_create("RX_TO_WORKER", 1024, socket, RING_F_SP_ENQ | RING_F_SC_DEQ)</code> and a symmetric TX ring</div></div>
<div class="lab-step"><span class="sn">2</span><div><strong>RX lcore (lcore 0):</strong> <code>rte_eth_rx_burst()</code> → timestamp each mbuf → <code>rte_ring_enqueue_burst()</code></div></div>
<div class="lab-step"><span class="sn">3</span><div><strong>Worker lcore (lcore 1):</strong> <code>rte_ring_dequeue_burst()</code> → compute latency = <code>rte_rdtsc() - mbuf_timestamp</code> → <code>rte_eth_tx_burst()</code></div></div>
<div class="lab-step"><span class="sn">4</span><div>Print ring latency statistics: min, max, avg, p99 in nanoseconds</div></div>
<div class="lab-step"><span class="sn">5</span><div>Compare with RTC: move all processing to one lcore (no ring) — measure the latency difference</div></div>
<div class="lab-step"><span class="sn">6</span><div><strong>Extension:</strong> try MPMC ring with 2 producers and 2 consumers — observe CAS overhead in the latency numbers</div></div>
</div>
</div>

<div class="lab-box">
<div class="lab-hdr">&#128293; Lab 7: rte_distributor Flow Affinity Verification</div>
<div class="lab-body">
<p style="font-size:.87rem;margin:.3rem 0 .8rem">Verify that the distributor routes all packets of the same 5-tuple to the same worker core.</p>

<div class="lab-step"><span class="sn">1</span><div>Set up distributor with 4 workers using <code>rte_distributor_create()</code></div></div>
<div class="lab-step"><span class="sn">2</span><div>In coordinator: set <code>pkts[i]->hash.usr = pkts[i]->hash.rss</code> as flow tag</div></div>
<div class="lab-step"><span class="sn">3</span><div>In each worker: maintain a per-worker hash map of <code>rss_hash → count</code></div></div>
<div class="lab-step"><span class="sn">4</span><div>Generate traffic with 8 distinct 5-tuples (e.g., using pktgen or scapy)</div></div>
<div class="lab-step"><span class="sn">5</span><div>After 1M packets: verify each RSS hash value appears on exactly one worker lcore — never split</div></div>
</div>
</div>

<p class="sep">MASTERY CHECKLIST</p>
<ul class="cl">
<li>Can draw rte_ring internal layout: prod/cons head/tail, ring array, mask calculation</li>
<li>Can explain the CAS retry protocol for multi-producer enqueue</li>
<li>Can explain SPSC vs MPMC tradeoffs and when to choose each</li>
<li>Can explain bulk vs burst semantics and when to use each</li>
<li>Can explain how rte_distributor guarantees flow affinity</li>
<li>Can draw and compare run-to-completion vs pipeline architectures</li>
<li>Can identify when pipeline adds value vs when RTC is better</li>
<li>Can explain why ring size must be a power of 2 (bitwise AND trick)</li>
</ul>

</div><!-- /t-lab -->

<div class="mod-nav">
  <a href="{{ '/learning/data-plane/dpdk/module-p2-pmd/' | relative_url }}">&#8592; P2A: PMD &amp; Port Config</a>
  <a href="{{ '/learning/data-plane/dpdk/dpdk-roadmap/' | relative_url }}">&#8593; Roadmap</a>
  <a class="nb" href="{{ '/learning/data-plane/dpdk/module-p3-advanced/' | relative_url }}">P3A: Multi-Process &amp; rte_flow &#8594;</a>
</div>

<script>
function vt(e,id){
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  e.target.classList.add('active');
}
</script>
