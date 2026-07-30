---
layout: learning
title: "M03 — REST API Design"
permalink: /learning/backend/m03-rest/
---

<style>
/* ── Base ───────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#060d28 0%,#0d1a4a 35%,#121040 70%,#0a0d30 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0;
}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#7ab0f8;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#a8c4f8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#c8d8fc}

/* Tabs */
.tab-bar{display:flex;flex-wrap:wrap;background:#060d28;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab0f8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#a5b4fc;border-bottom-color:#a5b4fc}
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
.p-indigo .cp-hdr{background:#eceeff}[data-theme=dark] .p-indigo .cp-hdr{background:#141028}

.tag-blue  {background:#d0e8f8;color:#1a4a7c}
.tag-teal  {background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}
.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green {background:#c8e8d4;color:#0e4a28}
.tag-red   {background:#f4d0d0;color:#6c1a1a}
.tag-amber {background:#fae8a0;color:#5a3800}
.tag-indigo{background:#dde0ff;color:#2a2a7c}

/* Code blocks */
.cb{background:#080e28;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #6366f1}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#c8d4fc;white-space:pre}
.cm{color:#5a7a9a}.ck{color:#7ab0f8}.cv{color:#f0d080}.cs{color:#f0a060}

/* HTTP message blocks */
.http-msg{background:#080e28;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.7;border:1px solid #2a3468}
.http-msg .h-method{color:#f0a060;font-weight:700}
.http-msg .h-url{color:#a5b4fc}
.http-msg .h-hdr{color:#7ab0f8}
.http-msg .h-val{color:#f0d080}
.http-msg .h-status{color:#4ade80;font-weight:700}
.http-msg .h-err{color:#f87171;font-weight:700}
.http-msg .h-body{color:#c8d4fc}
.http-msg .h-comment{color:#4a5a8a;font-style:italic}

/* Insight / warning / note */
.ins{background:#eceeff;border:1.5px solid #6366f1;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#141028;border-color:#5054c8}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#3730a3}
[data-theme=dark] .ins strong{color:#a5b4fc}

.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}

.note{background:#e8eeff;border:1.5px solid #3b82f6;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .note{background:#0d1840;border-color:#2a5aac}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.note strong{color:#1a3a8c}
[data-theme=dark] .note strong{color:#7ab0f8}

.analogy{background:linear-gradient(135deg,#eef2ff,#ede9fe);border:1.5px solid #a5b4fc;border-radius:10px;padding:1.1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .analogy{background:linear-gradient(135deg,#0d1028,#140e28);border-color:#3a3a80}
.analogy p{margin:0;font-size:.88rem;line-height:1.7;color:var(--text-color,#222)}

/* Flow list */
.flow-list{list-style:none;padding:0;margin:.8rem 0}
.flow-list li{display:flex;align-items:flex-start;gap:.8rem;padding:.6rem 0;border-bottom:1px dashed var(--border-color,#e4e4e4);font-size:.88rem;line-height:1.6;color:var(--text-color,#222)}
.flow-list li:last-child{border-bottom:none}
.fl-step{min-width:28px;height:28px;border-radius:50%;background:#6366f1;color:#fff;font-size:.72rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:.1rem}

/* Tables */
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#6366f1;color:#fff;padding:.5rem .8rem;text-align:left;font-weight:700}
.t-table td{padding:.45rem .8rem;border-bottom:1px solid var(--border-color,#eee);vertical-align:top;color:var(--text-color,#222)}
.t-table tr:nth-child(even) td{background:rgba(99,102,241,.05)}
[data-theme=dark] .t-table th{background:#4040b0}
[data-theme=dark] .t-table tr:nth-child(even) td{background:rgba(99,102,241,.1)}

/* Two column */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.8rem 0}
@media(max-width:640px){.two-col{grid-template-columns:1fr}}

/* Do/Don't grid */
.do-dont{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.8rem 0}
@media(max-width:640px){.do-dont{grid-template-columns:1fr}}
.do-box,.dont-box{border-radius:8px;overflow:hidden}
.do-box .dd-hdr{background:#166534;color:#fff;padding:.4rem .8rem;font-size:.78rem;font-weight:700;font-family:monospace}
.dont-box .dd-hdr{background:#991b1b;color:#fff;padding:.4rem .8rem;font-size:.78rem;font-weight:700;font-family:monospace}
.do-box .dd-body,.dont-box .dd-body{background:#080e28;padding:.6rem .8rem;font-family:'Courier New',monospace;font-size:.8rem;line-height:1.7}
.do-box .dd-body{color:#86efac}
.dont-box .dd-body{color:#fca5a5}

/* Status code badges */
.sc{display:inline-block;font-family:monospace;font-size:.75rem;font-weight:700;padding:2px 7px;border-radius:4px;margin:1px}
.sc-2{background:#d1fae5;color:#065f46}
.sc-3{background:#dbeafe;color:#1e3a8a}
.sc-4{background:#fee2e2;color:#7f1d1d}
.sc-5{background:#fef3c7;color:#78350f}

/* RMM (Richardson Maturity Model) */
.rmm-levels{display:grid;grid-template-columns:repeat(4,1fr);gap:.6rem;margin:.8rem 0}
@media(max-width:640px){.rmm-levels{grid-template-columns:1fr 1fr}}
.rmm-level{border-radius:8px;overflow:hidden;border:1.5px solid var(--border-color,#ddd)}
.rmm-hdr{padding:.5rem .8rem;font-size:.78rem;font-weight:800;font-family:monospace}
.rmm-body{padding:.6rem .8rem;font-size:.8rem;line-height:1.5;color:var(--text-color,#555)}
.rmm-0 .rmm-hdr{background:#fde8e8;color:#7f1d1d}
.rmm-1 .rmm-hdr{background:#fef3c7;color:#78350f}
.rmm-2 .rmm-hdr{background:#d1fae5;color:#065f46}
.rmm-3 .rmm-hdr{background:#dde0ff;color:#2a2a7c}
[data-theme=dark] .rmm-level{background:#0a0e28;border-color:#2a2a50}
[data-theme=dark] .rmm-0 .rmm-hdr{background:#3a0808}
[data-theme=dark] .rmm-1 .rmm-hdr{background:#2a1800}
[data-theme=dark] .rmm-2 .rmm-hdr{background:#0a2818}
[data-theme=dark] .rmm-3 .rmm-hdr{background:#141038}

/* Method matrix */
.method-tag{display:inline-block;font-family:monospace;font-size:.72rem;font-weight:800;padding:2px 7px;border-radius:4px;margin:1px}
.m-get   {background:#d1fae5;color:#065f46}
.m-post  {background:#dbeafe;color:#1e3a8a}
.m-put   {background:#fef3c7;color:#78350f}
.m-patch {background:#ede9fe;color:#4c1d95}
.m-delete{background:#fee2e2;color:#7f1d1d}
.m-head  {background:#f0fdf4;color:#14532d}
.m-opts  {background:#f5f3ff;color:#4c1d95}

/* Lab box */
.lab-box{border:2px solid #6366f1;border-radius:12px;overflow:hidden;margin:1.5rem 0}
.lab-hdr{background:linear-gradient(90deg,#6366f1,#3b82f6);padding:.8rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr h3{margin:0;font-size:1rem;font-weight:800;color:#fff;border:none}
.lab-hdr .lab-tag{background:rgba(255,255,255,.25);border-radius:4px;padding:2px 8px;font-size:.7rem;font-family:monospace;color:#fff;font-weight:700}
.lab-body{padding:1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#222);margin:.4rem 0}
.lab-step{display:flex;gap:.7rem;margin:.6rem 0;align-items:flex-start;font-size:.88rem;line-height:1.6;color:var(--text-color,#222)}
.sn{min-width:24px;height:24px;border-radius:50%;background:#6366f1;color:#fff;font-size:.7rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:.15rem}

/* Checklist */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.4rem 0;font-size:.88rem;line-height:1.6;color:var(--text-color,#222);border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";color:#6366f1;font-size:1rem;flex-shrink:0;margin-top:.05rem}

/* Module nav */
.mod-nav{display:flex;justify-content:space-between;align-items:center;padding:1.2rem 0;margin-top:2rem;border-top:2px solid var(--border-color,#eee);flex-wrap:wrap;gap:.8rem}
.nb{display:inline-flex;align-items:center;gap:.4rem;font-size:.85rem;font-weight:600;color:#6366f1;text-decoration:none;padding:.45rem .9rem;border:1.5px solid #6366f1;border-radius:6px;transition:background .15s,color .15s}
.nb:hover{background:#6366f1;color:#fff}

/* Section separator */
.sep{border:none;border-top:1.5px dashed var(--border-color,#ddd);margin:1.5rem 0}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">Backend Engineering · Phase 1 · Module 3</div>
  <div class="mod-title">REST API Design</div>
  <div class="mod-subtitle">Design APIs that are intuitive, evolvable, and production-ready — before writing a single line of server code.</div>
  <div class="mod-pills">
    <span class="mod-pill">REST Constraints</span>
    <span class="mod-pill">Resource Modelling</span>
    <span class="mod-pill">HTTP Methods</span>
    <span class="mod-pill">Status Codes</span>
    <span class="mod-pill">Pagination</span>
    <span class="mod-pill">RFC 7807</span>
    <span class="mod-pill">Versioning</span>
    <span class="mod-pill">C/libcurl</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt('t0',this)">📋 Overview</button>
  <button class="tab-btn" onclick="vt('t1',this)">🏗️ Resource Design</button>
  <button class="tab-btn" onclick="vt('t2',this)">⚡ HTTP Methods</button>
  <button class="tab-btn" onclick="vt('t3',this)">🔢 Status Codes</button>
  <button class="tab-btn" onclick="vt('t4',this)">📄 Req &amp; Resp</button>
  <button class="tab-btn" onclick="vt('t5',this)">⚠️ Errors &amp; Versioning</button>
  <button class="tab-btn" onclick="vt('t6',this)">⚙️ C Implementation</button>
  <button class="tab-btn" onclick="vt('t7',this)">🔬 Labs</button>
  <button class="tab-btn" onclick="vt('t8',this)">✅ Checklist</button>
</div>

<!-- ══════════════════════════════════════════════════════ t0 Overview -->
<div id="t0" class="tab-pane active">

<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">🏛️</span><h3>REST: Architectural Style, Not a Protocol</h3><span class="tag tag-indigo">ROY FIELDING, 2000</span></div>
  <div class="cp-body">
    <p>REST (Representational State Transfer) was defined by Roy Fielding in his 2000 PhD dissertation. It is a set of architectural <em>constraints</em> on how a distributed hypermedia system should behave — not a spec, not a library, not a protocol.</p>
    <p>Most "REST APIs" in the wild only partially implement these constraints. Understanding the full model lets you make deliberate trade-offs rather than accidental ones.</p>
  </div>
</div>

<h3>The 6 REST Constraints</h3>
<ul class="flow-list">
  <li><span class="fl-step">1</span><span><strong>Client–Server</strong> — Separation of concerns: the UI/client and data storage/server evolve independently. Neither knows the internals of the other.</span></li>
  <li><span class="fl-step">2</span><span><strong>Stateless</strong> — Each request contains all information needed to process it. The server holds no session state between requests. Enables horizontal scaling and fault tolerance.</span></li>
  <li><span class="fl-step">3</span><span><strong>Cacheable</strong> — Responses must declare themselves cacheable or non-cacheable. Caching eliminates some client–server interactions, improving scalability and perceived performance.</span></li>
  <li><span class="fl-step">4</span><span><strong>Uniform Interface</strong> — The central REST constraint. Four sub-constraints: resource identification in requests, manipulation through representations, self-descriptive messages, and HATEOAS.</span></li>
  <li><span class="fl-step">5</span><span><strong>Layered System</strong> — The client cannot tell whether it's connected to the end server or an intermediary (load balancer, CDN, API gateway). Each layer only sees adjacent layers.</span></li>
  <li><span class="fl-step">6</span><span><strong>Code on Demand (optional)</strong> — Servers can extend client functionality by transferring executable code (JavaScript). The only optional constraint.</span></li>
</ul>

<div class="analogy"><p>🏛️ <strong>Analogy:</strong> REST is like a well-designed postal system. You write a self-contained letter (stateless request) addressed to a specific location (resource URL). The postal network (layered system) routes it without the sender knowing the path. The letter format is standardised (uniform interface). Replies can be archived (cacheable). The sender and postal network are independent organisations (client–server).</p></div>

<h3>Richardson Maturity Model</h3>
<p>The RMM measures how thoroughly an HTTP API adheres to REST. Most production APIs should aim for Level 2.</p>

<div class="rmm-levels">
  <div class="rmm-level rmm-0">
    <div class="rmm-hdr">Level 0 — Swamp of POX</div>
    <div class="rmm-body">Single endpoint. Everything is POST. XML or JSON payload defines the action. Essentially RPC over HTTP.<br><br><em>POST /api {"action":"getUser","id":1}</em></div>
  </div>
  <div class="rmm-level rmm-1">
    <div class="rmm-hdr">Level 1 — Resources</div>
    <div class="rmm-body">Multiple endpoints, one per resource type. Still using POST for all operations but URL encodes the noun.<br><br><em>POST /users/1 {"action":"get"}</em></div>
  </div>
  <div class="rmm-level rmm-2">
    <div class="rmm-hdr">Level 2 — HTTP Verbs</div>
    <div class="rmm-body">Correct HTTP methods (GET/POST/PUT/DELETE) + correct status codes. The industry standard for "REST API".<br><br><em>GET /users/1 → 200 OK</em></div>
  </div>
  <div class="rmm-level rmm-3">
    <div class="rmm-hdr">Level 3 — HATEOAS</div>
    <div class="rmm-body">Hypermedia links in responses guide clients through available actions. Self-documenting, evolvable. Rare in practice.<br><br><em>{"id":1, "_links":{"self":"/users/1","posts":"/users/1/posts"}}</em></div>
  </div>
</div>

<div class="ins"><p><strong>Practical takeaway:</strong> Design to Level 2 consistently. Add HATEOAS only if you have clients you cannot coordinate deployments with (public APIs, third-party integrations). The stateless constraint is the most important to enforce — sessions stored on the server destroy horizontal scaling.</p></div>

</div>

<!-- ══════════════════════════════════════════════════════ t1 Resource Design -->
<div id="t1" class="tab-pane">

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏗️</span><h3>Resources Are Nouns, Not Verbs</h3><span class="tag tag-blue">CORE PRINCIPLE</span></div>
  <div class="cp-body">
    <p>The single biggest mistake in URL design is using verbs. In REST, HTTP methods <em>are</em> the verbs. Your URLs should identify things (resources) — nouns. The action is expressed by the combination of HTTP method + URL.</p>
  </div>
</div>

<div class="do-dont">
  <div class="dont-box">
    <div class="dd-hdr">✗ DON'T — Verb URLs (RPC style)</div>
    <div class="dd-body">POST /getUser?id=42
POST /createUser
POST /deleteUser?id=42
POST /getUserPosts?userId=42
GET  /fetchAllOrders
POST /cancelOrder?orderId=5</div>
  </div>
  <div class="do-box">
    <div class="dd-hdr">✓ DO — Noun URLs (REST style)</div>
    <div class="dd-body">GET    /users/42
POST   /users
DELETE /users/42
GET    /users/42/posts
GET    /orders
DELETE /orders/5</div>
  </div>
</div>

<h3>URL Naming Conventions</h3>
<table class="t-table">
  <thead><tr><th>Rule</th><th>Good</th><th>Bad</th><th>Why</th></tr></thead>
  <tbody>
    <tr><td>Use plural nouns</td><td><code>/users</code>, <code>/orders</code></td><td><code>/user</code>, <code>/getOrder</code></td><td>Consistent regardless of count; collections are plural</td></tr>
    <tr><td>Lowercase, hyphen-separated</td><td><code>/blog-posts</code></td><td><code>/blogPosts</code>, <code>/BlogPosts</code></td><td>URLs are case-sensitive; hyphens improve readability</td></tr>
    <tr><td>No file extensions</td><td><code>/users/42</code></td><td><code>/users/42.json</code></td><td>Use <code>Accept</code> header for content negotiation</td></tr>
    <tr><td>No trailing slashes</td><td><code>/users/42</code></td><td><code>/users/42/</code></td><td>Trailing slash implies a directory; inconsistency causes 404s</td></tr>
    <tr><td>IDs in path for single resources</td><td><code>/users/42</code></td><td><code>/users?id=42</code></td><td>Path params for identity, query params for filtering</td></tr>
    <tr><td>Hierarchy mirrors relationships</td><td><code>/users/42/posts</code></td><td><code>/posts?author=42</code></td><td>Either works; use nesting max 2 levels deep</td></tr>
  </tbody>
</table>

<h3>Collections vs Items</h3>
<table class="t-table">
  <thead><tr><th>URL Pattern</th><th>Represents</th><th>Typical Operations</th></tr></thead>
  <tbody>
    <tr><td><code>/users</code></td><td>Collection of all users</td><td>GET (list), POST (create)</td></tr>
    <tr><td><code>/users/42</code></td><td>Single user with id=42</td><td>GET, PUT, PATCH, DELETE</td></tr>
    <tr><td><code>/users/42/posts</code></td><td>Posts belonging to user 42</td><td>GET (list), POST (create)</td></tr>
    <tr><td><code>/users/42/posts/7</code></td><td>Post 7 by user 42</td><td>GET, PUT, PATCH, DELETE</td></tr>
  </tbody>
</table>

<h3>Nesting: When to Stop</h3>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">📐</span><h3>Maximum 2 Levels of Nesting</h3><span class="tag tag-amber">DESIGN RULE</span></div>
  <div class="cp-body">
    <p>Deep nesting creates URLs that are hard to remember, hard to construct, and tightly coupled to your data model. After 2 levels, use query parameters or a flat URL with filter params.</p>
    <div class="do-dont">
      <div class="dont-box">
        <div class="dd-hdr">✗ Too Deep</div>
        <div class="dd-body">/orgs/5/teams/3/members/42/posts/7/comments/2</div>
      </div>
      <div class="do-box">
        <div class="dd-hdr">✓ Flatten at 2 Levels</div>
        <div class="dd-body">/comments/2
# or
/posts/7/comments/2</div>
      </div>
    </div>
    <p>The resource <code>/comments/2</code> is unambiguous — comment IDs are globally unique. The parent context is available from the comment's own <code>post_id</code> field in the response.</p>
  </div>
</div>

<h3>Special Actions That Don't Fit the Resource Model</h3>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Action Sub-Resources</h3><span class="tag tag-purple">PRAGMATISM</span></div>
  <div class="cp-body">
    <p>Some operations are inherently procedural and don't map cleanly to CRUD on a resource: "send a password reset email", "archive a conversation", "retry a failed payment". The pragmatic approach is to use an action sub-resource with POST.</p>
    <table class="t-table">
      <thead><tr><th>Action</th><th>REST-ish URL</th><th>Method</th></tr></thead>
      <tbody>
        <tr><td>Send password reset</td><td><code>/users/42/password-reset</code></td><td>POST</td></tr>
        <tr><td>Archive a post</td><td><code>/posts/7/archive</code></td><td>POST</td></tr>
        <tr><td>Publish a draft</td><td><code>/posts/7/publish</code></td><td>POST</td></tr>
        <tr><td>Retry payment</td><td><code>/payments/9/retry</code></td><td>POST</td></tr>
        <tr><td>Transfer ownership</td><td><code>/orgs/5/ownership-transfers</code></td><td>POST (creates a transfer resource)</td></tr>
      </tbody>
    </table>
    <p>Note: "archive" creates an archived state, "publish" creates a publication event — these can be modelled as resource state transitions triggered by POST. The verb form (<code>/archive</code>) is tolerated here because the action sub-resource approach is the least bad option.</p>
  </div>
</div>

<h3>Query Parameters: Filtering, Sorting, Searching</h3>
<table class="t-table">
  <thead><tr><th>Operation</th><th>Convention</th><th>Example</th></tr></thead>
  <tbody>
    <tr><td>Filter by field</td><td><code>?field=value</code></td><td><code>GET /users?status=active&amp;role=admin</code></td></tr>
    <tr><td>Sort</td><td><code>?sort=field</code>, <code>?sort=-field</code> (minus = desc)</td><td><code>GET /users?sort=-created_at</code></td></tr>
    <tr><td>Full-text search</td><td><code>?q=term</code> or <code>?search=term</code></td><td><code>GET /posts?q=kubernetes</code></td></tr>
    <tr><td>Sparse fieldsets</td><td><code>?fields=f1,f2</code></td><td><code>GET /users/42?fields=id,name,email</code></td></tr>
    <tr><td>Embedded relations</td><td><code>?include=rel1,rel2</code></td><td><code>GET /posts/7?include=author,comments</code></td></tr>
    <tr><td>Pagination</td><td>see Req &amp; Resp tab</td><td><code>GET /users?page=2&amp;per_page=20</code></td></tr>
  </tbody>
</table>

</div>

<!-- ══════════════════════════════════════════════════════ t2 HTTP Methods -->
<div id="t2" class="tab-pane">

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Safety and Idempotency</h3><span class="tag tag-blue">RFC 9110</span></div>
  <div class="cp-body">
    <p>Two properties of HTTP methods govern how clients, proxies, and servers can safely retry and cache requests. Violating these contracts breaks the entire HTTP caching and reliability infrastructure.</p>
    <div class="two-col">
      <div>
        <h4>Safe</h4>
        <p>A method is <strong>safe</strong> if it does not alter server state. Clients, crawlers, and prefetch logic can freely call safe methods without side effects. GET, HEAD, OPTIONS, TRACE are safe.</p>
      </div>
      <div>
        <h4>Idempotent</h4>
        <p>A method is <strong>idempotent</strong> if calling it N times has the same effect as calling it once. Safe methods are inherently idempotent. PUT and DELETE are idempotent but not safe.</p>
      </div>
    </div>
  </div>
</div>

<h3>Method Reference</h3>
<table class="t-table">
  <thead><tr><th>Method</th><th>Safe</th><th>Idempotent</th><th>Has Body</th><th>Semantics</th></tr></thead>
  <tbody>
    <tr>
      <td><span class="method-tag m-get">GET</span></td>
      <td>✅</td><td>✅</td><td>No</td>
      <td>Retrieve resource or collection. Parameters via query string only. Responses should be cacheable.</td>
    </tr>
    <tr>
      <td><span class="method-tag m-head">HEAD</span></td>
      <td>✅</td><td>✅</td><td>No</td>
      <td>Same as GET but response body omitted. Used to check existence, get ETag, or measure response size without downloading.</td>
    </tr>
    <tr>
      <td><span class="method-tag m-post">POST</span></td>
      <td>❌</td><td>❌</td><td>Yes</td>
      <td>Create a new resource in a collection. Server assigns the ID. Returns 201 Created with Location header pointing to the new resource.</td>
    </tr>
    <tr>
      <td><span class="method-tag m-put">PUT</span></td>
      <td>❌</td><td>✅</td><td>Yes</td>
      <td>Full replacement of a resource. Client sends the complete representation. If resource doesn't exist, create it (optional). Idempotent — sending same request twice has same result.</td>
    </tr>
    <tr>
      <td><span class="method-tag m-patch">PATCH</span></td>
      <td>❌</td><td>❌*</td><td>Yes</td>
      <td>Partial update. Only the specified fields are modified. Not inherently idempotent (a <code>{"views": {"op":"increment"}}</code> patch is not). JSON Merge Patch (RFC 7396) or JSON Patch (RFC 6902) for structured updates.</td>
    </tr>
    <tr>
      <td><span class="method-tag m-delete">DELETE</span></td>
      <td>❌</td><td>✅</td><td>Rare</td>
      <td>Delete a resource. First call returns 200/204; repeat calls should return 404 (or 204 again for strict idempotency). Soft-delete returns 200 with archived representation.</td>
    </tr>
    <tr>
      <td><span class="method-tag m-opts">OPTIONS</span></td>
      <td>✅</td><td>✅</td><td>No</td>
      <td>Returns allowed methods for a URL. Used by browsers in CORS preflight. Also useful for API discovery.</td>
    </tr>
  </tbody>
</table>

<div class="note"><p>*PATCH can be made idempotent by using a <strong>conditional update</strong> with <code>If-Match: "etag-value"</code> — the server only applies the patch if the current ETag matches, preventing lost updates.</p></div>

<h3>PUT vs PATCH: Choosing the Right One</h3>
<div class="two-col">
  <div>
    <div class="cp p-blue" style="margin:0">
      <div class="cp-hdr"><span class="ico">🔄</span><h3>PUT — Full Replacement</h3></div>
      <div class="cp-body">
        <p>Client must send the <em>entire</em> resource. Missing fields are set to null/default, not preserved.</p>
        <div class="http-msg">
<span class="h-method">PUT</span> <span class="h-url">/users/42</span>
<span class="h-hdr">Content-Type:</span> <span class="h-val">application/json</span>

<span class="h-body">{
  "name": "Alice",
  "email": "alice@example.com",
  "role": "admin"
}
</span><span class="h-comment">// ALL fields required — omitting
// "role" would clear it</span>
        </div>
        <p>Use when: client owns the full resource and wants a clean replacement.</p>
      </div>
    </div>
  </div>
  <div>
    <div class="cp p-purple" style="margin:0">
      <div class="cp-hdr"><span class="ico">✏️</span><h3>PATCH — Partial Update</h3></div>
      <div class="cp-body">
        <p>Client sends only the fields to change. Other fields are preserved.</p>
        <div class="http-msg">
<span class="h-method">PATCH</span> <span class="h-url">/users/42</span>
<span class="h-hdr">Content-Type:</span> <span class="h-val">application/merge-patch+json</span>

<span class="h-body">{
  "email": "newemail@example.com"
}
</span><span class="h-comment">// Only email updated; name
// and role unchanged</span>
        </div>
        <p>Use when: only a subset of fields should change, or partial updates are the main use case.</p>
      </div>
    </div>
  </div>
</div>

<h3>JSON Merge Patch vs JSON Patch</h3>
<table class="t-table">
  <thead><tr><th>Format</th><th>RFC</th><th>Mechanism</th><th>Best for</th></tr></thead>
  <tbody>
    <tr><td><strong>JSON Merge Patch</strong></td><td>RFC 7396</td><td>Merge the patch object into the resource. Set field to <code>null</code> to delete it.</td><td>Simple field updates, human-readable patches</td></tr>
    <tr><td><strong>JSON Patch</strong></td><td>RFC 6902</td><td>Array of operations: <code>add</code>, <code>remove</code>, <code>replace</code>, <code>move</code>, <code>copy</code>, <code>test</code>. Operates on JSON Pointer paths.</td><td>Complex mutations, array element updates, transactional multi-field updates</td></tr>
  </tbody>
</table>
<div class="cb"><pre><span class="h-comment">// JSON Patch (RFC 6902) example</span>
[
  { "op": "replace", "path": "/email", "value": "new@example.com" },
  { "op": "add",     "path": "/tags/-", "value": "premium" },
  { "op": "remove",  "path": "/legacy_id" },
  { "op": "test",    "path": "/version", "value": 3 }  <span class="cm">// fails patch if version != 3</span>
]</pre></div>

<h3>Idempotency Keys for POST</h3>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔑</span><h3>Making POST Safe to Retry</h3><span class="tag tag-green">DISTRIBUTED SYSTEMS</span></div>
  <div class="cp-body">
    <p>POST is not idempotent — retrying a failed payment POST could charge twice. The solution is an <strong>idempotency key</strong>: a client-generated UUID sent with the request. The server stores the key + response, and on retry returns the cached response without re-executing.</p>
    <div class="http-msg">
<span class="h-method">POST</span> <span class="h-url">/payments</span>
<span class="h-hdr">Idempotency-Key:</span> <span class="h-val">550e8400-e29b-41d4-a716-446655440000</span>
<span class="h-hdr">Content-Type:</span> <span class="h-val">application/json</span>

<span class="h-body">{ "amount": 9900, "currency": "USD", "card_id": "card_abc" }</span>
    </div>
    <p>Stripe, PayPal, and most payment APIs use this pattern. Idempotency key storage: Redis or DB table with TTL of 24 hours is standard.</p>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════ t3 Status Codes -->
<div id="t3" class="tab-pane">

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔢</span><h3>Status Codes Are Semantic Contracts</h3><span class="tag tag-blue">RFC 9110</span></div>
  <div class="cp-body">
    <p>Returning the wrong status code breaks client retry logic, caching, monitoring dashboards, and on-call alerting. Always use the most specific code available. Never return 200 for errors ("200 with an error body" is a Level 0 anti-pattern).</p>
  </div>
</div>

<h3>2xx — Success</h3>
<table class="t-table">
  <thead><tr><th>Code</th><th>Name</th><th>Use when</th></tr></thead>
  <tbody>
    <tr><td><span class="sc sc-2">200</span></td><td>OK</td><td>GET, PUT, PATCH succeeded. Return the updated representation in body.</td></tr>
    <tr><td><span class="sc sc-2">201</span></td><td>Created</td><td>POST created a new resource. Include <code>Location: /resources/new-id</code> header. Optionally return the created resource.</td></tr>
    <tr><td><span class="sc sc-2">202</span></td><td>Accepted</td><td>Request accepted but processing not yet complete (async job queued). Return a job/status resource URL.</td></tr>
    <tr><td><span class="sc sc-2">204</span></td><td>No Content</td><td>DELETE succeeded, or PATCH/PUT with no response body needed. No body — not even <code>{}</code>.</td></tr>
    <tr><td><span class="sc sc-2">206</span></td><td>Partial Content</td><td>Response is a range of a larger resource (used with <code>Range</code> header for resumable downloads).</td></tr>
  </tbody>
</table>

<h3>3xx — Redirection</h3>
<table class="t-table">
  <thead><tr><th>Code</th><th>Name</th><th>Use when</th></tr></thead>
  <tbody>
    <tr><td><span class="sc sc-3">301</span></td><td>Moved Permanently</td><td>Resource has a new permanent URL. Clients and search engines should update their bookmarks. Method may change to GET.</td></tr>
    <tr><td><span class="sc sc-3">302</span></td><td>Found</td><td>Temporary redirect. Often misused as permanent redirect. Browsers change POST → GET.</td></tr>
    <tr><td><span class="sc sc-3">303</span></td><td>See Other</td><td>After a POST (create), redirect client to the created resource with GET. The Post/Redirect/Get pattern.</td></tr>
    <tr><td><span class="sc sc-3">304</span></td><td>Not Modified</td><td>Conditional GET (with <code>If-None-Match</code> or <code>If-Modified-Since</code>) — cached version is still fresh. No body.</td></tr>
    <tr><td><span class="sc sc-3">307</span></td><td>Temporary Redirect</td><td>Like 302 but method is preserved. POST → same POST at new URL.</td></tr>
    <tr><td><span class="sc sc-3">308</span></td><td>Permanent Redirect</td><td>Like 301 but method is preserved. POST → same POST at new URL permanently.</td></tr>
  </tbody>
</table>

<h3>4xx — Client Errors</h3>
<table class="t-table">
  <thead><tr><th>Code</th><th>Name</th><th>Use when</th></tr></thead>
  <tbody>
    <tr><td><span class="sc sc-4">400</span></td><td>Bad Request</td><td>Request is malformed, missing required fields, or fails validation. Include error details in body.</td></tr>
    <tr><td><span class="sc sc-4">401</span></td><td>Unauthorized</td><td>Not authenticated. Despite the name, means "please authenticate". Include <code>WWW-Authenticate</code> header.</td></tr>
    <tr><td><span class="sc sc-4">403</span></td><td>Forbidden</td><td>Authenticated but not authorised. Client identity is known; the action is not permitted for this identity.</td></tr>
    <tr><td><span class="sc sc-4">404</span></td><td>Not Found</td><td>Resource doesn't exist. Also used to hide existence of protected resources (instead of 403).</td></tr>
    <tr><td><span class="sc sc-4">405</span></td><td>Method Not Allowed</td><td>HTTP method not supported for this URL. Include <code>Allow: GET, POST</code> header listing supported methods.</td></tr>
    <tr><td><span class="sc sc-4">409</span></td><td>Conflict</td><td>State conflict — duplicate key, version mismatch (optimistic locking), or concurrent modification.</td></tr>
    <tr><td><span class="sc sc-4">410</span></td><td>Gone</td><td>Resource existed but was permanently deleted. Use when you want clients/crawlers to remove cached reference.</td></tr>
    <tr><td><span class="sc sc-4">422</span></td><td>Unprocessable Entity</td><td>Well-formed request but semantic validation failed (e.g., start_date &gt; end_date). Distinguished from 400 (malformed).</td></tr>
    <tr><td><span class="sc sc-4">429</span></td><td>Too Many Requests</td><td>Rate limit exceeded. Include <code>Retry-After</code> and <code>X-RateLimit-*</code> headers.</td></tr>
  </tbody>
</table>

<h3>5xx — Server Errors</h3>
<table class="t-table">
  <thead><tr><th>Code</th><th>Name</th><th>Use when</th></tr></thead>
  <tbody>
    <tr><td><span class="sc sc-5">500</span></td><td>Internal Server Error</td><td>Unhandled exception, bug, or unexpected state. Never expose stack traces. Log internally, return safe error message.</td></tr>
    <tr><td><span class="sc sc-5">502</span></td><td>Bad Gateway</td><td>Upstream server (DB, microservice) returned an invalid response. Set by proxies/load balancers.</td></tr>
    <tr><td><span class="sc sc-5">503</span></td><td>Service Unavailable</td><td>Server temporarily overloaded or in maintenance. Include <code>Retry-After</code> header. Clients should back off.</td></tr>
    <tr><td><span class="sc sc-5">504</span></td><td>Gateway Timeout</td><td>Upstream server didn't respond in time. Set by proxies/load balancers. Distinguished from 503.</td></tr>
  </tbody>
</table>

<div class="warn"><p>⚠️ <strong>The 401 vs 403 trap:</strong> 401 = "I don't know who you are, please authenticate". 403 = "I know who you are, but you can't do this". Never return 403 to an unauthenticated request — it reveals that the resource exists and is protected. Prefer 401 or 404 depending on whether you want to expose existence.</p></div>

</div>

<!-- ══════════════════════════════════════════════════════ t4 Req & Resp -->
<div id="t4" class="tab-pane">

<h3>Content Negotiation</h3>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📋</span><h3>Accept &amp; Content-Type</h3><span class="tag tag-blue">RFC 9110</span></div>
  <div class="cp-body">
    <p>HTTP allows clients and servers to negotiate representation format without changing the URL. Use the standard headers — don't invent <code>/api/users.json</code> URL-based formats.</p>
    <table class="t-table">
      <thead><tr><th>Header</th><th>Direction</th><th>Meaning</th></tr></thead>
      <tbody>
        <tr><td><code>Accept</code></td><td>Client → Server</td><td>Formats the client can handle, by preference: <code>Accept: application/json, application/xml;q=0.8</code></td></tr>
        <tr><td><code>Content-Type</code></td><td>Both</td><td>Format of the body being sent: <code>Content-Type: application/json</code></td></tr>
        <tr><td><code>Accept-Language</code></td><td>Client → Server</td><td>Preferred language for localised responses</td></tr>
        <tr><td><code>Accept-Encoding</code></td><td>Client → Server</td><td>Compression formats supported: <code>Accept-Encoding: gzip, deflate, br</code></td></tr>
      </tbody>
    </table>
    <p>If the server cannot satisfy the <code>Accept</code> header, return <span class="sc sc-4">406</span> Not Acceptable.</p>
  </div>
</div>

<h3>Pagination Strategies</h3>
<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">📄</span><h3>Three Pagination Patterns</h3><span class="tag tag-indigo">SCALABILITY</span></div>
  <div class="cp-body">
    <div class="two-col">
      <div>
        <h4>Offset Pagination</h4>
        <div class="http-msg">
<span class="h-method">GET</span> <span class="h-url">/users?page=3&amp;per_page=20</span>
<span class="h-comment">// SQL: LIMIT 20 OFFSET 40</span>
        </div>
        <p><strong>Pros:</strong> Simple, random access to any page, total count available.</p>
        <p><strong>Cons:</strong> Inconsistent results when items are inserted/deleted during pagination (items shift). Slow for high offsets (DB scans all preceding rows). Not recommended past page 100.</p>
      </div>
      <div>
        <h4>Cursor Pagination</h4>
        <div class="http-msg">
<span class="h-method">GET</span> <span class="h-url">/users?after=cursor_abc&amp;limit=20</span>
<span class="h-comment">// SQL: WHERE id > :cursor LIMIT 20</span>
        </div>
        <p><strong>Pros:</strong> Stable under mutations (no shifting). O(1) regardless of page depth. The only scalable strategy for high-volume feeds.</p>
        <p><strong>Cons:</strong> No random access (must walk from start). No total count without a separate query.</p>
      </div>
    </div>
    <h4>Keyset Pagination (Time-based)</h4>
    <div class="http-msg">
<span class="h-method">GET</span> <span class="h-url">/events?before=2026-03-26T10:00:00Z&amp;limit=50</span>
<span class="h-comment">// SQL: WHERE created_at &lt; :before ORDER BY created_at DESC LIMIT 50</span>
    </div>
    <p>Variant of cursor pagination using a meaningful timestamp or composite key instead of an opaque cursor. Natural for time-series data (activity feeds, logs, notifications).</p>
  </div>
</div>

<h3>Pagination Response Envelope</h3>
<div class="http-msg">
<span class="h-hdr">HTTP/1.1</span> <span class="h-status">200 OK</span>
<span class="h-hdr">Content-Type:</span> <span class="h-val">application/json</span>
<span class="h-hdr">Link:</span> <span class="h-val">&lt;/users?after=cursor_xyz&gt;; rel="next", &lt;/users&gt;; rel="first"</span>

<span class="h-body">{
  "data": [
    { "id": 1, "name": "Alice", "email": "alice@example.com" },
    { "id": 2, "name": "Bob",   "email": "bob@example.com" }
  ],
  "pagination": {
    "next_cursor": "cursor_xyz",
    "has_more": true,
    "per_page": 20
  }
}</span>
</div>

<div class="ins"><p><strong>Use the <code>Link</code> header</strong> (RFC 5988) for hypermedia pagination links — this is the standard HTTP way. The response body pagination object is a convenience for clients that don't parse headers. Provide both.</p></div>

<h3>Response Envelope vs Bare Resources</h3>
<div class="two-col">
  <div>
    <h4>Bare Resource (simple)</h4>
    <div class="http-msg">
<span class="h-body">{
  "id": 42,
  "name": "Alice",
  "email": "alice@example.com"
}</span>
    </div>
    <p style="font-size:.82rem;color:var(--text-color,#555)">Clean, minimal. Standard for single-resource responses. Client knows it's talking to <code>/users/42</code>.</p>
  </div>
  <div>
    <h4>Envelope (for collections)</h4>
    <div class="http-msg">
<span class="h-body">{
  "data": [...],
  "meta": {
    "total": 1234,
    "page": 2
  },
  "links": {
    "next": "/users?page=3",
    "prev": "/users?page=1"
  }
}</span>
    </div>
    <p style="font-size:.82rem;color:var(--text-color,#555)">Wraps collection with metadata. JSON:API and HAL both use envelope patterns.</p>
  </div>
</div>

<h3>Caching with ETags</h3>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">💾</span><h3>Conditional Requests</h3><span class="tag tag-green">PERFORMANCE</span></div>
  <div class="cp-body">
    <p>ETags (entity tags) enable cache validation and optimistic locking. The server returns an ETag (hash of resource content) with each response. Clients send it back on subsequent requests.</p>
    <div class="http-msg">
<span class="h-comment">// First request</span>
<span class="h-method">GET</span> <span class="h-url">/users/42</span>

<span class="h-hdr">HTTP/1.1</span> <span class="h-status">200 OK</span>
<span class="h-hdr">ETag:</span> <span class="h-val">"abc123"</span>
<span class="h-hdr">Cache-Control:</span> <span class="h-val">max-age=60</span>

<span class="h-comment">// Conditional GET (after cache expires)</span>
<span class="h-method">GET</span> <span class="h-url">/users/42</span>
<span class="h-hdr">If-None-Match:</span> <span class="h-val">"abc123"</span>

<span class="h-hdr">HTTP/1.1</span> <span class="h-status">304 Not Modified</span>  <span class="h-comment">← no body, saves bandwidth</span>

<span class="h-comment">// Conditional UPDATE (optimistic locking)</span>
<span class="h-method">PATCH</span> <span class="h-url">/users/42</span>
<span class="h-hdr">If-Match:</span> <span class="h-val">"abc123"</span>
<span class="h-comment">// → 412 Precondition Failed if someone else modified it first</span>
    </div>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════ t5 Errors & Versioning -->
<div id="t5" class="tab-pane">

<h3>RFC 7807 — Problem Details</h3>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">📄</span><h3>Structured Error Responses</h3><span class="tag tag-red">RFC 7807</span></div>
  <div class="cp-body">
    <p>RFC 7807 defines a standard JSON format for HTTP API error responses. Adopting it means clients can parse errors predictably, and monitoring tools can aggregate them by type.</p>
    <p>Content-Type: <code>application/problem+json</code></p>
    <table class="t-table">
      <thead><tr><th>Field</th><th>Type</th><th>Required</th><th>Description</th></tr></thead>
      <tbody>
        <tr><td><code>type</code></td><td>URI</td><td>Yes</td><td>A URI identifying the problem type. Should resolve to human-readable documentation. Use <code>about:blank</code> if no docs exist.</td></tr>
        <tr><td><code>title</code></td><td>string</td><td>Yes</td><td>Short, human-readable summary. Should not change between occurrences of the same problem type.</td></tr>
        <tr><td><code>status</code></td><td>integer</td><td>Yes</td><td>HTTP status code. Must match the response status.</td></tr>
        <tr><td><code>detail</code></td><td>string</td><td>No</td><td>Human-readable explanation specific to this occurrence.</td></tr>
        <tr><td><code>instance</code></td><td>URI</td><td>No</td><td>URI identifying this specific occurrence. Can be used to look up a log entry or support ticket.</td></tr>
      </tbody>
    </table>
  </div>
</div>

<h3>RFC 7807 Examples</h3>
<div class="two-col">
  <div>
    <h4>Validation Error (400/422)</h4>
    <div class="http-msg">
<span class="h-hdr">HTTP/1.1</span> <span class="h-err">422 Unprocessable Entity</span>
<span class="h-hdr">Content-Type:</span> <span class="h-val">application/problem+json</span>

<span class="h-body">{
  "type": "https://api.example.com/errors/validation-error",
  "title": "Validation Failed",
  "status": 422,
  "detail": "Request body contains invalid fields.",
  "instance": "/requests/req_abc123",
  "errors": [
    {
      "field": "email",
      "code": "INVALID_FORMAT",
      "message": "Must be a valid email address"
    },
    {
      "field": "age",
      "code": "OUT_OF_RANGE",
      "message": "Must be between 0 and 150"
    }
  ]
}</span>
    </div>
  </div>
  <div>
    <h4>Not Found (404)</h4>
    <div class="http-msg">
<span class="h-hdr">HTTP/1.1</span> <span class="h-err">404 Not Found</span>
<span class="h-hdr">Content-Type:</span> <span class="h-val">application/problem+json</span>

<span class="h-body">{
  "type": "https://api.example.com/errors/resource-not-found",
  "title": "Resource Not Found",
  "status": 404,
  "detail": "User with id 42 does not exist.",
  "instance": "/requests/req_def456"
}</span>
    </div>
    <h4>Rate Limit (429)</h4>
    <div class="http-msg">
<span class="h-hdr">HTTP/1.1</span> <span class="h-err">429 Too Many Requests</span>
<span class="h-hdr">Retry-After:</span> <span class="h-val">30</span>
<span class="h-hdr">X-RateLimit-Limit:</span> <span class="h-val">100</span>
<span class="h-hdr">X-RateLimit-Remaining:</span> <span class="h-val">0</span>
<span class="h-hdr">X-RateLimit-Reset:</span> <span class="h-val">1711447230</span>

<span class="h-body">{
  "type": "https://api.example.com/errors/rate-limit-exceeded",
  "title": "Rate Limit Exceeded",
  "status": 429,
  "detail": "100 requests per minute limit reached. Retry after 30 seconds."
}</span>
    </div>
  </div>
</div>

<h3>API Versioning Strategies</h3>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">🔖</span><h3>When and How to Version</h3><span class="tag tag-amber">EVOLVABILITY</span></div>
  <div class="cp-body">
    <p>You need versioning when a change is <strong>breaking</strong> — removes a field, changes a field type, alters semantics, removes an endpoint. Additive changes (new optional fields, new endpoints) are non-breaking and don't require a new version.</p>
  </div>
</div>

<table class="t-table">
  <thead><tr><th>Strategy</th><th>Example</th><th>Pros</th><th>Cons</th></tr></thead>
  <tbody>
    <tr>
      <td><strong>URL path</strong></td>
      <td><code>/v1/users</code>, <code>/v2/users</code></td>
      <td>Explicit, easily visible in logs and browsers, cacheable</td>
      <td>URL changes break bookmarks/hardcoded URLs</td>
    </tr>
    <tr>
      <td><strong>Query parameter</strong></td>
      <td><code>/users?version=2</code></td>
      <td>URL stable, easy to test in browser</td>
      <td>Easy to forget, pollutes query string, cache complications</td>
    </tr>
    <tr>
      <td><strong>Accept header</strong></td>
      <td><code>Accept: application/vnd.api+json;version=2</code></td>
      <td>Purist REST, URL unchanged, proper content negotiation</td>
      <td>Hard to test in browser, verbose, poorly supported by API gateways</td>
    </tr>
    <tr>
      <td><strong>Custom header</strong></td>
      <td><code>API-Version: 2026-03-01</code></td>
      <td>URL stable, Stripe-style date versioning is explicit</td>
      <td>Non-standard header, requires documentation</td>
    </tr>
  </tbody>
</table>

<div class="ins"><p><strong>Industry recommendation:</strong> URL path versioning (<code>/v1/</code>, <code>/v2/</code>) is the most widely adopted. It is explicit, easy to understand, and works with every HTTP client. Stripe uses date-based header versioning successfully, but they have exceptional API docs — for most teams, URL versioning is safer. Never version endpoints individually — version the whole API.</p></div>

<h3>Deprecation Process</h3>
<ul class="flow-list">
  <li><span class="fl-step">1</span><span><strong>Add deprecation headers</strong> to old API responses: <code>Deprecation: true</code>, <code>Sunset: Sat, 01 Jan 2028 00:00:00 GMT</code>, <code>Link: &lt;/v2/users&gt;; rel="successor-version"</code></span></li>
  <li><span class="fl-step">2</span><span><strong>Publish changelog</strong> with migration guide. List every breaking change and its replacement. Provide a diff of request/response shapes.</span></li>
  <li><span class="fl-step">3</span><span><strong>Email active consumers</strong> from your API key records. Give at least 6 months notice for significant breaking changes.</span></li>
  <li><span class="fl-step">4</span><span><strong>Monitor old version traffic</strong> — track last-call timestamps per API key. Sunset date should be after the last active consumer migrates (or times out).</span></li>
  <li><span class="fl-step">5</span><span><strong>Hard sunset</strong> — return 410 Gone with a body pointing to the migration guide. Never return 404 (implies the endpoint never existed).</span></li>
</ul>

</div>

<!-- ══════════════════════════════════════════════════════ t6 C Implementation -->
<div id="t6" class="tab-pane">

<h3>HTTP Request Parsing in C (Minimal)</h3>
<div class="cb"><pre><span class="ck">#include</span> <span class="cv">&lt;string.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;stdio.h&gt;</span>

<span class="ck">typedef struct</span> {
    <span class="ck">char</span> method[<span class="cv">16</span>];
    <span class="ck">char</span> path[<span class="cv">256</span>];
    <span class="ck">char</span> version[<span class="cv">16</span>];
    <span class="ck">char</span> host[<span class="cv">256</span>];
    <span class="ck">char</span> content_type[<span class="cv">64</span>];
    <span class="ck">int</span>  content_length;
    <span class="ck">char</span> body[<span class="cv">8192</span>];
} http_request_t;

<span class="ck">int</span> parse_request(<span class="ck">const char</span> *raw, http_request_t *req) {
    <span class="cm">/* Parse request line: "METHOD /path HTTP/1.1\r\n" */</span>
    <span class="ck">if</span> (sscanf(raw, <span class="cs">"%15s %255s %15s"</span>,
               req->method, req->path, req->version) != <span class="cv">3</span>)
        <span class="ck">return</span> -<span class="cv">1</span>;

    <span class="cm">/* Parse headers line by line */</span>
    <span class="ck">const char</span> *p = strstr(raw, <span class="cs">"\r\n"</span>) + <span class="cv">2</span>;
    req->content_length = <span class="cv">0</span>;

    <span class="ck">while</span> (p &amp;&amp; *p != <span class="cv">'\r'</span>) {
        <span class="ck">if</span> (strncasecmp(p, <span class="cs">"Host: "</span>, <span class="cv">6</span>) == <span class="cv">0</span>)
            sscanf(p + <span class="cv">6</span>, <span class="cs">"%255[^\r]"</span>, req->host);
        <span class="ck">else if</span> (strncasecmp(p, <span class="cs">"Content-Type: "</span>, <span class="cv">14</span>) == <span class="cv">0</span>)
            sscanf(p + <span class="cv">14</span>, <span class="cs">"%63[^\r]"</span>, req->content_type);
        <span class="ck">else if</span> (strncasecmp(p, <span class="cs">"Content-Length: "</span>, <span class="cv">16</span>) == <span class="cv">0</span>)
            sscanf(p + <span class="cv">16</span>, <span class="cs">"%d"</span>, &amp;req->content_length);
        p = strstr(p, <span class="cs">"\r\n"</span>);
        <span class="ck">if</span> (p) p += <span class="cv">2</span>;
    }

    <span class="cm">/* Body starts after \r\n\r\n */</span>
    <span class="ck">const char</span> *body_start = strstr(raw, <span class="cs">"\r\n\r\n"</span>);
    <span class="ck">if</span> (body_start &amp;&amp; req->content_length > <span class="cv">0</span>) {
        body_start += <span class="cv">4</span>;
        <span class="ck">int</span> len = req->content_length < (<span class="ck">int</span>)<span class="ck">sizeof</span>(req->body) - <span class="cv">1</span>
                  ? req->content_length
                  : (<span class="ck">int</span>)<span class="ck">sizeof</span>(req->body) - <span class="cv">1</span>;
        memcpy(req->body, body_start, len);
        req->body[len] = <span class="cv">'\0'</span>;
    }
    <span class="ck">return</span> <span class="cv">0</span>;
}</pre></div>

<div class="warn"><p>⚠️ <strong>This is for learning only.</strong> Production HTTP parsing is complex: chunked encoding, multipart bodies, header folding, request smuggling defences, binary content. Use a battle-tested HTTP parser library (llhttp — the Node.js HTTP parser, or picohttpparser for C) in production code.</p></div>

<h3>HTTP Response Builder in C</h3>
<div class="cb"><pre><span class="ck">#include</span> <span class="cv">&lt;stdio.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;string.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;time.h&gt;</span>

<span class="ck">typedef struct</span> {
    <span class="ck">int</span>  status;
    <span class="ck">char</span> content_type[<span class="cv">64</span>];
    <span class="ck">char</span> body[<span class="cv">65536</span>];
    <span class="ck">int</span>  body_len;
} http_response_t;

<span class="ck">int</span> build_response(http_response_t *resp, <span class="ck">char</span> *out, <span class="ck">int</span> out_size) {
    <span class="ck">const char</span> *status_text;
    <span class="ck">switch</span> (resp->status) {
        <span class="ck">case</span> <span class="cv">200</span>: status_text = <span class="cs">"OK"</span>;                    <span class="ck">break</span>;
        <span class="ck">case</span> <span class="cv">201</span>: status_text = <span class="cs">"Created"</span>;               <span class="ck">break</span>;
        <span class="ck">case</span> <span class="cv">204</span>: status_text = <span class="cs">"No Content"</span>;             <span class="ck">break</span>;
        <span class="ck">case</span> <span class="cv">400</span>: status_text = <span class="cs">"Bad Request"</span>;            <span class="ck">break</span>;
        <span class="ck">case</span> <span class="cv">404</span>: status_text = <span class="cs">"Not Found"</span>;              <span class="ck">break</span>;
        <span class="ck">case</span> <span class="cv">422</span>: status_text = <span class="cs">"Unprocessable Entity"</span>;   <span class="ck">break</span>;
        <span class="ck">case</span> <span class="cv">500</span>: status_text = <span class="cs">"Internal Server Error"</span>; <span class="ck">break</span>;
        <span class="ck">default</span>:  status_text = <span class="cs">"Unknown"</span>;
    }

    <span class="cm">/* RFC 7231 date format */</span>
    <span class="ck">char</span> date_buf[<span class="cv">64</span>];
    time_t now = time(<span class="cs">NULL</span>);
    strftime(date_buf, <span class="ck">sizeof</span>(date_buf),
             <span class="cs">"%a, %d %b %Y %H:%M:%S GMT"</span>, gmtime(&amp;now));

    <span class="ck">int</span> n = snprintf(out, out_size,
        <span class="cs">"HTTP/1.1 %d %s\r\n"</span>
        <span class="cs">"Content-Type: %s\r\n"</span>
        <span class="cs">"Content-Length: %d\r\n"</span>
        <span class="cs">"Date: %s\r\n"</span>
        <span class="cs">"Connection: keep-alive\r\n"</span>
        <span class="cs">"\r\n"</span>,
        resp->status, status_text,
        resp->content_type,
        resp->body_len,
        date_buf);

    <span class="ck">if</span> (n + resp->body_len >= out_size) <span class="ck">return</span> -<span class="cv">1</span>;
    memcpy(out + n, resp->body, resp->body_len);
    <span class="ck">return</span> n + resp->body_len;
}

<span class="cm">/* Helper: respond with JSON */</span>
<span class="ck">void</span> respond_json(<span class="ck">int</span> fd, <span class="ck">int</span> status, <span class="ck">const char</span> *json) {
    http_response_t resp = {
        .status    = status,
        .body_len  = strlen(json)
    };
    strncpy(resp.content_type, <span class="cs">"application/json"</span>, <span class="ck">sizeof</span>(resp.content_type));
    memcpy(resp.body, json, resp.body_len);

    <span class="ck">char</span> out[<span class="cv">66000</span>];
    <span class="ck">int</span> len = build_response(&amp;resp, out, <span class="ck">sizeof</span>(out));
    <span class="ck">if</span> (len > <span class="cv">0</span>) send(fd, out, len, MSG_NOSIGNAL);
}

<span class="cm">/* Helper: RFC 7807 problem response */</span>
<span class="ck">void</span> respond_problem(<span class="ck">int</span> fd, <span class="ck">int</span> status, <span class="ck">const char</span> *type,
                      <span class="ck">const char</span> *title, <span class="ck">const char</span> *detail) {
    <span class="ck">char</span> body[<span class="cv">1024</span>];
    snprintf(body, <span class="ck">sizeof</span>(body),
        <span class="cs">"{"</span>
        <span class="cs">"\"type\":\"%s\","</span>
        <span class="cs">"\"title\":\"%s\","</span>
        <span class="cs">"\"status\":%d,"</span>
        <span class="cs">"\"detail\":\"%s\""</span>
        <span class="cs">"}"</span>,
        type, title, status, detail);

    http_response_t resp = { .status = status };
    strncpy(resp.content_type, <span class="cs">"application/problem+json"</span>, <span class="ck">sizeof</span>(resp.content_type));
    resp.body_len = strlen(body);
    memcpy(resp.body, body, resp.body_len);

    <span class="ck">char</span> out[<span class="cv">66000</span>];
    <span class="ck">int</span> len = build_response(&amp;resp, out, <span class="ck">sizeof</span>(out));
    <span class="ck">if</span> (len > <span class="cv">0</span>) send(fd, out, len, MSG_NOSIGNAL);
}</pre></div>

<h3>Consuming a REST API with libcurl (C)</h3>
<div class="cb"><pre><span class="ck">#include</span> <span class="cv">&lt;curl/curl.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;string.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;stdlib.h&gt;</span>
<span class="ck">#include</span> <span class="cv">&lt;stdio.h&gt;</span>

<span class="cm">/* Compile: gcc rest_client.c -lcurl -o rest_client */</span>

<span class="ck">typedef struct</span> { <span class="ck">char</span> *data; <span class="ck">size_t</span> len; } buf_t;

<span class="ck">static size_t</span> write_cb(<span class="ck">void</span> *ptr, <span class="ck">size_t</span> sz, <span class="ck">size_t</span> nmemb, buf_t *b) {
    <span class="ck">size_t</span> n = sz * nmemb;
    b->data = realloc(b->data, b->len + n + <span class="cv">1</span>);
    memcpy(b->data + b->len, ptr, n);
    b->len += n;
    b->data[b->len] = <span class="cv">'\0'</span>;
    <span class="ck">return</span> n;
}

<span class="cm">/* GET /users/42 with Bearer token */</span>
<span class="ck">int</span> get_user(<span class="ck">const char</span> *base_url, <span class="ck">int</span> user_id, <span class="ck">const char</span> *token) {
    CURL *curl = curl_easy_init();
    <span class="ck">if</span> (!curl) <span class="ck">return</span> -<span class="cv">1</span>;

    <span class="ck">char</span> url[<span class="cv">256</span>];
    snprintf(url, <span class="ck">sizeof</span>(url), <span class="cs">"%s/users/%d"</span>, base_url, user_id);

    buf_t resp = {<span class="cs">NULL</span>, <span class="cv">0</span>};

    <span class="cm">/* Auth header */</span>
    <span class="ck">char</span> auth[<span class="cv">512</span>];
    snprintf(auth, <span class="ck">sizeof</span>(auth), <span class="cs">"Authorization: Bearer %s"</span>, token);
    <span class="ck">struct</span> curl_slist *hdrs = curl_slist_append(<span class="cs">NULL</span>, auth);
    hdrs = curl_slist_append(hdrs, <span class="cs">"Accept: application/json"</span>);

    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, hdrs);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_cb);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &amp;resp);

    CURLcode rc = curl_easy_perform(curl);
    <span class="ck">long</span> http_code = <span class="cv">0</span>;
    curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &amp;http_code);

    <span class="ck">if</span> (rc == CURLE_OK) {
        printf(<span class="cs">"HTTP %ld\n%s\n"</span>, http_code, resp.data);
    } <span class="ck">else</span> {
        fprintf(stderr, <span class="cs">"curl error: %s\n"</span>, curl_easy_strerror(rc));
    }

    free(resp.data);
    curl_slist_free_all(hdrs);
    curl_easy_cleanup(curl);
    <span class="ck">return</span> rc == CURLE_OK ? <span class="cv">0</span> : -<span class="cv">1</span>;
}

<span class="cm">/* POST /users with JSON body */</span>
<span class="ck">int</span> create_user(<span class="ck">const char</span> *base_url, <span class="ck">const char</span> *json_body) {
    CURL *curl = curl_easy_init();
    <span class="ck">if</span> (!curl) <span class="ck">return</span> -<span class="cv">1</span>;

    <span class="ck">char</span> url[<span class="cv">256</span>];
    snprintf(url, <span class="ck">sizeof</span>(url), <span class="cs">"%s/users"</span>, base_url);

    buf_t resp = {<span class="cs">NULL</span>, <span class="cv">0</span>};
    <span class="ck">struct</span> curl_slist *hdrs = curl_slist_append(<span class="cs">NULL</span>, <span class="cs">"Content-Type: application/json"</span>);
    hdrs = curl_slist_append(hdrs, <span class="cs">"Accept: application/json"</span>);

    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_POST, <span class="cv">1L</span>);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, json_body);
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, hdrs);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_cb);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &amp;resp);

    CURLcode rc = curl_easy_perform(curl);
    <span class="ck">long</span> http_code = <span class="cv">0</span>;
    curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &amp;http_code);

    <span class="ck">if</span> (rc == CURLE_OK) {
        printf(<span class="cs">"HTTP %ld\n%s\n"</span>, http_code, resp.data);
        <span class="cm">/* 201: check Location header for new resource URL */</span>
    }

    free(resp.data);
    curl_slist_free_all(hdrs);
    curl_easy_cleanup(curl);
    <span class="ck">return</span> rc == CURLE_OK ? (<span class="ck">int</span>)http_code : -<span class="cv">1</span>;
}</pre></div>

<h3>Simple Router in C</h3>
<div class="cb"><pre><span class="ck">typedef void</span> (*handler_fn)(<span class="ck">int</span> fd, http_request_t *req);

<span class="ck">typedef struct</span> {
    <span class="ck">const char</span> *method;
    <span class="ck">const char</span> *path_prefix;
    handler_fn  handler;
} route_t;

<span class="ck">void</span> handle_get_users  (<span class="ck">int</span> fd, http_request_t *req);
<span class="ck">void</span> handle_get_user   (<span class="ck">int</span> fd, http_request_t *req);
<span class="ck">void</span> handle_create_user(<span class="ck">int</span> fd, http_request_t *req);

<span class="ck">static</span> route_t routes[] = {
    { <span class="cs">"GET"</span>,    <span class="cs">"/users/"</span>, handle_get_user   },  <span class="cm">/* /users/42 */</span>
    { <span class="cs">"GET"</span>,    <span class="cs">"/users"</span>,  handle_get_users  },  <span class="cm">/* /users    */</span>
    { <span class="cs">"POST"</span>,   <span class="cs">"/users"</span>,  handle_create_user},
    { <span class="cs">NULL</span>,     <span class="cs">NULL</span>,      <span class="cs">NULL</span>              }
};

<span class="ck">void</span> dispatch(<span class="ck">int</span> fd, http_request_t *req) {
    <span class="ck">for</span> (<span class="ck">int</span> i = <span class="cv">0</span>; routes[i].method; i++) {
        <span class="ck">if</span> (strcmp(req->method, routes[i].method) == <span class="cv">0</span> &amp;&amp;
            strncmp(req->path, routes[i].path_prefix,
                    strlen(routes[i].path_prefix)) == <span class="cv">0</span>) {
            routes[i].handler(fd, req);
            <span class="ck">return</span>;
        }
    }
    <span class="cm">/* 404 fallthrough */</span>
    respond_problem(fd, <span class="cv">404</span>,
        <span class="cs">"about:blank"</span>, <span class="cs">"Not Found"</span>,
        <span class="cs">"The requested resource does not exist."</span>);
}</pre></div>

</div>

<!-- ══════════════════════════════════════════════════════ t7 Labs -->
<div id="t7" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr">
    <h3>🔬 Lab 1 — Design a REST API (Paper Exercise)</h3>
    <span class="lab-tag">TOOLS: pen &amp; paper / whiteboard</span>
  </div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Practice resource modelling before writing code. Design the URL structure for a simple task management API.</p>
    <p><strong>Domain:</strong> Users create projects. Projects contain tasks. Tasks have comments. Tasks can be assigned to users.</p>
    <div class="lab-step"><span class="sn">1</span><span>List all the resources: users, projects, tasks, comments, assignments. For each, define the collection URL and item URL.</span></div>
    <div class="lab-step"><span class="sn">2</span><span>Define the full CRUD operations for each resource. For each operation write: <code>METHOD /path → STATUS</code> and describe the request body and response body.</span></div>
    <div class="lab-step"><span class="sn">3</span><span>Identify 3 operations that don't map cleanly to CRUD (e.g., "mark task complete", "reassign all tasks when user leaves"). Design action sub-resources for them.</span></div>
    <div class="lab-step"><span class="sn">4</span><span>Design the error responses for: creating a task in a project you don't own (403), creating a task with missing required fields (422), listing tasks for a non-existent project (404). Write full RFC 7807 bodies for each.</span></div>
    <div class="lab-step"><span class="sn">5</span><span>Add pagination to <code>GET /projects/:id/tasks</code>. Choose between offset and cursor pagination and justify your choice. Design the full response envelope including headers.</span></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">
    <h3>🔬 Lab 2 — Build a REST API Server in C</h3>
    <span class="lab-tag">TOOLS: gcc · curl · jq</span>
  </div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Build a minimal in-memory REST API for the Users resource using the TCP server and HTTP helpers from this module.</p>
    <div class="lab-step"><span class="sn">1</span><span>Start with the TCP echo server from M01 Lab 2. Replace the echo logic with <code>parse_request()</code> + <code>dispatch()</code>.</span></div>
    <div class="lab-step"><span class="sn">2</span><span>Implement an in-memory user store: <code>user_t users[MAX_USERS]</code> with fields id, name, email. Implement <code>handle_get_users</code> to return all users as a JSON array.</span></div>
    <div class="lab-step"><span class="sn">3</span><span>Implement <code>handle_create_user</code>: parse the JSON body (use simple <code>sscanf</code> or hand-roll a tiny parser), validate required fields (400/422 on failure), assign an auto-increment ID, return 201 with <code>Location: /users/:id</code>.</span></div>
    <div class="lab-step"><span class="sn">4</span><span>Implement <code>handle_get_user</code>: extract the ID from the path (<code>/users/42</code>), look up in the store, return 200 with user JSON or 404 RFC 7807 problem.</span></div>
    <div class="lab-step"><span class="sn">5</span><span>Test with curl:<br>
    <code>curl -s -X POST http://localhost:8080/users -H "Content-Type: application/json" -d '{"name":"Alice","email":"a@b.com"}' | jq</code><br>
    <code>curl -s http://localhost:8080/users | jq</code><br>
    <code>curl -s http://localhost:8080/users/1 | jq</code><br>
    <code>curl -s http://localhost:8080/users/999 | jq</code>
    </span></div>
    <div class="lab-step"><span class="sn">6</span><span><strong>Challenge:</strong> Add DELETE /users/:id returning 204, and PATCH /users/:id for partial updates. Add an <code>If-Match</code> ETag check to PATCH — return 412 if ETag doesn't match the current version hash.</span></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">
    <h3>🔬 Lab 3 — Consume a Public REST API with libcurl</h3>
    <span class="lab-tag">TOOLS: gcc · libcurl · jq</span>
  </div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Write a C program that consumes the GitHub REST API to list your own repositories.</p>
    <div class="lab-step"><span class="sn">1</span><span>Install libcurl: <code>sudo apt install libcurl4-openssl-dev</code> (Debian) or <code>brew install curl</code> (macOS).</span></div>
    <div class="lab-step"><span class="sn">2</span><span>Use the <code>create_user</code> / <code>get_user</code> libcurl code as a template. Call <code>GET https://api.github.com/users/YOUR_USERNAME/repos?per_page=5&amp;sort=updated</code>. Set header <code>User-Agent: my-rest-client/1.0</code> (GitHub requires this).</span></div>
    <div class="lab-step"><span class="sn">3</span><span>Print the HTTP status code and raw JSON response body.</span></div>
    <div class="lab-step"><span class="sn">4</span><span>Parse the JSON manually or with a tiny library (jsmn — single-file, no deps). Extract and print each repo's <code>name</code> and <code>stargazers_count</code>.</span></div>
    <div class="lab-step"><span class="sn">5</span><span>Handle pagination: read the <code>Link</code> header from the response. Extract the <code>rel="next"</code> URL and fetch the next page. Print all repos across pages.</span></div>
    <div class="lab-step"><span class="sn">6</span><span><strong>Stretch:</strong> Add a GitHub personal access token via <code>Authorization: Bearer TOKEN</code>. Verify you can now see private repos.</span></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">
    <h3>🔬 Lab 4 — Test Your API with Behaviour-Driven Tests</h3>
    <span class="lab-tag">TOOLS: bash · curl · jq · diff</span>
  </div>
  <div class="lab-body">
    <p><strong>Goal:</strong> Write a shell test suite for your REST server from Lab 2. Practice test-first API design thinking.</p>
    <div class="lab-step"><span class="sn">1</span><span>Create <code>test_api.sh</code>. Start with a helper function <code>assert_status(url, method, expected_code)</code> using curl's <code>-o /dev/null -s -w "%{http_code}"</code> output.</span></div>
    <div class="lab-step"><span class="sn">2</span><span>Test happy paths: POST creates user (201), GET /users returns array (200), GET /users/:id returns user (200), DELETE /users/:id returns 204.</span></div>
    <div class="lab-step"><span class="sn">3</span><span>Test error paths: POST with missing email (422), GET /users/9999 (404), DELETE /users/9999 (404). Verify each returns the correct status AND a <code>Content-Type: application/problem+json</code> header.</span></div>
    <div class="lab-step"><span class="sn">4</span><span>Test idempotency: call DELETE /users/:id twice. The first returns 204, the second should return 404. Call GET /users/:id twice — both must return the same body (verify with diff).</span></div>
  </div>
</div>

</div>

<!-- ══════════════════════════════════════════════════════ t8 Checklist -->
<div id="t8" class="tab-pane">

<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">✅</span><h3>Module Mastery Checklist</h3><span class="tag tag-indigo">M03 COMPLETE</span></div>
  <div class="cp-body">
    <p>You have mastered this module when you can check off every item below without referring to notes.</p>
  </div>
</div>

<h3>REST Fundamentals</h3>
<ul class="cl">
  <li>State the 6 REST constraints and identify which one is "uniform interface"</li>
  <li>Describe the 4 sub-constraints of the uniform interface (resource identification, manipulation through representations, self-descriptive messages, HATEOAS)</li>
  <li>Place a given API at the correct Richardson Maturity Model level and explain what changes would elevate it</li>
  <li>Explain why the stateless constraint is the most important for horizontal scaling</li>
</ul>

<h3>Resource Design</h3>
<ul class="cl">
  <li>Rewrite a set of verb URLs as correct REST resource URLs</li>
  <li>Explain the difference between path parameters (identity) and query parameters (filtering/sorting)</li>
  <li>Design URLs for a nested resource hierarchy with maximum 2 levels of nesting</li>
  <li>Design action sub-resources for non-CRUD operations (publish, archive, retry)</li>
  <li>Define the correct query parameter conventions for filtering, sorting, and full-text search</li>
</ul>

<h3>HTTP Methods</h3>
<ul class="cl">
  <li>Define safe and idempotent; classify GET, POST, PUT, PATCH, DELETE correctly on both axes</li>
  <li>Explain the difference between PUT (full replacement) and PATCH (partial update)</li>
  <li>Describe JSON Merge Patch (RFC 7396) vs JSON Patch (RFC 6902) and when to use each</li>
  <li>Explain idempotency keys: why they are needed for POST, how they work, where to store them</li>
  <li>Explain how to make a PATCH idempotent using conditional requests with <code>If-Match</code></li>
</ul>

<h3>Status Codes</h3>
<ul class="cl">
  <li>State the correct status codes for: create (201), no body (204), validation error (422), auth failure (401 vs 403), conflict (409), async accepted (202)</li>
  <li>Explain the difference between 401 and 403 — and why returning 403 to an unauthenticated user leaks information</li>
  <li>Explain when to use 410 Gone instead of 404 Not Found</li>
  <li>State which headers to include with 405 (Allow), 429 (Retry-After, X-RateLimit-*), and 201 (Location)</li>
</ul>

<h3>Request &amp; Response Design</h3>
<ul class="cl">
  <li>Compare offset pagination vs cursor pagination — state two advantages of cursor and one disadvantage</li>
  <li>Design a paginated response with correct <code>Link</code> header (RFC 5988) and response envelope</li>
  <li>Explain ETags: how they enable conditional GET (304) and optimistic locking on PATCH</li>
  <li>Use content negotiation correctly: <code>Accept</code> in request, <code>Content-Type</code> in response, 406 if unsatisfied</li>
</ul>

<h3>Errors &amp; Versioning</h3>
<ul class="cl">
  <li>Write a correct RFC 7807 problem detail response for a validation error, including the <code>errors</code> extension array</li>
  <li>Name 4 versioning strategies and state the pros and cons of URL path versioning</li>
  <li>Describe the full API deprecation process from announcement headers through hard sunset</li>
</ul>

<h3>Implementation</h3>
<ul class="cl">
  <li>Use libcurl in C to perform GET and POST requests with custom headers and JSON body, checking the response status code</li>
  <li>Build a minimal HTTP router in C using a method + path prefix dispatch table</li>
  <li>Return RFC 7807 problem+json responses from a C HTTP handler</li>
</ul>

<hr class="sep">
<div class="ins"><p><strong>Next modules in Phase 1:</strong> M04 covers OpenAPI specification and gRPC — moving from documentation by convention to contract-first design. M05 covers GraphQL — a fundamentally different query model that solves over-fetching and under-fetching at the cost of caching complexity.</p></div>

</div>

<!-- Module Nav -->
<div class="mod-nav">
  <a href="{{ '/learning/backend/m01-dns-tcp-tls/' | relative_url }}" class="nb">← M01 DNS/TCP/TLS</a>
  <span style="font-size:.8rem;color:var(--text-color,#888);font-family:monospace">Phase 1 · Module 3 of 5</span>
  <a href="{{ '/learning/backend/backend-roadmap/' | relative_url }}" class="nb">↑ Roadmap</a>
</div>

<script>
function vt(id, btn) {
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
}
</script>
