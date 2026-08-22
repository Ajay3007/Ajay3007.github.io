---
title: "M02 — HTTP Deep Dive & Web Server Internals"
description: "HTTP request parsing, header internals, epoll event loops, middleware pipelines, routing, content negotiation — with full C implementations."
domain: engineering
track: backend
order: 2
ownHeader: true
url: /learning/backend/m02-http-servers/
---

<style>
.mod-wrap{max-width:960px;margin:0 auto;padding:0 1rem 4rem;font-family:'Segoe UI',system-ui,sans-serif;color:#1e293b}
.mod-header{background:#fff;border-left:5px solid #00c9a7;border-radius:10px;padding:1.6rem 2rem;margin-bottom:1.5rem;box-shadow:0 2px 12px rgba(0,0,0,.08)}
.mod-header h1{margin:0 0 .4rem;font-size:1.75rem;color:#0f172a}
.mod-header .sub{color:#64748b;font-size:.95rem}
.phase-tag{display:inline-block;background:linear-gradient(90deg,#00c9a7,#00b4d8);color:#fff;font-size:.75rem;font-weight:700;padding:.25rem .75rem;border-radius:20px;margin-right:.5rem;text-transform:uppercase;letter-spacing:.05em}
.tab-bar{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:1.25rem}
.tab-btn{padding:.45rem 1rem;border:2px solid #e2e8f0;border-radius:20px;background:#fff;font-size:.82rem;font-weight:600;cursor:pointer;color:#64748b;transition:all .2s}
.tab-btn:hover{border-color:#00c9a7;color:#00897b}
.tab-btn.active{background:linear-gradient(135deg,#00c9a7,#00b4d8);border-color:transparent;color:#fff;box-shadow:0 3px 10px rgba(0,201,167,.35)}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.cp-hdr{padding:.65rem 1.1rem;font-weight:700;font-size:.9rem;display:flex;align-items:center;gap:.5rem}
.cp-body{padding:1rem 1.2rem;background:#fff;font-size:.9rem;line-height:1.75}
.p-teal .cp-hdr{background:linear-gradient(90deg,#f0fdf4,#ccfbf1);color:#0f766e;border-left:4px solid #00c9a7}
.p-blue .cp-hdr{background:linear-gradient(90deg,#eff6ff,#dbeafe);color:#1d4ed8;border-left:4px solid #3b82f6}
.p-green .cp-hdr{background:linear-gradient(90deg,#f0fdf4,#dcfce7);color:#15803d;border-left:4px solid #22c55e}
.p-orange .cp-hdr{background:linear-gradient(90deg,#fff7ed,#ffedd5);color:#c2410c;border-left:4px solid #f97316}
.p-purple .cp-hdr{background:linear-gradient(90deg,#faf5ff,#f3e8ff);color:#7e22ce;border-left:4px solid #a855f7}
.p-red .cp-hdr{background:linear-gradient(90deg,#fff1f2,#ffe4e6);color:#be123c;border-left:4px solid #f43f5e}
.p-amber .cp-hdr{background:linear-gradient(90deg,#fffbeb,#fef3c7);color:#92400e;border-left:4px solid #f59e0b}
.p-cyan .cp-hdr{background:linear-gradient(90deg,#ecfeff,#cffafe);color:#0e7490;border-left:4px solid #06b6d4}
.p-orange{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.p-purple{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.ins,.warn,.note,.analogy{border-radius:8px;padding:.75rem 1rem;margin:.75rem 0;font-size:.87rem;line-height:1.7}
.ins{background:#f0fdf4;border-left:4px solid #00c9a7;color:#134e4a}
.warn{background:#fff7ed;border-left:4px solid #f97316;color:#7c2d12}
.note{background:#eff6ff;border-left:4px solid #3b82f6;color:#1e3a5f}
.analogy{background:#faf5ff;border-left:4px solid #a855f7;color:#581c87}
.cb{background:#0f172a;border-radius:10px;padding:1.1rem 1.3rem;margin:.75rem 0;overflow-x:auto;font-size:.82rem;line-height:1.75;font-family:'Cascadia Code','Fira Code',monospace}
.cm{color:#94a3b8}.ck{color:#7dd3fc}.cv{color:#86efac}.cs{color:#fca5a5}
.cn{color:#fdba74}.cf{color:#c4b5fd}.co{color:#fde68a}.cg{color:#6ee7b7}
.flow-list{list-style:none;padding:0;margin:.5rem 0}
.fl-step{display:flex;align-items:flex-start;gap:.85rem;padding:.65rem .85rem;margin-bottom:.5rem;border-radius:8px;background:#f8fafc;border-left:3px solid #00c9a7;font-size:.88rem;line-height:1.65}
.fl-num{background:linear-gradient(135deg,#00c9a7,#00b4d8);color:#fff;border-radius:50%;width:1.6rem;height:1.6rem;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.75rem;flex-shrink:0}
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.75rem 0}
.t-table th{background:linear-gradient(90deg,#00c9a7,#00b4d8);color:#fff;padding:.6rem .9rem;text-align:left}
.t-table td{padding:.55rem .9rem;border-bottom:1px solid #e2e8f0;vertical-align:top}
.t-table tr:nth-child(even) td{background:#f8fafc}
.t-table tr:hover td{background:#f0fdf4}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.75rem 0}
@media(max-width:640px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #00c9a7;border-radius:10px;margin-bottom:1.25rem;overflow:hidden}
.lab-hdr{background:linear-gradient(90deg,#f0fdf4,#ccfbf1);padding:.7rem 1.1rem;display:flex;align-items:center;gap:.6rem;font-weight:700;font-size:.9rem;color:#0f766e}
.lab-body{padding:1rem 1.2rem;font-size:.88rem;line-height:1.75}
.lab-step{padding:.4rem 0;padding-left:1.1rem;border-left:2px solid #00c9a7;margin-bottom:.4rem}
.sn{display:inline-block;background:#00c9a7;color:#fff;border-radius:50%;width:1.3rem;height:1.3rem;font-size:.7rem;font-weight:700;text-align:center;line-height:1.3rem;margin-right:.4rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{padding:.35rem .5rem;font-size:.87rem;display:flex;align-items:flex-start;gap:.6rem}
.cl li::before{content:"☐";color:#00c9a7;font-size:1rem;flex-shrink:0}
.diagram-box{background:#0f172a;border-radius:10px;padding:1.1rem 1.3rem;margin:.75rem 0;overflow-x:auto;font-family:'Cascadia Code','Fira Code',monospace;font-size:.78rem;line-height:1.8;color:#94a3b8}
.dg-teal{color:#5eead4}.dg-blue{color:#93c5fd}.dg-green{color:#86efac}.dg-amber{color:#fde68a}.dg-gray{color:#64748b}.dg-red{color:#fca5a5}.dg-purple{color:#c4b5fd}
.mod-nav{display:flex;justify-content:space-between;align-items:center;margin-top:2.5rem;padding:1rem 0;border-top:2px solid #e2e8f0;font-size:.88rem}
.nb{padding:.5rem 1.1rem;border:2px solid #00c9a7;border-radius:20px;color:#00897b;text-decoration:none;font-weight:600;transition:all .2s}
.nb:hover{background:#00c9a7;color:#fff}
.sep{text-align:center;color:#94a3b8;font-size:.8rem;letter-spacing:.1em;margin:1.5rem 0;text-transform:uppercase}
</style>

<div class="mod-wrap">
<div class="mod-header">
  <h1>M02 — HTTP Deep Dive &amp; Web Server Internals</h1>
  <div class="sub">
    <span class="phase-tag">Phase 0</span>
    HTTP request parsing · Header internals · epoll event loop · Middleware pipeline · Trie-based routing · Content negotiation · Chunked transfer · Keep-alive &amp; connection pooling
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt('t-overview',this)">Overview</button>
  <button class="tab-btn" onclick="vt('t-parsing',this)">HTTP Parsing</button>
  <button class="tab-btn" onclick="vt('t-headers',this)">Headers &amp; Encoding</button>
  <button class="tab-btn" onclick="vt('t-eventloop',this)">Event Loop</button>
  <button class="tab-btn" onclick="vt('t-middleware',this)">Middleware &amp; Routing</button>
  <button class="tab-btn" onclick="vt('t-http2',this)">HTTP/2 Internals</button>
  <button class="tab-btn" onclick="vt('t-impl',this)">C Implementation</button>
  <button class="tab-btn" onclick="vt('t-labs',this)">Labs &amp; Checklist</button>
</div>

<!-- TAB 1 — Overview -->
<div id="t-overview" class="tab-pane active">

<div class="cp p-teal">
  <div class="cp-hdr">🔧 What This Module Covers</div>
  <div class="cp-body">
    M01 covered the transport layer (TCP, TLS) and protocol overview. M02 goes deeper into <strong>how HTTP actually works at the byte level</strong> and how a production web server processes requests — the request pipeline every backend engineer must understand to debug performance issues, write efficient servers, and understand frameworks like Nginx, Express, or Actix.
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">📋 HTTP/1.1 Request Format — Byte by Byte</div>
  <div class="cp-body">
    An HTTP/1.1 request is plain text over a TCP stream:
<div class="cb"><span class="cm">POST /orders HTTP/1.1\r\n</span>           <span class="dg-teal">← request line: method SP request-target SP HTTP-version CRLF</span>
<span class="cv">Host: api.example.com\r\n</span>             <span class="cm">← required in HTTP/1.1</span>
<span class="cv">Content-Type: application/json\r\n</span>
<span class="cv">Content-Length: 47\r\n</span>                <span class="cm">← exact byte count of body</span>
<span class="cv">Authorization: Bearer eyJhbGci...\r\n</span>
<span class="cv">Connection: keep-alive\r\n</span>
<span class="cv">\r\n</span>                                   <span class="cm">← blank line = end of headers</span>
<span class="cv">{"customer_id":"c-42","items":[{"id":"p-7"}]}</span>  <span class="cm">← body (47 bytes)</span></div>
    <strong>Key structural rules:</strong>
    <ul>
      <li>Request line and each header line ends with <code>\r\n</code> (CRLF)</li>
      <li>Header section ends with an empty line (<code>\r\n\r\n</code>)</li>
      <li>Header name is case-insensitive; value is case-sensitive (mostly)</li>
      <li>Body length determined by <code>Content-Length</code> or <code>Transfer-Encoding: chunked</code></li>
    </ul>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">📋 HTTP/1.1 Response Format</div>
  <div class="cp-body">
<div class="cb"><span class="cm">HTTP/1.1 201 Created\r\n</span>              <span class="cm">← status line: version SP status-code SP reason CRLF</span>
<span class="cv">Content-Type: application/json\r\n</span>
<span class="cv">Content-Length: 33\r\n</span>
<span class="cv">Location: /orders/ord-9821\r\n</span>        <span class="cm">← URL of new resource (201 response)</span>
<span class="cv">Cache-Control: no-store\r\n</span>
<span class="cv">\r\n</span>
<span class="cv">{"id":"ord-9821","status":"pending"}</span></div>
    <div class="note">HTTP is a <strong>text protocol</strong> — both request and response are human-readable ASCII (headers). The body can be binary. This is why HTTP/2 moved to binary framing — text parsing is slower and more fragile.</div>
  </div>
</div>

</div><!-- /t-overview -->

<!-- TAB 2 — HTTP Parsing -->
<div id="t-parsing" class="tab-pane">

<div class="cp p-teal">
  <div class="cp-hdr">⚙️ HTTP/1.1 Request Parser State Machine</div>
  <div class="cp-body">
    A production HTTP parser is a state machine. It reads data from the TCP stream in chunks (not necessarily aligned to request boundaries) and must handle:
    <ul>
      <li>Partial reads — CRLF split across two recv() calls</li>
      <li>Pipelining — multiple requests in one TCP read buffer</li>
      <li>Slowloris attack — client sends headers one byte at a time</li>
      <li>Header injection — values containing CRLF sequences</li>
    </ul>
  </div>
</div>

<div class="diagram-box">
<span class="dg-teal">PARSE_REQUEST_LINE</span> → reads until first CRLF
  extract method, URI, HTTP-version
  validate method ∈ {GET,POST,PUT,DELETE,PATCH,HEAD,OPTIONS}
                  ↓
<span class="dg-blue">PARSE_HEADERS</span> → reads until CRLFCRLF
  for each line: split on first ': '
  normalize header name to lowercase
  check for Content-Length or Transfer-Encoding
  enforce max_header_count (prevent DoS)
  enforce max_header_value_length
                  ↓
<span class="dg-green">PARSE_BODY</span>
  if Content-Length:
    read exactly N bytes
  elif Transfer-Encoding: chunked:
    read chunk-size CRLF chunk-data CRLF, repeat until 0 CRLF
  else:
    no body (GET, HEAD, DELETE)
                  ↓
<span class="dg-amber">REQUEST_COMPLETE</span> → dispatch to router
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🧩 Chunked Transfer Encoding</div>
  <div class="cp-body">
    Used when the total body size is unknown at send time (streaming, compression). Each chunk is prefixed with its size in hex:
<div class="cb"><span class="cv">Transfer-Encoding: chunked</span>
<span class="cv">\r\n</span>
<span class="cn">1a</span><span class="cv">\r\n</span>                    <span class="cm">← chunk-size: 26 bytes (hex)</span>
<span class="cv">abcdefghijklmnopqrstuvwxyz</span><span class="cv">\r\n</span>  <span class="cm">← chunk data</span>
<span class="cn">5</span><span class="cv">\r\n</span>
<span class="cv">hello</span><span class="cv">\r\n</span>
<span class="cn">0</span><span class="cv">\r\n</span>                     <span class="cm">← final chunk: size = 0 signals end</span>
<span class="cv">\r\n</span>                         <span class="cm">← trailing CRLF after final chunk</span></div>
    <div class="warn">Never trust <code>Content-Length</code> if <code>Transfer-Encoding: chunked</code> is also set. Per RFC 7230, chunked wins and <code>Content-Length</code> must be removed. A mismatch is a potential HTTP request smuggling vector.</div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">🔒 HTTP Request Smuggling</div>
  <div class="cp-body">
    When a frontend proxy (CDN, load balancer) and backend server disagree on where one HTTP request ends and the next begins, an attacker can "smuggle" a prefix of a subsequent request past security controls.
    <br><br>
    <strong>CL.TE attack:</strong> frontend uses Content-Length, backend uses Transfer-Encoding:
<div class="cb"><span class="cv">POST / HTTP/1.1\r\n</span>
<span class="cv">Content-Length: 13\r\n</span>        <span class="cm">← frontend reads 13 bytes: "0\r\n\r\nGET /admin"</span>
<span class="cv">Transfer-Encoding: chunked\r\n</span>  <span class="cm">← backend: reads chunk 0 → end, then starts "GET /admin" as new request</span>
<span class="cv">\r\n</span>
<span class="cv">0\r\n</span>
<span class="cv">\r\n</span>
<span class="cv">GET /admin</span></div>
    <strong>Prevention:</strong> normalize all requests at the proxy; reject ambiguous requests; use HTTP/2 end-to-end (binary framing eliminates this class).
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">📏 Parser Security: Limits to Enforce</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Limit</th><th>Nginx Default</th><th>Why</th></tr></thead>
      <tbody>
        <tr><td>Request line max length</td><td>8KB</td><td>Prevent buffer overflow in URI parsing</td></tr>
        <tr><td>Max header count</td><td>~100</td><td>Prevent CPU DoS from O(N) header processing</td></tr>
        <tr><td>Max single header value</td><td>8KB</td><td>Prevent memory DoS</td></tr>
        <tr><td>Max body size</td><td>1MB</td><td>Prevent disk/memory exhaustion</td></tr>
        <tr><td>Header read timeout</td><td>60s</td><td>Prevent Slowloris (slow header attack)</td></tr>
        <tr><td>Body read timeout</td><td>60s</td><td>Prevent slow POST attacks</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div><!-- /t-parsing -->

<!-- TAB 3 — Headers & Encoding -->
<div id="t-headers" class="tab-pane">

<div class="cp p-teal">
  <div class="cp-hdr">📋 Essential Request Headers</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Header</th><th>Purpose</th><th>Notes</th></tr></thead>
      <tbody>
        <tr><td><code>Host</code></td><td>Virtual hosting — which domain is being requested</td><td>Required in HTTP/1.1; enables multiple sites on one IP</td></tr>
        <tr><td><code>Accept</code></td><td>Content types client accepts: <code>application/json, text/html;q=0.9</code></td><td>q= is quality factor (0–1). Server picks best match.</td></tr>
        <tr><td><code>Accept-Encoding</code></td><td>Compression algorithms: <code>gzip, br, deflate</code></td><td>Server compresses response body if supported</td></tr>
        <tr><td><code>Accept-Language</code></td><td>Preferred languages: <code>en-US,en;q=0.8</code></td><td>Used for i18n</td></tr>
        <tr><td><code>Content-Type</code></td><td>Body media type: <code>application/json; charset=utf-8</code></td><td>Required when body is present</td></tr>
        <tr><td><code>Authorization</code></td><td>Credentials: <code>Bearer {token}</code>, <code>Basic {b64}</code></td><td>Never in URL (logged by proxies)</td></tr>
        <tr><td><code>If-None-Match</code></td><td>Conditional GET — send ETag from previous response</td><td>Server returns 304 if unchanged → saves bandwidth</td></tr>
        <tr><td><code>If-Modified-Since</code></td><td>Conditional GET by date</td><td>Weaker than ETag (1-second granularity)</td></tr>
        <tr><td><code>X-Forwarded-For</code></td><td>Original client IP behind a proxy/LB</td><td>Rightmost non-trusted IP is the last known client</td></tr>
        <tr><td><code>X-Request-Id</code></td><td>Request correlation ID</td><td>Generate at edge; propagate through all services</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">🗜️ Content Negotiation</div>
    <div class="cp-body">
      Server selects the best response format based on <code>Accept</code> header:
<div class="cb"><span class="cm">/* Client request */</span>
Accept: <span class="cv">application/json;q=1.0</span>,
        <span class="cv">application/xml;q=0.8</span>,
        <span class="cv">text/html;q=0.5</span>

<span class="cm">/* Server algorithm */</span>
<span class="ck">for each</span> supported_type in server_types:
    <span class="ck">find</span> matching accept entry
    <span class="ck">score</span> = q * specificity
<span class="ck">pick</span> highest score
<span class="cm">→ response: application/json (q=1.0 wins)</span></div>
      If no match: return <code>406 Not Acceptable</code>.
    </div>
  </div>
  <div class="cp p-green">
    <div class="cp-hdr">📦 Response Caching Headers</div>
    <div class="cp-body">
      <table class="t-table">
        <thead><tr><th>Header</th><th>Meaning</th></tr></thead>
        <tbody>
          <tr><td><code>Cache-Control: max-age=3600</code></td><td>Cache for 1 hour</td></tr>
          <tr><td><code>Cache-Control: no-cache</code></td><td>Revalidate before using cached copy</td></tr>
          <tr><td><code>Cache-Control: no-store</code></td><td>Never cache (auth, sensitive)</td></tr>
          <tr><td><code>Cache-Control: private</code></td><td>Browser-only, not CDN</td></tr>
          <tr><td><code>ETag: "abc123"</code></td><td>Version token for conditional GET</td></tr>
          <tr><td><code>Last-Modified</code></td><td>Date-based conditional GET</td></tr>
          <tr><td><code>Vary: Accept-Encoding</code></td><td>Cache by encoding variant</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">🔄 Keep-Alive &amp; Connection Pooling</div>
  <div class="cp-body">
    HTTP/1.1 defaults to persistent connections (<code>Connection: keep-alive</code>). The TCP connection is reused for multiple requests:
    <div class="diagram-box">
<span class="dg-teal">Without Keep-Alive</span>: TCP handshake + TLS handshake per request (~100ms overhead)
  GET /a  [TCP 3-way] [TLS handshake] → response → [TCP FIN]
  GET /b  [TCP 3-way] [TLS handshake] → response → [TCP FIN]

<span class="dg-green">With Keep-Alive</span>: single TCP+TLS handshake for N requests
  [TCP 3-way] [TLS handshake]
  GET /a → response
  GET /b → response
  GET /c → response
  [TCP FIN when idle timeout or max-requests reached]
    </div>
    <strong>Server-side controls:</strong>
    <ul style="margin:.4rem 0;padding-left:1.2rem">
      <li><code>keepalive_timeout 65s</code> — close idle connection after 65s</li>
      <li><code>keepalive_requests 1000</code> — max requests per connection (prevent memory leak)</li>
      <li><code>Connection: close</code> — explicitly close after this response</li>
    </ul>
    <div class="note">HTTP/2 solves keep-alive inefficiency better — it multiplexes all requests over one connection without head-of-line blocking between requests.</div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">📏 CORS — Cross-Origin Resource Sharing</div>
  <div class="cp-body">
    Browsers block cross-origin requests by default (same-origin policy). CORS headers tell the browser which cross-origin requests are allowed.
    <table class="t-table" style="margin-top:.5rem">
      <thead><tr><th>Header</th><th>Example Value</th><th>Meaning</th></tr></thead>
      <tbody>
        <tr><td><code>Access-Control-Allow-Origin</code></td><td><code>https://app.example.com</code></td><td>Allowed origin (or <code>*</code> for public APIs)</td></tr>
        <tr><td><code>Access-Control-Allow-Methods</code></td><td><code>GET,POST,PUT,DELETE</code></td><td>Allowed HTTP methods</td></tr>
        <tr><td><code>Access-Control-Allow-Headers</code></td><td><code>Authorization,Content-Type</code></td><td>Allowed request headers</td></tr>
        <tr><td><code>Access-Control-Max-Age</code></td><td><code>86400</code></td><td>Cache preflight result for 24h</td></tr>
        <tr><td><code>Access-Control-Allow-Credentials</code></td><td><code>true</code></td><td>Allow cookies/auth headers cross-origin</td></tr>
      </tbody>
    </table>
    <div class="warn"><strong>Preflight:</strong> browsers send an <code>OPTIONS</code> request before any non-simple cross-origin request. Your server must respond to OPTIONS with CORS headers, or the actual request is blocked. Never set <code>Access-Control-Allow-Origin: *</code> with <code>Allow-Credentials: true</code> — that's a security mistake browsers reject.</div>
  </div>
</div>

</div><!-- /t-headers -->

<!-- TAB 4 — Event Loop -->
<div id="t-eventloop" class="tab-pane">

<div class="cp p-teal">
  <div class="cp-hdr">⚡ epoll vs Thread-Per-Request: The C10K Problem</div>
  <div class="cp-body">
    In 1999, Dan Kegel posed the "C10K problem" — can a single server handle 10,000 simultaneous connections? Thread-per-request breaks at scale because:
    <ul>
      <li>Each thread = 8MB stack (default) → 10K threads = 80GB RAM just for stacks</li>
      <li>Context switch overhead between 10K threads is CPU-expensive</li>
      <li>Most threads are blocked on I/O — wasted resources</li>
    </ul>
    <strong>Solution:</strong> I/O multiplexing with <code>epoll</code> — one thread, thousands of connections, only active on I/O events.
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🔄 epoll Edge-Triggered Event Loop</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>syscall</th><th>Purpose</th></tr></thead>
      <tbody>
        <tr><td><code>epoll_create1(0)</code></td><td>Create epoll instance, returns fd</td></tr>
        <tr><td><code>epoll_ctl(epfd, EPOLL_CTL_ADD, fd, &amp;event)</code></td><td>Register fd to watch</td></tr>
        <tr><td><code>epoll_wait(epfd, events, MAX, timeout_ms)</code></td><td>Block until events ready, returns count</td></tr>
      </tbody>
    </table>
    <br>
    <strong>Level-triggered (LT) vs Edge-triggered (ET):</strong>
    <ul>
      <li><strong>LT (default):</strong> epoll_wait returns event repeatedly while data available — simpler, forgiving of partial reads</li>
      <li><strong>ET:</strong> epoll_wait returns event <em>once</em> per state change — you must read until EAGAIN or data is lost. Higher performance, requires non-blocking sockets + retry loops.</li>
    </ul>
  </div>
</div>

<div class="diagram-box">
<span class="dg-teal">Event Loop</span>

<span class="dg-gray">1. Create listen socket + set O_NONBLOCK</span>
<span class="dg-gray">2. Create epoll fd</span>
<span class="dg-gray">3. Register listen socket: EPOLLIN (new connection)</span>
<span class="dg-gray">4. Loop:</span>

   n = epoll_wait(epfd, events, MAX_EVENTS, -1)
   for i in 0..n:
     if events[i].fd == listen_fd:
       <span class="dg-teal">accept()</span> → new client_fd
       <span class="dg-teal">fcntl(client_fd, F_SETFL, O_NONBLOCK)</span>
       <span class="dg-teal">epoll_ctl(EPOLL_CTL_ADD, client_fd, EPOLLIN|EPOLLET)</span>
     else:
       <span class="dg-blue">parse_http(events[i].fd)</span>
       if request complete:
         <span class="dg-green">route_and_dispatch(request)</span>
         <span class="dg-amber">send_response(events[i].fd)</span>
         if !keep_alive: <span class="dg-gray">epoll_ctl(DEL); close(fd)</span>

<span class="dg-purple">Worker threads</span>: for CPU-bound work, use a thread pool
  event loop enqueues work → thread pool executes → posts result back
</div>

<div class="cp p-green">
  <div class="cp-hdr">🏗️ Nginx Architecture: Master + Workers</div>
  <div class="cp-body">
    Nginx uses a master process + N worker processes (one per CPU core):
    <ul>
      <li><strong>Master process:</strong> reads config, manages worker lifecycle, handles signals, zero-downtime reload (<code>nginx -s reload</code>)</li>
      <li><strong>Worker process:</strong> single-threaded epoll event loop; handles all connections assigned to it</li>
      <li><strong>SO_REUSEPORT:</strong> each worker binds to the same port independently; kernel load-balances accept() calls across workers — eliminates accept mutex contention</li>
    </ul>
    <div class="ins">A single Nginx worker can handle ~10,000+ simultaneous connections because all I/O is non-blocking and the worker never sleeps waiting for one connection's data while others are ready.</div>
  </div>
</div>

</div><!-- /t-eventloop -->

<!-- TAB 5 — Middleware & Routing -->
<div id="t-middleware" class="tab-pane">

<div class="cp p-teal">
  <div class="cp-hdr">🔗 Middleware Pipeline Pattern</div>
  <div class="cp-body">
    A middleware pipeline is an ordered chain of functions where each function can: process the request, modify it, call the next middleware, or short-circuit (return a response without calling next).
  </div>
</div>

<div class="diagram-box">
<span class="dg-teal">Request</span> → [Logger] → [Rate Limiter] → [Auth] → [CORS] → [Body Parser] → [Handler]
                                                                                              ↓
<span class="dg-teal">Response</span> ← [Logger] ← [Compression] ←─────────────────────────────────── handler result

<span class="dg-gray">Each middleware: (ctx, next) → { pre-logic; next(ctx); post-logic }</span>
<span class="dg-amber">Short circuit: Rate Limiter returns 429 without calling next()</span>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🌲 Trie-Based HTTP Router</div>
  <div class="cp-body">
    A naive router compares each route pattern sequentially O(N). A trie (radix tree) routes in O(path_depth) — constant for most APIs:
    <div class="diagram-box">
<span class="dg-teal">Routes registered:</span>
  GET  /users
  GET  /users/:id
  POST /users
  GET  /users/:id/orders
  GET  /orders/:id

<span class="dg-blue">Radix tree:</span>
/ ─┬─ users ─┬─ (GET → list_users_handler)
   │          ├─ (POST → create_user_handler)
   │          └─ /:id ─┬─ (GET → get_user_handler)
   │                   └─ /orders (GET → get_user_orders_handler)
   └─ orders ─ /:id (GET → get_order_handler)

<span class="dg-gray">Path: GET /users/42/orders</span>
  match /users → match /:id (capture "42") → match /orders → handler
    </div>
    <strong>Path parameters</strong>: captured values (<code>id=42</code>) are extracted during trie traversal and placed in the request context.
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">🔌 Common Middleware Implementations</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Middleware</th><th>Responsibilities</th><th>Notes</th></tr></thead>
      <tbody>
        <tr><td><strong>Logger</strong></td><td>Log method, path, status, latency, request_id</td><td>Run first (pre) and last (post) to capture full latency</td></tr>
        <tr><td><strong>Request ID</strong></td><td>Generate/propagate X-Request-Id</td><td>Set before logger so all logs carry the ID</td></tr>
        <tr><td><strong>Auth</strong></td><td>Validate JWT/session; attach user to context</td><td>Short-circuit with 401 if invalid</td></tr>
        <tr><td><strong>Rate Limiter</strong></td><td>Check token bucket; return 429 if over limit</td><td>After auth (rate limit by user ID, not IP)</td></tr>
        <tr><td><strong>CORS</strong></td><td>Add Access-Control-* headers; handle OPTIONS preflight</td><td>Must run before auth for OPTIONS to pass without credentials</td></tr>
        <tr><td><strong>Body Parser</strong></td><td>Read body bytes; parse JSON/form; attach to context</td><td>Enforce size limits here</td></tr>
        <tr><td><strong>Compression</strong></td><td>Gzip/br response if Accept-Encoding matches</td><td>Post-handler; skip for small responses (&lt;1KB)</td></tr>
        <tr><td><strong>Panic Recovery</strong></td><td>Catch panics/crashes; return 500</td><td>Always the outermost middleware</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div><!-- /t-middleware -->

<!-- TAB 6 — HTTP/2 Internals -->
<div id="t-http2" class="tab-pane">

<div class="cp p-teal">
  <div class="cp-hdr">🔢 HTTP/2 Binary Framing Layer</div>
  <div class="cp-body">
    HTTP/2 replaces the text-based HTTP/1.1 format with a binary framing layer. All communication happens through <strong>frames</strong> sent over <strong>streams</strong> within a single TCP connection.
    <br><br>
    <strong>Frame structure</strong> (9-byte fixed header):
  </div>
</div>

<div class="diagram-box">
<span class="dg-teal">HTTP/2 Frame Format (9 bytes fixed header + variable payload)</span>

 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
┌───────────────────────────────┐
│         Length (24 bits)      │  payload length (0–16384 default)
├───────────────┬───────────────┤
│  Type (8 bits)│  Flags (8)    │
├─┬─────────────────────────────┤
│R│         Stream ID (31 bits) │  R = reserved
└─┴─────────────────────────────┘
│           Frame Payload       │
└───────────────────────────────┘

<span class="dg-blue">Frame Types:</span>
  DATA       (0x0) → request/response body chunks
  HEADERS    (0x1) → compressed headers (HPACK)
  PRIORITY   (0x2) → stream dependency weight
  RST_STREAM (0x3) → abort a stream
  SETTINGS   (0x4) → connection parameters
  PUSH_PROMISE(0x5)→ server push announcement
  PING       (0x6) → keep-alive / RTT measurement
  GOAWAY     (0x7) → graceful connection close
  WINDOW_UPDATE(0x8)→ flow control
  CONTINUATION(0x9)→ continuation of HEADERS
</div>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">🌊 Streams &amp; Multiplexing</div>
    <div class="cp-body">
      A <strong>stream</strong> is a bidirectional sequence of frames with an integer ID. Multiple streams are interleaved over one TCP connection:
      <ul style="margin:0;padding-left:1.2rem">
        <li>Client-initiated streams: odd IDs (1, 3, 5, …)</li>
        <li>Server push streams: even IDs (2, 4, 6, …)</li>
        <li>Stream 0: connection-level control (SETTINGS, PING)</li>
        <li>Max concurrent streams: negotiated via SETTINGS_MAX_CONCURRENT_STREAMS</li>
        <li>Frames from different streams freely interleaved → no HOL blocking between requests</li>
      </ul>
    </div>
  </div>
  <div class="cp p-green">
    <div class="cp-hdr">📦 HPACK Header Compression</div>
    <div class="cp-body">
      HTTP/1.1 resends all headers on every request (~500B overhead). HPACK maintains two tables:
      <ul style="margin:0;padding-left:1.2rem">
        <li><strong>Static table:</strong> 61 common headers predefined (e.g., <code>:method GET</code> = index 2)</li>
        <li><strong>Dynamic table:</strong> headers added during session; referenced by index on repeat</li>
      </ul>
      Result: <code>:method GET</code> takes 1 byte (index reference) instead of 12 bytes. Repeated headers across requests are nearly free.
      <div class="warn" style="margin-top:.4rem"><strong>CRIME attack:</strong> compressing secret data (cookies) alongside attacker-controlled data allows compression oracle attacks. HTTPS only — never compress sensitive headers over plaintext.</div>
    </div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">🚰 HTTP/2 Flow Control</div>
  <div class="cp-body">
    HTTP/2 has two levels of flow control to prevent a fast sender from overwhelming a slow receiver:
    <ul>
      <li><strong>Connection-level:</strong> total bytes in flight across all streams</li>
      <li><strong>Stream-level:</strong> bytes in flight per individual stream</li>
    </ul>
    Each side advertises a <strong>receive window</strong> (initial: 65,535 bytes). Sender must stop when window is exhausted. Receiver sends <code>WINDOW_UPDATE</code> to grant more capacity after processing data.
    <br><br>
    <div class="note">HTTP/2 flow control is independent of TCP flow control. A receiver can throttle a single stream without blocking others — unlike HTTP/1.1 where slow reading of one response blocks the entire connection.</div>
  </div>
</div>

</div><!-- /t-http2 -->

<!-- TAB 7 — C Implementation -->
<div id="t-impl" class="tab-pane">

<div class="sep">── Implementation 1 — HTTP/1.1 Request Parser ──</div>

<div class="cp p-teal">
  <div class="cp-hdr">🔧 HTTP/1.1 Parser in C (State Machine)</div>
  <div class="cp-body">
<div class="cb"><span class="cm">/* http_parser.c — minimal HTTP/1.1 request parser */</span>
<span class="cs">#include</span> &lt;string.h&gt;
<span class="cs">#include</span> &lt;stdlib.h&gt;
<span class="cs">#include</span> &lt;stdio.h&gt;
<span class="cs">#include</span> &lt;ctype.h&gt;

<span class="cs">#define</span> MAX_HEADERS   <span class="cn">64</span>
<span class="cs">#define</span> MAX_URI_LEN   <span class="cn">8192</span>
<span class="cs">#define</span> MAX_HDR_LEN   <span class="cn">8192</span>

<span class="cs">typedef struct</span> {
    <span class="cs">char</span>  method[<span class="cn">16</span>];
    <span class="cs">char</span>  uri[MAX_URI_LEN];
    <span class="cs">char</span>  version[<span class="cn">16</span>];
    <span class="cs">struct</span> { <span class="cs">char</span> name[<span class="cn">128</span>]; <span class="cs">char</span> value[MAX_HDR_LEN]; } headers[MAX_HEADERS];
    <span class="cs">int</span>   header_count;
    <span class="cs">char</span> *body;
    <span class="cs">int</span>   body_len;
    <span class="cs">int</span>   content_length;
} http_request_t;

<span class="cm">/* Parse request line: "METHOD URI HTTP/1.x\r\n" */</span>
<span class="ck">static int</span> <span class="cf">parse_request_line</span>(http_request_t *req, <span class="cs">char</span> *line, <span class="cs">int</span> len) {
    (void)len;
    <span class="cm">/* sscanf is acceptable for bounded inputs with fixed format */</span>
    <span class="ck">if</span> (sscanf(line, <span class="cv">"%15s %8191s %15s"</span>,
               req-&gt;method, req-&gt;uri, req-&gt;version) != <span class="cn">3</span>)
        <span class="ck">return</span> -<span class="cn">1</span>;

    <span class="cm">/* Validate method (allowlist) */</span>
    <span class="cs">const char</span> *valid[] = {<span class="cv">"GET"</span>,<span class="cv">"POST"</span>,<span class="cv">"PUT"</span>,<span class="cv">"DELETE"</span>,<span class="cv">"PATCH"</span>,<span class="cv">"HEAD"</span>,<span class="cv">"OPTIONS"</span>,NULL};
    <span class="ck">for</span> (<span class="cs">int</span> i = <span class="cn">0</span>; valid[i]; i++)
        <span class="ck">if</span> (strcmp(req-&gt;method, valid[i]) == <span class="cn">0</span>) <span class="ck">return</span> <span class="cn">0</span>;
    <span class="ck">return</span> -<span class="cn">1</span>;  <span class="cm">/* unknown method */</span>
}

<span class="cm">/* Parse one header line: "Name: value\r\n" */</span>
<span class="ck">static int</span> <span class="cf">parse_header_line</span>(http_request_t *req, <span class="cs">char</span> *line) {
    <span class="ck">if</span> (req-&gt;header_count &gt;= MAX_HEADERS) <span class="ck">return</span> -<span class="cn">1</span>;

    <span class="cs">char</span> *colon = strchr(line, <span class="cn">':'</span>);
    <span class="ck">if</span> (!colon) <span class="ck">return</span> -<span class="cn">1</span>;

    *colon = <span class="cn">'\0'</span>;
    <span class="cs">char</span> *value = colon + <span class="cn">1</span>;
    <span class="ck">while</span> (*value == <span class="cn">' '</span>) value++;  <span class="cm">/* strip leading whitespace */</span>

    <span class="cs">int</span> i = req-&gt;header_count++;
    <span class="cm">/* Normalize name to lowercase */</span>
    strncpy(req-&gt;headers[i].name, line, <span class="cn">127</span>);
    <span class="ck">for</span> (<span class="cs">char</span> *p = req-&gt;headers[i].name; *p; p++) *p = tolower(*p);
    strncpy(req-&gt;headers[i].value, value, MAX_HDR_LEN - <span class="cn">1</span>);

    <span class="cm">/* Track content-length for body parsing */</span>
    <span class="ck">if</span> (strcmp(req-&gt;headers[i].name, <span class="cv">"content-length"</span>) == <span class="cn">0</span>)
        req-&gt;content_length = atoi(req-&gt;headers[i].value);

    <span class="ck">return</span> <span class="cn">0</span>;
}

<span class="cm">/* Parse full HTTP/1.1 request from buffer */</span>
<span class="cs">int</span> <span class="cf">http_parse_request</span>(http_request_t *req, <span class="cs">char</span> *buf, <span class="cs">int</span> len) {
    memset(req, <span class="cn">0</span>, <span class="ck">sizeof</span>(*req));

    <span class="cm">/* Find end of headers: \r\n\r\n */</span>
    <span class="cs">char</span> *header_end = strstr(buf, <span class="cv">"\r\n\r\n"</span>);
    <span class="ck">if</span> (!header_end) <span class="ck">return</span> -<span class="cn">1</span>;  <span class="cm">/* incomplete */</span>
    *header_end = <span class="cn">'\0'</span>;

    <span class="cs">char</span> *line = buf;
    <span class="cs">char</span> *nl;
    <span class="cs">int</span> first_line = <span class="cn">1</span>;

    <span class="ck">while</span> ((nl = strstr(line, <span class="cv">"\r\n"</span>)) != NULL) {
        *nl = <span class="cn">'\0'</span>;
        <span class="ck">if</span> (first_line) {
            <span class="ck">if</span> (parse_request_line(req, line, nl - line) &lt; <span class="cn">0</span>) <span class="ck">return</span> -<span class="cn">1</span>;
            first_line = <span class="cn">0</span>;
        } <span class="ck">else if</span> (nl &gt; line) {
            <span class="ck">if</span> (parse_header_line(req, line) &lt; <span class="cn">0</span>) <span class="ck">return</span> -<span class="cn">1</span>;
        }
        line = nl + <span class="cn">2</span>;
    }

    <span class="cm">/* Body follows the \r\n\r\n separator */</span>
    req-&gt;body = header_end + <span class="cn">4</span>;
    req-&gt;body_len = req-&gt;content_length;

    <span class="ck">return</span> <span class="cn">0</span>;
}</div>
  </div>
</div>

<div class="sep">── Implementation 2 — epoll HTTP Server ──</div>

<div class="cp p-blue">
  <div class="cp-hdr">🔄 Non-Blocking epoll HTTP Server with Middleware</div>
  <div class="cp-body">
<div class="cb"><span class="cm">/* epoll_server.c — minimal non-blocking HTTP/1.1 server with middleware */</span>
<span class="cs">#include</span> &lt;sys/epoll.h&gt;
<span class="cs">#include</span> &lt;sys/socket.h&gt;
<span class="cs">#include</span> &lt;netinet/in.h&gt;
<span class="cs">#include</span> &lt;fcntl.h&gt;
<span class="cs">#include</span> &lt;unistd.h&gt;
<span class="cs">#include</span> &lt;string.h&gt;
<span class="cs">#include</span> &lt;stdio.h&gt;
<span class="cs">#include</span> &lt;stdlib.h&gt;
<span class="cs">#include</span> &lt;time.h&gt;

<span class="cs">#define</span> MAX_EVENTS  <span class="cn">1024</span>
<span class="cs">#define</span> BUF_SIZE    <span class="cn">65536</span>
<span class="cs">#define</span> PORT        <span class="cn">8080</span>

<span class="cs">typedef struct</span> {
    <span class="cs">int</span>    fd;
    <span class="cs">char</span>   rbuf[BUF_SIZE];
    <span class="cs">int</span>    rlen;
    <span class="cs">char</span>   wbuf[BUF_SIZE];
    <span class="cs">int</span>    wlen;
    <span class="cs">int</span>    woff;
} conn_t;

<span class="ck">static void</span> <span class="cf">set_nonblocking</span>(<span class="cs">int</span> fd) {
    <span class="cs">int</span> flags = fcntl(fd, F_GETFL, <span class="cn">0</span>);
    fcntl(fd, F_SETFL, flags | O_NONBLOCK);
}

<span class="cm">/* HTTP response builder */</span>
<span class="ck">static int</span> <span class="cf">build_response</span>(<span class="cs">char</span> *buf, <span class="cs">int</span> sz,
                            <span class="cs">int</span> status, <span class="cs">const char</span> *body) {
    <span class="cs">const char</span> *reason =
        status == <span class="cn">200</span> ? <span class="cv">"OK"</span> :
        status == <span class="cn">201</span> ? <span class="cv">"Created"</span> :
        status == <span class="cn">404</span> ? <span class="cv">"Not Found"</span> :
        status == <span class="cn">405</span> ? <span class="cv">"Method Not Allowed"</span> : <span class="cv">"Internal Server Error"</span>;

    <span class="ck">return</span> snprintf(buf, sz,
        <span class="cv">"HTTP/1.1 %d %s\r\n"</span>
        <span class="cv">"Content-Type: application/json\r\n"</span>
        <span class="cv">"Content-Length: %zu\r\n"</span>
        <span class="cv">"Connection: keep-alive\r\n"</span>
        <span class="cv">"\r\n"</span>
        <span class="cv">"%s"</span>,
        status, reason, strlen(body), body);
}

<span class="cm">/* Route handler — returns 0 on success, -1 on unknown route */</span>
<span class="ck">static int</span> <span class="cf">handle_request</span>(conn_t *conn,
                            <span class="cs">const char</span> *method, <span class="cs">const char</span> *uri) {
    <span class="ck">if</span> (strcmp(method, <span class="cv">"GET"</span>) == <span class="cn">0</span> &amp;&amp; strcmp(uri, <span class="cv">"/"</span>) == <span class="cn">0</span>) {
        conn-&gt;wlen = build_response(conn-&gt;wbuf, BUF_SIZE,
            <span class="cn">200</span>, <span class="cv">"{\"status\":\"ok\"}"</span>);
        <span class="ck">return</span> <span class="cn">0</span>;
    }
    <span class="ck">if</span> (strncmp(uri, <span class="cv">"/orders"</span>, <span class="cn">7</span>) == <span class="cn">0</span> &amp;&amp; strcmp(method, <span class="cv">"GET"</span>) == <span class="cn">0</span>) {
        conn-&gt;wlen = build_response(conn-&gt;wbuf, BUF_SIZE,
            <span class="cn">200</span>, <span class="cv">"{\"orders\":[]}"</span>);
        <span class="ck">return</span> <span class="cn">0</span>;
    }
    conn-&gt;wlen = build_response(conn-&gt;wbuf, BUF_SIZE,
        <span class="cn">404</span>, <span class="cv">"{\"error\":\"NOT_FOUND\"}"</span>);
    <span class="ck">return</span> -<span class="cn">1</span>;
}

<span class="cs">int</span> <span class="cf">main</span>(<span class="cs">void</span>) {
    <span class="cm">/* Create listen socket */</span>
    <span class="cs">int</span> listen_fd = socket(AF_INET, SOCK_STREAM, <span class="cn">0</span>);
    <span class="cs">int</span> opt = <span class="cn">1</span>;
    setsockopt(listen_fd, SOL_SOCKET, SO_REUSEADDR, &amp;opt, <span class="ck">sizeof</span>(opt));
    set_nonblocking(listen_fd);

    <span class="cs">struct sockaddr_in</span> addr = {
        .sin_family = AF_INET,
        .sin_port   = htons(PORT),
        .sin_addr.s_addr = INADDR_ANY
    };
    bind(listen_fd, (<span class="cs">struct sockaddr</span>*)&amp;addr, <span class="ck">sizeof</span>(addr));
    listen(listen_fd, SOMAXCONN);

    <span class="cm">/* Create epoll instance */</span>
    <span class="cs">int</span> epfd = epoll_create1(<span class="cn">0</span>);
    <span class="cs">struct epoll_event</span> ev = { .events = EPOLLIN, .data.fd = listen_fd };
    epoll_ctl(epfd, EPOLL_CTL_ADD, listen_fd, &amp;ev);

    <span class="cs">struct epoll_event</span> events[MAX_EVENTS];
    conn_t *conns[65536] = {<span class="cn">0</span>};  <span class="cm">/* indexed by fd (simplified) */</span>

    fprintf(stdout, <span class="cv">"Server listening on :%d\n"</span>, PORT);

    <span class="ck">for</span> (;;) {
        <span class="cs">int</span> n = epoll_wait(epfd, events, MAX_EVENTS, -<span class="cn">1</span>);
        <span class="ck">for</span> (<span class="cs">int</span> i = <span class="cn">0</span>; i &lt; n; i++) {
            <span class="cs">int</span> fd = events[i].data.fd;

            <span class="ck">if</span> (fd == listen_fd) {
                <span class="cm">/* Accept new connections */</span>
                <span class="ck">for</span> (;;) {
                    <span class="cs">int</span> cfd = accept(listen_fd, NULL, NULL);
                    <span class="ck">if</span> (cfd &lt; <span class="cn">0</span>) <span class="ck">break</span>;  <span class="cm">/* EAGAIN: no more waiting */</span>
                    set_nonblocking(cfd);
                    conn_t *c = calloc(<span class="cn">1</span>, <span class="ck">sizeof</span>(conn_t));
                    c-&gt;fd = cfd;
                    conns[cfd] = c;
                    <span class="cs">struct epoll_event</span> cev = {
                        .events = EPOLLIN | EPOLLET,
                        .data.fd = cfd
                    };
                    epoll_ctl(epfd, EPOLL_CTL_ADD, cfd, &amp;cev);
                }
            } <span class="ck">else if</span> (events[i].events &amp; EPOLLIN) {
                conn_t *c = conns[fd];
                ssize_t nr = recv(fd, c-&gt;rbuf + c-&gt;rlen,
                                  BUF_SIZE - c-&gt;rlen - <span class="cn">1</span>, <span class="cn">0</span>);
                <span class="ck">if</span> (nr &lt;= <span class="cn">0</span>) {
                    epoll_ctl(epfd, EPOLL_CTL_DEL, fd, NULL);
                    close(fd); free(c); conns[fd] = NULL;
                    <span class="ck">continue</span>;
                }
                c-&gt;rlen += nr;
                c-&gt;rbuf[c-&gt;rlen] = <span class="cn">'\0'</span>;

                <span class="cm">/* Check if full request received */</span>
                <span class="ck">if</span> (strstr(c-&gt;rbuf, <span class="cv">"\r\n\r\n"</span>)) {
                    <span class="cs">char</span> method[<span class="cn">16</span>], uri[<span class="cn">256</span>];
                    sscanf(c-&gt;rbuf, <span class="cv">"%15s %255s"</span>, method, uri);
                    handle_request(c, method, uri);

                    <span class="cm">/* Switch to write mode */</span>
                    <span class="cs">struct epoll_event</span> wev = {
                        .events = EPOLLOUT | EPOLLET,
                        .data.fd = fd
                    };
                    epoll_ctl(epfd, EPOLL_CTL_MOD, fd, &amp;wev);
                }
            } <span class="ck">else if</span> (events[i].events &amp; EPOLLOUT) {
                conn_t *c = conns[fd];
                ssize_t nw = send(fd, c-&gt;wbuf + c-&gt;woff,
                                  c-&gt;wlen - c-&gt;woff, <span class="cn">0</span>);
                <span class="ck">if</span> (nw &gt; <span class="cn">0</span>) c-&gt;woff += nw;

                <span class="ck">if</span> (c-&gt;woff &gt;= c-&gt;wlen) {
                    <span class="cm">/* Done writing — reset for next request (keep-alive) */</span>
                    c-&gt;rlen = c-&gt;wlen = c-&gt;woff = <span class="cn">0</span>;
                    <span class="cs">struct epoll_event</span> rev = {
                        .events = EPOLLIN | EPOLLET,
                        .data.fd = fd
                    };
                    epoll_ctl(epfd, EPOLL_CTL_MOD, fd, &amp;rev);
                }
            }
        }
    }
}</div>
  </div>
</div>

</div><!-- /t-impl -->

<!-- TAB 8 — Labs & Checklist -->
<div id="t-labs" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 1 — Build &amp; Benchmark an epoll HTTP Server</div>
  <div class="lab-body">
    <div class="lab-step"><span class="sn">1</span> Compile and run the epoll server from Tab 7. Test with <code>curl -v http://localhost:8080/</code> — verify headers and body.</div>
    <div class="lab-step"><span class="sn">2</span> Benchmark with <code>wrk -t4 -c1000 -d30s http://localhost:8080/</code>. Record req/sec and latency p99.</div>
    <div class="lab-step"><span class="sn">3</span> Compare: modify server to use thread-per-request (one <code>pthread_create</code> per accept). Re-benchmark at c=1000. Compare req/sec, memory usage (<code>valgrind --tool=massif</code>).</div>
    <div class="lab-step"><span class="sn">4</span> Add a keep-alive test: <code>wrk --connections 100 --threads 4 --duration 30s --pipeline 10</code>. Observe connection reuse in server logs.</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 2 — HTTP Parser Fuzzing</div>
  <div class="lab-body">
    <div class="lab-step"><span class="sn">1</span> Compile the parser from Tab 7 with AddressSanitizer: <code>gcc -fsanitize=address,undefined -g http_parser.c -o parser_test</code></div>
    <div class="lab-step"><span class="sn">2</span> Write a test harness that feeds malformed inputs: missing CRLF, header without colon, zero Content-Length with body, negative Content-Length. Verify no crashes or buffer overflows.</div>
    <div class="lab-step"><span class="sn">3</span> Test HTTP request smuggling input: body with both Content-Length and Transfer-Encoding chunked. Verify your parser handles it per RFC (chunked wins).</div>
    <div class="lab-step"><span class="sn">4</span> <strong>Bonus:</strong> use libFuzzer: <code>clang -fsanitize=fuzzer,address -o fuzz_parser fuzz_parser.c http_parser.c</code>. Run for 60 seconds and inspect corpus.</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 3 — HTTP Headers &amp; Content Negotiation</div>
  <div class="lab-body">
    <div class="lab-step"><span class="sn">1</span> Add content negotiation to your server: if <code>Accept: application/xml</code> is requested, return XML; if <code>Accept: application/json</code>, return JSON. For unsupported types, return <code>406</code>.</div>
    <div class="lab-step"><span class="sn">2</span> Implement ETag caching: generate a simple ETag (e.g., SHA-1 of response body). On <code>If-None-Match</code> match, return <code>304 Not Modified</code> with empty body.</div>
    <div class="lab-step"><span class="sn">3</span> Add gzip compression: if <code>Accept-Encoding: gzip</code> present, compress response body with zlib. Add <code>Content-Encoding: gzip</code> header. Verify with <code>curl --compressed</code>.</div>
    <div class="lab-step"><span class="sn">4</span> Implement CORS middleware: add <code>Access-Control-Allow-Origin</code> and handle <code>OPTIONS</code> preflight. Test with a browser <code>fetch()</code> from a different origin.</div>
  </div>
</div>

<div class="sep">── Phase 0 Batch 2 Checklist ──</div>
<div class="two-col">
  <div>
    <ul class="cl">
      <li>Parse an HTTP/1.1 request at the byte level (request line, headers, body)</li>
      <li>Explain chunked transfer encoding and when it's used</li>
      <li>Describe HTTP request smuggling (CL.TE) and prevention</li>
      <li>Implement a non-blocking epoll server with keep-alive</li>
    </ul>
  </div>
  <div>
    <ul class="cl">
      <li>Describe HTTP/2 frame format and the 9 frame types</li>
      <li>Explain HPACK compression and the static/dynamic table</li>
      <li>Implement a middleware pipeline with short-circuit semantics</li>
      <li>Explain CORS preflight and which headers are required</li>
    </ul>
  </div>
</div>

<div class="mod-nav">
  <a href="/learning/backend/m01-dns-tcp-tls/" class="nb">← M01: DNS, TCP &amp; TLS</a>
  <a href="/learning/backend/" class="nb">↑ Roadmap</a>
  <a href="/learning/backend/m03-rest/" class="nb">M03: REST &amp; API Design →</a>
</div>

</div><!-- /t-labs -->
</div><!-- /mod-wrap -->

<script>
function vt(id,btn){
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
}
</script>
