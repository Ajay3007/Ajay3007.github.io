---
title: "M13 - MPLS, VxLAN, GRE and Tunneling"
description: "NETWORKING MASTERY · PHASE 3 · MODULE 13 · WEEK 11 · PHASE 3 FINAL 🔗 MPLS, VxLAN, GRE and Tunneling Label switching · Overlay networks · VxLAN VTEP · GRE encapsulation · IPsec…"
domain: networking
track: networking-mastery
order: 13
ownHeader: true
url: /learning/networking-mastery/m13-tunneling/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 35%,#0f6e56 65%,#0a4a38 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#7ab8d8;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#a8d8f0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#c8ecff}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#5dd6c8;border-bottom-color:#5dd6c8}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #0f6e56}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#a8e8d8;white-space:pre}
.cm{color:#4a8a70}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#e8f5f0;border:1.5px solid #0f6e56;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0a2420;border-color:#2a9a8e}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#0e5248}
[data-theme=dark] .ins strong{color:#5dd6c8}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.note{background:#e8f1f9;border:1.5px solid #1a3a5c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .note{background:#0d2030;border-color:#2a5a8c}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#0f6e56;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#0f6e56}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #0f6e56;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#0f6e56;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#0f6e56;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#0f6e56;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
/* Encap visual */
.encap-row{display:flex;gap:2px;min-width:500px;margin-bottom:4px;align-items:stretch;overflow-x:auto}
.encap-label{font-size:.7rem;font-family:monospace;min-width:80px;display:flex;align-items:center;color:var(--light-text,#666);flex-shrink:0}
.ef{border-radius:5px;padding:7px 6px;font-size:.7rem;font-weight:600;text-align:center;border:1.5px solid transparent;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1.3}
.ef-outer{background:#fdf4dc;border-color:#e8c870;color:#5a3800}
.ef-mpls {background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c}
.ef-inner{background:#e8f5e8;border-color:#90d890;color:#1a5a1a}
.ef-orig {background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c}
.ef-new  {outline:2px solid #0f6e56;outline-offset:1px}
/* Phase complete */
.phase-complete{background:linear-gradient(135deg,#0a2018,#1e6b3c);border-radius:10px;padding:1.4rem 1.6rem;margin:2rem 0;border:1.5px solid #2a9a5c;color:#fff}
.phase-complete h3{margin:0 0 .5rem;font-size:1.1rem;font-weight:800;color:#fff;border:none}
.phase-complete p{margin:0;font-size:.88rem;line-height:1.65;color:#c0f0c0}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 3 · MODULE 13 · WEEK 11 · PHASE 3 FINAL</div>
  <div class="mod-title">🔗 MPLS, VxLAN, GRE and Tunneling</div>
  <div class="mod-subtitle">Label switching · Overlay networks · VxLAN VTEP · GRE encapsulation · IPsec tunnels · Tunnel comparison</div>
  <div class="mod-pills">
    <span class="mod-pill">Intermediate → Advanced</span>
    <span class="mod-pill">Prerequisite: M10, M12</span>
    <span class="mod-pill">RFC 3032 · RFC 7348 · RFC 2784</span>
    <span class="mod-pill">Data Centre and VPN Core</span>
    <span class="mod-pill">2 Labs</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">Tunneling Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">MPLS</button>
  <button class="tab-btn" onclick="vt(event,'t2')">GRE</button>
  <button class="tab-btn" onclick="vt(event,'t3')">VxLAN</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Other Tunnels</button>
  <button class="tab-btn" onclick="vt(event,'t5')">Tunnel Comparison</button>
  <button class="tab-btn" onclick="vt(event,'t6')">NGFW and Tunnels</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Checklist</button>
</div>
<!-- ════ TAB 0 — TUNNELING OVERVIEW ════ -->
<div id="t0" class="tab-pane active">
<p class="sep">WHY TUNNELING EXISTS — OVERLAY OVER UNDERLAY</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>The Tunneling Concept</h3><span class="tag tag-teal">OVERVIEW</span></div>
  <div class="cp-body">
    <p>Tunneling encapsulates one network protocol inside another — creating a virtual link between two endpoints that may be separated by many intermediate hops that don't need to understand the inner protocol. The <strong>underlay</strong> is the physical/IP network; the <strong>overlay</strong> is the virtual network running on top.</p>
    <p><strong>Core use cases for tunneling:</strong></p>
    <ul>
      <li><strong>Carry non-IP traffic over IP</strong> — legacy protocols (IPX, SNA) encapsulated in IP/GRE for transport over modern IP networks</li>
      <li><strong>Connect private networks over public internet</strong> — VPN tunnels (GRE+IPsec, WireGuard) connect branch offices over the internet as if they were directly connected</li>
      <li><strong>Scale L2 over L3</strong> — VxLAN extends Layer 2 Ethernet broadcast domains across Layer 3 IP networks — essential for data centre multi-tenancy and VM migration</li>
      <li><strong>Traffic engineering</strong> — MPLS labels allow routers to forward packets along pre-computed explicit paths, bypassing normal IP routing</li>
      <li><strong>Network virtualisation</strong> — SDN overlays (OVN, NSX, ACI) use tunnels to implement virtual networks with arbitrary topology on top of physical hardware</li>
    </ul>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📦</span><h3>Encapsulation Overhead Comparison</h3><span class="tag tag-blue">OVERHEAD</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Tunnel Type</th><th>Added Headers</th><th>Total Overhead</th><th>Effective MTU (from 1500)</th></tr></thead>
      <tbody>
        <tr><td>GRE (basic)</td><td>IP(20) + GRE(4)</td><td>24 bytes</td><td>1476 bytes</td></tr>
        <tr><td>GRE + IPsec (ESP)</td><td>IP(20) + GRE(4) + ESP(~50)</td><td>~74 bytes</td><td>~1426 bytes</td></tr>
        <tr><td>VxLAN</td><td>Eth(14) + IP(20) + UDP(8) + VxLAN(8)</td><td>50 bytes</td><td>1450 bytes</td></tr>
        <tr><td>MPLS (1 label)</td><td>MPLS label(4)</td><td>4 bytes per label</td><td>1496 bytes</td></tr>
        <tr><td>MPLS (2 labels)</td><td>MPLS label(8)</td><td>8 bytes</td><td>1492 bytes</td></tr>
        <tr><td>WireGuard</td><td>IP(20) + UDP(8) + WireGuard(~32)</td><td>~60 bytes</td><td>~1440 bytes</td></tr>
        <tr><td>IPsec (ESP transport)</td><td>ESP(~40)</td><td>~40 bytes</td><td>~1460 bytes</td></tr>
      </tbody>
    </table>
    <div class="warn"><p>⚠️ <strong>MTU fragmentation is the #1 tunneling operational problem.</strong> When the effective MTU is reduced by tunnel overhead, packets that filled the original MTU now exceed the tunnel's MTU. If DF=1 is set (common with TCP), they get dropped. Solutions: MSS clamping (TCP only), Path MTU Discovery, configuring tunnel endpoints with reduced MTU, jumbo frames on the underlay.</p></div>
  </div>
</div>
</div>
<!-- ════ TAB 1 — MPLS ════ -->
<div id="t1" class="tab-pane">
<p class="sep">MPLS — MULTIPROTOCOL LABEL SWITCHING</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🏷️</span><h3>MPLS Architecture and Label Forwarding</h3><span class="tag tag-purple">MPLS</span></div>
  <div class="cp-body">
    <p>MPLS (RFC 3032) inserts a 32-bit label between the Layer 2 header and the IP header — often called "Layer 2.5". Labels allow routers to forward packets based on a fixed-length label lookup (O(1)) rather than an IP LPM lookup (more complex), and enable traffic engineering by pre-computing explicit paths through the network.</p>
<div class="cb"><pre><span class="cm">/* MPLS label format (32 bits) */</span>
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                Label (20 bits)                | Exp(3b)|S|  TTL  |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 
Label:  20-bit forwarding label (0–15 = reserved)
Exp:    3-bit traffic class (QoS, formerly called "EXP")
S bit:  Bottom of Stack — set on the innermost label
TTL:    copied from IP TTL on ingress, decremented at each LSR hop
 
<span class="cm">/* MPLS packet structure */</span>
[Ethernet hdr][MPLS label 1][MPLS label 2][IP hdr][TCP hdr][Data]
                ↑ outer label  ↑ inner label
                (multiple labels = "label stack")
 
<span class="cm">/* Label operations */</span>
PUSH:   Ingress LER adds label(s) to packet
SWAP:   Transit LSR replaces label with new label (the forwarding operation)
POP:    Egress LER removes label, exposes inner packet
 
<span class="cm">/* MPLS forwarding table (LFIB) */</span>
Incoming label | Operation | Outgoing label | Outgoing interface
100            | SWAP→200  | 200            | eth1
200            | POP       | (none)         | eth2  → IP routing takes over
300            | PUSH 400  | 400            | eth3  → add outer label</pre></div>
    <div class="ins"><p>💡 <strong>Penultimate Hop Popping (PHP):</strong> The second-to-last router in an MPLS path removes the label (POP) before forwarding to the egress router. This allows the egress router to process the packet as pure IP without needing a label lookup. Signalled by the egress router advertising label 3 (Implicit NULL) to its upstream neighbour.</p></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🛣️</span><h3>MPLS Traffic Engineering and VPNs</h3><span class="tag tag-blue">APPLICATIONS</span></div>
  <div class="cp-body">
    <p>MPLS has two dominant applications in service-provider networks:</p>
    <div class="two-col">
      <div>
        <h4>MPLS-TE (Traffic Engineering)</h4>
        <p>RSVP-TE or LDP establishes explicit Label Switched Paths (LSPs) through the network following a pre-computed route (not necessarily the shortest IGP path). Allows bandwidth reservation, fast-reroute (50ms failover), and load distribution across parallel paths.</p>
      </div>
      <div>
        <h4>MPLS L3VPN (BGP/MPLS VPN)</h4>
        <p>Service providers use MPLS+BGP to provide isolated virtual private networks to customers. Customer routes are carried in BGP with a Route Distinguisher (RD) to separate them. The MPLS label stack (outer=transport, inner=VPN) directs packets to the correct customer VRF at the egress PE router.</p>
      </div>
    </div>
  </div>
</div>
</div>
<!-- ════ TAB 2 — GRE ════ -->
<div id="t2" class="tab-pane">
<p class="sep">GRE — GENERIC ROUTING ENCAPSULATION (RFC 2784)</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>GRE Header and Operation</h3><span class="tag tag-teal">GRE</span></div>
  <div class="cp-body">
    <p>GRE (Generic Routing Encapsulation) is the simplest tunnel protocol. It encapsulates any L3 protocol packet inside an IP packet with a small GRE header. GRE itself provides no encryption or authentication — it's just a wrapper. Encryption is typically added by combining GRE with IPsec.</p>
<div class="cb"><pre><span class="cm">/* GRE packet structure */</span>
[Outer IP hdr: src=tunnel_src dst=tunnel_dst proto=47]
[GRE header: 4 bytes minimum]
  Flags(4b) | Reserved(9b) | Version(3b) | Protocol Type(16b)
  [Optional: Checksum(16b) + Reserved(16b)]
  [Optional: Key(32b)]
  [Optional: Sequence Number(32b)]
[Inner IP packet: src=orig_src dst=orig_dst]
[Original payload]
 
<span class="cm">/* GRE Protocol Type field — what's inside */</span>
0x0800 = IPv4 (most common)
0x86DD = IPv6
0x0806 = ARP
0x8847 = MPLS
 
<span class="cm">/* Linux GRE tunnel setup */</span>
<span class="cm"># Create GRE tunnel interface</span>
ip tunnel add gre1 mode gre local 203.0.113.1 remote 198.51.100.1 ttl 255
ip link set gre1 up
ip addr add 10.100.0.1/30 dev gre1
 
<span class="cm"># Route traffic through tunnel</span>
ip route add 192.168.2.0/24 via 10.100.0.2 dev gre1
 
<span class="cm"># Verify</span>
ip tunnel show
ping 10.100.0.2   <span class="cm"># ping tunnel endpoint</span>
<span class="cm">/* GRE keepalives (Cisco extension) */</span>
<span class="cm"># GRE itself has no keepalive — use OSPF/BFD over the tunnel for failure detection</span>
<span class="cm"># Or configure GRE keepalives (encapsulate keepalive inside GRE inside tunnel)</span></pre></div>
    <div class="note"><p>💡 <strong>GRE + IPsec is the classic site-to-site VPN.</strong> GRE provides the tunnel (any-protocol encapsulation, routing over the tunnel), and IPsec provides encryption and authentication. Most enterprise VPN gateways still use this combination. Modern alternatives: WireGuard (simpler, faster), IPsec IKEv2 (no GRE needed), OpenVPN.</p></div>
  </div>
</div>
</div>
<!-- ════ TAB 3 — VxLAN ════ -->
<div id="t3" class="tab-pane">
<p class="sep">VxLAN — VIRTUAL EXTENSIBLE LAN (RFC 7348)</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🏗️</span><h3>Why VxLAN Exists — Scaling L2 Over L3</h3><span class="tag tag-green">VXLAN</span></div>
  <div class="cp-body">
    <p>Traditional VLANs have a fundamental limitation: they are bounded by a Layer 3 network. Two VMs in the same VLAN must be on the same L2 segment — you can't have VLAN 100 span across multiple data centre buildings connected by IP routing. With cloud and hyperscale data centres needing millions of isolated tenant networks, the 4094 VLAN limit was also a constraint.</p>
    <p>VxLAN solves both problems: it encapsulates entire Ethernet frames (including VLAN tags) inside UDP/IP packets, allowing L2 segments to span any IP network. The VxLAN Network Identifier (VNI) is 24 bits — supporting 16 million isolated networks.</p>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📦</span><h3>VxLAN Encapsulation and VTEP</h3><span class="tag tag-blue">VXLAN DETAILS</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* VxLAN packet structure */</span>
[Outer Ethernet: src=VTEP_MAC dst=next-hop_MAC type=0x0800]
[Outer IP: src=VTEP_IP dst=remote_VTEP_IP proto=17 (UDP)]
[Outer UDP: src=ephemeral dst=4789 (IANA VxLAN port)]
[VxLAN header: 8 bytes]
  Flags(8b) | Reserved(24b) | VNI(24b) | Reserved(8b)
  (I flag = 1 when VNI is valid)
[Inner Ethernet frame: src=VM_MAC dst=dest_VM_MAC type=0x0800]
[Inner IP packet]
[Payload]
 
Total overhead: 50 bytes → effective MTU 1450 from standard 1500-byte underlay
 
<span class="cm">/* VNI — VxLAN Network Identifier */</span>
24 bits → 16,777,216 unique overlay networks
Equivalent to VLAN ID but vastly larger scale
Each VNI is a separate L2 broadcast domain
 
<span class="cm">/* VTEP — VxLAN Tunnel End Point */</span>
The device that encapsulates/decapsulates VxLAN:
  On ingress (from VM): Ethernet frame → wrap in VxLAN/UDP/IP
  On egress (to VM):    VxLAN/UDP/IP → unwrap → deliver Ethernet frame
VTEPs can be:
  - Hypervisor (Linux bridge/OVS with VXLAN)
  - Hardware switch (ToR switch with VxLAN support)
  - Dedicated gateway appliance
 
<span class="cm">/* Linux VxLAN setup */</span>
<span class="cm"># Create VxLAN tunnel interface</span>
ip link add vxlan100 type vxlan id 100 dstport 4789 \
    local 10.0.0.1 remote 10.0.0.2 dev eth0
 
ip link set vxlan100 up
ip addr add 192.168.100.1/24 dev vxlan100
 
<span class="cm"># Add static FDB entry (tell Linux: MAC xx is at remote VTEP 10.0.0.2)</span>
bridge fdb add aa:bb:cc:dd:ee:ff dev vxlan100 dst 10.0.0.2
 
<span class="cm"># Multicast VxLAN (learning mode)</span>
ip link add vxlan100 type vxlan id 100 group 239.1.1.1 dev eth0
<span class="cm"># BUM (Broadcast, Unknown unicast, Multicast) traffic → multicast group</span>
<span class="cm"># VTEPs join the multicast group — learn each other's MACs via flooding</span></pre></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🎛️</span><h3>EVPN — BGP Control Plane for VxLAN</h3><span class="tag tag-teal">EVPN</span></div>
  <div class="cp-body">
    <p>Traditional VxLAN floods BUM (Broadcast, Unknown unicast, Multicast) traffic to discover MACs — this doesn't scale. <strong>EVPN (Ethernet VPN, RFC 7432)</strong> uses BGP as a control plane to distribute MAC-to-IP-to-VTEP mappings, eliminating flooding:</p>
<div class="cb"><pre><span class="cm">/* EVPN Route Types (the key ones) */</span>
Type 2 (MAC/IP Advertisement):
  "MAC aa:bb:cc:dd:ee:ff, IP 192.168.1.5 is at VTEP 10.0.0.1, VNI 100"
  → VTEPs learn MAC/IP locations via BGP, no flooding needed
 
Type 3 (Inclusive Multicast):
  "VTEP 10.0.0.1 participates in VNI 100 BUM forwarding"
  → Ingress replication list instead of multicast
 
<span class="cm">/* Symmetric IRB — Integrated Routing and Bridging */</span>
<span class="cm"># Layer 3 routing between VNIs without leaving the VxLAN fabric</span>
<span class="cm"># Each VTEP acts as a distributed gateway for its local VMs</span>
<span class="cm"># No hairpinning through a central gateway router</span>
<span class="cm">/* Modern data centre: Leaf-Spine with VxLAN+EVPN */</span>
Spine switches:  pure IP underlay + iBGP route reflector for EVPN
Leaf switches:   VTEPs + EVPN BGP speakers
VMs/containers:  connected to leaf switches, in VxLAN VNIs
 
<span class="cm">/* FRR VxLAN+EVPN config */</span>
router bgp 65001
  address-family l2vpn evpn
    neighbor SPINE activate
    advertise-all-vni</pre></div>
  </div>
</div>
</div>
<!-- ════ TAB 4 — OTHER TUNNELS ════ -->
<div id="t4" class="tab-pane">
<p class="sep">OTHER TUNNEL TYPES — GENEVE, WIREGUARD, 6IN4</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>Tunnel Protocol Reference</h3><span class="tag tag-blue">REFERENCE</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Protocol</th><th>RFC</th><th>Transport</th><th>Overhead</th><th>Use Case</th></tr></thead>
      <tbody>
        <tr><td><strong>GRE</strong></td><td>RFC 2784</td><td>IP Proto 47</td><td>24B</td><td>Site-to-site VPN (with IPsec), multi-protocol transport, GRE keepalives</td></tr>
        <tr><td><strong>IP-in-IP</strong></td><td>RFC 2003</td><td>IP Proto 4</td><td>20B</td><td>Simple IPv4-in-IPv4; no options/encryption, minimum overhead</td></tr>
        <tr><td><strong>6in4</strong></td><td>RFC 4213</td><td>IP Proto 41</td><td>20B</td><td>IPv6-in-IPv4 tunnels; connect IPv6 islands over IPv4 backbone</td></tr>
        <tr><td><strong>VxLAN</strong></td><td>RFC 7348</td><td>UDP 4789</td><td>50B</td><td>Data centre overlay, VM mobility, L2 over L3, cloud networking</td></tr>
        <tr><td><strong>GENEVE</strong></td><td>RFC 8926</td><td>UDP 6081</td><td>50B+</td><td>Next-gen overlay (OpenStack, OVN); extensible TLV options in header</td></tr>
        <tr><td><strong>MPLS</strong></td><td>RFC 3032</td><td>Between L2/L3</td><td>4B/label</td><td>Service provider TE, L3VPN, L2VPN, fast-reroute</td></tr>
        <tr><td><strong>IPsec (tunnel)</strong></td><td>RFC 4303</td><td>IP Proto 50/51</td><td>~50B</td><td>Encrypted site-to-site and remote-access VPN; mandatory encryption</td></tr>
        <tr><td><strong>WireGuard</strong></td><td>—</td><td>UDP (custom)</td><td>~60B</td><td>Modern VPN: simple, fast, strong crypto (ChaCha20/Poly1305/Curve25519)</td></tr>
        <tr><td><strong>VLAN (802.1Q)</strong></td><td>IEEE 802.1Q</td><td>Ethernet tag</td><td>4B</td><td>L2 network segmentation; not technically a tunnel but a virtual L2 overlay</td></tr>
        <tr><td><strong>PPPoE</strong></td><td>RFC 2516</td><td>Ethernet</td><td>8B</td><td>ISP DSL access; encapsulates PPP in Ethernet; reduces MTU to 1492</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>
<!-- ════ TAB 5 — TUNNEL COMPARISON ════ -->
<div id="t5" class="tab-pane">
<p class="sep">WHEN TO USE WHICH TUNNEL — DECISION GUIDE</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>Tunnel Selection Decision Guide</h3><span class="tag tag-green">DECISION</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Which tunnel to use — decision tree */</span>
 
Need to connect two office networks over internet securely?
  → IPsec IKEv2 (standard, vendor-interoperable)
  → WireGuard (modern, simple, fast — if both ends are Linux/modern)
  → GRE + IPsec (if you need routing protocols over the tunnel)
 
Need to carry non-IP traffic (e.g., IPX, MPLS) over IP?
  → GRE (supports any EtherType in Protocol Type field)
 
Need to scale L2 (VMs, containers) across IP data centre fabric?
  → VxLAN (with EVPN for control plane)
  → GENEVE (if you need extensible metadata in the header)
 
Need traffic engineering and bandwidth reservation in SP network?
  → MPLS-TE with RSVP-TE
 
Need the absolute minimum overhead (no encryption needed)?
  → IP-in-IP (20 bytes overhead, IPv4 only)
 
Connecting IPv6 island over IPv4 network?
  → 6in4 (static), 6to4 (automatic), Teredo (through NAT)
 
Need a simple test or diagnostic tunnel?
  → GRE (easiest to configure on Linux with ip tunnel add)</pre></div>
  </div>
</div>
</div>
<!-- ════ TAB 6 — NGFW AND TUNNELS ════ -->
<div id="t6" class="tab-pane">
<p class="sep">NGFW CHALLENGES WITH TUNNELED TRAFFIC</p>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>The Tunnel Inspection Problem</h3><span class="tag tag-red">NGFW</span></div>
  <div class="cp-body">
    <p>Tunnels present a fundamental challenge for NGFWs: the firewall sees the outer packet (which may be innocuous — UDP to port 4789, or IP proto 47) but not the inner packet (which may contain malicious traffic). An attacker can use a tunnel to bypass firewall rules by hiding prohibited traffic inside permitted tunnel traffic.</p>
    <table class="t-table">
      <thead><tr><th>Tunnel Type</th><th>What NGFW Sees Without Inspection</th><th>Inspection Approach</th></tr></thead>
      <tbody>
        <tr><td>GRE</td><td>IP packets destined to tunnel endpoint (Proto 47)</td><td>Decapsulate GRE at firewall, inspect inner IP packet against policy, re-encapsulate or forward</td></tr>
        <tr><td>VxLAN</td><td>UDP port 4789 traffic between VTEPs</td><td>Decapsulate at hypervisor/switch level before reaching NGFW, or deploy NGFW as a VTEP; EVPN allows policy attachment to VNIs</td></tr>
        <tr><td>IPsec (encrypted)</td><td>Encrypted ESP/AH packets — opaque content</td><td>Terminate IPsec at NGFW → inspect decrypted content → re-encrypt. Or use split-tunneling to bypass NGFW for trusted traffic</td></tr>
        <tr><td>DNS tunnelling</td><td>Legitimate-looking UDP 53 traffic</td><td>Deep DNS inspection: entropy analysis, label length, query frequency (see M07)</td></tr>
        <tr><td>HTTPS tunnels</td><td>TLS-encrypted traffic on 443</td><td>SSL inspection (see M08)</td></tr>
        <tr><td>ICMP tunnels</td><td>ICMP Echo Request/Reply</td><td>Inspect ICMP data field for non-standard content (see M06)</td></tr>
      </tbody>
    </table>
<div class="cb"><pre><span class="cm">/* GRE decapsulation in NGFW (VPP-style) */</span>
<span class="cm">/* Packet arrives: outer IP → GRE → inner IP → TCP → payload */</span>
 
1. ip4-input: outer IP validated, routed to gre-input graph node
2. gre-input: outer IP and GRE header stripped
3. Inner packet injected back into ip4-input
4. ip4-input: inner IP subject to full policy (ACL, conntrack, DPI)
5. If policy permits: route inner packet; NGFW logs both
   outer (IP src/dst of tunnel endpoints) and inner (actual src/dst)
 
<span class="cm">/* VxLAN inspection flow */</span>
Outer UDP dst=4789 → vxlan-input → strip outer Eth+IP+UDP+VxLAN
Inner Ethernet frame → subject to L2/L3 policy per VNI
VNI 100 = "tenant network A" → apply tenant A's security policy
VNI 200 = "tenant network B" → apply tenant B's security policy</pre></div>
  </div>
</div>
</div>
<!-- ════ TAB 7 — LABS ════ -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>GRE Tunnel Setup and Analysis</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Create a GRE tunnel between two Linux VMs, route traffic through it, and capture the encapsulated packets to understand the header structure.</p>
    <div class="lab-step"><div class="sn">1</div><div>On VM1 (outer IP 10.0.0.1): <code>sudo ip tunnel add gre1 mode gre local 10.0.0.1 remote 10.0.0.2 ttl 255; sudo ip link set gre1 up; sudo ip addr add 172.16.0.1/30 dev gre1</code>. On VM2 (outer IP 10.0.0.2): same commands with reversed IPs. Test: <code>ping 172.16.0.2</code>.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Capture the traffic: on VM1, run <code>sudo tcpdump -i eth0 proto 47 -v</code> while pinging through the tunnel. You should see GRE packets (IP proto 47) with an outer IP src/dst and an inner ICMP payload. Note the double IP header in the capture.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Open the capture in Wireshark. Expand the GRE packet: outer Ethernet, outer IP (proto=47), GRE header (protocol type=0x0800 = IPv4), inner IP, inner ICMP. Identify the tunnel overhead: how many extra bytes vs a direct ICMP ping?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Test MTU: ping with large packets: <code>ping -M do -s 1472 172.16.0.2</code>. The effective MTU through GRE is 1476 (1500-20-4). With -s 1473 (1501B IP = exceeds 1476B GRE MTU), you should get "Frag needed". Add a route to a remote subnet through the tunnel and verify end-to-end connectivity.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>VxLAN Overlay Network</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Create a VxLAN overlay that allows two VMs on different physical hosts (different subnets) to appear as if they're on the same L2 segment.</p>
    <div class="lab-step"><div class="sn">1</div><div>On Host1 (underlay IP 10.0.0.1): create VxLAN interface with VNI 100: <code>sudo ip link add vxlan100 type vxlan id 100 dstport 4789 local 10.0.0.1 remote 10.0.0.2 dev eth0; sudo ip link set vxlan100 up; sudo ip addr add 192.168.100.1/24 dev vxlan100</code>. On Host2: same with .2 addresses.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Capture VxLAN traffic: on Host1, <code>sudo tcpdump -i eth0 udp port 4789 -v</code> while pinging 192.168.100.2. In Wireshark, expand the packet: outer Ethernet, outer IP (UDP), VxLAN header (VNI=100), inner Ethernet, inner ICMP.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Verify the inner Ethernet frame: the inner Ethernet dst/src are the VxLAN interface MAC addresses, not the physical interface MACs. This is the key insight: to the overlay network, the VxLAN interfaces appear directly connected at L2 regardless of the physical topology.</div></div>
    <div class="lab-step"><div class="sn">4</div><div><strong>Bonus — multiple VNIs:</strong> Add a second VxLAN interface with VNI 200 on both hosts with a different /24 overlay subnet. Verify VNI 100 and VNI 200 are completely isolated — ping from VNI 100 cannot reach VNI 200 addresses (no inter-VNI routing configured). This is L2 isolation between tenants.</div></div>
  </div>
</div>
</div>
<!-- ════ TAB 8 — CHECKLIST ════ -->
<div id="t8" class="tab-pane">
<p class="sep">M13 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know the tunneling concept: overlay over underlay, encapsulate inner packet inside outer packet</li>
  <li>Know 5 use cases for tunneling: carry non-IP over IP, connect private nets over internet, scale L2 over L3, traffic engineering, network virtualisation</li>
  <li>Know tunnel overhead and effective MTU for each: GRE=24B/1476B, VxLAN=50B/1450B, MPLS=4B/label, WireGuard=~60B</li>
  <li>Know MTU is the #1 tunneling operational problem; know solutions: MSS clamping, PMTUD, jumbo frames on underlay</li>
  <li>Know MPLS label format: 20-bit label, 3-bit Exp (QoS), S bit (bottom of stack), 8-bit TTL</li>
  <li>Know 3 MPLS operations: PUSH (ingress adds label), SWAP (transit replaces label), POP (egress removes label)</li>
  <li>Know PHP (Penultimate Hop Popping): second-to-last router pops label so egress does pure IP lookup</li>
  <li>Know MPLS applications: Traffic Engineering (explicit paths), L3VPN (isolated customer routing)</li>
  <li>Know GRE: IP proto 47, 4-byte header, Protocol Type field (0x0800=IPv4), no built-in encryption</li>
  <li>Know GRE+IPsec is the classic site-to-site VPN combination</li>
  <li>Know why VxLAN exists: scale L2 over L3 networks, overcome 4094 VLAN limit (VNI=24 bits, 16M networks)</li>
  <li>Know VxLAN encapsulation: outer Eth+IP+UDP(4789)+VxLAN(8B) + inner Ethernet frame; total overhead=50B</li>
  <li>Know VTEP: device that encapsulates/decapsulates VxLAN; can be hypervisor, hardware switch, or appliance</li>
  <li>Know VNI: 24-bit VxLAN Network Identifier; each VNI is an isolated L2 broadcast domain</li>
  <li>Know EVPN: BGP control plane for VxLAN; distributes MAC/IP/VTEP mappings; eliminates BUM flooding</li>
  <li>Know GENEVE: next-gen overlay (RFC 8926), extensible TLV header, used by OVN and OpenStack</li>
  <li>Know when to use each tunnel: VxLAN for DC overlay, GRE+IPsec for site-to-site VPN, MPLS for SP TE</li>
  <li>Know the NGFW tunnel inspection challenge: outer packet may be permitted while inner packet violates policy</li>
  <li>Know NGFW approaches: GRE decapsulation for inspection, VxLAN per-VNI policy, IPsec termination + inspect + re-encrypt</li>
  <li>Completed Lab 1: created GRE tunnel, captured encapsulated packets, tested MTU limits</li>
  <li>Completed Lab 2: created VxLAN overlay, verified L2 connectivity across L3 network, tested VNI isolation</li>
</ul>
<div class="phase-complete">
  <h3>🎉 Phase 3 Complete — Routing and Forwarding</h3>
  <p>You have completed all 4 modules of Phase 3: Routing and FIB (M10), OSPF (M11), BGP (M12), and Tunneling (M13). You can now design, analyse, and implement the routing infrastructure an enterprise or service-provider network requires. Move to <strong>Phase 4 — Linux Networking and Socket Programming</strong>, starting with <strong>M14 - Linux Network Stack</strong>.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/networking-mastery/m12-bgp/">← M12 BGP</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m14-linux-stack/">Next: M14 - Linux Network Stack →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
