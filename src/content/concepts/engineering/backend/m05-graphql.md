---
title: "M05 — GraphQL & API Contracts"
description: "SDL type system, query/mutation/subscription execution, resolver chain, N+1 & DataLoader, cursor pagination, schema federation, persisted queries, and building a GraphQL parser in C."
domain: engineering
track: backend
order: 5
ownHeader: true
url: /learning/backend/m05-graphql/
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
.p-green{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.p-red{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
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
  <h1>M05 — GraphQL &amp; API Contracts</h1>
  <div class="sub">
<span class="phase-tag">Phase 1</span>
    SDL type system · Query / mutation / subscription · Resolver execution model · N+1 &amp; DataLoader · Cursor pagination · Schema federation · Persisted queries · GraphQL parser in C
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt('t-overview',this)">Overview</button>
  <button class="tab-btn" onclick="vt('t-sdl',this)">SDL &amp; Types</button>
  <button class="tab-btn" onclick="vt('t-ops',this)">Queries &amp; Mutations</button>
  <button class="tab-btn" onclick="vt('t-subs',this)">Subscriptions</button>
  <button class="tab-btn" onclick="vt('t-resolver',this)">Resolver Chain</button>
  <button class="tab-btn" onclick="vt('t-pagination',this)">Pagination</button>
  <button class="tab-btn" onclick="vt('t-advanced',this)">Federation &amp; Contracts</button>
  <button class="tab-btn" onclick="vt('t-labs',this)">Labs &amp; Checklist</button>
</div>
<!-- ═══════════════════════════════ OVERVIEW ═══════════════════════════════ -->
<div id="t-overview" class="tab-pane active">
<div class="cp p-blue">
  <div class="cp-hdr">🌐 Why GraphQL?</div>
  <div class="cp-body">
    GraphQL is a <strong>query language for APIs</strong> and a runtime for executing those queries. Clients describe exactly what data they need — the server returns precisely that structure. This eliminates over-fetching (getting more fields than needed) and under-fetching (needing multiple round-trips).
<br><br>
    Conceived at Facebook in 2012, open-sourced in 2015, and now governed by the <strong>GraphQL Foundation</strong>. It sits above your transport (HTTP POST by convention) and serialisation (JSON) layers.
  </div>
</div>
<div class="sep">REST vs GraphQL vs gRPC</div>
<table class="t-table">
  <thead><tr><th>Dimension</th><th>REST</th><th>GraphQL</th><th>gRPC</th></tr></thead>
  <tbody>
<tr><td><strong>Data shape</strong></td><td>Fixed by endpoint</td><td>Client-defined per query</td><td>Fixed by proto message</td></tr>
<tr><td><strong>Transport</strong></td><td>HTTP/1.1 or 2</td><td>HTTP POST (or WebSocket)</td><td>HTTP/2 only</td></tr>
<tr><td><strong>Schema</strong></td><td>OpenAPI (optional)</td><td>SDL (mandatory)</td><td>Proto3 (mandatory)</td></tr>
<tr><td><strong>Versioning</strong></td><td>URL/header</td><td>Schema evolution (deprecated)</td><td>Package + reserved fields</td></tr>
<tr><td><strong>Real-time</strong></td><td>SSE / polling</td><td>Subscriptions over WS</td><td>Server / bidi streaming</td></tr>
<tr><td><strong>Tooling</strong></td><td>Swagger UI, Postman</td><td>GraphiQL, Apollo Studio</td><td>grpcurl, Evans</td></tr>
<tr><td><strong>Over/under-fetch</strong></td><td>Common problem</td><td>Solved by design</td><td>Solved by design</td></tr>
<tr><td><strong>N+1 risk</strong></td><td>Low (batched endpoints)</td><td>High without DataLoader</td><td>Low (explicit streams)</td></tr>
<tr><td><strong>Best for</strong></td><td>Public APIs, CRUD</td><td>Mobile/BFF, many consumers</td><td>Internal microservices</td></tr>
  </tbody>
</table>
<div class="sep">GraphQL Request / Response Lifecycle</div>
<div class="diagram-box">
<span class="dg-gray">Client                  Server Runtime                  Resolvers</span>
<span class="dg-blue">  │                          │                               │</span>
<span class="dg-blue">  │─── HTTP POST /graphql ──▶│</span>
<span class="dg-blue">  │   { query, variables }   │</span>
<span class="dg-blue">  │                          │──── 1. Parse query ──────────│</span>
<span class="dg-blue">  │                          │   (AST Document node)        │</span>
<span class="dg-blue">  │                          │──── 2. Validate ─────────────│</span>
<span class="dg-blue">  │                          │   (against SDL schema)       │</span>
<span class="dg-blue">  │                          │──── 3. Execute ──────────────│</span>
<span class="dg-green">  │                          │        Query.user() ─────────▶ db.findUser(id)</span>
<span class="dg-green">  │                          │        User.posts() ─────────▶ db.postsByUser(id)</span>
<span class="dg-green">  │                          │        Post.author() ────────▶ db.findUser(authorId)</span>
<span class="dg-blue">  │                          │──── 4. Coerce &amp; shape ────────│</span>
<span class="dg-blue">  │◀─── { data, errors } ───│</span>
</div>
<div class="two-col">
<div class="cp p-green">
  <div class="cp-hdr">✅ Use GraphQL when…</div>
  <div class="cp-body">
<ul style="margin:0;padding-left:1.2rem">
<li>Multiple clients (mobile, web, TV) need different shapes</li>
<li>Building a BFF (Backend For Frontend) layer</li>
<li>Rapid product iteration — add fields without breaking old clients</li>
<li>Schema-driven development with strong type contracts</li>
<li>Exposing a public, self-documenting developer API</li>
</ul>
  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr">⚠️ Prefer REST / gRPC when…</div>
  <div class="cp-body">
<ul style="margin:0;padding-left:1.2rem">
<li>Simple CRUD with few consumers</li>
<li>HTTP caching is important (GET semantics)</li>
<li>File uploads are a primary use case</li>
<li>Tight performance budget on edge/embedded devices</li>
<li>Internal microservice calls (prefer gRPC)</li>
</ul>
  </div>
</div>
</div>
</div><!-- /t-overview -->
<!-- ═══════════════════════════════ SDL & TYPES ═══════════════════════════════ -->
<div id="t-sdl" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr">📄 Schema Definition Language (SDL)</div>
  <div class="cp-body">
    The SDL is GraphQL's <strong>Interface Definition Language</strong>. Every field, type, argument, and return value is declared here. The server runtime uses it for validation and execution. Clients use it (via introspection) for type-safe code generation.
  </div>
</div>
<div class="sep">Complete SDL Example — Blog Service</div>
<div class="cb">
<span class="cm"># ── Scalars ──────────────────────────────────────────────────────</span>
<span class="ck">scalar</span> <span class="cv">DateTime</span>   <span class="cm"># ISO-8601 string; validated by custom scalar coercion</span>
<span class="ck">scalar</span> <span class="cv">UUID</span>
<span class="cm"># ── Enums ────────────────────────────────────────────────────────</span>
<span class="ck">enum</span> <span class="cv">PostStatus</span> {
  <span class="co">DRAFT</span>
  <span class="co">PUBLISHED</span>
  <span class="co">ARCHIVED</span>
}

<span class="ck">enum</span> <span class="cv">SortDirection</span> { <span class="co">ASC</span>  <span class="co">DESC</span> }

<span class="cm"># ── Interfaces ───────────────────────────────────────────────────</span>
<span class="ck">interface</span> <span class="cv">Node</span> {
  <span class="cn">id</span>: <span class="cv">ID</span>!
}

<span class="cm"># ── Object types ─────────────────────────────────────────────────</span>
<span class="ck">type</span> <span class="cv">User</span> <span class="ck">implements</span> <span class="cv">Node</span> {
  <span class="cn">id</span>:        <span class="cv">ID</span>!
  <span class="cn">username</span>:  <span class="cv">String</span>!
  <span class="cn">email</span>:     <span class="cv">String</span>!
  <span class="cn">createdAt</span>: <span class="cv">DateTime</span>!
  <span class="cn">posts</span>(<span class="cn">first</span>: <span class="cv">Int</span>, <span class="cn">after</span>: <span class="cv">String</span>): <span class="cv">PostConnection</span>!
}

<span class="ck">type</span> <span class="cv">Post</span> <span class="ck">implements</span> <span class="cv">Node</span> {
  <span class="cn">id</span>:        <span class="cv">ID</span>!
  <span class="cn">title</span>:     <span class="cv">String</span>!
  <span class="cn">body</span>:      <span class="cv">String</span>!
  <span class="cn">status</span>:    <span class="cv">PostStatus</span>!
  <span class="cn">author</span>:    <span class="cv">User</span>!
  <span class="cn">tags</span>:      [<span class="cv">String</span>!]!
  <span class="cn">createdAt</span>: <span class="cv">DateTime</span>!
}

<span class="cm"># ── Connection / Edge (Relay cursor pagination) ───────────────────</span>
<span class="ck">type</span> <span class="cv">PostConnection</span> {
  <span class="cn">edges</span>:    [<span class="cv">PostEdge</span>!]!
  <span class="cn">pageInfo</span>: <span class="cv">PageInfo</span>!
  <span class="cn">totalCount</span>: <span class="cv">Int</span>!
}
<span class="ck">type</span> <span class="cv">PostEdge</span> {
  <span class="cn">node</span>:   <span class="cv">Post</span>!
  <span class="cn">cursor</span>: <span class="cv">String</span>!
}
<span class="ck">type</span> <span class="cv">PageInfo</span> {
  <span class="cn">hasNextPage</span>:     <span class="cv">Boolean</span>!
  <span class="cn">hasPreviousPage</span>: <span class="cv">Boolean</span>!
  <span class="cn">startCursor</span>:     <span class="cv">String</span>
  <span class="cn">endCursor</span>:       <span class="cv">String</span>
}

<span class="cm"># ── Input types (arguments for mutations) ────────────────────────</span>
<span class="ck">input</span> <span class="cv">CreatePostInput</span> {
  <span class="cn">title</span>:  <span class="cv">String</span>!
  <span class="cn">body</span>:   <span class="cv">String</span>!
  <span class="cn">tags</span>:   [<span class="cv">String</span>!]
}

<span class="cm"># ── Union ─────────────────────────────────────────────────────────</span>
<span class="ck">union</span> <span class="cv">SearchResult</span> = <span class="cv">User</span> | <span class="cv">Post</span>
<span class="cm"># ── Root types ────────────────────────────────────────────────────</span>
<span class="ck">type</span> <span class="cv">Query</span> {
  <span class="cn">user</span>(<span class="cn">id</span>: <span class="cv">ID</span>!):              <span class="cv">User</span>
  <span class="cn">posts</span>(<span class="cn">first</span>: <span class="cv">Int</span>, <span class="cn">after</span>: <span class="cv">String</span>, <span class="cn">status</span>: <span class="cv">PostStatus</span>): <span class="cv">PostConnection</span>!
  <span class="cn">search</span>(<span class="cn">query</span>: <span class="cv">String</span>!):      [<span class="cv">SearchResult</span>!]!
}

<span class="ck">type</span> <span class="cv">Mutation</span> {
  <span class="cn">createPost</span>(<span class="cn">input</span>: <span class="cv">CreatePostInput</span>!): <span class="cv">Post</span>!
  <span class="cn">publishPost</span>(<span class="cn">id</span>: <span class="cv">ID</span>!):             <span class="cv">Post</span>!
  <span class="cn">deletePost</span>(<span class="cn">id</span>: <span class="cv">ID</span>!):              <span class="cv">Boolean</span>!
}

<span class="ck">type</span> <span class="cv">Subscription</span> {
  <span class="cn">postPublished</span>: <span class="cv">Post</span>!
  <span class="cn">commentAdded</span>(<span class="cn">postId</span>: <span class="cv">ID</span>!): <span class="cv">Comment</span>!
}
</div>
<div class="sep">Type System Reference</div>
<table class="t-table">
  <thead><tr><th>Construct</th><th>SDL syntax</th><th>Purpose</th><th>Notes</th></tr></thead>
  <tbody>
<tr><td><strong>Scalar</strong></td><td><code>scalar DateTime</code></td><td>Leaf value (no sub-fields)</td><td>Built-in: Int, Float, String, Boolean, ID. Custom scalars need serialize/parse/parseLiteral coercion.</td></tr>
<tr><td><strong>Object type</strong></td><td><code>type User { … }</code></td><td>Named set of fields</td><td>All fields are nullable by default; <code>!</code> makes non-null.</td></tr>
<tr><td><strong>Interface</strong></td><td><code>interface Node { id: ID! }</code></td><td>Abstract type contract</td><td>Types that implement must define all interface fields.</td></tr>
<tr><td><strong>Union</strong></td><td><code>union SearchResult = A | B</code></td><td>One-of type (no shared fields)</td><td>Use <code>__typename</code> or inline fragments (<code>... on User</code>) to distinguish.</td></tr>
<tr><td><strong>Enum</strong></td><td><code>enum Status { DRAFT … }</code></td><td>Fixed set of string values</td><td>Serialized as strings in JSON; validated server-side.</td></tr>
<tr><td><strong>Input type</strong></td><td><code>input CreatePost { … }</code></td><td>Argument objects for mutations</td><td>Cannot contain object types — only scalars, enums, and other input types.</td></tr>
<tr><td><strong>Non-null</strong></td><td><code>String!</code></td><td>Field/arg must not be null</td><td>If resolver returns null, GraphQL propagates null up to nearest nullable parent.</td></tr>
<tr><td><strong>List</strong></td><td><code>[String!]!</code></td><td>Array of values</td><td>Outer <code>!</code> = list not null; inner <code>!</code> = no null elements.</td></tr>
<tr><td><strong>Directive</strong></td><td><code>@deprecated(reason: "…")</code></td><td>Metadata on types/fields</td><td>Built-in: @deprecated, @skip, @include, @specifiedBy. Custom directives extend this.</td></tr>
  </tbody>
</table>
<div class="note">💡 <strong>Non-null propagation rule:</strong> if a non-null field resolver throws or returns null, GraphQL does not return a partial object — it sets the nearest nullable parent to null. This "error bubbling" means you must think carefully about which fields to mark <code>!</code>.</div>
</div><!-- /t-sdl -->
<!-- ═══════════════════════════════ QUERIES & MUTATIONS ═══════════════════════════════ -->
<div id="t-ops" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr">📝 GraphQL Operations</div>
  <div class="cp-body">
    GraphQL defines three root operation types: <strong>query</strong> (read, parallel execution), <strong>mutation</strong> (write, serial execution), and <strong>subscription</strong> (long-lived event stream). Every request document contains one or more named or anonymous operations.
  </div>
</div>
<div class="sep">Query Anatomy</div>
<div class="cb">
<span class="cm"># Named query with variables and fragments</span>
<span class="ck">query</span> <span class="cv">GetUserWithPosts</span>(<span class="cn">$userId</span>: <span class="cv">ID</span>!, <span class="cn">$first</span>: <span class="cv">Int</span> = <span class="cs">10</span>) {
  <span class="cn">user</span>(<span class="cn">id</span>: <span class="cn">$userId</span>) {
    ...<span class="cv">UserCore</span>           <span class="cm"># fragment spread</span>
<span class="cn">posts</span>(<span class="cn">first</span>: <span class="cn">$first</span>) {
<span class="cn">edges</span> {
<span class="cn">node</span> {
<span class="cn">id</span>
<span class="cn">title</span>
<span class="cn">status</span>
<span class="cn">author</span> { ...<span class="cv">UserCore</span> }   <span class="cm"># reuse same fragment</span>
        }
<span class="cn">cursor</span>
      }
<span class="cn">pageInfo</span> { <span class="cn">hasNextPage</span> <span class="cn">endCursor</span> }
    }
  }
}

<span class="ck">fragment</span> <span class="cv">UserCore</span> <span class="ck">on</span> <span class="cv">User</span> {
  <span class="cn">id</span>
  <span class="cn">username</span>
  <span class="cn">email</span>
}
</div>
<div class="cb">
<span class="cm">// Variables sent as a separate JSON object (NOT interpolated into the query string)</span>
{
  <span class="cs">"userId"</span>: <span class="cs">"abc-123"</span>,
  <span class="cs">"first"</span>: <span class="cv">5</span>
}
</div>
<div class="sep">Inline Fragments for Unions / Interfaces</div>
<div class="cb">
<span class="ck">query</span> <span class="cv">Search</span>(<span class="cn">$q</span>: <span class="cv">String</span>!) {
  <span class="cn">search</span>(<span class="cn">query</span>: <span class="cn">$q</span>) {
<span class="cn">__typename</span>                <span class="cm"># always include to discriminate union members</span>
    ... <span class="ck">on</span> <span class="cv">User</span> {
<span class="cn">id</span>
<span class="cn">username</span>
    }
    ... <span class="ck">on</span> <span class="cv">Post</span> {
<span class="cn">id</span>
<span class="cn">title</span>
<span class="cn">status</span>
    }
  }
}
</div>
<div class="sep">Mutations</div>
<div class="cp p-indigo">
  <div class="cp-hdr">⚡ Mutation Execution Semantics</div>
  <div class="cp-body">
    Unlike queries (which execute fields in parallel), <strong>mutation root fields execute serially</strong> — one after another, in document order. This prevents race conditions between writes. Field resolvers <em>within</em> the mutation response shape still run in parallel.
  </div>
</div>
<div class="cb">
<span class="ck">mutation</span> <span class="cv">CreateAndPublish</span>(<span class="cn">$input</span>: <span class="cv">CreatePostInput</span>!) {
  <span class="cn">createPost</span>(<span class="cn">input</span>: <span class="cn">$input</span>) {
<span class="cn">id</span>
<span class="cn">title</span>
<span class="cn">status</span>
<span class="cn">author</span> { <span class="cn">id</span> <span class="cn">username</span> }
  }
}

<span class="cm">/* Response shape mirrors the selection set exactly */</span>
{
  <span class="cs">"data"</span>: {
<span class="cs">"createPost"</span>: {
<span class="cs">"id"</span>: <span class="cs">"post-789"</span>,
<span class="cs">"title"</span>: <span class="cs">"Hello World"</span>,
<span class="cs">"status"</span>: <span class="cs">"DRAFT"</span>,
<span class="cs">"author"</span>: { <span class="cs">"id"</span>: <span class="cs">"abc-123"</span>, <span class="cs">"username"</span>: <span class="cs">"ajay"</span> }
    }
  }
}
</div>
<div class="sep">Error Handling</div>
<div class="two-col">
<div class="cp p-orange">
  <div class="cp-hdr">⚠️ Partial Success Pattern</div>
  <div class="cp-body">
    GraphQL can return <strong>both data AND errors</strong> in the same response. A resolver that throws populates the <code>errors</code> array; other resolvers still run. This is fundamentally different from HTTP 4xx/5xx.
<br><br>
<code>{ "data": { "user": null }, "errors": [{ "message": "Not found", "locations": [...], "path": ["user"] }] }</code>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr">🏷️ Error Extensions Pattern</div>
  <div class="cp-body">
    Add structured error metadata via <code>extensions</code>:
<br><br>
<code>{ "message": "Unauthorized", "extensions": { "code": "UNAUTHENTICATED", "http": { "status": 401 } } }</code>
<br><br>
    Common codes: <code>UNAUTHENTICATED</code>, <code>FORBIDDEN</code>, <code>NOT_FOUND</code>, <code>BAD_USER_INPUT</code>, <code>INTERNAL_SERVER_ERROR</code>
  </div>
</div>
</div>
<div class="sep">Directives in Queries</div>
<div class="cb">
<span class="ck">query</span> <span class="cv">ConditionalQuery</span>(<span class="cn">$withEmail</span>: <span class="cv">Boolean</span>!, <span class="cn">$skipTags</span>: <span class="cv">Boolean</span>!) {
  <span class="cn">user</span>(<span class="cn">id</span>: <span class="cs">"123"</span>) {
<span class="cn">id</span>
<span class="cn">username</span>
<span class="cn">email</span>     <span class="ck">@include</span>(<span class="cn">if</span>: <span class="cn">$withEmail</span>)   <span class="cm"># field included only if true</span>
<span class="cn">posts</span>(<span class="cn">first</span>: <span class="cs">5</span>) {
<span class="cn">edges</span> { <span class="cn">node</span> {
<span class="cn">title</span>
<span class="cn">tags</span> <span class="ck">@skip</span>(<span class="cn">if</span>: <span class="cn">$skipTags</span>)        <span class="cm"># field omitted if true</span>
      } }
    }
  }
}
</div>
</div><!-- /t-ops -->
<!-- ═══════════════════════════════ SUBSCRIPTIONS ═══════════════════════════════ -->
<div id="t-subs" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr">📡 Subscriptions — Real-time Events</div>
  <div class="cp-body">
    Subscriptions are long-lived connections where the server pushes events to the client. The transport is typically <strong>WebSocket</strong> (graphql-ws protocol) or <strong>Server-Sent Events</strong>. The server maintains a pub/sub channel (Redis, in-memory) per subscription topic.
  </div>
</div>
<div class="sep">Subscription Operation</div>
<div class="cb">
<span class="cm"># Client sends this once over WebSocket</span>
<span class="ck">subscription</span> <span class="cv">WatchPost</span>(<span class="cn">$postId</span>: <span class="cv">ID</span>!) {
  <span class="cn">commentAdded</span>(<span class="cn">postId</span>: <span class="cn">$postId</span>) {
<span class="cn">id</span>
<span class="cn">body</span>
<span class="cn">author</span> { <span class="cn">id</span> <span class="cn">username</span> }
<span class="cn">createdAt</span>
  }
}

<span class="cm">/* Server pushes one event per new comment: */</span>
{ <span class="cs">"data"</span>: { <span class="cs">"commentAdded"</span>: { <span class="cs">"id"</span>: <span class="cs">"c-42"</span>, <span class="cs">"body"</span>: <span class="cs">"Great post!"</span>, ... } } }
</div>
<div class="sep">graphql-ws Protocol Message Flow</div>
<div class="diagram-box">
<span class="dg-gray">Client                                  Server</span>
<span class="dg-blue">  │── WS upgrade ──────────────────────▶│</span>
<span class="dg-blue">  │◀─ 101 Switching Protocols ──────────│</span>
<span class="dg-amber">  │── { type: "connection_init" } ──────▶│</span>
<span class="dg-amber">  │◀─ { type: "connection_ack" } ───────│</span>
<span class="dg-green">  │── { type: "subscribe",               │</span>
<span class="dg-green">  │     id: "1",                         │</span>
<span class="dg-green">  │     payload: { query, variables } } ─▶│  ← registers AsyncIterator</span>
<span class="dg-indigo">  │◀─ { type: "next", id: "1",          │</span>
<span class="dg-indigo">  │     payload: { data: {...} } } ──────│  ← event 1</span>
<span class="dg-indigo">  │◀─ { type: "next", id: "1", ... } ───│  ← event 2 …</span>
<span class="dg-red">  │── { type: "complete", id: "1" } ────▶│  ← client unsubscribes</span>
</div>
<div class="sep">Server-Side Subscription Resolver Pattern</div>
<div class="cb">
<span class="cm">// Node.js / graphql-js pattern (pseudocode)</span>
<span class="ck">const</span> <span class="cv">resolvers</span> = {
  <span class="cv">Subscription</span>: {
<span class="cn">commentAdded</span>: {
<span class="cm">// subscribe returns an AsyncIterator</span>
<span class="ck">subscribe</span>: (<span class="cn">_</span>, { <span class="cn">postId</span> }, { <span class="cn">pubsub</span> }) =>
<span class="cn">pubsub</span>.<span class="cf">asyncIterableIterator</span>(<span class="cs">`COMMENT_ADDED_${postId}`</span>),

<span class="cm">// resolve shapes each event payload</span>
<span class="ck">resolve</span>: (<span class="cn">payload</span>) => <span class="cn">payload</span>.<span class="cn">commentAdded</span>,
    },
  },
  <span class="cv">Mutation</span>: {
<span class="cn">addComment</span>: <span class="ck">async</span> (<span class="cn">_</span>, { <span class="cn">postId</span>, <span class="cn">body</span> }, { <span class="cn">db</span>, <span class="cn">pubsub</span>, <span class="cn">user</span> }) => {
<span class="ck">const</span> <span class="cv">comment</span> = <span class="ck">await</span> <span class="cn">db</span>.<span class="cf">createComment</span>({ <span class="cn">postId</span>, <span class="cn">body</span>, <span class="cn">authorId</span>: <span class="cn">user</span>.<span class="cn">id</span> });
<span class="ck">await</span> <span class="cn">pubsub</span>.<span class="cf">publish</span>(<span class="cs">`COMMENT_ADDED_${postId}`</span>, { <span class="cn">commentAdded</span>: <span class="cv">comment</span> });
<span class="ck">return</span> <span class="cv">comment</span>;
    },
  },
};
</div>
<div class="warn">⚠️ <strong>Subscription scaling:</strong> In-memory pub/sub only works for single-server deployments. In production, use Redis Pub/Sub (or Kafka) so events propagate across all server instances. Each subscriber node receives the event and delivers it to its connected WebSocket clients.</div>
<div class="sep">SSE as Lightweight Alternative</div>
<div class="cb">
<span class="cm">/* HTTP response headers for SSE */</span>
Content-Type: text/event-stream
Cache-Control: no-cache
Connection: keep-alive

<span class="cm">/* Each event is text/plain, double-newline terminated */</span>
data: {"data":{"commentAdded":{"id":"c-42","body":"Hello!"}}}

data: {"data":{"commentAdded":{"id":"c-43","body":"Nice!"}}}
</div>
<div class="note">💡 <strong>SSE vs WebSocket:</strong> SSE is uni-directional (server → client) and works over standard HTTP/1.1 — simpler to set up and proxy. WebSocket is full-duplex but requires special proxy configuration. For GraphQL subscriptions (server-push only), SSE is often sufficient and easier to operate.</div>
</div><!-- /t-subs -->
<!-- ═══════════════════════════════ RESOLVER CHAIN ═══════════════════════════════ -->
<div id="t-resolver" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr">🔗 Resolver Execution Model</div>
  <div class="cp-body">
    Execution walks the query AST depth-first. Each field calls a <strong>resolver function</strong>: <code>(parent, args, context, info) → value | Promise</code>. If no explicit resolver is provided, a default resolver reads <code>parent[fieldName]</code>. Leaf scalars terminate the walk.
  </div>
</div>
<div class="sep">Resolver Function Signature</div>
<div class="cb">
<span class="cm">/**
 * @param parent   - resolved value of the parent object
 * @param args     - field arguments from the query
 * @param context  - shared request state: db, auth user, DataLoader instances
 * @param info     - AST metadata: fieldName, returnType, path, schema
 */</span>
<span class="ck">async function</span> <span class="cf">userResolver</span>(<span class="cn">parent</span>, { <span class="cn">id</span> }, { <span class="cn">db</span>, <span class="cn">user</span> }, <span class="cn">info</span>) {
  <span class="ck">if</span> (!<span class="cn">user</span>) <span class="ck">throw new</span> <span class="cf">AuthenticationError</span>(<span class="cs">'Must be logged in'</span>);
  <span class="ck">return</span> <span class="cn">db</span>.<span class="cf">users</span>.<span class="cf">findById</span>(<span class="cn">id</span>);  <span class="cm">// returns Promise; runtime awaits it</span>
}
</div>
<div class="sep">N+1 Problem</div>
<div class="cp p-red">
  <div class="cp-hdr">🚨 N+1 — The Most Common GraphQL Performance Bug</div>
  <div class="cp-body">
    When a list query fetches N posts and each post's <code>author</code> resolver runs individually, you get <strong>1 query for posts + N queries for authors</strong> — even if many posts share the same author.
  </div>
</div>
<div class="diagram-box">
<span class="dg-amber">Query: posts(first: 100) { edges { node { title author { username } } } }</span>
<span class="dg-red">Without DataLoader:</span>
  SELECT * FROM posts LIMIT 100;           <span class="dg-gray">← 1 query</span>
  SELECT * FROM users WHERE id = 'u1';     <span class="dg-gray">← post 1</span>
  SELECT * FROM users WHERE id = 'u2';     <span class="dg-gray">← post 2</span>
  SELECT * FROM users WHERE id = 'u1';     <span class="dg-gray">← post 3 (duplicate!)</span>
  <span class="dg-gray">... 100 more individual selects</span>
  <span class="dg-red">Total: 101 queries</span>
<span class="dg-green">With DataLoader:</span>
  SELECT * FROM posts LIMIT 100;                          <span class="dg-gray">← 1 query</span>
  SELECT * FROM users WHERE id IN ('u1','u2','u3',...);  <span class="dg-gray">← 1 batched query</span>
  <span class="dg-green">Total: 2 queries</span>
</div>
<div class="sep">DataLoader — Batch + Cache</div>
<div class="cb">
<span class="cm">// DataLoader batches all loads queued in the same event-loop tick</span>
<span class="ck">import</span> <span class="cv">DataLoader</span> <span class="ck">from</span> <span class="cs">'dataloader'</span>;

<span class="cm">// Batch function: receives array of keys, returns array of values (same order!)</span>
<span class="ck">async function</span> <span class="cf">batchUsers</span>(<span class="cn">userIds</span>) {
  <span class="ck">const</span> <span class="cv">rows</span> = <span class="ck">await</span> <span class="cn">db</span>.<span class="cf">query</span>(<span class="cs">'SELECT * FROM users WHERE id = ANY($1)'</span>, [<span class="cn">userIds</span>]);
  <span class="ck">const</span> <span class="cv">map</span> = <span class="cv">Object</span>.<span class="cf">fromEntries</span>(<span class="cn">rows</span>.<span class="cf">map</span>(<span class="cn">r</span> => [<span class="cn">r</span>.<span class="cn">id</span>, <span class="cn">r</span>]));
  <span class="ck">return</span> <span class="cn">userIds</span>.<span class="cf">map</span>(<span class="cn">id</span> => <span class="cn">map</span>[<span class="cn">id</span>] || <span class="ck">new</span> <span class="cv">Error</span>(<span class="cs">`User ${id} not found`</span>));
}

<span class="cm">// Create one DataLoader per REQUEST (not global — to avoid cross-request cache)</span>
<span class="ck">function</span> <span class="cf">createContext</span>({ <span class="cn">req</span> }) {
  <span class="ck">return</span> {
<span class="cn">db</span>,
<span class="cn">user</span>: <span class="cf">authenticate</span>(<span class="cn">req</span>),
<span class="cn">loaders</span>: {
<span class="cn">user</span>: <span class="ck">new</span> <span class="cv">DataLoader</span>(<span class="cn">batchUsers</span>),
<span class="cm">// one loader per entity type</span>
    },
  };
}

<span class="cm">// Resolver uses loader instead of direct DB call</span>
<span class="ck">const</span> <span class="cv">resolvers</span> = {
  <span class="cv">Post</span>: {
<span class="cn">author</span>: (<span class="cn">post</span>, <span class="cn">_</span>, { <span class="cn">loaders</span> }) => <span class="cn">loaders</span>.<span class="cn">user</span>.<span class="cf">load</span>(<span class="cn">post</span>.<span class="cn">authorId</span>),
  },
};
</div>
<div class="note">💡 <strong>DataLoader contract:</strong> The batch function must return an array of the <em>same length</em> as the input keys, in the <em>same order</em>. DataLoader uses positional matching. Return an <code>Error</code> instance for missing keys — DataLoader will reject that specific <code>load()</code> promise.</div>
<div class="sep">Resolver Execution Trace — Depth-First, Breadth-Parallel</div>
<div class="diagram-box">
<span class="dg-gray">Execution order for: query { user(id:"1") { username posts { title author { username } } } }</span>
<span class="dg-blue">Level 0 (parallel): Query.user</span>
<span class="dg-indigo">  Level 1 (parallel): User.username, User.posts</span>
<span class="dg-purple">    Level 2 (parallel, per edge): Post.title, Post.author</span>
<span class="dg-green">      Level 3 (parallel, per post): User.username  ← batched by DataLoader</span>
<span class="dg-gray">Rules:</span>
  <span class="dg-amber">• Siblings at same level execute in parallel (Promise.all)</span>
  <span class="dg-amber">• Children wait for parent resolver to return</span>
  <span class="dg-amber">• Mutations: root fields are sequential; child fields are parallel</span>
</div>
</div><!-- /t-resolver -->
<!-- ═══════════════════════════════ PAGINATION ═══════════════════════════════ -->
<div id="t-pagination" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr">📄 Pagination in GraphQL</div>
  <div class="cp-body">
    The <strong>Relay Connection Spec</strong> is the de-facto standard for GraphQL pagination. It wraps results in a <code>Connection → [Edge { node, cursor }] + PageInfo</code> envelope, enabling both forward and backward cursor pagination without page-numbering problems.
  </div>
</div>
<div class="sep">Offset vs Cursor vs Keyset</div>
<table class="t-table">
  <thead><tr><th>Strategy</th><th>Query pattern</th><th>Pros</th><th>Cons</th></tr></thead>
  <tbody>
<tr><td><strong>Offset + Limit</strong></td><td><code>posts(offset:20, limit:10)</code></td><td>Simple, supports random page jumps</td><td>Skips/duplicates on concurrent inserts; full table scan for large offsets</td></tr>
<tr><td><strong>Cursor (Relay)</strong></td><td><code>posts(first:10, after:"cursor")</code></td><td>Stable, no skips on inserts, works well with infinite scroll</td><td>No random page access; cursor is opaque</td></tr>
<tr><td><strong>Keyset</strong></td><td><code>posts(after_id:42, limit:10)</code></td><td>O(log N) with index; most scalable</td><td>Tied to sort column; no skip; non-standard</td></tr>
  </tbody>
</table>
<div class="sep">Relay Connection — Forward Pagination</div>
<div class="cb">
<span class="ck">query</span> <span class="cv">PaginatePosts</span>(<span class="cn">$after</span>: <span class="cv">String</span>, <span class="cn">$first</span>: <span class="cv">Int</span> = <span class="cs">10</span>) {
  <span class="cn">posts</span>(<span class="cn">first</span>: <span class="cn">$first</span>, <span class="cn">after</span>: <span class="cn">$after</span>) {
<span class="cn">totalCount</span>
<span class="cn">pageInfo</span> {
<span class="cn">hasNextPage</span>
<span class="cn">endCursor</span>     <span class="cm"># pass this as $after in next request</span>
    }
<span class="cn">edges</span> {
<span class="cn">cursor</span>         <span class="cm"># per-edge cursor (base64 opaque string)</span>
<span class="cn">node</span> { <span class="cn">id</span> <span class="cn">title</span> <span class="cn">createdAt</span> }
    }
  }
}
</div>
<div class="sep">Cursor Encoding Pattern</div>
<div class="cb">
<span class="cm">// Cursor = base64( "PostCursor:" + sortKey )</span>
<span class="cm">// sortKey is typically the column used for ORDER BY</span>
<span class="ck">function</span> <span class="cf">encodeCursor</span>(<span class="cn">sortValue</span>) {
  <span class="ck">return</span> <span class="cv">Buffer</span>.<span class="cf">from</span>(<span class="cs">`PostCursor:${sortValue}`</span>).<span class="cf">toString</span>(<span class="cs">'base64'</span>);
}

<span class="ck">function</span> <span class="cf">decodeCursor</span>(<span class="cn">cursor</span>) {
  <span class="ck">const</span> <span class="cv">raw</span> = <span class="cv">Buffer</span>.<span class="cf">from</span>(<span class="cn">cursor</span>, <span class="cs">'base64'</span>).<span class="cf">toString</span>(<span class="cs">'utf8'</span>); <span class="cm">// "PostCursor:2024-01-15T..."</span>
  <span class="ck">return</span> <span class="cv">raw</span>.<span class="cf">replace</span>(<span class="cs">'PostCursor:'</span>, <span class="cs">''</span>);
}

<span class="cm">// Resolver builds SQL using decoded cursor</span>
<span class="ck">async function</span> <span class="cf">postsResolver</span>(<span class="cn">_</span>, { <span class="cn">first</span> = <span class="cs">10</span>, <span class="cn">after</span> }, { <span class="cn">db</span> }) {
  <span class="ck">const</span> <span class="cv">cursorValue</span> = <span class="cn">after</span> ? <span class="cf">decodeCursor</span>(<span class="cn">after</span>) : <span class="ck">null</span>;
  <span class="ck">const</span> <span class="cv">rows</span> = <span class="ck">await</span> <span class="cn">db</span>.<span class="cf">query</span>(
<span class="cs">`SELECT * FROM posts
     WHERE ($1::timestamptz IS NULL OR created_at < $1)
     ORDER BY created_at DESC
     LIMIT $2`</span>,
    [<span class="cn">cursorValue</span>, <span class="cn">first</span> + <span class="cs">1</span>]   <span class="cm">// fetch +1 to detect hasNextPage</span>
  );
  <span class="ck">const</span> <span class="cv">hasNextPage</span> = <span class="cn">rows</span>.<span class="cn">length</span> > <span class="cn">first</span>;
  <span class="ck">if</span> (<span class="cn">hasNextPage</span>) <span class="cn">rows</span>.<span class="cf">pop</span>();
  <span class="ck">return</span> {
<span class="cn">edges</span>: <span class="cn">rows</span>.<span class="cf">map</span>(<span class="cn">r</span> => ({ <span class="cn">node</span>: <span class="cn">r</span>, <span class="cn">cursor</span>: <span class="cf">encodeCursor</span>(<span class="cn">r</span>.<span class="cn">created_at</span>) })),
<span class="cn">pageInfo</span>: {
<span class="cn">hasNextPage</span>,
<span class="cn">endCursor</span>: <span class="cn">rows</span>.<span class="cn">length</span> ? <span class="cf">encodeCursor</span>(<span class="cn">rows</span>.<span class="cf">at</span>(-<span class="cs">1</span>).<span class="cn">created_at</span>) : <span class="ck">null</span>,
    },
<span class="cn">totalCount</span>: <span class="ck">await</span> <span class="cn">db</span>.<span class="cf">count</span>(<span class="cs">'posts'</span>),
  };
}
</div>
<div class="sep">Filtering & Sorting Pattern</div>
<div class="cb">
<span class="cm"># SDL for flexible filtering</span>
<span class="ck">input</span> <span class="cv">PostFilter</span> {
  <span class="cn">status</span>:    <span class="cv">PostStatus</span>
  <span class="cn">authorId</span>:  <span class="cv">ID</span>
  <span class="cn">tags</span>:      [<span class="cv">String</span>!]
  <span class="cn">createdAfter</span>:  <span class="cv">DateTime</span>
  <span class="cn">createdBefore</span>: <span class="cv">DateTime</span>
}

<span class="ck">input</span> <span class="cv">PostSort</span> {
  <span class="cn">field</span>:     <span class="cv">PostSortField</span>!
  <span class="cn">direction</span>: <span class="cv">SortDirection</span>!
}

<span class="ck">enum</span> <span class="cv">PostSortField</span> { <span class="co">CREATED_AT</span>  <span class="co">TITLE</span>  <span class="co">AUTHOR_NAME</span> }

<span class="ck">type</span> <span class="cv">Query</span> {
  <span class="cn">posts</span>(
<span class="cn">first</span>:   <span class="cv">Int</span>,
<span class="cn">after</span>:   <span class="cv">String</span>,
<span class="cn">filter</span>:  <span class="cv">PostFilter</span>,
<span class="cn">sort</span>:    <span class="cv">PostSort</span>
  ): <span class="cv">PostConnection</span>!
}
</div>
<div class="analogy">🧠 <strong>Mental model:</strong> Think of a cursor as a bookmark in a sorted list — it points to the last item you read. Next time you open the book, you pick up exactly where you left off, regardless of what was added or removed elsewhere in the list.</div>
</div><!-- /t-pagination -->
<!-- ═══════════════════════════════ FEDERATION & CONTRACTS ═══════════════════════════════ -->
<div id="t-advanced" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr">🏛️ Schema Federation</div>
  <div class="cp-body">
<strong>Apollo Federation</strong> lets you split a GraphQL schema across multiple independent services (<em>subgraphs</em>). A <em>gateway</em> composes them into a unified <em>supergraph</em>. Each subgraph owns its types and can extend types owned by other subgraphs via <code>@key</code> + <code>@external</code> directives.
  </div>
</div>
<div class="sep">Federation Architecture</div>
<div class="diagram-box">
<span class="dg-gray">Client</span>
<span class="dg-blue">  │── POST /graphql ──────────────▶ Gateway (Router)</span>
<span class="dg-blue">                                        │</span>
<span class="dg-blue">                   ┌────────────────────┼───────────────────┐</span>
<span class="dg-green">                   ▼                    ▼                   ▼</span>
<span class="dg-green">             User Service          Post Service        Comment Service</span>
<span class="dg-green">             (subgraph)            (subgraph)           (subgraph)</span>
<span class="dg-amber">             type User @key(       type Post @key(     type Comment {</span>
<span class="dg-amber">               fields:"id") {        fields:"id") {      postId: ID!</span>
<span class="dg-amber">               id: ID!               id: ID!             body: String!</span>
<span class="dg-amber">               username: String!     author: User!       author: User!</span>
<span class="dg-amber">             }                     }                   }</span>
<span class="dg-gray">             ↑ owns User            ↑ references User    ↑ references User</span>
</div>
<div class="cb">
<span class="cm"># Post subgraph — references User from User subgraph</span>
<span class="ck">extend type</span> <span class="cv">User</span> <span class="ck">@key</span>(<span class="cn">fields</span>: <span class="cs">"id"</span>) {
  <span class="cn">id</span>: <span class="cv">ID</span>! <span class="ck">@external</span>     <span class="cm"># owned by User subgraph</span>
}

<span class="ck">type</span> <span class="cv">Post</span> <span class="ck">@key</span>(<span class="cn">fields</span>: <span class="cs">"id"</span>) {
  <span class="cn">id</span>:     <span class="cv">ID</span>!
  <span class="cn">title</span>:  <span class="cv">String</span>!
  <span class="cn">author</span>: <span class="cv">User</span>!         <span class="cm"># gateway will resolve via User subgraph</span>
}
</div>
<div class="sep">Persisted Queries</div>
<div class="cp p-indigo">
  <div class="cp-hdr">🔒 Persisted Queries — Security + Performance</div>
  <div class="cp-body">
    Instead of sending the full query string on every request, the client registers queries at build time and sends only a <strong>hash/ID</strong> at runtime. Benefits: (1) smaller payloads, (2) server can whitelist approved queries, (3) prevents arbitrary query injection.
  </div>
</div>
<div class="cb">
<span class="cm">/* Automatic Persisted Query (APQ) protocol */</span>
<span class="cm">/* Step 1 — Send hash only */</span>
POST /graphql
{ <span class="cs">"extensions"</span>: { <span class="cs">"persistedQuery"</span>: { <span class="cs">"version"</span>: <span class="cs">1</span>, <span class="cs">"sha256Hash"</span>: <span class="cs">"abc123..."</span> } } }

<span class="cm">/* Server responds with 404 if not cached */</span>
{ <span class="cs">"errors"</span>: [{ <span class="cs">"message"</span>: <span class="cs">"PersistedQueryNotFound"</span> }] }

<span class="cm">/* Step 2 — Resend with full query to register */</span>
POST /graphql
{
  <span class="cs">"query"</span>: <span class="cs">"query GetUser($id:ID!){user(id:$id){id username}}"</span>,
  <span class="cs">"extensions"</span>: { <span class="cs">"persistedQuery"</span>: { <span class="cs">"version"</span>: <span class="cs">1</span>, <span class="cs">"sha256Hash"</span>: <span class="cs">"abc123..."</span> } }
}

<span class="cm">/* Server caches query; subsequent requests use hash only */</span>
</div>
<div class="sep">Introspection</div>
<div class="cb">
<span class="cm"># Introspection query — clients use this for schema discovery</span>
{ __schema { types { name kind fields { name type { name kind } } } } }

<span class="cm"># Disable in production to prevent schema enumeration by attackers</span>
<span class="cm"># Apollo Server: introspection: process.env.NODE_ENV !== 'production'</span>
</div>
<div class="sep">Schema Evolution Rules</div>
<table class="t-table">
  <thead><tr><th>Change</th><th>Safe?</th><th>Reason</th></tr></thead>
  <tbody>
<tr><td>Add nullable field to object type</td><td>✅ Safe</td><td>Existing clients ignore unknown fields</td></tr>
<tr><td>Add optional argument to field</td><td>✅ Safe</td><td>Clients that omit the arg still work</td></tr>
<tr><td>Add new enum value</td><td>⚠️ Breaking for exhaustive switches</td><td>Client code doing switch/case may fail on new value</td></tr>
<tr><td>Remove field</td><td>❌ Breaking</td><td>Existing queries referencing it fail validation</td></tr>
<tr><td>Change field type</td><td>❌ Breaking</td><td>Type mismatch at runtime</td></tr>
<tr><td>Add non-null field</td><td>❌ Breaking</td><td>Old clients may not provide required field</td></tr>
<tr><td>Remove enum value</td><td>❌ Breaking</td><td>Old clients may send the removed value</td></tr>
<tr><td>Rename type</td><td>❌ Breaking</td><td>Fragment spreads use type names</td></tr>
  </tbody>
</table>
<div class="note">💡 <strong>Deprecation workflow:</strong> mark fields with <code>@deprecated(reason: "Use newField instead")</code> — introspection tools surface it to developers. Keep deprecated fields for at least one release cycle before removal.</div>
<div class="sep">Query Complexity & Depth Limiting</div>
<div class="cb">
<span class="cm">// Prevent deeply-nested or expensive queries from DoS-ing your server</span>
<span class="ck">import</span> { <span class="cv">createComplexityRule</span> } <span class="ck">from</span> <span class="cs">'graphql-query-complexity'</span>;

<span class="ck">const</span> <span class="cv">server</span> = <span class="ck">new</span> <span class="cv">ApolloServer</span>({
  <span class="cn">validationRules</span>: [
<span class="cf">createComplexityRule</span>({
<span class="cn">maximumComplexity</span>: <span class="cs">1000</span>,
<span class="cn">variables</span>: {},
<span class="cf">onComplete</span>: (<span class="cn">complexity</span>) => <span class="cn">console</span>.<span class="cf">log</span>(<span class="cs">`Query complexity: ${complexity}`</span>),
<span class="cn">createError</span>: (<span class="cn">max</span>, <span class="cn">actual</span>) =>
<span class="ck">new</span> <span class="cv">Error</span>(<span class="cs">`Query too complex: ${actual} > ${max}`</span>),
    }),
  ],
  <span class="cn">depthLimit</span>: <span class="cs">7</span>,   <span class="cm">// reject queries deeper than 7 levels</span>
});
</div>
</div><!-- /t-advanced -->
<!-- ═══════════════════════════════ C IMPLEMENTATION ═══════════════════════════════ -->
<!-- Reusing tab slot for C implementation, accessed via Labs tab -->
<!-- ═══════════════════════════════ LABS & CHECKLIST ═══════════════════════════════ -->
<div id="t-labs" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr">🔧 GraphQL Parser Sketch in C</div>
  <div class="cp-body">
    Real-world GraphQL servers are implemented in JS/Go/Rust/Python. However, understanding how the <strong>lexer and parser</strong> work is essential for deep mastery. Below is a minimal hand-rolled lexer for GraphQL query strings.
  </div>
</div>
<div class="cb">
<span class="cm">/* gql_lexer.h — minimal GraphQL lexer in C */</span>
<span class="ck">#include</span> <span class="cs">&lt;stdio.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;string.h&gt;</span>
<span class="ck">#include</span> <span class="cs">&lt;ctype.h&gt;</span>
<span class="ck">typedef enum</span> {
  <span class="co">TOK_NAME</span>, <span class="co">TOK_INT</span>, <span class="co">TOK_FLOAT</span>, <span class="co">TOK_STRING</span>,
  <span class="co">TOK_LBRACE</span>, <span class="co">TOK_RBRACE</span>, <span class="co">TOK_LPAREN</span>, <span class="co">TOK_RPAREN</span>,
  <span class="co">TOK_COLON</span>, <span class="co">TOK_BANG</span>, <span class="co">TOK_DOLLAR</span>, <span class="co">TOK_AT</span>,
  <span class="co">TOK_SPREAD</span>,   <span class="cm">/* ... */</span>
  <span class="co">TOK_EOF</span>, <span class="co">TOK_ERR</span>
} <span class="cv">GqlTokKind</span>;

<span class="ck">typedef struct</span> {
  <span class="cv">GqlTokKind</span>  <span class="cn">kind</span>;
  <span class="ck">const char</span> *<span class="cn">start</span>;
  <span class="cv">size_t</span>      <span class="cn">len</span>;
} <span class="cv">GqlToken</span>;

<span class="ck">typedef struct</span> {
  <span class="ck">const char</span> *<span class="cn">src</span>;
  <span class="cv">size_t</span>      <span class="cn">pos</span>;
  <span class="cv">size_t</span>      <span class="cn">len</span>;
} <span class="cv">GqlLexer</span>;

<span class="ck">static void</span> <span class="cf">gql_skip_ignored</span>(<span class="cv">GqlLexer</span> *<span class="cn">l</span>) {
  <span class="ck">while</span> (<span class="cn">l</span>-><span class="cn">pos</span> < <span class="cn">l</span>-><span class="cn">len</span>) {
<span class="ck">char</span> <span class="cn">c</span> = <span class="cn">l</span>-><span class="cn">src</span>[<span class="cn">l</span>-><span class="cn">pos</span>];
<span class="ck">if</span> (<span class="cn">c</span> == <span class="co">'#'</span>) {    <span class="cm">/* comment: skip to end of line */</span>
<span class="ck">while</span> (<span class="cn">l</span>-><span class="cn">pos</span> < <span class="cn">l</span>-><span class="cn">len</span> && <span class="cn">l</span>-><span class="cn">src</span>[<span class="cn">l</span>-><span class="cn">pos</span>] != <span class="co">'\n'</span>) <span class="cn">l</span>-><span class="cn">pos</span>++;
    } <span class="ck">else if</span> (<span class="cn">isspace</span>(<span class="cn">c</span>) || <span class="cn">c</span> == <span class="co">','</span>) {
<span class="cn">l</span>-><span class="cn">pos</span>++;     <span class="cm">/* commas are whitespace in GraphQL */</span>
    } <span class="ck">else</span> <span class="ck">break</span>;
  }
}

<span class="cv">GqlToken</span> <span class="cf">gql_next_token</span>(<span class="cv">GqlLexer</span> *<span class="cn">l</span>) {
  <span class="cf">gql_skip_ignored</span>(<span class="cn">l</span>);
  <span class="ck">if</span> (<span class="cn">l</span>-><span class="cn">pos</span> >= <span class="cn">l</span>-><span class="cn">len</span>) <span class="ck">return</span> (<span class="cv">GqlToken</span>){ <span class="co">TOK_EOF</span>, <span class="ck">NULL</span>, <span class="cs">0</span> };

  <span class="ck">char</span> <span class="cn">c</span> = <span class="cn">l</span>-><span class="cn">src</span>[<span class="cn">l</span>-><span class="cn">pos</span>];
  <span class="ck">if</span> (<span class="cn">isalpha</span>(<span class="cn">c</span>) || <span class="cn">c</span> == <span class="co">'_'</span>) {
<span class="ck">size_t</span> <span class="cn">start</span> = <span class="cn">l</span>-><span class="cn">pos</span>++;
<span class="ck">while</span> (<span class="cn">l</span>-><span class="cn">pos</span> < <span class="cn">l</span>-><span class="cn">len</span> && (<span class="cn">isalnum</span>(<span class="cn">l</span>-><span class="cn">src</span>[<span class="cn">l</span>-><span class="cn">pos</span>]) || <span class="cn">l</span>-><span class="cn">src</span>[<span class="cn">l</span>-><span class="cn">pos</span>] == <span class="co">'_'</span>)) <span class="cn">l</span>-><span class="cn">pos</span>++;
<span class="ck">return</span> (<span class="cv">GqlToken</span>){ <span class="co">TOK_NAME</span>, <span class="cn">l</span>-><span class="cn">src</span> + <span class="cn">start</span>, <span class="cn">l</span>-><span class="cn">pos</span> - <span class="cn">start</span> };
  }
  <span class="ck">switch</span> (<span class="cn">c</span>) {
<span class="ck">case</span> <span class="co">'{'</span>: <span class="cn">l</span>-><span class="cn">pos</span>++; <span class="ck">return</span> (<span class="cv">GqlToken</span>){ <span class="co">TOK_LBRACE</span>, <span class="cn">l</span>-><span class="cn">src</span>+<span class="cn">l</span>-><span class="cn">pos</span>-<span class="cs">1</span>, <span class="cs">1</span> };
<span class="ck">case</span> <span class="co">'}'</span>: <span class="cn">l</span>-><span class="cn">pos</span>++; <span class="ck">return</span> (<span class="cv">GqlToken</span>){ <span class="co">TOK_RBRACE</span>, <span class="cn">l</span>-><span class="cn">src</span>+<span class="cn">l</span>-><span class="cn">pos</span>-<span class="cs">1</span>, <span class="cs">1</span> };
<span class="ck">case</span> <span class="co">'('</span>: <span class="cn">l</span>-><span class="cn">pos</span>++; <span class="ck">return</span> (<span class="cv">GqlToken</span>){ <span class="co">TOK_LPAREN</span>, <span class="cn">l</span>-><span class="cn">src</span>+<span class="cn">l</span>-><span class="cn">pos</span>-<span class="cs">1</span>, <span class="cs">1</span> };
<span class="ck">case</span> <span class="co">')'</span>: <span class="cn">l</span>-><span class="cn">pos</span>++; <span class="ck">return</span> (<span class="cv">GqlToken</span>){ <span class="co">TOK_RPAREN</span>, <span class="cn">l</span>-><span class="cn">src</span>+<span class="cn">l</span>-><span class="cn">pos</span>-<span class="cs">1</span>, <span class="cs">1</span> };
<span class="ck">case</span> <span class="co">':'</span>: <span class="cn">l</span>-><span class="cn">pos</span>++; <span class="ck">return</span> (<span class="cv">GqlToken</span>){ <span class="co">TOK_COLON</span>,  <span class="cn">l</span>-><span class="cn">src</span>+<span class="cn">l</span>-><span class="cn">pos</span>-<span class="cs">1</span>, <span class="cs">1</span> };
<span class="ck">case</span> <span class="co">'!'</span>: <span class="cn">l</span>-><span class="cn">pos</span>++; <span class="ck">return</span> (<span class="cv">GqlToken</span>){ <span class="co">TOK_BANG</span>,   <span class="cn">l</span>-><span class="cn">src</span>+<span class="cn">l</span>-><span class="cn">pos</span>-<span class="cs">1</span>, <span class="cs">1</span> };
<span class="ck">case</span> <span class="co">'$'</span>: <span class="cn">l</span>-><span class="cn">pos</span>++; <span class="ck">return</span> (<span class="cv">GqlToken</span>){ <span class="co">TOK_DOLLAR</span>, <span class="cn">l</span>-><span class="cn">src</span>+<span class="cn">l</span>-><span class="cn">pos</span>-<span class="cs">1</span>, <span class="cs">1</span> };
<span class="ck">case</span> <span class="co">'@'</span>: <span class="cn">l</span>-><span class="cn">pos</span>++; <span class="ck">return</span> (<span class="cv">GqlToken</span>){ <span class="co">TOK_AT</span>,     <span class="cn">l</span>-><span class="cn">src</span>+<span class="cn">l</span>-><span class="cn">pos</span>-<span class="cs">1</span>, <span class="cs">1</span> };
<span class="ck">default</span>: <span class="cn">l</span>-><span class="cn">pos</span>++; <span class="ck">return</span> (<span class="cv">GqlToken</span>){ <span class="co">TOK_ERR</span>,   <span class="cn">l</span>-><span class="cn">src</span>+<span class="cn">l</span>-><span class="cn">pos</span>-<span class="cs">1</span>, <span class="cs">1</span> };
  }
}

<span class="ck">int</span> <span class="cf">main</span>(<span class="ck">void</span>) {
  <span class="ck">const char</span> *<span class="cn">src</span> = <span class="cs">"{ user(id: \"abc\") { id username } }"</span>;
  <span class="cv">GqlLexer</span> <span class="cn">lexer</span> = { <span class="cn">src</span>, <span class="cs">0</span>, <span class="cf">strlen</span>(<span class="cn">src</span>) };
  <span class="cv">GqlToken</span> <span class="cn">tok</span>;
  <span class="ck">while</span> ((<span class="cn">tok</span> = <span class="cf">gql_next_token</span>(&<span class="cn">lexer</span>)).<span class="cn">kind</span> != <span class="co">TOK_EOF</span>) {
<span class="cf">printf</span>(<span class="cs">"kind=%d  text=%.*s\n"</span>, <span class="cn">tok</span>.<span class="cn">kind</span>, (<span class="ck">int</span>)<span class="cn">tok</span>.<span class="cn">len</span>, <span class="cn">tok</span>.<span class="cn">start</span>);
  }
  <span class="ck">return</span> <span class="cs">0</span>;
}
</div>
<div class="sep">Labs</div>
<div class="lab-box">
  <div class="lab-hdr">🧪 Lab 1 — Schema-First Blog API</div>
  <div class="lab-body">
<strong>Goal:</strong> Design and implement a complete GraphQL schema for a blogging platform with users, posts, comments, and tags.
<div class="lab-step"><span class="sn">1</span> Write the full SDL: scalars, enums, interfaces (Node), all object types, input types, and root Query/Mutation/Subscription types</div>
<div class="lab-step"><span class="sn">2</span> Implement all resolvers using a SQLite or in-memory data store</div>
<div class="lab-step"><span class="sn">3</span> Add DataLoader for all parent→child relationships (post.author, comment.author, post.comments)</div>
<div class="lab-step"><span class="sn">4</span> Verify N+1 elimination: log all SQL queries and count them for a <code>posts { author }</code> query</div>
<div class="lab-step"><span class="sn">5</span> Implement cursor pagination on posts list with proper <code>PageInfo</code></div>
<div class="lab-step"><span class="sn">6</span> Test with GraphiQL or Apollo Sandbox: query, mutation, and subscription</div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr">🧪 Lab 2 — Federation Across Two Services</div>
  <div class="lab-body">
<strong>Goal:</strong> Split the blog API into User Service and Post Service, federate them with Apollo Router.
<div class="lab-step"><span class="sn">1</span> Create User subgraph: own <code>type User @key(fields: "id")</code>; expose <code>Query.user(id)</code> and <code>Query.me</code></div>
<div class="lab-step"><span class="sn">2</span> Create Post subgraph: reference User via <code>extend type User @key(fields: "id")</code>; implement <code>@requires</code> if needed</div>
<div class="lab-step"><span class="sn">3</span> Run Apollo Router (or Apollo Gateway) to compose both subgraphs into a supergraph</div>
<div class="lab-step"><span class="sn">4</span> Issue a query that spans both services: <code>{ post(id:"1") { title author { username email } } }</code></div>
<div class="lab-step"><span class="sn">5</span> Inspect Router query plan to understand how it splits and joins the request</div>
<div class="lab-step"><span class="sn">6</span> Add <code>@deprecated</code> to a field in the Post schema and verify it surfaces in introspection</div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr">🧪 Lab 3 — GraphQL Lexer in C</div>
  <div class="lab-body">
<strong>Goal:</strong> Extend the minimal C lexer above into a working parser that produces a field-selection AST.
<div class="lab-step"><span class="sn">1</span> Extend <code>GqlLexer</code> to handle string literals (quoted, escaped), integer, and float tokens</div>
<div class="lab-step"><span class="sn">2</span> Define <code>GqlNode</code> (AST node) with fields: <code>kind</code>, <code>name</code>, <code>children[]</code>, <code>args[]</code></div>
<div class="lab-step"><span class="sn">3</span> Write a recursive-descent parser: <code>parse_document → parse_operation → parse_selection_set → parse_field</code></div>
<div class="lab-step"><span class="sn">4</span> Pretty-print the resulting AST for input <code>{ user(id:"1") { id username posts { title } } }</code></div>
<div class="lab-step"><span class="sn">5</span> Add variable extraction: collect all <code>$varName: Type</code> from the operation definition</div>
<div class="lab-step"><span class="sn">6</span> Validate that every field in the selection set exists in a hard-coded schema map (key = "TypeName.fieldName")</div>
  </div>
</div>
<div class="sep">Mastery Checklist</div>
<ul class="cl">
  <li>Define object types, interfaces, unions, enums, input types, and custom scalars in SDL</li>
  <li>Explain non-null semantics and null propagation with an example</li>
  <li>Write a named query with variables, fragments, and inline fragments for unions</li>
  <li>Implement a mutation with an input type; explain serial vs parallel execution</li>
  <li>Explain the N+1 problem with a concrete SQL trace; implement DataLoader batching</li>
  <li>Implement cursor pagination following the Relay Connection spec</li>
  <li>Set up a GraphQL subscription over WebSocket using graphql-ws protocol</li>
  <li>Use @skip and @include directives in client queries</li>
  <li>Explain @deprecated and describe the safe schema evolution workflow</li>
  <li>Set up Apollo Federation with two subgraphs and a gateway/router</li>
  <li>Explain Automatic Persisted Queries (APQ) — protocol, benefits, and security</li>
  <li>Implement query complexity limiting and depth limiting</li>
  <li>Disable introspection in production; explain the security risk</li>
  <li>Distinguish GraphQL error handling (partial success) from HTTP status code semantics</li>
  <li>Describe the GraphQL execution pipeline: parse → validate → execute → coerce</li>
</ul>
<div class="mod-nav">
  <a href="/learning/backend/m04-grpc/" class="nb">← M04 gRPC</a>
  <a href="/learning/backend/" class="nb">↑ Roadmap</a>
  <a href="/learning/backend/m06-sql-indexing/" class="nb">M06 SQL Indexing →</a>
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
