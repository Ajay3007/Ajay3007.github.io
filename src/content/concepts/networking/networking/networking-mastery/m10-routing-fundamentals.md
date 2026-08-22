---
title: "M10 - Routing Fundamentals and FIB"
description: "NETWORKING MASTERY · PHASE 3 · MODULE 10 · WEEK 8 🗺️ Routing Fundamentals and FIB FIB/RIB architecture · Longest Prefix Match · LPM algorithms · ECMP · Policy routing ·…"
domain: networking
track: networking-mastery
order: 10
ownHeader: true
url: /learning/networking-mastery/m10-routing-fundamentals/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 35%,#1a5a3c 70%,#0a3a28 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#80d8a0;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#b0e8c0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#c8f8d8}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#80d8a0;border-bottom-color:#80d8a0}
.tab-pane{display:none}
.tab-pane.active{display:block}
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
.tag-blue{background:#d0e8f8;color:#1a4a7c}
.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}
.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}
.tag-red{background:#f4d0d0;color:#6c1a1a}
.tag-amber{background:#fae8a0;color:#5a3800}
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1a5a3c}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#b0e8c0;white-space:pre}
.cm{color:#4a7a50}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#e8f8ee;border:1.5px solid #1a5a3c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0a2018;border-color:#2a8a50}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#1a4a28}
[data-theme=dark] .ins strong{color:#80d8a0}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.note{background:#e8f1f9;border:1.5px solid #1a3a5c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .note{background:#0d2030;border-color:#2a5a8c}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.analogy{background:linear-gradient(135deg,#f0fff4,#e8f8ee);border:1.5px solid #80c890;border-radius:10px;padding:1.1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .analogy{background:linear-gradient(135deg,#0a1a0e,#0a2014);border-color:#306840}
.analogy-title{font-size:.72rem;font-family:monospace;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#1a4a28;margin-bottom:.5rem}
[data-theme=dark] .analogy-title{color:#80d8a0}
.analogy p{font-size:.88rem;line-height:1.7;color:var(--text-color,#222);margin:0}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#1a4a28;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a5a3c}
/* Trie visual */
.trie-node{display:inline-flex;flex-direction:column;align-items:center;gap:4px;margin:0 8px}
.trie-bit{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.78rem;font-weight:700;border:2px solid}
.trie-children{display:flex;gap:0;position:relative}
.trie-children::before{content:'';position:absolute;top:-12px;left:50%;right:50%;border-top:2px solid var(--border-color,#ccc)}
.flow-list{display:flex;flex-direction:column;gap:0;margin:1rem 0}
.fl-step{display:flex;gap:14px;padding:10px 14px;border-left:2px solid var(--border-color,#e0e0e0);margin-left:14px;position:relative}
.fl-step::before{content:attr(data-n);position:absolute;left:-14px;top:12px;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;color:#fff;background:var(--sc,#1a4a28)}
.fl-step:last-child{border-left-color:transparent}
.fl-title{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin-bottom:.25rem}
.fl-detail{font-size:.85rem;color:var(--text-color,#444);line-height:1.6}
.fl-code{font-family:monospace;font-size:.78rem;display:inline-block;background:#0a1628;color:#80d8a0;padding:2px 8px;border-radius:4px;margin-top:.3rem}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #1a5a3c;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#1a5a3c;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#1a5a3c;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#1a5a3c;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 3 · MODULE 10 · WEEK 8</div>
  <div class="mod-title">🗺️ Routing Fundamentals and FIB</div>
  <div class="mod-subtitle">FIB/RIB architecture · Longest Prefix Match · LPM algorithms · ECMP · Policy routing · Administrative distance</div>
  <div class="mod-pills">
<span class="mod-pill">Intermediate</span>
<span class="mod-pill">Prerequisite: M03 IPv4</span>
<span class="mod-pill">RFC 1812</span>
<span class="mod-pill">Core Data-Plane Operation</span>
<span class="mod-pill">3 Labs</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">Routing Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">RIB and FIB</button>
  <button class="tab-btn" onclick="vt(event,'t2')">LPM Algorithm</button>
  <button class="tab-btn" onclick="vt(event,'t3')">ECMP</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Administrative Distance</button>
  <button class="tab-btn" onclick="vt(event,'t5')">Policy Routing</button>
  <button class="tab-btn" onclick="vt(event,'t6')">Linux Routing</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Checklist</button>
</div>
<!-- ════ TAB 0 — ROUTING OVERVIEW ════ -->
<div id="t0" class="tab-pane active">
<p class="sep">HOW ROUTERS DECIDE WHERE PACKETS GO</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🗺️</span><h3>The Routing Problem</h3><span class="tag tag-green">OVERVIEW</span></div>
  <div class="cp-body">
<p>Routing is the process of selecting a path for network traffic. When a packet arrives at a router, the router must answer one question in microseconds: <strong>which interface should I send this packet out of?</strong> The answer depends on the packet's destination IP address and the router's routing table.</p>
<p>Three types of routes populate a routing table:</p>
<ul>
<li><strong>Connected routes</strong> — automatically created when an interface is brought up and assigned an IP. The router knows it can reach that subnet directly. These have the highest trustworthiness.</li>
<li><strong>Static routes</strong> — manually configured by an administrator. Simple, predictable, but don't adapt to topology changes.</li>
<li><strong>Dynamic routes</strong> — learned from other routers via routing protocols (OSPF, BGP, RIP). Adapt automatically when links fail or topology changes.</li>
</ul>
  </div>
</div>
<div class="analogy">
  <div class="analogy-title">🚦 Analogy — GPS Navigation System</div>
  <p>A router's routing table is like a GPS navigation system's map. When you enter a destination, the GPS looks at all known roads, finds the best route, and gives you turn-by-turn directions. A routing table contains all known network destinations (like roads on a map) with their next hops (like turns). The GPS's "fastest route" is like a router's "lowest metric". Just as GPS updates its map when roads are closed, dynamic routing protocols update the routing table when links fail. And just as GPS uses the most specific address you enter — a full street address wins over just a city name — routers use the most specific prefix that matches.</p>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📊</span><h3>The Five-Step Packet Forwarding Process</h3><span class="tag tag-blue">FORWARDING</span></div>
  <div class="cp-body">


```bash
/* When a router receives a packet */

Step 1: Receive packet on ingress interface
  - NIC copies frame from wire to memory
  - Strip Ethernet header, verify CRC

Step 2: Verify IP header
  - Check IP version (4 or 6)
  - Validate IP header checksum (drop if corrupt)
  - Check TTL: if TTL == 0 → discard + send ICMP Time Exceeded
  - Decrement TTL

Step 3: FIB lookup (Longest Prefix Match)
  - Look up destination IP in Forwarding Information Base
  - Find most specific matching prefix
  - Get: egress interface + next-hop IP

Step 4: Resolve next-hop MAC (ARP / Neighbour Cache)
  - Look up next-hop IP in ARP cache
  - If miss: send ARP request, queue packet

Step 5: Rewrite L2 header + transmit
  - New Ethernet header: dst=next-hop MAC, src=egress port MAC
  - Recompute IP checksum (TTL changed)
  - Transmit on egress interface

/* What the router does NOT change */
# Source IP, Destination IP — unchanged (except NAT)
# Payload (TCP/UDP/application data) — unchanged
# Only TTL (decremented) and checksum (recomputed) change in IP header
```


  </div>
</div>
</div>
<!-- ════ TAB 1 — RIB AND FIB ════ -->
<div id="t1" class="tab-pane">
<p class="sep">RIB AND FIB — THE TWO ROUTING DATABASES</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📚</span><h3>RIB vs FIB — Different Purposes, Different Structures</h3><span class="tag tag-blue">ARCHITECTURE</span></div>
  <div class="cp-body">
<p>Modern routing systems maintain two separate databases for routes. Understanding the distinction is critical for data-plane engineering:</p>
<div class="two-col">
<div>
<h4>RIB — Routing Information Base</h4>
<p>The <em>control plane</em> database. Contains <strong>all routes learned</strong> from all sources — connected, static, OSPF, BGP, RIP, etc. — including multiple competing routes to the same destination from different protocols or next-hops. The RIB is the "complete knowledge" database. It is managed by the routing daemon (Quagga, FRR, VPP's routing engine).</p>
<p>The RIB is <strong>not used for packet forwarding</strong> — it's too large and complex for per-packet lookups at line rate.</p>
</div>
<div>
<h4>FIB — Forwarding Information Base</h4>
<p>The <em>data plane</em> database. Contains only the <strong>best route per destination prefix</strong> — selected from the RIB by the routing daemon after applying administrative distance and metric comparisons. The FIB is what the forwarding engine (ASIC, NP, or CPU) uses for every packet lookup.</p>
<p>The FIB is optimised for <strong>speed</strong>: it may be stored in TCAM (hardware), a radix trie, or a hash table. In VPP, the FIB is a multi-level lookup structure in hugepage memory. In Linux, it's the kernel routing table.</p>
</div>
</div>



```python
/* RIB → FIB population process */

RIB contains (for destination 10.0.0.0/8):
  OSPF:   10.0.0.0/8 via 192.168.1.2  metric=20  AD=110
  Static: 10.0.0.0/8 via 192.168.1.3  metric=0   AD=1
  BGP:    10.0.0.0/8 via 10.255.0.1   metric=100  AD=200

Route selection:
  1. Prefer lower Administrative Distance: Static AD=1 wins over OSPF(110) and BGP(200)
  2. Among equal AD routes: prefer lower metric
  Best route: Static 10.0.0.0/8 via 192.168.1.3

FIB entry: 10.0.0.0/8 → egress=eth1 nexthop=192.168.1.3 mac=aa:bb:cc:dd:ee:ff

/* Linux commands */
ip route show table main        # FIB (main routing table)
ip route show table all         # all routing tables
ip route get 8.8.8.8            # which route would be used for 8.8.8.8?

/* VPP FIB inspection */
# vppctl: show ip fib
# vppctl: show ip fib 10.0.0.0/8
# vppctl: show ip fib summary
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🏎️</span><h3>Hardware FIB — TCAM</h3><span class="tag tag-teal">HARDWARE</span></div>
  <div class="cp-body">
<p>High-end routers and switches implement the FIB in <strong>TCAM (Ternary Content-Addressable Memory)</strong> — a specialised memory that can match a search key against all stored entries simultaneously in O(1) time, regardless of table size.</p>
<p>TCAM stores entries with three states per bit: 0, 1, or X (don't care). For IP routing: the network bits are stored as 0/1, and the host bits as X. A lookup of any destination IP matches the most specific entry in a single clock cycle at line rate — 100 Gbps, no software involved.</p>


```bash
/* TCAM entry for 192.168.1.0/24 */
Value: 11000000.10101000.00000001.00000000
Mask:  11111111.11111111.11111111.00000000  (X = don't care on unmasked bits)

/* A lookup of 192.168.1.55: */
Match: 11000000.10101000.00000001.00110111
AND mask: first 24 bits match → HIT

/* TCAM limitations */
# Expensive per-bit (vs SRAM)
# High power consumption
# Limited capacity (typically 256K–2M entries in enterprise routers)
# Internet full routing table ~950K prefixes — approaches TCAM limits
# BGP router TCAM exhaustion is a real operational concern
```


  </div>
</div>
</div>
<!-- ════ TAB 2 — LPM ALGORITHM ════ -->
<div id="t2" class="tab-pane">
<p class="sep">LONGEST PREFIX MATCH — THE CORE ROUTING ALGORITHM</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>What is Longest Prefix Match?</h3><span class="tag tag-green">CONCEPT</span></div>
  <div class="cp-body">
<p>Longest Prefix Match (LPM) is the rule for selecting which route to use when multiple routes match a destination address. The route with the <strong>most specific prefix</strong> (longest subnet mask / highest prefix length) wins.</p>
<div class="cb"><pre><span class="cm">/* Routing table example */</span>
10.0.0.0/8       via 192.168.1.1   <span class="cm"># matches any 10.x.x.x</span>
10.10.0.0/16     via 192.168.1.2   <span class="cm"># matches any 10.10.x.x</span>
10.10.1.0/24     via 192.168.1.3   <span class="cm"># matches any 10.10.1.x</span>
10.10.1.5/32     via 192.168.1.4   <span class="cm"># matches ONLY 10.10.1.5</span>
0.0.0.0/0        via 192.168.1.254 <span class="cm"># default — matches anything</span>
<span class="cm">/* LPM for destination 10.10.1.5 */</span>
0.0.0.0/0     matches  → /0  prefix length
10.0.0.0/8    matches  → /8  prefix length
10.10.0.0/16  matches  → /16 prefix length
10.10.1.0/24  matches  → /24 prefix length
10.10.1.5/32  matches  → /32 prefix length  ← LONGEST MATCH → use this route
 
<span class="cm">/* LPM for destination 10.10.2.50 */</span>
0.0.0.0/0     matches  → /0
10.0.0.0/8    matches  → /8
10.10.0.0/16  matches  → /16  ← LONGEST MATCH → use this route
10.10.1.0/24  no match (wrong third octet)
10.10.1.5/32  no match
 
<span class="cm">/* LPM for destination 8.8.8.8 */</span>
0.0.0.0/0     matches  → /0   ← LONGEST (only) MATCH → default route</pre></div>
<div class="ins"><p>💡 <strong>The /32 host route is the most specific possible</strong> — it matches exactly one IP address. Used for: BGP next-hop routes, traffic engineering, sinkholing specific IPs, loopback interfaces. In VPP/DPDK data planes you will frequently add /32 routes for specific flows.</p></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🌳</span><h3>LPM Data Structures — Radix Trie</h3><span class="tag tag-blue">ALGORITHM</span></div>
  <div class="cp-body">
<p>Software LPM (used in Linux kernel, VPP for IPv6, and when TCAM isn't available) is typically implemented with a <strong>radix trie</strong> (Patricia trie). Each bit of the IP address is a branch point. The lookup traverses the trie bit by bit from MSB to LSB, recording the last matching node that has a route entry. After all bits are processed, the last recorded entry is the LPM result.</p>


```c
/* Binary trie LPM lookup for 10.10.1.5 */
/* 10.10.1.5 = 00001010.00001010.00000001.00000101 */

Bit 1 (MSB): 0 → go left
Bit 2:       0 → go left
Bit 3:       0 → go left
Bit 4:       0 → go left
Bit 5:       1 → go right  ← first '1' bit
  Found entry: 10.0.0.0/8 (prefix ends at bit 8) → record as current best
...continue to bit 8, record 10.0.0.0/8...
...continue to bit 16, record 10.10.0.0/16...
...continue to bit 24, record 10.10.1.0/24...
...continue to bit 32, record 10.10.1.5/32...
End of bits → return 10.10.1.5/32 (last recorded = longest match)

/* Implementing LPM in C — simple version */
typedef struct trie_node {
    struct trie_node *child[2]; /* 0=left, 1=right */
    uint32_t nexthop;           /* 0 = no route at this node */
    uint8_t  prefix_len;
} trie_node_t;

uint32_t lpm_lookup(trie_node_t *root, uint32_t dst_ip) {
    trie_node_t *node = root;
    uint32_t best_nexthop = 0;
    for (int bit = 31; bit >= 0 && node; bit--) {
        if (node->nexthop) best_nexthop = node->nexthop;
        int b = (dst_ip >> bit) & 1;
        node = node->child[b];
    }
    if (node && node->nexthop) best_nexthop = node->nexthop;
    return best_nexthop; /* 0 = no route (drop) */
}
```



<h4>LPM at Scale — DIR-24-8 and LC-Trie</h4>
<p>For IPv4 in software at high speed, routers often use <strong>DIR-24-8</strong> (Direct Index Route lookup): a two-level table where the first 24 bits index a 16M-entry array (with one 32-bit entry per /24 prefix), and the last 8 bits are resolved with a secondary table for prefixes longer than /24. This achieves O(1) or O(2) lookup with excellent cache performance.</p>
  </div>
</div>
</div>
<!-- ════ TAB 3 — ECMP ════ -->
<div id="t3" class="tab-pane">
<p class="sep">ECMP — EQUAL-COST MULTI-PATH ROUTING</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">⚖️</span><h3>What ECMP Is and Why It Exists</h3><span class="tag tag-teal">CONCEPT</span></div>
  <div class="cp-body">
<p>ECMP (Equal-Cost Multi-Path) allows a router to use <strong>multiple next-hops simultaneously</strong> for a destination when multiple paths have the same metric. This provides both load balancing (traffic distributed across multiple links) and redundancy (if one path fails, others continue).</p>


```python
/* ECMP in Linux routing table */
$ ip route show
10.0.0.0/8
    nexthop via 192.168.1.1 dev eth0 weight 1
    nexthop via 192.168.1.2 dev eth1 weight 1
    nexthop via 192.168.1.3 dev eth2 weight 1
# Three equal-cost paths — traffic balanced across all three

/* ECMP hashing — how traffic is distributed */
# Each packet is assigned to a path using a hash of its flow identifier
# This ensures packets of the SAME FLOW go to the SAME next-hop
# (required for stateful protocols — TCP reordering causes retransmits)

/* Hash inputs (per-flow consistent hashing) */
5-tuple hash (most common):
  hash(src_ip, dst_ip, src_port, dst_port, protocol) % num_paths

/* For IPv6: also include Flow Label (20-bit) */
hash(src_ip6, dst_ip6, flow_label) % num_paths

/* Weighted ECMP (unequal links) */
10.0.0.0/8
    nexthop via 192.168.1.1 weight 3   # 3/4 of traffic
    nexthop via 192.168.1.2 weight 1   # 1/4 of traffic
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>ECMP Challenges — The Polarisation Problem</h3><span class="tag tag-blue">CHALLENGES</span></div>
  <div class="cp-body">
<p>ECMP has two well-known operational problems:</p>
<ul>
<li><strong>Hash polarisation</strong> — if every router in a topology uses the same hash function and inputs, all traffic may land on the same path through the network. The fix: vary hash seeds per router, or include router-specific fields (e.g., ingress interface) in the hash.</li>
<li><strong>Large flows dominate</strong> — ECMP distributes by flow, not by byte count. A single TCP elephant flow (file download) sending 10 Gbps gets one path. 1000 small flows might be evenly distributed across 3 paths but the elephant's path carries 10× more traffic. Fix: flow-aware traffic engineering (MPLS TE, Segment Routing).</li>
</ul>
<h4>ECMP and Stateful Firewalls</h4>
<p>ECMP creates a critical challenge for stateful firewalls and NGFW clusters: if outbound and inbound packets of the same TCP session take different paths and hit different firewall nodes, the firewall node handling the return traffic has no state for the connection and drops it (asymmetric routing). Solutions: session synchronisation between firewall nodes, consistent hashing to ensure symmetric path, or stateless inspection modes.</p>


```bash
/* ECMP configuration in Linux */
# Add ECMP route
ip route add 10.0.0.0/8 \
    nexthop via 192.168.1.1 dev eth0 weight 1 \
    nexthop via 192.168.1.2 dev eth1 weight 1

# Control ECMP hash inputs
sysctl net.ipv4.fib_multipath_hash_policy
# 0 = L3 (src+dst IP only)
# 1 = L3+L4 (5-tuple) — recommended for better distribution
# 2 = L3+L4 including inner headers for encapsulated packets

# VPP ECMP (load-balance object)
# vppctl: ip route add 10.0.0.0/8 via 192.168.1.1 GigE0/0
# vppctl: ip route add 10.0.0.0/8 via 192.168.1.2 GigE0/1
# VPP creates a load-balance object with flow-hash buckets
```


  </div>
</div>
</div>
<!-- ════ TAB 4 — ADMINISTRATIVE DISTANCE ════ -->
<div id="t4" class="tab-pane">
<p class="sep">ADMINISTRATIVE DISTANCE — ROUTE TRUSTWORTHINESS</p>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">🏆</span><h3>Administrative Distance — Route Source Preference</h3><span class="tag tag-amber">AD</span></div>
  <div class="cp-body">
<p>When multiple routing protocols learn routes to the same destination, the router must choose which one to install in the FIB. Administrative Distance (AD) is the preference value assigned to each routing source — lower AD = more trusted = preferred. AD is a Cisco term; other vendors use similar concepts (route preference, distance).</p>
<table class="t-table">
<thead><tr><th>Route Source</th><th>AD (Cisco)</th><th>AD (Linux metric)</th><th>Why This Priority</th></tr></thead>
<tbody>
<tr><td>Connected interface</td><td>0</td><td>0</td><td>Router is directly attached — 100% reliable</td></tr>
<tr><td>Static route</td><td>1</td><td>—</td><td>Manually configured — administrator knows best</td></tr>
<tr><td>EIGRP (internal)</td><td>90</td><td>—</td><td>Cisco proprietary — high trust</td></tr>
<tr><td>OSPF</td><td>110</td><td>—</td><td>Standard IGP — trusted but below static</td></tr>
<tr><td>IS-IS</td><td>115</td><td>—</td><td>Standard IGP — similar to OSPF</td></tr>
<tr><td>RIP</td><td>120</td><td>—</td><td>Old distance-vector — lower trust</td></tr>
<tr><td>EIGRP (external)</td><td>170</td><td>—</td><td>Redistributed from another protocol — less trusted</td></tr>
<tr><td>BGP (eBGP)</td><td>20</td><td>—</td><td>External BGP — specific route from peer, high trust</td></tr>
<tr><td>BGP (iBGP)</td><td>200</td><td>—</td><td>Internal BGP — redistributed, lowest trust by default</td></tr>
<tr><td>Unreachable (blackhole)</td><td>255</td><td>—</td><td>Used to mark routes as unusable</td></tr>
</tbody>
</table>



```bash
/* AD in practice — floating static route */
# Primary path: OSPF learns 10.0.0.0/8 via fiber link (AD=110)
# Backup: static route via 4G modem (should only be used if OSPF fails)

ip route add 10.0.0.0/8 via 192.168.100.1 metric 200
# In Linux: metric 200 = lower priority than OSPF routes
# While OSPF is active: OSPF route wins (metric 110)
# When OSPF fails: OSPF route removed → static route with metric 200 activates
# This is a "floating static route" — floats below dynamic routes

/* Viewing route sources in Linux */
ip route show proto ospf    # routes from OSPF
ip route show proto bgp     # routes from BGP
ip route show proto static  # static routes
ip route show proto kernel  # connected (kernel-generated)
```


  </div>
</div>
</div>
<!-- ════ TAB 5 — POLICY ROUTING ════ -->
<div id="t5" class="tab-pane">
<p class="sep">POLICY-BASED ROUTING — BEYOND DESTINATION-ONLY FORWARDING</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📋</span><h3>What Policy Routing Adds</h3><span class="tag tag-purple">PBR</span></div>
  <div class="cp-body">
<p>Standard routing forwards packets based only on <strong>destination IP address</strong>. Policy-Based Routing (PBR) allows routing decisions based on additional criteria: source IP, DSCP/TOS, protocol, port, or even incoming interface. This is essential for NGFW deployments where different traffic classes must take different paths.</p>


```sql
/* Linux Policy Routing (ip rule + multiple routing tables) */

# Scenario: ISP-A (eth0) for normal traffic, ISP-B (eth1) for VoIP

# Step 1: Create separate routing tables
# /etc/iproute2/rt_tables: add "200 isp_b"
echo "200 isp_b" >> /etc/iproute2/rt_tables

# Step 2: Populate table for ISP-B
ip route add default via 10.2.0.1 dev eth1 table isp_b
ip route add 10.2.0.0/24 dev eth1 table isp_b  # local subnet

# Step 3: Create rules to select table based on criteria
ip rule add from 192.168.1.0/24 dport 5060 table isp_b  # SIP → ISP-B
ip rule add dscp 46 table isp_b                           # EF (VoIP) → ISP-B
ip rule add from 10.0.0.5 table isp_b                    # specific host → ISP-B
# Default rule: use main table (ISP-A)

# View rules (evaluated in priority order, lower = first)
ip rule show
# 0:      from all lookup local
# 100:    from 10.0.0.5 lookup isp_b
# 200:    dscp 46 lookup isp_b
# 32766:  from all lookup main
# 32767:  from all lookup default
```



<div class="ins"><p>💡 <strong>NGFW use cases for PBR:</strong> Route management traffic out a dedicated OOB (out-of-band) interface. Send IDS/IPS traffic to an inline inspection appliance. Route different VLANs to different next-hops. Forward specific threat-tagged traffic to a honeypot or sandbox. Force all DNS to the internal resolver regardless of destination port.</p></div>
  </div>
</div>
</div>
<!-- ════ TAB 6 — LINUX ROUTING ════ -->
<div id="t6" class="tab-pane">
<p class="sep">LINUX ROUTING INTERNALS AND COMMANDS</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🐧</span><h3>Linux Kernel Routing Architecture</h3><span class="tag tag-teal">LINUX</span></div>
  <div class="cp-body">


```bash
/* Linux routing table management commands */

# View main routing table (FIB)
ip route show
ip route show table main
route -n   # older tool (still useful)

# View a specific route and which would be used
ip route get 8.8.8.8
# 8.8.8.8 via 192.168.1.1 dev eth0 src 192.168.1.5 uid 1000
#    cache

# Add static routes
ip route add 10.0.0.0/8 via 192.168.1.1              # via next-hop
ip route add 10.0.0.0/8 dev eth0                     # directly connected
ip route add 10.0.0.0/8 via 192.168.1.1 metric 100  # with metric
ip route add blackhole 203.0.113.0/24                # null route (drop)
ip route add prohibit 192.0.2.0/24                   # drop + ICMP prohibit
ip route add unreachable 198.51.100.0/24             # drop + ICMP unreachable

# Delete routes
ip route del 10.0.0.0/8 via 192.168.1.1

# Default route
ip route add default via 192.168.1.1
ip route add 0.0.0.0/0 via 192.168.1.1  # same thing

# Make Linux forward packets (act as router)
sysctl net.ipv4.ip_forward=1
echo 1 > /proc/sys/net/ipv4/ip_forward
# Permanent: add to /etc/sysctl.conf

# Route cache (Linux 3.6+ uses FIB directly — no separate route cache)
# Previous versions had a route cache (dst_entry) that caused hash table attacks

# IPv6 routing
ip -6 route show
ip -6 route add 2001:db8::/32 via fe80::1 dev eth0
ip -6 route get 2001:4860:4860::8888
```


  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>Routing in VPP — The Data-Plane Perspective</h3><span class="tag tag-green">VPP</span></div>
  <div class="cp-body">


```bash
/* VPP FIB architecture */
# VPP uses a multi-level FIB structure in hugepage memory
# IP4 FIB: hash table + mtrie (multi-way trie) for IPv4
# IP6 FIB: hash table for /128s, mtrie for others

# VPP routing commands (vppctl)
show ip fib                          # entire IPv4 FIB
show ip fib 10.0.0.0/8              # specific prefix
show ip fib summary                  # prefix count by length

ip route add 10.0.0.0/8 via 192.168.1.1 GigabitEthernet0/8/0
ip route add 0.0.0.0/0  via 192.168.1.254 GigabitEthernet0/8/0

# ECMP in VPP
ip route add 10.0.0.0/8 via 192.168.1.1 GigabitEthernet0/8/0
ip route add 10.0.0.0/8 via 192.168.1.2 GigabitEthernet0/8/1
# VPP automatically creates a load-balance adjacency with flow-hash buckets
show ip fib 10.0.0.0/8    # shows load-balance object with N buckets

# VPP FIB lookup in C (graph node)
/* In ip4_lookup.c: */
ip4_fib_mtrie_lookup_step (mtrie, &leaf, &a->dst_address, 0);
ip4_fib_mtrie_lookup_step (mtrie, &leaf, &a->dst_address, 1);
ip4_fib_mtrie_lookup_step (mtrie, &leaf, &a->dst_address, 2);
ip4_fib_mtrie_lookup_step (mtrie, &leaf, &a->dst_address, 3);
/* 4 pipeline stages for 32-bit IPv4 address lookup */
```


  </div>
</div>
</div>
<!-- ════ TAB 7 — LABS ════ -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>LPM Trie Implementation in C</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Implement a binary trie for LPM routing lookups. Insert routes and verify the correct next-hop is returned for various destination IPs.</p>
<div class="lab-step"><div class="sn">1</div><div>Implement the <code>trie_node_t</code> struct and <code>trie_insert(root, prefix, prefix_len, nexthop)</code> function. For each prefix, set bits 0–prefix_len of the address path in the trie and store the nexthop at the terminal node.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Implement <code>lpm_lookup(root, dst_ip)</code> — traverse the trie bit by bit from MSB to LSB, recording the most recently seen nexthop. Return the last recorded nexthop (or 0 for no route).</div></div>
<div class="lab-step"><div class="sn">3</div><div>Insert: 0.0.0.0/0 → 1, 10.0.0.0/8 → 2, 10.10.0.0/16 → 3, 10.10.1.0/24 → 4, 10.10.1.5/32 → 5. Verify: lookup(10.10.1.5)=5, lookup(10.10.1.6)=4, lookup(10.10.2.1)=3, lookup(10.20.0.1)=2, lookup(8.8.8.8)=1.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Benchmark: insert 100,000 random /24 prefixes and measure lookups/second. Compare with a linear scan of the same routes. The trie should be 100–1000× faster on large tables.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Build a Multi-Path Router with ECMP</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Configure a Linux VM as a router with ECMP, observe traffic distribution, and test failover when one path goes down.</p>
<div class="lab-step"><div class="sn">1</div><div>Enable IP forwarding: <code>sudo sysctl net.ipv4.ip_forward=1</code>. Add an ECMP route with two nexthops: <code>sudo ip route add 10.0.0.0/8 nexthop via 192.168.1.1 dev eth0 weight 1 nexthop via 192.168.1.2 dev eth1 weight 1</code>.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Verify traffic distribution: use <code>ip route get</code> with different destination IPs to see which nexthop is selected. The hash of the destination IP determines the path: <code>for i in $(seq 1 20); do ip route get 10.0.$i.1 | grep via; done</code>. Count how many go to each nexthop — should be roughly 50/50.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Enable L4 hashing: <code>sudo sysctl net.ipv4.fib_multipath_hash_policy=1</code>. Repeat. The distribution should change because port numbers now affect the hash.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Test failover: bring down eth1 (<code>sudo ip link set eth1 down</code>). Verify the ECMP route has only one nexthop remaining: <code>ip route show</code>. Bring it back up and re-add the nexthop.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Policy Routing — Multiple Uplinks</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Configure Linux Policy Routing to route different traffic classes to different uplinks.</p>
<div class="lab-step"><div class="sn">1</div><div>Add routing tables: <code>echo "100 isp1" >> /etc/iproute2/rt_tables; echo "200 isp2" >> /etc/iproute2/rt_tables</code>. Populate each: <code>ip route add default via 10.1.0.1 table isp1; ip route add default via 10.2.0.1 table isp2</code>.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Add rules: SSH traffic (port 22) to ISP1 (management), web traffic to ISP2: <code>ip rule add dport 22 table isp1 priority 100; ip rule add dport 80 table isp2 priority 101; ip rule add dport 443 table isp2 priority 102</code>. View with <code>ip rule show</code>.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Test: <code>ip route get 8.8.8.8 dport 22</code> vs <code>ip route get 8.8.8.8 dport 80</code>. Verify different nexthops are selected. Use <code>traceroute</code> on each to confirm different first hops.</div></div>
  </div>
</div>
</div>
<!-- ════ TAB 8 — CHECKLIST ════ -->
<div id="t8" class="tab-pane">
<p class="sep">M10 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know the 5-step forwarding process: receive → validate IP (TTL, checksum) → FIB lookup (LPM) → ARP resolve → rewrite L2 + transmit</li>
  <li>Know what the router changes: decrements TTL, recomputes IP checksum, rewrites Ethernet src/dst MAC</li>
  <li>Know what the router does NOT change: src IP, dst IP, payload</li>
  <li>Know the difference between RIB (control plane, all routes) and FIB (data plane, best routes for forwarding)</li>
  <li>Know how TCAM works: ternary (0/1/X) match, all entries searched simultaneously, O(1) lookup</li>
  <li>Know TCAM limitations: expensive, power-hungry, limited capacity (~1M entries), BGP full table exhaustion risk</li>
  <li>Know LPM rule: among all matching prefixes, the one with the longest (most specific) prefix length wins</li>
  <li>Can manually perform LPM given a routing table and destination IP</li>
  <li>Know the radix trie LPM algorithm: traverse bit by bit MSB to LSB, record last matching node</li>
  <li>Know DIR-24-8: two-level array for IPv4 LPM at near-O(1) with good cache behaviour</li>
  <li>Know ECMP: multiple equal-cost next-hops, flow-based consistent hashing for per-flow path selection</li>
  <li>Know ECMP hash inputs: 5-tuple (src_ip, dst_ip, src_port, dst_port, proto) ensures same flow → same path</li>
  <li>Know ECMP challenges: hash polarisation, elephant flows, asymmetric routing breaking stateful firewalls</li>
  <li>Know Administrative Distance: lower AD = more trusted = installed in FIB. Key values: connected=0, static=1, OSPF=110, iBGP=200</li>
  <li>Know floating static route: static with high metric used as backup when dynamic route disappears</li>
  <li>Know Policy-Based Routing: route decisions based on src IP, DSCP, protocol, port — not just dst IP</li>
  <li>Know Linux PBR: ip rule + multiple routing tables; rules evaluated in priority order</li>
  <li>Know key Linux routing commands: ip route show/add/del/get, ip rule show/add, sysctl net.ipv4.ip_forward</li>
  <li>Know null/blackhole routes: drop packets matching prefix (used for traffic engineering and anti-DDoS)</li>
  <li>Completed Lab 1: implemented binary trie LPM in C, verified correct nexthop for all test cases</li>
  <li>Completed Lab 2: configured ECMP with two nexthops, verified hash distribution, tested failover</li>
  <li>Completed Lab 3: configured policy routing with two uplinks, verified different traffic classes use different paths</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M11 - OSPF Internals</strong>. You now understand how routers forward packets — M11 covers how they <em>learn</em> routes dynamically via OSPF's link-state flooding and Dijkstra's SPF algorithm.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/networking-mastery/m09-app-protocols/">← M09 SMTP/FTP/DHCP</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m11-ospf/">Next: M11 - OSPF →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
