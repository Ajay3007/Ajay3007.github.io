---
title: "M08 - HTTP/1.1, HTTP/2, HTTP/3 and QUIC"
description: "NETWORKING MASTERY · PHASE 2 · MODULE 08 · WEEK 6 🌍 HTTP/1.1, HTTP/2, HTTP/3 and QUIC Request/response · Methods · Headers · Status codes · Pipelining · Multiplexing · QUIC…"
domain: networking
track: networking-mastery
order: 8
ownHeader: true
url: /learning/networking-mastery/m08-http/
---

<style>
/* ── Base ───────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 30%,#6a1a8c 65%,#3a0a5c 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0;
}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#c8a0f0;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#e0c8ff;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#ecdcff}

/* Tabs */
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#c8a0f0;border-bottom-color:#c8a0f0}
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

/* Panel colours */
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #7a3a9c}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#e0c8ff;white-space:pre}
.cm{color:#7a5a90}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}

/* Insight / warning / note */
.ins{background:#f5eeff;border:1.5px solid #7a3a9c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#1e0a30;border-color:#8a50ac}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#5a1a8c}
[data-theme=dark] .ins strong{color:#c8a0f0}

.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}

.note{background:#e8f5f0;border:1.5px solid #0f6e56;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .note{background:#0a2420;border-color:#2a9a8e}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}

/* Analogy */
.analogy{background:linear-gradient(135deg,#f8f0ff,#f0e8ff);border:1.5px solid #c090e0;border-radius:10px;padding:1.1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .analogy{background:linear-gradient(135deg,#180828,#1c1030);border-color:#7050a0}
.analogy-title{font-size:.72rem;font-family:monospace;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#5a1a8c;margin-bottom:.5rem}
[data-theme=dark] .analogy-title{color:#c8a0f0}
.analogy p{font-size:.88rem;line-height:1.7;color:var(--text-color,#222);margin:0}

/* HTTP request/response visual */
.http-msg{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto}
.http-msg pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.7;white-space:pre}
.hm-method{color:#f0c080;font-weight:700}
.hm-path{color:#c8f0c8}
.hm-proto{color:#7ab8d8}
.hm-hdr-name{color:#c8a0f0}
.hm-hdr-val{color:#e0d8f0}
.hm-status{color:#f0a060;font-weight:700}
.hm-body{color:#d8d0e8;font-style:italic}
.hm-comment{color:#6a5a80}

/* Timeline / evolution */
.version-timeline{display:flex;gap:0;margin:1rem 0;border-radius:8px;overflow:hidden;border:1.5px solid var(--border-color,#e0e0e0)}
.vt-item{flex:1;padding:.8rem .6rem;text-align:center;border-right:1px solid var(--border-color,#e0e0e0)}
.vt-item:last-child{border-right:none}
.vt-version{font-size:.88rem;font-weight:700;font-family:monospace;margin-bottom:.2rem}
.vt-year{font-size:.68rem;font-family:monospace;color:var(--light-text,#888);margin-bottom:.4rem}
.vt-key{font-size:.72rem;color:var(--text-color,#444);line-height:1.5}

/* Comparison table */
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#5a1a8c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#7a3a9c}

/* Pipeline / multiplexing diagram */
.pipe-diagram{margin:1rem 0;overflow-x:auto}
.pipe-row{display:flex;gap:3px;min-width:500px;margin-bottom:4px;align-items:stretch}
.pipe-label{font-size:.72rem;font-family:monospace;min-width:80px;display:flex;align-items:center;color:var(--light-text,#666);flex-shrink:0}
.pipe-req{border-radius:5px;padding:6px 8px;font-size:.72rem;font-weight:600;text-align:center;border:1.5px solid transparent;display:flex;align-items:center;justify-content:center}
.pr-r1{background:#e8f1f9;border-color:#b0ccec;color:#1a3a5c}
.pr-r2{background:#e0f0ee;border-color:#90c8b8;color:#0a3a30}
.pr-r3{background:#e2f0e8;border-color:#a0d0a0;color:#1a4a1a}
.pr-r4{background:#faeee4;border-color:#e8b090;color:#6a2800}
.pr-r5{background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c}
.pr-wait{background:var(--bg-color,#f0f0f0);border-color:var(--border-color,#ddd);color:var(--light-text,#999);font-style:italic}
.pr-block{background:#faeaea;border-color:#e8b0b0;color:#6c1a1a}

/* QUIC frame types */
.frame-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:.6rem;margin:.8rem 0}
.frame-card{border-radius:8px;border:1.5px solid var(--border-color,#e0e0e0);background:var(--card-bg,#fff);padding:.7rem .9rem}
.frame-type{font-size:.8rem;font-weight:700;font-family:monospace;margin-bottom:.2rem}
.frame-id{font-size:.68rem;font-family:monospace;padding:2px 6px;border-radius:4px;display:inline-block;margin-bottom:.3rem;font-weight:700}
.frame-desc{font-size:.78rem;color:var(--text-color,#444);line-height:1.5}

/* Flow steps */
.flow-list{display:flex;flex-direction:column;gap:0;margin:1rem 0}
.fl-step{display:flex;gap:14px;padding:10px 14px;border-left:2px solid var(--border-color,#e0e0e0);margin-left:14px;position:relative}
.fl-step::before{content:attr(data-n);position:absolute;left:-14px;top:12px;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;color:#fff;background:var(--sc,#5a1a8c)}
.fl-step:last-child{border-left-color:transparent}
.fl-title{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin-bottom:.25rem}
.fl-detail{font-size:.85rem;color:var(--text-color,#444);line-height:1.6}
.fl-code{font-family:monospace;font-size:.78rem;display:inline-block;background:#0a1628;color:#c8a0f0;padding:2px 8px;border-radius:4px;margin-top:.3rem}

/* Two-col */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}

/* Lab box */
.lab-box{border:2px solid #7a3a9c;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#7a3a9c;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#7a3a9c;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}

/* Checklist */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#7a3a9c;margin-top:-.05rem}

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
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 2 · MODULE 08 · WEEK 6</div>
  <div class="mod-title">🌍 HTTP/1.1, HTTP/2, HTTP/3 and QUIC</div>
  <div class="mod-subtitle">Request/response · Methods · Headers · Status codes · Pipelining · Multiplexing · QUIC frames · NGFW inspection</div>
  <div class="mod-pills">
<span class="mod-pill">Intermediate</span>
<span class="mod-pill">Prerequisite: M05 TCP, M07 DNS</span>
<span class="mod-pill">RFC 9110 · RFC 9113 · RFC 9114</span>
<span class="mod-pill">Dominant Web Protocol</span>
<span class="mod-pill">3 Labs</span>
  </div>
</div>
<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">HTTP Evolution</button>
  <button class="tab-btn" onclick="vt(event,'t1')">HTTP/1.1</button>
  <button class="tab-btn" onclick="vt(event,'t2')">Methods and Status Codes</button>
  <button class="tab-btn" onclick="vt(event,'t3')">Key Headers</button>
  <button class="tab-btn" onclick="vt(event,'t4')">HTTP/2</button>
  <button class="tab-btn" onclick="vt(event,'t5')">HTTP/3 and QUIC</button>
  <button class="tab-btn" onclick="vt(event,'t6')">HTTPS and TLS</button>
  <button class="tab-btn" onclick="vt(event,'t7')">NGFW HTTP Inspection</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Checklist</button>
</div>
<!-- ════════════ TAB 0 — HTTP EVOLUTION ════════════ -->
<div id="t0" class="tab-pane active">
<p class="sep">FROM HTTP/0.9 TO HTTP/3 — 30 YEARS OF EVOLUTION</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📜</span><h3>Why HTTP Has Evolved So Dramatically</h3><span class="tag tag-purple">OVERVIEW</span></div>
  <div class="cp-body">
<p>HTTP (HyperText Transfer Protocol) is the application protocol that powers the web. Every browser request, every API call, every web service interaction uses HTTP. It began in 1991 as a trivially simple protocol for fetching HTML documents, and has evolved into a sophisticated multiplexed binary protocol because the web it carries has changed beyond recognition.</p>
<p>The core problem each version solves: <strong>latency</strong>. The web went from single HTML pages (1991) to pages requiring 100+ assets — CSS, JavaScript, images, fonts, API calls — all of which need to be fetched to render a page. Each protocol version attempts to reduce the number of round-trips and the total time to first byte.</p>
  </div>
</div>
<div class="version-timeline">
  <div class="vt-item" style="background:#f8f8f8">
<div class="vt-version">HTTP/0.9</div>
<div class="vt-year">1991</div>
<div class="vt-key">GET only. No headers. No status codes. Response is the file content.</div>
  </div>
  <div class="vt-item" style="background:#f0f0f8">
<div class="vt-version">HTTP/1.0</div>
<div class="vt-year">1996 RFC 1945</div>
<div class="vt-key">Headers added. POST, HEAD methods. Status codes. 1 request per TCP connection.</div>
  </div>
  <div class="vt-item" style="background:#e8e8f8">
<div class="vt-version">HTTP/1.1</div>
<div class="vt-year">1997 RFC 2068 / 2616 / 9110</div>
<div class="vt-key">Persistent connections. Chunked encoding. Host header (virtual hosting). Pipelining (limited use). Still dominant for simple APIs.</div>
  </div>
  <div class="vt-item" style="background:#e0e0f8">
<div class="vt-version">HTTP/2</div>
<div class="vt-year">2015 RFC 7540 / 9113</div>
<div class="vt-key">Binary framing. Multiplexing. Header compression (HPACK). Server push. One TCP connection per origin. Solves HOL blocking at HTTP layer but not TCP layer.</div>
  </div>
  <div class="vt-item" style="background:#d8d0f8">
<div class="vt-version">HTTP/3</div>
<div class="vt-year">2022 RFC 9114</div>
<div class="vt-key">Runs over QUIC (UDP). Eliminates TCP HOL blocking. 0-RTT connection resumption. Connection migration. Mandatory encryption.</div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🌐</span><h3>HTTP in the Protocol Stack</h3><span class="tag tag-blue">POSITION</span></div>
  <div class="cp-body">


```python
/* Protocol stack comparison */

HTTP/1.1 and HTTP/2:          HTTP/3:
┌─────────────────┐           ┌─────────────────┐
│   HTTP/1.1 or   │           │     HTTP/3       │
│     HTTP/2      │           ├─────────────────┤
├─────────────────┤           │      QUIC        │
│   TLS 1.2/1.3   │           │  (includes TLS) │
├─────────────────┤           ├─────────────────┤
│      TCP        │           │      UDP         │
├─────────────────┤           ├─────────────────┤
│      IP         │           │      IP          │
└─────────────────┘           └─────────────────┘

/* HTTP is always text-based in HTTP/1.1 (line-delimited) */
/* HTTP/2 is binary framing over the same TCP+TLS */
/* HTTP/3 moves the entire stack to UDP with QUIC handling */
/* reliability, ordering, and encryption that TCP+TLS provided */

/* Check which HTTP version a server uses */
curl -v --http1.1 https://google.com 2>&1 | grep '&1 | grep '&1 | grep '# if curl has HTTP/3
```


  </div>
</div>
</div>
<!-- ════════════ TAB 1 — HTTP/1.1 ════════════ -->
<div id="t1" class="tab-pane">
<p class="sep">HTTP/1.1 — THE CLASSIC TEXT-BASED PROTOCOL</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📨</span><h3>HTTP/1.1 Request Format</h3><span class="tag tag-blue">FORMAT</span></div>
  <div class="cp-body">
<p>HTTP/1.1 is a plain-text protocol. Every message — request or response — is human-readable ASCII, line-delimited. A request consists of a <strong>request line</strong>, followed by <strong>headers</strong>, a blank line (CRLF), and optionally a <strong>body</strong>.</p>
<div class="http-msg">
<pre><span class="hm-method">POST</span> <span class="hm-path">/api/v1/users</span> <span class="hm-proto">HTTP/1.1</span>            <span class="hm-comment">← Request line: Method SP Path SP Version CRLF</span>
<span class="hm-hdr-name">Host:</span> <span class="hm-hdr-val">api.example.com</span>                  <span class="hm-comment">← Mandatory in HTTP/1.1 (virtual hosting)</span>
<span class="hm-hdr-name">Content-Type:</span> <span class="hm-hdr-val">application/json</span>         <span class="hm-comment">← Body format</span>
<span class="hm-hdr-name">Content-Length:</span> <span class="hm-hdr-val">27</span>                    <span class="hm-comment">← Body length in bytes</span>
<span class="hm-hdr-name">Authorization:</span> <span class="hm-hdr-val">Bearer eyJhbGciOiJIUzI1...</span>
<span class="hm-hdr-name">Accept:</span> <span class="hm-hdr-val">application/json</span>
<span class="hm-hdr-name">User-Agent:</span> <span class="hm-hdr-val">MyApp/2.1 (Linux x86_64)</span>
<span class="hm-hdr-name">Connection:</span> <span class="hm-hdr-val">keep-alive</span>
                                         <span class="hm-comment">← Empty line (CRLF) separates headers from body</span>
<span class="hm-body">{"name":"Ajay","role":"admin"}</span>         <span class="hm-comment">← Request body (27 bytes)</span></pre>
</div>
<div class="http-msg" style="margin-top:.5rem">
<pre><span class="hm-proto">HTTP/1.1</span> <span class="hm-status">201 Created</span>                   <span class="hm-comment">← Status line: Version SP Status-Code SP Reason CRLF</span>
<span class="hm-hdr-name">Content-Type:</span> <span class="hm-hdr-val">application/json</span>
<span class="hm-hdr-name">Content-Length:</span> <span class="hm-hdr-val">45</span>
<span class="hm-hdr-name">Location:</span> <span class="hm-hdr-val">/api/v1/users/42</span>              <span class="hm-comment">← URL of created resource</span>
<span class="hm-hdr-name">Set-Cookie:</span> <span class="hm-hdr-val">session=abc123; HttpOnly; Secure; SameSite=Strict</span>
<span class="hm-hdr-name">X-Request-ID:</span> <span class="hm-hdr-val">7f3a9c2d</span>
<span class="hm-hdr-name">Date:</span> <span class="hm-hdr-val">Wed, 18 Mar 2026 10:00:00 GMT</span>
<span class="hm-body">{"id":42,"name":"Ajay","role":"admin"}</span></pre>
</div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Persistent Connections and Pipelining</h3><span class="tag tag-teal">CONNECTIONS</span></div>
  <div class="cp-body">
<p>HTTP/1.0 opened a new TCP connection for every request — 3-way handshake + TLS handshake for every single asset. A page with 30 assets = 30 TCP connections. HTTP/1.1 introduced <strong>persistent connections</strong> (keep-alive) as the default: after a response, the TCP connection stays open for subsequent requests.</p>
<div class="pipe-diagram">
<div class="pipe-row">
<div class="pipe-label">HTTP/1.0</div>
<div class="pipe-req pr-r1" style="flex:1">TCP SYN</div>
<div class="pipe-req pr-r1" style="flex:1.5">Request 1</div>
<div class="pipe-req pr-r2" style="flex:1.5">Response 1</div>
<div class="pipe-req pr-r1" style="flex:.8">FIN</div>
<div class="pipe-req pr-r3" style="flex:1">TCP SYN</div>
<div class="pipe-req pr-r3" style="flex:1.5">Request 2</div>
<div class="pipe-req pr-r4" style="flex:1.5">Response 2</div>
<div class="pipe-req pr-r3" style="flex:.8">FIN</div>
</div>
<div class="pipe-row">
<div class="pipe-label">HTTP/1.1</div>
<div class="pipe-req pr-r1" style="flex:1">TCP SYN</div>
<div class="pipe-req pr-r1" style="flex:1.5">Request 1</div>
<div class="pipe-req pr-r2" style="flex:1.5">Response 1</div>
<div class="pipe-req pr-r3" style="flex:1.5">Request 2</div>
<div class="pipe-req pr-r4" style="flex:1.5">Response 2</div>
<div class="pipe-req pr-r5" style="flex:1">Req 3…</div>
</div>
<div class="pipe-row">
<div class="pipe-label">HOL block</div>
<div class="pipe-req pr-r1" style="flex:1">TCP SYN</div>
<div class="pipe-req pr-r1" style="flex:2">Large Request 1 (slow)</div>
<div class="pipe-req pr-block" style="flex:2">Req 2 BLOCKED</div>
<div class="pipe-req pr-block" style="flex:2">Req 3 BLOCKED</div>
<div class="pipe-req pr-r2" style="flex:1.5">Resp 1</div>
</div>
</div>
<p><strong>Head-of-Line (HOL) blocking</strong> is HTTP/1.1's critical weakness: responses must be returned in request order on a single connection. If request 1 is slow (large file, slow server), requests 2, 3, 4 all wait behind it even if they'd complete instantly. Browsers work around this by opening <strong>6 parallel TCP connections per origin</strong> — but this wastes resources and still isn't a clean solution.</p>
<h4>Chunked Transfer Encoding</h4>


```yaml
/* Server sends response body in chunks — no Content-Length needed */
HTTP/1.1 200 OK
Transfer-Encoding: chunked
Content-Type: text/html

1a               ← chunk size in hex: 0x1a = 26 bytes
This is the first chunk.
13               ← 0x13 = 19 bytes
And the second chunk.
0                ← zero-length chunk = end of body
                 ← trailing CRLF

/* Used for: streaming responses, server-sent events */
/* server starts sending before it knows total size */
```


  </div>
</div>
</div>
<!-- ════════════ TAB 2 — METHODS AND STATUS CODES ════════════ -->
<div id="t2" class="tab-pane">
<p class="sep">HTTP METHODS AND STATUS CODES — THE COMPLETE REFERENCE</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📋</span><h3>HTTP Request Methods</h3><span class="tag tag-blue">METHODS</span></div>
  <div class="cp-body">
<table class="t-table">
<thead><tr><th>Method</th><th>Semantics</th><th>Safe?</th><th>Idempotent?</th><th>Has Body?</th><th>Common Use</th></tr></thead>
<tbody>
<tr><td><code>GET</code></td><td>Retrieve a resource</td><td>Yes</td><td>Yes</td><td>No (ignored)</td><td>Fetch web page, API data, images</td></tr>
<tr><td><code>POST</code></td><td>Create/submit data</td><td>No</td><td>No</td><td>Yes</td><td>Create resource, form submit, login</td></tr>
<tr><td><code>PUT</code></td><td>Replace a resource completely</td><td>No</td><td>Yes</td><td>Yes</td><td>Replace entire user record</td></tr>
<tr><td><code>PATCH</code></td><td>Partially update a resource</td><td>No</td><td>No</td><td>Yes</td><td>Change user's email only</td></tr>
<tr><td><code>DELETE</code></td><td>Remove a resource</td><td>No</td><td>Yes</td><td>Optional</td><td>Delete a user, file, record</td></tr>
<tr><td><code>HEAD</code></td><td>GET but response body omitted</td><td>Yes</td><td>Yes</td><td>No</td><td>Check if resource exists/changed (ETag/Last-Modified)</td></tr>
<tr><td><code>OPTIONS</code></td><td>Describe communication options</td><td>Yes</td><td>Yes</td><td>No</td><td>CORS preflight, discover allowed methods</td></tr>
<tr><td><code>CONNECT</code></td><td>Establish a tunnel through proxy</td><td>No</td><td>No</td><td>No</td><td>HTTPS through HTTP proxy (CONNECT example.com:443)</td></tr>
<tr><td><code>TRACE</code></td><td>Echo request for debugging</td><td>Yes</td><td>Yes</td><td>No</td><td>Diagnostic (mostly disabled — XST attack risk)</td></tr>
</tbody>
</table>
<div class="note"><p>💡 <strong>Safe</strong> = no side effects (read-only). <strong>Idempotent</strong> = calling multiple times has same effect as calling once. These properties matter for retry logic (retrying a non-idempotent POST could create duplicates) and NGFW policy (blocking unsafe methods on read-only APIs).</p></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔢</span><h3>HTTP Status Codes — Every Category</h3><span class="tag tag-teal">STATUS CODES</span></div>
  <div class="cp-body">
<div class="two-col">
<div>
<h4>1xx — Informational</h4>
<ul>
<li><code>100 Continue</code> — server received request headers, client should send body</li>
<li><code>101 Switching Protocols</code> — upgrading to WebSocket or HTTP/2</li>
</ul>
<h4>2xx — Success</h4>
<ul>
<li><code>200 OK</code> — standard success</li>
<li><code>201 Created</code> — resource created (POST)</li>
<li><code>204 No Content</code> — success, no body (DELETE)</li>
<li><code>206 Partial Content</code> — range request fulfilled</li>
</ul>
<h4>3xx — Redirection</h4>
<ul>
<li><code>301 Moved Permanently</code> — permanent redirect, update bookmarks</li>
<li><code>302 Found</code> — temporary redirect</li>
<li><code>304 Not Modified</code> — cached version is still valid (ETag/If-None-Match)</li>
<li><code>307 Temporary Redirect</code> — keep method (don't change POST → GET)</li>
<li><code>308 Permanent Redirect</code> — like 301 but preserves method</li>
</ul>
</div>
<div>
<h4>4xx — Client Errors</h4>
<ul>
<li><code>400 Bad Request</code> — malformed request syntax</li>
<li><code>401 Unauthorized</code> — authentication required</li>
<li><code>403 Forbidden</code> — authenticated but not authorised</li>
<li><code>404 Not Found</code> — resource doesn't exist</li>
<li><code>405 Method Not Allowed</code> — wrong HTTP method</li>
<li><code>408 Request Timeout</code> — client too slow</li>
<li><code>409 Conflict</code> — state conflict (duplicate resource)</li>
<li><code>429 Too Many Requests</code> — rate limited</li>
</ul>
<h4>5xx — Server Errors</h4>
<ul>
<li><code>500 Internal Server Error</code> — generic server error</li>
<li><code>502 Bad Gateway</code> — upstream proxy/backend error</li>
<li><code>503 Service Unavailable</code> — server overloaded or maintenance</li>
<li><code>504 Gateway Timeout</code> — upstream took too long</li>
</ul>
</div>
</div>
<div class="ins"><p>💡 <strong>NGFW status code monitoring:</strong> A spike in 401/403 responses from a single source may indicate a credential stuffing or brute-force attack. A flood of 500 responses may indicate a vulnerability scan or SQL injection attempt. A stream of 404s from a single source is likely a web crawler or directory enumeration scan. These patterns are detectable in your NGFW's HTTP inspection logs.</p></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 3 — KEY HEADERS ════════════ -->
<div id="t3" class="tab-pane">
<p class="sep">KEY HTTP HEADERS — REQUEST, RESPONSE, AND SECURITY HEADERS</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📋</span><h3>Critical Request Headers</h3><span class="tag tag-purple">REQUEST HEADERS</span></div>
  <div class="cp-body">
<table class="t-table">
<thead><tr><th>Header</th><th>Format / Values</th><th>Purpose</th><th>NGFW Relevance</th></tr></thead>
<tbody>
<tr><td><code>Host</code></td><td><code>api.example.com</code></td><td>Target virtual host. Mandatory in HTTP/1.1. Enables multiple sites on one IP.</td><td>URL filtering — identifies domain even when IP is shared. SNI cross-check for TLS inspection.</td></tr>
<tr><td><code>User-Agent</code></td><td><code>Mozilla/5.0 (Linux...)</code></td><td>Client application identity. Browser, OS, version.</td><td>Detect bots, scanners, known malware user-agents (C2 beaconing uses custom UA strings).</td></tr>
<tr><td><code>Authorization</code></td><td><code>Bearer token</code> / <code>Basic base64</code></td><td>Authentication credential.</td><td>DLP: detect credential exfiltration in plaintext HTTP. Inspect for known compromised tokens.</td></tr>
<tr><td><code>Cookie</code></td><td><code>session=abc; pref=dark</code></td><td>Session state sent to server.</td><td>Session hijacking detection. Cookie flags (HttpOnly, Secure) enforcement.</td></tr>
<tr><td><code>Referer</code></td><td><code>https://google.com/search?q=...</code></td><td>Where the user came from. (Yes, historically misspelled.)</td><td>Data leakage — Referer may contain sensitive search queries or internal URLs.</td></tr>
<tr><td><code>Content-Type</code></td><td><code>application/json</code> / <code>multipart/form-data</code></td><td>Format of request body.</td><td>DPI dispatch: parse body as JSON/XML/form-data for content inspection.</td></tr>
<tr><td><code>X-Forwarded-For</code></td><td><code>203.x.x.x, 10.0.0.1</code></td><td>Original client IP when going through proxies.</td><td>Real client IP for logging and policy. Must validate chain — easily forged by clients.</td></tr>
<tr><td><code>Origin</code></td><td><code>https://app.example.com</code></td><td>Origin of cross-origin request (CORS).</td><td>Detect cross-origin attacks. Origin ≠ Host may indicate CSRF or XSS attempt.</td></tr>
</tbody>
</table>
  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>Security Response Headers — What Your NGFW Should Enforce</h3><span class="tag tag-green">SECURITY HEADERS</span></div>
  <div class="cp-body">
<p>Security headers are HTTP response headers that instruct the browser to enable security protections. A WAF or NGFW proxy can inject missing security headers into responses:</p>


```bash
/* Security headers — every production server should send these */

Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
  # HSTS: browser must use HTTPS for this domain for 1 year
  # Prevents SSL stripping attacks
  # preload: submit to browser preload list

Content-Security-Policy: default-src 'self'; script-src 'self' cdn.example.com; object-src 'none'
  # CSP: whitelist of allowed content sources
  # Prevents XSS by blocking inline scripts and untrusted sources

X-Frame-Options: DENY
  # Prevent clickjacking — page cannot be embedded in iframe
  # Superseded by CSP frame-ancestors, but still widely needed

X-Content-Type-Options: nosniff
  # Browser must not MIME-sniff — prevents content-type confusion attacks

Referrer-Policy: strict-origin-when-cross-origin
  # Controls what goes in Referer header on cross-origin requests
  # Prevents leaking sensitive URLs to third parties

Permissions-Policy: camera=(), microphone=(), geolocation=(self)
  # Restrict browser APIs — prevent malicious pages accessing camera/mic

Set-Cookie: session=abc; HttpOnly; Secure; SameSite=Strict; Path=/
  # HttpOnly: JS cannot access cookie (prevents XSS cookie theft)
  # Secure: only sent over HTTPS
  # SameSite=Strict: not sent on cross-site requests (prevents CSRF)
```


  </div>
</div>
</div>
<!-- ════════════ TAB 4 — HTTP/2 ════════════ -->
<div id="t4" class="tab-pane">
<p class="sep">HTTP/2 — BINARY FRAMING AND MULTIPLEXING</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>HTTP/2 Core Innovations</h3><span class="tag tag-purple">HTTP/2</span></div>
  <div class="cp-body">
<p>HTTP/2 (RFC 9113) keeps the same HTTP semantics (methods, status codes, headers) but completely replaces the wire format. It moves from text-based line-by-line messages to a <strong>binary framing layer</strong> that enables multiplexing — multiple concurrent request/response exchanges over a single TCP connection.</p>
<p>Four key innovations:</p>
<ul>
<li><strong>Binary framing</strong> — messages broken into typed binary frames instead of text lines. More efficient to parse, less error-prone, enables features impossible in text</li>
<li><strong>Multiplexing</strong> — multiple streams (each stream = one request/response pair) interleaved on the same TCP connection. No more 6-connection limit. No more HOL blocking at the HTTP layer</li>
<li><strong>HPACK header compression</strong> — headers compressed using a shared static table + dynamic table. Eliminates the overhead of repeating User-Agent, Cookie, Authorization on every request</li>
<li><strong>Server push</strong> — server can proactively send resources the client will need (push CSS/JS when it sends HTML) without waiting for the client to request them</li>
</ul>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📊</span><h3>HTTP/2 Streams and Framing</h3><span class="tag tag-blue">STREAMS</span></div>
  <div class="cp-body">
<p>An HTTP/2 <strong>stream</strong> is a bidirectional sequence of frames on a single TCP connection. Each stream has an integer ID (client-initiated streams use odd IDs: 1, 3, 5…; server-initiated use even IDs). Multiple streams run concurrently — frames from different streams are interleaved:</p>
<div class="pipe-diagram">
<div class="pipe-row">
<div class="pipe-label">HTTP/1.1<br>(6 conns)</div>
<div class="pipe-req pr-r1" style="flex:1.5">Conn1: HTML</div>
<div class="pipe-req pr-r2" style="flex:1.5">Conn2: CSS</div>
<div class="pipe-req pr-r3" style="flex:1.5">Conn3: JS</div>
<div class="pipe-req pr-r4" style="flex:1.5">Conn4: img1</div>
<div class="pipe-req pr-r5" style="flex:1.5">Conn5: img2</div>
<div class="pipe-req pr-block" style="flex:1">Wait...</div>
</div>
<div class="pipe-row">
<div class="pipe-label">HTTP/2<br>(1 conn)</div>
<div class="pipe-req pr-r1" style="flex:.6">S1:H</div>
<div class="pipe-req pr-r2" style="flex:.6">S3:H</div>
<div class="pipe-req pr-r3" style="flex:.6">S5:H</div>
<div class="pipe-req pr-r1" style="flex:.8">S1:DATA</div>
<div class="pipe-req pr-r4" style="flex:.6">S7:H</div>
<div class="pipe-req pr-r2" style="flex:.8">S3:DATA</div>
<div class="pipe-req pr-r5" style="flex:.6">S9:H</div>
<div class="pipe-req pr-r3" style="flex:.8">S5:DATA</div>
<div class="pipe-req pr-r4" style="flex:.8">S7:DATA</div>
<div class="pipe-req pr-r5" style="flex:.8">S9:DATA</div>
</div>
</div>
<div class="cb"><pre><span class="cm">/* HTTP/2 Frame format */</span>
+-----------------------------------------------+
| Length (24 bits) | Type (8 bits) | Flags (8b) |
+-----------------------------------------------+
|R|            Stream ID (31 bits)               |
+-----------------------------------------------+
|                  Frame Payload                 |
+-----------------------------------------------+
 
<span class="cm">/* Frame types */</span>
Type 0x0 DATA:        <span class="cs">request/response body data</span>
Type 0x1 HEADERS:     <span class="cs">request/response headers (HPACK compressed)</span>
Type 0x2 PRIORITY:    <span class="cs">stream dependency and weight for scheduling</span>
Type 0x3 RST_STREAM:  <span class="cs">cancel/error a specific stream</span>
Type 0x4 SETTINGS:    <span class="cs">negotiate connection parameters (max frame size, max streams)</span>
Type 0x5 PUSH_PROMISE:<span class="cs">server announces pushed resource</span>
Type 0x6 PING:        <span class="cs">keepalive and RTT measurement</span>
Type 0x7 GOAWAY:      <span class="cs">graceful connection shutdown — last processed stream ID</span>
Type 0x8 WINDOW_UPDATE:<span class="cs">flow control — increase receive window</span>
Type 0x9 CONTINUATION:<span class="cs">continue HEADERS frame if too large for one frame</span>
<span class="cm">/* HEADERS frame example — HPACK compressed */</span>
<span class="cm">/* Static table entry: :method GET = index 2, :path / = index 4 */</span>
\x82           <span class="cm"># :method = GET  (index 2 from static table)</span>
\x84           <span class="cm"># :path = /       (index 4)</span>
\x86           <span class="cm"># :scheme = https (index 6)</span>
\x41 \x8a...   <span class="cm"># :authority = www.google.com (literal with indexing)</span></pre></div>
<div class="warn"><p>⚠️ <strong>HTTP/2 still has TCP HOL blocking.</strong> While HTTP/2 eliminates application-layer head-of-line blocking (requests no longer wait behind each other at the HTTP layer), it still runs over TCP. If a single TCP packet is lost, TCP holds ALL streams until retransmission completes — even streams that have no dependency on the lost data. This is the core motivation for HTTP/3's move to QUIC/UDP.</p></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🗜️</span><h3>HPACK Header Compression</h3><span class="tag tag-teal">HPACK</span></div>
  <div class="cp-body">
<p>HTTP headers are verbose and repetitive. A typical request sends the same User-Agent, Accept, Cookie, and Authorization headers on every request — hundreds of bytes of overhead per request. HPACK (RFC 7541) compresses these to a handful of bytes using two techniques:</p>
<ul>
<li><strong>Static table</strong> — 61 pre-defined name/value pairs that are indexed by number. <code>:method GET</code> = index 2 (1 byte). <code>:status 200</code> = index 8 (1 byte). Eliminates overhead for common headers entirely.</li>
<li><strong>Dynamic table</strong> — previously seen name/value pairs are added to a shared dynamic table. Subsequent occurrences are replaced by their table index. A long Cookie header sent once can be referenced by 1 byte on all future requests.</li>
</ul>


```python
/* HPACK compression example */
Request 1 — first time User-Agent is sent:
  Header: user-agent: Mozilla/5.0 (Linux; Android 11)
  Wire bytes: ~45 bytes (literal encoding, added to dynamic table at index 62)

Request 2 — same User-Agent:
  Wire bytes: \xbe (1 byte = index 62 in dynamic table)
  Savings: 98%

/* CRIME and BREACH attacks — why HPACK must be careful */
# If attacker can inject chosen plaintext adjacent to secrets in compressed data,
# they can observe compression ratio to infer secret values byte by byte.
# TLS compression was disabled due to CRIME. HPACK deliberately does NOT
# compress across streams (separate compression contexts) to mitigate.
```


  </div>
</div>
</div>
<!-- ════════════ TAB 5 — HTTP/3 AND QUIC ════════════ -->
<div id="t5" class="tab-pane">
<p class="sep">HTTP/3 AND QUIC — REIMAGINING THE WEB TRANSPORT STACK</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🚀</span><h3>Why QUIC Was Invented</h3><span class="tag tag-orange">MOTIVATION</span></div>
  <div class="cp-body">
<p>HTTP/2 over TCP still had TCP's fundamental limitations. Fixing these would require changing TCP itself — which means changing every operating system kernel worldwide. That's essentially impossible at any reasonable timescale. Google's solution: <strong>build a new transport protocol in user space over UDP</strong>, implement it in the browser and server, and deploy it without any OS changes.</p>
<p>QUIC (RFC 9000) addresses four problems that TCP cannot solve without OS-level changes:</p>
<ul>
<li><strong>TCP HOL blocking</strong> — a lost TCP packet stalls all HTTP/2 streams. QUIC streams are independent: a lost QUIC packet only stalls the one stream it belongs to</li>
<li><strong>Connection establishment latency</strong> — TCP requires 1 RTT for handshake + 1 RTT for TLS = 2 RTTs before first byte. QUIC combines transport and crypto handshake in 1 RTT. With 0-RTT, returning clients can send data immediately</li>
<li><strong>Connection migration</strong> — TCP connections are tied to a 4-tuple (src IP, src port, dst IP, dst port). If you walk from WiFi to cellular, your IP changes, TCP connection breaks. QUIC uses Connection IDs — connections survive IP changes</li>
<li><strong>Ossification</strong> — TCP middleboxes (firewalls, NATs, proxies) inspect and sometimes modify TCP headers. This prevented TCP from evolving. QUIC is encrypted — middleboxes see only UDP packets, cannot inspect or modify internals</li>
</ul>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📦</span><h3>QUIC Architecture</h3><span class="tag tag-blue">QUIC INTERNALS</span></div>
  <div class="cp-body">


```python
/* QUIC packet structure (simplified) */
┌─────────────────────────────────────────────────────┐
│  UDP Header (8 bytes)                               │
├─────────────────────────────────────────────────────┤
│  QUIC Long/Short Header                             │
│  - Header Form (1 bit): Long=1, Short=0             │
│  - Connection ID (0–20 bytes): identifies connection│
│    without IP/port (enables migration!)             │
│  - Packet Number (1–4 bytes): sequence for ACK      │
├─────────────────────────────────────────────────────┤
│  QUIC Frames (encrypted with TLS 1.3)              │
│  - STREAM frames: carry application data            │
│  - ACK frames: acknowledge received packets         │
│  - CRYPTO frames: TLS handshake messages            │
│  - PADDING, PING, CONNECTION_CLOSE, etc.            │
└─────────────────────────────────────────────────────┘

/* QUIC connection establishment — 1-RTT */
Client → Server: Initial (ClientHello inside CRYPTO frame)
Server → Client: Initial (ServerHello, certificates, Finished) + Handshake + 1-RTT data
Client → Server: Handshake (Finished) + 1-RTT data ← FIRST DATA HERE

vs TLS over TCP: SYN → SYN+ACK → ACK → ClientHello → ServerHello...Finished → data
                 That's 2 RTTs minimum before data flows.

/* 0-RTT resumption */
Client received a "session ticket" from prior connection:
Client → Server: 0-RTT data immediately (with replay-protected pre-shared key)
                 Server accepts 0-RTT data — zero round trips!
Caveat: 0-RTT data is replay-vulnerable — only safe for idempotent requests (GET)
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📊</span><h3>QUIC Frame Types</h3><span class="tag tag-teal">FRAMES</span></div>
  <div class="cp-body">
<div class="frame-grid">
<div class="frame-card">
<div class="frame-type">STREAM</div>
<div class="frame-id" style="background:#e8f1f9;color:#1a3a5c">Type 0x08–0x0f</div>
<div class="frame-desc">Carries application data for a specific stream. Flags control FIN (end of stream), LEN, and OFF (offset). Multiple streams multiplexed, each independently ordered.</div>
</div>
<div class="frame-card">
<div class="frame-type">ACK</div>
<div class="frame-id" style="background:#e0f0ee;color:#0a3a30">Type 0x02–0x03</div>
<div class="frame-desc">Acknowledges received QUIC packets. ACK ranges allow selective acknowledgement natively — no need for SACK option like TCP. Includes ACK delay measurement.</div>
</div>
<div class="frame-card">
<div class="frame-type">CRYPTO</div>
<div class="frame-id" style="background:#ede8f5;color:#3a1a6c">Type 0x06</div>
<div class="frame-desc">Carries TLS handshake messages (ClientHello, ServerHello, Certificate, Finished). Used during connection establishment before 1-RTT keys are available.</div>
</div>
<div class="frame-card">
<div class="frame-type">NEW_CONNECTION_ID</div>
<div class="frame-id" style="background:#e2f0e8;color:#1a4a1a">Type 0x18</div>
<div class="frame-desc">Server provides new Connection IDs client can use. Enables connection migration — client switches to new ID on network change, preventing linkability.</div>
</div>
<div class="frame-card">
<div class="frame-type">MAX_DATA / MAX_STREAM_DATA</div>
<div class="frame-id" style="background:#fdf4dc;color:#5a3800">Type 0x10–0x13</div>
<div class="frame-desc">Flow control — increase the connection-level or stream-level receive window. Equivalent to TCP's window update but per-stream.</div>
</div>
<div class="frame-card">
<div class="frame-type">CONNECTION_CLOSE</div>
<div class="frame-id" style="background:#faeaea;color:#6c1a1a">Type 0x1c–0x1d</div>
<div class="frame-desc">Graceful connection termination. Carries error code and reason phrase. Unlike TCP FIN — closes entire connection, not individual streams.</div>
</div>
</div>
  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🌐</span><h3>HTTP/3 — HTTP over QUIC</h3><span class="tag tag-green">HTTP/3</span></div>
  <div class="cp-body">
<p>HTTP/3 (RFC 9114) is HTTP/2's semantics (same methods, status codes, header compression) re-implemented over QUIC instead of TCP+TLS. Key differences from HTTP/2:</p>
<ul>
<li><strong>QPACK instead of HPACK</strong> — header compression adapted for QUIC's independent stream ordering. HPACK's dynamic table requires strict ordering (which TCP guaranteed); QPACK uses separate encoder/decoder streams to avoid this dependency</li>
<li><strong>No TCP HOL blocking</strong> — QUIC streams are truly independent. A lost UDP packet only pauses the stream it belongs to</li>
<li><strong>Stream IDs</strong> — HTTP/3 uses QUIC stream IDs directly. Bidirectional streams for request/response, unidirectional for control and QPACK encoder/decoder</li>
<li><strong>Mandatory HTTPS</strong> — QUIC always uses TLS 1.3; there is no "plain HTTP/3 without TLS"</li>
</ul>


```bash
# Detect HTTP/3 support — look for Alt-Svc header in HTTP/1.1 or HTTP/2 response
curl -I https://cloudflare.com | grep -i alt-svc
# alt-svc: h3=":443"; ma=86400
# "I support HTTP/3 (h3) on port 443, this hint is valid for 86400 seconds"

# Test HTTP/3 with curl (requires --http3 support)
curl --http3 -v https://cloudflare.com 2>&1 | head -20

# Wireshark capture of QUIC traffic
# Filter: udp.port == 443 (QUIC uses UDP 443)
# QUIC packets appear as "QUIC" in protocol column
# Content is encrypted — only metadata visible without TLS keys

# Provide TLS keys to Wireshark for decryption
SSLKEYLOGFILE=/tmp/keys.log curl --http3 https://cloudflare.com
# In Wireshark: Edit → Preferences → Protocols → TLS → Master Secret log
```


  </div>
</div>
</div>
<!-- ════════════ TAB 6 — HTTPS AND TLS ════════════ -->
<div id="t6" class="tab-pane">
<p class="sep">HTTPS — HTTP OVER TLS, AND WHY THE URL BAR IS GREEN</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔒</span><h3>HTTPS — What It Does and What It Doesn't</h3><span class="tag tag-blue">HTTPS</span></div>
  <div class="cp-body">
<p>HTTPS is simply HTTP running inside a TLS tunnel. TLS (Transport Layer Security) adds three properties to the connection:</p>
<ul>
<li><strong>Confidentiality</strong> — all HTTP content (headers, body, URL path) is encrypted. An on-path attacker can see the destination IP and SNI hostname, but cannot read the request path, headers, cookies, or response body</li>
<li><strong>Integrity</strong> — TLS MAC ensures the content hasn't been tampered with in transit. Attacker cannot modify HTTP responses (inject ads, malware) without detection</li>
<li><strong>Authentication</strong> — the server's TLS certificate proves its identity. Your browser verifies the certificate was issued by a trusted CA and matches the hostname</li>
</ul>
<div class="warn"><p>⚠️ <strong>What HTTPS does NOT protect:</strong> The destination hostname is visible in the TLS SNI (Server Name Indication) extension — the server needs to know which certificate to present before decryption. The destination IP is always visible (IP routing requires it). HTTP/2 header sizes are visible even though content is encrypted. HTTPS proves the server is who it claims to be — it does NOT prove the site is legitimate or safe.</p></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🤝</span><h3>TLS Handshake Timeline — HTTP/1.1 vs HTTP/2 vs HTTP/3</h3><span class="tag tag-teal">HANDSHAKE</span></div>
  <div class="cp-body">


```bash
/* HTTP/1.1 over TLS 1.3 — minimum 2 RTTs before data */
RTT 0: → TCP SYN
        ← TCP SYN+ACK
RTT 1: → TCP ACK + TLS ClientHello (with key_share)
        ← TLS ServerHello + Certificate + CertVerify + Finished (encrypted)
RTT 2: → TLS Finished + HTTP GET   ← HTTP response arrives
                                      ← DATA arrives

/* HTTP/2 over TLS 1.3 — same, but ALPN negotiates h2 in handshake */
TLS ClientHello includes: ALPN extension ["h2", "http/1.1"]
TLS ServerHello includes: ALPN selected "h2"
After handshake: HTTP/2 binary framing on the same connection

/* HTTP/3 over QUIC — 1 RTT (0-RTT for returning clients) */
RTT 0: → QUIC Initial (ClientHello in CRYPTO frame)
        ← QUIC Initial+Handshake (ServerHello+Cert+Finished)
           + 1-RTT data (server can already send response!)
RTT 1: → QUIC Handshake Finished + HTTP/3 request arrives
        ← (server was already sending response from RTT 0)

/* ALPN — Application-Layer Protocol Negotiation */
# Allows HTTP version negotiation within TLS handshake
# No extra round-trip needed
# Values: "h3" = HTTP/3, "h2" = HTTP/2, "http/1.1" = HTTP/1.1
```


  </div>
</div>
</div>
<!-- ════════════ TAB 7 — NGFW HTTP INSPECTION ════════════ -->
<div id="t7" class="tab-pane">
<p class="sep">NGFW HTTP INSPECTION — URL FILTERING, DPI, AND SSL INSPECTION</p>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🛡️</span><h3>HTTP Inspection in an NGFW — What Gets Inspected</h3><span class="tag tag-red">INSPECTION</span></div>
  <div class="cp-body">
<p>For plain HTTP traffic (port 80), an NGFW can inspect everything. For HTTPS, the NGFW must either trust the SNI (limited information) or perform SSL inspection (full access but requires certificate deployment).</p>
<table class="t-table">
<thead><tr><th>Element</th><th>Visible in HTTP</th><th>Visible in HTTPS (no SSL inspection)</th><th>Visible with SSL Inspection</th></tr></thead>
<tbody>
<tr><td>Destination IP</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Destination hostname</td><td>Host header</td><td>TLS SNI only</td><td>Host header</td></tr>
<tr><td>URL path and query string</td><td>Yes (<code>GET /path?q=...</code>)</td><td>No (encrypted)</td><td>Yes</td></tr>
<tr><td>HTTP method</td><td>Yes</td><td>No</td><td>Yes</td></tr>
<tr><td>Request headers (Cookie, Auth)</td><td>Yes</td><td>No</td><td>Yes</td></tr>
<tr><td>Response status code</td><td>Yes</td><td>No</td><td>Yes</td></tr>
<tr><td>Response body (file content)</td><td>Yes</td><td>No</td><td>Yes</td></tr>
<tr><td>File downloads (malware scan)</td><td>Yes</td><td>No</td><td>Yes</td></tr>
<tr><td>TLS certificate</td><td>N/A</td><td>Yes (server cert visible)</td><td>Yes</td></tr>
<tr><td>TLS version and cipher suite</td><td>N/A</td><td>Yes (during handshake)</td><td>Yes</td></tr>
</tbody>
</table>
  </div>
</div>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔬</span><h3>SSL Inspection — How NGFW Decrypts HTTPS</h3><span class="tag tag-purple">SSL INSPECTION</span></div>
  <div class="cp-body">
<p>SSL inspection (also called TLS inspection, SSL bump, or MITM proxy) allows an NGFW to decrypt, inspect, and re-encrypt HTTPS traffic. It is the most powerful — and most controversial — NGFW capability.</p>
<div class="flow-list">
<div class="fl-step" data-n="1" style="--sc:#5a1a8c">
<div>
<div class="fl-title">Client initiates TLS connection to server</div>
<div class="fl-detail">Client sends TLS ClientHello to server IP. The NGFW intercepts this connection — it acts as a transparent proxy.</div>
</div>
</div>
<div class="fl-step" data-n="2" style="--sc:#5a1a8c">
<div>
<div class="fl-title">NGFW establishes TLS with the real server</div>
<div class="fl-detail">NGFW opens its own separate TLS connection to the destination server. It receives and validates the server's real certificate. NGFW now has the session keys — it can decrypt all server traffic.</div>
<div class="fl-code">NGFW ↔ Real Server: legitimate TLS with server's real cert</div>
</div>
</div>
<div class="fl-step" data-n="3" style="--sc:#5a1a8c">
<div>
<div class="fl-title">NGFW generates a forged certificate for the client</div>
<div class="fl-detail">NGFW dynamically generates a certificate for the domain (e.g., google.com), signed by the NGFW's own CA certificate. This "forged" cert has the correct hostname but is signed by the corporate CA — not by DigiCert or Let's Encrypt.</div>
<div class="fl-code">NGFW → Client: "Here is google.com's cert" (signed by corporate CA)</div>
</div>
</div>
<div class="fl-step" data-n="4" style="--sc:#5a1a8c">
<div>
<div class="fl-title">Client trusts the corporate CA — verifies successfully</div>
<div class="fl-detail">The corporate CA cert was pushed to all managed devices via MDM/GPO. Client's browser trusts it. TLS handshake with NGFW completes — client thinks it has a direct connection to google.com.</div>
</div>
</div>
<div class="fl-step" data-n="5" style="--sc:#5a1a8c">
<div>
<div class="fl-title">NGFW decrypts, inspects, re-encrypts all traffic</div>
<div class="fl-detail">All HTTPS traffic passes through the NGFW in cleartext. Full HTTP inspection is possible: URL filtering, DLP, malware scanning, application identification. After inspection, NGFW re-encrypts and forwards to the real server.</div>
<div class="fl-code">Client → [NGFW decrypts] → inspect → [re-encrypt] → Server</div>
</div>
</div>
</div>
<div class="note"><p>💡 <strong>Exclusion list:</strong> SSL inspection should exclude financial and healthcare sites (banks, healthcare portals) where privacy regulations require client-to-server TLS integrity. Certificate pinning (used by some mobile apps) will break — those apps must be excluded. Most NGFWs maintain an exclusion list of domains where SSL inspection is bypassed.</p></div>
  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>HTTP-Based Attack Detection</h3><span class="tag tag-orange">ATTACKS</span></div>
  <div class="cp-body">
<table class="t-table">
<thead><tr><th>Attack</th><th>HTTP Indicators</th><th>NGFW Detection</th></tr></thead>
<tbody>
<tr><td><strong>SQL Injection</strong></td><td>URL query: <code>?id=1' OR '1'='1</code>; POST body with SQL keywords (SELECT, UNION, DROP)</td><td>Regex/signature match on URL params and POST body. Rate-limit 400 errors from same source.</td></tr>
<tr><td><strong>Cross-Site Scripting (XSS)</strong></td><td>URL/body contains: <code>&lt;script&gt;</code>, <code>javascript:</code>, <code>onload=</code>, encoded variants (<code>%3Cscript%3E</code>)</td><td>Decode URL encoding first, then signature match. Block reflected XSS patterns in GET params.</td></tr>
<tr><td><strong>Path Traversal</strong></td><td>URL contains: <code>../</code>, <code>..\</code>, encoded variants (<code>%2e%2e%2f</code>)</td><td>Normalise and decode URL, detect directory traversal sequences.</td></tr>
<tr><td><strong>Command Injection</strong></td><td>Body contains: <code>; ls</code>, <code>| cat /etc/passwd</code>, <code>`whoami`</code></td><td>Signature match on shell metacharacters in POST body.</td></tr>
<tr><td><strong>Web Shell Upload</strong></td><td>POST to <code>/upload</code> with Content-Type: multipart; file content contains PHP/JSP code</td><td>Scan uploaded file content for webshell signatures, not just extension.</td></tr>
<tr><td><strong>Data Exfiltration</strong></td><td>Large POST bodies to external sites. Unusual User-Agent. HTTP CONNECT to non-standard ports.</td><td>DLP policy on POST body size/content. Block CONNECT to non-80/443 ports.</td></tr>
<tr><td><strong>HTTP DDoS</strong></td><td>Flood of GET requests to same URL; slowloris (partial requests held open)</td><td>Rate-limit requests per source IP per second. Detect incomplete request bodies.</td></tr>
</tbody>
</table>
  </div>
</div>
</div>
<!-- ════════════ TAB 8 — LABS ════════════ -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>HTTP Protocol Analysis with curl and Wireshark</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Capture and fully decode HTTP/1.1, HTTP/2, and observe the protocol upgrade mechanism. Understand every header in a real request/response exchange.</p>
<div class="lab-step"><div class="sn">1</div><div>Start Wireshark capture. Make an HTTP/1.1 request: <code>curl -v --http1.1 http://httpbin.org/get</code>. In Wireshark, filter <code>http</code>. Expand the HTTP request packet: find method (GET), URI path (/get), HTTP version (1.1), all request headers. Expand the response: status code (200), all response headers, JSON body.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Examine the raw TCP stream: right-click the HTTP GET packet → Follow → TCP Stream. You'll see the full plaintext HTTP/1.1 exchange. Identify the empty CRLF line that separates headers from body. Count header bytes vs body bytes — calculate overhead ratio.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Test persistent connections: <code>curl -v --http1.1 http://httpbin.org/get http://httpbin.org/headers</code> (two URLs to same server). In Wireshark, verify both requests use the same TCP connection (same port numbers in stream). Look for <code>Connection: keep-alive</code> header.</div></div>
<div class="lab-step"><div class="sn">4</div><div>HTTP/2 analysis: <code>curl -v --http2 https://nghttp2.org</code>. In Wireshark: because HTTP/2 is encrypted, use SSL key log: <code>SSLKEYLOGFILE=/tmp/keys.log curl --http2 https://nghttp2.org</code>. Configure Wireshark to use the key log (Edit → Preferences → TLS → Master Secret log). Now HTTP/2 frames are visible — find HEADERS, DATA frame types.</div></div>
<div class="lab-step"><div class="sn">5</div><div>Test various HTTP methods with httpbin: <br><code>curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://httpbin.org/post</code><br><code>curl -X DELETE https://httpbin.org/delete</code><br><code>curl -X PUT -d 'data' https://httpbin.org/put</code>.<br>In each response, examine the <code>json</code>/<code>data</code>/<code>form</code> fields showing what the server received.</div></div>
<div class="lab-step"><div class="sn">6</div><div><strong>Bonus — QUIC traffic:</strong> <code>SSLKEYLOGFILE=/tmp/keys.log curl --http3 https://cloudflare.com</code>. In Wireshark: filter <code>udp.port == 443</code>. Without key log you see QUIC packet metadata but encrypted content. With key log configured, QUIC frames become visible. Compare frame structure to what you studied in Tab 5.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Build an HTTP/1.1 Server and Client in C</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Write a minimal HTTP/1.1 server from scratch using TCP sockets. Manually construct and parse HTTP request lines, headers, and bodies. This gives you the deepest possible understanding of the protocol.</p>
<div class="lab-step"><div class="sn">1</div><div>Write a minimal HTTP/1.1 server: create a TCP socket, bind to port 8080, listen, accept connections. For each connection, read bytes until you find the double CRLF (<code>\r\n\r\n</code>) marking the end of headers. Parse the request line: method, path, version.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Parse headers line-by-line: split on <code>: </code> to get name/value pairs. Store in a simple key-value array. Implement: extract Content-Length header (to know how many body bytes to read after the header CRLF).</div></div>
<div class="lab-step"><div class="sn">3</div><div>Implement routing: if path == "/", return <code>200 OK</code> with an HTML body. If path == "/api/echo", return the request body as JSON. If path is anything else, return <code>404 Not Found</code>. Construct response by writing the status line, headers (Content-Type, Content-Length, Connection: keep-alive), blank line, body.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Test your server: <code>curl -v http://localhost:8080/</code> and <code>curl -v -X POST -d "hello" http://localhost:8080/api/echo</code>. In Wireshark, verify your responses have correct HTTP/1.1 format. Then test with a browser — it should render your HTML response.</div></div>
<div class="lab-step"><div class="sn">5</div><div><strong>Bonus — implement chunked encoding:</strong> For the <code>/stream</code> endpoint, set <code>Transfer-Encoding: chunked</code> and send the response body in 5 chunks of 10 bytes each with proper hex length prefixes. Use <code>curl -v http://localhost:8080/stream</code> to verify the chunked response is reassembled correctly.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>HTTP Security Header Audit and Attack Simulation</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Audit a web server's security headers, simulate HTTP-based attacks, and observe how headers prevent them. Understand what an NGFW sees in HTTP attack traffic.</p>
<div class="lab-step"><div class="sn">1</div><div><strong>Security header audit:</strong> Use curl to inspect security headers: <code>curl -sI https://google.com | grep -iE 'strict|content-security|x-frame|x-content|referrer|permissions'</code>. Do the same for 5 different sites. Which ones have all security headers? Which are missing? Note which are missing CSP — those are vulnerable to XSS.</div></div>
<div class="lab-step"><div class="sn">2</div><div><strong>SQL injection patterns:</strong> Send test SQL injection payloads to httpbin (a safe echo server): <code>curl "https://httpbin.org/get?id=1%27%20OR%20%271%27%3D%271"</code>. The <code>%27</code> is URL-encoded single quote. In the response, verify the server received the decoded SQL. Write a simple Python script that scans a list of URLs for SQL injection patterns in the response (errors, SQL keywords in output).</div></div>
<div class="lab-step"><div class="sn">3</div><div><strong>XSS detection:</strong> Send an XSS payload: <code>curl "https://httpbin.org/get?q=%3Cscript%3Ealert(1)%3C%2Fscript%3E"</code>. Capture in Wireshark. Write a filter rule (in Python or BPF syntax) that would detect this: match URL-encoded or decoded <code>&lt;script&gt;</code> tags in HTTP GET query strings.</div></div>
<div class="lab-step"><div class="sn">4</div><div><strong>User-Agent analysis:</strong> Make requests with various user agents and observe server responses: <code>curl -A "sqlmap/1.0" https://httpbin.org/headers</code> (known scanner UA). <code>curl -A "" https://httpbin.org/headers</code> (empty UA). <code>curl -A "Mozilla/5.0" https://httpbin.org/headers</code> (normal browser). Build a list of malicious/scanner User-Agent strings and write a detection rule.</div></div>
<div class="lab-step"><div class="sn">5</div><div><strong>Rate limiting simulation:</strong> Write a Python script that sends 100 GET requests per second to your HTTP server from Lab 2. Observe: does your server handle it? Add rate limiting: track requests per source IP in a hash map, return 429 Too Many Requests if rate exceeds 10 req/sec. Test the rate limiter works.</div></div>
  </div>
</div>
</div>
<!-- ════════════ TAB 9 — CHECKLIST ════════════ -->
<div id="t9" class="tab-pane">
<p class="sep">M08 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain the key problem each HTTP version solved: 1.0=persistent, 1.1=keep-alive+chunked, 2=multiplexing, 3=no TCP HOL blocking</li>
  <li>Know HTTP/1.1 message format: request line + headers + CRLF + body; status line + headers + CRLF + body</li>
  <li>Know the mandatory HTTP/1.1 header: Host (enables virtual hosting)</li>
  <li>Know all 9 HTTP methods: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS, CONNECT, TRACE</li>
  <li>Know safe vs idempotent: GET/HEAD/OPTIONS are safe; GET/PUT/DELETE/HEAD/OPTIONS are idempotent; POST/PATCH are neither</li>
  <li>Know all 5 status code ranges and 15+ specific codes (200, 201, 204, 301, 302, 304, 400, 401, 403, 404, 405, 429, 500, 502, 503)</li>
  <li>Know Head-of-Line blocking in HTTP/1.1: responses must return in request order; one slow response blocks all subsequent</li>
  <li>Know chunked transfer encoding: hex length prefix per chunk, zero-length chunk = end</li>
  <li>Know 8 critical request headers: Host, User-Agent, Authorization, Cookie, Referer, Content-Type, X-Forwarded-For, Origin</li>
  <li>Know 6 security response headers: HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy</li>
  <li>Know cookie security flags: HttpOnly (no JS access), Secure (HTTPS only), SameSite=Strict (no cross-site)</li>
  <li>Know HTTP/2's four innovations: binary framing, multiplexing, HPACK compression, server push</li>
  <li>Know HTTP/2 frame types: DATA, HEADERS, RST_STREAM, SETTINGS, PUSH_PROMISE, PING, GOAWAY, WINDOW_UPDATE</li>
  <li>Know HTTP/2 still has TCP HOL blocking — a lost TCP packet stalls all streams</li>
  <li>Know HPACK: static table (61 entries), dynamic table (per-connection learned headers), both compressed to 1-byte index</li>
  <li>Know QUIC's 4 motivations: TCP HOL blocking, 2-RTT connection setup, no connection migration, TCP ossification</li>
  <li>Know QUIC Connection ID: enables connection migration when client IP changes (WiFi → cellular)</li>
  <li>Know QUIC 1-RTT vs 0-RTT: 1-RTT = standard first connection; 0-RTT = session resumption, replay-vulnerable</li>
  <li>Know 6 QUIC frame types: STREAM, ACK, CRYPTO, NEW_CONNECTION_ID, MAX_DATA, CONNECTION_CLOSE</li>
  <li>Know QPACK vs HPACK: QPACK adapted for out-of-order QUIC streams using separate encoder/decoder streams</li>
  <li>Know HTTP/3 uses ALPN "h3", runs on UDP 443, always requires TLS 1.3</li>
  <li>Know what HTTPS encrypts: URL path, headers, body. What it doesn't hide: destination IP, TLS SNI hostname</li>
  <li>Know how SSL inspection works: NGFW → server (real TLS), NGFW → client (forged cert signed by corporate CA)</li>
  <li>Know SSL inspection limitations: certificate pinning, privacy regulations, requires CA cert deployment</li>
  <li>Know HTTP inspection visibility matrix: what's visible in plain HTTP vs HTTPS vs with SSL inspection</li>
  <li>Know 7 HTTP attack types for NGFW detection: SQLi, XSS, path traversal, command injection, webshell, exfiltration, DDoS</li>
  <li>Know NGFW HTTP monitoring: 401/403 spikes = brute force; 404 flood = directory enumeration; 500 flood = injection scan</li>
  <li>Completed Lab 1: captured and decoded HTTP/1.1 and HTTP/2 traffic in Wireshark with TLS key log</li>
  <li>Completed Lab 2: built HTTP/1.1 server from scratch in C with routing, header parsing, and chunked encoding</li>
  <li>Completed Lab 3: audited security headers, simulated SQLi/XSS patterns, implemented rate limiting</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M09 - SMTP, FTP, and DHCP</strong>. These are the protocols an NGFW must parse to protect email infrastructure, file transfers, and network bootstrapping — each introduces unique ALG (Application-Level Gateway) challenges for firewall traversal.</p>
</div>
</div>
<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/networking-mastery/m07-dns/">← M07 DNS</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m09-app-protocols/">Next: M09 - SMTP, FTP, DHCP →</a>
</div>
<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
</script>
