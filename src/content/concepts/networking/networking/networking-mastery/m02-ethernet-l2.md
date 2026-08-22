---
title: "M02 - Ethernet and Layer 2"
description: "NETWORKING MASTERY · PHASE 1 · MODULE 02 · WEEKS 1–2 🔌 Ethernet and Layer 2 MAC addressing · Ethernet frames · ARP · Switching · VLANs · STP · RSTP Beginner Prerequisite: M01…"
domain: networking
track: networking-mastery
order: 2
ownHeader: true
url: /learning/networking-mastery/m02-ethernet-l2/
---

<style>
/* ── Base ───────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 40%,#7a5800 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0;
}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#f0c880;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#f0dfa0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#faecc8}

/* Tabs */
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#f0c880;border-bottom-color:#f0c880}
.tab-pane{display:none}
.tab-pane.active{display:block}

/* Concept panels */
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

/* Panel colour variants */
.p-blue  .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue  .cp-hdr{background:#0d2030}
.p-teal  .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal  .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.p-green  .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green  .cp-hdr{background:#0a2018}
.p-red    .cp-hdr{background:#faeaea}[data-theme=dark] .p-red    .cp-hdr{background:#2a0808}
.p-amber  .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber  .cp-hdr{background:#2a1e00}
.p-gray   .cp-hdr{background:#f0f0f0}[data-theme=dark] .p-gray   .cp-hdr{background:#1a1a1a}

.tag-blue  {background:#d0e8f8;color:#1a4a7c}
.tag-teal  {background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}
.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green {background:#c8e8d4;color:#0e4a28}
.tag-red   {background:#f4d0d0;color:#6c1a1a}
.tag-amber {background:#fae8a0;color:#5a3800}
.tag-gray  {background:#e0e0e0;color:#444}

/* Code blocks */
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #c09030}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#f0e0a8;white-space:pre}
.cm{color:#8a7a40}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}

/* Insight + warning */
.ins{background:#fdf8e8;border:1.5px solid #c09030;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#2a1e00;border-color:#c09030}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#7a5800}
[data-theme=dark] .ins strong{color:#f0c880}

.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}

.note{background:#e8f5f0;border:1.5px solid #0f6e56;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .note{background:#0a2420;border-color:#2a9a8e}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.note strong{color:#0e5248}
[data-theme=dark] .note strong{color:#5dd6c8}

/* Analogy box */
.analogy{background:linear-gradient(135deg,#fffbe8,#fdf4dc);border:1.5px solid #e8c870;border-radius:10px;padding:1.1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .analogy{background:linear-gradient(135deg,#201800,#1a1200);border-color:#c09030}
.analogy-title{font-size:.72rem;font-family:monospace;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#7a5800;margin-bottom:.5rem}
[data-theme=dark] .analogy-title{color:#f0c880}
.analogy p{font-size:.88rem;line-height:1.7;color:var(--text-color,#222);margin:0}

/* Ethernet frame diagram */
.frame-diagram{margin:1rem 0;overflow-x:auto}
.frame-row{display:flex;gap:2px;min-width:600px;align-items:stretch;margin-bottom:4px}
.frame-label{font-size:.72rem;font-family:monospace;min-width:80px;display:flex;align-items:center;color:var(--light-text,#666);flex-shrink:0;padding-right:6px}
.ff{
  border-radius:5px;padding:8px 6px;font-size:.72rem;
  font-weight:600;text-align:center;border:1.5px solid transparent;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  line-height:1.3;
}
.ff-pre{background:#e8e8f8;border-color:#b0b0d8;color:#3a3a6c}
.ff-dst{background:#fdf4dc;border-color:#e8c870;color:#5a3800}
.ff-src{background:#faeee4;border-color:#e8b090;color:#6a2800}
.ff-typ{background:#e0f0ee;border-color:#90c8b8;color:#0a3a30}
.ff-dat{background:#e8f5e8;border-color:#a0d0a0;color:#1a4a1a}
.ff-crc{background:#faeaea;border-color:#e8b0b0;color:#6c1a1a}
.ff-vlan{background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c;outline:2px solid #5b3a8c;outline-offset:1px}
.ff-bytes{font-size:.65rem;font-weight:400;opacity:.8;margin-top:2px}
[data-theme=dark] .ff-pre{background:#1a1a30;border-color:#6060a8;color:#a0a0e0}
[data-theme=dark] .ff-dst{background:#201800;border-color:#c09030;color:#f0d080}
[data-theme=dark] .ff-src{background:#1e1000;border-color:#b06030;color:#f0b070}
[data-theme=dark] .ff-typ{background:#0a2020;border-color:#3a9080;color:#80d8c0}
[data-theme=dark] .ff-dat{background:#0c2010;border-color:#3a8040;color:#80d890}
[data-theme=dark] .ff-crc{background:#2a0808;border-color:#a03030;color:#f09090}
[data-theme=dark] .ff-vlan{background:#1c1030;border-color:#7060a8;color:#c0a8f0}

/* MAC address visual */
.mac-visual{display:flex;gap:2px;align-items:stretch;margin:.8rem 0;flex-wrap:wrap}
.mac-octet{
  background:#fdf4dc;border:1.5px solid #e8c870;border-radius:6px;
  padding:8px 12px;text-align:center;font-family:monospace;font-size:.9rem;
  font-weight:700;color:#5a3800;min-width:50px;
}
[data-theme=dark] .mac-octet{background:#201800;border-color:#c09030;color:#f0d080}
.mac-sep{display:flex;align-items:center;font-size:1.2rem;color:var(--light-text,#aaa);padding:0 2px}
.mac-label{font-size:.7rem;color:var(--light-text,#666);margin-top:4px;font-family:monospace}
.mac-group{display:flex;flex-direction:column;align-items:center;gap:0}
.mac-section-label{font-size:.68rem;font-family:monospace;font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:3px}

/* Switching table */
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.86rem}
.t-table th{background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#7a5800}

/* Topology diagram using divs */
.topo{display:flex;flex-direction:column;gap:8px;margin:1rem 0;padding:1.2rem;background:var(--bg-color,#f8f8f8);border-radius:10px;border:1.5px solid var(--border-color,#e0e0e0)}
.topo-row{display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap}
.topo-device{
  background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#ddd);
  border-radius:8px;padding:.5rem .9rem;text-align:center;
  font-size:.78rem;font-weight:600;min-width:80px;
}
.topo-device.active{background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c}
.topo-device.switch{background:#fdf4dc;border-color:#e8c870;color:#5a3800}
.topo-device.router{background:#e0f0ee;border-color:#90c8b8;color:#0a3a30}
.topo-device.host{background:#e8f5e8;border-color:#a0d0a0;color:#1a4a1a}
.topo-link{font-size:.8rem;color:var(--light-text,#888);font-family:monospace}
.topo-label{font-size:.7rem;color:var(--light-text,#888);font-family:monospace;text-align:center;margin-top:3px}

/* ARP flow steps */
.flow-list{display:flex;flex-direction:column;gap:0;margin:1rem 0}
.fl-step{
  display:flex;gap:14px;padding:10px 14px;
  border-left:2px solid var(--border-color,#e0e0e0);
  margin-left:14px;position:relative;
}
.fl-step::before{
  content:attr(data-n);position:absolute;left:-14px;top:12px;
  width:26px;height:26px;border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  font-size:.72rem;font-weight:700;color:#fff;
  background:var(--sc,#7a5800);
}
.fl-step:last-child{border-left-color:transparent}
.fl-title{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin-bottom:.25rem}
.fl-detail{font-size:.85rem;color:var(--text-color,#444);line-height:1.6}
.fl-code{font-family:monospace;font-size:.78rem;display:inline-block;background:#0a1628;color:#f0c880;padding:2px 8px;border-radius:4px;margin-top:.3rem}

/* VLAN diagram */
.vlan-wrap{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:1rem 0}
@media(max-width:540px){.vlan-wrap{grid-template-columns:1fr}}
.vlan-box{border-radius:10px;border:2px solid;padding:1rem;overflow:hidden}
.vlan-title{font-size:.8rem;font-family:monospace;font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.6rem}
.vlan-member{font-size:.82rem;padding:4px 8px;border-radius:5px;margin-bottom:3px;font-family:monospace}

/* STP states */
.stp-states{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:.7rem;margin:1rem 0}
.stp-state{border-radius:8px;padding:.8rem 1rem;border:1.5px solid var(--border-color,#e0e0e0);background:var(--card-bg,#fff)}
.stp-state-name{font-size:.82rem;font-weight:700;font-family:monospace;margin-bottom:.3rem}
.stp-state-desc{font-size:.78rem;color:var(--text-color,#444);line-height:1.55}

/* Two-col */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}

/* Lab box */
.lab-box{border:2px solid #7a5800;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#7a5800;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#7a5800;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}

/* Checklist */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#7a5800;margin-top:-.05rem}

/* Nav */
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}

/* Section divider */
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>
<!-- ── HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 1 · MODULE 02 · WEEKS 1–2</div>
  <div class="mod-title">🔌 Ethernet and Layer 2</div>
  <div class="mod-subtitle">MAC addressing · Ethernet frames · ARP · Switching · VLANs · STP · RSTP</div>
  <div class="mod-pills">
    <span class="mod-pill">Beginner</span>
    <span class="mod-pill">Prerequisite: M01</span>
    <span class="mod-pill">IEEE 802.3</span>
    <span class="mod-pill">802.1Q VLANs</span>
    <span class="mod-pill">802.1D STP</span>
    <span class="mod-pill">3 Labs</span>
  </div>
</div>
<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">Ethernet Basics</button>
  <button class="tab-btn" onclick="vt(event,'t1')">Ethernet Frame</button>
  <button class="tab-btn" onclick="vt(event,'t2')">MAC Addresses</button>
  <button class="tab-btn" onclick="vt(event,'t3')">ARP</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Switches and Forwarding</button>
  <button class="tab-btn" onclick="vt(event,'t5')">VLANs</button>
  <button class="tab-btn" onclick="vt(event,'t6')">STP and RSTP</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Checklist</button>
</div>
<!-- ════════════ TAB 0 — ETHERNET BASICS ════════════ -->
<div id="t0" class="tab-pane active">
<p class="sep">WHAT IS ETHERNET AND WHY IT DOMINATES</p>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">📜</span><h3>Ethernet — A Brief History</h3><span class="tag tag-amber">BACKGROUND</span></div>
  <div class="cp-body">
    <p>Ethernet was invented at Xerox PARC in 1973 by Robert Metcalfe and David Boggs. It was standardised as IEEE 802.3 in 1983 and has since become the dominant wired networking technology on the planet. Today it runs at speeds from 10 Mbps (historical) to 400 Gbps (data centre), over copper cable, optical fibre, and even backplane connections inside chassis switches.</p>
    <p>Why has Ethernet survived for 50+ years? Because it is <strong>simple, cheap, and extensible</strong>. The core frame format has barely changed since 1983. The same Ethernet frame that worked on a 10 Mbps coaxial cable in 1985 is structurally identical to the one flying over a 100 Gbps fibre link today.</p>
    <ul>
      <li><strong>Ubiquity:</strong> Every laptop, server, router, switch, and data-plane NIC speaks Ethernet natively</li>
      <li><strong>Scalability:</strong> Speed has scaled 10,000× (10 Mbps → 100 Gbps) without changing the fundamental frame format</li>
      <li><strong>Cost:</strong> Commodity Ethernet hardware (NICs, switches) is extremely cheap compared to alternatives</li>
      <li><strong>Simplicity:</strong> The protocol is well-understood and easy to implement and debug</li>
    </ul>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Layer 2 — What It Does in the Stack</h3><span class="tag tag-blue">ROLE IN STACK</span></div>
  <div class="cp-body">
    <p>As you learned in M01, Layer 2 (Data Link) handles <strong>node-to-node delivery on the same network segment</strong>. The key word is "same network" — Layer 2 only moves frames between devices that are directly connected (or connected through switches). When a packet needs to cross to a different network, Layer 3 (IP routing) takes over.</p>
    <p>A useful mental model: <strong>Layer 2 is the local delivery van, Layer 3 is the national courier.</strong> The van moves parcels within a city (your LAN). When a parcel needs to go cross-country, the national courier (IP routing) takes it to the destination city, then a local van (another L2 network) makes the final delivery.</p>
    <p><strong>Layer 2 devices on a typical network:</strong></p>
    <ul>
      <li><strong>NIC (Network Interface Card)</strong> — every host has one; generates and receives Ethernet frames</li>
      <li><strong>Switch</strong> — forwards frames between ports using MAC address learning; operates entirely at L2</li>
      <li><strong>Bridge</strong> — an older device connecting two network segments; conceptually the same as a 2-port switch</li>
      <li><strong>Access Point (WiFi)</strong> — bridges WiFi (802.11) frames to Ethernet (802.3) frames</li>
    </ul>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📡</span><h3>Ethernet Speed Standards</h3><span class="tag tag-teal">STANDARDS</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Standard</th><th>Speed</th><th>Medium</th><th>Max Distance</th><th>Common Use</th></tr></thead>
      <tbody>
        <tr><td><code>10BASE-T</code></td><td>10 Mbps</td><td>Cat3/Cat5 copper</td><td>100 m</td><td>Legacy — almost extinct</td></tr>
        <tr><td><code>100BASE-TX</code></td><td>100 Mbps</td><td>Cat5e copper</td><td>100 m</td><td>Old office networks</td></tr>
        <tr><td><code>1000BASE-T</code></td><td>1 Gbps</td><td>Cat5e/Cat6 copper</td><td>100 m</td><td>Desktops, home networks</td></tr>
        <tr><td><code>10GBASE-T</code></td><td>10 Gbps</td><td>Cat6A copper</td><td>100 m</td><td>Server uplinks, data centres</td></tr>
        <tr><td><code>10GBASE-SR</code></td><td>10 Gbps</td><td>Multi-mode fibre</td><td>300 m</td><td>Data centre racks</td></tr>
        <tr><td><code>25GBASE-SR</code></td><td>25 Gbps</td><td>Multi-mode fibre</td><td>100 m</td><td>Server NICs (your Mellanox)</td></tr>
        <tr><td><code>100GBASE-SR4</code></td><td>100 Gbps</td><td>Multi-mode fibre</td><td>100 m</td><td>Spine switches, DPDK servers</td></tr>
        <tr><td><code>400GBASE-DR4</code></td><td>400 Gbps</td><td>Single-mode fibre</td><td>500 m</td><td>Hyperscale data centres</td></tr>
      </tbody>
    </table>
    <p>For your DPDK and VPP work, you're most likely working with 10G, 25G, or 100G Ethernet over SFP+/QSFP28 optical modules on Mellanox ConnectX NICs.</p>
  </div>
</div>
</div>
<!-- ════════════ TAB 1 — ETHERNET FRAME ════════════ -->
<div id="t1" class="tab-pane">
<p class="sep">ETHERNET FRAME FORMAT — BYTE BY BYTE</p>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">📦</span><h3>The Ethernet II Frame</h3><span class="tag tag-amber">FRAME FORMAT</span></div>
  <div class="cp-body">
    <p>There are two Ethernet frame formats in use: <strong>Ethernet II</strong> (DIX) and <strong>IEEE 802.3</strong>. Ethernet II is dominant on modern networks — it's what you'll see in every packet capture. The key difference is the 2-byte field after the MAC addresses: Ethernet II uses it as an <strong>EtherType</strong> (identifies the L3 protocol), while 802.3 uses it as a <strong>Length</strong> field. Since EtherType values are always ≥ 1536 (0x0600) and length values are ≤ 1500, a receiver can tell them apart instantly.</p>
  </div>
</div>
<div class="frame-diagram">
  <div class="frame-row">
    <div class="frame-label">On wire</div>
    <div class="ff ff-pre" style="flex:.7">Preamble<div class="ff-bytes">7 bytes</div></div>
    <div class="ff ff-pre" style="flex:.4">SFD<div class="ff-bytes">1 byte</div></div>
    <div class="ff ff-dst" style="flex:1.2">Destination MAC<div class="ff-bytes">6 bytes</div></div>
    <div class="ff ff-src" style="flex:1.2">Source MAC<div class="ff-bytes">6 bytes</div></div>
    <div class="ff ff-typ" style="flex:.7">EtherType<div class="ff-bytes">2 bytes</div></div>
    <div class="ff ff-dat" style="flex:3">Payload (Data)<div class="ff-bytes">46–1500 bytes</div></div>
    <div class="ff ff-crc" style="flex:.5">CRC/FCS<div class="ff-bytes">4 bytes</div></div>
  </div>
  <div style="font-size:.72rem;color:var(--light-text,#888);margin-top:4px;font-family:monospace;text-align:right">Total: 64–1518 bytes (minimum 64B to detect collisions, max 1518B standard MTU)</div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Every Field Explained</h3><span class="tag tag-blue">FIELD REFERENCE</span></div>
  <div class="cp-body">
    <h4>Preamble (7 bytes) + SFD (1 byte)</h4>
    <p>The preamble is 7 bytes of alternating 1s and 0s (<code>10101010...</code>). It allows the receiver's clock to synchronise with the sender's clock before actual data arrives — like a "ready?" signal. The Start Frame Delimiter (SFD) is <code>10101011</code> — the final bit breaks the alternating pattern to signal "frame starts NOW". These 8 bytes are added and stripped by the NIC hardware and never appear in software packet buffers.</p>
    <h4>Destination MAC Address (6 bytes)</h4>
    <p>The hardware address of the intended recipient. The switch uses this to decide which port to forward the frame to. Three special cases:</p>
    <ul>
      <li><strong>Unicast</strong> — sent to one specific device (LSB of first byte = 0)</li>
      <li><strong>Broadcast</strong> — <code>FF:FF:FF:FF:FF:FF</code> — all devices on the segment receive it</li>
      <li><strong>Multicast</strong> — <code>01:00:5E:xx:xx:xx</code> for IPv4 multicast — sent to a group of devices</li>
    </ul>
    <h4>Source MAC Address (6 bytes)</h4>
    <p>The hardware address of the sender. Switches read this field to <strong>learn</strong> which MAC address is reachable on which port and build their MAC address table.</p>
    <h4>EtherType (2 bytes)</h4>
    <p>Identifies the Layer 3 protocol carried in the payload. Most important values:</p>
    <ul>
      <li><code>0x0800</code> — IPv4 payload</li>
      <li><code>0x0806</code> — ARP payload</li>
      <li><code>0x86DD</code> — IPv6 payload</li>
      <li><code>0x8100</code> — 802.1Q VLAN tag (frame is VLAN-tagged)</li>
      <li><code>0x88CC</code> — LLDP (Link Layer Discovery Protocol)</li>
      <li><code>0x8847</code> — MPLS unicast</li>
    </ul>
    <p>In DPDK and VPP, the EtherType field is the first thing the <code>ethernet-input</code> graph node reads to dispatch the frame to the correct next node (ip4-input, ip6-input, arp-input, etc.).</p>
    <h4>Payload / Data (46–1500 bytes)</h4>
    <p>The IP packet (or ARP message, or other L3 PDU) carried by the frame. The minimum payload is 46 bytes — if the IP packet is smaller, it gets <strong>padded</strong> with zeros to reach 46 bytes. This ensures the total frame is at least 64 bytes, which is required for collision detection in half-duplex Ethernet (legacy).</p>
    <h4>FCS / CRC (4 bytes)</h4>
    <p>Frame Check Sequence — a 32-bit CRC (Cyclic Redundancy Check) computed over all frame fields from Destination MAC through Payload. The receiver recomputes the CRC and compares to the transmitted value. If they differ, the frame is silently <strong>dropped</strong> (no error is sent back — error recovery is TCP's job at L4). NICs typically handle CRC computation in hardware, and most OSes strip the FCS before passing the frame to software — so you won't see it in Wireshark captures from a NIC in normal mode.</p>
    <h4>MTU — Maximum Transmission Unit</h4>
    <p>The maximum payload size is <strong>1500 bytes</strong> — this is the standard Ethernet MTU. If an IP packet is larger, it must be <strong>fragmented</strong> at the IP layer (or the application told to send smaller chunks via Path MTU Discovery). Many data-centre networks use <strong>Jumbo Frames</strong> with MTU 9000 bytes to reduce CPU overhead for large transfers — your DPDK/VPP setup likely uses jumbo frames.</p>
  </div>
</div>
<div class="ins">
  <p>💡 <strong>Why minimum 64 bytes?</strong> In classic CSMA/CD Ethernet (before full-duplex switches), a sending station needed to keep transmitting long enough that if a collision occurred at the far end of the cable, the collision signal could travel back and reach the sender while it was still transmitting. At 10 Mbps on a 100m cable, this required a minimum frame size of 64 bytes. Modern switched full-duplex Ethernet has no collisions, but the 64-byte minimum is kept for backwards compatibility.</p>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Frame Overhead Calculation</h3><span class="tag tag-green">PERFORMANCE</span></div>
  <div class="cp-body">
    <p>Understanding Ethernet overhead is essential for data-plane performance engineering:</p>
<div class="cb"><pre><span class="cm">/* Ethernet frame overhead breakdown */</span>
Preamble + SFD :  8 bytes  (NIC hardware only — not in software buffer)
Ethernet header: 14 bytes  (dst MAC 6 + src MAC 6 + EtherType 2)
FCS/CRC        :  4 bytes  (usually stripped by NIC)
Interframe Gap :  12 bytes (minimum idle time between frames — layer 1)
─────────────────────────
Wire overhead  :  38 bytes per frame (preamble + header + FCS + IFG)
 
<span class="cm">/* Efficiency at minimum frame size (64 bytes) */</span>
Payload bytes  : 46 bytes (64 - 14 header - 4 FCS = 46)
Wire bytes     : 64 + 8 preamble + 12 IFG = 84 bytes total
Efficiency     : 46 / 84 = 54.8%  ← terrible! lots of overhead for small pkts
 
<span class="cm">/* Efficiency at maximum frame size (1518 bytes) */</span>
Payload bytes  : 1500 bytes
Wire bytes     : 1518 + 8 + 12 = 1538 bytes
Efficiency     : 1500 / 1538 = 97.5%  ← much better
 
<span class="cm">/* This is WHY jumbo frames (MTU 9000) help in data centres */</span>
<span class="cm">/* Fewer frames per byte = less header processing overhead */</span></pre></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 2 — MAC ADDRESSES ════════════ -->
<div id="t2" class="tab-pane">
<p class="sep">MAC ADDRESSES — HARDWARE IDENTITY</p>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">🏷️</span><h3>What is a MAC Address?</h3><span class="tag tag-amber">CORE CONCEPT</span></div>
  <div class="cp-body">
    <p>A MAC (Media Access Control) address is a <strong>48-bit (6-byte) hardware identifier</strong> assigned to every network interface. Unlike IP addresses which are logical and can be changed by software, MAC addresses are (traditionally) burned into the NIC's hardware at manufacture and intended to be globally unique. In practice, modern OSes allow MAC address spoofing in software.</p>
    <p><strong>MAC address notation:</strong> Written as 6 pairs of hexadecimal digits, separated by colons or hyphens:</p>
    <ul>
      <li><code>aa:bb:cc:dd:ee:ff</code> — colon-separated (Linux, most tools)</li>
      <li><code>AA-BB-CC-DD-EE-FF</code> — hyphen-separated (Windows)</li>
      <li><code>aabb.ccdd.eeff</code> — dot-separated groups of 4 (Cisco)</li>
    </ul>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🗂️</span><h3>MAC Address Structure — OUI and NIC-Specific</h3><span class="tag tag-blue">STRUCTURE</span></div>
  <div class="cp-body">
    <p>A MAC address has a precise internal structure:</p>
    <div style="text-align:center;margin:.8rem 0">
      <div style="font-size:.72rem;font-family:monospace;margin-bottom:4px;color:var(--light-text,#666)">← OUI (Organisationally Unique Identifier) → ← NIC-Specific →</div>
      <div class="mac-visual" style="justify-content:center">
        <div class="mac-group">
          <div class="mac-section-label" style="color:#7a5800">OUI — Vendor ID (3 bytes)</div>
          <div style="display:flex;gap:2px">
            <div class="mac-group"><div class="mac-octet">aa</div><div class="mac-label">byte 1</div></div>
            <div class="mac-sep">:</div>
            <div class="mac-group"><div class="mac-octet">bb</div><div class="mac-label">byte 2</div></div>
            <div class="mac-sep">:</div>
            <div class="mac-group"><div class="mac-octet">cc</div><div class="mac-label">byte 3</div></div>
          </div>
        </div>
        <div class="mac-sep" style="font-size:1.5rem;padding:0 8px">—</div>
        <div class="mac-group">
          <div class="mac-section-label" style="color:#0a3a30">Device Identifier (3 bytes)</div>
          <div style="display:flex;gap:2px">
            <div class="mac-group"><div class="mac-octet" style="background:#e0f0ee;border-color:#90c8b8;color:#0a3a30">dd</div><div class="mac-label">byte 4</div></div>
            <div class="mac-sep">:</div>
            <div class="mac-group"><div class="mac-octet" style="background:#e0f0ee;border-color:#90c8b8;color:#0a3a30">ee</div><div class="mac-label">byte 5</div></div>
            <div class="mac-sep">:</div>
            <div class="mac-group"><div class="mac-octet" style="background:#e0f0ee;border-color:#90c8b8;color:#0a3a30">ff</div><div class="mac-label">byte 6</div></div>
          </div>
        </div>
      </div>
    </div>
    <ul>
      <li><strong>OUI (bytes 1–3)</strong> — Assigned by IEEE to each NIC manufacturer. Identifies the vendor. Examples: <code>00:1A:2B</code> = Cisco, <code>24:8A:07</code> = Mellanox/NVIDIA, <code>3C:FD:FE</code> = Intel. You can look up any OUI at <code>https://regauth.standards.ieee.org/</code></li>
      <li><strong>NIC-specific (bytes 4–6)</strong> — Assigned by the manufacturer to uniquely identify the specific interface within all their products</li>
    </ul>
    <h4>Two special bits in byte 1:</h4>
    <ul>
      <li><strong>Bit 0 (LSB) — I/G bit (Individual/Group)</strong>: <code>0</code> = unicast (sent to one device), <code>1</code> = multicast/broadcast (sent to a group)</li>
      <li><strong>Bit 1 — U/L bit (Universal/Local)</strong>: <code>0</code> = globally unique (burned-in OUI), <code>1</code> = locally administered (manually assigned or randomly generated)</li>
    </ul>
<div class="cb"><pre><span class="cm">/* Reading MAC address bits in C (network byte order) */</span>
uint8_t mac[6] = {0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff};
 
<span class="cm">/* Check if unicast or multicast/broadcast */</span>
<span class="ck">if</span> (mac[0] & 0x01)
    printf(<span class="cs">"Multicast or broadcast\n"</span>);
<span class="ck">else</span>
    printf(<span class="cs">"Unicast\n"</span>);
 
<span class="cm">/* Check if globally or locally administered */</span>
<span class="ck">if</span> (mac[0] & 0x02)
    printf(<span class="cs">"Locally administered MAC\n"</span>);
<span class="ck">else</span>
    printf(<span class="cs">"Globally unique (OUI assigned)\n"</span>);
 
<span class="cm">/* Broadcast check: all bytes == 0xFF */</span>
<span class="ck">if</span> (memcmp(mac, "\xff\xff\xff\xff\xff\xff", 6) == 0)
    printf(<span class="cs">"Broadcast frame\n"</span>);</pre></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>Working with MAC Addresses on Linux</h3><span class="tag tag-teal">PRACTICAL</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm"># Show MAC address of all interfaces</span>
ip link show
<span class="cm"># Output: link/ether aa:bb:cc:dd:ee:ff brd ff:ff:ff:ff:ff:ff</span>
<span class="cm"># Show just eth0's MAC</span>
ip link show eth0 | awk '/ether/ {print $2}'
 
<span class="cm"># Show MAC in /sys filesystem (useful in scripts)</span>
cat /sys/class/net/eth0/address
 
<span class="cm"># Temporarily spoof/change MAC address</span>
ip link set eth0 down
ip link set eth0 address 02:00:00:00:00:01
ip link set eth0 up
<span class="cm"># Note: bit 1 of first byte = 1 (locally administered)</span>
<span class="cm"># Show neighbour (ARP) table — maps IP → MAC</span>
ip neigh show
 
<span class="cm"># Show ARP table with arp command (older)</span>
arp -n
 
<span class="cm"># In Wireshark: filter by MAC</span>
<span class="cm"># eth.dst == aa:bb:cc:dd:ee:ff</span>
<span class="cm"># eth.src == aa:bb:cc:dd:ee:ff</span>
<span class="cm"># eth.addr == aa:bb:cc:dd:ee:ff  (src OR dst)</span></pre></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 3 — ARP ════════════ -->
<div id="t3" class="tab-pane">
<p class="sep">ARP — ADDRESS RESOLUTION PROTOCOL</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>The Problem ARP Solves</h3><span class="tag tag-orange">MOTIVATION</span></div>
  <div class="cp-body">
    <p>Layer 3 (IP) routes packets using logical IP addresses. Layer 2 (Ethernet) delivers frames using physical MAC addresses. When your computer wants to send data to another device <em>on the same local network</em>, it knows the destination's <strong>IP address</strong> (from DNS or configuration), but the Ethernet hardware needs a <strong>MAC address</strong> to build the frame. ARP bridges this gap.</p>
    <p><strong>ARP's job in one sentence:</strong> Given an IP address on the local network, tell me the MAC address of the device that owns it.</p>
  </div>
</div>
<div class="analogy">
  <div class="analogy-title">📢 Analogy — Shouting in a Room</div>
  <p>Imagine you're in a room full of people. You know your friend's name ("10.0.0.5") but not their face (MAC address). You shout: <em>"Hey everyone — I'm looking for 10.0.0.5, please tell me who you are!"</em> Only the person with that name raises their hand and says <em>"That's me! My face looks like aa:bb:cc:dd:ee:ff"</em>. Everyone else ignores your shout. You now know their face and can walk up and talk directly. This is exactly how ARP works — the broadcast is the shout, the ARP reply is the hand raised.</p>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📋</span><h3>ARP Packet Format</h3><span class="tag tag-blue">PACKET FORMAT</span></div>
  <div class="cp-body">
    <p>ARP is carried directly in an Ethernet frame with EtherType <code>0x0806</code>. The ARP message itself has a fixed format:</p>
    <div class="frame-diagram">
      <div class="frame-row" style="min-width:500px">
        <div class="frame-label">ARP msg</div>
        <div class="ff ff-typ" style="flex:.8">Hardware Type<div class="ff-bytes">2B (1=Eth)</div></div>
        <div class="ff ff-typ" style="flex:.8">Protocol Type<div class="ff-bytes">2B (0x0800=IPv4)</div></div>
        <div class="ff ff-pre" style="flex:.5">HLen<div class="ff-bytes">1B (6)</div></div>
        <div class="ff ff-pre" style="flex:.5">PLen<div class="ff-bytes">1B (4)</div></div>
        <div class="ff ff-dst" style="flex:.7">Operation<div class="ff-bytes">2B (1=req,2=rep)</div></div>
        <div class="ff ff-src" style="flex:1.1">Sender MAC<div class="ff-bytes">6 bytes</div></div>
        <div class="ff ff-ip" style="flex:.8;background:#e8f5e8;border-color:#a0d0a0;color:#1a4a1a">Sender IP<div class="ff-bytes">4 bytes</div></div>
        <div class="ff ff-dst" style="flex:1.1">Target MAC<div class="ff-bytes">6 bytes (0s in req)</div></div>
        <div class="ff ff-ip" style="flex:.8;background:#e8f5e8;border-color:#a0d0a0;color:#1a4a1a">Target IP<div class="ff-bytes">4 bytes</div></div>
      </div>
    </div>
    <p>The <strong>Operation</strong> field distinguishes requests (1) from replies (2). In a request, the Target MAC is <code>00:00:00:00:00:00</code> (unknown — that's what we're asking for). The entire request is sent as an Ethernet <strong>broadcast</strong> (<code>FF:FF:FF:FF:FF:FF</code>).</p>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>ARP Exchange — Step by Step</h3><span class="tag tag-teal">PROCESS</span></div>
  <div class="cp-body">
    <p>Scenario: Host A (<code>10.0.0.5 / aa:aa:aa:aa:aa:aa</code>) wants to send a packet to Host B (<code>10.0.0.10</code>). It doesn't know B's MAC address yet.</p>
    <div class="flow-list">
      <div class="fl-step" data-n="1" style="--sc:#7a5800">
        <div>
          <div class="fl-title">A checks its ARP cache</div>
          <div class="fl-detail">Before sending an ARP request, the OS checks its in-memory ARP cache (a table of IP→MAC mappings from recent exchanges). If there's a valid entry for 10.0.0.10, skip directly to step 5. ARP cache entries typically expire after 60 seconds (Linux default).</div>
          <div class="fl-code">$ ip neigh show | grep 10.0.0.10</div>
        </div>
      </div>
      <div class="fl-step" data-n="2" style="--sc:#7a5800">
        <div>
          <div class="fl-title">A sends ARP Request — broadcast</div>
          <div class="fl-detail">A constructs an ARP request: Operation=1 (request), Sender MAC=aa:aa:aa:aa:aa:aa, Sender IP=10.0.0.5, Target MAC=00:00:00:00:00:00, Target IP=10.0.0.10. Wraps it in an Ethernet frame with dst MAC=<strong>FF:FF:FF:FF:FF:FF</strong> (broadcast). Every device on the segment receives this frame.</div>
          <div class="fl-code">Ethernet: dst=FF:FF:FF:FF:FF:FF src=aa:aa:aa:aa:aa:aa type=0x0806</div>
        </div>
      </div>
      <div class="fl-step" data-n="3" style="--sc:#7a5800">
        <div>
          <div class="fl-title">All hosts receive the broadcast — only B responds</div>
          <div class="fl-detail">Every device on the segment receives the broadcast frame and reads the ARP message. Each device checks if its IP matches the Target IP (10.0.0.10). Only Host B matches — all others silently discard the ARP request.</div>
        </div>
      </div>
      <div class="fl-step" data-n="4" style="--sc:#7a5800">
        <div>
          <div class="fl-title">B sends ARP Reply — unicast</div>
          <div class="fl-detail">B constructs an ARP reply: Operation=2 (reply), Sender MAC=<strong>bb:bb:bb:bb:bb:bb</strong>, Sender IP=10.0.0.10, Target MAC=aa:aa:aa:aa:aa:aa, Target IP=10.0.0.5. This is sent as a <strong>unicast</strong> Ethernet frame directly to A (not broadcast).</div>
          <div class="fl-code">Ethernet: dst=aa:aa:aa:aa:aa:aa src=bb:bb:bb:bb:bb:bb type=0x0806</div>
        </div>
      </div>
      <div class="fl-step" data-n="5" style="--sc:#7a5800">
        <div>
          <div class="fl-title">A caches the result and sends the original packet</div>
          <div class="fl-detail">A stores <code>10.0.0.10 → bb:bb:bb:bb:bb:bb</code> in its ARP cache. It now builds the IP packet with Ethernet dst=bb:bb:bb:bb:bb:bb and transmits it. All subsequent packets to 10.0.0.10 use the cached entry without another ARP exchange (until it expires).</div>
          <div class="fl-code">Ethernet: dst=bb:bb:bb:bb:bb:bb src=aa:aa:aa:aa:aa:aa type=0x0800 → [IP packet]</div>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>ARP Security Issues — Gratuitous ARP and ARP Spoofing</h3><span class="tag tag-red">SECURITY</span></div>
  <div class="cp-body">
    <p>ARP has <strong>no authentication</strong> — any device can send an ARP reply claiming to own any IP address. This makes it vulnerable to two important attacks that NGFW engineers must understand:</p>
    <h4>Gratuitous ARP</h4>
    <p>A gratuitous ARP is an unsolicited ARP reply — a device announces its own IP→MAC mapping without being asked. This is used legitimately by OSes at startup (to update neighbour caches) and by failover systems (to redirect traffic to a new IP owner after failover). But an attacker can send a gratuitous ARP to <strong>poison</strong> every device's ARP cache on the segment.</p>
    <h4>ARP Spoofing / ARP Poisoning</h4>
    <p>An attacker sends forged ARP replies claiming "I am the gateway (10.0.0.1) — my MAC is aa:at:ta:ck:er:00". Every host that receives this updates its ARP cache. Now all traffic intended for the gateway is sent to the attacker. The attacker can forward it on (man-in-the-middle) or drop it (denial of service).</p>
    <p><strong>NGFW mitigation techniques:</strong></p>
    <ul>
      <li><strong>Dynamic ARP Inspection (DAI)</strong> — switch feature that validates ARP packets against a DHCP snooping binding table</li>
      <li><strong>Static ARP entries</strong> — manually configure critical IP→MAC mappings on sensitive hosts</li>
      <li><strong>ARP rate limiting</strong> — limit the rate of ARP requests per port to detect scanning</li>
      <li><strong>IPSG (IP Source Guard)</strong> — validates that source IP and MAC match the DHCP binding table</li>
    </ul>
  </div>
</div>
</div>
<!-- ════════════ TAB 4 — SWITCHES AND FORWARDING ════════════ -->
<div id="t4" class="tab-pane">
<p class="sep">ETHERNET SWITCHING AND MAC ADDRESS LEARNING</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>How a Switch Works</h3><span class="tag tag-blue">INTERNALS</span></div>
  <div class="cp-body">
    <p>A <strong>switch</strong> is a Layer 2 device that connects multiple Ethernet devices and forwards frames between them intelligently — sending each frame only to the port where the destination MAC address is reachable, rather than flooding to all ports like an old hub.</p>
    <p>Switches maintain a <strong>MAC Address Table</strong> (also called the CAM table — Content-Addressable Memory). This table maps MAC addresses to switch ports. It is built dynamically through <strong>MAC address learning</strong>.</p>
    <h4>MAC Learning — How the Table Gets Built</h4>
    <p>When a switch receives a frame on port X from source MAC <code>aa:bb:cc:dd:ee:ff</code>, it records: <em>"MAC aa:bb:cc:dd:ee:ff is reachable on port X"</em>. It does this for every frame it receives — gradually building a complete map of which MAC address is behind which port.</p>
    <h4>Frame Forwarding Decision</h4>
    <p>When a switch receives a frame, it makes one of three decisions based on the destination MAC:</p>
    <ul>
      <li><strong>Known unicast</strong> — destination MAC is in the MAC table → forward ONLY to the listed port</li>
      <li><strong>Unknown unicast</strong> — destination MAC is NOT in the table → flood to ALL ports except the port it arrived on (this is how new MACs get discovered)</li>
      <li><strong>Broadcast/Multicast</strong> — destination is <code>FF:FF:FF:FF:FF:FF</code> or multicast → flood to ALL ports except the arrival port</li>
    </ul>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📋</span><h3>MAC Address Table — Worked Example</h3><span class="tag tag-teal">EXAMPLE</span></div>
  <div class="cp-body">
    <p>A switch has 4 ports. Three hosts are connected. The table starts empty.</p>
    <div class="topo">
      <div class="topo-row">
        <div>
          <div class="topo-device host">Host A<div class="topo-label">MAC: aa:aa:aa:aa:aa:aa<br>Port 1</div></div>
        </div>
        <div class="topo-link">───</div>
        <div>
          <div class="topo-device switch">Switch<div class="topo-label">4-port</div></div>
        </div>
        <div class="topo-link">───</div>
        <div>
          <div class="topo-device host">Host B<div class="topo-label">MAC: bb:bb:bb:bb:bb:bb<br>Port 2</div></div>
        </div>
      </div>
      <div class="topo-row">
        <div style="margin-top:-8px">
          <div class="topo-device host">Host C<div class="topo-label">MAC: cc:cc:cc:cc:cc:cc<br>Port 3</div></div>
        </div>
        <div class="topo-link">↑ Port 3</div>
      </div>
    </div>
    <p><strong>Step 1:</strong> Host A sends a frame to Host B. Switch receives frame on <strong>port 1</strong>:</p>
    <table class="t-table" style="margin-bottom:.5rem">
      <thead><tr><th>MAC Address</th><th>Port</th><th>Age</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td><code>aa:aa:aa:aa:aa:aa</code></td><td>1</td><td>0s</td><td>Learned from frame source</td></tr>
      </tbody>
    </table>
    <p>Destination <code>bb:bb:bb:bb:bb:bb</code> is unknown → <strong>flood to ports 2 and 3</strong>. Host B receives it (port 2). Host C receives it but discards (not its MAC).</p>
    <p><strong>Step 2:</strong> Host B replies to Host A. Switch receives on <strong>port 2</strong>:</p>
    <table class="t-table" style="margin-bottom:.5rem">
      <thead><tr><th>MAC Address</th><th>Port</th><th>Age</th></tr></thead>
      <tbody>
        <tr><td><code>aa:aa:aa:aa:aa:aa</code></td><td>1</td><td>5s</td></tr>
        <tr><td><code>bb:bb:bb:bb:bb:bb</code></td><td>2</td><td>0s</td></tr>
      </tbody>
    </table>
    <p>Destination <code>aa:aa:aa:aa:aa:aa</code> is NOW known → forward <strong>only to port 1</strong>. Host C receives nothing.</p>
    <p><strong>After a few more exchanges</strong> — full table, all forwarding is unicast:</p>
    <table class="t-table">
      <thead><tr><th>MAC Address</th><th>Port</th><th>Notes</th></tr></thead>
      <tbody>
        <tr><td><code>aa:aa:aa:aa:aa:aa</code></td><td>1</td><td>Host A — all frames for A go to port 1 only</td></tr>
        <tr><td><code>bb:bb:bb:bb:bb:bb</code></td><td>2</td><td>Host B — all frames for B go to port 2 only</td></tr>
        <tr><td><code>cc:cc:cc:cc:cc:cc</code></td><td>3</td><td>Host C — all frames for C go to port 3 only</td></tr>
      </tbody>
    </table>
    <p>Entries age out (typically 300 seconds) to handle moved devices. If a device is physically moved to a different port, the switch learns the new port when it next sends a frame, overwriting the old entry.</p>
  </div>
</div>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Hub vs Switch vs Router — Key Differences</h3><span class="tag tag-purple">COMPARISON</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Device</th><th>OSI Layer</th><th>Forwarding Logic</th><th>Collision Domain</th><th>Broadcast Domain</th></tr></thead>
      <tbody>
        <tr><td><strong>Hub</strong></td><td>L1</td><td>Repeats all bits to all ports — no intelligence</td><td>All ports share one</td><td>All ports share one</td></tr>
        <tr><td><strong>Switch</strong></td><td>L2</td><td>Forwards frames by MAC address — per-port</td><td>One per port (full-duplex)</td><td>All ports share one (unless VLANs used)</td></tr>
        <tr><td><strong>Router</strong></td><td>L3</td><td>Routes packets by IP address between networks</td><td>One per port</td><td>One per port — breaks broadcast domains</td></tr>
      </tbody>
    </table>
    <div class="note"><p>💡 <strong>Broadcast domain matters for performance.</strong> Every ARP request, every DHCP broadcast, every Spanning Tree BPDU floods the entire broadcast domain. A single broadcast domain with 1000 hosts means every host must process every broadcast from all 999 others. VLANs split the broadcast domain — critical for large networks. This is exactly why VLANs exist.</p></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 5 — VLANs ════════════ -->
<div id="t5" class="tab-pane">
<p class="sep">VLANs — VIRTUAL LOCAL AREA NETWORKS (IEEE 802.1Q)</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🧱</span><h3>What Problem VLANs Solve</h3><span class="tag tag-purple">MOTIVATION</span></div>
  <div class="cp-body">
    <p>A VLAN (Virtual LAN) allows you to <strong>logically divide a single physical switch into multiple isolated broadcast domains</strong>. Without VLANs, all ports on a switch share one broadcast domain — every ARP, DHCP, and broadcast packet hits every port. With VLANs, each VLAN is its own isolated segment; broadcasts in VLAN 10 never reach VLAN 20.</p>
    <p><strong>Key benefits:</strong></p>
    <ul>
      <li><strong>Security isolation</strong> — HR hosts in VLAN 10 cannot communicate at L2 with Engineering in VLAN 20 (even on the same physical switch)</li>
      <li><strong>Broadcast control</strong> — reduces broadcast noise and scales large networks</li>
      <li><strong>Simplified management</strong> — move a host between VLANs by reconfiguring the switch port, not physically moving cables</li>
      <li><strong>Traffic segmentation</strong> — critical for NGFW deployments (separate VLAN per security zone: inside, DMZ, outside)</li>
    </ul>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏷️</span><h3>802.1Q VLAN Tagging</h3><span class="tag tag-blue">FRAME FORMAT</span></div>
  <div class="cp-body">
    <p>IEEE 802.1Q adds a <strong>4-byte VLAN tag</strong> to the Ethernet frame between the Source MAC and the EtherType field. The EtherType <code>0x8100</code> signals that a VLAN tag follows:</p>
    <div class="frame-diagram">
      <div class="frame-row" style="min-width:560px">
        <div class="frame-label">Tagged frame</div>
        <div class="ff ff-dst" style="flex:1.2">Dst MAC<div class="ff-bytes">6 bytes</div></div>
        <div class="ff ff-src" style="flex:1.2">Src MAC<div class="ff-bytes">6 bytes</div></div>
        <div class="ff ff-vlan" style="flex:.6">0x8100<div class="ff-bytes">2B (TPID)</div></div>
        <div class="ff ff-vlan" style="flex:.6">PCP DEI<div class="ff-bytes">3+1 bits</div></div>
        <div class="ff ff-vlan" style="flex:.8">VLAN ID<div class="ff-bytes">12 bits (0–4095)</div></div>
        <div class="ff ff-typ" style="flex:.7">EtherType<div class="ff-bytes">2B (0x0800)</div></div>
        <div class="ff ff-dat" style="flex:3">Payload<div class="ff-bytes">46–1500 bytes</div></div>
        <div class="ff ff-crc" style="flex:.5">CRC<div class="ff-bytes">4 bytes</div></div>
      </div>
    </div>
    <p><strong>VLAN tag fields:</strong></p>
    <ul>
      <li><strong>TPID</strong> (Tag Protocol Identifier, <code>0x8100</code>) — identifies this as an 802.1Q tagged frame</li>
      <li><strong>PCP</strong> (Priority Code Point, 3 bits) — 802.1p QoS priority 0–7 (7=highest). Used by switches to prioritise traffic</li>
      <li><strong>DEI</strong> (Drop Eligible Indicator, 1 bit) — marks frames that can be dropped under congestion</li>
      <li><strong>VID</strong> (VLAN Identifier, 12 bits) — VLAN number 0–4095. VLAN 0 = untagged/no VLAN, VLAN 1 = default, VLAN 4095 = reserved. Usable range: 1–4094</li>
    </ul>
    <p>The VLAN tag increases the maximum frame size from 1518 to <strong>1522 bytes</strong>.</p>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔌</span><h3>Access Ports vs Trunk Ports</h3><span class="tag tag-teal">PORT TYPES</span></div>
  <div class="cp-body">
    <div class="two-col">
      <div>
        <h4>Access Port</h4>
        <p>Connects an end device (server, PC) to the switch. The device sends <strong>untagged</strong> frames — it doesn't know or care about VLANs. The switch <strong>adds a VLAN tag</strong> when the frame enters (based on port configuration) and <strong>strips it</strong> before sending back to the device. The device never sees the VLAN tag.</p>
        <p><strong>Used for:</strong> Server NICs, workstation Ethernet ports, printer ports, access-layer switch ports</p>
      </div>
      <div>
        <h4>Trunk Port</h4>
        <p>Connects a switch to another switch (or a router, or a NIC configured for trunking). Carries frames for <strong>multiple VLANs simultaneously</strong>, each identified by its 802.1Q tag. Both sides see and process the tags. A trunk port is commonly used for:</p>
        <p><strong>Used for:</strong> Switch-to-switch uplinks, switch-to-router links, server NICs where the OS needs multiple VLANs, VPP/DPDK setups with VLAN subinterfaces</p>
      </div>
    </div>
    <div class="vlan-wrap" style="margin-top:1rem">
      <div class="vlan-box" style="border-color:#5b3a8c">
        <div class="vlan-title" style="color:#5b3a8c">VLAN 10 — Engineering</div>
        <div class="vlan-member" style="background:#ede8f5;color:#3a1a6c">Port 1 (access) — Server 1</div>
        <div class="vlan-member" style="background:#ede8f5;color:#3a1a6c">Port 2 (access) — Server 2</div>
        <div class="vlan-member" style="background:#ede8f5;color:#3a1a6c">Port 8 (trunk)  — carries VLAN10+20+30</div>
      </div>
      <div class="vlan-box" style="border-color:#0f6e56">
        <div class="vlan-title" style="color:#0f6e56">VLAN 20 — HR</div>
        <div class="vlan-member" style="background:#e0f0ee;color:#0a3a30">Port 3 (access) — HR PC 1</div>
        <div class="vlan-member" style="background:#e0f0ee;color:#0a3a30">Port 4 (access) — HR PC 2</div>
        <div class="vlan-member" style="background:#e0f0ee;color:#0a3a30">Port 8 (trunk)  — carries VLAN10+20+30</div>
      </div>
    </div>
    <p style="font-size:.83rem;color:var(--text-color,#444);margin-top:.5rem">Hosts in VLAN 10 and VLAN 20 cannot communicate at L2 even though they're on the same physical switch. To route between VLANs you need a router or Layer 3 switch ("router on a stick").</p>
  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🖥️</span><h3>VLANs in Linux and DPDK</h3><span class="tag tag-green">PRACTICAL</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm"># Create VLAN subinterface on Linux (eth0 = trunk port)</span>
ip link add link eth0 name eth0.10 type vlan id 10
ip link add link eth0 name eth0.20 type vlan id 20
ip link set eth0.10 up
ip link set eth0.20 up
ip addr add 10.10.0.1/24 dev eth0.10
ip addr add 10.20.0.1/24 dev eth0.20
 
<span class="cm"># Show VLAN info</span>
cat /proc/net/vlan/config
ip -d link show eth0.10   <span class="cm"># shows vlan id, proto 802.1Q</span>
<span class="cm"># In VPP — create VLAN subinterface on a DPDK port</span>
<span class="cm"># vppctl: create sub-interfaces GigabitEthernet0/8/0 10</span>
<span class="cm"># vppctl: set interface state GigabitEthernet0/8/0.10 up</span>
<span class="cm"># vppctl: set interface ip address GigabitEthernet0/8/0.10 10.10.0.1/24</span>
<span class="cm"># Wireshark VLAN filter</span>
<span class="cm"># vlan.id == 10         — show only VLAN 10 frames</span>
<span class="cm"># vlan.priority == 6    — show high-priority tagged frames</span></pre></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 6 — STP AND RSTP ════════════ -->
<div id="t6" class="tab-pane">
<p class="sep">SPANNING TREE PROTOCOL (STP) AND RSTP — LOOP PREVENTION</p>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>The Broadcast Storm Problem</h3><span class="tag tag-red">THE PROBLEM</span></div>
  <div class="cp-body">
    <p>Networks need redundant links for fault tolerance — if one cable fails, traffic should route around it automatically. But redundant L2 links create <strong>loops</strong>, and loops in a switched network are catastrophic:</p>
    <ul>
      <li>A broadcast frame (e.g., ARP request) sent into the loop <strong>never dies</strong> — switches forward it in circles forever (unlike IP packets which have TTL)</li>
      <li>The loop <strong>multiplies the frame</strong> — it arrives on multiple ports simultaneously, triggering additional floods</li>
      <li>Within milliseconds, the network saturates at 100% utilisation — nothing else can pass</li>
      <li>Switch MAC tables <strong>thrash</strong> constantly — the same MAC appears on different ports simultaneously, causing incorrect forwarding</li>
    </ul>
    <p>This is called a <strong>broadcast storm</strong>. It will take down an entire network in seconds. STP prevents this by blocking redundant links unless a primary link fails.</p>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🌲</span><h3>STP — How It Works</h3><span class="tag tag-blue">MECHANISM</span></div>
  <div class="cp-body">
    <p>STP (IEEE 802.1D) prevents loops by automatically blocking redundant ports while keeping one active path between any two network points — a <strong>loop-free logical tree topology</strong>. STP runs between switches automatically using special messages called <strong>BPDUs (Bridge Protocol Data Units)</strong>.</p>
    <h4>STP Election Process — 3 Steps</h4>
    <ol>
      <li><strong>Elect a Root Bridge</strong> — All switches exchange BPDUs and elect one switch as the "root" of the spanning tree. The switch with the <strong>lowest Bridge ID</strong> wins. Bridge ID = Priority (default 32768) + MAC address. You can manually set priority lower to control which switch becomes root.</li>
      <li><strong>Elect Root Ports</strong> — Each non-root switch selects one <strong>root port</strong>: the port with the lowest-cost path to the root bridge. Cost is based on link speed (higher speed = lower cost: 10 Gbps = cost 2, 1 Gbps = cost 4, 100 Mbps = cost 19).</li>
      <li><strong>Elect Designated Ports and Block Others</strong> — For each network segment, one switch port is elected as the <strong>designated port</strong> (the one closest to root). All other ports on that segment are put into <strong>blocking state</strong> — they receive but do not forward frames. This breaks all loops.</li>
    </ol>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>STP Port States</h3><span class="tag tag-teal">PORT STATES</span></div>
  <div class="cp-body">
    <div class="stp-states">
      <div class="stp-state" style="border-color:#e8b0b0;background:#faeaea">
        <div class="stp-state-name" style="color:#6c1a1a">Blocking</div>
        <div class="stp-state-desc">Receives BPDUs. Does NOT forward frames. Does NOT learn MACs. Prevents loops. Duration: indefinite while loop exists.</div>
      </div>
      <div class="stp-state" style="border-color:#e8c870;background:#fdf4dc">
        <div class="stp-state-name" style="color:#5a3800">Listening</div>
        <div class="stp-state-desc">Transitioning to forwarding. Processes BPDUs. Does NOT forward frames. Does NOT learn MACs. Duration: 15 seconds (Forward Delay).</div>
      </div>
      <div class="stp-state" style="border-color:#b0d0e8;background:#e8f1f9">
        <div class="stp-state-name" style="color:#1a3a5c">Learning</div>
        <div class="stp-state-desc">Processes BPDUs. Does NOT forward frames. DOES learn MAC addresses (builds table without forwarding). Duration: 15 seconds (Forward Delay).</div>
      </div>
      <div class="stp-state" style="border-color:#a0d0a0;background:#e8f5e8">
        <div class="stp-state-name" style="color:#1a4a1a">Forwarding</div>
        <div class="stp-state-desc">Fully active. Processes BPDUs. Forwards frames. Learns MACs. This is the normal operational state for active ports.</div>
      </div>
      <div class="stp-state" style="border-color:#c0a8e8;background:#ede8f5">
        <div class="stp-state-name" style="color:#3a1a6c">Disabled</div>
        <div class="stp-state-desc">Administratively shut down. Does nothing. No BPDUs, no learning, no forwarding.</div>
      </div>
    </div>
    <div class="warn">
      <p>⚠️ <strong>STP convergence takes up to 50 seconds.</strong> When a link fails, STP must detect it (20s Max Age) and transition blocked ports through Listening (15s) and Learning (15s) states before forwarding. This 50-second outage is unacceptable for modern networks — which is why RSTP was invented.</p>
    </div>
  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>RSTP — Rapid Spanning Tree Protocol (IEEE 802.1w)</h3><span class="tag tag-green">RSTP</span></div>
  <div class="cp-body">
    <p>RSTP (802.1w, later incorporated into 802.1D-2004) reduces convergence time from 50 seconds to <strong>under 1 second</strong> in most cases. Key improvements:</p>
    <ul>
      <li><strong>Proposal/Agreement mechanism</strong> — switches negotiate directly with neighbours to synchronise port roles quickly without waiting for timers</li>
      <li><strong>Edge ports (PortFast)</strong> — ports connected to end devices bypass Listening/Learning states entirely and go straight to Forwarding. Reduces startup delay for servers and workstations</li>
      <li><strong>Simplified port roles</strong> — Root, Designated, Alternate (backup for root port), Backup (backup for designated)</li>
      <li><strong>Backward compatible</strong> — RSTP falls back to STP mode when it detects an old STP switch</li>
    </ul>
    <p><strong>BPDU Guard</strong> — a security feature on edge ports: if a BPDU is received on an edge port (someone plugged in a switch), the port is immediately shut down. Essential for NGFW deployments to prevent unauthorised switch insertion.</p>
  </div>
</div>
</div>
<!-- ════════════ TAB 7 — LABS ════════════ -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Dissect an Ethernet Frame with Wireshark</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Capture real Ethernet frames and identify every field — preamble (simulated), dst/src MAC, EtherType, payload, CRC. Also observe a VLAN-tagged frame if your environment supports it.</p>
    <div class="lab-step"><div class="sn">1</div><div>Open Wireshark. Start a capture on your active interface. In another terminal: <code>ping -c 5 8.8.8.8</code>. Stop the capture.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Filter for ARP traffic: type <code>arp</code> in the filter bar. Find an ARP request. Expand the "Ethernet II" section in the packet detail pane. Record: Destination MAC, Source MAC, EtherType value.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Now filter for <code>icmp</code>. Find a ping packet. Expand Ethernet II again — note EtherType is 0x0800 (IPv4). Then expand the IPv4 section, then ICMP. This shows the full encapsulation: Ethernet → IP → ICMP.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>In the hex dump at the bottom of Wireshark, click on different bytes of the Ethernet header. Wireshark highlights the corresponding field. Identify the exact byte offsets of: dst MAC (bytes 0–5), src MAC (bytes 6–11), EtherType (bytes 12–13).</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Bonus — Read MAC OUI:</strong> Right-click a captured frame, select "Protocol Preferences > Name Resolution > Resolve MAC Addresses". Wireshark will show the vendor name next to each MAC address (e.g., "Intel_xx:xx:xx" or "Mellanox_xx:xx:xx").</div></div>
    <div class="lab-step"><div class="sn">6</div><div><strong>Bonus — VLAN tag:</strong> If you have a trunk interface configured, run <code>tcpdump -i eth0 -e -nn vlan</code>. The <code>-e</code> flag shows L2 headers including VLAN tags. You should see output like: <code>vlan 10, ethertype IPv4</code>.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Observe the ARP Exchange</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Capture and decode a complete ARP request/reply exchange. Understand every field in each message.</p>
    <div class="lab-step"><div class="sn">1</div><div>First, flush your ARP cache to force a fresh exchange: <code>sudo ip neigh flush all</code>. This removes all cached IP→MAC mappings.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Start a Wireshark capture filtered to ARP: <code>arp</code> in the filter bar. Then in a terminal: <code>ping -c 1 10.0.0.1</code> (use your actual default gateway IP — find it with <code>ip route | grep default</code>).</div></div>
    <div class="lab-step"><div class="sn">3</div><div>You should see two ARP packets: the request (broadcast) and the reply (unicast). For the <strong>request</strong>, record: Sender MAC, Sender IP, Target MAC (should be all zeros), Target IP. For the <strong>reply</strong>, record: Sender MAC (this is your gateway's MAC!), Sender IP, Target MAC, Target IP.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Verify your ARP cache was populated: <code>ip neigh show</code>. You should see your gateway IP with its MAC address and state "REACHABLE".</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Bonus — ARP spoofing demonstration (on your own VM only):</strong> Use Scapy to send a gratuitous ARP: <code>from scapy.all import *; sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=2, pdst="10.0.0.1", hwdst="ff:ff:ff:ff:ff:ff", psrc="10.0.0.1", hwsrc="de:ad:be:ef:00:01"), iface="eth0", count=3)</code>. Check <code>ip neigh show</code> on another VM — the gateway's MAC has been poisoned to de:ad:be:ef:00:01.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Build an Ethernet Frame from Scratch in C</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Use a raw socket in C to construct and transmit an Ethernet frame manually — no IP or TCP involved. This gives you a deep understanding of frame structure and prepares you for DPDK raw packet work.</p>
    <div class="lab-step"><div class="sn">1</div><div>Create a file <code>send_arp.c</code>. You will manually build an ARP request using a raw socket (<code>AF_PACKET, SOCK_RAW</code>) and send it on your loopback or virtual interface.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>The program structure: open a raw socket → get interface index → build the Ethernet header (dst=broadcast, src=your MAC, type=0x0806) → build the ARP payload (op=1, sender MAC/IP, target IP) → call sendto(). Compile with: <code>gcc -o send_arp send_arp.c && sudo ./send_arp eth0 10.0.0.1</code>.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Capture the result: run <code>sudo tcpdump -i eth0 -e arp</code> in a parallel terminal before running your program. Verify that your handcrafted ARP request appears in the capture with the exact fields you set in code.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Extend it: modify your program to read the ARP reply from the socket. When a reply arrives, parse the Ethernet header (bytes 0–13), then the ARP payload (bytes 14–41) and print the answering device's MAC address. You've just built a minimal ARP resolver in C.</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Starter code skeleton:</strong>
<div class="cb"><pre><span class="cs">#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;linux/if_packet.h&gt;
#include &lt;net/ethernet.h&gt;
#include &lt;net/if.h&gt;
#include &lt;arpa/inet.h&gt;</span>
<span class="ck">struct</span> arp_frame {
    <span class="cm">/* Ethernet header */</span>
    uint8_t  eth_dst[6];   <span class="cm">/* 6 bytes */</span>
    uint8_t  eth_src[6];   <span class="cm">/* 6 bytes */</span>
    uint16_t eth_type;     <span class="cm">/* 0x0806 for ARP */</span>
    <span class="cm">/* ARP payload */</span>
    uint16_t hw_type;      <span class="cm">/* 0x0001 = Ethernet */</span>
    uint16_t proto_type;   <span class="cm">/* 0x0800 = IPv4 */</span>
    uint8_t  hw_len;       <span class="cm">/* 6 */</span>
    uint8_t  proto_len;    <span class="cm">/* 4 */</span>
    uint16_t operation;    <span class="cm">/* 1 = request */</span>
    uint8_t  sender_mac[6];
    uint8_t  sender_ip[4];
    uint8_t  target_mac[6];
    uint8_t  target_ip[4];
} __attribute__((packed));
 
<span class="ck">int</span> main(<span class="ck">int</span> argc, <span class="ck">char</span> *argv[]) {
    <span class="ck">int</span> sock = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
    <span class="cm">/* TODO: fill frame, sendto(), receive reply */</span>
    <span class="ck">return</span> 0;
}</pre></div>
    </div></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 8 — CHECKLIST ════════════ -->
<div id="t8" class="tab-pane">
<p class="sep">M02 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain why Ethernet has dominated networking for 50+ years — simplicity, cost, scalability</li>
  <li>Know the role of Layer 2 in the stack: node-to-node delivery on the same network segment</li>
  <li>Can draw an Ethernet II frame from memory with all field names and sizes: Preamble(7), SFD(1), Dst MAC(6), Src MAC(6), EtherType(2), Payload(46-1500), FCS(4)</li>
  <li>Know the key EtherType values: 0x0800 (IPv4), 0x0806 (ARP), 0x86DD (IPv6), 0x8100 (802.1Q VLAN)</li>
  <li>Know what the minimum 64-byte frame size is for and why smaller frames get padded</li>
  <li>Understand Ethernet overhead and why jumbo frames improve efficiency for large transfers</li>
  <li>Know MAC address structure: 6 bytes, OUI (first 3) + NIC-specific (last 3), colon-separated hex notation</li>
  <li>Know the I/G bit (bit 0 of byte 1): 0=unicast, 1=multicast/broadcast</li>
  <li>Know the three special MAC address types: unicast, broadcast (FF:FF:FF:FF:FF:FF), multicast (01:00:5E:...)</li>
  <li>Can explain the ARP process step-by-step: cache check → broadcast request → unicast reply → cache entry</li>
  <li>Know what a gratuitous ARP is and how it enables ARP spoofing attacks</li>
  <li>Understand how a switch builds its MAC address table through source MAC learning</li>
  <li>Know the three forwarding decisions: known unicast → forward to port, unknown unicast → flood, broadcast → flood</li>
  <li>Understand 802.1Q VLAN tag structure: TPID(0x8100), PCP(3 bits), DEI(1 bit), VID(12 bits)</li>
  <li>Know the difference between access ports (untagged, for end devices) and trunk ports (tagged, multi-VLAN)</li>
  <li>Understand why STP exists: prevents broadcast storms from L2 loops in redundant topologies</li>
  <li>Know the 5 STP port states: Blocking, Listening, Learning, Forwarding, Disabled</li>
  <li>Know why RSTP (802.1w) replaced STP: convergence in &lt;1s vs 50s for STP</li>
  <li>Completed Lab 1: identified all Ethernet frame fields in Wireshark including EtherType values</li>
  <li>Completed Lab 2: captured a complete ARP request/reply exchange and decoded all fields</li>
  <li>Completed Lab 3: built and sent a raw Ethernet ARP frame in C using AF_PACKET socket</li>
</ul>
<div class="note" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M03 - IPv4 Deep Dive</strong>. You've now seen the Ethernet frame wrapper — M03 goes inside the payload and dissects the IP header byte-by-byte: addressing, subnetting, fragmentation, TTL, ICMP, and how routers make forwarding decisions.</p>
</div>
</div>
<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/networking-mastery/m01-osi-tcpip/">← M01 OSI and TCP/IP</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m03-ipv4/">Next: M03 - IPv4 →</a>
</div>
<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
</script>
