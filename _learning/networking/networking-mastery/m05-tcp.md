---
layout: default
title: "M05 - TCP Internals"
permalink: /learning/networking-mastery/m05-tcp/
---

<style>
/* ── Base ───────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 35%,#0a3a50 70%,#0f6e56 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0;
}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#7ab8d8;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#a8d8e8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#c8ecf8}

/* Tabs */
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#5dd6c8;border-bottom-color:#5dd6c8}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #0f6e56}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#a8e8d8;white-space:pre}
.cm{color:#4a8a70}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}

/* Insight / warning / note */
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
.note strong{color:#1a3a5c}
[data-theme=dark] .note strong{color:#7ab8d8}

/* Analogy */
.analogy{background:linear-gradient(135deg,#eef8ff,#e4f4f0);border:1.5px solid #80c8d8;border-radius:10px;padding:1.1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .analogy{background:linear-gradient(135deg,#0a1820,#0a2020);border-color:#306880}
.analogy-title{font-size:.72rem;font-family:monospace;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#0a3a50;margin-bottom:.5rem}
[data-theme=dark] .analogy-title{color:#7ab8d8}
.analogy p{font-size:.88rem;line-height:1.7;color:var(--text-color,#222);margin:0}

/* TCP Header diagram */
.hdr-diagram{margin:1rem 0;overflow-x:auto}
.hdr-row{display:flex;gap:2px;min-width:580px;margin-bottom:3px;align-items:stretch}
.hdr-label{font-size:.7rem;font-family:monospace;min-width:76px;display:flex;align-items:center;color:var(--light-text,#666);flex-shrink:0;padding-right:4px}
.hf{border-radius:5px;padding:7px 5px;font-size:.7rem;font-weight:600;text-align:center;border:1.5px solid transparent;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1.3}
.hf-sp {background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c}
.hf-dp {background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c}
.hf-sq {background:#e0f0ee;border-color:#90c8b8;color:#0a3a30}
.hf-ak {background:#e2f0e8;border-color:#a0d0a0;color:#1a4a1a}
.hf-fl {background:#faeee4;border-color:#e8b090;color:#6a2800}
.hf-wn {background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c}
.hf-ck {background:#faeaea;border-color:#e8b0b0;color:#6c1a1a}
.hf-ug {background:#fdf4dc;border-color:#e8c870;color:#5a3800}
.hf-op {background:#f0f0f0;border-color:#c0c0c0;color:#555}
.hf-bytes{font-size:.62rem;font-weight:400;opacity:.8;margin-top:2px}

/* Flag bits */
.flag-row{display:flex;gap:4px;flex-wrap:wrap;margin:.8rem 0}
.flag-bit{border-radius:6px;padding:8px 10px;text-align:center;border:1.5px solid;min-width:52px}
.flag-bit-name{font-size:.8rem;font-weight:700;font-family:monospace}
.flag-bit-desc{font-size:.65rem;color:var(--light-text,#666);margin-top:2px;line-height:1.3}
.fb-cwr{background:#fdf4dc;border-color:#e8c870;color:#5a3800}
.fb-ece{background:#fdf4dc;border-color:#e8c870;color:#5a3800}
.fb-urg{background:#f0f0f0;border-color:#c0c0c0;color:#555}
.fb-ack{background:#e2f0e8;border-color:#a0d0a0;color:#1a4a1a}
.fb-psh{background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c}
.fb-rst{background:#faeaea;border-color:#e8b0b0;color:#6c1a1a}
.fb-syn{background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c}
.fb-fin{background:#e0f0ee;border-color:#90c8b8;color:#0a3a30}

/* Sequence diagram */
.seq-diagram{display:grid;grid-template-columns:1fr auto 1fr;gap:0;margin:1rem 0;overflow-x:auto;min-width:420px}
.seq-actor{padding:.5rem 1rem;text-align:center;font-size:.82rem;font-weight:700;font-family:monospace;border-radius:7px 7px 0 0}
.seq-spacer{width:80px}
.seq-timeline{display:flex;flex-direction:column;align-items:center}
.seq-line{width:2px;flex:1;min-height:10px}
.seq-row{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:0;margin:2px 0}
.seq-left{text-align:right;padding-right:8px;font-size:.78rem;font-family:monospace;font-weight:600}
.seq-right{text-align:left;padding-left:8px;font-size:.78rem;font-family:monospace;font-weight:600}
.seq-arrow-lr{text-align:center;font-size:.72rem;white-space:nowrap;padding:2px 4px;border-radius:4px}
.seq-note{grid-column:1/-1;text-align:center;font-size:.72rem;color:var(--light-text,#666);padding:3px 0;font-style:italic}
.seq-box{border-radius:4px;padding:2px 8px;font-size:.72rem;font-family:monospace;font-weight:600;white-space:nowrap}

/* State machine */
.states-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:.6rem;margin:1rem 0}
.state-box{border-radius:8px;padding:.75rem 1rem;border:1.5px solid var(--border-color,#e0e0e0);background:var(--card-bg,#fff)}
.state-name{font-size:.82rem;font-weight:700;font-family:monospace;margin-bottom:.3rem}
.state-desc{font-size:.78rem;color:var(--text-color,#444);line-height:1.55}

/* Window / buffer visual */
.window-vis{margin:1rem 0;overflow-x:auto}
.wv-row{display:flex;gap:2px;min-width:500px;align-items:stretch;margin-bottom:4px}
.wv-label{font-size:.72rem;font-family:monospace;min-width:100px;display:flex;align-items:center;color:var(--light-text,#666);flex-shrink:0}
.wv-seg{border-radius:5px;padding:6px 4px;font-size:.68rem;font-weight:600;text-align:center;border:1.5px solid transparent;display:flex;align-items:center;justify-content:center}
.ws-sent-acked{background:#e2f0e8;border-color:#a0d0a0;color:#1a4a1a}
.ws-sent-unacked{background:#fdf4dc;border-color:#e8c870;color:#5a3800}
.ws-can-send{background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c}
.ws-no-send{background:var(--bg-color,#f0f0f0);border-color:var(--border-color,#e0e0e0);color:var(--light-text,#999)}
.ws-recv{background:#e0f0ee;border-color:#90c8b8;color:#0a3a30}
.ws-ooo{background:#faeee4;border-color:#e8b090;color:#6a2800}
.ws-empty{background:var(--bg-color,#f8f8f8);border-color:var(--border-color,#eee);color:var(--light-text,#bbb)}

/* Congestion diagram */
.congestion-phases{display:flex;gap:0;margin:1rem 0;overflow-x:auto;border-radius:8px;overflow:hidden;border:1.5px solid var(--border-color,#e0e0e0)}
.cong-phase{flex:1;padding:.8rem .6rem;text-align:center;min-width:110px}
.cong-phase-name{font-size:.75rem;font-weight:700;font-family:monospace;margin-bottom:.3rem}
.cong-phase-desc{font-size:.7rem;color:var(--text-color,#444);line-height:1.5}

/* Tables */
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#0f6e56}

/* Flow steps */
.flow-list{display:flex;flex-direction:column;gap:0;margin:1rem 0}
.fl-step{display:flex;gap:14px;padding:10px 14px;border-left:2px solid var(--border-color,#e0e0e0);margin-left:14px;position:relative}
.fl-step::before{content:attr(data-n);position:absolute;left:-14px;top:12px;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;color:#fff;background:var(--sc,#1a3a5c)}
.fl-step:last-child{border-left-color:transparent}
.fl-title{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin-bottom:.25rem}
.fl-detail{font-size:.85rem;color:var(--text-color,#444);line-height:1.6}
.fl-code{font-family:monospace;font-size:.78rem;display:inline-block;background:#0a1628;color:#5dd6c8;padding:2px 8px;border-radius:4px;margin-top:.3rem}

/* Two-col */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}

/* Lab box */
.lab-box{border:2px solid #0f6e56;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#0f6e56;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#0f6e56;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}

/* Checklist */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#0f6e56;margin-top:-.05rem}

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
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 2 · MODULE 05 · WEEKS 4–5</div>
  <div class="mod-title">⚡ TCP Internals</div>
  <div class="mod-subtitle">3-way handshake · State machine · Sequence numbers · Flow control · Congestion control · SACK · Timers</div>
  <div class="mod-pills">
    <span class="mod-pill">Beginner → Intermediate</span>
    <span class="mod-pill">Prerequisite: M03 IPv4</span>
    <span class="mod-pill">RFC 793 + RFC 9293</span>
    <span class="mod-pill">Most Critical Transport Protocol</span>
    <span class="mod-pill">3 Labs</span>
  </div>
</div>

<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">What is TCP?</button>
  <button class="tab-btn" onclick="vt(event,'t1')">TCP Header</button>
  <button class="tab-btn" onclick="vt(event,'t2')">3-Way Handshake</button>
  <button class="tab-btn" onclick="vt(event,'t3')">State Machine</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Sequence Numbers</button>
  <button class="tab-btn" onclick="vt(event,'t5')">Flow Control</button>
  <button class="tab-btn" onclick="vt(event,'t6')">Congestion Control</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Timers and SACK</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Connection Teardown</button>
  <button class="tab-btn" onclick="vt(event,'t9')">NGFW and TCP</button>
  <button class="tab-btn" onclick="vt(event,'ta')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'tb')">Checklist</button>
</div>


<!-- ════════════ TAB 0 — WHAT IS TCP ════════════ -->
<div id="t0" class="tab-pane active">
<p class="sep">TCP — RELIABLE, ORDERED, BIDIRECTIONAL BYTE STREAMS</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📡</span><h3>What TCP Guarantees — and What It Doesn't</h3><span class="tag tag-teal">OVERVIEW</span></div>
  <div class="cp-body">
    <p>TCP (Transmission Control Protocol, RFC 793 / RFC 9293) is Layer 4's workhorse. It takes IP's unreliable, unordered packet delivery and builds a <strong>reliable, ordered, bidirectional byte stream</strong> on top of it. Every major application protocol — HTTP, HTTPS, SSH, SMTP, FTP — runs over TCP because reliability matters more than raw speed for those use cases.</p>
    <p><strong>What TCP guarantees:</strong></p>
    <ul>
      <li><strong>Reliability</strong> — every byte sent will be received, or the sender will know it failed. If a packet is lost, TCP detects it and retransmits automatically</li>
      <li><strong>Ordering</strong> — bytes arrive in the same order they were sent, even if packets arrive out of order in transit</li>
      <li><strong>No duplication</strong> — TCP detects and discards duplicate packets</li>
      <li><strong>Error detection</strong> — checksum on every segment</li>
      <li><strong>Flow control</strong> — sender doesn't overwhelm receiver's buffer</li>
      <li><strong>Congestion control</strong> — sender adapts to network capacity, doesn't collapse the network</li>
    </ul>
    <p><strong>What TCP does NOT guarantee:</strong></p>
    <ul>
      <li><strong>Timing / latency</strong> — retransmissions add unpredictable delay</li>
      <li><strong>Bandwidth</strong> — TCP adapts to available capacity, never reserves it</li>
      <li><strong>Message boundaries</strong> — TCP is a <em>stream</em>, not a message protocol. If you send "Hello" and "World" as two separate write() calls, the receiver may get "HelloWorld" in one read() or "He" and "lloWorld" in two. Applications must implement their own framing</li>
    </ul>
  </div>
</div>

<div class="analogy">
  <div class="analogy-title">📞 Analogy — A Phone Call vs Postcards</div>
  <p>UDP is like sending postcards — you write one, drop it in the postbox, and hope it arrives. No confirmation, no order guarantee, no retry. TCP is like a phone call: first you establish the call (3-way handshake), then both parties speak in turn and confirm they heard each other ("uh-huh, go on"), and if one side goes silent the other says "hello? are you still there?" (keepalive). When the call ends, both sides say goodbye properly (4-way teardown). This setup and teardown overhead is why TCP is slower for small one-shot queries — but the reliability is worth it for file transfers, web pages, and anything where missing data is unacceptable.</p>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚖️</span><h3>TCP vs UDP — When to Use Which</h3><span class="tag tag-blue">COMPARISON</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Property</th><th>TCP</th><th>UDP</th></tr></thead>
      <tbody>
        <tr><td>Connection</td><td>Connection-oriented (3-way handshake)</td><td>Connectionless — fire and forget</td></tr>
        <tr><td>Reliability</td><td>Guaranteed delivery + retransmission</td><td>Best-effort — no retransmission</td></tr>
        <tr><td>Ordering</td><td>In-order delivery guaranteed</td><td>Packets may arrive out of order</td></tr>
        <tr><td>Speed</td><td>Slower — overhead for reliability</td><td>Faster — minimal overhead</td></tr>
        <tr><td>Header size</td><td>20–60 bytes</td><td>8 bytes</td></tr>
        <tr><td>Flow control</td><td>Yes — sliding window</td><td>No</td></tr>
        <tr><td>Congestion control</td><td>Yes — reduces sending rate under congestion</td><td>No — keeps sending regardless</td></tr>
        <tr><td>Use cases</td><td>HTTP/HTTPS, SSH, SMTP, FTP, database</td><td>DNS, VoIP, video streaming, gaming, QUIC</td></tr>
      </tbody>
    </table>
    <div class="ins"><p>💡 <strong>NGFW relevance:</strong> TCP is the dominant protocol for web traffic (HTTP/HTTPS), management traffic (SSH), and email (SMTP). Your NGFW must maintain connection state for every TCP session — tracking sequence numbers, connection phase (handshake/established/closing), and detecting anomalies. UDP sessions are tracked differently (timeout-based, no handshake state). Understanding TCP deeply is essential for building correct stateful inspection.</p></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 1 — TCP HEADER ════════════ -->
<div id="t1" class="tab-pane">
<p class="sep">TCP HEADER — 20 BYTES MINIMUM, UP TO 60 BYTES WITH OPTIONS</p>

<div class="hdr-diagram">
  <div class="hdr-row">
    <div class="hdr-label">Row 1</div>
    <div class="hf hf-sp" style="flex:2">Source Port<div class="hf-bytes">16 bits</div></div>
    <div class="hf hf-dp" style="flex:2">Destination Port<div class="hf-bytes">16 bits</div></div>
  </div>
  <div class="hdr-row">
    <div class="hdr-label">Row 2</div>
    <div class="hf hf-sq" style="flex:4">Sequence Number<div class="hf-bytes">32 bits</div></div>
  </div>
  <div class="hdr-row">
    <div class="hdr-label">Row 3</div>
    <div class="hf hf-ak" style="flex:4">Acknowledgement Number<div class="hf-bytes">32 bits</div></div>
  </div>
  <div class="hdr-row">
    <div class="hdr-label">Row 4</div>
    <div class="hf hf-fl" style="flex:.6">Data Offset<div class="hf-bytes">4 bits</div></div>
    <div class="hf hf-fl" style="flex:.4">Res<div class="hf-bytes">3b</div></div>
    <div class="hf hf-fl" style="flex:1.6">Flags: CWR ECE URG ACK PSH RST SYN FIN<div class="hf-bytes">9 bits</div></div>
    <div class="hf hf-wn" style="flex:2">Window Size<div class="hf-bytes">16 bits</div></div>
  </div>
  <div class="hdr-row">
    <div class="hdr-label">Row 5</div>
    <div class="hf hf-ck" style="flex:2">Checksum<div class="hf-bytes">16 bits</div></div>
    <div class="hf hf-ug" style="flex:2">Urgent Pointer<div class="hf-bytes">16 bits</div></div>
  </div>
  <div class="hdr-row">
    <div class="hdr-label">Row 6+</div>
    <div class="hf hf-op" style="flex:4">Options (if Data Offset &gt; 5) + Padding<div class="hf-bytes">0–40 bytes — MSS, SACK, Timestamps, Window Scale</div></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Every Field Explained</h3><span class="tag tag-blue">FIELD REFERENCE</span></div>
  <div class="cp-body">

    <h4>Source Port and Destination Port (16 bits each)</h4>
    <p>Port numbers identify the application on each end. Combined with IP addresses, they form the <strong>5-tuple</strong> that uniquely identifies a TCP connection: (src_ip, src_port, dst_ip, dst_port, protocol=TCP). Well-known ports: 80=HTTP, 443=HTTPS, 22=SSH, 25=SMTP, 53=DNS-TCP, 3306=MySQL. The client uses an <strong>ephemeral port</strong> (typically 49152–65535) assigned randomly by the OS.</p>

    <h4>Sequence Number (32 bits)</h4>
    <p>Identifies the position of the first byte of data in this segment within the entire byte stream. The sequence number space is 0 to 2³²−1 (wraps around). The Initial Sequence Number (ISN) is chosen randomly at connection setup — not starting at 0 — to prevent stale segments from old connections being confused with new ones. In a SYN segment, the sequence number is the ISN itself (no data yet).</p>

    <h4>Acknowledgement Number (32 bits)</h4>
    <p>The sequence number of the <strong>next byte the receiver expects</strong> from the sender. This acknowledges all bytes up to (but not including) this number. For example, if the receiver has successfully received bytes 0–999, it sends ACK=1000 meaning "I have everything up to 999, send me 1000 next". ACK is only valid when the ACK flag is set.</p>

    <h4>Data Offset (4 bits)</h4>
    <p>TCP header length in 32-bit words — same concept as IPv4's IHL. Minimum 5 (20 bytes). Maximum 15 (60 bytes). Tells the receiver where the payload data starts: data_offset_bytes = data_offset × 4.</p>

    <h4>TCP Flags (9 bits) — The Most Important Field for NGFW</h4>
    <div class="flag-row">
      <div class="flag-bit fb-cwr"><div class="flag-bit-name">CWR</div><div class="flag-bit-desc">Congestion Window Reduced — ECN response</div></div>
      <div class="flag-bit fb-ece"><div class="flag-bit-name">ECE</div><div class="flag-bit-desc">ECN Echo — congestion signal received</div></div>
      <div class="flag-bit fb-urg"><div class="flag-bit-name">URG</div><div class="flag-bit-desc">Urgent Pointer is valid (rarely used)</div></div>
      <div class="flag-bit fb-ack"><div class="flag-bit-name">ACK</div><div class="flag-bit-desc">ACK number is valid — set on all except initial SYN</div></div>
      <div class="flag-bit fb-psh"><div class="flag-bit-name">PSH</div><div class="flag-bit-desc">Push — receiver should flush buffer to app immediately</div></div>
      <div class="flag-bit fb-rst"><div class="flag-bit-name">RST</div><div class="flag-bit-desc">Reset — abortive connection close</div></div>
      <div class="flag-bit fb-syn"><div class="flag-bit-name">SYN</div><div class="flag-bit-desc">Synchronise — connection initiation</div></div>
      <div class="flag-bit fb-fin"><div class="flag-bit-name">FIN</div><div class="flag-bit-desc">Finish — orderly connection close</div></div>
    </div>
    <p>Flag combinations reveal connection phase: <strong>SYN only</strong> = new connection attempt; <strong>SYN+ACK</strong> = server accepting; <strong>ACK only</strong> = data transfer; <strong>FIN+ACK</strong> = graceful close; <strong>RST</strong> = abort. Your NGFW inspects these flags to track connection state in its connection table.</p>

    <h4>Window Size (16 bits)</h4>
    <p>Advertises how many bytes the receiver can accept in its buffer right now. This is the foundation of TCP flow control — the sender must not send more unacknowledged data than the receiver's window allows. Scaled by the Window Scale option (up to ×65535) for high-bandwidth links. We cover this in the Flow Control tab.</p>

    <h4>Checksum (16 bits)</h4>
    <p>Computed over a "pseudo-header" (IP src, IP dst, Protocol=6, TCP length) plus the entire TCP header and payload. Detects corruption. The pseudo-header inclusion means the checksum also validates that the segment reached the correct destination IP — no mis-delivery.</p>

    <h4>Key TCP Options</h4>
    <table class="t-table">
      <thead><tr><th>Option</th><th>Kind</th><th>Purpose</th><th>NGFW Impact</th></tr></thead>
      <tbody>
        <tr><td>MSS</td><td>2</td><td>Maximum Segment Size — largest payload sender will send</td><td>NGFW can reduce MSS to avoid fragmentation (MSS clamping)</td></tr>
        <tr><td>Window Scale</td><td>3</td><td>Multiplier for Window Size (2^scale, up to ×65535)</td><td>Must track for correct window calculation</td></tr>
        <tr><td>SACK Permitted</td><td>4</td><td>Signals both sides support Selective ACK</td><td>Signals need to track SACK blocks</td></tr>
        <tr><td>SACK</td><td>5</td><td>Reports which out-of-order blocks were received</td><td>Must parse for correct retransmit tracking</td></tr>
        <tr><td>Timestamps</td><td>8</td><td>RTT measurement + PAWS (protect against wrapped seqs)</td><td>Used for RTT monitoring in NGFW analytics</td></tr>
        <tr><td>TFO (Fast Open)</td><td>34</td><td>Send data in SYN packet (1-RTT connection setup)</td><td>NGFW must parse data-in-SYN for DPI</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>


<!-- ════════════ TAB 2 — 3-WAY HANDSHAKE ════════════ -->
<div id="t2" class="tab-pane">
<p class="sep">THE THREE-WAY HANDSHAKE — CONNECTION ESTABLISHMENT</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🤝</span><h3>Why Three Steps?</h3><span class="tag tag-teal">CONCEPT</span></div>
  <div class="cp-body">
    <p>A TCP connection needs both sides to agree on two things before data can flow: (1) the connection exists, and (2) both sides know each other's <strong>initial sequence numbers (ISN)</strong> so they can properly track bytes. The three-way handshake achieves both with the minimum number of round trips.</p>
    <p>Two steps (SYN → SYN+ACK) would let the server know the client's ISN, but the client wouldn't know the server acknowledged its SYN. Three steps (SYN → SYN+ACK → ACK) confirms both sides have exchanged and acknowledged ISNs, establishing a reliable bidirectional channel.</p>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📊</span><h3>The Handshake Step by Step</h3><span class="tag tag-blue">SEQUENCE DIAGRAM</span></div>
  <div class="cp-body">
    <div class="seq-diagram">
      <div class="seq-actor" style="background:#e8f1f9;color:#1a3a5c">Client</div>
      <div class="seq-spacer"></div>
      <div class="seq-actor" style="background:#e0f0ee;color:#0a3a30">Server</div>

      <!-- Step 1: SYN -->
      <div style="display:flex;flex-direction:column;align-items:flex-end;padding-top:8px">
        <div class="seq-box" style="background:#e8f1f9;border:1.5px solid #b0ccec;color:#1a3a5c">SYN<br><span style="font-size:.65rem;font-weight:400">seq=x ISN</span></div>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;padding-top:8px">
        <div style="width:80px;border-top:2px solid #1a3a5c;position:relative">
          <span style="position:absolute;right:-6px;top:-8px;color:#1a3a5c;font-size:1rem">▶</span>
        </div>
      </div>
      <div style="padding-top:8px">
        <div style="font-size:.72rem;color:var(--light-text,#666)">SYN received</div>
      </div>

      <!-- Step 2: SYN+ACK -->
      <div style="padding-top:10px">
        <div style="font-size:.72rem;color:var(--light-text,#666)">SYN+ACK received</div>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;padding-top:10px">
        <div style="width:80px;border-top:2px solid #0f6e56;position:relative">
          <span style="position:absolute;left:-6px;top:-8px;color:#0f6e56;font-size:1rem">◀</span>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;align-items:flex-start;padding-top:10px">
        <div class="seq-box" style="background:#e0f0ee;border:1.5px solid #90c8b8;color:#0a3a30">SYN+ACK<br><span style="font-size:.65rem;font-weight:400">seq=y ack=x+1</span></div>
      </div>

      <!-- Step 3: ACK -->
      <div style="display:flex;flex-direction:column;align-items:flex-end;padding-top:10px">
        <div class="seq-box" style="background:#e2f0e8;border:1.5px solid #a0d0a0;color:#1a4a1a">ACK<br><span style="font-size:.65rem;font-weight:400">seq=x+1 ack=y+1</span></div>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;padding-top:10px">
        <div style="width:80px;border-top:2px solid #1a5a1a;position:relative">
          <span style="position:absolute;right:-6px;top:-8px;color:#1a5a1a;font-size:1rem">▶</span>
        </div>
      </div>
      <div style="padding-top:10px">
        <div style="font-size:.72rem;color:var(--light-text,#666)">ACK received</div>
      </div>

      <!-- ESTABLISHED -->
      <div style="padding-top:10px;text-align:right">
        <div style="font-size:.72rem;font-family:monospace;font-weight:700;color:#1a5a1a">ESTABLISHED ✓</div>
      </div>
      <div></div>
      <div style="padding-top:10px">
        <div style="font-size:.72rem;font-family:monospace;font-weight:700;color:#1a5a1a">ESTABLISHED ✓</div>
      </div>
    </div>

<div class="cb"><pre><span class="cm">/* Step 1 — Client sends SYN */</span>
Flags:  SYN
Seq:    x        <span class="cm"># randomly chosen ISN — e.g. 1,000,000</span>
Ack:    0        <span class="cm"># ACK flag not set — nothing to ack yet</span>
Options: MSS=1460, SACK permitted, Window Scale=7, Timestamps

<span class="cm">/* Step 2 — Server sends SYN+ACK */</span>
Flags:  SYN, ACK
Seq:    y        <span class="cm"># server's own randomly chosen ISN — e.g. 5,000,000</span>
Ack:    x+1      <span class="cm"># "I received your SYN (which consumed 1 seq byte), send me x+1 next"</span>
Options: MSS=1460, SACK permitted, Window Scale=9, Timestamps

<span class="cm">/* Step 3 — Client sends ACK */</span>
Flags:  ACK
Seq:    x+1      <span class="cm"># client's next byte</span>
Ack:    y+1      <span class="cm"># "I received your SYN, send me y+1 next"</span>
<span class="cm"># Connection is now ESTABLISHED on both sides</span>
<span class="cm"># Client may include data in this segment (TCP Fast Open)</span></pre></div>

    <div class="ins"><p>💡 <strong>Why random ISN?</strong> If ISN always started at 0, an attacker could inject forged segments into an existing connection — they just need to guess the current sequence number, which is trivial if it started from 0. Random ISN makes it computationally infeasible to forge in-window segments.</p></div>
  </div>
</div>

<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>SYN Flood Attack and SYN Cookies</h3><span class="tag tag-red">SECURITY</span></div>
  <div class="cp-body">
    <p>A <strong>SYN flood</strong> is one of the oldest and most effective DoS attacks. The attacker sends thousands of SYN packets with spoofed source IPs. The server allocates state for each half-open connection, waiting for the final ACK that never comes. Eventually, the server's connection table fills up and it can't accept legitimate connections.</p>
    <p><strong>SYN Cookies</strong> (RFC 4987) solve this: instead of allocating state on SYN receipt, the server encodes the connection parameters (MSS, timestamp, etc.) into the initial sequence number (ISN) of the SYN+ACK. The state is "stored" in the sequence number itself. When the final ACK arrives, the server decodes the parameters from the ACK number and allocates state only then. No state is allocated for connections that never complete — SYN flood has no effect.</p>
<div class="cb"><pre><span class="cm"># Check if SYN cookies are enabled on Linux</span>
cat /proc/sys/net/ipv4/tcp_syncookies
<span class="cm"># 0 = disabled, 1 = enabled when backlog full, 2 = always enabled</span>

<span class="cm"># Enable permanently</span>
echo 1 > /proc/sys/net/ipv4/tcp_syncookies

<span class="cm"># NGFW-level SYN flood protection</span>
<span class="cm"># Rate-limit SYN packets per source IP per second</span>
<span class="cm"># Drop SYN packets exceeding threshold (e.g., >100 SYN/sec from one IP)</span>
<span class="cm"># TCP proxy: NGFW completes handshake on behalf of server, only forwards verified connections</span></pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 3 — STATE MACHINE ════════════ -->
<div id="t3" class="tab-pane">
<p class="sep">TCP STATE MACHINE — 11 STATES, EVERY TRANSITION</p>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>TCP States — What Each Means</h3><span class="tag tag-purple">STATE MACHINE</span></div>
  <div class="cp-body">
    <p>A TCP connection moves through a well-defined sequence of states. Your NGFW must track the state of every TCP connection in its connection table — this is the essence of "stateful inspection". A packet that doesn't match expected state transitions is suspicious or malicious.</p>
    <div class="states-grid">
      <div class="state-box" style="border-color:#c0c0c0">
        <div class="state-name" style="color:#555">CLOSED</div>
        <div class="state-desc">No connection. Initial and final state. No resources allocated.</div>
      </div>
      <div class="state-box" style="border-color:#b0ccec">
        <div class="state-name" style="color:#1a3a5c">LISTEN</div>
        <div class="state-desc">Server waiting for incoming SYN. Socket bound and listening.</div>
      </div>
      <div class="state-box" style="border-color:#90c8b8">
        <div class="state-name" style="color:#0a3a30">SYN_SENT</div>
        <div class="state-desc">Client sent SYN, waiting for SYN+ACK from server.</div>
      </div>
      <div class="state-box" style="border-color:#a0d0a0">
        <div class="state-name" style="color:#1a4a1a">SYN_RECEIVED</div>
        <div class="state-desc">Server received SYN, sent SYN+ACK, waiting for client's ACK.</div>
      </div>
      <div class="state-box" style="border-color:#0f6e56;background:#e0f0ee">
        <div class="state-name" style="color:#0a3a30">ESTABLISHED ✓</div>
        <div class="state-desc">Full duplex connection open. Data transfer in progress. This is the normal operating state.</div>
      </div>
      <div class="state-box" style="border-color:#c0a8e8">
        <div class="state-name" style="color:#3a1a6c">FIN_WAIT_1</div>
        <div class="state-desc">This side sent FIN, waiting for ACK or FIN+ACK.</div>
      </div>
      <div class="state-box" style="border-color:#c0a8e8">
        <div class="state-name" style="color:#3a1a6c">FIN_WAIT_2</div>
        <div class="state-desc">Our FIN acknowledged. Waiting for remote FIN.</div>
      </div>
      <div class="state-box" style="border-color:#e8c870">
        <div class="state-name" style="color:#5a3800">CLOSE_WAIT</div>
        <div class="state-desc">Remote side closed. Waiting for local app to close its side.</div>
      </div>
      <div class="state-box" style="border-color:#e8c870">
        <div class="state-name" style="color:#5a3800">CLOSING</div>
        <div class="state-desc">Both sides sent FIN simultaneously. Waiting for ACK.</div>
      </div>
      <div class="state-box" style="border-color:#e8c870">
        <div class="state-name" style="color:#5a3800">LAST_ACK</div>
        <div class="state-desc">Passive close side sent FIN, waiting for final ACK.</div>
      </div>
      <div class="state-box" style="border-color:#e8b0b0;background:#faeaea">
        <div class="state-name" style="color:#6c1a1a">TIME_WAIT</div>
        <div class="state-desc">Both FINs ACKed. Wait 2×MSL before CLOSED. Prevents stale segment confusion.</div>
      </div>
    </div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🗺️</span><h3>State Transitions — Full Diagram in Text</h3><span class="tag tag-blue">TRANSITIONS</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* CLIENT (active open) state transitions */</span>
CLOSED
  → app calls connect()                    → SYN_SENT
  → SYN_SENT  + receive SYN+ACK, send ACK → ESTABLISHED
  → SYN_SENT  + receive SYN (simultaneous) → SYN_RECEIVED

<span class="cm">/* SERVER (passive open) state transitions */</span>
CLOSED
  → app calls listen()                     → LISTEN
  → LISTEN    + receive SYN, send SYN+ACK  → SYN_RECEIVED
  → SYN_RECEIVED + receive ACK             → ESTABLISHED

<span class="cm">/* TEARDOWN — active close (initiating side) */</span>
ESTABLISHED
  → app calls close(), send FIN            → FIN_WAIT_1
  → FIN_WAIT_1 + receive ACK              → FIN_WAIT_2
  → FIN_WAIT_2 + receive FIN, send ACK    → TIME_WAIT
  → TIME_WAIT  + 2*MSL timeout            → CLOSED

<span class="cm">/* TEARDOWN — passive close (receiving side) */</span>
ESTABLISHED
  → receive FIN, send ACK                  → CLOSE_WAIT
  → CLOSE_WAIT + app calls close(), send FIN → LAST_ACK
  → LAST_ACK   + receive ACK               → CLOSED

<span class="cm">/* RST — abortive close (any state) */</span>
<span class="ck">any state</span>
  → receive RST or send RST                → CLOSED (immediately)

<span class="cm">/* Check states on Linux */</span>
ss -tn          <span class="cm"># show TCP connections with states</span>
ss -tn state established
ss -tn state time-wait | wc -l   <span class="cm"># count TIME_WAIT connections</span>
netstat -an | grep TCP</pre></div>

    <div class="warn"><p>⚠️ <strong>TIME_WAIT accumulation</strong> is a common production problem. Each connection in TIME_WAIT holds a socket for 2×MSL (typically 60–120 seconds on Linux). A high-traffic server closing 10,000 connections/second will have 600,000–1,200,000 TIME_WAIT sockets. This exhausts the ephemeral port range and can prevent new connections. Solutions: <code>SO_REUSEADDR</code>, <code>tcp_tw_reuse</code> (Linux sysctl), or reduce MSL. Your NGFW must not confuse TIME_WAIT connections with malicious activity.</p></div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔥</span><h3>NGFW State Tracking — What to Watch For</h3><span class="tag tag-orange">NGFW</span></div>
  <div class="cp-body">
    <p>A stateful NGFW must track TCP state transitions and reject packets that violate them:</p>
    <table class="t-table">
      <thead><tr><th>Anomaly</th><th>Flags</th><th>Why It's Suspicious</th><th>Action</th></tr></thead>
      <tbody>
        <tr><td>SYN-ACK without prior SYN</td><td>SYN+ACK</td><td>No SYN seen — spoofed or session spliced</td><td>Drop + log</td></tr>
        <tr><td>Data without ESTABLISHED</td><td>PSH+ACK, no connection entry</td><td>Injected data, blind injection attack</td><td>Drop</td></tr>
        <tr><td>RST with wrong sequence number</td><td>RST</td><td>RST injection attack to terminate connections</td><td>Drop if seq out of window</td></tr>
        <tr><td>FIN before ESTABLISHED</td><td>FIN</td><td>Port scan (FIN scan) or evasion attempt</td><td>Drop + log</td></tr>
        <tr><td>SYN to non-listening port</td><td>SYN</td><td>Port scan</td><td>Drop (no server) or RST</td></tr>
        <tr><td>Christmas tree packet</td><td>SYN+FIN+PSH+URG</td><td>Nmap XMAS scan — OS fingerprinting</td><td>Drop + alert</td></tr>
        <tr><td>NULL scan</td><td>no flags</td><td>Nmap NULL scan — firewall evasion</td><td>Drop + alert</td></tr>
        <tr><td>Overlapping segments</td><td>varies</td><td>IDS evasion — inconsistent reassembly</td><td>Reassemble + inspect</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>


<!-- ════════════ TAB 4 — SEQUENCE NUMBERS ════════════ -->
<div id="t4" class="tab-pane">
<p class="sep">SEQUENCE NUMBERS — ORDERING, RELIABILITY, AND BYTE TRACKING</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔢</span><h3>How Sequence Numbers Work</h3><span class="tag tag-teal">CORE CONCEPT</span></div>
  <div class="cp-body">
    <p>TCP numbers every byte it sends with a sequence number. This enables: (1) the receiver to detect missing bytes, (2) the receiver to reorder out-of-order segments, and (3) the sender to know exactly which bytes were received via the ACK number.</p>
<div class="cb"><pre><span class="cm">/* Example: sending "Hello World" (11 bytes) */</span>
ISN = 1000  <span class="cm"># chosen randomly at handshake</span>

Segment 1: seq=1001  data="Hello" (5 bytes)   → covers bytes 1001-1005
Segment 2: seq=1006  data=" Worl" (5 bytes)   → covers bytes 1006-1010
Segment 3: seq=1011  data="d"     (1 byte)    → covers bytes 1011-1011

<span class="cm">/* Receiver sends ACKs */</span>
After Segment 1: ACK=1006  <span class="cm"># "I have 1001-1005, send me 1006 next"</span>
After Segment 2: ACK=1011  <span class="cm"># "I have 1001-1010, send me 1011 next"</span>
After Segment 3: ACK=1012  <span class="cm"># "I have 1001-1011, send me 1012 next"</span>

<span class="cm">/* What if Segment 2 is lost? */</span>
Receiver gets Segment 1:  ACK=1006  (normal)
Receiver gets Segment 3:  ACK=1006  (still 1006 — can't advance past gap!)
                          → This is a duplicate ACK — signals a gap</span>

<span class="cm">/* Sequence number arithmetic — always modular (wraps at 2^32) */</span>
<span class="cm">/* Use int32_t arithmetic for correct comparison */</span>
int32_t diff = (int32_t)(seq_a - seq_b);
if (diff > 0) ...  <span class="cm"># seq_a is ahead of seq_b</span></pre></div>

    <div class="ins"><p>💡 <strong>SYN and FIN each consume one sequence number</strong> even though they carry no data. This is why the ACK after a SYN is ISN+1 (not ISN+0). It means both sides can unambiguously detect whether the connection control messages (SYN/FIN) were delivered.</p></div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📬</span><h3>Cumulative vs Selective Acknowledgement</h3><span class="tag tag-blue">ACK MODES</span></div>
  <div class="cp-body">
    <p>TCP's basic ACK is <strong>cumulative</strong> — it acknowledges all bytes up to a point. This works well in the common case but is inefficient when segments arrive out of order:</p>
<div class="cb"><pre><span class="cm">/* Cumulative ACK — without SACK */</span>
Sender sends:  seg[1000] seg[1500] seg[2000] seg[2500]
Network drops: seg[1500]
Receiver gets: seg[1000] ✓  ACK=1500
               seg[2000] ✓  ACK=1500  (still! — can't advance past 1500)
               seg[2500] ✓  ACK=1500  (still!)

Without SACK: sender must retransmit seg[1500] AND all after it
(go-back-N behaviour, though modern TCP is smarter)

<span class="cm">/* Selective ACK (SACK) — RFC 2018 */</span>
Receiver gets: seg[1000] ✓  ACK=1500
               seg[2000] ✓  ACK=1500  SACK=[2000-2499]
               seg[2500] ✓  ACK=1500  SACK=[2000-2999]

With SACK: sender knows ONLY seg[1500] is missing
           retransmits ONLY seg[1500]
           receiver ACKs=3000 after receiving it → done

SACK enabled by: "SACK Permitted" option in SYN/SYN+ACK
Up to 4 SACK blocks per segment (each block = 2×32-bit seq numbers = 8 bytes)</pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 5 — FLOW CONTROL ════════════ -->
<div id="t5" class="tab-pane">
<p class="sep">FLOW CONTROL — SLIDING WINDOW</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🪟</span><h3>The Sliding Window Mechanism</h3><span class="tag tag-teal">CONCEPT</span></div>
  <div class="cp-body">
    <p>Flow control prevents a fast sender from overwhelming a slow receiver's buffer. The receiver tells the sender exactly how much buffer space it has available via the <strong>Window Size</strong> field in every ACK. The sender must not have more than Window Size bytes of unacknowledged data in flight at any time.</p>
    <p>The window "slides" forward as data is acknowledged — the sender's send window moves right as ACKs arrive, allowing more data to be sent.</p>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Sender's View of the Sequence Number Space</h3><span class="tag tag-blue">SEND BUFFER</span></div>
  <div class="cp-body">
    <p>The sender categorises its byte stream into four regions:</p>
    <div class="window-vis">
      <div class="wv-row">
        <div class="wv-label">Sender</div>
        <div class="wv-seg ws-sent-acked" style="flex:2">Sent + ACKed<br><span style="font-size:.62rem;font-weight:400">already delivered</span></div>
        <div class="wv-seg ws-sent-unacked" style="flex:1.5">Sent, not ACKed<br><span style="font-size:.62rem;font-weight:400">in flight</span></div>
        <div class="wv-seg ws-can-send" style="flex:1.5">Can send<br><span style="font-size:.62rem;font-weight:400">within window</span></div>
        <div class="wv-seg ws-no-send" style="flex:2">Cannot send yet<br><span style="font-size:.62rem;font-weight:400">window full or no data</span></div>
      </div>
      <div style="font-size:.72rem;font-family:monospace;color:var(--light-text,#666);margin-top:3px">
        ← SND.UNA (last unACKed) → ← SND.NXT (next to send) → ← SND.UNA + win (window edge) →
      </div>
    </div>

    <div class="window-vis">
      <div class="wv-row">
        <div class="wv-label">Receiver</div>
        <div class="wv-seg ws-sent-acked" style="flex:2">Received + Delivered<br><span style="font-size:.62rem;font-weight:400">to application</span></div>
        <div class="wv-seg ws-recv" style="flex:1.5">Received in-order<br><span style="font-size:.62rem;font-weight:400">buffered, not read yet</span></div>
        <div class="wv-seg ws-ooo" style="flex:1">Out-of-order<br><span style="font-size:.62rem;font-weight:400">buffered, gap before</span></div>
        <div class="wv-seg ws-empty" style="flex:2">Available buffer<br><span style="font-size:.62rem;font-weight:400">= advertised window</span></div>
      </div>
      <div style="font-size:.72rem;font-family:monospace;color:var(--light-text,#666);margin-top:3px">
        ← RCV.NXT (next expected) → ← RCV.WND (advertised window size) →
      </div>
    </div>

<div class="cb"><pre><span class="cm">/* Flow control in action */</span>
Receiver has 64KB buffer, app reads slowly:
  Initial window advertised: 65535 bytes

Sender sends 32KB → receiver buffers it, app hasn't read yet:
  Receiver advertises: Window = 65535 - 32768 = 32767 bytes

Sender sends another 20KB → receiver buffers:
  Receiver advertises: Window = 65535 - 52768 = 12767 bytes

Sender sends 12KB → buffer nearly full:
  Receiver advertises: Window = 767 bytes

App reads 40KB from buffer:
  Receiver advertises: Window = 40767 bytes   <span class="cm"># window re-opens</span>

<span class="cm">/* Zero window — sender must stop */</span>
Buffer completely full:
  Receiver advertises: Window = 0   <span class="cm"># sender MUST stop sending data</span>
  Sender starts Zero Window Probe timer
  Sender sends 1-byte probes periodically
  When receiver's app reads data → receiver sends Window Update ACK</pre></div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Window Scale Option — High-Bandwidth Networks</h3><span class="tag tag-green">OPTIMIZATION</span></div>
  <div class="cp-body">
    <p>The Window Size field is 16 bits — maximum 65,535 bytes. On a 1 Gbps link with 10ms RTT, the bandwidth-delay product (BDP) is 1 Gbps × 0.01s = 1.25 MB. With only 64 KB in flight, the link is only 64KB/1250KB = 5% utilised. The <strong>Window Scale option</strong> (RFC 7323) solves this by multiplying the window by a power of 2:</p>
<div class="cb"><pre><span class="cm">/* Window Scale option in SYN */</span>
Scale factor = 7  <span class="cm"># window size is multiplied by 2^7 = 128</span>
Effective max window = 65535 × 128 = 8,388,480 bytes (8 MB)

<span class="cm">/* Both sides must negotiate it in SYN / SYN+ACK */</span>
<span class="cm">/* If one side doesn't include Window Scale in SYN, neither side uses scaling */</span>

<span class="cm">/* Check on Linux */</span>
ss -tni | grep rcv_space   <span class="cm"># shows receiver socket buffer size</span>
sysctl net.ipv4.tcp_rmem   <span class="cm"># min/default/max receive buffer: "4096 131072 6291456"</span>
sysctl net.ipv4.tcp_wmem   <span class="cm"># min/default/max send buffer</span></pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 6 — CONGESTION CONTROL ════════════ -->
<div id="t6" class="tab-pane">
<p class="sep">CONGESTION CONTROL — PROTECTING THE NETWORK</p>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🌐</span><h3>The Congestion Collapse Problem</h3><span class="tag tag-orange">MOTIVATION</span></div>
  <div class="cp-body">
    <p>Flow control protects the <em>receiver</em>. Congestion control protects the <em>network</em>. In 1986, the internet experienced "congestion collapse" — throughput dropped to 0.1% of capacity because all senders kept retransmitting lost packets, further overloading already-saturated routers. Van Jacobson designed TCP congestion control (RFC 5681) to solve this: senders automatically reduce their sending rate when they detect packet loss.</p>
    <p>TCP's congestion control maintains a <strong>Congestion Window (cwnd)</strong> — a sender-side limit on unacknowledged data in addition to the receiver's window. The effective window is: <code>min(cwnd, receiver_window)</code>.</p>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📈</span><h3>Four Phases of TCP Congestion Control</h3><span class="tag tag-blue">ALGORITHM</span></div>
  <div class="cp-body">
    <div class="congestion-phases">
      <div class="cong-phase" style="background:#e8f5e8;border-right:1px solid var(--border-color,#e0e0e0)">
        <div class="cong-phase-name" style="color:#1a5a1a">Slow Start</div>
        <div class="cong-phase-desc">cwnd starts at 1-10 MSS. Doubles every RTT (exponential growth). Continues until cwnd reaches ssthresh.</div>
      </div>
      <div class="cong-phase" style="background:#e8f1f9;border-right:1px solid var(--border-color,#e0e0e0)">
        <div class="cong-phase-name" style="color:#1a3a5c">Congestion Avoidance</div>
        <div class="cong-phase-desc">cwnd grows by 1 MSS per RTT (linear). Cautious probing of available bandwidth until loss detected.</div>
      </div>
      <div class="cong-phase" style="background:#faeaea;border-right:1px solid var(--border-color,#e0e0e0)">
        <div class="cong-phase-name" style="color:#6c1a1a">Fast Retransmit</div>
        <div class="cong-phase-desc">3 duplicate ACKs signal loss. Retransmit missing segment immediately without waiting for RTO timeout.</div>
      </div>
      <div class="cong-phase" style="background:#ede8f5">
        <div class="cong-phase-name" style="color:#3a1a6c">Fast Recovery</div>
        <div class="cong-phase-desc">After fast retransmit: ssthresh = cwnd/2, cwnd = ssthresh + 3. Then enters Congestion Avoidance (not Slow Start).</div>
      </div>
    </div>

<div class="cb"><pre><span class="cm">/* NewReno algorithm (most common baseline) */</span>
<span class="cm">/* State variables */</span>
cwnd = 10 * MSS    <span class="cm"># congestion window (starts at 10 MSS per RFC 6928)</span>
ssthresh = 65535   <span class="cm"># slow start threshold (initial: large value)</span>

<span class="cm">/* Slow Start phase */</span>
on each ACK: cwnd += MSS          <span class="cm"># doubles every RTT (exponential)</span>
when cwnd >= ssthresh: → Congestion Avoidance

<span class="cm">/* Congestion Avoidance phase */</span>
on each ACK: cwnd += MSS² / cwnd  <span class="cm"># +1 MSS per RTT (linear)</span>

<span class="cm">/* Packet loss detected by TIMEOUT */</span>
ssthresh = max(cwnd / 2, 2*MSS)
cwnd = 1 MSS        <span class="cm"># drastic reduction — restart Slow Start</span>

<span class="cm">/* Packet loss detected by 3 DUPLICATE ACKs (mild congestion) */</span>
ssthresh = max(cwnd / 2, 2*MSS)
cwnd = ssthresh + 3*MSS   <span class="cm"># smaller reduction — Fast Recovery</span>
<span class="cm"># retransmit the missing segment immediately</span>
<span class="cm"># then enter Congestion Avoidance (skip Slow Start)</span>

<span class="cm">/* Check congestion control algorithm in use */</span>
sysctl net.ipv4.tcp_congestion_control   <span class="cm"># typical: "cubic" or "bbr"</span>
ss -tni dst :80 | grep cwnd              <span class="cm"># see live cwnd for connections</span></pre></div>

    <div class="ins"><p>💡 <strong>Modern algorithms — CUBIC and BBR:</strong> NewReno is the baseline. Linux defaults to <strong>CUBIC</strong> (RFC 8312), which uses a cubic function for window growth — faster recovery after loss on high-BDP links. Google's <strong>BBR</strong> (Bottleneck Bandwidth and RTT) is newer and model-based rather than loss-based — it probes the actual bandwidth and RTT instead of reacting to drops. BBR dramatically improves performance on lossy networks (mobile, satellite). Understanding NewReno gives you the conceptual foundation; CUBIC and BBR are optimisations on the same principles.</p></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 7 — TIMERS AND SACK ════════════ -->
<div id="t7" class="tab-pane">
<p class="sep">TCP TIMERS — RETRANSMISSION, KEEPALIVE, TIME-WAIT</p>

<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">⏱️</span><h3>The Four TCP Timers</h3><span class="tag tag-amber">TIMERS</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Timer</th><th>Trigger</th><th>Action on Expiry</th><th>Default Value</th></tr></thead>
      <tbody>
        <tr>
          <td><strong>RTO (Retransmission Timeout)</strong></td>
          <td>Segment sent with no ACK received within RTO</td>
          <td>Retransmit oldest unacknowledged segment. Double RTO (exponential backoff). Reduce cwnd (Slow Start). Max 15 retries (then RST).</td>
          <td>Dynamically calculated from RTT (min 200ms, max ~120s)</td>
        </tr>
        <tr>
          <td><strong>Persist (Zero Window)</strong></td>
          <td>Receiver advertises window=0</td>
          <td>Send 1-byte Zero Window Probe to check if window has opened. Exponential backoff.</td>
          <td>Starts at RTO, doubles each probe</td>
        </tr>
        <tr>
          <td><strong>Keepalive</strong></td>
          <td>No data exchanged for keepalive idle time</td>
          <td>Send TCP keepalive probe (1-byte with seq=SND.NXT-1). If no response after N probes → close connection.</td>
          <td>Idle: 7200s (2 hrs), Interval: 75s, Count: 9 probes (Linux defaults)</td>
        </tr>
        <tr>
          <td><strong>TIME_WAIT (2×MSL)</strong></td>
          <td>Connection enters TIME_WAIT state</td>
          <td>After 2×MSL expires, move to CLOSED. Prevents stale segments from old connection being received by new connection with same 4-tuple.</td>
          <td>MSL=60s on Linux → TIME_WAIT=120s. Configurable.</td>
        </tr>
      </tbody>
    </table>

    <h4>RTO Calculation — Karn's Algorithm</h4>
<div class="cb"><pre><span class="cm">/* RTT measurement and RTO calculation (RFC 6298) */</span>

<span class="cm">/* Measure RTT for each ACKed segment (not retransmitted ones — Karn's rule) */</span>
SRTT = 0.875 * SRTT + 0.125 * RTT_sample    <span class="cm"># smoothed RTT (EWMA)</span>
RTTVAR = 0.75 * RTTVAR + 0.25 * |SRTT - RTT_sample|  <span class="cm"># RTT variance</span>
RTO = SRTT + 4 * RTTVAR                      <span class="cm"># RTO with safety margin</span>
RTO = max(1 second, RTO)                     <span class="cm"># floor: 1 second</span>

<span class="cm">/* On RTO timeout: double the RTO (exponential backoff) */</span>
RTO = RTO * 2   <span class="cm"># until max (typically 120 seconds)</span>

<span class="cm">/* After successful retransmission: restart RTT measurement from scratch */</span>
<span class="cm"># (Can't tell if ACK is for original or retransmitted — Karn's algorithm)</span>

<span class="cm">/* Check on Linux */</span>
ss -tni | grep rtt   <span class="cm"># shows rtt:X/Y for established connections</span></pre></div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">⚙️</span><h3>Key TCP Tuning Parameters (Linux)</h3><span class="tag tag-green">TUNING</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm"># View all TCP-relevant sysctl parameters</span>
sysctl -a | grep tcp

<span class="cm"># Buffer sizes (affects window size and throughput)</span>
sysctl net.ipv4.tcp_rmem    <span class="cm"># receive: "4096 87380 6291456" (min/default/max)</span>
sysctl net.ipv4.tcp_wmem    <span class="cm"># send:    "4096 16384 4194304"</span>
sysctl net.core.rmem_max    <span class="cm"># max receive socket buffer (override tcp_rmem max)</span>

<span class="cm"># Connection setup</span>
sysctl net.ipv4.tcp_syn_retries      <span class="cm"># SYN retransmit attempts (default 6)</span>
sysctl net.ipv4.tcp_synack_retries   <span class="cm"># SYN+ACK retransmit attempts (default 5)</span>
sysctl net.ipv4.tcp_syncookies       <span class="cm"># SYN flood protection</span>
sysctl net.ipv4.tcp_max_syn_backlog  <span class="cm"># max half-open connections per socket</span>

<span class="cm"># TIME_WAIT</span>
sysctl net.ipv4.tcp_tw_reuse    <span class="cm"># reuse TIME_WAIT sockets for new connections</span>
sysctl net.ipv4.tcp_fin_timeout <span class="cm"># FIN_WAIT_2 timeout (default 60s)</span>

<span class="cm"># Keepalive</span>
sysctl net.ipv4.tcp_keepalive_time     <span class="cm"># idle time before probes (default 7200s)</span>
sysctl net.ipv4.tcp_keepalive_intvl   <span class="cm"># interval between probes (default 75s)</span>
sysctl net.ipv4.tcp_keepalive_probes  <span class="cm"># probe count before giving up (default 9)</span>

<span class="cm"># Congestion control</span>
sysctl net.ipv4.tcp_congestion_control  <span class="cm"># algorithm: cubic, bbr, reno</span>
sysctl net.ipv4.tcp_sack                <span class="cm"># SACK enabled (default 1)</span>
sysctl net.ipv4.tcp_timestamps          <span class="cm"># timestamps enabled (default 1)</span></pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 8 — CONNECTION TEARDOWN ════════════ -->
<div id="t8" class="tab-pane">
<p class="sep">TCP CONNECTION TEARDOWN — GRACEFUL AND ABORTIVE CLOSE</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">👋</span><h3>Four-Way Graceful Close</h3><span class="tag tag-blue">TEARDOWN</span></div>
  <div class="cp-body">
    <p>TCP is full-duplex — each direction must be closed independently. The graceful close uses four messages (or three if the remote side closes simultaneously):</p>

    <div class="seq-diagram">
      <div class="seq-actor" style="background:#e8f1f9;color:#1a3a5c">Client (active close)</div>
      <div class="seq-spacer"></div>
      <div class="seq-actor" style="background:#e0f0ee;color:#0a3a30">Server (passive close)</div>

      <div style="display:flex;flex-direction:column;align-items:flex-end;padding-top:10px">
        <div class="seq-box" style="background:#e0f0ee;border:1.5px solid #90c8b8;color:#0a3a30">FIN+ACK<br><span style="font-size:.65rem;font-weight:400">seq=m</span></div>
        <div style="font-size:.68rem;color:var(--light-text,#666);margin-top:2px">→ FIN_WAIT_1</div>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;padding-top:10px">
        <div style="width:80px;border-top:2px solid #0f6e56;position:relative">
          <span style="position:absolute;right:-6px;top:-8px;color:#0f6e56;font-size:1rem">▶</span>
        </div>
      </div>
      <div style="padding-top:10px">
        <div style="font-size:.72rem;color:var(--light-text,#666)">receive FIN → CLOSE_WAIT</div>
      </div>

      <div style="padding-top:10px">
        <div style="font-size:.72rem;color:var(--light-text,#666)">ACK received → FIN_WAIT_2</div>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;padding-top:10px">
        <div style="width:80px;border-top:2px solid #1a3a5c;position:relative">
          <span style="position:absolute;left:-6px;top:-8px;color:#1a3a5c;font-size:1rem">◀</span>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;align-items:flex-start;padding-top:10px">
        <div class="seq-box" style="background:#e8f1f9;border:1.5px solid #b0ccec;color:#1a3a5c">ACK<br><span style="font-size:.65rem;font-weight:400">ack=m+1</span></div>
      </div>

      <div style="padding-top:10px;text-align:right;font-size:.72rem;color:var(--light-text,#666)">wait for server FIN...</div>
      <div></div>
      <div style="padding-top:10px;font-size:.72rem;color:var(--light-text,#666)">app closes → send FIN → LAST_ACK</div>

      <div style="padding-top:8px">
        <div style="font-size:.72rem;color:var(--light-text,#666)">receive FIN → TIME_WAIT (2×MSL)</div>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;padding-top:8px">
        <div style="width:80px;border-top:2px solid #5b3a8c;position:relative">
          <span style="position:absolute;left:-6px;top:-8px;color:#5b3a8c;font-size:1rem">◀</span>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;align-items:flex-start;padding-top:8px">
        <div class="seq-box" style="background:#ede8f5;border:1.5px solid #c0a8e8;color:#3a1a6c">FIN+ACK<br><span style="font-size:.65rem;font-weight:400">seq=n</span></div>
      </div>

      <div style="display:flex;flex-direction:column;align-items:flex-end;padding-top:8px">
        <div class="seq-box" style="background:#e2f0e8;border:1.5px solid #a0d0a0;color:#1a4a1a">ACK<br><span style="font-size:.65rem;font-weight:400">ack=n+1</span></div>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;padding-top:8px">
        <div style="width:80px;border-top:2px solid #1a5a1a;position:relative">
          <span style="position:absolute;right:-6px;top:-8px;color:#1a5a1a;font-size:1rem">▶</span>
        </div>
      </div>
      <div style="padding-top:8px">
        <div style="font-size:.72rem;color:var(--light-text,#666)">ACK received → CLOSED</div>
      </div>
    </div>

    <div class="note"><p>💡 <strong>Half-close:</strong> After sending FIN, the local side can no longer send data but <em>can still receive</em> data. The server may continue sending data (e.g., flushing a file) after acknowledging the client's FIN. This "half-closed" state (FIN_WAIT_2 on client, CLOSE_WAIT on server) persists until the server also sends its FIN.</p></div>
  </div>
</div>

<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>RST — Abortive Close</h3><span class="tag tag-red">RESET</span></div>
  <div class="cp-body">
    <p>A RST (Reset) segment immediately closes a connection without the graceful 4-way teardown. No data is buffered, no TIME_WAIT is entered — the connection is gone instantly. RST is sent in three main situations:</p>
    <ul>
      <li><strong>Connection to closed port</strong> — server receives SYN or data for a port nothing is listening on → sends RST</li>
      <li><strong>Abortive close</strong> — application calls <code>close()</code> with <code>SO_LINGER</code> set to 0 → kernel sends RST instead of FIN</li>
      <li><strong>Out-of-window segment</strong> — segment arrives with sequence number completely outside the current window → RST to signal error</li>
    </ul>
<div class="cb"><pre><span class="cm">/* RST injection attack */</span>
<span class="cm">/* Attacker crafts RST segment with sequence number in receiver's window */</span>
<span class="cm">/* Target receives RST → connection terminated immediately */</span>
<span class="cm">/* Historically used to disrupt BGP sessions (e.g., the 2004 RFC 4953 attack) */</span>

<span class="cm">/* Protection: check sequence number is in [RCV.NXT, RCV.NXT + RCV.WND) */</span>
<span class="cm">/* RFC 5961 "Improving TCP's Robustness to Blind In-Window Attacks" */</span>

<span class="cm">/* NGFW RST injection for connection termination */</span>
<span class="cm">/* Some NGFWs send RST to both sides to terminate blacklisted connections */</span>
<span class="cm">/* Must spoof the correct source IP and use a valid in-window sequence number */</span></pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB 9 — NGFW AND TCP ════════════ -->
<div id="t9" class="tab-pane">
<p class="sep">TCP IN AN NGFW — STATEFUL INSPECTION DEEP DIVE</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>How a Stateful Firewall Tracks TCP</h3><span class="tag tag-teal">STATEFUL INSPECTION</span></div>
  <div class="cp-body">
    <p>A stateful firewall maintains a <strong>connection table</strong> (also called session table or conntrack table) — a hash table keyed by the 5-tuple, storing the connection's current state and sequence number tracking data.</p>
<div class="cb"><pre><span class="cm">/* Connection table entry (conntrack) */</span>
<span class="ck">typedef struct</span> {
    <span class="cm">/* 5-tuple key (stored in bihash) */</span>
    ip4_address_t   src_ip, dst_ip;
    uint16_t        src_port, dst_port;
    uint8_t         proto;              <span class="cm">/* 6 = TCP */</span>

    <span class="cm">/* TCP state tracking */</span>
    tcp_state_t     state;              <span class="cm">/* SYN_SENT, ESTABLISHED, etc. */</span>
    uint32_t        client_isn;         <span class="cm">/* client's initial sequence number */</span>
    uint32_t        server_isn;         <span class="cm">/* server's initial sequence number */</span>
    uint32_t        client_next_seq;    <span class="cm">/* expected next seq from client */</span>
    uint32_t        server_next_seq;    <span class="cm">/* expected next seq from server */</span>
    uint32_t        client_window;      <span class="cm">/* client's advertised window */</span>
    uint32_t        server_window;      <span class="cm">/* server's advertised window */</span>

    <span class="cm">/* Policy and metadata */</span>
    uint32_t        policy_id;          <span class="cm">/* which policy matched this flow */</span>
    uint64_t        bytes_client;       <span class="cm">/* bytes from client → server */</span>
    uint64_t        bytes_server;       <span class="cm">/* bytes from server → client */</span>
    uint64_t        last_seen;          <span class="cm">/* timestamp for idle timeout */</span>
    uint8_t         app_id;             <span class="cm">/* L7 application (from DPI) */</span>
} conntrack_entry_t;</pre></div>

    <p><strong>For every packet, the NGFW:</strong></p>
    <ol>
      <li>Extracts the 5-tuple from IP + TCP headers</li>
      <li>Looks up the 5-tuple in the connection table (O(1) bihash lookup)</li>
      <li>If found: validates the packet against expected state (sequence numbers, flags) → allow, drop, or flag</li>
      <li>If not found: check if it's a valid new connection attempt (SYN only, SYN+ACK for asymmetric routing) → create new entry or drop</li>
      <li>Updates the connection entry (sequence numbers, bytes, last_seen)</li>
      <li>Applies policy (allow, drop, inspect for DPI)</li>
    </ol>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔬</span><h3>TCP Sequence Number Validation</h3><span class="tag tag-purple">SEQUENCE TRACKING</span></div>
  <div class="cp-body">
    <p>A sophisticated NGFW validates sequence numbers on every packet to detect injection attacks:</p>
<div class="cb"><pre><span class="cm">/* Validate incoming segment from client */</span>
<span class="ck">bool</span> validate_tcp_segment(conntrack_entry_t *ct,
                          tcp_header_t *tcp, uint32_t payload_len) {
    uint32_t seq     = ntohl(tcp->seq);
    uint32_t ack     = ntohl(tcp->ack_seq);
    uint32_t win     = ntohs(tcp->window) << ct->server_wscale;

    <span class="cm">/* Check 1: sequence number in valid receive window */</span>
    <span class="cm">/* seq must be in [next_expected, next_expected + window) */</span>
    int32_t seq_delta = (int32_t)(seq - ct->client_next_seq);
    <span class="ck">if</span> (seq_delta < 0 || seq_delta > (int32_t)ct->server_window) {
        <span class="cs">/* Out-of-window segment — could be injected */</span>
        <span class="ck">return false</span>;
    }

    <span class="cm">/* Check 2: ACK number in valid range */</span>
    int32_t ack_delta = (int32_t)(ack - ct->server_isn);
    <span class="ck">if</span> (ack_delta < 0 || ack_delta > (int32_t)ct->server_next_seq) {
        <span class="ck">return false</span>;   <span class="cm">/* ACKing data we haven't sent */</span>
    }

    <span class="cm">/* Check 3: flags match expected state */</span>
    <span class="ck">if</span> (ct->state == TCP_ESTABLISHED) {
        <span class="ck">if</span> (tcp->syn && !tcp->rst)
            <span class="ck">return false</span>;   <span class="cm">/* SYN in ESTABLISHED is suspicious */</span>
    }

    <span class="ck">return true</span>;
}</pre></div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>MSS Clamping — Preventing Fragmentation</h3><span class="tag tag-orange">MSS CLAMPING</span></div>
  <div class="cp-body">
    <p>When a TCP connection passes through a firewall or VPN that reduces the effective MTU (e.g., PPPoE reduces MTU from 1500 to 1492, VPN adds header overhead), packets larger than the new MTU need to be fragmented — or dropped if DF=1. MSS clamping rewrites the MSS option in SYN/SYN+ACK segments to force both sides to use smaller segments that fit without fragmentation.</p>
<div class="cb"><pre><span class="cm">/* MSS clamping — rewrite MSS option in SYN segments */</span>
<span class="cm">/* Called "TCP MSS clamping" — applied on SYN and SYN+ACK */</span>

Original SYN: MSS=1460 (assuming Ethernet MTU=1500, IP hdr=20, TCP hdr=20)
PPPoE link MTU: 1492 bytes
New MSS: 1492 - 20 (IP) - 20 (TCP) = 1452

NGFW rewrites MSS=1460 → MSS=1452 in the SYN before forwarding
Both sides now use 1452-byte segments → no fragmentation needed

<span class="cm">/* Linux iptables MSS clamping */</span>
iptables -t mangle -A FORWARD -p tcp --tcp-flags SYN,RST SYN \
  -j TCPMSS --clamp-mss-to-pmtu

<span class="cm">/* In VPP (your data plane) */</span>
<span class="cm"># This would be implemented in your TCP normalisation plugin</span>
<span class="cm"># Find TCP Options in SYN segment, locate MSS option (Kind=2),</span>
<span class="cm"># compare with interface MTU, rewrite if MSS > (MTU - 40)</span></pre></div>
  </div>
</div>
</div>


<!-- ════════════ TAB A — LABS ════════════ -->
<div id="ta" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Capture and Decode a Complete TCP Lifecycle</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Capture a full TCP session — handshake, data transfer, and teardown — and decode every flag, sequence number, ACK, and window size in Wireshark. Understand the connection from first SYN to last ACK.</p>
    <div class="lab-step"><div class="sn">1</div><div>Start Wireshark capture on your interface. Run: <code>curl http://example.com</code>. Stop capture. Filter: <code>ip.addr == 93.184.216.34</code> to isolate the example.com conversation.</div></div>
    <div class="lab-step"><div class="sn">2</div><div><strong>Handshake analysis:</strong> Find the SYN packet. Record: Sequence Number (ISN), Window Size, MSS option, SACK Permitted option, Window Scale option. Find SYN+ACK: verify ACK = client ISN + 1. Find the final ACK: verify ACK = server ISN + 1.</div></div>
    <div class="lab-step"><div class="sn">3</div><div><strong>Data transfer analysis:</strong> Find the HTTP GET request packet. Record: Flags (PSH+ACK), Sequence Number, payload length. Find the HTTP response: record sequence numbers of the first and last response segment. Use Wireshark's "Follow TCP Stream" to see the full conversation.</div></div>
    <div class="lab-step"><div class="sn">4</div><div><strong>Teardown analysis:</strong> Find the FIN+ACK from one side, the ACK reply, then the FIN+ACK from the other side, and the final ACK. Identify which side initiated the close. Look for TIME_WAIT: run <code>ss -tn state time-wait</code> immediately after curl — you may catch the socket in TIME_WAIT.</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Sequence number graph:</strong> In Wireshark, go to Statistics → TCP Stream Graphs → Time/Sequence (Stevens). You'll see the sawtooth pattern of slow start, linear growth, and any retransmissions. If there are no retransmissions, artificially increase delay: <code>tc qdisc add dev eth0 root netem delay 100ms loss 2%</code> then curl again.</div></div>
    <div class="lab-step"><div class="sn">6</div><div>Check the connection state machine using: <code>ss -tn</code> (during the connection) — observe ESTABLISHED state. Check <code>ss -tn state time-wait</code> after connection closes. Map each ss state to the TCP state diagram in Tab 3.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Simulate TCP Attacks and Defences with Scapy</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Use Scapy to craft malformed TCP segments and observe how Linux handles them. Understand SYN flood, RST injection, and invalid flag combinations.</p>
    <div class="lab-step"><div class="sn">1</div><div><strong>SYN flood simulation (on loopback — safe):</strong> <code>from scapy.all import *</code>, then send 100 SYNs with random source IPs to a closed port: <code>for i in range(100): send(IP(src=RandIP(), dst="127.0.0.1")/TCP(sport=RandShort(), dport=9999, flags="S"), verbose=0)</code>. Capture with <code>tcpdump -i lo -n 'port 9999'</code>. What does the server return for a closed port?</div></div>
    <div class="lab-step"><div class="sn">2</div><div><strong>Flag anomaly detection:</strong> Send a Christmas tree packet (all flags set) to a listening port and observe: <code>send(IP(dst="127.0.0.1")/TCP(dport=22, flags="FSRPAU"), verbose=1)</code>. Start a listening server first: <code>nc -l 12345</code>. Does the server accept it? What does the Linux kernel do with it?</div></div>
    <div class="lab-step"><div class="sn">3</div><div><strong>SYN cookies demo:</strong> Enable SYN cookies: <code>sudo sysctl net.ipv4.tcp_syncookies=2</code>. Start <code>nc -l 8888</code>. Send 500 SYNs from random IPs to port 8888. Monitor the connection backlog: <code>ss -tn state syn-recv | wc -l</code>. With syncookies=2, the backlog should not grow indefinitely.</div></div>
    <div class="lab-step"><div class="sn">4</div><div><strong>Build a mini port scanner:</strong> Write a Python script using Scapy that sends SYN to ports 1-1024 on localhost and records which ports return SYN+ACK (open) vs RST (closed) vs no response (filtered). This is exactly how Nmap's SYN scan works.</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Analyse the output:</strong> Run your port scanner against your local machine. Cross-reference with <code>ss -tlnp</code> (listening TCP ports). Every port showing SYN+ACK in your scan should match a listening service. Ports showing RST are closed. Understand why firewall-filtered ports show no response.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Write a TCP Connection Tracker in C</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Implement a simplified TCP state machine tracker using libpcap. This is the core of what a stateful firewall does — track each connection through its state transitions based on observed TCP flags.</p>
    <div class="lab-step"><div class="sn">1</div><div>Install libpcap: <code>sudo apt install libpcap-dev</code>. Create <code>tcp_tracker.c</code>. Define a connection table as a simple array of structs with fields: src_ip, dst_ip, src_port, dst_port, state (enum: SYN_SENT, ESTABLISHED, FIN_WAIT, CLOSED), last_seen.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Use pcap to capture TCP packets: <code>pcap_open_live("eth0", 65535, 1, 1000, errbuf)</code>. Set filter: <code>pcap_compile</code> + <code>pcap_setfilter</code> with filter string <code>"tcp"</code>. In the packet handler, parse Ethernet → IP → TCP headers manually using byte offsets.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Implement state transitions: if SYN-only → create new entry with state=SYN_SENT; if SYN+ACK → find matching entry (reversed 5-tuple), update to state=SYN_RECEIVED; if ACK after SYN+ACK → state=ESTABLISHED; if FIN → state=FIN_WAIT; after second FIN+ACK → state=CLOSED, remove entry.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Print a summary every second: number of connections in each state (SYN_SENT, ESTABLISHED, FIN_WAIT, CLOSED), total connections seen, connections per second. Run it while browsing the web or downloading a file — watch the ESTABLISHED count grow and shrink.</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Bonus — Add anomaly detection:</strong> Log a warning when you see: (a) SYN+ACK without a prior SYN in the table, (b) RST with a sequence number outside the expected window, (c) data segments before ESTABLISHED state, (d) more than 5 SYNs per second from the same source IP.</div></div>
  </div>
</div>

</div>


<!-- ════════════ TAB B — CHECKLIST ════════════ -->
<div id="tb" class="tab-pane">
<p class="sep">M05 MASTERY CHECKLIST</p>

<ul class="cl">
  <li>Can explain TCP's 6 guarantees: reliability, ordering, no duplication, error detection, flow control, congestion control</li>
  <li>Know what TCP does NOT guarantee: timing, bandwidth, message boundaries</li>
  <li>Can draw the TCP header from memory with all field names and sizes (20 bytes, 5 rows)</li>
  <li>Know all 8 TCP flags and what each does: CWR, ECE, URG, ACK, PSH, RST, SYN, FIN</li>
  <li>Know flag combinations that indicate state: SYN=new connection, SYN+ACK=server reply, ACK=data, FIN+ACK=close, RST=abort</li>
  <li>Know the key TCP options: MSS, Window Scale, SACK Permitted, SACK, Timestamps</li>
  <li>Can explain the 3-way handshake step by step with sequence numbers: SYN(seq=x) → SYN+ACK(seq=y,ack=x+1) → ACK(ack=y+1)</li>
  <li>Know why ISN is random: prevents stale segment injection and sequence number prediction attacks</li>
  <li>Know what a SYN flood attack is and how SYN cookies defend against it</li>
  <li>Can name and describe all 11 TCP states: CLOSED, LISTEN, SYN_SENT, SYN_RECEIVED, ESTABLISHED, FIN_WAIT_1, FIN_WAIT_2, CLOSE_WAIT, CLOSING, LAST_ACK, TIME_WAIT</li>
  <li>Know the active vs passive close distinction and which side enters TIME_WAIT</li>
  <li>Know why TIME_WAIT lasts 2×MSL and what problem it solves</li>
  <li>Understand sequence numbers: each byte is numbered, SYN and FIN consume one number each</li>
  <li>Understand ACK semantics: ACK=N means "I have received all bytes up to N-1, send me N next"</li>
  <li>Understand cumulative vs selective ACK (SACK): SACK reports received out-of-order blocks, allows selective retransmission</li>
  <li>Explain flow control: receiver's window size limits sender's unACKed data in flight</li>
  <li>Know the four flow control regions: sent+ACKed, sent+unACKed, can send, cannot send</li>
  <li>Know what zero window means and how the sender handles it: persist timer + zero window probes</li>
  <li>Explain congestion control's 4 phases: Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery</li>
  <li>Know cwnd and ssthresh: cwnd doubles in SS, grows linearly in CA, halves on loss</li>
  <li>Know the difference between timeout loss (cwnd→1) and 3-dupACK loss (cwnd→ssthresh, skip SS)</li>
  <li>Know the 4 TCP timers: RTO (retransmit), Persist (zero window), Keepalive, TIME_WAIT</li>
  <li>Know how RTO is calculated: SRTT + 4×RTTVAR, minimum 1 second</li>
  <li>Understand 4-way teardown vs RST: FIN is graceful (buffered data delivered), RST is abortive (immediate)</li>
  <li>Know what a stateful NGFW stores per TCP connection: 5-tuple, state, ISNs, sequence tracking, window sizes</li>
  <li>Know 7+ TCP attack types and NGFW defences: SYN flood, RST injection, Christmas tree scan, NULL scan, data before ESTABLISHED, overlapping segments, invalid flags</li>
  <li>Know MSS clamping: why it's needed, when applied (SYN/SYN+ACK), how it prevents fragmentation</li>
  <li>Completed Lab 1: captured full TCP lifecycle in Wireshark, decoded sequence numbers and flags at every stage</li>
  <li>Completed Lab 2: used Scapy to craft TCP attacks, implemented mini SYN port scanner</li>
  <li>Completed Lab 3: built TCP connection tracker in C using libpcap with state machine and anomaly detection</li>
</ul>

<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M06 - UDP and ICMP</strong>. You now have deep TCP knowledge. M06 is shorter — UDP has almost no complexity by design — but understanding UDP's simplicity (and its implications for NGFW) is essential before moving to DNS (M07) and HTTP (M08), both of which use UDP heavily.</p>
</div>
</div>


<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="{{ '/learning/networking-mastery/m04-ipv6/' | relative_url }}">← M04 IPv6</a>
  <a href="{{ '/learning/networking-mastery/' | relative_url }}">🗺️ Roadmap</a>
  <a class="nb" href="{{ '/learning/networking-mastery/m06-udp-icmp/' | relative_url }}">Next: M06 - UDP and ICMP →</a>
</div>

<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
</script>
