---
title: "M04 — gRPC & Protocol Buffers Deep Dive"
description: "Proto3 syntax, all 4 streaming modes, Protobuf wire encoding, gRPC error model, interceptors, gRPC-Gateway, and schema evolution — with C implementations using protobuf-c."
domain: engineering
track: backend
order: 4
ownHeader: true
url: /learning/backend/m04-grpc/
---

<style>
.mod-wrap{max-width:960px;margin:0 auto;padding:0 1rem 4rem;font-family:'Segoe UI',system-ui,sans-serif;color:#1e293b}
.mod-header{background:#fff;border-left:5px solid #3b82f6;border-radius:10px;padding:1.6rem 2rem;margin-bottom:1.5rem;box-shadow:0 2px 12px rgba(0,0,0,.08)}
.mod-header h1{margin:0 0 .4rem;font-size:1.75rem;color:#0f172a}
.mod-header .sub{color:#64748b;font-size:.95rem}
.phase-tag{display:inline-block;background:linear-gradient(90deg,#3b82f6,#6366f1);color:#fff;font-size:.75rem;font-weight:700;padding:.25rem .75rem;border-radius:20px;margin-right:.5rem;text-transform:uppercase;letter-spacing:.05em}
.tab-bar{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:1.25rem}
.tab-btn{padding:.45rem 1rem;border:2px solid #e2e8f0;border-radius:20px;background:#fff;font-size:.82rem;font-weight:600;cursor:pointer;color:#64748b;transition:all .2s}
.tab-btn:hover{border-color:#3b82f6;color:#1d4ed8}
.tab-btn.active{background:linear-gradient(135deg,#3b82f6,#6366f1);border-color:transparent;color:#fff;box-shadow:0 3px 10px rgba(59,130,246,.35)}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.cp-hdr{padding:.65rem 1.1rem;font-weight:700;font-size:.9rem;display:flex;align-items:center;gap:.5rem}
.cp-body{padding:1rem 1.2rem;background:#fff;font-size:.9rem;line-height:1.75}
.p-teal .cp-hdr{background:linear-gradient(90deg,#f0fdf4,#ccfbf1);color:#0f766e;border-left:4px solid #00c9a7}
.p-blue .cp-hdr{background:linear-gradient(90deg,#eff6ff,#dbeafe);color:#1d4ed8;border-left:4px solid #3b82f6}
.p-indigo .cp-hdr{background:linear-gradient(90deg,#eef2ff,#e0e7ff);color:#3730a3;border-left:4px solid #6366f1}
.p-green .cp-hdr{background:linear-gradient(90deg,#f0fdf4,#dcfce7);color:#15803d;border-left:4px solid #22c55e}
.p-orange .cp-hdr{background:linear-gradient(90deg,#fff7ed,#ffedd5);color:#c2410c;border-left:4px solid #f97316}
.p-purple .cp-hdr{background:linear-gradient(90deg,#faf5ff,#f3e8ff);color:#7e22ce;border-left:4px solid #a855f7}
.p-red .cp-hdr{background:linear-gradient(90deg,#fff1f2,#ffe4e6);color:#be123c;border-left:4px solid #f43f5e}
.p-amber .cp-hdr{background:linear-gradient(90deg,#fffbeb,#fef3c7);color:#92400e;border-left:4px solid #f59e0b}
.p-cyan .cp-hdr{background:linear-gradient(90deg,#ecfeff,#cffafe);color:#0e7490;border-left:4px solid #06b6d4}
.p-indigo{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.p-blue{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.p-orange{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.p-purple{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.ins,.warn,.note,.analogy{border-radius:8px;padding:.75rem 1rem;margin:.75rem 0;font-size:.87rem;line-height:1.7}
.ins{background:#eff6ff;border-left:4px solid #3b82f6;color:#1e3a5f}
.warn{background:#fff7ed;border-left:4px solid #f97316;color:#7c2d12}
.note{background:#eef2ff;border-left:4px solid #6366f1;color:#312e81}
.analogy{background:#faf5ff;border-left:4px solid #a855f7;color:#581c87}
.cb{background:#0f172a;border-radius:10px;padding:1.1rem 1.3rem;margin:.75rem 0;overflow-x:auto;font-size:.82rem;line-height:1.75;font-family:'Cascadia Code','Fira Code',monospace}
.cm{color:#94a3b8}.ck{color:#7dd3fc}.cv{color:#86efac}.cs{color:#fca5a5}
.cn{color:#fdba74}.cf{color:#c4b5fd}.co{color:#fde68a}.cg{color:#6ee7b7}
.flow-list{list-style:none;padding:0;margin:.5rem 0}
.fl-step{display:flex;align-items:flex-start;gap:.85rem;padding:.65rem .85rem;margin-bottom:.5rem;border-radius:8px;background:#f8fafc;border-left:3px solid #3b82f6;font-size:.88rem;line-height:1.65}
.fl-num{background:linear-gradient(135deg,#3b82f6,#6366f1);color:#fff;border-radius:50%;width:1.6rem;height:1.6rem;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.75rem;flex-shrink:0}
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.75rem 0}
.t-table th{background:linear-gradient(90deg,#3b82f6,#6366f1);color:#fff;padding:.6rem .9rem;text-align:left}
.t-table td{padding:.55rem .9rem;border-bottom:1px solid #e2e8f0;vertical-align:top}
.t-table tr:nth-child(even) td{background:#f8fafc}
.t-table tr:hover td{background:#eff6ff}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.75rem 0}
@media(max-width:640px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #3b82f6;border-radius:10px;margin-bottom:1.25rem;overflow:hidden}
.lab-hdr{background:linear-gradient(90deg,#eff6ff,#dbeafe);padding:.7rem 1.1rem;display:flex;align-items:center;gap:.6rem;font-weight:700;font-size:.9rem;color:#1d4ed8}
.lab-body{padding:1rem 1.2rem;font-size:.88rem;line-height:1.75}
.lab-step{padding:.4rem 0;padding-left:1.1rem;border-left:2px solid #3b82f6;margin-bottom:.4rem}
.sn{display:inline-block;background:#3b82f6;color:#fff;border-radius:50%;width:1.3rem;height:1.3rem;font-size:.7rem;font-weight:700;text-align:center;line-height:1.3rem;margin-right:.4rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{padding:.35rem .5rem;font-size:.87rem;display:flex;align-items:flex-start;gap:.6rem}
.cl li::before{content:"☐";color:#3b82f6;font-size:1rem;flex-shrink:0}
.diagram-box{background:#0f172a;border-radius:10px;padding:1.1rem 1.3rem;margin:.75rem 0;overflow-x:auto;font-family:'Cascadia Code','Fira Code',monospace;font-size:.78rem;line-height:1.8;color:#94a3b8}
.dg-blue{color:#93c5fd}.dg-indigo{color:#a5b4fc}.dg-green{color:#86efac}.dg-amber{color:#fde68a}.dg-gray{color:#64748b}.dg-red{color:#fca5a5}.dg-purple{color:#c4b5fd}.dg-teal{color:#5eead4}
.mod-nav{display:flex;justify-content:space-between;align-items:center;margin-top:2.5rem;padding:1rem 0;border-top:2px solid #e2e8f0;font-size:.88rem}
.nb{padding:.5rem 1.1rem;border:2px solid #3b82f6;border-radius:20px;color:#1d4ed8;text-decoration:none;font-weight:600;transition:all .2s}
.nb:hover{background:#3b82f6;color:#fff}
.sep{text-align:center;color:#94a3b8;font-size:.8rem;letter-spacing:.1em;margin:1.5rem 0;text-transform:uppercase}
</style>
<div class="mod-wrap">
<div class="mod-header">
  <h1>M04 — gRPC &amp; Protocol Buffers Deep Dive</h1>
  <div class="sub">
<span class="phase-tag">Phase 1</span>
    Proto3 syntax &amp; field encoding · Wire types &amp; varint · 4 streaming modes · gRPC error model · Interceptors &amp; middleware · gRPC-Gateway · Health checking · Schema evolution &amp; field rules
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt('t-overview',this)">Overview</button>
  <button class="tab-btn" onclick="vt('t-proto3',this)">Proto3 Syntax</button>
  <button class="tab-btn" onclick="vt('t-wire',this)">Wire Encoding</button>
  <button class="tab-btn" onclick="vt('t-streaming',this)">Streaming Modes</button>
  <button class="tab-btn" onclick="vt('t-errors',this)">Errors &amp; Interceptors</button>
  <button class="tab-btn" onclick="vt('t-gateway',this)">gRPC-Gateway</button>
  <button class="tab-btn" onclick="vt('t-c-impl',this)">C Implementation</button>
  <button class="tab-btn" onclick="vt('t-labs',this)">Labs &amp; Checklist</button>
</div>
<!-- ── OVERVIEW ─────────────────────────────────────────────── -->
<div id="t-overview" class="tab-pane active">
<div class="cp p-blue">
  <div class="cp-hdr">⚡ Why gRPC Exists</div>
  <div class="cp-body">
    REST over JSON is human-readable and universally supported — but every hop parses text, allocates strings, and re-serialises.
    Inside a datacenter where services talk thousands of times per second, that overhead compounds fast.<br><br>
    gRPC solves this with two decisions: <strong>binary serialisation</strong> (Protocol Buffers) and <strong>HTTP/2 multiplexing</strong>.
    A 100-field message that takes 2 KB as JSON may compress to 300 bytes as Protobuf.
    HTTP/2 lets 1,000 concurrent RPCs share one TCP connection — no head-of-line blocking per stream.
  </div>
</div>
<div class="analogy">
  <strong>Analogy — REST vs gRPC:</strong> REST is a postcard: readable by anyone, slow to write and parse.
  gRPC is a binary radio protocol: compact, fast, typed — but you need the schema (proto file) to decode it.
</div>
<div class="two-col">
  <div class="cp p-indigo">
<div class="cp-hdr">✅ Use gRPC When…</div>
<div class="cp-body">
<ul>
<li>Internal microservice-to-microservice calls</li>
<li>You need server or bidirectional streaming</li>
<li>Latency &lt; 5 ms is a hard requirement</li>
<li>Strong contract (IDL) enforcement matters</li>
<li>Polyglot services (generated clients in 12 languages)</li>
<li>Mobile apps — smaller payload = less battery</li>
</ul>
</div>
  </div>
  <div class="cp p-orange">
<div class="cp-hdr">🚫 Prefer REST When…</div>
<div class="cp-body">
<ul>
<li>Public API consumed by unknown clients</li>
<li>Browser JS front-ends (gRPC-Web workaround exists)</li>
<li>Simple CRUD with low traffic</li>
<li>Team unfamiliar with Protobuf toolchain</li>
<li>You need human-readable request/response in logs</li>
<li>Firewall/CDN doesn't pass HTTP/2 trailers</li>
</ul>
</div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr">🏗 gRPC Stack Layers</div>
  <div class="cp-body">
<div class="diagram-box">
<span class="dg-blue">┌─────────────────────────────────────────────────────────────┐</span>
<span class="dg-blue">│                     Application Code                        │</span>
<span class="dg-blue">│  Generated Stub (client)          Generated Service (server) │</span>
<span class="dg-blue">├─────────────────────────────────────────────────────────────┤</span>
<span class="dg-indigo">│                  gRPC Framework Layer                        │</span>
<span class="dg-indigo">│  Serialise/deserialise · Interceptors · Deadline propagation │</span>
<span class="dg-indigo">│  Health check · Retry · Load balancing                       │</span>
<span class="dg-indigo">├─────────────────────────────────────────────────────────────┤</span>
<span class="dg-green">│              Protocol Buffers (Encoding/Decoding)            │</span>
<span class="dg-green">│  Field tags · Varint encoding · Length-delimited bytes       │</span>
<span class="dg-green">├─────────────────────────────────────────────────────────────┤</span>
<span class="dg-amber">│                   HTTP/2 Transport                           │</span>
<span class="dg-amber">│  HEADERS frame (metadata) · DATA frames (Protobuf body)      │</span>
<span class="dg-amber">│  TRAILERS frame (status code + error details)                │</span>
<span class="dg-amber">├─────────────────────────────────────────────────────────────┤</span>
<span class="dg-gray">│                   TLS 1.3 / TCP                              │</span>
<span class="dg-gray">└─────────────────────────────────────────────────────────────┘</span>
</div>
  </div>
</div>
<table class="t-table">
  <thead><tr><th>Feature</th><th>REST / JSON</th><th>gRPC / Protobuf</th></tr></thead>
  <tbody>
<tr><td>Transport</td><td>HTTP/1.1 or HTTP/2</td><td>HTTP/2 only</td></tr>
<tr><td>Payload format</td><td>JSON (text)</td><td>Protobuf (binary)</td></tr>
<tr><td>Schema</td><td>Optional (OpenAPI)</td><td>Mandatory (.proto IDL)</td></tr>
<tr><td>Streaming</td><td>SSE / WebSocket (ad-hoc)</td><td>4 built-in modes</td></tr>
<tr><td>Code generation</td><td>Optional (openapi-generator)</td><td>Core requirement (protoc)</td></tr>
<tr><td>Browser support</td><td>Native</td><td>gRPC-Web proxy needed</td></tr>
<tr><td>Payload size (typical)</td><td>~3–10× larger</td><td>Baseline</td></tr>
<tr><td>Error model</td><td>HTTP status + body</td><td>Status code + rich details</td></tr>
  </tbody>
</table>
</div><!-- /t-overview -->
<!-- ── PROTO3 SYNTAX ─────────────────────────────────────────── -->
<div id="t-proto3" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr">📝 Proto3 File Structure</div>
  <div class="cp-body">
    Every <code>.proto</code> file begins with a syntax declaration and optional package/import directives.
    Field numbers (not names) are the stable API contract — they become the wire-format tag.
<div class="cb">
<span class="cm">// user_service.proto</span><br>
<span class="ck">syntax</span> = <span class="cv">"proto3"</span>;<br>
<span class="ck">package</span> <span class="cv">user.v1</span>;<br>
<br>
<span class="cm">// Go package option — ignored by other languages</span><br>
<span class="ck">option</span> go_package = <span class="cv">"github.com/acme/user/v1;userv1"</span>;<br>
<br>
<span class="ck">import</span> <span class="cv">"google/protobuf/timestamp.proto"</span>;<br>
<span class="ck">import</span> <span class="cv">"google/protobuf/empty.proto"</span>;<br>
<br>
<span class="cm">// ── Messages ────────────────────────────────────────────────</span><br>
<span class="ck">message</span> <span class="cf">User</span> {<br>
  <span class="ck">string</span>  id         = <span class="cn">1</span>;   <span class="cm">// field number = wire tag</span><br>
  <span class="ck">string</span>  email      = <span class="cn">2</span>;<br>
  <span class="ck">string</span>  username   = <span class="cn">3</span>;<br>
  <span class="ck">Role</span>    role       = <span class="cn">4</span>;   <span class="cm">// enum field</span><br>
  google.protobuf.<span class="ck">Timestamp</span> created_at = <span class="cn">5</span>;<br>
  <span class="ck">repeated</span> <span class="ck">string</span> tags = <span class="cn">6</span>;  <span class="cm">// list field</span><br>
  <span class="ck">oneof</span> contact {              <span class="cm">// only one field set at a time</span><br>
<span class="ck">string</span> phone = <span class="cn">7</span>;<br>
<span class="ck">string</span> slack = <span class="cn">8</span>;<br>
  }<br>
}<br>
<br>
<span class="ck">enum</span> <span class="cf">Role</span> {<br>
  <span class="ck">ROLE_UNSPECIFIED</span> = <span class="cn">0</span>;   <span class="cm">// proto3 default; first value MUST be 0</span><br>
  <span class="ck">ROLE_USER</span>        = <span class="cn">1</span>;<br>
  <span class="ck">ROLE_ADMIN</span>       = <span class="cn">2</span>;<br>
}<br>
<br>
<span class="ck">message</span> <span class="cf">GetUserRequest</span>  { <span class="ck">string</span> user_id = <span class="cn">1</span>; }<br>
<span class="ck">message</span> <span class="cf">ListUsersRequest</span> { <span class="ck">int32</span> page_size = <span class="cn">1</span>; <span class="ck">string</span> page_token = <span class="cn">2</span>; }<br>
<span class="ck">message</span> <span class="cf">ListUsersResponse</span>{ <span class="ck">repeated</span> <span class="ck">User</span> users = <span class="cn">1</span>; <span class="ck">string</span> next_page_token = <span class="cn">2</span>; }<br>
<br>
<span class="cm">// ── Service Definition ──────────────────────────────────────</span><br>
<span class="ck">service</span> <span class="cf">UserService</span> {<br>
  <span class="ck">rpc</span> GetUser      (<span class="cf">GetUserRequest</span>)                          <span class="ck">returns</span> (<span class="cf">User</span>);<br>
  <span class="ck">rpc</span> ListUsers    (<span class="cf">ListUsersRequest</span>)                        <span class="ck">returns</span> (<span class="cf">ListUsersResponse</span>);<br>
  <span class="ck">rpc</span> WatchUser    (<span class="cf">GetUserRequest</span>)                          <span class="ck">returns</span> (<span class="ck">stream</span> <span class="cf">User</span>);<br>
  <span class="ck">rpc</span> UploadUsers  (<span class="ck">stream</span> <span class="cf">User</span>)                            <span class="ck">returns</span> (<span class="cf">google.protobuf.Empty</span>);<br>
  <span class="ck">rpc</span> SyncUsers    (<span class="ck">stream</span> <span class="cf">GetUserRequest</span>)                  <span class="ck">returns</span> (<span class="ck">stream</span> <span class="cf">User</span>);<br>
}
</div>
  </div>
</div>
<div class="cp p-indigo">
  <div class="cp-hdr">📋 Field Type Cheat-Sheet</div>
  <div class="cp-body">
<table class="t-table">
  <thead><tr><th>Proto Type</th><th>Wire Type</th><th>C/C++ Mapping</th><th>Notes</th></tr></thead>
  <tbody>
<tr><td>double</td><td>1 (64-bit)</td><td>double</td><td>IEEE 754 little-endian</td></tr>
<tr><td>float</td><td>5 (32-bit)</td><td>float</td><td></td></tr>
<tr><td>int32 / int64</td><td>0 (varint)</td><td>int32_t / int64_t</td><td>Negative values cost 10 bytes; use sint32 instead</td></tr>
<tr><td>uint32 / uint64</td><td>0 (varint)</td><td>uint32_t / uint64_t</td><td></td></tr>
<tr><td>sint32 / sint64</td><td>0 (varint)</td><td>int32_t / int64_t</td><td>ZigZag-encoded; efficient for negatives</td></tr>
<tr><td>fixed32 / sfixed32</td><td>5 (32-bit)</td><td>uint32_t / int32_t</td><td>Always 4 bytes; efficient if values > 2²⁸</td></tr>
<tr><td>fixed64 / sfixed64</td><td>1 (64-bit)</td><td>uint64_t / int64_t</td><td>Always 8 bytes</td></tr>
<tr><td>bool</td><td>0 (varint)</td><td>bool</td><td>0 = false, 1 = true</td></tr>
<tr><td>string</td><td>2 (length-delimited)</td><td>char* / std::string</td><td>Must be valid UTF-8</td></tr>
<tr><td>bytes</td><td>2 (length-delimited)</td><td>uint8_t* + len</td><td>Arbitrary binary</td></tr>
<tr><td>message (nested)</td><td>2 (length-delimited)</td><td>struct pointer</td><td>Encoded as its own byte sequence</td></tr>
<tr><td>enum</td><td>0 (varint)</td><td>int32_t</td><td>Unknown values preserved in proto3</td></tr>
  </tbody>
</table>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr">🔒 Schema Evolution Rules (Backward &amp; Forward Compatibility)</div>
  <div class="cp-body">
<div class="two-col">
  <div>
<strong style="color:#15803d">✅ Safe Changes</strong>
<ul>
<li>Add a new field (new number)</li>
<li>Remove a field (mark number as <code>reserved</code>)</li>
<li>Add a value to an enum</li>
<li>Change a singular to <code>repeated</code></li>
<li>Change <code>string</code> to <code>bytes</code> (compatible wire type)</li>
</ul>
  </div>
  <div>
<strong style="color:#be123c">❌ Breaking Changes</strong>
<ul>
<li>Reuse a field number with a different type</li>
<li>Rename a field (breaks JSON mapping)</li>
<li>Change a field number</li>
<li>Remove the first enum value (changes default)</li>
<li>Move a field out of / into a <code>oneof</code></li>
</ul>
  </div>
</div>
<div class="cb">
<span class="cm">// Always reserve deleted field numbers and names:</span><br>
<span class="ck">message</span> <span class="cf">User</span> {<br>
  <span class="ck">reserved</span> <span class="cn">3</span>, <span class="cn">7</span>;<span class="cm">          // numbers can't be reused</span><br>
  <span class="ck">reserved</span> <span class="cv">"old_phone"</span>, <span class="cv">"legacy_id"</span>; <span class="cm">// names can't be reused</span><br>
  <span class="ck">string</span> id    = <span class="cn">1</span>;<br>
  <span class="ck">string</span> email = <span class="cn">2</span>;<br>
  <span class="cm">// field 3 was "username" — reserved above</span><br>
}
</div>
  </div>
</div>
<div class="warn">
  <strong>Proto3 Default Values Trap:</strong> In proto3, every field has a default (0/""/""/false).
  You cannot distinguish "field not set" from "field set to zero." Use <code>google.protobuf.Int32Value</code> wrappers or <code>optional</code> keyword (proto3 optional) when you need a three-state: unset / zero / non-zero.
</div>
</div><!-- /t-proto3 -->
<!-- ── WIRE ENCODING ─────────────────────────────────────────── -->
<div id="t-wire" class="tab-pane">
<div class="cp p-indigo">
  <div class="cp-hdr">🔬 The Wire Format</div>
  <div class="cp-body">
    Protobuf encodes each field as a <strong>key-value pair</strong>.
    The key is a varint combining the field number and wire type: <code>key = (field_number &lt;&lt; 3) | wire_type</code>.
    There are 6 wire types:
<table class="t-table">
  <thead><tr><th>Wire Type</th><th>Meaning</th><th>Used For</th></tr></thead>
  <tbody>
<tr><td>0</td><td>Varint</td><td>int32/64, uint32/64, sint32/64, bool, enum</td></tr>
<tr><td>1</td><td>64-bit</td><td>fixed64, sfixed64, double</td></tr>
<tr><td>2</td><td>Length-delimited</td><td>string, bytes, embedded messages, packed repeated</td></tr>
<tr><td>3</td><td>Start group (deprecated)</td><td>Legacy — do not use</td></tr>
<tr><td>4</td><td>End group (deprecated)</td><td>Legacy — do not use</td></tr>
<tr><td>5</td><td>32-bit</td><td>fixed32, sfixed32, float</td></tr>
  </tbody>
</table>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr">📐 Varint Encoding Step by Step</div>
  <div class="cp-body">
    Varints encode integers using 1–10 bytes. Each byte contributes 7 bits; the MSB is a <em>continuation bit</em> (1 = more bytes follow, 0 = last byte).
<div class="cb">
<span class="cm">// Encoding the integer 300 as a varint:</span><br>
<span class="cm">//  300 in binary = 0000 0001 0010 1100</span><br>
<span class="cm">//  Split into 7-bit groups (LSB first): 010 1100 | 000 0010</span><br>
<span class="cm">//  Add continuation bits:              1010 1100 | 0000 0010</span><br>
<span class="cm">//  Result bytes: 0xAC 0x02</span><br>
<br>
<span class="cm">// Encoding field_number=1, wire_type=0, value=150:</span><br>
<span class="cm">//  key = (1 << 3) | 0 = 0x08</span><br>
<span class="cm">//  value 150 = 0x96 0x01</span><br>
<span class="cm">//  Wire bytes: 08 96 01</span><br>
<br>
<span class="ck">uint8_t</span>* encode_varint(<span class="ck">uint8_t</span> *buf, <span class="ck">uint64_t</span> v) {<br>
  <span class="ck">while</span> (v > <span class="cn">0x7F</span>) {<br>
    *buf++ = (<span class="ck">uint8_t</span>)(v | <span class="cn">0x80</span>);  <span class="cm">// set MSB = more bytes</span><br>
    v >>= <span class="cn">7</span>;<br>
  }<br>
  *buf++ = (<span class="ck">uint8_t</span>)v;            <span class="cm">// last byte, MSB clear</span><br>
  <span class="ck">return</span> buf;<br>
}<br>
<br>
<span class="ck">const</span> <span class="ck">uint8_t</span>* decode_varint(<span class="ck">const</span> <span class="ck">uint8_t</span> *buf, <span class="ck">uint64_t</span> *out) {<br>
  <span class="ck">uint64_t</span> result = <span class="cn">0</span>;<br>
  <span class="ck">int</span> shift = <span class="cn">0</span>;<br>
  <span class="ck">do</span> {<br>
<span class="ck">if</span> (shift >= <span class="cn">64</span>) <span class="ck">return</span> <span class="cv">NULL</span>;  <span class="cm">// malformed</span><br>
    result |= (<span class="ck">uint64_t</span>)(*buf &amp; <span class="cn">0x7F</span>) &lt;&lt; shift;<br>
    shift += <span class="cn">7</span>;<br>
  } <span class="ck">while</span> (*buf++ &amp; <span class="cn">0x80</span>);<br>
  *out = result;<br>
  <span class="ck">return</span> buf;<br>
}
</div>
  </div>
</div>
<div class="cp p-indigo">
  <div class="cp-hdr">🔄 ZigZag Encoding (sint32/sint64)</div>
  <div class="cp-body">
    Normal varint encoding of −1 uses 10 bytes (it's treated as a large unsigned number 2⁶⁴−1).
    ZigZag maps signed ints to unsigned: positive n → 2n, negative n → 2|n|−1.
    This means small negative numbers also get small varint encodings.
<div class="cb">
<span class="cm">// ZigZag encode: (n << 1) ^ (n >> 31) for int32</span><br>
<span class="cm">//  0  → 0      -1  → 1       1  → 2</span><br>
<span class="cm">//  -2 → 3       2  → 4      -3 → 5</span><br>
<br>
<span class="ck">uint32_t</span> zigzag_encode32(<span class="ck">int32_t</span> n) {<br>
  <span class="ck">return</span> ((uint32_t)n &lt;&lt; <span class="cn">1</span>) ^ ((uint32_t)(n >> <span class="cn">31</span>));<br>
}<br>
<span class="ck">int32_t</span> zigzag_decode32(<span class="ck">uint32_t</span> n) {<br>
  <span class="ck">return</span> (<span class="ck">int32_t</span>)((n >> <span class="cn">1</span>) ^ -(n &amp; <span class="cn">1</span>));<br>
}
</div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr">📦 Length-Delimited Encoding (strings, bytes, nested messages)</div>
  <div class="cp-body">
<div class="cb">
<span class="cm">// Field number=2 (string "hi"), wire type=2:</span><br>
<span class="cm">// key = (2 << 3) | 2 = 0x12</span><br>
<span class="cm">// length varint = 0x02</span><br>
<span class="cm">// data bytes = 0x68 0x69 ('h', 'i')</span><br>
<span class="cm">// Wire bytes: 12 02 68 69</span><br>
<br>
<span class="cm">// Nested message: serialise inner message, prefix its byte length</span><br>
<span class="cm">// User { id="abc", email="x@y.com" } encoded then embedded in:</span><br>
<span class="cm">// GetUserResponse { user=&lt;User bytes&gt; }</span><br>
<br>
<span class="cm">// Packed repeated fields (default in proto3 for numeric types):</span><br>
<span class="cm">// [1, 2, 3] as repeated int32 field_number=4:</span><br>
<span class="cm">//  key = (4<<3)|2 = 0x22  (wire type 2, not 0!)</span><br>
<span class="cm">//  length = 3 bytes</span><br>
<span class="cm">//  data: 01 02 03  (three varints packed together)</span>
</div>
  </div>
</div>
<div class="note">
  <strong>Why know the wire format?</strong> Debugging gRPC in Wireshark, writing custom serialisers (e.g., embedded firmware without a Protobuf runtime), optimising field ordering for cache locality, or implementing partial-decode ("field 5 only") for read amplification reduction.
</div>
</div><!-- /t-wire -->
<!-- ── STREAMING MODES ────────────────────────────────────────── -->
<div id="t-streaming" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr">📡 The 4 Streaming Patterns</div>
  <div class="cp-body">
    Every gRPC RPC is fundamentally a function: request → response. The streaming variants replace one or both sides with an <em>ordered sequence</em> of messages over the same HTTP/2 stream.
  </div>
</div>
<ol class="flow-list">
  <li class="fl-step"><span class="fl-num">1</span><div><strong>Unary RPC</strong> — <code>rpc GetUser(Request) returns (Response)</code><br>One request, one response. Equivalent to a REST POST. Client sends request frame → server processes → server sends response + TRAILERS. Simplest; 99% of internal APIs start here.</div></li>
  <li class="fl-step"><span class="fl-num">2</span><div><strong>Server Streaming</strong> — <code>rpc WatchPrices(Symbol) returns (stream Tick)</code><br>Client sends one message; server sends N messages then closes. Ideal for live feeds, log tailing, paginated results without cursor round-trips. HTTP/2 DATA frames keep arriving until FIN.</div></li>
  <li class="fl-step"><span class="fl-num">3</span><div><strong>Client Streaming</strong> — <code>rpc UploadChunks(stream Chunk) returns (Summary)</code><br>Client sends N messages, server responds once at the end. For bulk ingestion (file upload, sensor telemetry). Server buffers or processes incrementally, replies after client sends EOF.</div></li>
  <li class="fl-step"><span class="fl-num">4</span><div><strong>Bidirectional Streaming</strong> — <code>rpc Chat(stream Msg) returns (stream Msg)</code><br>Both sides send independently. Order within each side is preserved; the two streams interleave freely. Real-time collaboration, game state sync, interactive ML inference pipelines.</div></li>
</ol>
<div class="diagram-box">
<span class="dg-gray">Mode              Client →              Server →</span>
<span class="dg-gray">─────────────────────────────────────────────────────────────</span>
<span class="dg-blue">Unary           ──[Req]──────────→    ←──[Res]──────────</span>
<span class="dg-indigo">Server stream   ──[Req]──────────→    ←──[Res1][Res2]...[END]</span>
<span class="dg-green">Client stream   ──[Req1][Req2]...[END]→ ←──[Res]──────────</span>
<span class="dg-amber">Bidirectional   ──[R1][R2][R3]...[END]→ ←──[S1][S2]...[END]</span>
<span class="dg-gray">                Both sides independent; order within side preserved</span>
</div>
<div class="cp p-indigo">
  <div class="cp-hdr">⚙️ HTTP/2 Mechanics Under the Hood</div>
  <div class="cp-body">
    Each gRPC call maps to one HTTP/2 stream (unique stream ID). The request uses:
<ul>
<li><strong>HEADERS frame</strong> — <code>:method POST</code>, <code>:path /pkg.Service/Method</code>, <code>content-type: application/grpc</code>, <code>grpc-timeout</code>, custom metadata as headers</li>
<li><strong>DATA frames</strong> — 5-byte length-prefix + Protobuf bytes. First byte is compression flag (0=none, 1=compressed); next 4 bytes are message length big-endian.</li>
<li><strong>TRAILERS (HTTP/2 HEADERS with END_STREAM)</strong> — <code>grpc-status</code> (int) + <code>grpc-message</code> (percent-encoded string) + optional <code>grpc-status-details-bin</code></li>
</ul>
<div class="cb">
<span class="cm">/* gRPC length-prefix framing — hand-decode a DATA payload */</span><br>
<span class="ck">typedef struct</span> {<br>
  <span class="ck">uint8_t</span>  compressed;   <span class="cm">// 0 = none, 1 = gzip/deflate/snappy</span><br>
  <span class="ck">uint32_t</span> length;       <span class="cm">// big-endian message length</span><br>
  <span class="ck">uint8_t</span> *data;         <span class="cm">// Protobuf bytes (length bytes)</span><br>
} grpc_frame_t;<br>
<br>
<span class="ck">int</span> grpc_decode_frame(<span class="ck">const</span> <span class="ck">uint8_t</span> *buf, <span class="ck">size_t</span> buflen,<br>
                      grpc_frame_t *out) {<br>
  <span class="ck">if</span> (buflen &lt; <span class="cn">5</span>) <span class="ck">return</span> -<span class="cn">1</span>;<br>
  out->compressed = buf[<span class="cn">0</span>];<br>
  out->length     = ((uint32_t)buf[<span class="cn">1</span>] &lt;&lt; <span class="cn">24</span>) |<br>
                    ((uint32_t)buf[<span class="cn">2</span>] &lt;&lt; <span class="cn">16</span>) |<br>
                    ((uint32_t)buf[<span class="cn">3</span>] &lt;&lt;  <span class="cn">8</span>) |<br>
                     (uint32_t)buf[<span class="cn">4</span>];<br>
  <span class="ck">if</span> (buflen &lt; <span class="cn">5</span> + out->length) <span class="ck">return</span> -<span class="cn">2</span>;<br>
  out->data = (<span class="ck">uint8_t</span>*)&amp;buf[<span class="cn">5</span>];<br>
  <span class="ck">return</span> <span class="cn">0</span>;<br>
}
</div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr">⏱ Deadlines &amp; Cancellation</div>
  <div class="cp-body">
    gRPC propagates deadlines automatically. The client sets <code>grpc-timeout</code> in the HEADERS frame; every hop decrements the remaining budget. If the deadline expires mid-stream:
<ul>
<li>Client sends RST_STREAM with error code CANCEL</li>
<li>Server receives context cancellation; I/O operations return error</li>
<li>All open streams on the RPC are torn down</li>
</ul>
    This enables <strong>deadline propagation</strong>: a 200 ms end-to-end budget shrinks as it passes through each service, preventing cascading timeouts where upstream services pile up waiting for a dead downstream.
<div class="cb">
<span class="cm">// gRPC timeout header format: ASCII integer + unit suffix</span><br>
<span class="cm">// grpc-timeout: 200m     → 200 milliseconds</span><br>
<span class="cm">// grpc-timeout: 5S       → 5 seconds</span><br>
<span class="cm">// grpc-timeout: 100000u  → 100 ms in microseconds</span><br>
<span class="cm">// Units: H(hours) M(minutes) S(seconds) m(ms) u(µs) n(ns)</span>
</div>
  </div>
</div>
</div><!-- /t-streaming -->
<!-- ── ERRORS & INTERCEPTORS ──────────────────────────────────── -->
<div id="t-errors" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr">🚨 gRPC Status Codes</div>
  <div class="cp-body">
    gRPC defines 16 canonical status codes transmitted in the <code>grpc-status</code> trailer.
    Map HTTP status codes to gRPC equivalents when building gRPC-Gateway or REST bridges.
<table class="t-table">
  <thead><tr><th>Code</th><th>Name</th><th>HTTP ≈</th><th>When to Use</th></tr></thead>
  <tbody>
<tr><td>0</td><td>OK</td><td>200</td><td>Success</td></tr>
<tr><td>1</td><td>CANCELLED</td><td>499</td><td>Client cancelled (RST_STREAM)</td></tr>
<tr><td>2</td><td>UNKNOWN</td><td>500</td><td>Unknown server error</td></tr>
<tr><td>3</td><td>INVALID_ARGUMENT</td><td>400</td><td>Bad request field values</td></tr>
<tr><td>4</td><td>DEADLINE_EXCEEDED</td><td>504</td><td>Timeout expired</td></tr>
<tr><td>5</td><td>NOT_FOUND</td><td>404</td><td>Resource not found</td></tr>
<tr><td>6</td><td>ALREADY_EXISTS</td><td>409</td><td>Create of existing resource</td></tr>
<tr><td>7</td><td>PERMISSION_DENIED</td><td>403</td><td>Authenticated but not authorised</td></tr>
<tr><td>8</td><td>RESOURCE_EXHAUSTED</td><td>429</td><td>Quota / rate limit exceeded</td></tr>
<tr><td>9</td><td>FAILED_PRECONDITION</td><td>400</td><td>Precondition not met (e.g., non-empty bucket before delete)</td></tr>
<tr><td>10</td><td>ABORTED</td><td>409</td><td>Concurrency conflict (optimistic lock failed)</td></tr>
<tr><td>11</td><td>OUT_OF_RANGE</td><td>400</td><td>Value out of valid range (e.g., seek past end)</td></tr>
<tr><td>12</td><td>UNIMPLEMENTED</td><td>501</td><td>Method not implemented</td></tr>
<tr><td>13</td><td>INTERNAL</td><td>500</td><td>Internal invariant broken</td></tr>
<tr><td>14</td><td>UNAVAILABLE</td><td>503</td><td>Server temporarily unavailable — safe to retry</td></tr>
<tr><td>15</td><td>DATA_LOSS</td><td>500</td><td>Unrecoverable data corruption</td></tr>
<tr><td>16</td><td>UNAUTHENTICATED</td><td>401</td><td>Missing / invalid credentials</td></tr>
  </tbody>
</table>
  </div>
</div>
<div class="cp p-indigo">
  <div class="cp-hdr">📋 Rich Error Details (<code>google.rpc.Status</code>)</div>
  <div class="cp-body">
    A bare status code is not enough for clients to act. The <code>google.rpc.Status</code> proto embeds structured error payloads in the <code>grpc-status-details-bin</code> trailer (base64-encoded).
<div class="cb">
<span class="cm">// google/rpc/status.proto (simplified)</span><br>
<span class="ck">message</span> <span class="cf">Status</span> {<br>
  <span class="ck">int32</span>  code    = <span class="cn">1</span>;<span class="cm">      // gRPC status code integer</span><br>
  <span class="ck">string</span> message = <span class="cn">2</span>;<span class="cm">    // Human-readable, not for machines</span><br>
  <span class="ck">repeated</span> google.protobuf.<span class="cf">Any</span> details = <span class="cn">3</span>;<br>
}<br>
<br>
<span class="cm">// Common detail types (google/rpc/error_details.proto):</span><br>
<span class="cm">//  ErrorInfo       — domain + reason + metadata</span><br>
<span class="cm">//  RetryInfo       — retry_delay (client should wait before retry)</span><br>
<span class="cm">//  BadRequest      — list of field violations</span><br>
<span class="cm">//  QuotaFailure    — which quota was exceeded</span><br>
<span class="cm">//  RequestInfo     — request_id for correlation</span><br>
<br>
<span class="cm">// Example: INVALID_ARGUMENT with field violations (Go pseudocode)</span><br>
<span class="cm">// st, _ := status.New(codes.InvalidArgument, "validation failed")</span><br>
<span class="cm">// br := &errdetails.BadRequest{}</span><br>
<span class="cm">// br.FieldViolations = append(br.FieldViolations,</span><br>
<span class="cm">//   &errdetails.BadRequest_FieldViolation{</span><br>
<span class="cm">//     Field: "email", Description: "must be valid RFC 5321 address"})</span><br>
<span class="cm">// st.WithDetails(br)</span>
</div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr">🔗 Interceptors (Middleware)</div>
  <div class="cp-body">
    Interceptors wrap RPC handler calls — analogous to HTTP middleware. They run for every RPC on that connection.
    Typical uses: auth token validation, request logging, tracing span injection, rate limiting, retry logic, metrics counters.
<div class="diagram-box">
<span class="dg-blue">Client side:   [Retry] → [Auth token inject] → [Logging] → [Codec] → network</span>
<span class="dg-indigo">Server side:   network → [Auth validator] → [Rate limiter] → [Logging] → [Handler]</span>
</div>
<div class="cb">
<span class="cm">/* Conceptual unary interceptor signature (language-agnostic) */</span><br>
<span class="cm">// invoke(ctx, request, method_info, handler) → (response, error)</span><br>
<br>
<span class="cm">// Server unary interceptor: JWT auth check (pseudocode)</span><br>
<span class="ck">func</span> AuthInterceptor(ctx, req, info, handler) (resp, err) {<br>
  token := metadata.FromIncomingContext(ctx)[<span class="cv">"authorization"</span>]<br>
  <span class="ck">if</span> !validate_jwt(token) {<br>
<span class="ck">return</span> nil, status.Error(UNAUTHENTICATED, <span class="cv">"invalid token"</span>)<br>
  }<br>
  <span class="ck">return</span> handler(ctx_with_claims, req)<span class="cm">// pass enriched context</span><br>
}<br>
<br>
<span class="cm">// Chain multiple interceptors:</span><br>
<span class="cm">// grpc.ChainUnaryInterceptor(LoggingInterceptor, AuthInterceptor, RateLimitInterceptor)</span>
</div>
  </div>
</div>
<div class="cp p-indigo">
  <div class="cp-hdr">🔄 Retry Policy</div>
  <div class="cp-body">
    gRPC supports automatic client-side retries defined in service config JSON (passed during channel creation or via xDS).
    Only <strong>UNAVAILABLE</strong> and <strong>RESOURCE_EXHAUSTED</strong> (with retry hint) are safe to retry transparently.
<div class="cb">
<span class="cm">// Service config JSON snippet for retry policy:</span><br>
{<br>
  <span class="cv">"methodConfig"</span>: [{<br>
<span class="cv">"name"</span>: [{ <span class="cv">"service"</span>: <span class="cv">"user.v1.UserService"</span>, <span class="cv">"method"</span>: <span class="cv">"GetUser"</span> }],<br>
<span class="cv">"retryPolicy"</span>: {<br>
<span class="cv">"maxAttempts"</span>: <span class="cn">4</span>,<br>
<span class="cv">"initialBackoff"</span>: <span class="cv">"0.1s"</span>,<br>
<span class="cv">"maxBackoff"</span>: <span class="cv">"1s"</span>,<br>
<span class="cv">"backoffMultiplier"</span>: <span class="cn">2</span>,<br>
<span class="cv">"retryableStatusCodes"</span>: [<span class="cv">"UNAVAILABLE"</span>]<br>
    }<br>
  }]<br>
}
</div>
  </div>
</div>
<div class="warn">
  <strong>Idempotency &amp; Retries:</strong> Only retry RPCs that are idempotent (GET-like unary reads, or marked with the idempotency annotation). Retrying a <code>CreateOrder</code> can result in duplicate orders. Use <code>retry_push_back</code> from <code>RetryInfo</code> for server-directed backoff on RESOURCE_EXHAUSTED.
</div>
</div><!-- /t-errors -->
<!-- ── gRPC-GATEWAY ───────────────────────────────────────────── -->
<div id="t-gateway" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr">🌐 gRPC-Gateway: Serve REST + gRPC from One Proto</div>
  <div class="cp-body">
    gRPC-Gateway is a <code>protoc</code> plugin that generates a reverse proxy.
    It reads HTTP annotations in your <code>.proto</code> file and transcodes REST/JSON requests to gRPC, forwarding them to the gRPC server.
    One service definition, two surfaces: gRPC for internal services, REST/JSON for browsers and third-party consumers.
  </div>
</div>
<div class="diagram-box">
<span class="dg-gray">Browser / curl                   gRPC-Gateway Proxy              gRPC Server</span>
<span class="dg-gray">─────────────────────────────────────────────────────────────────────────────</span>
<span class="dg-blue">HTTP GET /v1/users/42  ──────→  Transcode to GetUserRequest  ──────→ Handler</span>
<span class="dg-blue">                               (JSON → Protobuf)                    (C/Go/Java)</span>
<span class="dg-indigo">HTTP 200 {"id":"42"…}  ←──────  Transcode response            ←──────</span>
<span class="dg-indigo">                               (Protobuf → JSON)                    </span>
<span class="dg-green">grpc://svc:50051       ──────────────────────────────────────→      (direct)</span>
</div>
<div class="cp p-indigo">
  <div class="cp-hdr">✏️ HTTP Annotations in Proto</div>
  <div class="cp-body">
<div class="cb">
<span class="ck">import</span> <span class="cv">"google/api/annotations.proto"</span>;<br>
<br>
<span class="ck">service</span> <span class="cf">UserService</span> {<br>
  <span class="ck">rpc</span> GetUser (<span class="cf">GetUserRequest</span>) <span class="ck">returns</span> (<span class="cf">User</span>) {<br>
<span class="ck">option</span> (google.api.http) = {<br>
      get: <span class="cv">"/v1/users/{user_id}"</span>      <span class="cm">// user_id binds from path</span><br>
    };<br>
  }<br>
  <span class="ck">rpc</span> CreateUser (<span class="cf">User</span>) <span class="ck">returns</span> (<span class="cf">User</span>) {<br>
<span class="ck">option</span> (google.api.http) = {<br>
      post: <span class="cv">"/v1/users"</span><br>
      body: <span class="cv">"*"</span>                      <span class="cm">// entire JSON body maps to User</span><br>
    };<br>
  }<br>
  <span class="ck">rpc</span> ListUsers (<span class="cf">ListUsersRequest</span>) <span class="ck">returns</span> (<span class="cf">ListUsersResponse</span>) {<br>
<span class="ck">option</span> (google.api.http) = {<br>
      get: <span class="cv">"/v1/users"</span>               <span class="cm">// page_size, page_token become query params</span><br>
    };<br>
  }<br>
  <span class="ck">rpc</span> UpdateUser (<span class="cf">UpdateUserRequest</span>) <span class="ck">returns</span> (<span class="cf">User</span>) {<br>
<span class="ck">option</span> (google.api.http) = {<br>
      patch: <span class="cv">"/v1/users/{user.id}"</span><br>
      body: <span class="cv">"user"</span>                  <span class="cm">// only "user" sub-message from body</span><br>
    };<br>
  }<br>
}
</div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr">💊 gRPC Health Checking Protocol</div>
  <div class="cp-body">
    The standard gRPC health check service lets Kubernetes liveness/readiness probes and load balancers check service health without custom endpoints.
<div class="cb">
<span class="cm">// grpc/health/v1/health.proto (standard)</span><br>
<span class="ck">service</span> <span class="cf">Health</span> {<br>
  <span class="ck">rpc</span> Check (<span class="cf">HealthCheckRequest</span>) <span class="ck">returns</span> (<span class="cf">HealthCheckResponse</span>);<br>
  <span class="ck">rpc</span> Watch (<span class="cf">HealthCheckRequest</span>) <span class="ck">returns</span> (<span class="ck">stream</span> <span class="cf">HealthCheckResponse</span>);<br>
}<br>
<span class="ck">message</span> <span class="cf">HealthCheckRequest</span>  { <span class="ck">string</span> service = <span class="cn">1</span>; }<br>
<span class="ck">message</span> <span class="cf">HealthCheckResponse</span> {<br>
  <span class="ck">enum</span> <span class="cf">ServingStatus</span> {<br>
    UNKNOWN     = <span class="cn">0</span>;<br>
    SERVING     = <span class="cn">1</span>;<br>
    NOT_SERVING = <span class="cn">2</span>;<br>
    SERVICE_UNKNOWN = <span class="cn">3</span>; <span class="cm">// health-check for unknown service name</span><br>
  }<br>
  <span class="cf">ServingStatus</span> status = <span class="cn">1</span>;<br>
}<br>
<br>
<span class="cm">// Kubernetes grpc probe (k8s 1.24+):</span><br>
<span class="cm">// livenessProbe:</span><br>
<span class="cm">//   grpc:</span><br>
<span class="cm">//     port: 50051</span><br>
<span class="cm">//     service: "user.v1.UserService"</span>
</div>
  </div>
</div>
<div class="cp p-indigo">
  <div class="cp-hdr">🔍 gRPC Reflection</div>
  <div class="cp-body">
    Server reflection allows clients to query the available services and their proto schemas at runtime — without a .proto file.
    Tools like <code>grpcurl</code> and Postman use reflection to discover and call services dynamically.
<div class="cb">
<span class="cm"># grpcurl: REST-like tool for gRPC</span><br>
<span class="cm"># List services (reflection required):</span><br>
grpcurl -plaintext localhost:<span class="cn">50051</span> list<br>
<span class="cm"># → user.v1.UserService</span><br>
<span class="cm"># → grpc.health.v1.Health</span><br>
<br>
<span class="cm"># Describe a method:</span><br>
grpcurl -plaintext localhost:<span class="cn">50051</span> describe user.v1.UserService.GetUser<br>
<br>
<span class="cm"># Call with JSON input:</span><br>
grpcurl -plaintext -d <span class="cv">'{"user_id": "42"}'</span> \<br>
  localhost:<span class="cn">50051</span> user.v1.UserService/GetUser
</div>
  </div>
</div>
</div><!-- /t-gateway -->
<!-- ── C IMPLEMENTATION ───────────────────────────────────────── -->
<div id="t-c-impl" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr">🔧 protobuf-c: Using Protocol Buffers in C</div>
  <div class="cp-body">
<code>protobuf-c</code> is the official C runtime for Protobuf. The <code>protoc-gen-c</code> plugin generates a <code>.pb-c.h</code> / <code>.pb-c.c</code> pair from each <code>.proto</code> file.
<div class="cb">
<span class="cm">/* Install: sudo apt install libprotobuf-c-dev protobuf-c-compiler */</span><br>
<span class="cm">/* Generate: protoc --c_out=. user.proto */</span><br>
<span class="cm">/* Generated files: user.pb-c.h, user.pb-c.c */</span><br>
<br>
<span class="cm">/* Compile: gcc -o demo demo.c user.pb-c.c -lprotobuf-c */</span>
</div>
  </div>
</div>
<div class="cp p-indigo">
  <div class="cp-hdr">📝 Encode / Decode a Message in C (protobuf-c)</div>
  <div class="cp-body">
<div class="cb">
<span class="ck">#include</span> <span class="cs">&lt;stdio.h&gt;</span><br>
<span class="ck">#include</span> <span class="cs">&lt;stdlib.h&gt;</span><br>
<span class="ck">#include</span> <span class="cs">"user.pb-c.h"</span>   <span class="cm">// generated from user.proto</span><br>
<br>
<span class="ck">int</span> main(<span class="ck">void</span>) {<br>
  <span class="cm">/* ── Encode ─────────────────────────────────────────── */</span><br>
  UserV1__User user;<br>
  user__v1__user__init(&amp;user);       <span class="cm">// zero-init with defaults</span><br>
  user.id       = <span class="cv">"42"</span>;<br>
  user.email    = <span class="cv">"alice@example.com"</span>;<br>
  user.username = <span class="cv">"alice"</span>;<br>
  user.role     = USER_V1__ROLE__ROLE_ADMIN;<br>
<br>
  <span class="ck">size_t</span> packed_size = user__v1__user__get_packed_size(&amp;user);<br>
  <span class="ck">uint8_t</span> *buf = malloc(packed_size);<br>
  user__v1__user__pack(&amp;user, buf);<br>
<br>
  printf(<span class="cv">"Packed %zu bytes\n"</span>, packed_size);<br>
<br>
  <span class="cm">/* ── Decode ─────────────────────────────────────────── */</span><br>
  UserV1__User *decoded =<br>
      user__v1__user__unpack(<span class="cv">NULL</span>, packed_size, buf);<br>
  <span class="ck">if</span> (!decoded) {<br>
    fprintf(stderr, <span class="cv">"decode failed\n"</span>);<br>
    free(buf); <span class="ck">return</span> <span class="cn">1</span>;<br>
  }<br>
<br>
  printf(<span class="cv">"id=%s email=%s role=%d\n"</span>,<br>
         decoded->id, decoded->email, decoded->role);<br>
<br>
  user__v1__user__free_unpacked(decoded, <span class="cv">NULL</span>);<br>
  free(buf);<br>
  <span class="ck">return</span> <span class="cn">0</span>;<br>
}
</div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr">🚀 Minimal gRPC Unary Server in C (grpc-c core)</div>
  <div class="cp-body">
<div class="cb">
<span class="cm">/* grpc_server.c — unary GetUser over gRPC */</span><br>
<span class="ck">#include</span> <span class="cs">&lt;grpc/grpc.h&gt;</span><br>
<span class="ck">#include</span> <span class="cs">&lt;grpc/support/log.h&gt;</span><br>
<span class="ck">#include</span> <span class="cs">"user.pb-c.h"</span><br>
<span class="ck">#include</span> <span class="cs">&lt;string.h&gt;</span><br>
<br>
<span class="ck">static void</span> run_server(<span class="ck">const char</span> *addr) {<br>
  grpc_init();<br>
  grpc_server          *server = grpc_server_create(<span class="cv">NULL</span>, <span class="cv">NULL</span>);<br>
  grpc_completion_queue *cq    = grpc_completion_queue_create_for_next(<span class="cv">NULL</span>);<br>
  grpc_server_register_completion_queue(server, cq, <span class="cv">NULL</span>);<br>
<br>
  grpc_server_credentials *creds = grpc_insecure_server_credentials_create();<br>
  grpc_server_add_http2_port(server, addr, creds);<br>
  grpc_server_credentials_release(creds);<br>
  grpc_server_start(server);<br>
  gpr_log(GPR_INFO, <span class="cv">"gRPC server listening on %s"</span>, addr);<br>
<br>
  <span class="cm">/* ── Event loop ────────────────────────────────────── */</span><br>
  <span class="ck">while</span> (<span class="cn">1</span>) {<br>
    grpc_call           *call;<br>
    grpc_call_details    details;<br>
    grpc_metadata_array  req_meta;<br>
    grpc_call_details_init(&amp;details);<br>
    grpc_metadata_array_init(&amp;req_meta);<br>
<br>
<span class="cm">/* request the next incoming call */</span><br>
    grpc_server_request_call(server, &amp;call, &amp;details, &amp;req_meta, cq, cq, (<span class="ck">void</span>*)<span class="cn">1</span>);<br>
    grpc_event ev = grpc_completion_queue_next(<br>
        cq, gpr_inf_future(GPR_CLOCK_REALTIME), <span class="cv">NULL</span>);<br>
<span class="ck">if</span> (ev.type != GRPC_OP_COMPLETE) <span class="ck">continue</span>;<br>
<br>
    gpr_log(GPR_INFO, <span class="cv">"RPC: %s"</span>, grpc_slice_to_c_string(details.method));<br>
<br>
<span class="cm">/* receive request message */</span><br>
    grpc_byte_buffer *recv_buf = <span class="cv">NULL</span>;<br>
    grpc_op recv_ops[<span class="cn">1</span>] = {{<br>
      .op = GRPC_OP_RECV_MESSAGE, .data.recv_message.recv_message = &amp;recv_buf<br>
    }};<br>
    grpc_call_start_batch(call, recv_ops, <span class="cn">1</span>, (<span class="ck">void</span>*)<span class="cn">2</span>, <span class="cv">NULL</span>);<br>
    grpc_completion_queue_next(cq, gpr_inf_future(GPR_CLOCK_REALTIME), <span class="cv">NULL</span>);<br>
<br>
<span class="cm">/* decode request protobuf */</span><br>
    grpc_byte_buffer_reader rdr;<br>
    grpc_byte_buffer_reader_init(&amp;rdr, recv_buf);<br>
    grpc_slice req_slice = grpc_byte_buffer_reader_readall(&amp;rdr);<br>
    UserV1__GetUserRequest *req = user__v1__get_user_request__unpack(<br>
<span class="cv">NULL</span>, GRPC_SLICE_LENGTH(req_slice),<br>
        (<span class="ck">const</span> <span class="ck">uint8_t</span>*)GRPC_SLICE_START_PTR(req_slice));<br>
<br>
<span class="cm">/* build response */</span><br>
    UserV1__User resp;<br>
    user__v1__user__init(&amp;resp);<br>
    resp.id    = req ? req->user_id : <span class="cv">"unknown"</span>;<br>
    resp.email = <span class="cv">"alice@example.com"</span>;<br>
<br>
<span class="ck">size_t</span> resp_len = user__v1__user__get_packed_size(&amp;resp);<br>
<span class="ck">uint8_t</span> *resp_buf = malloc(resp_len);<br>
    user__v1__user__pack(&amp;resp, resp_buf);<br>
<br>
<span class="cm">/* gRPC length-prefix framing: 1 byte flag + 4 bytes length */</span><br>
<span class="ck">uint8_t</span> frame_hdr[<span class="cn">5</span>] = {<span class="cn">0</span>};<br>
    frame_hdr[<span class="cn">1</span>] = (resp_len >> <span class="cn">24</span>) &amp; <span class="cn">0xFF</span>;<br>
    frame_hdr[<span class="cn">2</span>] = (resp_len >> <span class="cn">16</span>) &amp; <span class="cn">0xFF</span>;<br>
    frame_hdr[<span class="cn">3</span>] = (resp_len >>  <span class="cn">8</span>) &amp; <span class="cn">0xFF</span>;<br>
    frame_hdr[<span class="cn">4</span>] = (resp_len      ) &amp; <span class="cn">0xFF</span>;<br>
<br>
    grpc_slice slices[<span class="cn">2</span>] = {<br>
        grpc_slice_from_copied_buffer((<span class="ck">char</span>*)frame_hdr, <span class="cn">5</span>),<br>
        grpc_slice_from_copied_buffer((<span class="ck">char</span>*)resp_buf, resp_len)<br>
    };<br>
    grpc_byte_buffer *send_buf = grpc_raw_byte_buffer_create(slices, <span class="cn">2</span>);<br>
<br>
<span class="cm">/* send response + trailers */</span><br>
    grpc_metadata trailing_meta[<span class="cn">1</span>];<br>
    memset(trailing_meta, <span class="cn">0</span>, <span class="ck">sizeof</span>(trailing_meta));<br>
    grpc_op send_ops[<span class="cn">3</span>] = {<br>
      {.op = GRPC_OP_SEND_INITIAL_METADATA, .data.send_initial_metadata = {<span class="cn">0</span>, <span class="cv">NULL</span>}},<br>
      {.op = GRPC_OP_SEND_MESSAGE,          .data.send_message.send_message = send_buf},<br>
      {.op = GRPC_OP_SEND_STATUS_FROM_SERVER, .data.send_status_from_server = {<br>
          .trailing_metadata_count = <span class="cn">0</span>,<br>
          .status = GRPC_STATUS_OK,<br>
          .status_details = &amp;grpc_empty_slice()<br>
      }},<br>
    };<br>
    grpc_call_start_batch(call, send_ops, <span class="cn">3</span>, (<span class="ck">void</span>*)<span class="cn">3</span>, <span class="cv">NULL</span>);<br>
    grpc_completion_queue_next(cq, gpr_inf_future(GPR_CLOCK_REALTIME), <span class="cv">NULL</span>);<br>
<br>
<span class="cm">/* cleanup */</span><br>
    free(resp_buf);<br>
    if (req) user__v1__get_user_request__free_unpacked(req, <span class="cv">NULL</span>);<br>
    grpc_byte_buffer_destroy(recv_buf);<br>
    grpc_byte_buffer_destroy(send_buf);<br>
    grpc_call_unref(call);<br>
  }<br>
}
</div>
  </div>
</div>
<div class="note">
  In production C services, use the higher-level <code>grpc-c</code> wrapper or switch to C++ with gRPC's C++ API — it handles framing, completion queues, and threading for you. The C core API above is valuable for understanding the protocol mechanics and for embedding gRPC in constrained environments (RTOS, firmware).
</div>
</div><!-- /t-c-impl -->
<!-- ── LABS & CHECKLIST ────────────────────────────────────────── -->
<div id="t-labs" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr">🧪 Lab 1 — Build a Protobuf Serialiser from Scratch</div>
  <div class="lab-body">
    Understand wire encoding at the byte level by writing a minimal varint + length-delimited encoder without using any Protobuf library.
<div class="lab-step"><span class="sn">1</span>Define a simple 3-field message in a <code>.proto</code> file: <code>string name = 1; int32 age = 2; bool active = 3;</code></div>
<div class="lab-step"><span class="sn">2</span>Write <code>encode_varint()</code> and <code>decode_varint()</code> in C (target: handle up to 64-bit values).</div>
<div class="lab-step"><span class="sn">3</span>Write <code>encode_field(field_num, wire_type, value)</code> that emits the key varint followed by the value.</div>
<div class="lab-step"><span class="sn">4</span>Encode a test struct (name="Bob", age=30, active=true) into a byte buffer manually.</div>
<div class="lab-step"><span class="sn">5</span>Cross-verify: use <code>protoc --encode</code> to encode the same values and compare bytes with <code>xxd</code>.</div>
<div class="lab-step"><span class="sn">6</span>Benchmark: encode 1 million structs — hand-coded C vs protobuf-c library. Record ns/op.</div>
<p><strong>Expected outcome:</strong> Your manual encoding matches protobuf-c output byte-for-byte. Performance within 20% of library.</p>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr">🧪 Lab 2 — Bidirectional Streaming Chat Service</div>
  <div class="lab-body">
    Implement a bidirectional streaming gRPC service that simulates a chat session, exercising flow control and concurrent send/receive.
<div class="lab-step"><span class="sn">1</span>Define <code>ChatService</code> with <code>rpc Chat(stream ChatMessage) returns (stream ChatMessage)</code>. Messages: <code>string sender=1; string text=2; int64 timestamp=3;</code></div>
<div class="lab-step"><span class="sn">2</span>Implement a Go (or Python) server that echoes each message back prefixed with "Echo: " after a 50 ms artificial delay.</div>
<div class="lab-step"><span class="sn">3</span>Write a client that sends 100 messages and receives 100 replies, measuring P50/P99 RTT per message.</div>
<div class="lab-step"><span class="sn">4</span>Add server-side deadline enforcement: cancel the stream if the client sends nothing for 5 seconds.</div>
<div class="lab-step"><span class="sn">5</span>Test cancellation: have the client hang after sending 50 messages; verify server receives context cancellation.</div>
<div class="lab-step"><span class="sn">6</span>Add a logging interceptor on the server that prints sender + text length for every message.</div>
<p><strong>Expected outcome:</strong> P99 RTT &lt; 10 ms on localhost. Cancellation visible in server logs within 100 ms of client hang.</p>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr">🧪 Lab 3 — Schema Evolution &amp; gRPC-Gateway</div>
  <div class="lab-body">
    Practice backward-compatible schema evolution and expose your gRPC service as REST using gRPC-Gateway.
<div class="lab-step"><span class="sn">1</span>Start with <code>UserService v1</code>: fields id, email, username (field numbers 1–3).</div>
<div class="lab-step"><span class="sn">2</span>Serialize 100 User objects with v1. Save bytes to disk.</div>
<div class="lab-step"><span class="sn">3</span>Add a new field <code>string department = 4</code> and an enum <code>Role role = 5</code> — creating <code>user_v2.proto</code>.</div>
<div class="lab-step"><span class="sn">4</span>Deserialize the v1 bytes using the v2 schema. Verify: old fields intact, new fields at defaults.</div>
<div class="lab-step"><span class="sn">5</span>Try a breaking change: reuse field number 2 with a different type. Document the corruption you see.</div>
<div class="lab-step"><span class="sn">6</span>Add gRPC-Gateway annotations to <code>GetUser</code> and <code>ListUsers</code>. Run the gateway. Test with <code>curl</code>.</div>
<div class="lab-step"><span class="sn">7</span>Compare JSON payload size vs Protobuf payload size for the same 100-user list.</div>
<p><strong>Expected outcome:</strong> v1→v2 migration is seamless. REST endpoints work with curl. JSON ≈ 3–5× larger than Protobuf.</p>
  </div>
</div>
<div class="sep">— Concept Checklist —</div>
<div class="cp p-blue">
  <div class="cp-hdr">✅ Phase 1 gRPC Mastery Checklist</div>
  <div class="cp-body">
<ul class="cl">
<li>Can write a <code>.proto</code> file with messages, enums, <code>oneof</code>, <code>repeated</code>, and <code>map</code> fields</li>
<li>Explain field number vs field name and why numbers are the stable API contract</li>
<li>Decode a varint by hand: given <code>0xAC 0x02</code>, produce 300</li>
<li>Know all 6 wire types; identify which one <code>string</code> and <code>int32</code> use</li>
<li>Describe ZigZag encoding and when to prefer <code>sint32</code> over <code>int32</code></li>
<li>Implement all 4 streaming modes: unary, server-stream, client-stream, bidirectional</li>
<li>Explain how deadlines propagate through a gRPC call chain</li>
<li>Map gRPC status codes to HTTP equivalents for at least 8 codes</li>
<li>Use <code>google.rpc.Status</code> with rich error details (BadRequest field violations)</li>
<li>Write a server-side unary interceptor for JWT auth validation</li>
<li>Add HTTP annotations to a proto and run gRPC-Gateway transcoding</li>
<li>Implement the gRPC health check protocol; wire it to a Kubernetes liveness probe</li>
<li>List 3 safe and 3 breaking schema changes; always <code>reserved</code> deleted field numbers</li>
<li>Use <code>grpcurl</code> with server reflection to list services and call methods</li>
<li>Encode and decode a Protobuf message using <code>protobuf-c</code> in C</li>
</ul>
  </div>
</div>
<div class="mod-nav">
  <a href="/learning/backend/m03-rest/" class="nb">← M03 REST &amp; API Design</a>
  <a href="/learning/backend/" class="nb">↑ Roadmap</a>
  <a href="/learning/backend/m05-graphql/" class="nb">M05 GraphQL →</a>
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
