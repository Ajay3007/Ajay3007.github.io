---
title: "M03 - IPv4 Deep Dive"
description: "NETWORKING MASTERY · PHASE 1 · MODULE 03 · WEEK 2 🌐 IPv4 Deep Dive IP addressing · Subnetting · CIDR · Header fields · Fragmentation · TTL · ICMP · Routing basics Beginner →…"
domain: networking
track: networking-mastery
order: 3
ownHeader: true
url: /learning/networking-mastery/m03-ipv4/
---

<style>
/* ── Base ───────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 35%,#1a5a1a 75%,#1e6b3c 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0;
}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#90e890;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#c0f0c0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#d8f8d8}

/* Tabs */
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#5dd890;border-bottom-color:#5dd890}
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

.tag-blue  {background:#d0e8f8;color:#1a4a7c}
.tag-teal  {background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}
.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green {background:#c8e8d4;color:#0e4a28}
.tag-red   {background:#f4d0d0;color:#6c1a1a}
.tag-amber {background:#fae8a0;color:#5a3800}

/* Code blocks */
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1e6b3c}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#c8f0c8;white-space:pre}
.cm{color:#4a7a4a}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}

/* Insight / warning / note */
.ins{background:#eaf5ea;border:1.5px solid #1e6b3c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0a2018;border-color:#2a8a4a}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#1a5a1a}
[data-theme=dark] .ins strong{color:#5dd890}

.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}

.note{background:#e8f1f9;border:1.5px solid #1a3a5c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .note{background:#0d2030;border-color:#2a5a8c}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.note strong{color:#1a3a5c}
[data-theme=dark] .note strong{color:#7ab8d8}

/* Analogy box */
.analogy{background:linear-gradient(135deg,#f0fff0,#e8f8e8);border:1.5px solid #90c890;border-radius:10px;padding:1.1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .analogy{background:linear-gradient(135deg,#0a1a0a,#0a2010);border-color:#306830}
.analogy-title{font-size:.72rem;font-family:monospace;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#1a5a1a;margin-bottom:.5rem}
[data-theme=dark] .analogy-title{color:#5dd890}
.analogy p{font-size:.88rem;line-height:1.7;color:var(--text-color,#222);margin:0}

/* IPv4 header diagram */
.hdr-diagram{margin:1rem 0;overflow-x:auto}
.hdr-row{display:flex;gap:2px;min-width:640px;margin-bottom:3px;align-items:stretch}
.hdr-label{font-size:.7rem;font-family:monospace;min-width:76px;display:flex;align-items:center;color:var(--light-text,#666);flex-shrink:0;padding-right:4px}
.hf{
  border-radius:5px;padding:7px 5px;font-size:.7rem;
  font-weight:600;text-align:center;border:1.5px solid transparent;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  line-height:1.3;cursor:default;
}
.hf-ver {background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c}
.hf-ihl {background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c}
.hf-dscp{background:#fdf4dc;border-color:#e8c870;color:#5a3800}
.hf-tot {background:#e0f0ee;border-color:#90c8b8;color:#0a3a30}
.hf-id  {background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c}
.hf-flg {background:#faeaea;border-color:#e8b0b0;color:#6c1a1a}
.hf-off {background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c}
.hf-ttl {background:#faeee4;border-color:#e8b090;color:#6a2800}
.hf-pro {background:#e2f0e8;border-color:#a0d0a0;color:#1a4a1a}
.hf-chk {background:#faeaea;border-color:#e8b0b0;color:#6c1a1a}
.hf-src {background:#e8f5e8;border-color:#90d890;color:#1a5a1a}
.hf-dst {background:#e8f5e8;border-color:#90d890;color:#1a5a1a}
.hf-opt {background:#f0f0f0;border-color:#c0c0c0;color:#555}
.hf-bytes{font-size:.62rem;font-weight:400;opacity:.8;margin-top:2px}
[data-theme=dark] .hf-ver,.hf-ihl{background:#0d2030;border-color:#4080b0;color:#a0c8e8}
[data-theme=dark] .hf-src,[data-theme=dark] .hf-dst{background:#0c2010;border-color:#3a8040;color:#80d890}
[data-theme=dark] .hf-ttl{background:#1e1000;border-color:#b06030;color:#f0b070}
[data-theme=dark] .hf-pro{background:#0a2018;border-color:#3a8040;color:#80d890}

/* Bit fields */
.bit-row{display:flex;align-items:center;gap:6px;margin:.6rem 0;flex-wrap:wrap}
.bit-group{display:flex;flex-direction:column;align-items:center;gap:2px}
.bit-box{
  width:28px;height:28px;border-radius:4px;border:1.5px solid;
  display:flex;align-items:center;justify-content:center;
  font-size:.78rem;font-weight:700;font-family:monospace;
}
.bit-label{font-size:.62rem;font-family:monospace;color:var(--light-text,#666);text-align:center;max-width:30px;line-height:1.2}

/* IP address breakdown */
.ip-breakdown{display:flex;gap:2px;align-items:stretch;margin:.8rem 0;flex-wrap:wrap}
.ip-octet{
  border-radius:7px;padding:8px 10px;text-align:center;
  font-family:monospace;font-size:1.1rem;font-weight:800;
  border:1.5px solid;min-width:52px;
}
.ip-sep{display:flex;align-items:center;font-size:1.4rem;color:var(--light-text,#aaa);padding:0 1px}
.ip-octet-lbl{font-size:.68rem;font-family:monospace;color:var(--light-text,#666);margin-top:3px;text-align:center}
.ip-col{display:flex;flex-direction:column;align-items:center}

/* Subnet tables */
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#1a5a1a;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a5a1a}

/* CIDR visual */
.cidr-vis{display:flex;gap:2px;margin:.8rem 0;align-items:stretch;overflow-x:auto}
.cidr-net{background:#e8f5e8;border:1.5px solid #90d890;border-radius:5px;padding:6px 8px;font-size:.72rem;font-family:monospace;font-weight:700;color:#1a5a1a;text-align:center}
.cidr-host{background:#e8f1f9;border:1.5px solid #b0ccec;border-radius:5px;padding:6px 8px;font-size:.72rem;font-family:monospace;font-weight:700;color:#1a3a5c;text-align:center}
.cidr-sep{display:flex;align-items:center;font-family:monospace;color:var(--light-text,#aaa);padding:0 2px;font-size:.9rem}

/* Fragmentation visual */
.frag-vis{margin:.8rem 0}
.frag-original{display:flex;height:36px;border-radius:7px;overflow:hidden;margin-bottom:4px;border:1.5px solid #1e6b3c}
.frag-chunk{display:flex;align-items:center;justify-content:center;font-size:.72rem;font-family:monospace;font-weight:600}
.frag-arrow{text-align:center;font-size:1rem;color:var(--light-text,#888);margin:4px 0}
.frag-fragments{display:flex;gap:6px;flex-wrap:wrap}
.frag-fragment{border-radius:7px;overflow:hidden;border:1.5px solid #1a5a1a;flex:1;min-width:140px}
.frag-fragment-row{display:flex;height:30px}

/* ICMP table */
.icmp-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.icmp-table th{background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.icmp-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.icmp-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.icmp-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a3a5c}

/* Flow steps */
.flow-list{display:flex;flex-direction:column;gap:0;margin:1rem 0}
.fl-step{display:flex;gap:14px;padding:10px 14px;border-left:2px solid var(--border-color,#e0e0e0);margin-left:14px;position:relative}
.fl-step::before{content:attr(data-n);position:absolute;left:-14px;top:12px;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;color:#fff;background:var(--sc,#1a5a1a)}
.fl-step:last-child{border-left-color:transparent}
.fl-title{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin-bottom:.25rem}
.fl-detail{font-size:.85rem;color:var(--text-color,#444);line-height:1.6}
.fl-code{font-family:monospace;font-size:.78rem;display:inline-block;background:#0a1628;color:#5dd890;padding:2px 8px;border-radius:4px;margin-top:.3rem}

/* Two-col */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}

/* Lab box */
.lab-box{border:2px solid #1e6b3c;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#1e6b3c;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#1e6b3c;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}

/* Checklist */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#1e6b3c;margin-top:-.05rem}

/* Nav */
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}

.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>
<!-- ── HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 1 · MODULE 03 · WEEK 2</div>
  <div class="mod-title">🌐 IPv4 Deep Dive</div>
  <div class="mod-subtitle">IP addressing · Subnetting · CIDR · Header fields · Fragmentation · TTL · ICMP · Routing basics</div>
  <div class="mod-pills">
<span class="mod-pill">Beginner → Intermediate</span>
<span class="mod-pill">Prerequisite: M01, M02</span>
<span class="mod-pill">RFC 791</span>
<span class="mod-pill">Subnetting</span>
<span class="mod-pill">ICMP</span>
<span class="mod-pill">3 Labs</span>
  </div>
</div>
<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">What is IP?</button>
  <button class="tab-btn" onclick="vt(event,'t1')">IPv4 Header</button>
  <button class="tab-btn" onclick="vt(event,'t2')">IP Addressing</button>
  <button class="tab-btn" onclick="vt(event,'t3')">Subnetting and CIDR</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Special Addresses</button>
  <button class="tab-btn" onclick="vt(event,'t5')">TTL and Routing</button>
  <button class="tab-btn" onclick="vt(event,'t6')">Fragmentation</button>
  <button class="tab-btn" onclick="vt(event,'t7')">ICMP</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Checklist</button>
</div>
<!-- ════════════ TAB 0 — WHAT IS IP ════════════ -->
<div id="t0" class="tab-pane active">
<p class="sep">THE INTERNET PROTOCOL — WHY IT EXISTS</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🌐</span><h3>IP — The Language of the Internet</h3><span class="tag tag-green">FOUNDATION</span></div>
  <div class="cp-body">
<p>The Internet Protocol (IP) is the fundamental protocol that makes the internet work. Defined in <a href="https://datatracker.ietf.org/doc/html/rfc791" target="_blank" rel="noopener">RFC 791</a> (1981), it gives every device a <strong>logical address</strong> and defines how data is packaged into <strong>packets</strong> and routed across interconnected networks.</p>
<p>Without IP, you could only talk to devices on your <em>same physical network</em> — your switch's MAC table handles that. IP is what lets your laptop in Mumbai send data to a server in Frankfurt through dozens of intermediate networks and routers, none of which need to know anything about your laptop or the server directly.</p>
<p><strong>IP's three core jobs:</strong></p>
<ul>
<li><strong>Logical addressing</strong> — Every device gets an IP address. Unlike MAC addresses (hardware), IP addresses are logical and can be assigned, changed, and hierarchically organised for efficient routing</li>
<li><strong>Packet fragmentation and reassembly</strong> — If a packet is too large for a network link, IP splits it into smaller fragments and reassembles at the destination</li>
<li><strong>Best-effort delivery</strong> — IP makes its best effort to deliver packets but makes <strong>no guarantees</strong>. Packets can be lost, duplicated, reordered, or corrupted. Reliability is left to upper layers (TCP at L4)</li>
</ul>
  </div>
</div>
<div class="analogy">
  <div class="analogy-title">📮 Analogy — The Postal System</div>
  <p>IP is like the postal service. Your letter (packet) has a destination address (IP address). The postal system (internet) routes it through intermediate sorting offices (routers) without you needing to know the route. Each sorting office reads the destination address, decides which direction to send it, and passes it along. If the letter is too thick for a slot (MTU exceeded), it gets split into multiple envelopes (fragmentation). The postal service doesn't guarantee delivery — letters can get lost, arrive late, or arrive out of order. If you need guarantees, you use registered mail (TCP).</p>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📊</span><h3>IP in Context — The Protocol Stack</h3><span class="tag tag-blue">POSITION IN STACK</span></div>
  <div class="cp-body">
<p>IP sits at Layer 3 of the OSI model — above Ethernet (L2) and below TCP/UDP (L4). Every TCP connection, every UDP datagram, every DNS query, every HTTP request — they all travel inside IP packets.</p>
<div class="cb"><pre><span class="cm">/* Stack position of IPv4 */</span>
 
Application layer:  HTTP data ("GET /index.html...")
                         ↓ TCP wraps with segment header
Transport layer:    [TCP hdr: sport=52341 dport=80] + [HTTP data]
                         ↓ IP wraps with packet header
Network layer:      [IP hdr: src=10.0.0.5 dst=93.184.216.34] + [TCP] + [HTTP]
                         ↓ Ethernet wraps with frame header
Data Link layer:    [Eth hdr: dst_mac src_mac 0x0800] + [IP] + [TCP] + [HTTP] + [CRC]
                         ↓ NIC transmits as bits
Physical layer:     01001000 01010100 01010100...</pre></div>
<p>The IP header's <strong>Protocol field</strong> (1 byte) tells the receiver what L4 protocol lives inside the packet: <code>6</code> = TCP, <code>17</code> = UDP, <code>1</code> = ICMP, <code>89</code> = OSPF, <code>50</code> = ESP (IPsec). This is how the kernel knows which protocol handler to pass the packet to after stripping the IP header.</p>
  </div>
</div>
</div>
<!-- ════════════ TAB 1 — IPv4 HEADER ════════════ -->
<div id="t1" class="tab-pane">
<p class="sep">IPv4 HEADER — 20 BYTES MINIMUM, EVERY FIELD EXPLAINED</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📦</span><h3>IPv4 Header Layout</h3><span class="tag tag-green">HEADER FORMAT</span></div>
  <div class="cp-body">
<p>The IPv4 header is a minimum of <strong>20 bytes</strong> (160 bits). It precedes the payload (TCP segment, UDP datagram, ICMP message, etc.). Each row below represents 32 bits (4 bytes) as transmitted on the wire.</p>
  </div>
</div>
<div class="hdr-diagram">
  <!-- Row 1 -->
  <div class="hdr-row">
<div class="hdr-label">Row 1</div>
<div class="hf hf-ver" style="flex:.5">Ver<div class="hf-bytes">4 bits</div></div>
<div class="hf hf-ihl" style="flex:.5">IHL<div class="hf-bytes">4 bits</div></div>
<div class="hf hf-dscp" style="flex:1">DSCP / ECN<div class="hf-bytes">8 bits</div></div>
<div class="hf hf-tot" style="flex:2">Total Length<div class="hf-bytes">16 bits</div></div>
  </div>
  <!-- Row 2 -->
  <div class="hdr-row">
<div class="hdr-label">Row 2</div>
<div class="hf hf-id" style="flex:2">Identification<div class="hf-bytes">16 bits</div></div>
<div class="hf hf-flg" style="flex:.6">Flags<div class="hf-bytes">3 bits</div></div>
<div class="hf hf-off" style="flex:1.4">Fragment Offset<div class="hf-bytes">13 bits</div></div>
  </div>
  <!-- Row 3 -->
  <div class="hdr-row">
<div class="hdr-label">Row 3</div>
<div class="hf hf-ttl" style="flex:1">TTL<div class="hf-bytes">8 bits</div></div>
<div class="hf hf-pro" style="flex:1">Protocol<div class="hf-bytes">8 bits</div></div>
<div class="hf hf-chk" style="flex:2">Header Checksum<div class="hf-bytes">16 bits</div></div>
  </div>
  <!-- Row 4 -->
  <div class="hdr-row">
<div class="hdr-label">Row 4</div>
<div class="hf hf-src" style="flex:4">Source IP Address<div class="hf-bytes">32 bits (4 bytes)</div></div>
  </div>
  <!-- Row 5 -->
  <div class="hdr-row">
<div class="hdr-label">Row 5</div>
<div class="hf hf-dst" style="flex:4">Destination IP Address<div class="hf-bytes">32 bits (4 bytes)</div></div>
  </div>
  <!-- Row 6 (optional) -->
  <div class="hdr-row">
<div class="hdr-label">Row 6+</div>
<div class="hf hf-opt" style="flex:4">Options (if IHL &gt; 5) + Padding<div class="hf-bytes">0–40 bytes — rare in practice</div></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Every Field — What It Does and Why It Matters</h3><span class="tag tag-blue">FIELD REFERENCE</span></div>
  <div class="cp-body">
<h4>Version (4 bits)</h4>
<p>Always <code>0100</code> = 4 for IPv4. IPv6 uses <code>0110</code> = 6. The receiver checks this first to confirm which IP version it's dealing with. In DPDK/VPP, this is the first thing <code>ip4-input</code> validates.</p>
<h4>IHL — Internet Header Length (4 bits)</h4>
<p>Specifies the header length in <strong>32-bit words</strong>. Minimum value is <code>5</code> (5 × 4 bytes = 20 bytes, the minimum header with no options). Maximum is <code>15</code> (15 × 4 = 60 bytes). IHL tells the receiver where the payload starts: payload offset = IHL × 4.</p>
<div class="cb"><pre><span class="cm">/* C: find where IP payload begins */</span>
<span class="ck">uint8_t</span> *ip_hdr = packet_start;
<span class="ck">uint8_t</span>  ihl     = (ip_hdr[0] & 0x0F);     <span class="cm">/* low nibble of first byte */</span>
<span class="ck">uint8_t</span> *payload = ip_hdr + (ihl * 4);     <span class="cm">/* jump over header */</span></pre></div>
<h4>DSCP / ECN (8 bits — formerly TOS)</h4>
<p>Originally called <em>Type of Service</em>, now split into two fields:</p>
<ul>
<li><strong>DSCP</strong> (Differentiated Services Code Point, 6 bits) — QoS marking. Routers and firewalls use this to prioritise packets. Common values: <code>0</code> = Best Effort, <code>46</code> = Expedited Forwarding (voice/video), <code>34</code> = Assured Forwarding. NGFW policy engines can mark and classify traffic using DSCP.</li>
<li><strong>ECN</strong> (Explicit Congestion Notification, 2 bits) — allows congestion notification without packet drops. Routers mark ECN bits when they're near capacity; the receiver signals the sender to slow down.</li>
</ul>
<h4>Total Length (16 bits)</h4>
<p>The total size of the IP packet in bytes — header + payload. Maximum value: <code>65535</code>. Practical maximum on standard Ethernet: <code>1500</code> (MTU). This field is critical: receivers use it to know how many bytes to read, and it allows detection of truncated packets.</p>
<h4>Identification (16 bits)</h4>
<p>A unique ID assigned by the sender to identify all fragments of the same original packet. When a large packet is fragmented, all fragments get the same Identification value — the receiver uses it to reassemble them. Not used for non-fragmented packets (but still set by the OS).</p>
<h4>Flags (3 bits)</h4>
<div class="bit-row">
<div class="bit-group"><div class="bit-box" style="background:#f0f0f0;border-color:#ccc;color:#888">0</div><div class="bit-label">Reserved (always 0)</div></div>
<div class="bit-group" style="margin-left:6px"><div class="bit-box" style="background:#faeaea;border-color:#e8a0a0;color:#6c1a1a">DF</div><div class="bit-label">Don't Fragment</div></div>
<div class="bit-group" style="margin-left:6px"><div class="bit-box" style="background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c">MF</div><div class="bit-label">More Fragments</div></div>
</div>
<ul>
<li><strong>DF (Don't Fragment)</strong> — tells routers not to fragment this packet. If the packet is too large for a link and DF=1, the router drops it and sends an ICMP "Fragmentation Needed" message back. Used by Path MTU Discovery (PMTUD)</li>
<li><strong>MF (More Fragments)</strong> — set to 1 on all fragment except the last. Receiver uses this to know when it has collected all fragments</li>
</ul>
<h4>Fragment Offset (13 bits)</h4>
<p>Position of this fragment's data within the original packet, measured in units of 8 bytes. A value of <code>185</code> means this fragment's data starts at byte offset 185 × 8 = 1480 in the original packet. The receiver uses Identification + Fragment Offset to put fragments back in order.</p>
<h4>TTL — Time To Live (8 bits)</h4>
<p>A counter decremented by 1 at each router hop. When TTL reaches 0, the router discards the packet and sends an ICMP Time Exceeded message back to the sender. Purpose: prevent packets from looping forever in a routing loop. Starting TTL is typically 64 (Linux), 128 (Windows), or 255 (some routers). We cover TTL in detail in the TTL and Routing tab.</p>
<h4>Protocol (8 bits)</h4>
<p>Identifies the L4 protocol inside the payload:</p>
<ul>
<li><code>1</code> — ICMP</li>
<li><code>6</code> — TCP</li>
<li><code>17</code> — UDP</li>
<li><code>41</code> — IPv6-in-IPv4 (6in4 tunnel)</li>
<li><code>47</code> — GRE</li>
<li><code>50</code> — ESP (IPsec)</li>
<li><code>51</code> — AH (IPsec)</li>
<li><code>89</code> — OSPF</li>
<li><code>132</code> — SCTP</li>
</ul>
<h4>Header Checksum (16 bits)</h4>
<p>A checksum computed over the IP header only (not the payload — TCP/UDP have their own checksums). Each router must recompute it after decrementing TTL. If the checksum fails, the packet is silently dropped. Modern NICs (including your Mellanox) offload checksum verification to hardware.</p>
<h4>Source IP Address (32 bits) and Destination IP Address (32 bits)</h4>
<p>The 4-byte IPv4 addresses of sender and receiver. These are the primary fields routers use for forwarding decisions. In NAT, both source and destination addresses may be rewritten by the firewall/NAT device.</p>
  </div>
</div>
<div class="ins">
  <p>💡 <strong>In DPDK/VPP code</strong>, the IPv4 header is accessed via <code>ip4_header_t</code> (VPP) or a manual struct. Key fields accessed in the fast path: <code>ip4->dst_address</code> (FIB lookup), <code>ip4->protocol</code> (dispatch to TCP/UDP), <code>ip4->ttl</code> (decrement), <code>ip4->checksum</code> (recompute after TTL change). These are the fields your graph nodes will read millions of times per second.</p>
</div>
</div>
<!-- ════════════ TAB 2 — IP ADDRESSING ════════════ -->
<div id="t2" class="tab-pane">
<p class="sep">IPv4 ADDRESSING — 32-BIT ADDRESSES, NOTATION, CLASSES</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🏷️</span><h3>IPv4 Address Structure</h3><span class="tag tag-green">CORE CONCEPT</span></div>
  <div class="cp-body">
<p>An IPv4 address is a <strong>32-bit number</strong> — four groups of 8 bits (octets) separated by dots. We write it in <strong>dotted-decimal notation</strong> where each octet is expressed as a decimal number from 0 to 255.</p>
<div style="text-align:center;margin:1rem 0">
<div style="font-size:.72rem;font-family:monospace;color:var(--light-text,#666);margin-bottom:6px">Binary representation of 192.168.1.100</div>
<div class="ip-breakdown" style="justify-content:center">
<div class="ip-col">
<div class="ip-octet" style="background:#e8f5e8;border-color:#90d890;color:#1a5a1a">192</div>
<div class="ip-octet-lbl">11000000</div>
</div>
<div class="ip-sep">.</div>
<div class="ip-col">
<div class="ip-octet" style="background:#e8f5e8;border-color:#90d890;color:#1a5a1a">168</div>
<div class="ip-octet-lbl">10101000</div>
</div>
<div class="ip-sep">.</div>
<div class="ip-col">
<div class="ip-octet" style="background:#e8f5e8;border-color:#90d890;color:#1a5a1a">1</div>
<div class="ip-octet-lbl">00000001</div>
</div>
<div class="ip-sep">.</div>
<div class="ip-col">
<div class="ip-octet" style="background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c">100</div>
<div class="ip-octet-lbl">01100100</div>
</div>
</div>
<div style="font-size:.72rem;font-family:monospace;color:var(--light-text,#666);margin-top:4px">Full 32-bit binary: 11000000.10101000.00000001.01100100</div>
</div>
<p>Every IP address has two parts — a <strong>network portion</strong> and a <strong>host portion</strong>. The <strong>subnet mask</strong> tells you which bits are the network part (1s) and which are the host part (0s).</p>
<ul>
<li>All devices in the same network have identical network bits</li>
<li>Each device has a unique host portion within its network</li>
<li>Routers forward packets based on the network portion — they don't care about individual host bits</li>
</ul>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📚</span><h3>Classful Addressing — Historical but Still Referenced</h3><span class="tag tag-blue">BACKGROUND</span></div>
  <div class="cp-body">
<p>Before CIDR (1993), IPv4 addresses were divided into fixed classes. You still hear these terms in networking conversations:</p>
<table class="t-table">
<thead><tr><th>Class</th><th>First Bits</th><th>Range</th><th>Default Mask</th><th>Networks</th><th>Hosts/Network</th><th>Use</th></tr></thead>
<tbody>
<tr><td><strong>A</strong></td><td>0xxxxxxx</td><td>1.0.0.0 – 126.255.255.255</td><td>/8 (255.0.0.0)</td><td>126</td><td>16,777,214</td><td>Large orgs</td></tr>
<tr><td><strong>B</strong></td><td>10xxxxxx</td><td>128.0.0.0 – 191.255.255.255</td><td>/16 (255.255.0.0)</td><td>16,384</td><td>65,534</td><td>Medium orgs</td></tr>
<tr><td><strong>C</strong></td><td>110xxxxx</td><td>192.0.0.0 – 223.255.255.255</td><td>/24 (255.255.255.0)</td><td>2,097,152</td><td>254</td><td>Small orgs</td></tr>
<tr><td><strong>D</strong></td><td>1110xxxx</td><td>224.0.0.0 – 239.255.255.255</td><td>N/A</td><td>N/A</td><td>N/A</td><td>Multicast</td></tr>
<tr><td><strong>E</strong></td><td>1111xxxx</td><td>240.0.0.0 – 255.255.255.255</td><td>N/A</td><td>N/A</td><td>N/A</td><td>Reserved/Experimental</td></tr>
</tbody>
</table>
<p>Classful addressing wasted enormous numbers of IP addresses (a company needing 300 hosts got a Class B with 65,534 addresses — 65,234 wasted). CIDR replaced classful addressing, but the Class A/B/C terminology persists in configuration and documentation.</p>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>Subnet Mask — The Network/Host Boundary</h3><span class="tag tag-teal">SUBNET MASK</span></div>
  <div class="cp-body">
<p>A subnet mask is a 32-bit number where all <strong>network bits are 1</strong> and all <strong>host bits are 0</strong>. Two notation forms:</p>
<ul>
<li><strong>Dotted-decimal:</strong> <code>255.255.255.0</code> — easier to read for humans</li>
<li><strong>CIDR prefix length:</strong> <code>/24</code> — count of 1-bits. Much more compact.</li>
</ul>



```yaml
/* Example: 192.168.1.100/24 */
IP address:   192.168.1.100  =  11000000.10101000.00000001.01100100
Subnet mask:  255.255.255.0  =  11111111.11111111.11111111.00000000
                                 ←──── Network portion ────→ ←Host→

/* AND operation: IP & mask = Network address */
Network addr: 192.168.1.0    =  11000000.10101000.00000001.00000000

/* Broadcast: network with all host bits = 1 */
Broadcast:    192.168.1.255  =  11000000.10101000.00000001.11111111

/* Usable hosts: from .1 to .254 (254 hosts for /24) */
First host:   192.168.1.1
Last host:    192.168.1.254
```



<p><strong>Three critical addresses in every subnet:</strong></p>
<ul>
<li><strong>Network address</strong> — host bits all 0. Identifies the subnet itself, not assignable to a host (e.g., <code>192.168.1.0</code>)</li>
<li><strong>Broadcast address</strong> — host bits all 1. Sends to all hosts in the subnet, not assignable (e.g., <code>192.168.1.255</code>)</li>
<li><strong>Usable host range</strong> — everything between. For /24: 192.168.1.1 to 192.168.1.254 = 254 usable hosts</li>
</ul>
  </div>
</div>
</div>
<!-- ════════════ TAB 3 — SUBNETTING AND CIDR ════════════ -->
<div id="t3" class="tab-pane">
<p class="sep">SUBNETTING AND CIDR — DIVIDING ADDRESS SPACE EFFICIENTLY</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">✂️</span><h3>Why Subnetting Exists</h3><span class="tag tag-green">MOTIVATION</span></div>
  <div class="cp-body">
<p>Subnetting takes a large network and divides it into smaller sub-networks. This is done for three reasons:</p>
<ul>
<li><strong>Security isolation</strong> — different departments/zones in different subnets, firewall between them (your NGFW use case)</li>
<li><strong>Performance</strong> — smaller broadcast domains mean less broadcast noise</li>
<li><strong>Address efficiency</strong> — allocate exactly as many IPs as you need, no wastage</li>
</ul>
<p>When you subnet, you <strong>borrow bits from the host portion</strong> and add them to the network portion — increasing the prefix length. More network bits = smaller subnets = fewer hosts per subnet.</p>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📐</span><h3>CIDR Prefix Reference Table</h3><span class="tag tag-blue">REFERENCE</span></div>
  <div class="cp-body">
<table class="t-table">
<thead><tr><th>Prefix</th><th>Subnet Mask</th><th>Hosts</th><th>Usable Hosts</th><th>Typical Use</th></tr></thead>
<tbody>
<tr><td><code>/8</code></td><td>255.0.0.0</td><td>16,777,216</td><td>16,777,214</td><td>ISP, large org backbone</td></tr>
<tr><td><code>/16</code></td><td>255.255.0.0</td><td>65,536</td><td>65,534</td><td>Large campus, cloud VPC</td></tr>
<tr><td><code>/20</code></td><td>255.255.240.0</td><td>4,096</td><td>4,094</td><td>Medium office, data centre zone</td></tr>
<tr><td><code>/24</code></td><td>255.255.255.0</td><td>256</td><td>254</td><td>Standard office LAN, server subnet</td></tr>
<tr><td><code>/25</code></td><td>255.255.255.128</td><td>128</td><td>126</td><td>Split /24 into two halves</td></tr>
<tr><td><code>/26</code></td><td>255.255.255.192</td><td>64</td><td>62</td><td>Department subnets</td></tr>
<tr><td><code>/27</code></td><td>255.255.255.224</td><td>32</td><td>30</td><td>Small team subnet</td></tr>
<tr><td><code>/28</code></td><td>255.255.255.240</td><td>16</td><td>14</td><td>Small server cluster</td></tr>
<tr><td><code>/29</code></td><td>255.255.255.248</td><td>8</td><td>6</td><td>Router-to-router links</td></tr>
<tr><td><code>/30</code></td><td>255.255.255.252</td><td>4</td><td>2</td><td>Point-to-point links (2 hosts only)</td></tr>
<tr><td><code>/31</code></td><td>255.255.255.254</td><td>2</td><td>2*</td><td>P2P links (RFC 3021 — no network/broadcast)</td></tr>
<tr><td><code>/32</code></td><td>255.255.255.255</td><td>1</td><td>1</td><td>Host route, loopback, BGP next-hop</td></tr>
</tbody>
</table>
<p style="font-size:.8rem;color:var(--light-text,#666)">Formula: Hosts = 2^(32-prefix). Usable = Hosts - 2 (subtract network and broadcast). Exception: /31 and /32 have special rules.</p>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🧮</span><h3>Subnetting by Hand — Step-by-Step Method</h3><span class="tag tag-teal">TECHNIQUE</span></div>
  <div class="cp-body">
<p><strong>Problem:</strong> You have <code>192.168.10.0/24</code> and need to create 4 equal subnets. What are the subnets?</p>
<p><strong>Step 1 — How many bits to borrow?</strong></p>
<p>You need 4 subnets = 2² → borrow <strong>2 bits</strong> from the host portion. New prefix = /24 + 2 = <strong>/26</strong>.</p>
<p><strong>Step 2 — What is the block size?</strong></p>
<p>Block size = 256 - subnet_mask_last_octet = 256 - 192 = <strong>64</strong>. (For /26: mask = 255.255.255.192, last octet = 192.)</p>
<p><strong>Step 3 — List the subnets</strong> (increment by block size in the last octet):</p>
<table class="t-table">
<thead><tr><th>Subnet</th><th>Network Addr</th><th>First Host</th><th>Last Host</th><th>Broadcast</th></tr></thead>
<tbody>
<tr><td><code>/26</code> #1</td><td>192.168.10.0</td><td>192.168.10.1</td><td>192.168.10.62</td><td>192.168.10.63</td></tr>
<tr><td><code>/26</code> #2</td><td>192.168.10.64</td><td>192.168.10.65</td><td>192.168.10.126</td><td>192.168.10.127</td></tr>
<tr><td><code>/26</code> #3</td><td>192.168.10.128</td><td>192.168.10.129</td><td>192.168.10.190</td><td>192.168.10.191</td></tr>
<tr><td><code>/26</code> #4</td><td>192.168.10.192</td><td>192.168.10.193</td><td>192.168.10.254</td><td>192.168.10.255</td></tr>
</tbody>
</table>
<p><strong>Visual — network vs host bits for /26:</strong></p>
<div class="cidr-vis">
<div class="cidr-net" style="flex:8">Network bits (26 bits fixed)<br><span style="font-weight:400;font-size:.65rem">192.168.10.xx</span></div>
<div class="cidr-sep">|</div>
<div class="cidr-host" style="flex:6">Host bits (6 bits variable)<br><span style="font-weight:400;font-size:.65rem">0–63 per subnet</span></div>
</div>
<div class="ins"><p>💡 <strong>NGFW application:</strong> In a typical enterprise NGFW deployment you'll design security zones as subnets: <code>10.0.1.0/24</code> = Inside LAN, <code>10.0.2.0/24</code> = DMZ servers, <code>10.0.3.0/24</code> = Management. The firewall sits between these subnets and applies policy at the IP layer. Knowing subnetting lets you write precise ACL rules like <code>permit ip 10.0.1.0/24 10.0.2.0/24</code>.</p></div>
  </div>
</div>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">💻</span><h3>Subnet Arithmetic in C</h3><span class="tag tag-amber">CODE</span></div>
  <div class="cp-body">


```cpp
#include <stdio.h>
#include <arpa/inet.h>
#include <stdint.h>

int main() {
    /* IP and prefix */
    uint32_t ip     = inet_addr("192.168.10.100");  /* network byte order */
    uint32_t prefix = 26;

    /* Build mask: ~0 shifted left by (32-prefix) bits */
    uint32_t mask = htonl(~0u /* 0xFFFFFFC0 = /26 */

    /* Network address = ip AND mask */
    uint32_t network   = ip & mask;

    /* Broadcast = network OR (NOT mask) */
    uint32_t broadcast = network | ~mask;

    /* First and last host */
    uint32_t first = htonl(ntohl(network) + 1);
    uint32_t last  = htonl(ntohl(broadcast) - 1);

    /* Usable host count */
    uint32_t hosts = ntohl(broadcast) - ntohl(network) - 1;

    char buf[INET_ADDRSTRLEN];
    printf("Network:   %s\n", inet_ntop(AF_INET, &network,   buf, sizeof(buf)));
    printf("Broadcast: %s\n", inet_ntop(AF_INET, &broadcast, buf, sizeof(buf)));
    printf("First:     %s\n", inet_ntop(AF_INET, &first,     buf, sizeof(buf)));
    printf("Last:      %s\n", inet_ntop(AF_INET, &last,      buf, sizeof(buf)));
    printf("Hosts:     %u\n", hosts);
    return 0;
}
```


  </div>
</div>
</div>
<!-- ════════════ TAB 4 — SPECIAL ADDRESSES ════════════ -->
<div id="t4" class="tab-pane">
<p class="sep">SPECIAL IPv4 ADDRESS RANGES — KNOW THESE BY HEART</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🗺️</span><h3>Reserved and Special Address Ranges</h3><span class="tag tag-blue">REFERENCE</span></div>
  <div class="cp-body">
<table class="t-table">
<thead><tr><th>Range</th><th>Name</th><th>Purpose</th><th>RFC</th><th>NGFW Relevance</th></tr></thead>
<tbody>
<tr><td><code>10.0.0.0/8</code></td><td>Private Class A</td><td>Internal networks — not routed on internet</td><td>RFC 1918</td><td>Typically "inside" zone — allow policy</td></tr>
<tr><td><code>172.16.0.0/12</code></td><td>Private Class B</td><td>Internal networks — covers 172.16–172.31.x.x</td><td>RFC 1918</td><td>Often used for DMZ / management</td></tr>
<tr><td><code>192.168.0.0/16</code></td><td>Private Class C</td><td>Internal networks — common in SOHO/offices</td><td>RFC 1918</td><td>Home/branch office subnets</td></tr>
<tr><td><code>127.0.0.0/8</code></td><td>Loopback</td><td>Local host communication. 127.0.0.1 = "localhost"</td><td>RFC 5735</td><td>Never route this — drop at perimeter</td></tr>
<tr><td><code>169.254.0.0/16</code></td><td>Link-Local / APIPA</td><td>Auto-assigned when DHCP fails. Not routable</td><td>RFC 3927</td><td>Indicator of DHCP failure on host</td></tr>
<tr><td><code>100.64.0.0/10</code></td><td>Shared Address Space</td><td>CGN (Carrier-Grade NAT) — ISP internal use</td><td>RFC 6598</td><td>Treat like RFC 1918 — don't route externally</td></tr>
<tr><td><code>0.0.0.0/8</code></td><td>Unspecified</td><td>0.0.0.0 = "this host" — used before IP assigned</td><td>RFC 1122</td><td>Drop all packets with source 0.0.0.0</td></tr>
<tr><td><code>255.255.255.255/32</code></td><td>Broadcast</td><td>Limited broadcast — all hosts on local network</td><td>RFC 919</td><td>Drop at firewall — never route</td></tr>
<tr><td><code>224.0.0.0/4</code></td><td>Multicast</td><td>Group communication (OSPF, video streaming)</td><td>RFC 5771</td><td>Allow selectively (OSPF: 224.0.0.5/6)</td></tr>
<tr><td><code>240.0.0.0/4</code></td><td>Reserved</td><td>Reserved for future use — treat as invalid</td><td>RFC 1112</td><td>Drop all packets in this range</td></tr>
<tr><td><code>192.0.2.0/24</code></td><td>TEST-NET-1</td><td>Documentation and examples — never real traffic</td><td>RFC 5737</td><td>Drop at perimeter</td></tr>
<tr><td><code>198.51.100.0/24</code></td><td>TEST-NET-2</td><td>Documentation — as above</td><td>RFC 5737</td><td>Drop at perimeter</td></tr>
<tr><td><code>203.0.113.0/24</code></td><td>TEST-NET-3</td><td>Documentation — as above</td><td>RFC 5737</td><td>Drop at perimeter</td></tr>
</tbody>
</table>
  </div>
</div>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>Bogon Filtering — NGFW First Line of Defence</h3><span class="tag tag-red">SECURITY</span></div>
  <div class="cp-body">
<p>A <strong>bogon</strong> is an IP address that should never appear as a source on the public internet — either because it's reserved (RFC 1918 private, loopback, link-local) or unallocated. An NGFW at the internet perimeter should drop all packets with bogon source addresses — they indicate either misconfiguration or deliberate spoofing (attack).</p>



```python
/* Bogon filter — drop these source IPs at internet-facing interface */
/* These are source addresses that should NEVER arrive from the internet */

Bogon source ranges to block:
  10.0.0.0/8          RFC 1918 private
  172.16.0.0/12       RFC 1918 private
  192.168.0.0/16      RFC 1918 private
  127.0.0.0/8         Loopback
  169.254.0.0/16      Link-local
  100.64.0.0/10       Shared address space
  0.0.0.0/8           Unspecified
  240.0.0.0/4         Reserved
  224.0.0.0/4         Multicast (as source — invalid)
  192.0.2.0/24        TEST-NET-1
  198.51.100.0/24     TEST-NET-2
  203.0.113.0/24      TEST-NET-3

/* Unicas Reverse Path Forwarding (uRPF) — a smarter bogon filter */
/* Router drops packets if the source IP has no route back via the */
/* same interface the packet arrived on — prevents spoofed sources */
```



<p>In VPP, bogon filtering is implemented as an IP feature arc plugin with a bihash lookup of source address against a prefix table. You'll build a version of this in Phase 6 (NGFW Development).</p>
  </div>
</div>
</div>
<!-- ════════════ TAB 5 — TTL AND ROUTING ════════════ -->
<div id="t5" class="tab-pane">
<p class="sep">TTL, ROUTING BASICS, AND HOW ROUTERS FORWARD PACKETS</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">⏱️</span><h3>TTL — Time To Live</h3><span class="tag tag-orange">TTL</span></div>
  <div class="cp-body">
<p>TTL is an 8-bit counter in the IP header that starts at a value set by the sender (typically 64 for Linux, 128 for Windows, 255 for many routers) and is decremented by 1 at every router hop. When TTL reaches 0, the router discards the packet and sends an <strong>ICMP Time Exceeded</strong> message back to the original sender.</p>
<p><strong>Why TTL exists:</strong> Without TTL, a packet caught in a routing loop (two routers sending it back and forth) would circulate forever, consuming bandwidth indefinitely. TTL guarantees every packet has a finite lifetime.</p>



```yaml
/* TTL trace: packet from your laptop to 8.8.8.8 */
Hop 1: Your router     TTL: 64 → 63   (decremented, forwarded)
Hop 2: ISP router 1   TTL: 63 → 62   (decremented, forwarded)
Hop 3: ISP router 2   TTL: 62 → 61   (decremented, forwarded)
...
Hop 12: Google router  TTL: 52 → 51   (decremented, forwarded)
Hop 13: 8.8.8.8        TTL: 51        (received — destination reached)

/* If TTL hits 0 at an intermediate router: */
Router discards packet + sends ICMP Type 11, Code 0 (Time Exceeded)
Sender receives ICMP with source IP of the discarding router
→ This is how traceroute works! (see ICMP tab)

/* Default TTL values by OS */
Linux:   64    (set in /proc/sys/net/ipv4/ip_default_ttl)
Windows: 128
Cisco:   255
macOS:   64
```



<p><strong>NGFW use of TTL:</strong> TTL can reveal OS fingerprinting — a packet arriving with TTL=127 likely came from Windows (started at 128, lost 1 hop). Firewalls can use this for passive OS detection. Some NGFW features normalise TTL values to prevent fingerprinting attacks.</p>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🗺️</span><h3>How Routers Make Forwarding Decisions</h3><span class="tag tag-teal">ROUTING BASICS</span></div>
  <div class="cp-body">
<p>Every router maintains a <strong>routing table</strong> (also called the FIB — Forwarding Information Base). When a packet arrives, the router looks up the destination IP address in the FIB using <strong>Longest Prefix Match (LPM)</strong>: find the most specific route that covers the destination.</p>



```bash
/* Example routing table on a Linux router */
$ ip route show

10.0.0.0/8       via 192.168.1.1 dev eth0        # Match any 10.x.x.x
10.10.0.0/16     via 192.168.1.2 dev eth0        # More specific match
10.10.1.0/24     dev eth1 proto kernel scope link # Most specific — local
0.0.0.0/0        via 203.0.113.1 dev eth2         # Default route (catch-all)

/* LPM example: packet destined for 10.10.1.55 */
Matches 0.0.0.0/0    → /0  — too broad
Matches 10.0.0.0/8   → /8  — candidate
Matches 10.10.0.0/16 → /16 — more specific
Matches 10.10.1.0/24 → /24 — MOST SPECIFIC → this one wins

/* Router actions after lookup: */
1. Decrement TTL (if TTL becomes 0: drop + send ICMP Time Exceeded)
2. Recompute IP header checksum (TTL changed)
3. ARP-resolve next-hop MAC if not cached
4. Rewrite Ethernet header: new dst MAC (next-hop) + src MAC (this router's outgoing port)
5. Transmit on outgoing interface
```



<div class="note"><p>💡 <strong>What the router does NOT touch:</strong> Source IP, destination IP, and the entire IP payload (TCP/UDP/application data). IP routing is transparent to endpoints — your laptop doesn't know or care how many routers handled its packet. Routers only touch the Ethernet header and the TTL/checksum fields of the IP header.</p></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 6 — FRAGMENTATION ════════════ -->
<div id="t6" class="tab-pane">
<p class="sep">IP FRAGMENTATION AND PATH MTU DISCOVERY</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">✂️</span><h3>Why Fragmentation Exists</h3><span class="tag tag-purple">CONCEPT</span></div>
  <div class="cp-body">
<p>Every network link has a <strong>Maximum Transmission Unit (MTU)</strong> — the largest IP packet it can carry. Standard Ethernet: 1500 bytes. Some links are smaller (PPPoE adds 8 bytes overhead, reducing effective MTU to 1492). When a packet larger than a link's MTU needs to cross that link, IP fragments it into smaller pieces.</p>
<p>Fragmentation happens at any router along the path (not just the sender) and <strong>reassembly happens only at the destination host</strong> — not at intermediate routers. This design choice avoids reassembly overhead at every hop.</p>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">✂️</span><h3>How Fragmentation Works</h3><span class="tag tag-blue">MECHANICS</span></div>
  <div class="cp-body">
<p>Scenario: a 4000-byte IP packet arrives at a router whose outgoing link has MTU 1500. The router fragments it into three pieces.</p>
<div class="frag-vis">
<div style="font-size:.72rem;font-family:monospace;color:var(--light-text,#666);margin-bottom:3px">Original packet: 4000 bytes (IP header 20B + data 3980B) — too large for MTU 1500</div>
<div class="frag-original">
<div class="frag-chunk" style="flex:.5;background:#e8f1f9;color:#1a3a5c;border-right:1px solid #b0ccec">IP Hdr<br><span style="font-size:.65rem">20B</span></div>
<div class="frag-chunk" style="flex:3.98;background:#e8f5e8;color:#1a5a1a">Data: 3980 bytes</div>
</div>
<div class="frag-arrow">↓ Router fragments at MTU 1500 boundary</div>
<div class="frag-fragments">
<div class="frag-fragment">
<div style="font-size:.68rem;font-family:monospace;padding:2px 6px;background:#1a5a1a;color:#fff">Fragment 1 — 1500B total</div>
<div class="frag-fragment-row">
<div class="frag-chunk" style="flex:.5;background:#e8f1f9;color:#1a3a5c;border-right:1px solid #b0ccec">IP Hdr<br><span style="font-size:.62rem">20B<br>ID=x<br>MF=1<br>off=0</span></div>
<div class="frag-chunk" style="flex:1.48;background:#e8f5e8;color:#1a5a1a;font-size:.65rem">Data bytes 0–1479<br>(1480 bytes)</div>
</div>
</div>
<div class="frag-fragment">
<div style="font-size:.68rem;font-family:monospace;padding:2px 6px;background:#1a5a1a;color:#fff">Fragment 2 — 1500B total</div>
<div class="frag-fragment-row">
<div class="frag-chunk" style="flex:.5;background:#e8f1f9;color:#1a3a5c;border-right:1px solid #b0ccec">IP Hdr<br><span style="font-size:.62rem">20B<br>ID=x<br>MF=1<br>off=185</span></div>
<div class="frag-chunk" style="flex:1.48;background:#e8f5e8;color:#1a5a1a;font-size:.65rem">Data bytes 1480–2959<br>(1480 bytes)</div>
</div>
</div>
<div class="frag-fragment">
<div style="font-size:.68rem;font-family:monospace;padding:2px 6px;background:#1a5a1a;color:#fff">Fragment 3 — 1040B total</div>
<div class="frag-fragment-row">
<div class="frag-chunk" style="flex:.5;background:#e8f1f9;color:#1a3a5c;border-right:1px solid #b0ccec">IP Hdr<br><span style="font-size:.62rem">20B<br>ID=x<br>MF=0<br>off=370</span></div>
<div class="frag-chunk" style="flex:1;background:#e8f5e8;color:#1a5a1a;font-size:.65rem">Data bytes 2960–3979<br>(1020 bytes)</div>
</div>
</div>
</div>
</div>
<p><strong>Fragment field values explained:</strong></p>
<ul>
<li><strong>Identification = x</strong> — same value in all 3 fragments (receiver uses this to group them)</li>
<li><strong>MF=1</strong> — More Fragments — set on first two fragments, MF=0 on the last</li>
<li><strong>Fragment Offset</strong> — in units of 8 bytes: 0 / 185 (1480÷8) / 370 (2960÷8)</li>
<li><strong>Fragment data size</strong> — must be multiple of 8 bytes (except last) to allow correct offset calculation</li>
</ul>
  </div>
</div>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>Fragmentation Problems and PMTUD</h3><span class="tag tag-red">ISSUES</span></div>
  <div class="cp-body">
<p>Fragmentation causes several real-world problems:</p>
<ul>
<li><strong>Performance overhead</strong> — reassembly at the destination consumes CPU and memory. Fragments must be buffered until all arrive.</li>
<li><strong>Firewall complexity</strong> — stateful firewalls must reassemble fragments before inspecting the transport header (TCP/UDP ports are only in the first fragment). This is a significant processing cost.</li>
<li><strong>Fragment attacks</strong> — attackers exploit fragmentation: overlapping fragments (Teardrop), tiny first fragment (hides TCP flags from firewall), missing last fragment (holds reassembly buffer forever).</li>
<li><strong>ICMP filtering</strong> — some networks block ICMP, which breaks Path MTU Discovery (see below).</li>
</ul>
<h4>Path MTU Discovery (PMTUD)</h4>
<p>Modern systems avoid fragmentation by discovering the smallest MTU on the path before sending large packets:</p>
<div class="flow-list">
<div class="fl-step" data-n="1" style="--sc:#6c1a1a"><div><div class="fl-title">Sender sets DF=1 on all packets</div><div class="fl-detail">Don't Fragment bit = 1 tells routers not to fragment — drop instead.</div></div></div>
<div class="fl-step" data-n="2" style="--sc:#6c1a1a"><div><div class="fl-title">Router with smaller MTU drops packet</div><div class="fl-detail">Router drops the oversized packet and sends ICMP Type 3, Code 4 "Fragmentation Needed" with the MTU of its link.</div><div class="fl-code">ICMP: Type=3 Code=4 Next-Hop-MTU=1492</div></div></div>
<div class="fl-step" data-n="3" style="--sc:#6c1a1a"><div><div class="fl-title">Sender reduces packet size</div><div class="fl-detail">Sender receives the ICMP and records the reduced MTU for this destination. Future packets use the smaller size. TCP adjusts its MSS (Maximum Segment Size) accordingly.</div></div></div>
</div>
<div class="warn"><p>⚠️ <strong>ICMP Black Holes:</strong> If a firewall blocks ICMP (a common but misguided practice), PMTUD breaks. The sender never receives the "Fragmentation Needed" message, packets keep getting dropped silently, and connections hang. This manifests as "large downloads hang after a few KB". NGFW policy must allow ICMP Type 3, Code 4 through for PMTUD to work correctly.</p></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 7 — ICMP ════════════ -->
<div id="t7" class="tab-pane">
<p class="sep">ICMP — INTERNET CONTROL MESSAGE PROTOCOL (RFC 792)</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">📨</span><h3>What ICMP Is and Why It Exists</h3><span class="tag tag-orange">OVERVIEW</span></div>
  <div class="cp-body">
<p>ICMP is IP's built-in diagnostic and error-reporting protocol. It travels <em>inside</em> IP packets (Protocol = 1) and is used by routers and hosts to report errors and exchange control information. ICMP itself has no concept of ports — it operates below TCP/UDP.</p>
<p>ICMP is essential for:</p>
<ul>
<li><strong>Ping</strong> — testing reachability (Echo Request/Reply)</li>
<li><strong>Traceroute</strong> — discovering the path to a destination (abuses TTL expiry)</li>
<li><strong>Error reporting</strong> — telling senders why their packets were dropped</li>
<li><strong>Path MTU Discovery</strong> — informing senders of MTU limitations (Type 3, Code 4)</li>
</ul>
<p>ICMP format: 8-byte fixed header (Type, Code, Checksum, + 4 bytes of type-specific data) followed by optional additional data.</p>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📋</span><h3>ICMP Message Types — Complete Reference</h3><span class="tag tag-blue">REFERENCE</span></div>
  <div class="cp-body">
<table class="icmp-table">
<thead><tr><th>Type</th><th>Code</th><th>Name</th><th>Direction</th><th>Caused By / Use</th></tr></thead>
<tbody>
<tr><td><code>0</code></td><td>0</td><td>Echo Reply</td><td>Host → Pinger</td><td>Response to ping (Type 8)</td></tr>
<tr><td><code>3</code></td><td>0</td><td>Dest Unreachable — Net</td><td>Router → Sender</td><td>No route to destination network</td></tr>
<tr><td><code>3</code></td><td>1</td><td>Dest Unreachable — Host</td><td>Router → Sender</td><td>No route to specific host</td></tr>
<tr><td><code>3</code></td><td>2</td><td>Dest Unreachable — Protocol</td><td>Host → Sender</td><td>Protocol not supported on destination</td></tr>
<tr><td><code>3</code></td><td>3</td><td>Dest Unreachable — Port</td><td>Host → Sender</td><td>UDP port not listening (no process bound)</td></tr>
<tr><td><code>3</code></td><td>4</td><td>Fragmentation Needed</td><td>Router → Sender</td><td>Packet too large + DF=1 set. Includes next-hop MTU.</td></tr>
<tr><td><code>3</code></td><td>9</td><td>Dest Unreachable — Filtered</td><td>Router/FW → Sender</td><td>Firewall rejected the packet (admin filter)</td></tr>
<tr><td><code>5</code></td><td>0-3</td><td>Redirect</td><td>Router → Host</td><td>Better route exists via different gateway</td></tr>
<tr><td><code>8</code></td><td>0</td><td>Echo Request</td><td>Sender → Host</td><td>Ping — tests reachability</td></tr>
<tr><td><code>11</code></td><td>0</td><td>Time Exceeded (TTL)</td><td>Router → Sender</td><td>TTL reached 0 — used by traceroute</td></tr>
<tr><td><code>11</code></td><td>1</td><td>Time Exceeded (Reassembly)</td><td>Host → Sender</td><td>Fragment reassembly timer expired</td></tr>
<tr><td><code>12</code></td><td>0-2</td><td>Parameter Problem</td><td>Router/Host → Sender</td><td>IP header field is invalid</td></tr>
</tbody>
</table>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Traceroute — How It Works</h3><span class="tag tag-teal">TECHNIQUE</span></div>
  <div class="cp-body">
<p>Traceroute exploits TTL and ICMP Time Exceeded messages to discover every router on the path to a destination. It sends packets with progressively increasing TTL values (1, 2, 3, ...) and each router that drops the packet (TTL=0) sends back its IP address in the ICMP Time Exceeded message.</p>



```bash
/* Traceroute algorithm */
Round 1: Send 3 packets with TTL=1
  → First router decrements to 0, drops, sends ICMP Time Exceeded
  → Reveal: first hop IP = 192.168.1.1 (your gateway)

Round 2: Send 3 packets with TTL=2
  → Second router decrements to 0, drops, sends ICMP Time Exceeded
  → Reveal: second hop IP = 10.10.1.1 (ISP edge router)

Round 3: Send 3 packets with TTL=3
  → Third router... and so on until destination replies

/* Two implementations */
traceroute on Linux: sends UDP packets to high port (33434+)
                     destination replies with ICMP Port Unreachable (type 3, code 3)
tracert   on Windows: sends ICMP Echo Requests
                     destination replies with Echo Reply (type 0)

/* Run it */
$ traceroute -n 8.8.8.8    # -n skips DNS resolution (faster)
$ traceroute -I 8.8.8.8    # -I uses ICMP instead of UDP
$ mtr 8.8.8.8              # live updating traceroute
```



<p><strong>Interpreting traceroute output:</strong></p>
<ul>
<li><code>* * *</code> — router doesn't respond to probes (rate-limited or blocks ICMP) — does NOT mean the path is broken there</li>
<li>Increasing RTT — normal as you move further away</li>
<li>RTT jumping down — ICMP is rate-limited and TTL-exceeded replies travel a shorter path back</li>
<li>Asymmetric routing — forward and return path may be different (explains apparent RTT anomalies)</li>
</ul>
  </div>
</div>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>ICMP and NGFW — What to Allow, What to Block</h3><span class="tag tag-red">NGFW POLICY</span></div>
  <div class="cp-body">
<p>A common mistake is to block all ICMP at the firewall. This breaks PMTUD and troubleshooting. Here's the correct NGFW policy for ICMP:</p>
<table class="icmp-table">
<thead><tr><th>ICMP Type/Code</th><th>Direction</th><th>NGFW Action</th><th>Reason</th></tr></thead>
<tbody>
<tr><td>Type 8 (Echo Request)</td><td>Inbound from internet</td><td>Block or rate-limit</td><td>Reduces attack surface, prevents mapping</td></tr>
<tr><td>Type 0 (Echo Reply)</td><td>Inbound (reply to outbound ping)</td><td>Allow (stateful)</td><td>Return traffic for initiated pings</td></tr>
<tr><td>Type 3, Code 4 (Frag Needed)</td><td>Inbound</td><td><strong>Always allow</strong></td><td>PMTUD — blocking this breaks connections</td></tr>
<tr><td>Type 3, Code 0-3 (Dest Unreach)</td><td>Inbound</td><td>Allow (stateful)</td><td>Error replies for existing connections</td></tr>
<tr><td>Type 11 (TTL Exceeded)</td><td>Inbound</td><td>Allow</td><td>Traceroute return path, debugging</td></tr>
<tr><td>Type 5 (Redirect)</td><td>Inbound</td><td><strong>Block</strong></td><td>ICMP redirect attacks — can reroute traffic</td></tr>
<tr><td>All ICMP</td><td>Outbound</td><td>Allow</td><td>Internal users need full diagnostic capability</td></tr>
</tbody>
</table>
  </div>
</div>
</div>
<!-- ════════════ TAB 8 — LABS ════════════ -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Dissect an IPv4 Header with Scapy and Wireshark</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Craft raw IP packets with specific field values and observe exactly how each field appears in Wireshark. Build deep familiarity with every byte of the IP header.</p>
<div class="lab-step"><div class="sn">1</div><div>Install Scapy: <code>pip3 install scapy</code>. Open Python3 as root: <code>sudo python3</code>. Import: <code>from scapy.all import *</code>.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Construct a minimal IP packet and inspect its fields: <code>p = IP(dst="8.8.8.8") / ICMP()</code> then <code>p.show()</code>. Observe every field Scapy has automatically set: version=4, ihl=5, ttl=64, proto=1 (ICMP), src (your IP), dst (8.8.8.8).</div></div>
<div class="lab-step"><div class="sn">3</div><div>Examine the raw bytes: <code>bytes(p)</code>. Count them — 20 bytes of IP header + 8 bytes ICMP = 28 bytes. Identify which bytes correspond to which fields (e.g., bytes 8–9 = TTL + Protocol).</div></div>
<div class="lab-step"><div class="sn">4</div><div>Start a Wireshark capture. Send the packet: <code>send(p)</code>. Find it in Wireshark. Expand the Internet Protocol layer. Verify every field matches what Scapy showed.</div></div>
<div class="lab-step"><div class="sn">5</div><div>Now deliberately set unusual field values and observe: <code>p = IP(dst="8.8.8.8", ttl=1, flags="DF", id=0xBEEF) / ICMP()</code>. Send it. In Wireshark: (a) Does TTL appear as 1? (b) Is the DF flag set? (c) Is the Identification 0xBEEF (decimal 48879)? (d) What ICMP error did you get back — Time Exceeded?</div></div>
<div class="lab-step"><div class="sn">6</div><div><strong>Bonus — Hexdump analysis:</strong> <code>hexdump(p)</code> in Scapy shows the raw hex. Manually decode the first 20 bytes: byte 0 = version+IHL (0x45 = version 4, IHL 5), bytes 2-3 = total length, byte 8 = TTL, byte 9 = protocol. Cross-reference with the IP header diagram in Tab 1.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Subnetting Practice — Design an NGFW Network</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Design a complete network layout for an NGFW deployment from scratch using subnetting. This simulates real-world work.</p>
<div class="lab-step"><div class="sn">1</div><div><strong>Task:</strong> You have the network <code>10.0.0.0/16</code> and need to create: (a) Inside LAN for 500 hosts, (b) DMZ for 50 servers, (c) Management network for 20 devices, (d) NGFW to router link (2 hosts only). Design subnets with the minimum waste. Calculate network address, mask, broadcast, first host, last host for each.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Write the answer before checking. Then verify using: <code>python3 -c "import ipaddress; n = ipaddress.ip_network('10.0.0.0/23'); print(list(n.hosts())[0], list(n.hosts())[-1], n.broadcast_address)"</code>. Use Python's <code>ipaddress</code> module to validate all your subnet calculations.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Configure your subnets on Linux loopback interfaces to test them: <code>sudo ip addr add 10.0.0.1/23 dev lo label lo:0</code>. Add routes for each subnet: <code>sudo ip route add 10.0.2.0/25 dev lo</code>. Verify routing with <code>ip route get 10.0.2.50</code>.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Write iptables rules reflecting your NGFW policy between zones: allow all from Inside LAN to internet (MASQUERADE), allow only HTTP/HTTPS from internet to DMZ, deny Inside LAN to DMZ except port 443, deny all to Management except SSH from specific host. Verify with <code>iptables -L -n -v</code>.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>ICMP and Traceroute Analysis</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Capture and fully decode ICMP messages including ping, Time Exceeded (traceroute), and Destination Unreachable. Understand the complete ICMP interaction with IP.</p>
<div class="lab-step"><div class="sn">1</div><div>Start Wireshark capture with filter <code>icmp</code>. Run: <code>ping -c 4 8.8.8.8</code>. Identify Type 8 (Echo Request) and Type 0 (Echo Reply) packets. In the hex dump, find: byte 20 = ICMP Type, byte 21 = ICMP Code, bytes 22-23 = Checksum, bytes 24-27 = Identifier + Sequence number.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Run traceroute while capturing: <code>sudo traceroute -n -I 8.8.8.8</code>. Capture Type 11 (Time Exceeded) replies from intermediate routers. Expand an ICMP Time Exceeded packet — notice it includes the first 8 bytes of the original IP payload (the original IP header is embedded) so the sender knows which packet caused the error.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Generate a Destination Unreachable (Port Unreachable): <code>nc -u 8.8.8.8 9999</code> then type anything and press Enter. You'll get an ICMP Type 3, Code 3 (Port Unreachable) back from Google's server since nothing listens on UDP 9999. Capture and decode it in Wireshark.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Use Scapy to build a custom ICMP packet: force a specific TTL to trigger Time Exceeded from a known router hop. Use <code>ans, unans = sr(IP(dst="8.8.8.8", ttl=3)/ICMP(), timeout=2)</code>. Then <code>ans.show()</code> — you'll see the response from hop 3 on your path to 8.8.8.8.</div></div>
<div class="lab-step"><div class="sn">5</div><div><strong>Bonus:</strong> Write a 20-line Python traceroute using Scapy. Send ICMP with TTL=1,2,3,... until you reach the destination or TTL=30. Print the IP of each responding router. This is the core of how traceroute works — you're implementing it from scratch.</div></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 9 — CHECKLIST ════════════ -->
<div id="t9" class="tab-pane">
<p class="sep">M03 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain IP's three core jobs: logical addressing, fragmentation, best-effort delivery</li>
  <li>Know the IPv4 header is 20 bytes minimum (5 × 32-bit rows) and can draw it from memory</li>
  <li>Know every header field: Version, IHL, DSCP/ECN, Total Length, ID, Flags, Fragment Offset, TTL, Protocol, Checksum, Src IP, Dst IP</li>
  <li>Know the key Protocol field values: 1=ICMP, 6=TCP, 17=UDP, 47=GRE, 50=ESP, 89=OSPF</li>
  <li>Know how to find the payload start using IHL: payload_offset = IHL × 4</li>
  <li>Know the two flag bits: DF (Don't Fragment) and MF (More Fragments) and what each does</li>
  <li>Know the three classful address classes (A/B/C) and their default masks (/8, /16, /24)</li>
  <li>Can convert between dotted-decimal and CIDR notation for any prefix length</li>
  <li>Can manually calculate network address, broadcast address, first host, last host, and host count for any given CIDR prefix</li>
  <li>Can subnet a given network into N equal subnets by hand using the block-size method</li>
  <li>Know all RFC 1918 private ranges by heart: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16</li>
  <li>Know at least 8 special address ranges: loopback, link-local, multicast, broadcast, shared (CGN), TEST-NETs</li>
  <li>Understand bogon filtering and can list the key ranges an NGFW should drop at the internet perimeter</li>
  <li>Know how TTL works: decremented at each router, ICMP Time Exceeded when 0, default values per OS</li>
  <li>Understand how LPM routing works: router looks up destination IP in FIB, most specific match wins</li>
  <li>Know what a router does and does NOT modify: decrements TTL, recomputes checksum, rewrites Ethernet header — never touches IP src/dst or payload</li>
  <li>Can explain IP fragmentation: what triggers it, Identification/MF/Offset fields, reassembly at destination only</li>
  <li>Understand Path MTU Discovery (PMTUD): DF=1 + ICMP Type 3 Code 4 — and why blocking ICMP breaks it</li>
  <li>Know key ICMP types: 0 (Echo Reply), 3 (Unreachable), 5 (Redirect), 8 (Echo Request), 11 (Time Exceeded)</li>
  <li>Know which ICMP types to allow at NGFW: always allow Type 3 Code 4, block Type 5 (Redirect)</li>
  <li>Can explain how traceroute works: sends TTL=1,2,3... probes, collects ICMP Time Exceeded from each hop</li>
  <li>Completed Lab 1: crafted IPv4 packets in Scapy, decoded header bytes, verified fields in Wireshark</li>
  <li>Completed Lab 2: designed an NGFW subnet layout for 4 zones, configured on Linux, wrote iptables rules</li>
  <li>Completed Lab 3: captured ping, traceroute, and Destination Unreachable ICMP messages, wrote custom traceroute in Scapy</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M04 - IPv6</strong>. You now have deep IPv4 knowledge. IPv6 keeps the same layered approach but changes addressing fundamentally — 128-bit addresses, no broadcast, mandatory SLAAC, ICMPv6 replaces ARP. Much of what you learned here maps directly.</p>
</div>
</div>
<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/networking-mastery/m02-ethernet-l2/">← M02 Ethernet and L2</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m04-ipv6/">Next: M04 - IPv6 →</a>
</div>
<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
</script>
