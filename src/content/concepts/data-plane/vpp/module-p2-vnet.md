---
title: "VPP P2C - vnet - Networking Layer"
description: "VPP MASTERY · PHASE 2C · WEEKS 7–8 🌐 vnet - Networking Layer sw if index · Feature Arcs · FIB / DPO · ARP · Interface Abstraction src/vnet/ sw if index feature arcs FIB · DPO…"
domain: data-plane
track: vpp
order: 2
ownHeader: true
url: /learning/data-plane/vpp/module-p2-vnet/
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
.arc-flow{background:#f5f8ff;border:1.5px solid #b0c8e8;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto}
[data-theme="dark"] .arc-flow{background:#0d1828;border-color:#304860}
.arc-flow pre{margin:0;font-family:monospace;font-size:.83rem;line-height:1.7;color:var(--text-color,#222);white-space:pre}
[data-theme="dark"] .arc-flow pre{color:#c0d8f0}
.fib-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.87rem}
.fib-table th{background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.76rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.fib-table td{padding:.45rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.fib-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.fib-table code{font-size:.78rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a7a6e}
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
  <div class="mod-eyebrow">VPP MASTERY · PHASE 2C · WEEKS 7–8</div>
  <div class="mod-title">🌐 vnet - Networking Layer</div>
  <div class="mod-subtitle">sw_if_index · Feature Arcs · FIB / DPO · ARP · Interface Abstraction</div>
  <div class="mod-pills">
<span class="mod-pill">src/vnet/</span>
<span class="mod-pill">sw_if_index</span>
<span class="mod-pill">feature arcs</span>
<span class="mod-pill">FIB · DPO</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="switchTab(event,'t-ifidx')">sw_if_index</button>
  <button class="tab-btn" onclick="switchTab(event,'t-arcs')">Feature Arcs</button>
  <button class="tab-btn" onclick="switchTab(event,'t-fib')">FIB &amp; DPO</button>
  <button class="tab-btn" onclick="switchTab(event,'t-arp')">ARP &amp; Neighbours</button>
  <button class="tab-btn" onclick="switchTab(event,'t-l2')">L2 Bridging</button>
  <button class="tab-btn" onclick="switchTab(event,'t-check')">Checklist</button>
</div>
<!-- ══ SW_IF_INDEX ══ -->
<div id="t-ifidx" class="tab-pane active">
<p class="section-sep">THE UNIVERSAL INTERFACE HANDLE</p>
<div class="concept-panel panel-teal">
  <div class="concept-panel-hdr"><span class="icon">🔌</span><h3>sw_if_index - VPP's Interface Abstraction</h3><span class="tag tag-teal">CORE CONCEPT</span></div>
  <div class="concept-panel-body">
<p>Every interface in VPP - DPDK physical port, memif, TAP, loopback, VLAN sub-interface - is represented by a single <strong>u32 software interface index</strong>. Graph nodes never deal with concrete interface types; they always refer to interfaces by <code>sw_if_index</code>.</p>
<p>There are two levels of interface index:</p>
<ul>
<li><strong>hw_if_index</strong> - hardware interface: corresponds to a physical device or PMD (e.g., the DPDK port). One per physical NIC port.</li>
<li><strong>sw_if_index</strong> - software interface: can be the base interface OR a sub-interface (VLAN, QinQ). Multiple sw_if_index values can share one hw_if_index.</li>
</ul>
<div class="code-block"><pre><span class="c-comment">/* Get sw_if_index from a received packet */</span>
<span class="c-type">u32</span> sw_if_index = vnet_buffer(b)->sw_if_index[VLIB_RX];
 
<span class="c-comment">/* Get sw_if_index by name (for CLI/API handlers) */</span>
<span class="c-type">vnet_main_t</span> *vnm = vnet_get_main();
<span class="c-type">u32</span> sw_if_index = vnet_sw_interface_find_by_name(vnm, <span class="c-str">"GigabitEthernet0/8/0"</span>);
 
<span class="c-comment">/* Get interface details */</span>
<span class="c-type">vnet_sw_interface_t</span> *sw = vnet_get_sw_interface(vnm, sw_if_index);
<span class="c-type">vnet_hw_interface_t</span> *hw = vnet_get_hw_interface(vnm, sw->hw_if_index);
 
<span class="c-comment">/* Set interface admin state */</span>
vnet_sw_interface_set_flags(vnm, sw_if_index, VNET_SW_INTERFACE_FLAG_ADMIN_UP);
 
<span class="c-comment">/* Assign IP address programmatically (from a plugin) */</span>
<span class="c-type">ip4_add_del_interface_address_args_t</span> a = {
  .sw_if_index = sw_if_index,
  .address     = { .as_u32 = addr },
  .address_length = 24,
  .is_add      = 1,
};
vl_api_ip4_add_del_interface_address_t_handler(&a);</pre></div>
<div class="dpdk-box">
<div class="dpdk-hdr">⚙️ DPDK PARALLEL</div>
<ul>
<li><strong>sw_if_index ≈ port_id in DPDK</strong> - but sw_if_index is virtual and can represent logical interfaces above the physical device</li>
<li>In DPDK you call <code>rte_eth_rx_burst(port_id, queue_id, ...)</code>. In VPP the dpdk-input node calls it internally and stamps <code>vnet_buffer(b)->sw_if_index[VLIB_RX] = sw_if_index</code></li>
<li>Sub-interfaces are transparent - a VLAN tag on <code>sw_if_index=3</code> may resolve to <code>sw_if_index=5</code> after L2 classification, without any code change in your L3 node</li>
</ul>
</div>
  </div>
</div>
</div>
<!-- ══ FEATURE ARCS ══ -->
<div id="t-arcs" class="tab-pane">
<p class="section-sep">COMPOSABLE PACKET PIPELINES</p>
<div class="concept-panel panel-blue">
  <div class="concept-panel-hdr"><span class="icon">🔗</span><h3>Feature Arcs - What They Are</h3><span class="tag tag-blue">src/vnet/feature/</span></div>
  <div class="concept-panel-body">
<p>A feature arc is a <strong>per-interface ordered list of processing nodes</strong> that a packet traverses before the main routing/forwarding node. Features are registered at compile time, enabled per-interface at runtime via CLI or API. They are VPP's mechanism for composable, modular packet processing.</p>
<div class="arc-flow"><pre>Packet arrives at ip4-input
        │
        ▼
[ip4-unicast arc - per interface, in priority order]
  ┌─────────────────────────────────────────────────┐
  │  feature: ip4-full-reassembly (priority 50)     │
  │  feature: acl-plugin-in-ip4-fa (priority 40)    │
  │  feature: nat44-in2out (priority 30)             │
  │  feature: your-custom-node (priority 20)   ←──── inserted by you
  └─────────────────────────────────────────────────┘
        │
        ▼
ip4-lookup  (main forwarding - arc terminal)</pre></div>
<p>The framework calls <code>vnet_feature_next()</code> at the end of each feature node to advance to the next registered feature, or to the terminal node if none remain. Packets skip disabled features automatically - zero overhead per disabled feature.</p>
  </div>
</div>
<div class="concept-panel panel-teal">
  <div class="concept-panel-hdr"><span class="icon">📝</span><h3>Registering Your Node in an Arc</h3><span class="tag tag-teal">PATTERN</span></div>
  <div class="concept-panel-body">
<div class="code-block"><pre><span class="c-comment">/* In your plugin .c file: register as a feature in ip4-unicast arc */</span>
<span class="c-macro">VNET_FEATURE_INIT</span> (my_feature, <span class="c-key">static</span>) = {
  .arc_name    = <span class="c-str">"ip4-unicast"</span>,       <span class="c-comment">/* arc to join */</span>
  .node_name   = <span class="c-str">"my-feature-node"</span>,   <span class="c-comment">/* your node name */</span>
  .runs_before = VNET_FEATURES(<span class="c-str">"ip4-lookup"</span>),  <span class="c-comment">/* ordering constraint */</span>
  .runs_after  = VNET_FEATURES(<span class="c-str">"ip4-full-reassembly-feature"</span>),
};
 
<span class="c-comment">/* In your node function: advance to next feature when done */</span>
<span class="c-key">static</span> <span class="c-type">uword</span> my_feature_fn(...) {
  <span class="c-type">u32</span> next_index;
  <span class="c-type">u32</span> bi0 = from[0];
  <span class="c-type">vlib_buffer_t</span> *b0 = vlib_get_buffer(vm, bi0);
 
  <span class="c-comment">/* Determine next feature in arc (not a hard-coded node name!) */</span>
  vnet_feature_next(&next_index, b0);   <span class="c-comment">/* reads current_config_index */</span>
  <span class="c-comment">/* OR: early exit - bypass remaining features and go direct to drop */</span>
  next_index = VNET_FEATURE_ARC_DROP_INDEX;
 
  vlib_buffer_enqueue_to_next(vm, node, from, &next_index, 1);
  <span class="c-key">return</span> 1;
}
 
<span class="c-comment">/* Enable per interface via CLI */</span>
<span class="c-comment">/* set interface feature GigabitEthernet0/8/0 my-feature-node ip4-unicast enable */</span>
<span class="c-comment">/* Enable via API (from GoVPP or Python) */</span>
<span class="c-comment">/* feature_enable_disable { sw_if_index, arc_name, feature_name, enable=1 } */</span></pre></div>
<p><strong>Key arcs you will use:</strong></p>
<table class="fib-table">
<thead><tr><th>Arc Name</th><th>Terminal Node</th><th>Trigger</th></tr></thead>
<tbody>
<tr><td><code>ip4-unicast</code></td><td>ip4-lookup</td><td>IPv4 unicast inbound per interface</td></tr>
<tr><td><code>ip4-multicast</code></td><td>ip4-mfib-forward-lookup</td><td>IPv4 multicast inbound</td></tr>
<tr><td><code>ip4-output</code></td><td>ip4-rewrite</td><td>IPv4 outbound (post FIB, pre TX)</td></tr>
<tr><td><code>ip6-unicast</code></td><td>ip6-lookup</td><td>IPv6 unicast inbound</td></tr>
<tr><td><code>ethernet-output</code></td><td>interface-output</td><td>L2 output processing</td></tr>
</tbody>
</table>
  </div>
</div>
</div>
<!-- ══ FIB / DPO ══ -->
<div id="t-fib" class="tab-pane">
<p class="section-sep">FORWARDING INFORMATION BASE</p>
<div class="concept-panel panel-orange">
  <div class="concept-panel-hdr"><span class="icon">🗺️</span><h3>FIB Architecture - Prefix → DPO Chain</h3><span class="tag tag-orange">src/vnet/fib/</span></div>
  <div class="concept-panel-body">
<p>VPP's FIB is a <strong>recursive, multi-path forwarding database</strong>. It maps IP prefixes to <strong>Data Path Objects (DPOs)</strong> - a polymorphic chain of forwarding instructions. Understanding FIB is essential for writing plugins that affect routing.</p>
<div class="code-block"><pre><span class="c-comment">/* FIB entry structure (simplified) */</span>
<span class="c-comment">/* Prefix: 10.0.0.0/8 → [ECMP DPO → [adj_A, adj_B]]       */</span>
<span class="c-comment">/* Prefix: 0.0.0.0/0  → [Drop DPO]                        */</span>
<span class="c-comment">/* Prefix: 1.2.3.4/32 → [Receive DPO]  (local address)    */</span>
<span class="c-comment">/* Add a route programmatically from a plugin */</span>
<span class="c-type">fib_prefix_t</span> pfx = {
  .fp_len   = <span class="c-val">24</span>,
  .fp_proto = FIB_PROTOCOL_IP4,
  .fp_addr  = { .ip4 = { .as_u32 = clib_host_to_net_u32(0x0a000100) } },
};
<span class="c-type">fib_route_path_t</span> rpath = {
  .frp_proto     = DPO_PROTO_IP4,
  .frp_addr      = next_hop_addr,
  .frp_sw_if_index = sw_if_index,
  .frp_weight    = <span class="c-val">1</span>,
};
fib_table_entry_path_add(<span class="c-val">0</span>,       <span class="c-comment">/* FIB table 0 = default */</span>
                         &pfx,
                         FIB_SOURCE_PLUGIN_LOW,
                         FIB_ENTRY_FLAG_NONE,
                         &rpath, <span class="c-val">1</span>);
 
<span class="c-comment">/* Lookup in FIB (from a graph node) */</span>
<span class="c-type">fib_node_index_t</span> fei = fib_table_lookup(fib_index, &pfx);
<span class="c-type">load_balance_t</span>  *lb  = load_balance_get(
  fib_entry_get_dpo_index(fei, FIB_FORW_CHAIN_TYPE_UNICAST_IP4));
 
<span class="c-comment">/* The normal path: ip4-lookup does this automatically */</span>
<span class="c-comment">/* You rarely need to call fib_table_lookup directly from a node */</span></pre></div>
  </div>
</div>
<div class="concept-panel panel-green">
  <div class="concept-panel-hdr"><span class="icon">🔗</span><h3>DPO - Data Path Objects</h3><span class="tag tag-green">FORWARDING CHAIN</span></div>
  <div class="concept-panel-body">
<p>A DPO is a polymorphic forwarding object. Every FIB entry resolves to a DPO chain. Key DPO types:</p>
<table class="fib-table">
<thead><tr><th>DPO Type</th><th>Meaning</th><th>Next Node</th></tr></thead>
<tbody>
<tr><td><code>DPO_ADJACENCY</code></td><td>Rewrite header + send to output interface</td><td>ip4-rewrite</td></tr>
<tr><td><code>DPO_ADJACENCY_GLEAN</code></td><td>Trigger ARP for unknown next-hop</td><td>arp-input-glean</td></tr>
<tr><td><code>DPO_RECEIVE</code></td><td>Packet destined for VPP itself</td><td>ip4-local</td></tr>
<tr><td><code>DPO_DROP</code></td><td>Discard packet</td><td>error-drop</td></tr>
<tr><td><code>DPO_LOAD_BALANCE</code></td><td>ECMP - select one of N adjacencies</td><td>selected child DPO</td></tr>
<tr><td><code>DPO_MPLS_LABEL</code></td><td>Push MPLS label and forward</td><td>mpls-output</td></tr>
<tr><td><code>DPO_PUNT</code></td><td>Send to control plane via punt socket</td><td>punt-dispatch</td></tr>
</tbody>
</table>
<p>You can register your own DPO type with <code>dpo_register()</code> to intercept traffic and redirect it through a custom graph node. This is the correct mechanism for tunnel encapsulation, policy routing, and SRv6.</p>
  </div>
</div>
<div class="insight-box">
  <p>💡 <strong>Most plugin authors never touch the FIB directly.</strong> The typical pattern is: register a feature arc node to intercept inbound packets, do your processing, and call <code>vnet_feature_next()</code> to continue normal forwarding. Only plugins that add new route types (tunnels, SRv6, custom DPOs) need to interact with the FIB API.</p>
</div>
</div>
<!-- ══ ARP ══ -->
<div id="t-arp" class="tab-pane">
<p class="section-sep">ARP AND NEIGHBOUR RESOLUTION</p>
<div class="concept-panel panel-purple">
  <div class="concept-panel-hdr"><span class="icon">📡</span><h3>How ARP Works in VPP</h3><span class="tag tag-purple">src/vnet/arp/</span></div>
  <div class="concept-panel-body">
<p>VPP's ARP is entirely in the dataplane. When ip4-lookup resolves a route to a <code>DPO_ADJACENCY_GLEAN</code>, it punts the packet to <code>arp-input-glean</code>, which queues the packet and sends an ARP request. When the ARP reply arrives, <code>arp-reply</code> updates the adjacency table, and queued packets are re-forwarded.</p>
<div class="code-block"><pre><span class="c-comment">/* Manually add a static ARP entry */</span>
vnet_set_ip4_ethernet_arp(<span class="c-key">NULL</span>,           <span class="c-comment">/* main thread */</span>
                          sw_if_index,
                          &ip4_addr,
                          mac_addr,
                          <span class="c-val">1</span>,              <span class="c-comment">/* is_static */</span>
                          <span class="c-val">0</span>);             <span class="c-comment">/* is_no */</span>
<span class="c-comment">/* Show ARP table: vppctl> show ip neighbors */</span>
<span class="c-comment">/* Walk ARP entries programmatically */</span>
ip4_neighbor_walk(sw_if_index, my_cb_fn, my_arg);</pre></div>
<p><strong>Important:</strong> ARP processing is slow-path. Production deployments use static ARP entries for known peers (e.g., testpmd containers) to avoid ARP-generated glean drops at startup. In your mini-projects, add static ARP entries for container-to-container communication.</p>
  </div>
</div>
</div>
<!-- ══ L2 BRIDGING ══ -->
<div id="t-l2" class="tab-pane">
<p class="section-sep">L2 BRIDGING AND SWITCHING</p>
<div class="concept-panel panel-blue">
  <div class="concept-panel-hdr"><span class="icon">🌉</span><h3>Bridge Domains - L2 Forwarding</h3><span class="tag tag-blue">src/vnet/l2/</span></div>
  <div class="concept-panel-body">
<p>VPP supports full L2 bridging. Interfaces placed in the same <strong>bridge domain</strong> behave as ports on the same switch. The bridge domain handles MAC learning, flooding, and forwarding without involving the L3 FIB.</p>
<div class="code-block"><pre><span class="c-comment">/* Create bridge domain 1 and add two interfaces */</span>
<span class="c-comment">/* vppctl> set interface l2 bridge GigabitEthernet0/8/0 1 */</span>
<span class="c-comment">/* vppctl> set interface l2 bridge memif0/0 1             */</span>
<span class="c-comment">/* Programmatic: create bridge domain */</span>
<span class="c-type">l2_bridge_domain_add_del_args_t</span> a = {
  .bd_id     = <span class="c-val">1</span>,
  .flood     = <span class="c-val">1</span>,
  .uu_flood  = <span class="c-val">1</span>,
  .forward   = <span class="c-val">1</span>,
  .learn     = <span class="c-val">1</span>,
  .arp_term  = <span class="c-val">0</span>,
  .mac_age   = <span class="c-val">300</span>,  <span class="c-comment">/* MAC aging: 300 seconds */</span>
  .is_add    = <span class="c-val">1</span>,
};
bd_add_del(&a);
 
<span class="c-comment">/* Add interface to bridge domain */</span>
set_int_l2_mode(vm, vnm, MODE_L2_BRIDGE, sw_if_index, <span class="c-val">1</span>, <span class="c-comment">/* bd_id */</span>
               L2_BD_PORT_TYPE_NORMAL, <span class="c-val">0</span>, <span class="c-val">0</span>);
 
<span class="c-comment">/* Show L2 MAC table */</span>
<span class="c-comment">/* vppctl> show l2fib            */</span>
<span class="c-comment">/* vppctl> show bridge-domain 1  */</span></pre></div>
<p>Bridge domains are heavily used in the mini-projects - the memif vSwitch (Project 5) uses a bridge domain to connect multiple container VPP instances via memif interfaces.</p>
  </div>
</div>
</div>
<!-- ══ CHECKLIST ══ -->
<div id="t-check" class="tab-pane">
<p class="section-sep">P2C COMPLETION CHECKLIST</p>
<ul class="checklist">
  <li>Know the difference between hw_if_index and sw_if_index; know when each is used</li>
  <li>Can retrieve sw_if_index from a buffer, by name, and by walking the interface table</li>
  <li>Understand feature arcs: what they are, how ordering works, and how to register a node in an arc</li>
  <li>Can implement a feature arc node using <code>VNET_FEATURE_INIT</code> and <code>vnet_feature_next()</code></li>
  <li>Understand FIB prefix resolution to DPO chains; know the key DPO types and their next nodes</li>
  <li>Can add and delete FIB routes programmatically using <code>fib_table_entry_path_add</code></li>
  <li>Know how ARP works in VPP and how to add static ARP entries</li>
  <li>Can create a bridge domain and add interfaces to it</li>
  <li>Know the key vnet arcs: ip4-unicast, ip4-output, ip6-unicast, ethernet-output</li>
</ul>
<div class="insight-box" style="margin-top:1.2rem">
  <p>✅ Phase 2 complete. You now understand all three vpp layers from the ground up. Next: <strong>Phase 3 - Interface Technologies</strong>. Start with the DPDK plugin - it's the most familiar given your background.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/data-plane/vpp/module-p2-vlib/">← P2B: vlib</a>
  <a href="/learning/data-plane/vpp/vpp-roadmap/">🗺️ Roadmap</a>
  <a class="next-btn" href="/learning/data-plane/vpp/module-p3-dpdk/">Next: DPDK Plugin →</a>
</div>
<script>
function switchTab(e,id){
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
</script>
