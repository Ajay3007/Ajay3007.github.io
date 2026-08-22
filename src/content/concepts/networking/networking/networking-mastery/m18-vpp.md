---
title: "M18 - VPP and Data Plane Development"
description: "NETWORKING MASTERY · PHASE 4 · MODULE 18 · WEEK 16 · PHASE 4 FINAL ⚡ VPP and Data Plane Development Vector packet processing · Graph node framework · VPP plugins · FIB · VAPI ·…"
domain: networking
track: networking-mastery
order: 18
ownHeader: true
url: /learning/networking-mastery/m18-vpp/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#1a2a1a 40%,#1a4a3a 70%,#0a3028 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#60d8b0;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#a0f0d8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#c8fff0}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#60d8b0;border-bottom-color:#60d8b0}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1a6a50}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#a0f0d8;white-space:pre}
.cm{color:#408060}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#e8f8f0;border:1.5px solid #1a6a50;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#081e14;border-color:#2a9a78}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#0a4a30}[data-theme=dark] .ins strong{color:#60d8b0}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#0a4a30;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a6a50}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #1a6a50;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#1a6a50;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#1a6a50;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#1a6a50;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
.phase-complete{background:linear-gradient(135deg,#0a2018,#1a6a50);border-radius:10px;padding:1.4rem 1.6rem;margin:2rem 0;border:1.5px solid #2a9a78;color:#fff}
.phase-complete h3{margin:0 0 .5rem;font-size:1.1rem;font-weight:800;color:#fff;border:none}
.phase-complete p{margin:0;font-size:.88rem;line-height:1.65;color:#c0f0e0}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 4 · MODULE 18 · WEEK 16 · PHASE 4 FINAL</div>
  <div class="mod-title">⚡ VPP and Data Plane Development</div>
  <div class="mod-subtitle">Vector packet processing · Graph node framework · VPP plugins · FIB · VAPI · NGFW data plane</div>
  <div class="mod-pills">
<span class="mod-pill">Advanced</span>
<span class="mod-pill">Prerequisite: M17 DPDK</span>
<span class="mod-pill">FD.io VPP 23.x</span>
<span class="mod-pill">Your Team's R&amp;D Platform</span>
<span class="mod-pill">3 Labs</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">VPP Architecture</button>
  <button class="tab-btn" onclick="vt(event,'t1')">Vector Processing</button>
  <button class="tab-btn" onclick="vt(event,'t2')">Graph Node Framework</button>
  <button class="tab-btn" onclick="vt(event,'t3')">Writing a Plugin</button>
  <button class="tab-btn" onclick="vt(event,'t4')">VPP FIB</button>
  <button class="tab-btn" onclick="vt(event,'t5')">VAPI and CLI</button>
  <button class="tab-btn" onclick="vt(event,'t6')">NGFW Data Plane</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Performance Tools</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Checklist</button>
</div>
<!-- ════ TAB 0 — VPP ARCHITECTURE ════ -->
<div id="t0" class="tab-pane active">
<p class="sep">VPP — VECTOR PACKET PROCESSOR (FD.io)</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>What VPP Is and Why Your Team Uses It</h3><span class="tag tag-teal">OVERVIEW</span></div>
  <div class="cp-body">
<p>VPP (Vector Packet Processor, FD.io project by Cisco/Linux Foundation) is a full-featured userspace network stack built on DPDK. Where DPDK is a toolkit for packet I/O, VPP is a complete forwarding engine with L2/L3/L4 processing, routing, NAT, ACL, GRE, VxLAN, MPLS, IPsec, and a plugin framework — running at tens to hundreds of millions of packets per second.</p>
<p>VPP is ideal for NGFW development because it provides the fast data plane and rich protocol support you'd otherwise spend years building from scratch, while leaving the door open for custom processing nodes via its plugin system.</p>
<table class="t-table">
<thead><tr><th>System</th><th>Mpps/core (64B)</th><th>Features available</th></tr></thead>
<tbody>
<tr><td>Linux kernel</td><td>1–3</td><td>Everything, but slow</td></tr>
<tr><td>DPDK bare (basicfwd)</td><td>30–80</td><td>Only what you code</td></tr>
<tr><td>VPP (L3 forwarding)</td><td>20–100</td><td>Full routing, NAT, ACL, tunnels — built-in</td></tr>
<tr><td>VPP + ACL plugin</td><td>15–60</td><td>+ stateful conntrack</td></tr>
<tr><td>VPP + IPsec</td><td>5–20</td><td>+ encryption (DPDK crypto offload available)</td></tr>
</tbody>
</table>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚙️</span><h3>VPP Startup Configuration</h3><span class="tag tag-blue">SETUP</span></div>
  <div class="cp-body">


```bash
# /etc/vpp/startup.conf — key sections

unix {
  nodaemon
  log /var/log/vpp/vpp.log
  full-coredump
  cli-listen /run/vpp/cli.sock   # vppctl connects here
}

dpdk {
  dev 0000:01:00.0 { name eth0 num-rx-queues 4 num-tx-queues 4 }
  dev 0000:01:00.1 { name eth1 num-rx-queues 4 num-tx-queues 4 }
  num-mbufs 131072
  socket-mem 2048,0   # 2GB hugepages on NUMA 0
}

cpu {
  main-core 0                   # main thread (management)
  corelist-workers 2,3,4,5      # 4 worker threads
}

buffers {
  buffers-per-numa 131072
  default data-size 2048
}

# Start VPP
sudo systemctl start vpp
sudo vppctl show version
sudo vppctl show interface
```


  </div>
</div>
</div>
<!-- ════ TAB 1 — VECTOR PROCESSING ════ -->
<div id="t1" class="tab-pane">
<p class="sep">VECTOR PROCESSING — VPP'S CORE INNOVATION</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔢</span><h3>Why Processing Vectors Beats One-at-a-Time</h3><span class="tag tag-purple">CONCEPT</span></div>
  <div class="cp-body">
<p>VPP's central innovation is processing a <em>batch (vector) of packets through each graph node at once</em>, rather than processing each packet through all nodes in sequence. This exploits CPU microarchitecture in four ways:</p>
<div class="two-col">
<div>
<h4>I-Cache Efficiency</h4>
<p>When the same code path executes for 32 packets in a row, the instruction cache stays warm throughout. One-at-a-time processing causes I-cache eviction between the lengthy gap between packet arrivals. VPP nodes measure vector sizes of 16–64 packets as optimal.</p>
<h4>Branch Predictor Warm</h4>
<p>Processing 32 IPv4 packets in a row means the same branches (version==4, ihl==5, no options) execute with the same outcome repeatedly. The CPU branch predictor achieves near-100% accuracy across the vector.</p>
</div>
<div>
<h4>Prefetch Pipelining</h4>
<p>While processing packet N, you prefetch packet N+4. The 100ns DRAM latency is hidden behind actual computation. The canonical VPP 4x unrolled loop with prefetch is specifically designed to fill the memory latency gap.</p>
<h4>SIMD Opportunity</h4>
<p>Processing multiple identical structures (IP headers) in sequence creates opportunities for AVX2/AVX512 SIMD optimisation — operating on 4–8 headers simultaneously. The VPP checksum and hash inner loops exploit this.</p>
</div>
</div>


```python
/* Vector size measurement */
show run
# Thread 1 vpp_wk_0:
#  Name               Calls  Vectors  Clocks   Vectors/Call
#  dpdk-input           100   3200    8.7e3     32.0
#  ip4-input            100   3200    1.9e3     32.0
#  ip4-lookup           100   3200    2.8e3     32.0
#  ip4-rewrite          100   3200    1.4e3     32.0
#
# Vectors/Call = average batch size (32 = optimal for most hardware)
# Clocks/Vector = CPU cycles per packet in this node
#   ip4-lookup: 2800 clocks / 32 packets = 87.5 clocks/packet = ~30ns at 3GHz
```


  </div>
</div>
</div>
<!-- ════ TAB 2 — GRAPH NODE FRAMEWORK ════ -->
<div id="t2" class="tab-pane">
<p class="sep">GRAPH NODE FRAMEWORK — PACKET PIPELINE ARCHITECTURE</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🕸️</span><h3>Nodes, Frames, and Packet Flow</h3><span class="tag tag-blue">GRAPH</span></div>
  <div class="cp-body">


```python
/* VPP graph: directed acyclic graph of processing nodes */
/* Each edge carries a vlib_frame_t — an array of buffer indices */

Default IP4 forwarding path:
  dpdk-input → ethernet-input → ip4-input → ip4-lookup → ip4-rewrite → interface-output

With ACL and NAT inserted:
  dpdk-input → ethernet-input → ip4-input
    → [ip4-unicast feature arc]:
        acl-plugin-in-ip4-fa     (ingress ACL + conntrack)
        nat44-ed-in2out           (NAT inbound)
    → ip4-lookup → ip4-rewrite
    → [ip4-output feature arc]:
        nat44-ed-out2in-worker    (NAT outbound)
        acl-plugin-out-ip4-fa     (egress ACL)
    → interface-output

/* Node types */
VLIB_NODE_TYPE_INPUT:    Poll loop entry (dpdk-input, tap-inject)
VLIB_NODE_TYPE_INTERNAL: Processing nodes (ip4-lookup, acl-plugin)
VLIB_NODE_TYPE_PRE_INPUT: Runs before INPUT (for scheduling)
VLIB_NODE_TYPE_PROCESS:  Background process threads

/* vlib_frame_t — the unit of work between nodes */
typedef struct {
    u16  n_vectors;         /* number of packets in this frame */
    u32  vector_offset;     /* offset to u32[] array of buffer indices */
} vlib_frame_t;

/* Get the array of buffer indices from a frame */
u32 *bufs = vlib_frame_vector_args(frame);
/* bufs[0..n_vectors-1] are indices into vlib_main.buffer_pool */

/* Get packet data from a buffer index */
vlib_buffer_t *b = vlib_get_buffer(vm, bufs[0]);
ip4_header_t  *ip = vlib_buffer_get_current(b);
/* vlib_buffer_get_current(b) = b->data + b->current_data */

/* Key node commands */
show vlib graph           # all nodes and their next-node connections
show vlib graph ip4-input # next nodes of ip4-input
show run                  # per-node performance (vectors, clocks)
show errors               # error counters per node
```


  </div>
</div>
</div>
<!-- ════ TAB 3 — WRITING A PLUGIN ════ -->
<div id="t3" class="tab-pane">
<p class="sep">WRITING A VPP PLUGIN — THE CANONICAL PATTERN</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔌</span><h3>Minimal Plugin with the 4x Unroll Pattern</h3><span class="tag tag-green">PLUGIN</span></div>
  <div class="cp-body">


```cpp
/* my_node.c — packet counter plugin with canonical 4x loop */
#include <vnet/vnet.h>
#include <vnet/plugin/plugin.h>
#include <vpp/app/version.h>

VLIB_PLUGIN_REGISTER() = {
    .version     = VPP_BUILD_VER,
    .description = "Packet counter plugin",
};

typedef enum { MY_NEXT_IP4_LOOKUP, MY_NEXT_DROP, MY_N_NEXT } my_next_t;

typedef struct {
    u64 pkt_count[VLIB_MAX_WORKERS + 1];  /* per-thread, no locking */
} my_main_t;
my_main_t my_main;

VLIB_NODE_FN(my_counter_node)(vlib_main_t *vm,
                               vlib_node_runtime_t *node,
                               vlib_frame_t *frame)
{
    u32 n_left = frame->n_vectors;
    u32 *from  = vlib_frame_vector_args(frame);
    u16 nexts[VLIB_FRAME_SIZE], *next = nexts;
    u64 pkts = 0;

    /* ── 4x unrolled loop with prefetch ─────────────── */
    while (n_left >= 8) {
        /* Prefetch packet data 4 ahead */
        vlib_prefetch_buffer_with_index(vm, from[4], LOAD);
        vlib_prefetch_buffer_with_index(vm, from[5], LOAD);
        vlib_prefetch_buffer_with_index(vm, from[6], LOAD);
        vlib_prefetch_buffer_with_index(vm, from[7], LOAD);

        /* Get 4 buffers */
        vlib_buffer_t *b0 = vlib_get_buffer(vm, from[0]);
        vlib_buffer_t *b1 = vlib_get_buffer(vm, from[1]);
        vlib_buffer_t *b2 = vlib_get_buffer(vm, from[2]);
        vlib_buffer_t *b3 = vlib_get_buffer(vm, from[3]);
        (void)b0; (void)b1; (void)b2; (void)b3;

        next[0] = next[1] = next[2] = next[3] = MY_NEXT_IP4_LOOKUP;
        from += 4; next += 4; n_left -= 4; pkts += 4;
    }
    /* ── Scalar tail ─────────────────────────────────── */
    while (n_left > 0) {
        next[0] = MY_NEXT_IP4_LOOKUP;
        from++; next++; n_left--; pkts++;
    }

    my_main.pkt_count[vm->thread_index] += pkts;

    vlib_buffer_enqueue_to_next(vm, node,
        vlib_frame_vector_args(frame), nexts, frame->n_vectors);
    return frame->n_vectors;
}

VLIB_REGISTER_NODE(my_counter_node) = {
    .name          = "my-counter",
    .vector_size   = sizeof(u32),
    .type          = VLIB_NODE_TYPE_INTERNAL,
    .n_next_nodes  = MY_N_NEXT,
    .next_nodes    = {
        [MY_NEXT_IP4_LOOKUP] = "ip4-lookup",
        [MY_NEXT_DROP]       = "error-drop",
    },
};

/* Insert into ip4-unicast feature arc on an interface */
/* vnet_feature_enable_disable("ip4-unicast", "my-counter", sw_if_index, 1, 0, 0); */

/* CMakeLists.txt */
# add_vpp_plugin(my_plugin SOURCES my_node.c API_FILES my_plugin.api)
# Plugins auto-loaded from /usr/lib/vpp_plugins/ at VPP startup
```


<div class="ins"><p>💡 <strong>The 4x unroll + prefetch pattern is canonical VPP.</strong> Every performance-critical node in VPP core uses this exact structure. The prefetch distance of 4 is tuned for typical L1/L2 miss latency (~60–100ns) on Intel Xeon. Copy this template when writing your own DPI or NGFW nodes.</p></div>
  </div>
</div>
</div>
<!-- ════ TAB 4 — VPP FIB ════ -->
<div id="t4" class="tab-pane">
<p class="sep">VPP FIB — THE MULTI-LAYER FORWARDING DATABASE</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🗺️</span><h3>VPP FIB Architecture</h3><span class="tag tag-blue">FIB</span></div>
  <div class="cp-body">


```bash
/* VPP FIB is a three-layer structure */

Layer 1: IP4 FIB table (per VRF)
  Hash table → O(1) exact match for /32 host routes
  mtrie       → LPM for all other prefixes (4-level trie, 8 bits/level)

Layer 2: Load-Balance (LB) object
  Created when a prefix has multiple equal-cost next-hops (ECMP)
  Contains N hash buckets, each pointing to an adjacency
  Flow-hash over 5-tuple selects bucket (consistent per flow)

Layer 3: Adjacency
  Pre-built rewrite string: "dst_mac src_mac ethertype" (14 bytes)
  Stored as raw bytes — ip4-rewrite just memcpy's directly into packet
  Interface index for output

/* FIB inspection commands */
show ip fib                     # entire IPv4 FIB (can be huge)
show ip fib table 0             # VRF 0 (default)
show ip fib 10.0.0.0/8         # specific prefix details
show ip fib 8.8.8.8/32         # host route
show ip fib summary             # count of prefixes by length
show ip adjacency               # all adjacency objects
show ip adjacency 42            # specific adjacency: rewrite bytes, interface
show ip adjacency summary       # count by type (glean/rewrite/midchain)

/* Route management */
ip route add 10.0.0.0/8 via 192.168.1.1 GigabitEthernet0/8/0
ip route del 10.0.0.0/8 via 192.168.1.1 GigabitEthernet0/8/0

/* ECMP: add same prefix twice = LB with 2 buckets */
ip route add 10.0.0.0/8 via 192.168.1.1 GigabitEthernet0/8/0
ip route add 10.0.0.0/8 via 192.168.1.2 GigabitEthernet0/8/1
show ip fib 10.0.0.0/8
# Displays: load-balance [index N] buckets 2
#             [0]: adj[via 192.168.1.1 GigE0/8/0]
#             [1]: adj[via 192.168.1.2 GigE0/8/1]

/* Null routes — blackhole */
ip route add 192.0.2.0/24 drop
ip route add 198.51.100.0/24 local  # deliver to local stack

/* Multiple VRFs (for tenant isolation in NGFW) */
ip table add 100
ip route add table 100 0.0.0.0/0 via 10.100.0.1 GigabitEthernet0/8/0
set interface ip table GigabitEthernet0/8/2 100  # assign interface to VRF 100
```


  </div>
</div>
</div>
<!-- ════ TAB 5 — VAPI AND CLI ════ -->
<div id="t5" class="tab-pane">
<p class="sep">VAPI AND CLI — CONTROLLING VPP FROM CODE AND SCRIPTS</p>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">🔌</span><h3>VPP Control Plane Interfaces</h3><span class="tag tag-amber">VAPI</span></div>
  <div class="cp-body">


```python
/* Three control interfaces */

1. vppctl CLI — interactive and scripted
   vppctl show version
   vppctl ip route add 0.0.0.0/0 via 10.0.0.1
   echo "show ip fib summary" | vppctl
   vppctl exec /etc/vpp/setup.vpp   # run a config file

2. Python VAPI — programmatic automation
import vpp_papi
from vpp_papi import VPP

vpp = VPP(['/usr/share/vpp/api/vpe.api.json',
           '/usr/share/vpp/api/interface.api.json',
           '/usr/share/vpp/api/ip.api.json'])
vpp.connect('my-control-app')

# Show version
rv = vpp.api.show_version()
print(f"VPP version: {rv.version.decode()}")

# Add an IP route
from ipaddress import ip_address, ip_network
rv = vpp.api.ip_route_add_del(
    is_add=1,
    route={
        'prefix': {'address': {'af': 0, 'un': {'ip4': b'\x00\x00\x00\x00'}},
                   'len': 0},
        'n_paths': 1,
        'paths': [{'nh': {'address': {'af': 0,
                                       'un': {'ip4': b'\x0a\x00\x00\x01'}}},
                   'sw_if_index': 1,
                   'proto': 0}]
    }
)

# Create loopback interface
rv = vpp.api.create_loopback()
sw_if_index = rv.sw_if_index

vpp.disconnect()

3. VAT2 (JSON-based API test tool)
   # vat2 show_version
   # vat2 show_interface sw_if_index 0

/* Useful diagnostic commands */
show interface                    # all interfaces, TX/RX stats
show hardware-interfaces          # NIC capabilities, link state
show run                          # node performance (vectors/call, clocks)
show run summary                  # top CPU-consuming nodes
show errors                       # drop counters per node
show buffers                      # mempool usage
show threads                      # worker thread info and CPU pinning
show plugins                      # loaded plugins
show log                          # VPP log buffer
```


  </div>
</div>
</div>
<!-- ════ TAB 6 — NGFW DATA PLANE ════ -->
<div id="t6" class="tab-pane">
<p class="sep">VPP AS AN NGFW DATA PLANE</p>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>Building an NGFW Data Plane on VPP</h3><span class="tag tag-red">NGFW</span></div>
  <div class="cp-body">
<p>VPP's feature arc system lets you insert custom processing nodes into the packet pipeline without modifying VPP core. The <code>ip4-unicast</code> arc is the primary insertion point for NGFW functions on inbound IPv4 traffic.</p>


```bash
/* NGFW pipeline using VPP feature arcs */

ip4-input
  ↓ [ip4-unicast feature arc — ordered by feature weight]
  ├── acl-plugin-in-ip4-fa      (stateful conntrack + ACL rules)
  ├── nat44-ed-in2out            (DNAT / inbound NAT)
  ├── ipsec-input-ip4            (IPsec decrypt)
  └── YOUR-NGFW-DPI-NODE         (your custom DPI plugin)
  ↓
ip4-lookup → ip4-rewrite
  ↓ [ip4-output feature arc]
  ├── nat44-ed-out2in-worker     (SNAT / outbound NAT)
  └── acl-plugin-out-ip4-fa     (egress ACL)
  ↓
interface-output

/* Enable your plugin on an interface */
vnet_feature_enable_disable("ip4-unicast", "my-ngfw-dpi", sw_if_index, 1, 0, 0);

/* VPP ACL plugin — built-in stateful firewall */
# Create an ACL (permit HTTPS, permit HTTP, deny all)
acl_add_replace acl_index 0 r {is_permit 1 proto 6 dst_port 443 443 dst_ip 0.0.0.0/0},
                               {is_permit 1 proto 6 dst_port 80  80  dst_ip 0.0.0.0/0},
                               {is_permit 0}

# Apply to interface (inbound = filter traffic entering through eth0)
set acl-list interface GigabitEthernet0/8/0 input 0

/* VPP NAT44 — stateful NAT */
nat44 enable sessions 65536
set interface nat44 in GigabitEthernet0/8/0 out GigabitEthernet0/8/1
nat44 add interface address GigabitEthernet0/8/1

/* Connection tracking for custom node */
/* Access conntrack state from within your node: */
clib_bihash_kv_16_8_t kv;
/* Key = 5-tuple; Value = session state struct */
if (!clib_bihash_search_16_8(&ngfw_main.session_table, &kv, &kv)) {
    ngfw_session_t *s = (ngfw_session_t *)(uword)kv.value;
    /* session found — check state, increment counters */
}
```


<div class="ins"><p>💡 <strong>VPP clib_bihash is your primary data structure for session tables.</strong> It's a cache-friendly, lock-free concurrent hash table that VPP uses internally for ARP, FIB, and conntrack. For your NGFW session table keyed on 5-tuple, <code>clib_bihash_16_8</code> (16-byte key = 5-tuple, 8-byte value = session index) achieves ~100ns lookup at millions of sessions — far better than any kernel-side alternative.</p></div>
  </div>
</div>
</div>
<!-- ════ TAB 7 — PERFORMANCE TOOLS ════ -->
<div id="t7" class="tab-pane">
<p class="sep">VPP PERFORMANCE ANALYSIS TOOLS</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Reading show run and Diagnosing Bottlenecks</h3><span class="tag tag-green">PERF TOOLS</span></div>
  <div class="cp-body">


```python
/* show run output — interpreting the numbers */
vppctl show run
# Thread 1 vpp_wk_0 (lcore 2):
#   Name               State  Calls  Vectors  Clocks      Vec/Call  Clk/Vec
#   dpdk-input         active  1000  32000    8.70e+06     32.0     272
#   ip4-input          active  1000  32000    1.92e+06     32.0      60
#   ip4-lookup         active  1000  32000    2.84e+06     32.0      89
#   ip4-rewrite        active  1000  32000    1.44e+06     32.0      45
#   my-ngfw-dpi        active  1000  32000    9.60e+06     32.0     300

# Clk/Vec = CPU cycles per packet in this node (at 3GHz: 300 cycles = 100ns)
# Sum of all Clk/Vec = total cycles per packet through the pipeline
# my-ngfw-dpi is the bottleneck here (300 cycles vs 60-89 for built-ins)

/* Optimisation workflow */
1. Run: vppctl clear run; sleep 5; vppctl show run
2. Identify highest Clk/Vec node (your bottleneck)
3. Check: are we prefetching? 4x unrolled? NUMA-local memory?
4. Profile: perf stat -e cycles,cache-misses -C 2 sleep 5
5. Check vector sizes: Vectors/Call /* show errors — drop counter diagnosis */
vppctl show errors
# ip4-input: ip4 src address is multicast    12
# ip4-input: ip4 spoofed local-address       5
# acl-plugin-in-ip4-fa: ACL deny packets  4821

/* Buffer pressure — detect mempool exhaustion */
vppctl show buffers
# If "allocated" approaches "total": mempool running low → increase num-mbufs

/* Per-interface counters */
vppctl show interface GigabitEthernet0/8/0
# RX packets/bytes, TX packets/bytes, drops, errors
vppctl clear interfaces   # reset counters

/* Packet capture in VPP (pcap trace) */
pcap dispatch trace on max 1000 file /tmp/vpp.pcap
# ... generate traffic ...
pcap dispatch trace off
# Open /tmp/vpp.pcap in Wireshark — shows packet at each graph node!
```


  </div>
</div>
</div>
<!-- ════ TAB 8 — LABS ════ -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>VPP from Zero to Forwarding Packet</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Install VPP, configure interfaces and routing, verify packet forwarding, explore the FIB and graph.</p>
<div class="lab-step"><div class="sn">1</div><div>Install VPP: <code>sudo apt install vpp vpp-plugin-core vpp-plugin-dpdk</code>. Use tap interfaces for testing (no physical NIC required): create two tap interfaces in startup.conf using <code>tuntap { dev tap0 }</code>. Start VPP and verify: <code>sudo vppctl show version</code>.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Configure interfaces: <code>vppctl set interface state tap0 up</code>, <code>vppctl set interface ip address tap0 10.1.0.1/24</code>. Add a static route: <code>vppctl ip route add 10.2.0.0/24 via 10.1.0.2 tap0</code>. Inspect the FIB: <code>vppctl show ip fib</code>. Find the adjacency for your route: <code>vppctl show ip adjacency</code>.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Explore the graph: <code>vppctl show vlib graph ip4-input</code> — note the next nodes. Generate traffic (ping through tap interface) and run <code>vppctl show run</code>. Identify which nodes execute and their Clk/Vec values. Calculate: at your measured Clk/Vec, what is the maximum Mpps per core?</div></div>
<div class="lab-step"><div class="sn">4</div><div>Test ACL: create a deny-all ACL and apply to tap0 inbound: <code>vppctl acl_add_replace acl_index 0 r {is_permit 0}</code>, <code>vppctl set acl-list interface tap0 input 0</code>. Verify pings are dropped. Check: <code>vppctl show errors</code> — see the ACL deny counter increment.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Write a Custom VPP Counter Plugin</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Write, build, and load a VPP plugin that counts packets per source IP using clib_bihash.</p>
<div class="lab-step"><div class="sn">1</div><div>Set up the VPP development environment: <code>sudo apt install vpp-dev</code>. Create a plugin directory structure: <code>my_plugin/CMakeLists.txt</code> and <code>my_plugin/my_node.c</code>. Use the template from Tab 3.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Extend the template: add a <code>clib_bihash_8_8_t</code> (key=src_ip u64, value=pkt_count u64). In the processing loop, extract the source IP from the IP header, look up/insert in the hash table, increment the count. Handle IPv4 only; pass all packets to ip4-lookup.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Add a CLI command to display the top-10 source IPs by packet count. Register with: <code>VLIB_CLI_COMMAND(show_top_sources_cmd, static) = { .path = "show ngfw top-sources", .function = show_top_sources_fn }</code>.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Build: <code>mkdir build && cd build && cmake .. && make</code>. Copy the .so to VPP plugin directory. Restart VPP and verify the plugin loads: <code>vppctl show plugins | grep my</code>. Enable on an interface, generate traffic, and run your CLI command.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>NGFW Prototype — ACL + NAT + Custom Node</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Assemble a minimal NGFW data plane with VPP's ACL plugin, NAT44, and your custom counter node all operating in the same pipeline.</p>
<div class="lab-step"><div class="sn">1</div><div>Configure VPP with two interfaces: inside (tap0, 10.1.0.1/24) and outside (tap1, 203.0.113.1/24). Enable NAT44: <code>nat44 enable sessions 1024</code>, <code>set interface nat44 in tap0 out tap1</code>, <code>nat44 add interface address tap1</code>.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Apply an ACL on the inside interface: permit TCP 443, permit TCP 80, permit ICMP, deny all else. Test: verify HTTP/HTTPS traffic passes, Telnet (port 23) is dropped. Check <code>show errors</code> for ACL deny counts.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Enable your counter plugin from Lab 2 on the inside interface. Generate mixed traffic (ICMP, TCP 80, TCP 443). Run your <code>show ngfw top-sources</code> command and verify counts. Use <code>show run</code> to confirm your node's Clk/Vec — compare it to the built-in ACL node.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Capture packets at each stage using VPP's pcap trace: <code>pcap dispatch trace on max 500 file /tmp/vpp.pcap</code>. Open in Wireshark and identify the same packet at different graph nodes. Observe: pre-NAT vs post-NAT IP addresses confirming NAT rewrote the packet.</div></div>
  </div>
</div>
</div>
<!-- ════ TAB 9 — CHECKLIST ════ -->
<div id="t9" class="tab-pane">
<p class="sep">M18 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know VPP's position: full-featured userspace network stack on DPDK, not just I/O toolkit</li>
  <li>Know VPP performance range: 20–100 Mpps/core for L3 forwarding; 15–60 with ACL; 5–20 with IPsec</li>
  <li>Know the 4 CPU microarchitectural benefits of vector processing: I-cache, branch predictor, prefetch pipeline, SIMD</li>
  <li>Know what Vectors/Call and Clocks/Vector mean in show run output and how to use them for bottleneck diagnosis</li>
  <li>Know the VPP graph: nodes receive vlib_frame_t (array of buffer indices), process, dispatch to next nodes</li>
  <li>Know node types: INPUT (polling), INTERNAL (processing), PROCESS (background)</li>
  <li>Know the canonical 4x unroll + prefetch pattern: prefetch N+4 while processing N; 8-packet outer loop</li>
  <li>Know feature arcs: ip4-unicast and ip4-output arcs allow inserting custom nodes without modifying VPP core</li>
  <li>Know VLIB_REGISTER_NODE fields: name, vector_size, type, n_next_nodes, next_nodes array</li>
  <li>Know VPP FIB three layers: FIB table (hash + mtrie) → load-balance object → adjacency (pre-built rewrite)</li>
  <li>Know vppctl route commands: ip route add/del, ECMP via multiple add of same prefix</li>
  <li>Know null routes: ip route add prefix drop/local</li>
  <li>Know VRF support: ip table add N; set interface ip table sw_if_index N</li>
  <li>Know three control interfaces: vppctl CLI, Python VAPI, VAT2</li>
  <li>Know key diagnostic commands: show run, show errors, show interface, show buffers, show plugins, pcap dispatch trace</li>
  <li>Know VPP ACL plugin: stateful conntrack + rule matching; set acl-list interface in/out</li>
  <li>Know VPP NAT44: set interface nat44 in/out; nat44 add interface address</li>
  <li>Know clib_bihash as the primary data structure for session tables in VPP plugins</li>
  <li>Completed Lab 1: installed VPP, configured tap interfaces, routing, ACL; read FIB and graph</li>
  <li>Completed Lab 2: wrote plugin with clib_bihash per-IP counter and CLI show command</li>
  <li>Completed Lab 3: assembled ACL + NAT44 + custom node pipeline; pcap-traced through all stages</li>
</ul>
<div class="phase-complete">
  <h3>🎉 Phase 4 Complete — Linux Networking and Socket Programming</h3>
  <p>You have completed all 5 modules of Phase 4: Linux Network Stack (M14), Socket Programming (M15), eBPF and XDP (M16), DPDK (M17), and VPP (M18). You now have a complete and deep understanding of the Linux networking toolkit from kernel internals to the most advanced data-plane frameworks. Move to <strong>Phase 5 — Security Protocols</strong>, starting with <strong>M19 - Cryptography Foundations</strong>.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/networking-mastery/m17-dpdk/">← M17 DPDK</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m19-cryptography/">Next: M19 - Cryptography →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
