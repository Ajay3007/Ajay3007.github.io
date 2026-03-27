---
layout: default
title: "M15 — Microservices & Infrastructure"
description: "Service architecture decisions, API Gateway, circuit breaker, Docker multi-stage builds, Kubernetes fundamentals, CI/CD pipelines — with C implementations"
---

<style>
/* ── Module shell ── */
.mod-wrap{max-width:960px;margin:0 auto;padding:0 1rem 4rem;font-family:'Segoe UI',system-ui,sans-serif;color:#1e293b}
.mod-header{background:#fff;border-left:5px solid #f59e0b;border-radius:10px;padding:1.6rem 2rem;margin-bottom:1.5rem;box-shadow:0 2px 12px rgba(0,0,0,.08)}
.mod-header h1{margin:0 0 .4rem;font-size:1.75rem;color:#0f172a}
.mod-header .sub{color:#64748b;font-size:.95rem}
.phase-tag{display:inline-block;background:linear-gradient(90deg,#f59e0b,#10b981);color:#fff;font-size:.75rem;font-weight:700;padding:.25rem .75rem;border-radius:20px;margin-right:.5rem;text-transform:uppercase;letter-spacing:.05em}

/* ── Tabs ── */
.tab-bar{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:1.25rem}
.tab-btn{padding:.45rem 1rem;border:2px solid #e2e8f0;border-radius:20px;background:#fff;font-size:.82rem;font-weight:600;cursor:pointer;color:#64748b;transition:all .2s}
.tab-btn:hover{border-color:#f59e0b;color:#b45309}
.tab-btn.active{background:linear-gradient(135deg,#f59e0b,#10b981);border-color:transparent;color:#fff;box-shadow:0 3px 10px rgba(245,158,11,.35)}
.tab-pane{display:none}.tab-pane.active{display:block}

/* ── Cards / panels ── */
.cp{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.cp-hdr{padding:.65rem 1.1rem;font-weight:700;font-size:.9rem;display:flex;align-items:center;gap:.5rem}
.cp-body{padding:1rem 1.2rem;background:#fff;font-size:.9rem;line-height:1.75}
.p-amber .cp-hdr{background:linear-gradient(90deg,#fffbeb,#fef3c7);color:#92400e;border-left:4px solid #f59e0b}
.p-green .cp-hdr{background:linear-gradient(90deg,#f0fdf4,#dcfce7);color:#15803d;border-left:4px solid #10b981}
.p-blue  .cp-hdr{background:linear-gradient(90deg,#eff6ff,#dbeafe);color:#1d4ed8;border-left:4px solid #3b82f6}
.p-teal  .cp-hdr{background:linear-gradient(90deg,#f0fdf4,#dcfce7);color:#0f766e;border-left:4px solid #14b8a6}
.p-orange.cp-hdr,.p-orange>.cp-hdr{background:linear-gradient(90deg,#fff7ed,#ffedd5);color:#c2410c;border-left:4px solid #f97316}
.p-red   .cp-hdr{background:linear-gradient(90deg,#fff1f2,#ffe4e6);color:#be123c;border-left:4px solid #f43f5e}
.p-purple.cp-hdr,.p-purple>.cp-hdr{background:linear-gradient(90deg,#faf5ff,#f3e8ff);color:#7e22ce;border-left:4px solid #a855f7}
.p-indigo.cp-hdr{background:linear-gradient(90deg,#eef2ff,#e0e7ff);color:#3730a3;border-left:4px solid #6366f1}
.p-cyan  .cp-hdr{background:linear-gradient(90deg,#ecfeff,#cffafe);color:#0e7490;border-left:4px solid #06b6d4}
.p-orange{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.p-purple{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}

/* ── Callouts ── */
.ins,.warn,.note,.analogy{border-radius:8px;padding:.75rem 1rem;margin:.75rem 0;font-size:.87rem;line-height:1.7}
.ins  {background:#fffbeb;border-left:4px solid #f59e0b;color:#78350f}
.warn {background:#fff7ed;border-left:4px solid #f97316;color:#7c2d12}
.note {background:#f0fdf4;border-left:4px solid #10b981;color:#064e3b}
.analogy{background:#faf5ff;border-left:4px solid #a855f7;color:#581c87}

/* ── Code blocks ── */
.cb{background:#0f172a;border-radius:10px;padding:1.1rem 1.3rem;margin:.75rem 0;overflow-x:auto;font-size:.82rem;line-height:1.75;font-family:'Cascadia Code','Fira Code',monospace}
.cm{color:#94a3b8}.ck{color:#7dd3fc}.cv{color:#86efac}.cs{color:#fca5a5}
.cn{color:#fdba74}.cf{color:#c4b5fd}.co{color:#fde68a}.cg{color:#6ee7b7}

/* ── Flow list ── */
.flow-list{list-style:none;padding:0;margin:.5rem 0}
.fl-step{display:flex;align-items:flex-start;gap:.85rem;padding:.65rem .85rem;margin-bottom:.5rem;border-radius:8px;background:#f8fafc;border-left:3px solid #f59e0b;font-size:.88rem;line-height:1.65}
.fl-num{background:linear-gradient(135deg,#f59e0b,#10b981);color:#fff;border-radius:50%;width:1.6rem;height:1.6rem;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.75rem;flex-shrink:0}

/* ── Tables ── */
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.75rem 0}
.t-table th{background:linear-gradient(90deg,#f59e0b,#10b981);color:#fff;padding:.6rem .9rem;text-align:left}
.t-table td{padding:.55rem .9rem;border-bottom:1px solid #e2e8f0;vertical-align:top}
.t-table tr:nth-child(even) td{background:#f8fafc}
.t-table tr:hover td{background:#fffbeb}

/* ── Two-col ── */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.75rem 0}
@media(max-width:640px){.two-col{grid-template-columns:1fr}}

/* ── Lab box ── */
.lab-box{border:2px solid #f59e0b;border-radius:10px;margin-bottom:1.25rem;overflow:hidden}
.lab-hdr{background:linear-gradient(90deg,#fffbeb,#fef3c7);padding:.7rem 1.1rem;display:flex;align-items:center;gap:.6rem;font-weight:700;font-size:.9rem;color:#92400e}
.lab-body{padding:1rem 1.2rem;font-size:.88rem;line-height:1.75}
.lab-step{padding:.4rem 0;padding-left:1.1rem;border-left:2px solid #f59e0b;margin-bottom:.4rem}
.sn{display:inline-block;background:#f59e0b;color:#fff;border-radius:50%;width:1.3rem;height:1.3rem;font-size:.7rem;font-weight:700;text-align:center;line-height:1.3rem;margin-right:.4rem}

/* ── Checklist ── */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{padding:.35rem .5rem;font-size:.87rem;display:flex;align-items:flex-start;gap:.6rem}
.cl li::before{content:"☐";color:#f59e0b;font-size:1rem;flex-shrink:0}

/* ── State machine ── */
.diagram-box{background:#0f172a;border-radius:10px;padding:1.1rem 1.3rem;margin:.75rem 0;overflow-x:auto;font-family:'Cascadia Code','Fira Code',monospace;font-size:.78rem;line-height:1.8;color:#94a3b8}
.dg-amber{color:#fde68a}.dg-green{color:#86efac}.dg-red{color:#fca5a5}.dg-blue{color:#93c5fd}.dg-gray{color:#64748b}.dg-purple{color:#c4b5fd}.dg-cyan{color:#67e8f9}

/* ── Navigation ── */
.mod-nav{display:flex;justify-content:space-between;align-items:center;margin-top:2.5rem;padding:1rem 0;border-top:2px solid #e2e8f0;font-size:.88rem}
.nb{padding:.5rem 1.1rem;border:2px solid #f59e0b;border-radius:20px;color:#b45309;text-decoration:none;font-weight:600;transition:all .2s}
.nb:hover{background:#f59e0b;color:#fff}
.sep{text-align:center;color:#94a3b8;font-size:.8rem;letter-spacing:.1em;margin:1.5rem 0;text-transform:uppercase}
</style>

<div class="mod-wrap">

<div class="mod-header">
  <h1>M15 — Microservices &amp; Infrastructure</h1>
  <div class="sub">
    <span class="phase-tag">Phase 6</span>
    Service architecture decisions · API Gateway &amp; service discovery · Circuit breaker &amp; bulkhead · Docker multi-stage builds · Kubernetes fundamentals · CI/CD pipelines · 12-Factor App
  </div>
</div>

<!-- Tab bar -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt('t-overview',this)">Overview</button>
  <button class="tab-btn" onclick="vt('t-comms',this)">Service Communication</button>
  <button class="tab-btn" onclick="vt('t-resilience',this)">Resilience Patterns</button>
  <button class="tab-btn" onclick="vt('t-docker',this)">Docker</button>
  <button class="tab-btn" onclick="vt('t-k8s',this)">Kubernetes</button>
  <button class="tab-btn" onclick="vt('t-cicd',this)">CI/CD</button>
  <button class="tab-btn" onclick="vt('t-12factor',this)">12-Factor App</button>
  <button class="tab-btn" onclick="vt('t-impl',this)">C Implementation</button>
  <button class="tab-btn" onclick="vt('t-labs',this)">Labs &amp; Checklist</button>
</div>

<!-- ══════════════════════════════════════════════════════════
     TAB 1 — Overview
     ══════════════════════════════════════════════════════════ -->
<div id="t-overview" class="tab-pane active">

<div class="cp p-amber">
  <div class="cp-hdr">🏗️ Monolith vs Microservices: The Real Decision</div>
  <div class="cp-body">
    The default answer is <strong>start with a monolith</strong> — specifically a <em>modular monolith</em> with clean internal boundaries. Split only when you have a concrete reason to, not because microservices are trendy.
    <br><br>
    <strong>When microservices make sense:</strong>
    <ul>
      <li><strong>Team topology:</strong> Conway's Law — your system architecture mirrors your communication structure. If you have 5 independent teams, a monolith creates coordination overhead; separate services let teams deploy independently.</li>
      <li><strong>Independent scaling:</strong> one component (e.g., image processing) needs 10× more resources than others — split it to scale independently</li>
      <li><strong>Technology heterogeneity:</strong> ML model serving needs Python, low-latency trading needs C — different services, different stacks</li>
      <li><strong>Fault isolation:</strong> a crash in recommendations shouldn't crash checkout</li>
    </ul>
    <strong>Microservices costs you must accept:</strong>
    <ul>
      <li>Network latency and reliability in every inter-service call</li>
      <li>Distributed tracing, log aggregation, and health monitoring for N services</li>
      <li>Data consistency without distributed transactions (Saga, Outbox)</li>
      <li>Deployment pipeline for each service</li>
    </ul>
  </div>
</div>

<div class="analogy">
  <strong>Analogy — Bounded Contexts (DDD):</strong><br>
  In an e-commerce domain, "Customer" means something different to the <em>Billing</em> context (credit card, payment history) vs the <em>Shipping</em> context (address, preferred carrier). Each bounded context defines its own model of "Customer" — and each maps to a microservice boundary. Crossing context boundaries requires an explicit translation (anti-corruption layer).
</div>

<div class="two-col">
  <div class="cp p-green">
    <div class="cp-hdr">🌱 Modular Monolith First</div>
    <div class="cp-body">
      Before splitting, enforce module boundaries <em>inside</em> the monolith:
      <ul style="margin:0;padding-left:1.2rem">
        <li>Each module has a <strong>public API</strong> (headers/interfaces) — no reaching into internals</li>
        <li>Modules do not share database tables across boundaries</li>
        <li>Cross-module calls are synchronous function calls — trivially refactorable to HTTP/gRPC later</li>
        <li>Modules can be extracted one at a time (Strangler Fig)</li>
      </ul>
      <div class="ins" style="margin-top:.5rem">If your monolith has clean module boundaries, extracting a service is a lift-and-shift. If it's a big ball of mud, microservices just distribute the mess over a network.</div>
    </div>
  </div>
  <div class="cp p-blue">
    <div class="cp-hdr">🪴 Strangler Fig Pattern</div>
    <div class="cp-body">
      Incrementally replace a monolith without a big-bang rewrite:
      <ol style="margin:0;padding-left:1.2rem">
        <li>Identify a bounded context to extract (e.g., Notifications)</li>
        <li>Build the new service alongside the monolith</li>
        <li>Route specific endpoints (<code>/notify/*</code>) through the API Gateway to the new service</li>
        <li>Monolith still handles everything else — both coexist</li>
        <li>Once new service is stable, remove the monolith's notification module</li>
        <li>Repeat for next module</li>
      </ol>
    </div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">📐 Phase 6 Module Map</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Module</th><th>Topic</th><th>Key Concepts</th></tr></thead>
      <tbody>
        <tr><td><strong>M15 (this)</strong></td><td>Microservices &amp; Infrastructure</td><td>Architecture decisions, API Gateway, circuit breaker, Docker, K8s, CI/CD</td></tr>
        <tr><td>M16</td><td>Service Mesh &amp; Advanced Infra</td><td>Istio/Envoy, mTLS, traffic shaping, Helm, Terraform IaC</td></tr>
      </tbody>
    </table>
    <div class="note" style="margin-top:.75rem">Prerequisites: Ph3 (Auth — JWT validation at the gateway), Ph5 (Event-Driven — async inter-service communication, Outbox pattern)</div>
  </div>
</div>

</div><!-- /t-overview -->

<!-- ══════════════════════════════════════════════════════════
     TAB 2 — Service Communication
     ══════════════════════════════════════════════════════════ -->
<div id="t-comms" class="tab-pane">

<div class="cp p-amber">
  <div class="cp-hdr">🔗 Sync vs Async Inter-Service Communication</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Dimension</th><th>Synchronous (REST/gRPC)</th><th>Asynchronous (Events/Queues)</th></tr></thead>
      <tbody>
        <tr><td>Coupling</td><td>Temporal: caller blocks until callee responds</td><td>Loose: caller fires and continues</td></tr>
        <tr><td>Latency</td><td>Fast for simple request/reply</td><td>Adds queuing delay (ms–seconds)</td></tr>
        <tr><td>Failure propagation</td><td>Downstream failure cascades upstream</td><td>Broker buffers; caller unaffected by consumer down</td></tr>
        <tr><td>Consistency</td><td>Immediate</td><td>Eventual</td></tr>
        <tr><td>Observability</td><td>Easy: request trace follows call chain</td><td>Harder: events fan out; need correlation IDs</td></tr>
        <tr><td>Best for</td><td>Queries, user-facing reads, RPC</td><td>Side effects (email, analytics, downstream processing)</td></tr>
      </tbody>
    </table>
    <div class="ins"><strong>Hybrid pattern:</strong> Use sync for the user-facing response (place order → return order ID immediately), then async for all side effects (charge payment, send confirmation, update analytics) via events.</div>
  </div>
</div>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">🌐 REST Design for Microservices</div>
    <div class="cp-body">
      <ul style="margin:0;padding-left:1.2rem">
        <li>Versioned endpoints: <code>/v1/orders</code> — never break existing consumers</li>
        <li>Idempotency keys on POST: <code>Idempotency-Key: {uuid}</code> header</li>
        <li>Pagination: cursor-based over offset (stable under inserts)</li>
        <li>Timeout headers: <code>Request-Timeout: 5000</code> — avoid indefinite waits</li>
        <li>Structured error responses: <code>{"error":"NOT_FOUND","message":"..."}</code></li>
        <li>Health endpoints: <code>/health/live</code> (process alive), <code>/health/ready</code> (dependencies healthy)</li>
      </ul>
    </div>
  </div>
  <div class="cp p-teal">
    <div class="cp-hdr">⚡ gRPC for Internal Services</div>
    <div class="cp-body">
      gRPC is preferred over REST for internal service-to-service calls:
      <ul style="margin:0;padding-left:1.2rem">
        <li><strong>Binary (Protobuf):</strong> smaller payload vs JSON, faster serialization</li>
        <li><strong>Typed contracts:</strong> <code>.proto</code> file is the source of truth — no schema drift</li>
        <li><strong>Streaming:</strong> server-side, client-side, and bidirectional streaming</li>
        <li><strong>HTTP/2:</strong> multiplexed connections, header compression</li>
        <li><strong>Code generation:</strong> auto-generated client/server stubs in any language</li>
      </ul>
      <div class="note" style="margin-top:.4rem">Use REST for external-facing APIs (browsers, third parties). Use gRPC for internal service mesh.</div>
    </div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">🚪 API Gateway Responsibilities</div>
  <div class="cp-body">
    The API Gateway is the single entry point for all client traffic. It handles cross-cutting concerns so individual services don't have to:
    <table class="t-table" style="margin-top:.5rem">
      <thead><tr><th>Responsibility</th><th>How</th></tr></thead>
      <tbody>
        <tr><td><strong>Routing</strong></td><td>Path-based: <code>/orders/*</code> → Order Service, <code>/users/*</code> → User Service</td></tr>
        <tr><td><strong>Auth offload</strong></td><td>Validate JWT at gateway; forward <code>X-User-Id</code> header to services — services trust the header</td></tr>
        <tr><td><strong>Rate limiting</strong></td><td>Token bucket per client IP or API key; return <code>429 Too Many Requests</code></td></tr>
        <tr><td><strong>SSL termination</strong></td><td>HTTPS at gateway; plain HTTP on internal network (mTLS for higher security)</td></tr>
        <tr><td><strong>Request aggregation (BFF)</strong></td><td>Backend For Frontend: gateway calls 3 services and merges response — saves mobile client from 3 round trips</td></tr>
        <tr><td><strong>Canary routing</strong></td><td>Route 5% of traffic to new service version by header/cookie — gradual rollout</td></tr>
        <tr><td><strong>Observability</strong></td><td>Add <code>X-Request-Id</code> header; log request/response at entry point</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">🔍 Service Discovery</div>
  <div class="cp-body">
    Services are ephemeral — IPs change when containers restart. Service discovery provides stable addressing.
    <div class="two-col" style="margin-top:.75rem">
      <div>
        <strong>Client-side discovery (Consul/Eureka)</strong>
        <ul style="padding-left:1.2rem">
          <li>Service registers itself with registry on startup</li>
          <li>Client queries registry → gets list of healthy instances → client-side load balances (round-robin, etc.)</li>
          <li>More control but client must implement discovery logic</li>
        </ul>
      </div>
      <div>
        <strong>Server-side discovery (AWS ALB, Kubernetes)</strong>
        <ul style="padding-left:1.2rem">
          <li>Client sends request to load balancer</li>
          <li>LB queries registry and forwards to healthy instance</li>
          <li>Client is simple; LB handles all discovery</li>
        </ul>
      </div>
    </div>
    <div style="margin-top:.5rem">
      <strong>DNS-based (Kubernetes Services)</strong>: Kubernetes injects a DNS name for every Service (<code>orders.default.svc.cluster.local</code>). kube-proxy maintains iptables rules that load-balance across healthy Pods. Client just talks to the DNS name — no discovery library needed.
    </div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">🔀 Correlation ID: Tracing Async Request Chains</div>
  <div class="cp-body">
    When a request fans out across services (sync) or events (async), a <strong>correlation ID</strong> ties all logs together:
<div class="cb"><span class="cm">/* At API Gateway: generate if not present */</span>
<span class="cs">const char</span> *corr_id = get_header(req, <span class="cv">"X-Correlation-Id"</span>);
<span class="ck">if</span> (!corr_id) corr_id = generate_uuid();
set_header(req, <span class="cv">"X-Correlation-Id"</span>, corr_id);

<span class="cm">/* Each service: propagate to outgoing calls AND log every event */</span>
log_info(<span class="cv">"correlation_id=%s action=order_placed order_id=%s"</span>,
         corr_id, order_id);

<span class="cm">/* Each event published to Kafka: embed correlation_id in headers */</span>
rd_kafka_headers_add(headers,
    <span class="cv">"correlation_id"</span>, strlen(<span class="cv">"correlation_id"</span>),
    corr_id, strlen(corr_id));</div>
    <div class="note">When debugging a production issue, search all service logs by correlation ID to reconstruct the full request timeline across service boundaries and async event chains.</div>
  </div>
</div>

</div><!-- /t-comms -->

<!-- ══════════════════════════════════════════════════════════
     TAB 3 — Resilience Patterns
     ══════════════════════════════════════════════════════════ -->
<div id="t-resilience" class="tab-pane">

<div class="cp p-amber">
  <div class="cp-hdr">⚡ Why Resilience Patterns Are Necessary</div>
  <div class="cp-body">
    In a microservices system, any service call can fail or slow down. Without resilience patterns, one slow service causes a <strong>cascade failure</strong>: upstream services pile up blocked threads waiting for the slow service → thread pool exhaustion → entire system down.
    <br><br>
    The four primary resilience patterns:
    <table class="t-table">
      <thead><tr><th>Pattern</th><th>Problem Solved</th></tr></thead>
      <tbody>
        <tr><td><strong>Timeout</strong></td><td>Don't wait forever — bound the worst case latency</td></tr>
        <tr><td><strong>Retry</strong></td><td>Transient failures (network blip) often self-resolve — retry with backoff</td></tr>
        <tr><td><strong>Circuit Breaker</strong></td><td>Stop calling a failing service — give it time to recover, fail fast to callers</td></tr>
        <tr><td><strong>Bulkhead</strong></td><td>Isolate resource pools — one slow service can't exhaust all threads</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">🔌 Circuit Breaker — State Machine</div>
  <div class="cp-body">
    Named after electrical circuit breakers that trip to prevent damage. Three states:
  </div>
</div>

<div class="diagram-box">
<span class="dg-green">┌──────────────────────────────────────────────────────────────────┐</span>
<span class="dg-green">│  CLOSED</span> (normal operation)                                        <span class="dg-green">│</span>
<span class="dg-green">│  Requests pass through. Count consecutive failures.               │</span>
<span class="dg-green">│  failure_count &gt;= threshold (e.g. 5 in 10s) → </span><span class="dg-red">OPEN</span>              <span class="dg-green">│</span>
<span class="dg-green">└──────────────────────────────────────────────────────────────────┘</span>
                             │
            failures exceed threshold
                             ▼
<span class="dg-red">┌──────────────────────────────────────────────────────────────────┐</span>
<span class="dg-red">│  OPEN</span> (fail fast)                                                 <span class="dg-red">│</span>
<span class="dg-red">│  ALL requests rejected immediately (no call to downstream).       │</span>
<span class="dg-red">│  Returns cached/fallback response or error.                       │</span>
<span class="dg-red">│  After timeout (e.g. 30s) → </span><span class="dg-amber">HALF-OPEN</span>                          <span class="dg-red">│</span>
<span class="dg-red">└──────────────────────────────────────────────────────────────────┘</span>
                             │
               recovery timeout elapsed
                             ▼
<span class="dg-amber">┌──────────────────────────────────────────────────────────────────┐</span>
<span class="dg-amber">│  HALF-OPEN</span> (probe)                                               <span class="dg-amber">│</span>
<span class="dg-amber">│  Allow N probe requests through.                                  │</span>
<span class="dg-amber">│  All probes succeed → </span><span class="dg-green">CLOSED</span>                                   <span class="dg-amber">│</span>
<span class="dg-amber">│  Any probe fails → </span><span class="dg-red">OPEN</span> (reset timer)                          <span class="dg-amber">│</span>
<span class="dg-amber">└──────────────────────────────────────────────────────────────────┘</span>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🔑 Circuit Breaker: Key Configuration Parameters</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Parameter</th><th>What It Controls</th><th>Guidance</th></tr></thead>
      <tbody>
        <tr><td><code>failure_threshold</code></td><td>N failures to trip OPEN</td><td>5–10 over a rolling window (not total)</td></tr>
        <tr><td><code>failure_rate_threshold</code></td><td>% failure rate to trip (more robust than count)</td><td>50% failure rate over last 20 requests</td></tr>
        <tr><td><code>open_timeout</code></td><td>How long to stay OPEN before probing</td><td>30s–60s, or exponential backoff</td></tr>
        <tr><td><code>half_open_max_calls</code></td><td>Max probe calls in HALF-OPEN</td><td>1–3 probes; don't flood recovering service</td></tr>
        <tr><td><code>slow_call_threshold</code></td><td>Calls slower than N ms count as failures</td><td>Set to 2× normal p99 latency</td></tr>
        <tr><td>Fallback</td><td>What to return in OPEN state</td><td>Cached response, degraded response, or structured error</td></tr>
      </tbody>
    </table>
    <div class="warn"><strong>Don't set timeouts too generously.</strong> If your circuit breaker timeout is 30s but your HTTP timeout is 60s, threads still block 30–60s before the breaker opens. Always set HTTP timeout ≤ circuit breaker slow_call_threshold.</div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr">🚢 Bulkhead Pattern</div>
  <div class="cp-body">
    Named after the watertight compartments in a ship — if one compartment floods, others are sealed off and the ship survives.
    <br><br>
    <strong>In microservices:</strong> instead of one shared thread pool for all downstream calls, create <em>separate thread pools per dependency</em>:
<div class="cb"><span class="cm">/* Thread pool bulkhead: separate pool per downstream service */</span>
<span class="cs">typedef struct</span> {
    pthread_t  threads[POOL_SIZE];
    work_queue_t queue;
    <span class="cs">const char</span>  *name;         <span class="cm">/* e.g. "payment-service" */</span>
    <span class="cs">int</span>          max_queue;     <span class="cm">/* reject if queue full */</span>
} bulkhead_pool_t;

<span class="cm">/* Separate pools: payment can be slow without blocking inventory calls */</span>
bulkhead_pool_t payment_pool  = { .name=<span class="cv">"payment"</span>,   .max_queue=<span class="cn">50</span> };
bulkhead_pool_t inventory_pool = { .name=<span class="cv">"inventory"</span>, .max_queue=<span class="cn">200</span> };</div>
    <div class="note">If Payment Service slows down and fills the payment pool queue, the system returns <code>503 Service Unavailable</code> for payment calls only. Inventory calls proceed normally — the bulkhead contains the failure.</div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">🔁 Retry with Exponential Backoff + Jitter</div>
  <div class="cp-body">
    Retries are essential for transient failures, but naive retries can cause <strong>thundering herd</strong> — hundreds of services all retry at the same second and overwhelm the recovering service.
    <br><br>
    <strong>Solution:</strong> exponential backoff + random jitter:
<div class="cb"><span class="cm">/* Retry with exponential backoff and full jitter */</span>
<span class="cs">int</span> <span class="cf">retry_with_backoff</span>(int (*fn)(<span class="cs">void</span>*), <span class="cs">void</span> *ctx,
                          <span class="cs">int</span> max_attempts, <span class="cs">int</span> base_ms) {
    <span class="ck">for</span> (<span class="cs">int</span> attempt = <span class="cn">0</span>; attempt &lt; max_attempts; attempt++) {
        <span class="ck">if</span> (fn(ctx) == <span class="cn">0</span>) <span class="ck">return</span> <span class="cn">0</span>;  <span class="cm">/* success */</span>

        <span class="ck">if</span> (attempt + <span class="cn">1</span> == max_attempts) <span class="ck">break</span>;

        <span class="cm">/* Exponential: base_ms * 2^attempt, capped at 30s */</span>
        <span class="cs">int</span> cap = base_ms * (<span class="cn">1</span> &lt;&lt; attempt);
        <span class="ck">if</span> (cap &gt; <span class="cn">30000</span>) cap = <span class="cn">30000</span>;

        <span class="cm">/* Full jitter: random in [0, cap] — spreads retries */</span>
        <span class="cs">int</span> delay = rand() % (cap + <span class="cn">1</span>);
        usleep(delay * <span class="cn">1000</span>);
    }
    <span class="ck">return</span> -<span class="cn">1</span>;  <span class="cm">/* all attempts failed */</span>
}

<span class="cm">/* Usage: retry up to 5 times, starting at 100ms base delay */</span>
retry_with_backoff(call_payment_service, &amp;ctx, <span class="cn">5</span>, <span class="cn">100</span>);</div>
    <div class="warn">Only retry <strong>idempotent</strong> operations. Never blindly retry a POST that creates a resource — you'll create duplicates. Use idempotency keys (M13) to make POSTs safe to retry.</div>
  </div>
</div>

</div><!-- /t-resilience -->

<!-- ══════════════════════════════════════════════════════════
     TAB 4 — Docker
     ══════════════════════════════════════════════════════════ -->
<div id="t-docker" class="tab-pane">

<div class="cp p-amber">
  <div class="cp-hdr">🐳 Multi-Stage Docker Build for C/C++</div>
  <div class="cp-body">
    A C binary compiled in a full build image can run in a minimal runtime image. Multi-stage builds separate compilation from runtime, dramatically reducing image size (from ~1.2GB to ~20MB):
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">📄 Dockerfile — Multi-Stage C/C++ Build</div>
  <div class="cp-body">
<div class="cb"><span class="cm"># Stage 1: Builder — compile the binary</span>
<span class="ck">FROM</span> gcc:<span class="cv">13-bookworm</span> <span class="ck">AS</span> builder

<span class="ck">WORKDIR</span> /build

<span class="cm"># Install only build dependencies</span>
<span class="ck">RUN</span> apt-get update &amp;&amp; apt-get install -y --no-install-recommends \
    librdkafka-dev      \
    libssl-dev          \
    libpq-dev           \
    cmake               \
    &amp;&amp; rm -rf /var/lib/apt/lists/*

<span class="cm"># Copy source</span>
<span class="ck">COPY</span> . .

<span class="cm"># Compile — statically link where possible for portable binary</span>
<span class="ck">RUN</span> cmake -DCMAKE_BUILD_TYPE=Release -B build . \
    &amp;&amp; cmake --build build --target order_service -j$(nproc)

<span class="cm">############################################################</span>
<span class="cm"># Stage 2: Runtime — minimal image, just the binary</span>
<span class="ck">FROM</span> debian:<span class="cv">bookworm-slim</span>

<span class="cm"># Install only runtime libraries (no compilers, headers, or build tools)</span>
<span class="ck">RUN</span> apt-get update &amp;&amp; apt-get install -y --no-install-recommends \
    librdkafka1         \
    libssl3             \
    libpq5              \
    ca-certificates     \
    &amp;&amp; rm -rf /var/lib/apt/lists/*

<span class="cm"># Security: run as non-root</span>
<span class="ck">RUN</span> useradd -r -s /bin/false appuser
<span class="ck">USER</span> appuser

<span class="ck">WORKDIR</span> /app

<span class="cm"># Copy only the compiled binary from the builder stage</span>
<span class="ck">COPY</span> --from=builder /build/build/order_service /app/order_service

<span class="cm"># ENTRYPOINT: exec form — PID 1 gets signals properly (SIGTERM for graceful shutdown)</span>
<span class="ck">ENTRYPOINT</span> [<span class="cv">"/app/order_service"</span>]

<span class="cm"># Default arguments (overridable at runtime)</span>
<span class="ck">CMD</span> [<span class="cv">"--port=8080"</span>]</div>
  </div>
</div>

<div class="two-col">
  <div class="cp p-green">
    <div class="cp-hdr">✅ Docker Best Practices</div>
    <div class="cp-body">
      <ul style="margin:0;padding-left:1.2rem">
        <li><strong>Pin image versions:</strong> <code>debian:bookworm-slim</code> not <code>debian:latest</code> — reproducible builds</li>
        <li><strong>Non-root user:</strong> <code>useradd -r</code> + <code>USER appuser</code> — container escape with root = host root</li>
        <li><strong>No secrets in image:</strong> use environment variables or secrets mounts, never <code>ARG PASSWORD</code> (visible in layers)</li>
        <li><strong>COPY specific files:</strong> <code>COPY src/ /build/src/</code> not <code>COPY . .</code> — avoids copying <code>.git</code>, local configs</li>
        <li><strong>Read-only root filesystem:</strong> <code>--read-only</code> flag — forces explicit volume mounts for writable paths</li>
        <li><strong>Health check:</strong> <code>HEALTHCHECK CMD curl -f http://localhost:8080/health/live || exit 1</code></li>
      </ul>
    </div>
  </div>
  <div class="cp p-red">
    <div class="cp-hdr">🚫 Common Docker Mistakes</div>
    <div class="cp-body">
      <ul style="margin:0;padding-left:1.2rem">
        <li>Running as root (default if no USER set)</li>
        <li>Using <code>latest</code> tag — non-deterministic; breaks reproducibility</li>
        <li>Building in a single stage — final image carries GCC, headers, build tools</li>
        <li>Putting secrets in environment variables that get logged</li>
        <li>Using CMD instead of ENTRYPOINT — <code>docker stop</code> doesn't send SIGTERM to PID 1</li>
        <li><code>apt-get update</code> without <code>&amp;&amp; apt-get install</code> in same RUN — stale layer cache</li>
        <li>Not adding a <code>.dockerignore</code> — copies <code>node_modules/</code>, <code>.git/</code>, build artifacts</li>
      </ul>
    </div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">📄 .dockerignore</div>
  <div class="cp-body">
<div class="cb"><span class="cm"># .dockerignore — keep build context small and clean</span>
.git
.gitignore
.github
build/
*.o
*.a
*.so
cmake-build-debug/
CMakeCache.txt
CMakeFiles/
.env
.env.*
*.md
docs/
tests/</div>
    <div class="note">Every byte in the build context is sent to the Docker daemon. Large build contexts (accidental <code>.git</code> inclusion) slow down every build. A good <code>.dockerignore</code> is as important as the Dockerfile itself.</div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr">🔄 ENTRYPOINT vs CMD: Graceful Shutdown</div>
  <div class="cp-body">
    When Kubernetes sends SIGTERM (graceful shutdown), the signal goes to <strong>PID 1</strong> in the container. If your process is not PID 1, it never receives SIGTERM and gets hard-killed after <code>terminationGracePeriodSeconds</code>.
    <br><br>
    <table class="t-table">
      <thead><tr><th>Form</th><th>Shell</th><th>PID 1</th><th>Gets SIGTERM?</th></tr></thead>
      <tbody>
        <tr><td><code>ENTRYPOINT ["/app/service"]</code> (exec)</td><td>No</td><td>Your binary</td><td>✅ Yes</td></tr>
        <tr><td><code>ENTRYPOINT /app/service</code> (shell)</td><td>/bin/sh -c</td><td>sh</td><td>❌ No (sh is PID 1)</td></tr>
        <tr><td><code>CMD ["/app/service"]</code> (exec)</td><td>No</td><td>Your binary</td><td>✅ Yes (if no ENTRYPOINT)</td></tr>
      </tbody>
    </table>
    <div class="ins">Always use exec form: <code>ENTRYPOINT ["/app/service"]</code>. In your C process, register a SIGTERM handler that drains connections and exits cleanly.</div>
  </div>
</div>

</div><!-- /t-docker -->

<!-- ══════════════════════════════════════════════════════════
     TAB 5 — Kubernetes
     ══════════════════════════════════════════════════════════ -->
<div id="t-k8s" class="tab-pane">

<div class="cp p-amber">
  <div class="cp-hdr">☸️ Kubernetes Core Objects</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Object</th><th>Purpose</th><th>Key Fields</th></tr></thead>
      <tbody>
        <tr><td><strong>Pod</strong></td><td>Smallest deployable unit: one or more containers sharing network/storage</td><td><code>spec.containers[].image</code>, <code>resources</code>, <code>env</code></td></tr>
        <tr><td><strong>Deployment</strong></td><td>Declares desired state: N replicas of a Pod template; manages rolling updates and rollback</td><td><code>spec.replicas</code>, <code>spec.strategy</code>, <code>spec.template</code></td></tr>
        <tr><td><strong>Service</strong></td><td>Stable DNS name + ClusterIP that load-balances across matching Pods (by label selector)</td><td><code>spec.selector</code>, <code>spec.ports</code>, <code>spec.type</code></td></tr>
        <tr><td><strong>Ingress</strong></td><td>HTTP/S routing rules: hostname/path → Service; TLS termination</td><td><code>spec.rules[].host</code>, <code>spec.tls</code></td></tr>
        <tr><td><strong>ConfigMap</strong></td><td>Non-sensitive configuration: mounted as env vars or files</td><td><code>data</code> key-value pairs</td></tr>
        <tr><td><strong>Secret</strong></td><td>Sensitive data (passwords, tokens): base64-encoded, encrypted at rest</td><td><code>data</code> (base64), <code>type</code></td></tr>
        <tr><td><strong>HPA</strong></td><td>Horizontal Pod Autoscaler: scales replicas based on CPU/memory/custom metrics</td><td><code>spec.minReplicas</code>, <code>spec.maxReplicas</code>, <code>spec.metrics</code></td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">📄 Kubernetes Deployment — C Service Example</div>
  <div class="cp-body">
<div class="cb"><span class="cm"># order-service Deployment + Service</span>
<span class="ck">apiVersion</span>: <span class="cv">apps/v1</span>
<span class="ck">kind</span>: <span class="cv">Deployment</span>
<span class="ck">metadata</span>:
  <span class="ck">name</span>: <span class="cv">order-service</span>
  <span class="ck">labels</span>:
    <span class="ck">app</span>: <span class="cv">order-service</span>
<span class="ck">spec</span>:
  <span class="ck">replicas</span>: <span class="cn">3</span>
  <span class="ck">selector</span>:
    <span class="ck">matchLabels</span>:
      <span class="ck">app</span>: <span class="cv">order-service</span>
  <span class="ck">strategy</span>:
    <span class="ck">type</span>: <span class="cv">RollingUpdate</span>
    <span class="ck">rollingUpdate</span>:
      <span class="ck">maxUnavailable</span>: <span class="cn">1</span>      <span class="cm"># at most 1 Pod down during update</span>
      <span class="ck">maxSurge</span>: <span class="cn">1</span>           <span class="cm"># at most 1 extra Pod during update</span>
  <span class="ck">template</span>:
    <span class="ck">metadata</span>:
      <span class="ck">labels</span>:
        <span class="ck">app</span>: <span class="cv">order-service</span>
    <span class="ck">spec</span>:
      <span class="ck">containers</span>:
      - <span class="ck">name</span>: <span class="cv">order-service</span>
        <span class="ck">image</span>: <span class="cv">registry.example.com/order-service:1.4.2</span>
        <span class="ck">ports</span>:
        - <span class="ck">containerPort</span>: <span class="cn">8080</span>
        <span class="ck">env</span>:
        - <span class="ck">name</span>: <span class="cv">DATABASE_URL</span>
          <span class="ck">valueFrom</span>:
            <span class="ck">secretKeyRef</span>:
              <span class="ck">name</span>: <span class="cv">order-service-secrets</span>
              <span class="ck">key</span>: <span class="cv">database_url</span>
        - <span class="ck">name</span>: <span class="cv">KAFKA_BROKERS</span>
          <span class="ck">valueFrom</span>:
            <span class="ck">configMapKeyRef</span>:
              <span class="ck">name</span>: <span class="cv">order-service-config</span>
              <span class="ck">key</span>: <span class="cv">kafka_brokers</span>
        <span class="ck">resources</span>:
          <span class="ck">requests</span>:
            <span class="ck">cpu</span>: <span class="cv">"100m"</span>     <span class="cm"># 0.1 CPU cores guaranteed</span>
            <span class="ck">memory</span>: <span class="cv">"64Mi"</span>
          <span class="ck">limits</span>:
            <span class="ck">cpu</span>: <span class="cv">"500m"</span>     <span class="cm"># burst up to 0.5 CPU</span>
            <span class="ck">memory</span>: <span class="cv">"256Mi"</span>  <span class="cm"># OOM-killed if exceeded</span>
        <span class="ck">livenessProbe</span>:
          <span class="ck">httpGet</span>:
            <span class="ck">path</span>: <span class="cv">/health/live</span>
            <span class="ck">port</span>: <span class="cn">8080</span>
          <span class="ck">initialDelaySeconds</span>: <span class="cn">5</span>
          <span class="ck">periodSeconds</span>: <span class="cn">10</span>
          <span class="ck">failureThreshold</span>: <span class="cn">3</span>   <span class="cm"># restart after 3 consecutive failures</span>
        <span class="ck">readinessProbe</span>:
          <span class="ck">httpGet</span>:
            <span class="ck">path</span>: <span class="cv">/health/ready</span>
            <span class="ck">port</span>: <span class="cn">8080</span>
          <span class="ck">initialDelaySeconds</span>: <span class="cn">3</span>
          <span class="ck">periodSeconds</span>: <span class="cn">5</span>
          <span class="ck">failureThreshold</span>: <span class="cn">2</span>   <span class="cm"># remove from LB after 2 failures</span>
        <span class="ck">terminationGracePeriodSeconds</span>: <span class="cn">30</span>
---
<span class="ck">apiVersion</span>: <span class="cv">v1</span>
<span class="ck">kind</span>: <span class="cv">Service</span>
<span class="ck">metadata</span>:
  <span class="ck">name</span>: <span class="cv">order-service</span>
<span class="ck">spec</span>:
  <span class="ck">selector</span>:
    <span class="ck">app</span>: <span class="cv">order-service</span>
  <span class="ck">ports</span>:
  - <span class="ck">port</span>: <span class="cn">80</span>
    <span class="ck">targetPort</span>: <span class="cn">8080</span></div>
  </div>
</div>

<div class="two-col">
  <div class="cp p-green">
    <div class="cp-hdr">💓 Liveness vs Readiness Probes</div>
    <div class="cp-body">
      <table class="t-table">
        <thead><tr><th>Probe</th><th>Failure Action</th><th>Purpose</th></tr></thead>
        <tbody>
          <tr><td><strong>Liveness</strong></td><td>Restart the container</td><td>Is the process alive? (Detects deadlocks, infinite loops)</td></tr>
          <tr><td><strong>Readiness</strong></td><td>Remove from Service endpoints (stops traffic)</td><td>Is the process ready to serve? (DB connected, cache warm)</td></tr>
          <tr><td><strong>Startup</strong></td><td>Restart if not ready within window</td><td>Slow-starting apps — disables liveness until startup complete</td></tr>
        </tbody>
      </table>
      <div class="warn" style="margin-top:.4rem">Never make readiness probe depend on external services. If Payment Service is down, you don't want all Order Service pods removed from load balancing — implement graceful degradation instead.</div>
    </div>
  </div>
  <div class="cp p-teal">
    <div class="cp-hdr">🚀 Rolling Updates &amp; Rollback</div>
    <div class="cp-body">
      <ul style="margin:0;padding-left:1.2rem">
        <li>Update image: <code>kubectl set image deployment/order-service order-service=registry.example.com/order-service:1.4.3</code></li>
        <li>Monitor rollout: <code>kubectl rollout status deployment/order-service</code></li>
        <li>Rollback to previous: <code>kubectl rollout undo deployment/order-service</code></li>
        <li>Rollback to specific revision: <code>kubectl rollout undo deployment/order-service --to-revision=2</code></li>
      </ul>
      <div class="note" style="margin-top:.4rem"><strong>Pod Disruption Budget:</strong> <code>minAvailable: 2</code> — cluster autoscaler and rolling updates respect this; never takes down so many pods that fewer than 2 are available.</div>
    </div>
  </div>
</div>

</div><!-- /t-k8s -->

<!-- ══════════════════════════════════════════════════════════
     TAB 6 — CI/CD
     ══════════════════════════════════════════════════════════ -->
<div id="t-cicd" class="tab-pane">

<div class="cp p-amber">
  <div class="cp-hdr">🔄 CI/CD Pipeline Stages</div>
  <div class="cp-body">
    A complete pipeline runs on every commit and gates production deployment behind automated quality checks:
  </div>
</div>

<ul class="flow-list">
  <li class="fl-step"><div class="fl-num">1</div><div><strong>Lint &amp; Static Analysis</strong> — clang-tidy, cppcheck, clang-format check. Fail fast: bad code never reaches tests. (~30s)</div></li>
  <li class="fl-step"><div class="fl-num">2</div><div><strong>Unit Tests</strong> — fast, isolated tests with mocked dependencies. Target: &gt;80% coverage on core business logic. (~2m)</div></li>
  <li class="fl-step"><div class="fl-num">3</div><div><strong>Integration Tests</strong> — spin up Postgres, Kafka, Redis via Docker Compose; test real service behavior against real dependencies. (~5m)</div></li>
  <li class="fl-step"><div class="fl-num">4</div><div><strong>Security Scan</strong> — Trivy scans for CVEs in base image and dependencies; Semgrep for security antipatterns in code. Block on HIGH/CRITICAL CVEs.</div></li>
  <li class="fl-step"><div class="fl-num">5</div><div><strong>Build OCI Image</strong> — multi-stage Docker build. Tag with git SHA: <code>registry/service:abc1234</code>. SHA tags are immutable — never use <code>:latest</code> in production.</div></li>
  <li class="fl-step"><div class="fl-num">6</div><div><strong>Push to Registry</strong> — push to container registry. Sign image with cosign for supply chain security.</div></li>
  <li class="fl-step"><div class="fl-num">7</div><div><strong>Deploy to Staging</strong> — <code>kubectl set image</code> or Helm upgrade. Run smoke tests against staging URL.</div></li>
  <li class="fl-step"><div class="fl-num">8</div><div><strong>Deploy to Production</strong> — manual approval gate (or auto on green staging). Blue-green or canary rollout. Monitor error rate + latency for 10 minutes.</div></li>
</ul>

<div class="two-col">
  <div class="cp p-green">
    <div class="cp-hdr">🟢🔵 Blue-Green Deployment</div>
    <div class="cp-body">
      Maintain two identical environments (blue = current, green = new):
      <ol style="margin:0;padding-left:1.2rem">
        <li>Deploy new version to green environment</li>
        <li>Run smoke tests on green (not receiving production traffic)</li>
        <li>Switch load balancer to point to green (instant cutover)</li>
        <li>Blue environment kept running for instant rollback</li>
        <li>After confidence period, decommission blue</li>
      </ol>
      <strong>Pros:</strong> zero-downtime, instant rollback<br>
      <strong>Cons:</strong> requires 2× infrastructure during transition
    </div>
  </div>
  <div class="cp p-blue">
    <div class="cp-hdr">🐦 Canary Deployment</div>
    <div class="cp-body">
      Route a small percentage of traffic to new version first:
      <ol style="margin:0;padding-left:1.2rem">
        <li>Deploy new version alongside old; route 5% of traffic to it</li>
        <li>Monitor error rate, latency, business metrics (conversion rate)</li>
        <li>If healthy after 10m: increase to 20% → 50% → 100%</li>
        <li>If issues: instant rollback by routing 100% back to old version</li>
      </ol>
      <strong>Pros:</strong> real production traffic validation, minimal blast radius<br>
      <strong>Cons:</strong> two versions run simultaneously — must be API-compatible
    </div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">📄 GitHub Actions Example — C Service CI Pipeline</div>
  <div class="cp-body">
<div class="cb"><span class="cm"># .github/workflows/ci.yml</span>
<span class="ck">name</span>: <span class="cv">CI</span>
<span class="ck">on</span>:
  <span class="ck">push</span>:
    <span class="ck">branches</span>: [<span class="cv">main</span>]
  <span class="ck">pull_request</span>:

<span class="ck">jobs</span>:
  <span class="ck">build-test</span>:
    <span class="ck">runs-on</span>: <span class="cv">ubuntu-latest</span>
    <span class="ck">services</span>:
      <span class="ck">postgres</span>:
        <span class="ck">image</span>: <span class="cv">postgres:16</span>
        <span class="ck">env</span>:
          <span class="ck">POSTGRES_PASSWORD</span>: <span class="cv">test</span>
          <span class="ck">POSTGRES_DB</span>: <span class="cv">testdb</span>
        <span class="ck">options</span>: <span class="cv">&gt;-
          --health-cmd pg_isready
          --health-interval 10s</span>
    <span class="ck">steps</span>:
    - <span class="ck">uses</span>: <span class="cv">actions/checkout@v4</span>
    - <span class="ck">name</span>: <span class="cv">Install dependencies</span>
      <span class="ck">run</span>: <span class="cv">|
        sudo apt-get update
        sudo apt-get install -y libpq-dev librdkafka-dev clang-tidy cppcheck</span>
    - <span class="ck">name</span>: <span class="cv">Configure</span>
      <span class="ck">run</span>: <span class="cv">cmake -B build -DCMAKE_BUILD_TYPE=Debug -DENABLE_TESTS=ON</span>
    - <span class="ck">name</span>: <span class="cv">Build</span>
      <span class="ck">run</span>: <span class="cv">cmake --build build -j$(nproc)</span>
    - <span class="ck">name</span>: <span class="cv">Lint</span>
      <span class="ck">run</span>: <span class="cv">clang-tidy src/*.c -- -Iinclude</span>
    - <span class="ck">name</span>: <span class="cv">Unit tests</span>
      <span class="ck">run</span>: <span class="cv">./build/tests/unit_tests</span>
    - <span class="ck">name</span>: <span class="cv">Integration tests</span>
      <span class="ck">env</span>:
        <span class="ck">DATABASE_URL</span>: <span class="cv">postgres://postgres:test@localhost/testdb</span>
      <span class="ck">run</span>: <span class="cv">./build/tests/integration_tests</span>

  <span class="ck">docker-build</span>:
    <span class="ck">needs</span>: <span class="cv">build-test</span>
    <span class="ck">runs-on</span>: <span class="cv">ubuntu-latest</span>
    <span class="ck">if</span>: <span class="cv">github.ref == 'refs/heads/main'</span>
    <span class="ck">steps</span>:
    - <span class="ck">uses</span>: <span class="cv">actions/checkout@v4</span>
    - <span class="ck">name</span>: <span class="cv">Build and push image</span>
      <span class="ck">run</span>: <span class="cv">|
        docker build -t registry.example.com/order-service:${{ github.sha }} .
        docker push registry.example.com/order-service:${{ github.sha }}</span>
    - <span class="ck">name</span>: <span class="cv">Deploy to staging</span>
      <span class="ck">run</span>: <span class="cv">|
        kubectl set image deployment/order-service \
          order-service=registry.example.com/order-service:${{ github.sha }}
        kubectl rollout status deployment/order-service --timeout=5m</span></div>
  </div>
</div>

</div><!-- /t-cicd -->

<!-- ══════════════════════════════════════════════════════════
     TAB 7 — 12-Factor App
     ══════════════════════════════════════════════════════════ -->
<div id="t-12factor" class="tab-pane">

<div class="cp p-amber">
  <div class="cp-hdr">📋 The 12-Factor App Methodology</div>
  <div class="cp-body">
    A methodology for building software-as-a-service apps that are portable, scalable, and maintainable. Originally from Heroku — now the standard for cloud-native services.
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">🔑 The 12 Factors (Microservices-Relevant Highlights)</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>#</th><th>Factor</th><th>Rule</th><th>C Implementation</th></tr></thead>
      <tbody>
        <tr><td>1</td><td><strong>Codebase</strong></td><td>One codebase per service, tracked in version control</td><td>One git repo per service; <code>main</code> deploys to production</td></tr>
        <tr><td>2</td><td><strong>Dependencies</strong></td><td>Declare and isolate all dependencies explicitly</td><td>CMakeLists.txt pins exact library versions; no implicit system libraries</td></tr>
        <tr><td>3</td><td><strong>Config</strong></td><td>Config in environment, not in code</td><td><code>getenv("DATABASE_URL")</code> — never hardcode DSN/passwords</td></tr>
        <tr><td>4</td><td><strong>Backing Services</strong></td><td>Treat DB, cache, broker as attached resources</td><td>URL from env — swap Postgres for RDS without code change</td></tr>
        <tr><td>6</td><td><strong>Processes</strong></td><td>Execute app as one or more stateless processes</td><td>No in-process session state; sessions in Redis</td></tr>
        <tr><td>7</td><td><strong>Port Binding</strong></td><td>Export services via port binding, not app server injection</td><td>Service binds <code>$PORT</code> itself; Kubernetes routes to it</td></tr>
        <tr><td>8</td><td><strong>Concurrency</strong></td><td>Scale out via the process model</td><td>Multiple replicas (K8s <code>replicas: N</code>), not threads-per-monolith</td></tr>
        <tr><td>9</td><td><strong>Disposability</strong></td><td>Maximize robustness with fast startup and graceful shutdown</td><td>Handle SIGTERM: drain connections, flush buffers, exit 0</td></tr>
        <tr><td>11</td><td><strong>Logs</strong></td><td>Treat logs as event streams — write to stdout</td><td><code>fprintf(stdout, "...")</code> — never write to files inside container</td></tr>
        <tr><td>12</td><td><strong>Admin Processes</strong></td><td>Run admin/management tasks as one-off processes</td><td>DB migrations as a separate Job (Kubernetes Job), not in service startup</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">⚙️ Factor 3: Config via Environment</div>
    <div class="cp-body">
<div class="cb"><span class="cm">/* Never do this: */</span>
<span class="cs">const char</span> *db_url = <span class="cv">"postgres://prod-db:5432/app"</span>;

<span class="cm">/* Do this: */</span>
<span class="cs">const char</span> *db_url = getenv(<span class="cv">"DATABASE_URL"</span>);
<span class="ck">if</span> (!db_url) {
    fprintf(stderr, <span class="cv">"DATABASE_URL not set\n"</span>);
    exit(<span class="cn">1</span>);
}</div>
      Config that varies between environments (dev/staging/prod) must never be in code. The same binary runs in all environments — only the environment variables differ.
    </div>
  </div>
  <div class="cp p-teal">
    <div class="cp-hdr">🔄 Factor 9: Graceful Shutdown in C</div>
    <div class="cp-body">
<div class="cb"><span class="cs">static volatile</span> <span class="cs">int</span> shutting_down = <span class="cn">0</span>;

<span class="ck">static void</span> <span class="cf">handle_sigterm</span>(<span class="cs">int</span> sig) {
    (void)sig;
    shutting_down = <span class="cn">1</span>;
}

<span class="cs">int</span> <span class="cf">main</span>() {
    signal(SIGTERM, handle_sigterm);
    signal(SIGINT, handle_sigterm);

    <span class="ck">while</span> (!shutting_down) {
        <span class="cm">/* serve requests */</span>
    }

    <span class="cm">/* Graceful shutdown: drain connections */</span>
    drain_active_connections();
    rd_kafka_flush(rk, <span class="cn">10000</span>);  <span class="cm">/* flush pending events */</span>
    PQfinish(pg_conn);
    fprintf(stdout, <span class="cv">"Shutdown complete\n"</span>);
    <span class="ck">return</span> <span class="cn">0</span>;
}</div>
    </div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">📊 Factor 11: Structured Logs to stdout</div>
  <div class="cp-body">
    Write logs as structured JSON to stdout. The container runtime captures stdout and forwards to your log aggregation platform (ELK, Loki, Datadog).
<div class="cb"><span class="cm">/* Structured JSON logging */</span>
<span class="ck">#define</span> LOG_INFO(fmt, ...) \
    fprintf(stdout, \
        <span class="cv">"{\"level\":\"INFO\",\"ts\":\"%.3f\",\"msg\":\""</span> fmt <span class="cv">"\"}\n"</span>, \
        get_unix_ms(), ##__VA_ARGS__)

<span class="cm">/* Usage */</span>
LOG_INFO(<span class="cv">"order_placed order_id=%s user_id=%s amount=%.2f"</span>,
         order_id, user_id, amount);</div>
    <div class="ins">Include in every log line: <code>timestamp</code>, <code>level</code>, <code>service</code>, <code>correlation_id</code>, and the event. This makes logs searchable and correlatable across services in your log aggregator.</div>
  </div>
</div>

</div><!-- /t-12factor -->

<!-- ══════════════════════════════════════════════════════════
     TAB 8 — C Implementation
     ══════════════════════════════════════════════════════════ -->
<div id="t-impl" class="tab-pane">

<div class="sep">── Implementation 1 — Circuit Breaker (Thread-Safe, C11 Atomics) ──</div>

<div class="cp p-amber">
  <div class="cp-hdr">🔌 Circuit Breaker in C (stdatomic, three-state machine)</div>
  <div class="cp-body">
<div class="cb"><span class="cm">/* circuit_breaker.h — thread-safe circuit breaker */</span>
<span class="cs">#pragma once</span>
<span class="cs">#include</span> &lt;stdatomic.h&gt;
<span class="cs">#include</span> &lt;time.h&gt;
<span class="cs">#include</span> &lt;stdbool.h&gt;

<span class="cs">typedef enum</span> { CB_CLOSED, CB_OPEN, CB_HALF_OPEN } cb_state_t;

<span class="cs">typedef struct</span> {
    _Atomic(<span class="cs">int</span>)         state;          <span class="cm">/* cb_state_t */</span>
    _Atomic(<span class="cs">int</span>)         failure_count;
    _Atomic(<span class="cs">long</span>)        open_since_ms;  <span class="cm">/* epoch ms when opened */</span>
    <span class="cs">int</span>                  failure_threshold;
    <span class="cs">long</span>                 open_timeout_ms;
} circuit_breaker_t;

<span class="ck">static inline</span> <span class="cs">long</span> <span class="cf">now_ms</span>(<span class="cs">void</span>) {
    <span class="cs">struct timespec</span> ts;
    clock_gettime(CLOCK_MONOTONIC, &amp;ts);
    <span class="ck">return</span> ts.tv_sec * <span class="cn">1000LL</span> + ts.tv_nsec / <span class="cn">1000000LL</span>;
}

<span class="ck">static inline</span> <span class="cs">void</span> <span class="cf">cb_init</span>(circuit_breaker_t *cb,
                              <span class="cs">int</span> threshold, <span class="cs">long</span> timeout_ms) {
    atomic_store(&amp;cb-&gt;state,         CB_CLOSED);
    atomic_store(&amp;cb-&gt;failure_count, <span class="cn">0</span>);
    atomic_store(&amp;cb-&gt;open_since_ms, <span class="cn">0</span>);
    cb-&gt;failure_threshold = threshold;
    cb-&gt;open_timeout_ms   = timeout_ms;
}

<span class="cm">/* Returns true if the call should be allowed through */</span>
<span class="ck">static inline</span> <span class="cs">bool</span> <span class="cf">cb_allow</span>(circuit_breaker_t *cb) {
    <span class="cs">int</span> state = atomic_load(&amp;cb-&gt;state);

    <span class="ck">if</span> (state == CB_CLOSED) <span class="ck">return</span> <span class="cn">true</span>;

    <span class="ck">if</span> (state == CB_OPEN) {
        <span class="cs">long</span> elapsed = now_ms() - atomic_load(&amp;cb-&gt;open_since_ms);
        <span class="ck">if</span> (elapsed &gt;= cb-&gt;open_timeout_ms) {
            <span class="cm">/* Transition to HALF_OPEN to probe recovery */</span>
            <span class="cs">int</span> expected = CB_OPEN;
            <span class="ck">if</span> (atomic_compare_exchange_strong(&amp;cb-&gt;state,
                                               &amp;expected, CB_HALF_OPEN)) {
                <span class="ck">return</span> <span class="cn">true</span>;  <span class="cm">/* this thread gets the probe request */</span>
            }
        }
        <span class="ck">return</span> <span class="cn">false</span>;  <span class="cm">/* still open */</span>
    }

    <span class="cm">/* HALF_OPEN: allow one probe at a time */</span>
    <span class="ck">return</span> <span class="cn">true</span>;
}

<span class="ck">static inline</span> <span class="cs">void</span> <span class="cf">cb_on_success</span>(circuit_breaker_t *cb) {
    <span class="cs">int</span> state = atomic_load(&amp;cb-&gt;state);
    <span class="ck">if</span> (state == CB_HALF_OPEN) {
        <span class="cm">/* Recovery confirmed: close the breaker */</span>
        atomic_store(&amp;cb-&gt;failure_count, <span class="cn">0</span>);
        atomic_store(&amp;cb-&gt;state, CB_CLOSED);
    }
    <span class="ck">if</span> (state == CB_CLOSED) {
        <span class="cm">/* Reset failure count on success */</span>
        atomic_store(&amp;cb-&gt;failure_count, <span class="cn">0</span>);
    }
}

<span class="ck">static inline</span> <span class="cs">void</span> <span class="cf">cb_on_failure</span>(circuit_breaker_t *cb) {
    <span class="cs">int</span> state = atomic_load(&amp;cb-&gt;state);
    <span class="ck">if</span> (state == CB_HALF_OPEN) {
        <span class="cm">/* Probe failed: reopen the breaker */</span>
        atomic_store(&amp;cb-&gt;open_since_ms, now_ms());
        atomic_store(&amp;cb-&gt;state, CB_OPEN);
        <span class="ck">return</span>;
    }
    <span class="cs">int</span> count = atomic_fetch_add(&amp;cb-&gt;failure_count, <span class="cn">1</span>) + <span class="cn">1</span>;
    <span class="ck">if</span> (count &gt;= cb-&gt;failure_threshold) {
        <span class="cs">int</span> expected = CB_CLOSED;
        <span class="ck">if</span> (atomic_compare_exchange_strong(&amp;cb-&gt;state, &amp;expected, CB_OPEN)) {
            atomic_store(&amp;cb-&gt;open_since_ms, now_ms());
            fprintf(stderr, <span class="cv">"[CB] Circuit OPENED after %d failures\n"</span>, count);
        }
    }
}

<span class="cm">/* Usage */</span>
<span class="cs">int</span> <span class="cf">call_payment_service</span>(<span class="cs">void</span> *ctx) { <span class="ck">return</span> <span class="cn">0</span>; } <span class="cm">/* placeholder */</span>

circuit_breaker_t payment_cb;

<span class="cs">int</span> <span class="cf">charge_customer</span>(<span class="cs">const char</span> *order_id, <span class="cs">double</span> amount) {
    <span class="ck">if</span> (!cb_allow(&amp;payment_cb)) {
        fprintf(stderr, <span class="cv">"[CB] OPEN: payment service unavailable\n"</span>);
        <span class="ck">return</span> -<span class="cn">1</span>;  <span class="cm">/* fail fast */</span>
    }

    <span class="cs">int</span> result = call_payment_service(NULL);
    <span class="ck">if</span> (result == <span class="cn">0</span>)
        cb_on_success(&amp;payment_cb);
    <span class="ck">else</span>
        cb_on_failure(&amp;payment_cb);

    <span class="ck">return</span> result;
}</div>
  </div>
</div>

<div class="sep">── Implementation 2 — Health Check HTTP Server ──</div>

<div class="cp p-green">
  <div class="cp-hdr">💓 Minimal Health Check HTTP Server (POSIX sockets)</div>
  <div class="cp-body">
<div class="cb"><span class="cm">/* health.c — minimal HTTP health check endpoint for Kubernetes probes */</span>
<span class="cs">#include</span> &lt;sys/socket.h&gt;
<span class="cs">#include</span> &lt;netinet/in.h&gt;
<span class="cs">#include</span> &lt;pthread.h&gt;
<span class="cs">#include</span> &lt;string.h&gt;
<span class="cs">#include</span> &lt;unistd.h&gt;
<span class="cs">#include</span> &lt;stdio.h&gt;

<span class="cs">static volatile</span> <span class="cs">int</span> ready = <span class="cn">0</span>;  <span class="cm">/* set to 1 once DB connected etc. */</span>

<span class="ck">static void</span> *<span class="cf">health_thread</span>(<span class="cs">void</span> *arg) {
    (void)arg;
    <span class="cs">int</span> srv = socket(AF_INET, SOCK_STREAM, <span class="cn">0</span>);
    <span class="cs">int</span> opt = <span class="cn">1</span>;
    setsockopt(srv, SOL_SOCKET, SO_REUSEADDR, &amp;opt, <span class="ck">sizeof</span>(opt));

    <span class="cs">struct sockaddr_in</span> addr = {
        .sin_family = AF_INET,
        .sin_addr.s_addr = INADDR_ANY,
        .sin_port = htons(<span class="cn">8081</span>)
    };
    bind(srv, (<span class="cs">struct sockaddr</span> *)&amp;addr, <span class="ck">sizeof</span>(addr));
    listen(srv, <span class="cn">16</span>);

    <span class="ck">while</span> (<span class="cn">1</span>) {
        <span class="cs">int</span> conn = accept(srv, NULL, NULL);
        <span class="ck">if</span> (conn &lt; <span class="cn">0</span>) <span class="ck">continue</span>;

        <span class="cs">char</span> buf[<span class="cn">256</span>];
        ssize_t n = recv(conn, buf, <span class="ck">sizeof</span>(buf) - <span class="cn">1</span>, <span class="cn">0</span>);
        buf[n > <span class="cn">0</span> ? n : <span class="cn">0</span>] = <span class="cn">'\0'</span>;

        <span class="cs">const char</span> *resp;
        <span class="ck">if</span> (strstr(buf, <span class="cv">"GET /health/live"</span>)) {
            resp = <span class="cv">"HTTP/1.1 200 OK\r\nContent-Length:2\r\n\r\nOK"</span>;
        } <span class="ck">else if</span> (strstr(buf, <span class="cv">"GET /health/ready"</span>)) {
            resp = ready
                ? <span class="cv">"HTTP/1.1 200 OK\r\nContent-Length:5\r\n\r\nREADY"</span>
                : <span class="cv">"HTTP/1.1 503 Service Unavailable\r\nContent-Length:12\r\n\r\nNOT_READY_YET"</span>;
        } <span class="ck">else</span> {
            resp = <span class="cv">"HTTP/1.1 404 Not Found\r\nContent-Length:0\r\n\r\n"</span>;
        }

        send(conn, resp, strlen(resp), <span class="cn">0</span>);
        close(conn);
    }
    <span class="ck">return</span> NULL;
}

<span class="cs">void</span> <span class="cf">start_health_server</span>(<span class="cs">void</span>) {
    pthread_t t;
    pthread_create(&amp;t, NULL, health_thread, NULL);
    pthread_detach(t);
}

<span class="cs">void</span> <span class="cf">set_ready</span>(<span class="cs">int</span> r) { ready = r; }</div>
    <div class="note">Start the health server before connecting to databases so the <code>/health/live</code> probe succeeds immediately. Set <code>ready=1</code> only after all dependencies (DB, Kafka) are connected — this keeps the pod out of the Service load balancer until it's actually ready.</div>
  </div>
</div>

</div><!-- /t-impl -->

<!-- ══════════════════════════════════════════════════════════
     TAB 9 — Labs & Checklist
     ══════════════════════════════════════════════════════════ -->
<div id="t-labs" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 1 — Circuit Breaker Under Load</div>
  <div class="lab-body">
    Observe circuit breaker state transitions under real failure conditions.
    <div class="lab-step"><span class="sn">1</span> Build the circuit breaker from Tab 8. Write a test harness that calls a "downstream service" function that returns success/failure based on a configurable failure rate.</div>
    <div class="lab-step"><span class="sn">2</span> Run 100 concurrent goroutine-equivalent threads (using pthreads) calling the circuit breaker simultaneously. Set failure rate to 80%.</div>
    <div class="lab-step"><span class="sn">3</span> Observe and log state transitions: CLOSED → OPEN (trip after N failures) → HALF-OPEN (after timeout) → CLOSED (after probe success).</div>
    <div class="lab-step"><span class="sn">4</span> Measure: in OPEN state, what is the p99 response time? (Should be microseconds — fail fast.) Compare to CLOSED state with real downstream calls.</div>
    <div class="lab-step"><span class="sn">5</span> <strong>Bonus:</strong> add a sliding window failure rate threshold (failure rate over last 20 calls, not just a count) and verify it's more resilient to bursty failures.</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 2 — Docker Multi-Stage Build: Size Comparison</div>
  <div class="lab-body">
    Demonstrate the image size impact of multi-stage builds.
    <div class="lab-step"><span class="sn">1</span> Write a simple C HTTP server (or use the health server from Tab 8). Compile it manually to confirm it works.</div>
    <div class="lab-step"><span class="sn">2</span> Write a single-stage Dockerfile using <code>FROM gcc:13</code>. Build it: <code>docker build -t service:single-stage .</code>. Check size: <code>docker image ls service:single-stage</code>.</div>
    <div class="lab-step"><span class="sn">3</span> Write the multi-stage Dockerfile from Tab 4. Build it: <code>docker build -t service:multi-stage .</code>. Compare sizes.</div>
    <div class="lab-step"><span class="sn">4</span> Run <code>docker run --rm service:multi-stage</code>. Verify the binary executes correctly in the slim image.</div>
    <div class="lab-step"><span class="sn">5</span> Run <code>docker history service:multi-stage</code> — verify no build tools (gcc, make) appear in any layer of the final image.</div>
    <div class="lab-step"><span class="sn">6</span> Run <code>docker run --user $(id -u) service:multi-stage</code> — verify non-root execution. Check process inside container: <code>docker exec &lt;id&gt; id</code>.</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 3 — Kubernetes Deployment with Probes</div>
  <div class="lab-body">
    Deploy the C service to a local Kubernetes cluster (minikube or kind).
    <div class="lab-step"><span class="sn">1</span> Build and push the Docker image to a local registry: <code>minikube image load service:multi-stage</code>.</div>
    <div class="lab-step"><span class="sn">2</span> Apply the Deployment from Tab 5. Watch pods come up: <code>kubectl get pods -w</code>.</div>
    <div class="lab-step"><span class="sn">3</span> Observe readiness probe in action: modify the service to delay setting <code>ready=1</code> by 10 seconds. Watch the pod stay NotReady during startup.</div>
    <div class="lab-step"><span class="sn">4</span> Trigger a liveness probe failure: modify the <code>/health/live</code> endpoint to return 503 after receiving 5 requests. Observe Kubernetes restart the pod.</div>
    <div class="lab-step"><span class="sn">5</span> Perform a rolling update: rebuild with a different version tag, apply the new image. Watch rolling update: <code>kubectl rollout status deployment/order-service</code>.</div>
    <div class="lab-step"><span class="sn">6</span> Rollback: <code>kubectl rollout undo deployment/order-service</code>. Verify the previous image is running.</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 4 — Strangler Fig Migration (Simulated)</div>
  <div class="lab-body">
    Simulate extracting a service from a monolith using Strangler Fig.
    <div class="lab-step"><span class="sn">1</span> Write a "monolith": a C HTTP server handling <code>/orders/*</code>, <code>/users/*</code>, and <code>/notifications/*</code> all in one process.</div>
    <div class="lab-step"><span class="sn">2</span> Write a new "Notifications microservice": a separate C process handling <code>/notifications/*</code>.</div>
    <div class="lab-step"><span class="sn">3</span> Add an Nginx reverse proxy as the "API Gateway": route <code>/notifications/*</code> to the new service, all other paths to the monolith.</div>
    <div class="lab-step"><span class="sn">4</span> Verify: requests to <code>/orders/123</code> hit the monolith. Requests to <code>/notifications/send</code> hit the new service. Both return correct responses.</div>
    <div class="lab-step"><span class="sn">5</span> Remove the notifications handler from the monolith. Verify all notification requests still work (now served entirely by new service).</div>
  </div>
</div>

<div class="sep">── Phase 6 Mastery Checklist ──</div>

<div class="two-col">
  <div>
    <strong style="color:#92400e">Architecture</strong>
    <ul class="cl">
      <li>Explain Conway's Law and how it drives service boundaries</li>
      <li>Describe the Strangler Fig migration pattern step by step</li>
      <li>Compare sync REST/gRPC vs async events for inter-service communication</li>
      <li>List 5 responsibilities of an API Gateway</li>
      <li>Explain client-side vs server-side service discovery</li>
    </ul>
    <strong style="color:#92400e">Resilience</strong>
    <ul class="cl">
      <li>Draw the circuit breaker state machine (CLOSED/OPEN/HALF-OPEN)</li>
      <li>Implement retry with exponential backoff + jitter</li>
      <li>Explain the bulkhead pattern and when to apply it</li>
      <li>Set correct timeout values relative to circuit breaker thresholds</li>
    </ul>
  </div>
  <div>
    <strong style="color:#92400e">Docker &amp; Kubernetes</strong>
    <ul class="cl">
      <li>Write a multi-stage Dockerfile for a C binary</li>
      <li>Explain why non-root + exec-form ENTRYPOINT matters</li>
      <li>Write a Deployment with liveness + readiness probes</li>
      <li>Explain the difference between liveness and readiness probes</li>
      <li>Perform a rolling update and rollback with kubectl</li>
    </ul>
    <strong style="color:#92400e">CI/CD &amp; 12-Factor</strong>
    <ul class="cl">
      <li>List the 8 stages of a production CI/CD pipeline</li>
      <li>Explain blue-green vs canary deployment trade-offs</li>
      <li>Apply 12-Factor principles: config in env, logs to stdout, graceful shutdown</li>
      <li>Write structured JSON logging and graceful SIGTERM handling in C</li>
    </ul>
  </div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/backend/m13-messaging/' | relative_url }}" class="nb">← M13: Event-Driven Architecture</a>
  <a href="{{ '/learning/backend/' | relative_url }}" class="nb">↑ Roadmap</a>
  <a href="{{ '/learning/backend/m17-observability/' | relative_url }}" class="nb">M17: Observability →</a>
</div>

</div><!-- /t-labs -->

</div><!-- /mod-wrap -->

<script>
function vt(id, btn) {
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  btn.classList.add('active');
}
</script>
