---
title: "VPP P2B - vlib - Graph Dispatcher"
description: "VPP MASTERY · PHASE 2B · WEEKS 5–6 ⚙️ vlib - Graph Dispatcher Node Types · Dispatch Loop · Buffer Layout · Dual-Loop Pattern · Multi-Threading · Packet Tracing src/vlib/main.c…"
domain: data-plane
track: vpp
order: 2
ownHeader: true
url: /learning/data-plane/vpp/module-p2-vlib/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a2a20 0%,#1a7a6e 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#7ad8cc;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#a8e0d8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#c8f4f0}
.tab-bar{display:flex;flex-wrap:wrap;gap:0;background:#0a2a20;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ad8cc;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#5dd6c8;border-bottom-color:#5dd6c8}
.tab-pane{display:none}
.tab-pane.active{display:block}
.concept-panel{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.concept-panel-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee)}
.concept-panel-hdr .icon{font-size:1.2rem}
.concept-panel-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.concept-panel-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700;letter-spacing:.04em}
.concept-panel-body{padding:1.1rem 1.2rem}
.concept-panel-body p,.concept-panel-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.concept-panel-body ul{margin:.4rem 0;padding-left:1.4rem}
.concept-panel-body li{margin-bottom:.3rem}
.panel-blue .concept-panel-hdr{background:#e8f1f9}
.panel-teal .concept-panel-hdr{background:#e0f0ee}
.panel-orange .concept-panel-hdr{background:#faeee4}
.panel-purple .concept-panel-hdr{background:#ede8f5}
.panel-green .concept-panel-hdr{background:#e2f0e8}
[data-theme="dark"] .panel-blue .concept-panel-hdr{background:#0d2030}
[data-theme="dark"] .panel-teal .concept-panel-hdr{background:#0a2420}
[data-theme="dark"] .panel-orange .concept-panel-hdr{background:#2a1808}
[data-theme="dark"] .panel-purple .concept-panel-hdr{background:#1e1028}
[data-theme="dark"] .panel-green .concept-panel-hdr{background:#0a2018}
.tag-blue{background:#d0e8f8;color:#1a4a7c}
.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}
.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}
.code-block{background:#0d1b2a;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1a7a6e}
.code-block pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.6;color:#a8d8c0;white-space:pre}
.c-comment{color:#5d8a70}
.c-key{color:#7ab8d8}
.c-val{color:#f0c080}
.c-type{color:#d8a0f8}
.c-macro{color:#f0d070}
.c-str{color:#f0a860}
.dpdk-box{background:#f0ecf8;border:1.5px solid #9b7bd0;border-left:4px solid #5b3a8c;border-radius:8px;padding:1rem 1.2rem;margin:1rem 0}
[data-theme="dark"] .dpdk-box{background:#1a1028;border-color:#7060a8;border-left-color:#9b7bd0}
.dpdk-box .dpdk-hdr{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.08em;color:#5b3a8c;margin-bottom:.5rem;text-transform:uppercase}
[data-theme="dark"] .dpdk-box .dpdk-hdr{color:#b090e8}
.dpdk-box ul{margin:0;padding-left:1.2rem}
.dpdk-box li{font-size:.87rem;line-height:1.65;color:var(--text-color,#222);margin-bottom:.25rem}
.insight-box{background:#e8f5f0;border:1.5px solid #1a7a6e;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme="dark"] .insight-box{background:#0a2420;border-color:#2a9a8e}
.insight-box p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.insight-box strong{color:#0e5248}
[data-theme="dark"] .insight-box strong{color:#5dd6c8}
.warn-box{background:#fff8e0;border:1.5px solid #d4a020;border-left:4px solid #c08000;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme="dark"] .warn-box{background:#2a2000;border-color:#c09020;border-left-color:#e0b040}
.warn-box p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.node-type-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:.8rem;margin:1rem 0}
.node-type-card{border-radius:8px;padding:.9rem 1rem;border:1.5px solid var(--border-color,#eee);background:var(--card-bg,#fff)}
.node-type-card h4{margin:0 0 .4rem;font-size:.88rem;font-weight:700;border:none;font-family:monospace}
.node-type-card p{margin:0;font-size:.83rem;line-height:1.6;color:var(--text-color,#555)}
.project-box{border:2px solid #c05e1b;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.project-box-hdr{background:#c05e1b;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.project-box-hdr .pnum{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.project-box-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.project-box-body{padding:1.1rem 1.2rem}
.project-box-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.project-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.project-step:last-of-type{border-bottom:none}
.project-step .step-n{background:#c05e1b;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.checklist{list-style:none;padding:0;margin:.5rem 0}
.checklist li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;border-radius:6px;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.checklist li:last-child{border-bottom:none}
.checklist li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#1a7a6e;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .next-btn{background:#1a7a6e;color:#fff !important;border-color:#1a7a6e}
.mod-nav .next-btn:hover{background:#22998a}
.section-sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">VPP MASTERY · PHASE 2B · WEEKS 5–6</div>
  <div class="mod-title">⚙️ vlib - Graph Dispatcher</div>
  <div class="mod-subtitle">Node Types · Dispatch Loop · Buffer Layout · Dual-Loop Pattern · Multi-Threading · Packet Tracing</div>
  <div class="mod-pills">
<span class="mod-pill">src/vlib/main.c</span>
<span class="mod-pill">src/vlib/node.h</span>
<span class="mod-pill">src/vlib/buffer.h</span>
<span class="mod-pill">2 Mini-Projects</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="switchTab(event,'t-nodes')">Node Types</button>
  <button class="tab-btn" onclick="switchTab(event,'t-dispatch')">Dispatch Loop</button>
  <button class="tab-btn" onclick="switchTab(event,'t-buffer')">Buffer Layout</button>
  <button class="tab-btn" onclick="switchTab(event,'t-dualloop')">Dual-Loop Pattern</button>
  <button class="tab-btn" onclick="switchTab(event,'t-threads')">Multi-Threading</button>
  <button class="tab-btn" onclick="switchTab(event,'t-trace')">Tracing &amp; Counters</button>
  <button class="tab-btn" onclick="switchTab(event,'t-proj')">Mini-Projects</button>
  <button class="tab-btn" onclick="switchTab(event,'t-check')">Checklist</button>
</div>
<!-- ══ NODE TYPES ══ -->
<div id="t-nodes" class="tab-pane active">
<p class="section-sep">THE FOUR NODE TYPES</p>
<div class="node-type-grid">
  <div class="node-type-card" style="border-left:4px solid #1a7a6e">
<h4 style="color:#1a7a6e">VLIB_NODE_TYPE_INPUT</h4>
<p>Polled by the dispatcher on every main loop iteration. Used for packet ingress (dpdk-input, pg-input, memif-input). Returns number of vectors processed - used to switch between polling and sleep modes.</p>
  </div>
  <div class="node-type-card" style="border-left:4px solid #1a3a5c">
<h4 style="color:#1a3a5c">VLIB_NODE_TYPE_INTERNAL</h4>
<p>Called only when another node enqueues packets to it via <code>vlib_frame_t</code>. The vast majority of nodes: ip4-lookup, ip4-rewrite, ethernet-input, your custom processing nodes.</p>
  </div>
  <div class="node-type-card" style="border-left:4px solid #5b3a8c">
<h4 style="color:#5b3a8c">VLIB_NODE_TYPE_PROCESS</h4>
<p>Cooperative coroutine - runs with <code>vlib_process_suspend()</code> and <code>vlib_process_wait_for_event()</code>. Used for slow-path: ARP resolution, control-plane responses. Never handles packets directly.</p>
  </div>
  <div class="node-type-card" style="border-left:4px solid #c05e1b">
<h4 style="color:#c05e1b">VLIB_NODE_TYPE_PRE_INPUT</h4>
<p>Called before INPUT nodes on every loop. Used for global preprocessing. Rare - only a few VPP nodes use this type.</p>
  </div>
</div>
<div class="concept-panel panel-teal">
  <div class="concept-panel-hdr"><span class="icon">📝</span><h3>Registering a Node - VLIB_REGISTER_NODE</h3><span class="tag tag-teal">MACRO PATTERN</span></div>
  <div class="concept-panel-body">
<div class="code-block"><pre><span class="c-comment">/* The node function - processes up to n_vectors packets */</span>
<span class="c-key">static</span> <span class="c-type">uword</span>
my_node_fn (<span class="c-type">vlib_main_t</span> * vm,
            <span class="c-type">vlib_node_runtime_t</span> * node,
            <span class="c-type">vlib_frame_t</span> * frame)
{
  <span class="c-type">u32</span> n_left_from, *from;
  from        = vlib_frame_vector_args(frame);   <span class="c-comment">/* array of buf indices */</span>
  n_left_from = frame->n_vectors;
 
  <span class="c-comment">/* ... process packets ... */</span>
  <span class="c-key">return</span> frame->n_vectors;   <span class="c-comment">/* always return vectors processed */</span>
}
 
<span class="c-comment">/* Node registration - at file scope, executed at startup */</span>
<span class="c-macro">VLIB_REGISTER_NODE</span> (my_node) = {
  .function      = my_node_fn,
  .name          = <span class="c-str">"my-node"</span>,
  .vector_size   = <span class="c-key">sizeof</span>(<span class="c-type">u32</span>),   <span class="c-comment">/* buffer index size */</span>
  .type          = VLIB_NODE_TYPE_INTERNAL,
  .n_errors      = MY_NODE_N_ERROR,
  .error_strings = my_node_error_strings,
  .n_next_nodes  = MY_NODE_N_NEXT,
  .next_nodes    = {
    [MY_NODE_NEXT_IP4_LOOKUP] = <span class="c-str">"ip4-lookup"</span>,
    [MY_NODE_NEXT_DROP]       = <span class="c-str">"error-drop"</span>,
  },
  <span class="c-comment">/* Optional: for show run output */</span>
  .format_trace  = format_my_node_trace,
};
 
<span class="c-comment">/* Error strings (for show error) */</span>
<span class="c-key">static char</span> *my_node_error_strings[] = {
<span class="c-macro">#define</span> _(n, s) s,
  <span class="c-macro">foreach_my_node_error</span>
<span class="c-macro">#undef</span> _
};</pre></div>
  </div>
</div>
</div>
<!-- ══ DISPATCH LOOP ══ -->
<div id="t-dispatch" class="tab-pane">
<p class="section-sep">MAIN LOOP - src/vlib/main.c</p>
<div class="concept-panel panel-blue">
  <div class="concept-panel-hdr"><span class="icon">🔄</span><h3>vlib_main_loop - The Heart of VPP</h3><span class="tag tag-blue">ARCHITECTURE</span></div>
  <div class="concept-panel-body">
<p>The dispatcher lives in <code>vlib_main_loop()</code>. You never write a main loop in VPP - the framework calls your nodes. Understanding the loop explains VPP's performance model.</p>
<div class="code-block">

```python
/* Simplified pseudocode of vlib_main_loop (src/vlib/main.c) */
while (1) {
  /* 1. Poll all INPUT nodes */
  foreach input_node:
    vectors = input_node.fn(vm, node, frame);
    /* vectors returned drives adaptive polling rate */

  /* 2. Run INTERNAL nodes that have pending frames */
  while pending_frames:
    dispatch_node(next_pending_node);
    /* this may enqueue more frames to other nodes */

  /* 3. Run PROCESS nodes that are ready */
  foreach ready_process:
    resume_process(proc);

  /* 4. Adaptive sleep if no work (avoids busy-spin at 0 pps) */
  if (total_vectors == 0):
    sleep_us(min(sleep_us * 2, max_sleep_us));
  else:
    sleep_us = 0;  /* busy poll when traffic present */
}
```



<p><strong>Frame lifecycle:</strong> When an INPUT node receives packets, it allocates a <code>vlib_frame_t</code> and fills it with buffer indices. It calls <code>vlib_frame_enqueue</code> to schedule INTERNAL nodes. The dispatcher runs each INTERNAL node when its frame is non-empty. Each INTERNAL node can enqueue further frames - the graph unfolds packet by packet.</p>
  </div>
</div>
<div class="concept-panel panel-teal">
  <div class="concept-panel-hdr"><span class="icon">📦</span><h3>vlib_frame_t - Passing Packets Between Nodes</h3><span class="tag tag-teal">DATA STRUCTURE</span></div>
  <div class="concept-panel-body">
<div class="code-block"><pre><span class="c-comment">/* A frame is a batch of buffer indices destined for one next node */</span>
<span class="c-type">typedef struct</span> {
  <span class="c-type">u16</span>  <span class="c-key">n_vectors</span>;     <span class="c-comment">/* number of valid buffer indices in this frame */</span>
  <span class="c-type">u16</span>  <span class="c-key">flags</span>;
  <span class="c-type">u32</span>  <span class="c-key">frame_flags</span>;
  <span class="c-comment">/* followed immediately by: u32 buffer_indices[n_vectors] */</span>
} <span class="c-type">vlib_frame_t</span>;
 
<span class="c-comment">/* Get the buffer index array from a frame */</span>
<span class="c-type">u32</span> *from = vlib_frame_vector_args(frame);
 
<span class="c-comment">/* Enqueue packet(s) to a next node */</span>
<span class="c-type">vlib_frame_t</span> *f = vlib_get_next_frame(vm, node, MY_NEXT_INDEX);
<span class="c-type">u32</span> *to = vlib_frame_vector_args(f);
to[0] = buf_index;
vlib_put_next_frame(vm, node, MY_NEXT_INDEX, <span class="c-comment">/* n_left_to_next= */</span> n_remaining);
 
<span class="c-comment">/* Modern API: enqueue by next index array (preferred for multi-next nodes) */</span>
<span class="c-type">u16</span> nexts[VLIB_FRAME_SIZE];
nexts[i] = MY_NODE_NEXT_IP4_LOOKUP;
vlib_buffer_enqueue_to_next(vm, node, from, nexts, n_vectors);</pre></div>
<div class="insight-box">
<p>💡 <strong>Frame size limit:</strong> <code>VLIB_FRAME_SIZE = 256</code>. No single node invocation processes more than 256 packets. This is by design - it bounds worst-case latency for other nodes. INPUT nodes should return early once they have 256 packets.</p>
</div>
  </div>
</div>
</div>
<!-- ══ BUFFER LAYOUT ══ -->
<div id="t-buffer" class="tab-pane">
<p class="section-sep">vlib_buffer_t - EVERY PACKET IS ONE OF THESE</p>
<div class="concept-panel panel-orange">
  <div class="concept-panel-hdr"><span class="icon">📋</span><h3>Buffer Memory Layout</h3><span class="tag tag-orange">src/vlib/buffer.h</span></div>
  <div class="concept-panel-body">
<div class="code-block"><pre><span class="c-comment">/* Simplified vlib_buffer_t (src/vlib/buffer.h) */</span>
<span class="c-type">typedef struct</span> {
  <span class="c-comment">/* ── Cache line 0: hot fields ──────────────────────── */</span>
  <span class="c-type">CLIB_CACHE_LINE_ALIGN_MARK</span>(cacheline0);
 
  <span class="c-type">u32</span> <span class="c-key">current_data</span>;    <span class="c-comment">/* offset from data_u8[] to current L2/L3 header */</span>
  <span class="c-type">u16</span> <span class="c-key">current_length</span>;  <span class="c-comment">/* bytes of valid data from current_data onwards */</span>
  <span class="c-type">u16</span> <span class="c-key">flags</span>;           <span class="c-comment">/* VLIB_BUFFER_IS_TRACED, etc. */</span>
  <span class="c-type">u32</span> <span class="c-key">flow_id</span>;         <span class="c-comment">/* per-packet flow identifier */</span>
  <span class="c-type">u32</span> <span class="c-key">next_buffer</span>;     <span class="c-comment">/* chained buffer index (for multi-seg packets) */</span>
  <span class="c-type">u32</span> <span class="c-key">current_config_index</span>; <span class="c-comment">/* feature arc state */</span>
  <span class="c-type">u8</span>  <span class="c-key">error</span>;           <span class="c-comment">/* error code set by any node */</span>
  <span class="c-type">u8</span>  <span class="c-key">n_add_refs</span>;      <span class="c-comment">/* reference count for cloning */</span>
  <span class="c-comment">/* ── Cache line 1: opaque per-node scratch space ───── */</span>
  <span class="c-type">CLIB_CACHE_LINE_ALIGN_MARK</span>(cacheline1);
  <span class="c-type">vnet_buffer_opaque_t</span> <span class="c-key">opaque</span>;   <span class="c-comment">/* vnet_buffer(b)->ip.adj_index, etc. */</span>
  <span class="c-comment">/* ── Cache line 2: second opaque area ──────────────── */</span>
  <span class="c-type">CLIB_CACHE_LINE_ALIGN_MARK</span>(cacheline2);
  <span class="c-type">vnet_buffer_opaque2_t</span> <span class="c-key">opaque2</span>; <span class="c-comment">/* for your plugin's scratch data */</span>
  <span class="c-comment">/* ── Cache line 3+: packet data ─────────────────────  */</span>
  <span class="c-type">u8</span> <span class="c-key">pre_data</span>[VLIB_BUFFER_PRE_DATA_SIZE]; <span class="c-comment">/* pre-data area (for encap) */</span>
  <span class="c-type">u8</span> <span class="c-key">data_u8</span>[0];    <span class="c-comment">/* actual packet bytes start here */</span>
} <span class="c-type">vlib_buffer_t</span>;</pre></div>
  </div>
</div>
<div class="concept-panel panel-blue">
  <div class="concept-panel-hdr"><span class="icon">🔧</span><h3>Working With Buffers - Essential Macros</h3><span class="tag tag-blue">REFERENCE</span></div>
  <div class="concept-panel-body">
<div class="code-block"><pre><span class="c-comment">/* Get pointer to current header (L2, L3, or wherever we are) */</span>
<span class="c-type">void</span> *hdr = vlib_buffer_get_current(b);
 
<span class="c-comment">/* Advance past current header (e.g. past Ethernet to reach IP) */</span>
vlib_buffer_advance(b, <span class="c-key">sizeof</span>(<span class="c-type">ethernet_header_t</span>));
<span class="c-comment">/* current_data += sizeof(eth_hdr); current_length -= sizeof(eth_hdr) */</span>
<span class="c-comment">/* Step back (e.g. to prepend an encap header) */</span>
vlib_buffer_advance(b, -<span class="c-key">sizeof</span>(<span class="c-type">ip4_header_t</span>));
 
<span class="c-comment">/* Access vnet buffer opaque (contains L3/L4 metadata) */</span>
<span class="c-type">vnet_buffer_opaque_t</span> *vo = vnet_buffer(b);
<span class="c-type">u32</span> adj_idx   = vo->ip.adj_index[VLIB_TX];
<span class="c-type">u32</span> sw_if_idx = vo->sw_if_index[VLIB_RX];
 
<span class="c-comment">/* Get buffer from index (O(1) - base + offset) */</span>
<span class="c-type">vlib_buffer_t</span> *b = vlib_get_buffer(vm, buf_index);
 
<span class="c-comment">/* Get buffer index from pointer */</span>
<span class="c-type">u32</span> bi = vlib_get_buffer_index(vm, b);
 
<span class="c-comment">/* Prefetch next buffer's header - critical for dual-loop perf */</span>
<span class="c-type">vlib_buffer_t</span> *p2 = vlib_get_buffer(vm, from[2]);
<span class="c-macro">CLIB_PREFETCH</span>(&p2->data, <span class="c-key">sizeof</span>(*ip0), LOAD);
 
<span class="c-comment">/* Allocate and free buffers */</span>
<span class="c-type">u32</span> bi;
vlib_buffer_alloc(vm, &bi, <span class="c-val">1</span>);    <span class="c-comment">/* allocate 1 buffer */</span>
vlib_buffer_free(vm, &bi, <span class="c-val">1</span>);     <span class="c-comment">/* free 1 buffer */</span>
<span class="c-comment">/* Clone a buffer (reference counting) */</span>
vlib_buffer_clone(vm, src_bi, &dst_bi, <span class="c-val">1</span>, head_end_offset);</pre></div>
<div class="dpdk-box">
<div class="dpdk-hdr">⚙️ vlib_buffer_t vs rte_mbuf</div>
<ul>
<li><strong>current_data</strong> ≈ <code>rte_mbuf.data_off</code> - both are byte offsets into the data area</li>
<li><strong>current_length</strong> ≈ <code>rte_mbuf.data_len</code> - both track the valid data span</li>
<li><strong>opaque / opaque2</strong> ≈ <code>rte_mbuf.udata64</code> / private mbuf area - per-packet scratch space</li>
<li><strong>next_buffer</strong> ≈ <code>rte_mbuf.next</code> - both support chained multi-segment packets</li>
<li><strong>Key difference</strong>: VPP passes <em>u32 indices</em> between nodes, not pointers - index-to-pointer conversion is a single array offset</li>
<li><strong>Pre-data area</strong>: VPP reserves bytes before <code>data_u8[]</code> for encap headers - you can prepend headers by moving <code>current_data</code> negative without a new buffer allocation</li>
</ul>
</div>
  </div>
</div>
</div>
<!-- ══ DUAL-LOOP ══ -->
<div id="t-dualloop" class="tab-pane">
<p class="section-sep">THE DUAL-LOOP PERFORMANCE PATTERN</p>
<div class="concept-panel panel-teal">
  <div class="concept-panel-hdr"><span class="icon">⚡</span><h3>Why Dual-Loop?</h3><span class="tag tag-teal">PERFORMANCE</span></div>
  <div class="concept-panel-body">
<p>Memory latency is the bottleneck in packet processing. A 64-byte cache line takes ~200 cycles to load from DRAM. Processing one packet at a time means those 200 cycles are wasted. The dual-loop pattern hides latency by <strong>prefetching packet N+2 while processing packet N</strong>.</p>
<p>Structure: an outer loop processes 2 packets per iteration (prefetch 2 ahead). When fewer than 4 remain, fall into a single loop. This is the canonical VPP pattern - used in <code>ip4-lookup</code>, <code>ip4-rewrite</code>, and every high-performance node.</p>
  </div>
</div>
<div class="concept-panel panel-blue">
  <div class="concept-panel-hdr"><span class="icon">🔧</span><h3>Dual-Loop Template - Annotated</h3><span class="tag tag-blue">CANONICAL PATTERN · src/vnet/ip/ip4_forward.c</span></div>
  <div class="concept-panel-body">
<div class="code-block"><pre><span class="c-key">static</span> <span class="c-type">uword</span>
my_node_fn (<span class="c-type">vlib_main_t</span> *vm, <span class="c-type">vlib_node_runtime_t</span> *node,
            <span class="c-type">vlib_frame_t</span> *frame)
{
  <span class="c-type">u32</span> n_left_from, *from;
  <span class="c-type">u16</span> nexts[VLIB_FRAME_SIZE], *next = nexts;
 
  from        = vlib_frame_vector_args(frame);
  n_left_from = frame->n_vectors;
 
  <span class="c-comment">/* ── Prefetch first 4 buffers before entering loop ── */</span>
  {
    <span class="c-type">vlib_buffer_t</span> *p;
    p = vlib_get_buffer(vm, from[0]); <span class="c-macro">vlib_prefetch_buffer_header</span>(p, LOAD);
    p = vlib_get_buffer(vm, from[1]); <span class="c-macro">vlib_prefetch_buffer_header</span>(p, LOAD);
    p = vlib_get_buffer(vm, from[2]); <span class="c-macro">vlib_prefetch_buffer_header</span>(p, LOAD);
    p = vlib_get_buffer(vm, from[3]); <span class="c-macro">vlib_prefetch_buffer_header</span>(p, LOAD);
  }
 
  <span class="c-comment">/* ── DUAL LOOP: 2 packets per iteration ─────────── */</span>
  <span class="c-key">while</span> (n_left_from >= <span class="c-val">4</span>) {
    <span class="c-type">vlib_buffer_t</span> *b0, *b1;
    <span class="c-type">u32</span> bi0, bi1;
 
    <span class="c-comment">/* Prefetch 2 buffers ahead (hides DRAM latency) */</span>
    {
      <span class="c-type">vlib_buffer_t</span> *p2 = vlib_get_buffer(vm, from[2]);
      <span class="c-type">vlib_buffer_t</span> *p3 = vlib_get_buffer(vm, from[3]);
      <span class="c-macro">vlib_prefetch_buffer_header</span>(p2, LOAD);
      <span class="c-macro">vlib_prefetch_buffer_header</span>(p3, LOAD);
      <span class="c-macro">CLIB_PREFETCH</span>(p2->data, CLIB_CACHE_LINE_BYTES, LOAD);
      <span class="c-macro">CLIB_PREFETCH</span>(p3->data, CLIB_CACHE_LINE_BYTES, LOAD);
    }
 
    bi0 = from[0]; bi1 = from[1];
    from += 2; n_left_from -= 2;
 
    b0 = vlib_get_buffer(vm, bi0);   <span class="c-comment">/* now in cache - no stall */</span>
    b1 = vlib_get_buffer(vm, bi1);
 
    <span class="c-comment">/* ── YOUR PROCESSING LOGIC FOR b0 AND b1 ── */</span>
    <span class="c-type">ip4_header_t</span> *ip0 = vlib_buffer_get_current(b0);
    <span class="c-type">ip4_header_t</span> *ip1 = vlib_buffer_get_current(b1);
 
    next[0] = classify_packet(ip0);   <span class="c-comment">/* determine next node */</span>
    next[1] = classify_packet(ip1);
    next += 2;
    <span class="c-comment">/* ─────────────────────────────────────────── */</span>
  }
 
  <span class="c-comment">/* ── SINGLE LOOP: handle remaining 0-3 packets ── */</span>
  <span class="c-key">while</span> (n_left_from > <span class="c-val">0</span>) {
    <span class="c-type">vlib_buffer_t</span> *b0 = vlib_get_buffer(vm, from[0]);
    next[0] = classify_packet(vlib_buffer_get_current(b0));
    from++; next++; n_left_from--;
  }
 
  <span class="c-comment">/* Enqueue all packets to their respective next nodes */</span>
  vlib_buffer_enqueue_to_next(vm, node, vlib_frame_vector_args(frame),
                              nexts, frame->n_vectors);
  <span class="c-key">return</span> frame->n_vectors;
}</pre></div>
  </div>
</div>
<div class="concept-panel panel-green">
  <div class="concept-panel-hdr"><span class="icon">🚀</span><h3>Modern "qs" Pattern - vlib_get_buffers</h3><span class="tag tag-green">VPP v22+</span></div>
  <div class="concept-panel-body">
<p>Newer VPP nodes use the "quad-single" helper which fetches all buffers upfront using SIMD-friendly bulk get:</p>
<div class="code-block"><pre><span class="c-comment">/* Bulk fetch all buffer pointers - compiler can vectorise */</span>
<span class="c-type">vlib_buffer_t</span> *bufs[VLIB_FRAME_SIZE];
vlib_get_buffers(vm, from, bufs, n_vectors);
 
<span class="c-comment">/* Now iterate bufs[] directly */</span>
<span class="c-key">for</span> (<span class="c-type">int</span> i = <span class="c-val">0</span>; i < n_vectors; i++) {
  nexts[i] = my_classify(bufs[i]);
}
 
vlib_buffer_enqueue_to_next(vm, node, from, nexts, n_vectors);</pre></div>
<p>Use the qs pattern for new nodes. Use the hand-written dual-loop when you need ultra-precise prefetch control for memory-intensive operations (e.g., FIB lookup with pointer chasing).</p>
  </div>
</div>
</div>
<!-- ══ THREADS ══ -->
<div id="t-threads" class="tab-pane">
<p class="section-sep">MULTI-THREADING MODEL</p>
<div class="concept-panel panel-purple">
  <div class="concept-panel-hdr"><span class="icon">🧵</span><h3>Per-Worker vlib_main_t</h3><span class="tag tag-purple">ARCHITECTURE</span></div>
  <div class="concept-panel-body">
<p>VPP uses a <strong>share-nothing</strong> threading model. Each worker thread has its own <code>vlib_main_t</code>, its own buffer pool, and its own set of graph nodes. There is <strong>no global lock on the fast path</strong>.</p>
<ul>
<li>Worker 0 handles RX queue 0 of each interface; Worker 1 handles RX queue 1; etc.</li>
<li>Each worker thread runs an independent copy of <code>vlib_main_loop</code></li>
<li>Workers never share packet ownership - a packet assigned to Worker 0 stays on Worker 0 unless explicitly handed off</li>
<li>The main thread (Thread 0) handles control-plane: PROCESS nodes, CLI, API requests</li>
</ul>
<div class="code-block"><pre><span class="c-comment">/* Get the current worker's vlib_main_t (in node function context) */</span>
<span class="c-type">vlib_main_t</span> *vm = ...;   <span class="c-comment">/* already passed to your node function */</span>
<span class="c-type">u32</span> thread_index = vm->thread_index;   <span class="c-comment">/* 0 = main, 1..N = workers */</span>
<span class="c-comment">/* Access another thread's vlib_main */</span>
<span class="c-type">vlib_main_t</span> *wm = vlib_get_main_by_index(worker_idx);
 
<span class="c-comment">/* Per-worker data in your plugin - index by thread_index */</span>
<span class="c-type">typedef struct</span> {
  <span class="c-type">my_flow_t</span>       *flow_pool;
  <span class="c-type">clib_bihash_8_8_t</span> flow_table;
} <span class="c-type">my_worker_t</span>;
 
<span class="c-type">my_main_t</span> *mm = &my_main;
<span class="c-type">my_worker_t</span> *w = vec_elt_at_index(mm->workers, vm->thread_index);</pre></div>
  </div>
</div>
<div class="concept-panel panel-orange">
  <div class="concept-panel-hdr"><span class="icon">🔀</span><h3>Handoff - Cross-Worker Packet Transfer</h3><span class="tag tag-orange">src/vlib/threads.c</span></div>
  <div class="concept-panel-body">
<p>Sometimes a packet must be processed by a specific worker - for example, if your plugin requires all packets of the same flow to be handled by the same thread (stateful processing). Use the <strong>handoff mechanism</strong>.</p>
<div class="code-block"><pre><span class="c-comment">/* Enqueue buffers to a different worker's input queue */</span>
<span class="c-type">u32</span> target_worker = compute_flow_worker(flow_id);
<span class="c-key">if</span> (target_worker != vm->thread_index) {
  vlib_buffer_enqueue_to_thread(vm, node,
                                handoff_queue_index,  <span class="c-comment">/* registered queue */</span>
                                &bi, &target_worker,
                                <span class="c-val">1</span>);   <span class="c-comment">/* n_buffers */</span>
}</pre></div>
<p>See <code>src/examples/handoffdemo/</code> for a complete working example. The handoff node approach is also used by the NAT plugin to ensure symmetric flow handling.</p>
<div class="warn-box">
<p>⚠️ <strong>Avoid unnecessary handoffs.</strong> Each cross-worker transfer adds latency and overhead. Design your hashing strategy (startup.conf <code>num-rx-queues</code> + RSS hash type) so packets of the same flow arrive at the same worker naturally through NIC RSS. Handoff is the fallback, not the primary mechanism.</p>
</div>
  </div>
</div>
</div>
<!-- ══ TRACE & COUNTERS ══ -->
<div id="t-trace" class="tab-pane">
<p class="section-sep">PACKET TRACING</p>
<div class="concept-panel panel-green">
  <div class="concept-panel-hdr"><span class="icon">🔍</span><h3>Adding Trace Support to Your Node</h3><span class="tag tag-green">DEBUGGING</span></div>
  <div class="concept-panel-body">
<div class="code-block"><pre><span class="c-comment">/* Step 1: define your trace structure */</span>
<span class="c-type">typedef struct</span> {
  <span class="c-type">u32</span> sw_if_index;
  <span class="c-type">u8</span>  next_index;
  <span class="c-type">u8</span>  error;
  <span class="c-type">u32</span> flow_id;
} <span class="c-type">my_node_trace_t</span>;
 
<span class="c-comment">/* Step 2: format function - called by 'show trace' */</span>
<span class="c-key">static</span> <span class="c-type">u8</span> *
format_my_node_trace (<span class="c-type">u8</span> *s, <span class="c-type">va_list</span> *args) {
  <span class="c-type">vlib_main_t</span> *vm = va_arg(*args, <span class="c-type">vlib_main_t</span> *);
  <span class="c-type">vlib_node_t</span> *node = va_arg(*args, <span class="c-type">vlib_node_t</span> *);
  <span class="c-type">my_node_trace_t</span> *t = va_arg(*args, <span class="c-type">my_node_trace_t</span> *);
  s = format(s, <span class="c-str">"MY-NODE: sw_if_index %d next %d flow 0x%x"</span>,
             t->sw_if_index, t->next_index, t->flow_id);
  <span class="c-key">return</span> s;
}
 
<span class="c-comment">/* Step 3: in your node function, check trace flag and record */</span>
<span class="c-key">if</span> (<span class="c-macro">PREDICT_FALSE</span>(b0->flags & VLIB_BUFFER_IS_TRACED)) {
  <span class="c-type">my_node_trace_t</span> *t = vlib_add_trace(vm, node, b0, <span class="c-key">sizeof</span>(*t));
  t->sw_if_index = vnet_buffer(b0)->sw_if_index[VLIB_RX];
  t->next_index  = next0;
  t->flow_id     = b0->flow_id;
}
 
<span class="c-comment">/* Step 4: in VLIB_REGISTER_NODE, set: */</span>
<span class="c-comment">/* .format_trace = format_my_node_trace */</span></pre></div>
  </div>
</div>
<div class="concept-panel panel-blue">
  <div class="concept-panel-hdr"><span class="icon">📊</span><h3>Error Counters - show error</h3><span class="tag tag-blue">OBSERVABILITY</span></div>
  <div class="concept-panel-body">
<div class="code-block"><pre><span class="c-comment">/* Define errors with a foreach macro (standard VPP convention) */</span>
<span class="c-macro">#define foreach_my_node_error</span>  \
  _(PROCESSED,   "packets processed") \
  _(NO_FLOW,     "flow not found")    \
  _(CHECKSUM,    "checksum error")
 
<span class="c-key">typedef enum</span> {
<span class="c-macro">#define</span> _(n,s) MY_NODE_ERROR_##n,
  <span class="c-macro">foreach_my_node_error</span>
<span class="c-macro">#undef</span> _
  MY_NODE_N_ERROR,
} <span class="c-type">my_node_error_t</span>;
 
<span class="c-key">static char</span> * my_node_error_strings[] = {
<span class="c-macro">#define</span> _(n,s) s,
  <span class="c-macro">foreach_my_node_error</span>
<span class="c-macro">#undef</span> _
};
 
<span class="c-comment">/* Increment a counter (atomic, safe from any worker) */</span>
vlib_node_increment_counter(vm, my_node.index,
                            MY_NODE_ERROR_PROCESSED, n_processed);</pre></div>
  </div>
</div>
</div>
<!-- ══ PROJECTS ══ -->
<div id="t-proj" class="tab-pane">
<div class="project-box">
  <div class="project-box-hdr"><span class="pnum">PROJECT 2</span><h4>Graph Node Inspector</h4></div>
  <div class="project-box-body">
<p><strong>Objective:</strong> Understand the dispatch loop and node statistics by observation - no code yet.</p>
<div class="project-step"><div class="step-n">1</div><div>Start VPP with the packet generator (<code>pg</code>) plugin. Create a <code>pg</code> interface and configure it as an L3 interface with an IP address.</div></div>
<div class="project-step"><div class="step-n">2</div><div>Generate traffic: <code>packet-generator new { name pg0 limit 10000 ... }</code>. Run <code>show run</code> before and after. Record vectors/call, clocks/vector for each active node.</div></div>
<div class="project-step"><div class="step-n">3</div><div>Use <code>trace add pg-input 50</code>, send 50 packets, then <code>show trace</code>. Map each line of the trace to the corresponding node function in the source tree.</div></div>
<div class="project-step"><div class="step-n">4</div><div>Set a breakpoint in GDB on <code>ip4_lookup</code>'s node function. Inspect <code>frame->n_vectors</code> and the first 4 buffer indices in <code>from[]</code>. Dereference one buffer index and read <code>current_data</code> and <code>current_length</code>.</div></div>
<div class="project-step"><div class="step-n">5</div><div>Increase pg traffic to 1M packets/sec. Re-run <code>show run</code>. Observe that vectors/call increases toward VLIB_FRAME_SIZE (256). Explain why.</div></div>
  </div>
</div>
<div class="project-box">
  <div class="project-box-hdr"><span class="pnum">PROJECT 3</span><h4>Custom Buffer Inspector Node</h4></div>
  <div class="project-box-body">
<p><strong>Objective:</strong> Write your first VPP plugin - a simple node that reads buffer headers and emits trace output. No packet modification yet.</p>
<div class="project-step"><div class="step-n">1</div><div>Copy <code>src/examples/sample-plugin/</code> to a new directory <code>src/plugins/buffer-inspector/</code>. Rename all symbols.</div></div>
<div class="project-step"><div class="step-n">2</div><div>Create an INTERNAL node with one next: <code>ip4-lookup</code>. In the node function, implement the dual-loop pattern. For each packet, read <code>current_data</code>, <code>current_length</code>, and the first 4 bytes of the IP header.</div></div>
<div class="project-step"><div class="step-n">3</div><div>Add trace support with a struct that stores: sw_if_index, IP src addr, IP dst addr, protocol. Implement <code>format_buffer_inspector_trace</code>.</div></div>
<div class="project-step"><div class="step-n">4</div><div>Add a feature arc registration so your node can be inserted into the <code>ip4-unicast</code> arc. Test with <code>set interface feature vpp0 buffer-inspector ip4-unicast enable</code>.</div></div>
<div class="project-step"><div class="step-n">5</div><div>Add error counters for: packets seen, packets with TTL==1, packets with unknown protocol. Verify they appear correctly in <code>show error</code>.</div></div>
<div class="project-step"><div class="step-n">6</div><div>Run under the VPP test framework: write a Python test that sends 100 packets through the interface and asserts that the "packets seen" counter equals 100.</div></div>
  </div>
</div>
</div>
<!-- ══ CHECKLIST ══ -->
<div id="t-check" class="tab-pane">
<p class="section-sep">P2B COMPLETION CHECKLIST</p>
<ul class="checklist">
  <li>Know all four node types and when to use each (INPUT, INTERNAL, PROCESS, PRE_INPUT)</li>
  <li>Understand <code>vlib_main_loop</code>: poll INPUT → dispatch INTERNAL frames → run PROCESS nodes</li>
  <li>Know <code>vlib_buffer_t</code> layout: <code>current_data</code>, <code>current_length</code>, opaque, pre-data area</li>
  <li>Can convert between buffer index and pointer; know why indices are passed between nodes, not pointers</li>
  <li>Can implement the dual-loop pattern with correct 2-ahead prefetch</li>
  <li>Understand the modern <code>vlib_get_buffers</code> + <code>vlib_buffer_enqueue_to_next</code> pattern</li>
  <li>Know VPP's share-nothing threading model: per-worker <code>vlib_main_t</code>, no fast-path locks</li>
  <li>Understand handoff: when it's needed and the overhead cost</li>
  <li>Can add trace support to a node with a custom <code>format_trace</code> function</li>
  <li>Can define and increment error counters that appear in <code>show error</code></li>
  <li>Completed Projects 2 and 3: graph inspector and buffer inspector node with traces + counters</li>
</ul>
</div>
<div class="mod-nav">
  <a href="/learning/data-plane/vpp/module-p2-vppinfra/">← P2A: vppinfra</a>
  <a href="/learning/data-plane/vpp/vpp-roadmap/">🗺️ Roadmap</a>
  <a class="next-btn" href="/learning/data-plane/vpp/module-p2-vnet/">Next: vnet →</a>
</div>
<script>
function switchTab(e,id){
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
</script>
