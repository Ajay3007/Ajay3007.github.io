---
title: "M17 — Observability & Hardening"
description: "Logs, metrics, traces — the 3 pillars. Prometheus, distributed tracing, rate limiting, OWASP Top 10, secrets management, graceful shutdown — with C implementations."
domain: engineering
track: backend
order: 17
url: /learning/backend/m17-observability/
---

<style>
/* ── Module shell ── */
.mod-wrap{max-width:960px;margin:0 auto;padding:0 1rem 4rem;font-family:'Segoe UI',system-ui,sans-serif;color:#1e293b}
.mod-header{background:#fff;border-left:5px solid #e11d48;border-radius:10px;padding:1.6rem 2rem;margin-bottom:1.5rem;box-shadow:0 2px 12px rgba(0,0,0,.08)}
.mod-header h1{margin:0 0 .4rem;font-size:1.75rem;color:#0f172a}
.mod-header .sub{color:#64748b;font-size:.95rem}
.phase-tag{display:inline-block;background:linear-gradient(90deg,#e11d48,#dc2626);color:#fff;font-size:.75rem;font-weight:700;padding:.25rem .75rem;border-radius:20px;margin-right:.5rem;text-transform:uppercase;letter-spacing:.05em}

/* ── Tabs ── */
.tab-bar{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:1.25rem}
.tab-btn{padding:.45rem 1rem;border:2px solid #e2e8f0;border-radius:20px;background:#fff;font-size:.82rem;font-weight:600;cursor:pointer;color:#64748b;transition:all .2s}
.tab-btn:hover{border-color:#e11d48;color:#be123c}
.tab-btn.active{background:linear-gradient(135deg,#e11d48,#dc2626);border-color:transparent;color:#fff;box-shadow:0 3px 10px rgba(225,29,72,.35)}
.tab-pane{display:none}.tab-pane.active{display:block}

/* ── Cards / panels ── */
.cp{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.cp-hdr{padding:.65rem 1.1rem;font-weight:700;font-size:.9rem;display:flex;align-items:center;gap:.5rem}
.cp-body{padding:1rem 1.2rem;background:#fff;font-size:.9rem;line-height:1.75}
.p-rose  .cp-hdr{background:linear-gradient(90deg,#fff1f2,#ffe4e6);color:#9f1239;border-left:4px solid #e11d48}
.p-red   .cp-hdr{background:linear-gradient(90deg,#fff1f2,#ffe4e6);color:#be123c;border-left:4px solid #f43f5e}
.p-blue  .cp-hdr{background:linear-gradient(90deg,#eff6ff,#dbeafe);color:#1d4ed8;border-left:4px solid #3b82f6}
.p-teal  .cp-hdr{background:linear-gradient(90deg,#f0fdf4,#dcfce7);color:#0f766e;border-left:4px solid #14b8a6}
.p-green .cp-hdr{background:linear-gradient(90deg,#f0fdf4,#dcfce7);color:#15803d;border-left:4px solid #16a34a}
.p-orange.cp-hdr,.p-orange>.cp-hdr{background:linear-gradient(90deg,#fff7ed,#ffedd5);color:#c2410c;border-left:4px solid #f97316}
.p-purple.cp-hdr,.p-purple>.cp-hdr{background:linear-gradient(90deg,#faf5ff,#f3e8ff);color:#7e22ce;border-left:4px solid #a855f7}
.p-amber .cp-hdr{background:linear-gradient(90deg,#fffbeb,#fef3c7);color:#92400e;border-left:4px solid #f59e0b}
.p-indigo.cp-hdr{background:linear-gradient(90deg,#eef2ff,#e0e7ff);color:#3730a3;border-left:4px solid #6366f1}
.p-cyan  .cp-hdr{background:linear-gradient(90deg,#ecfeff,#cffafe);color:#0e7490;border-left:4px solid #06b6d4}
.p-orange{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}
.p-purple{border-radius:10px;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.07)}

/* ── Callouts ── */
.ins,.warn,.note,.analogy{border-radius:8px;padding:.75rem 1rem;margin:.75rem 0;font-size:.87rem;line-height:1.7}
.ins  {background:#fff1f2;border-left:4px solid #e11d48;color:#881337}
.warn {background:#fff7ed;border-left:4px solid #f97316;color:#7c2d12}
.note {background:#eff6ff;border-left:4px solid #3b82f6;color:#1e3a5f}
.analogy{background:#faf5ff;border-left:4px solid #a855f7;color:#581c87}

/* ── Code blocks ── */
.cb{background:#0f172a;border-radius:10px;padding:1.1rem 1.3rem;margin:.75rem 0;overflow-x:auto;font-size:.82rem;line-height:1.75;font-family:'Cascadia Code','Fira Code',monospace}
.cm{color:#94a3b8}.ck{color:#7dd3fc}.cv{color:#86efac}.cs{color:#fca5a5}
.cn{color:#fdba74}.cf{color:#c4b5fd}.co{color:#fde68a}.cg{color:#6ee7b7}

/* ── Flow list ── */
.flow-list{list-style:none;padding:0;margin:.5rem 0}
.fl-step{display:flex;align-items:flex-start;gap:.85rem;padding:.65rem .85rem;margin-bottom:.5rem;border-radius:8px;background:#f8fafc;border-left:3px solid #e11d48;font-size:.88rem;line-height:1.65}
.fl-num{background:linear-gradient(135deg,#e11d48,#dc2626);color:#fff;border-radius:50%;width:1.6rem;height:1.6rem;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.75rem;flex-shrink:0}

/* ── Tables ── */
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.75rem 0}
.t-table th{background:linear-gradient(90deg,#e11d48,#dc2626);color:#fff;padding:.6rem .9rem;text-align:left}
.t-table td{padding:.55rem .9rem;border-bottom:1px solid #e2e8f0;vertical-align:top}
.t-table tr:nth-child(even) td{background:#f8fafc}
.t-table tr:hover td{background:#fff1f2}

/* ── Two-col ── */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.75rem 0}
@media(max-width:640px){.two-col{grid-template-columns:1fr}}

/* ── Lab box ── */
.lab-box{border:2px solid #e11d48;border-radius:10px;margin-bottom:1.25rem;overflow:hidden}
.lab-hdr{background:linear-gradient(90deg,#fff1f2,#ffe4e6);padding:.7rem 1.1rem;display:flex;align-items:center;gap:.6rem;font-weight:700;font-size:.9rem;color:#9f1239}
.lab-body{padding:1rem 1.2rem;font-size:.88rem;line-height:1.75}
.lab-step{padding:.4rem 0;padding-left:1.1rem;border-left:2px solid #e11d48;margin-bottom:.4rem}
.sn{display:inline-block;background:#e11d48;color:#fff;border-radius:50%;width:1.3rem;height:1.3rem;font-size:.7rem;font-weight:700;text-align:center;line-height:1.3rem;margin-right:.4rem}

/* ── Checklist ── */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{padding:.35rem .5rem;font-size:.87rem;display:flex;align-items:flex-start;gap:.6rem}
.cl li::before{content:"☐";color:#e11d48;font-size:1rem;flex-shrink:0}

/* ── Diagram ── */
.diagram-box{background:#0f172a;border-radius:10px;padding:1.1rem 1.3rem;margin:.75rem 0;overflow-x:auto;font-family:'Cascadia Code','Fira Code',monospace;font-size:.78rem;line-height:1.8;color:#94a3b8}
.dg-rose{color:#fda4af}.dg-blue{color:#93c5fd}.dg-green{color:#86efac}.dg-amber{color:#fde68a}.dg-gray{color:#64748b}.dg-purple{color:#c4b5fd}.dg-cyan{color:#67e8f9}.dg-red{color:#fca5a5}

/* ── Navigation ── */
.mod-nav{display:flex;justify-content:space-between;align-items:center;margin-top:2.5rem;padding:1rem 0;border-top:2px solid #e2e8f0;font-size:.88rem}
.nb{padding:.5rem 1.1rem;border:2px solid #e11d48;border-radius:20px;color:#be123c;text-decoration:none;font-weight:600;transition:all .2s}
.nb:hover{background:#e11d48;color:#fff}
.sep{text-align:center;color:#94a3b8;font-size:.8rem;letter-spacing:.1em;margin:1.5rem 0;text-transform:uppercase}
</style>

<div class="mod-wrap">

<div class="mod-header">
  <h1>M17 — Observability &amp; Hardening</h1>
  <div class="sub">
    <span class="phase-tag">Phase 7</span>
    3 pillars: logs · metrics · traces · Prometheus &amp; PromQL · Distributed tracing &amp; OpenTelemetry · Rate limiting · OWASP Top 10 · Secrets management · Graceful shutdown
  </div>
</div>

<!-- Tab bar -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt('t-overview',this)">Overview</button>
  <button class="tab-btn" onclick="vt('t-logs',this)">Logs</button>
  <button class="tab-btn" onclick="vt('t-metrics',this)">Metrics</button>
  <button class="tab-btn" onclick="vt('t-tracing',this)">Tracing</button>
  <button class="tab-btn" onclick="vt('t-alerting',this)">Alerting &amp; SLO</button>
  <button class="tab-btn" onclick="vt('t-security',this)">Security Hardening</button>
  <button class="tab-btn" onclick="vt('t-ratelimit',this)">Rate Limiting</button>
  <button class="tab-btn" onclick="vt('t-impl',this)">C Implementation</button>
  <button class="tab-btn" onclick="vt('t-labs',this)">Labs &amp; Checklist</button>
</div>

<!-- ══════════════════════════════════════════════════════════
     TAB 1 — Overview
     ══════════════════════════════════════════════════════════ -->
<div id="t-overview" class="tab-pane active">

<div class="cp p-rose">
  <div class="cp-hdr">🔭 The 3 Pillars of Observability</div>
  <div class="cp-body">
    Observability is the ability to understand the internal state of a system from its external outputs. The three pillars each answer a different question:
    <table class="t-table" style="margin-top:.75rem">
      <thead><tr><th>Pillar</th><th>Question Answered</th><th>Data Type</th><th>Tools</th></tr></thead>
      <tbody>
        <tr><td><strong>Logs</strong></td><td>"What happened, exactly?"</td><td>Discrete events with context</td><td>ELK, Loki, Fluentd</td></tr>
        <tr><td><strong>Metrics</strong></td><td>"How fast / how many / how full?"</td><td>Aggregated numeric time-series</td><td>Prometheus, Grafana, Datadog</td></tr>
        <tr><td><strong>Traces</strong></td><td>"Why was this request slow?"</td><td>Causal chains across services</td><td>Jaeger, Tempo, Zipkin, Honeycomb</td></tr>
      </tbody>
    </table>
    <div class="note">The three pillars are <em>complementary</em>, not interchangeable. An alert fires on a metric (high p99 latency). You look at a trace to find the slow span. You look at logs from that span to see the exact error. Use all three together.</div>
  </div>
</div>

<div class="analogy">
  <strong>Analogy — The flight data recorder:</strong><br>
  Logs are the cockpit voice recorder — full narrative of what was said. Metrics are the flight data recorder — altitude, speed, attitude plotted over time. Traces are the air traffic control replay — the full path of the aircraft from departure to destination. An accident investigation uses all three.
</div>

<div class="cp p-blue">
  <div class="cp-hdr">📐 Observability vs Monitoring</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th></th><th>Monitoring</th><th>Observability</th></tr></thead>
      <tbody>
        <tr><td><strong>Approach</strong></td><td>Predefined thresholds and dashboards for known failure modes</td><td>Ability to ask arbitrary questions about system behavior</td></tr>
        <tr><td><strong>Limits</strong></td><td>Only catches failures you anticipated and built alerts for</td><td>Enables debugging novel, unknown failure modes</td></tr>
        <tr><td><strong>Data</strong></td><td>Aggregated metrics, simple health checks</td><td>Logs + metrics + traces with high cardinality</td></tr>
        <tr><td><strong>Tooling</strong></td><td>Nagios, simple dashboards</td><td>OpenTelemetry, Honeycomb, Grafana + Loki + Tempo</td></tr>
      </tbody>
    </table>
    <div class="ins">Start with monitoring (dashboards for known metrics, alerts on thresholds). Add observability as system complexity grows — when you start debugging failures you didn't anticipate.</div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">📐 Phase 7 Module Map</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Module</th><th>Topic</th><th>Key Concepts</th></tr></thead>
      <tbody>
        <tr><td><strong>M17 (this)</strong></td><td>Observability &amp; Hardening</td><td>Logs, metrics, traces, alerting, SLO, security, rate limiting</td></tr>
        <tr><td>M18</td><td>Performance Engineering</td><td>Profiling, flame graphs, memory analysis, benchmark methodology</td></tr>
      </tbody>
    </table>
    <div class="note" style="margin-top:.75rem">Prerequisites: Ph6 (Microservices — you need services to observe; health probes from M15 are the basis of readiness checks here)</div>
  </div>
</div>

</div><!-- /t-overview -->

<!-- ══════════════════════════════════════════════════════════
     TAB 2 — Logs
     ══════════════════════════════════════════════════════════ -->
<div id="t-logs" class="tab-pane">

<div class="cp p-rose">
  <div class="cp-hdr">📝 Structured Logging: JSON Lines Format</div>
  <div class="cp-body">
    Write one JSON object per line to stdout. Every log line must include mandatory fields for searchability:
<div class="cb"><span class="cm">/* Good: structured JSON log */</span>
{<span class="cv">"ts"</span>:<span class="cv">"2026-03-27T14:23:01.442Z"</span>,<span class="cv">"level"</span>:<span class="cv">"INFO"</span>,<span class="cv">"service"</span>:<span class="cv">"order-svc"</span>,
 <span class="cv">"trace_id"</span>:<span class="cv">"4bf92f3577b34da6"</span>,<span class="cv">"span_id"</span>:<span class="cv">"00f067aa0ba902b7"</span>,
 <span class="cv">"msg"</span>:<span class="cv">"order placed"</span>,<span class="cv">"order_id"</span>:<span class="cv">"ord-9821"</span>,<span class="cv">"user_id"</span>:<span class="cv">"u-44"</span>,<span class="cv">"amount_usd"</span>:<span class="cn">49.99</span>}

<span class="cm">/* Bad: unstructured text — unsearchable */</span>
[<span class="cv">2026-03-27 14:23:01</span>] INFO: Order ord-9821 placed by user u-44 for $49.99</div>
  </div>
</div>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">📋 Mandatory Log Fields</div>
    <div class="cp-body">
      <table class="t-table">
        <thead><tr><th>Field</th><th>Format</th><th>Purpose</th></tr></thead>
        <tbody>
          <tr><td><code>ts</code></td><td>ISO-8601 with ms</td><td>Timeline reconstruction</td></tr>
          <tr><td><code>level</code></td><td>DEBUG/INFO/WARN/ERROR/FATAL</td><td>Log level filtering</td></tr>
          <tr><td><code>service</code></td><td>service name</td><td>Multi-service log aggregation</td></tr>
          <tr><td><code>trace_id</code></td><td>hex string</td><td>Correlate with traces</td></tr>
          <tr><td><code>span_id</code></td><td>hex string</td><td>Correlate with specific span</td></tr>
          <tr><td><code>msg</code></td><td>human-readable</td><td>Event description</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="cp p-teal">
    <div class="cp-hdr">🎚️ Log Levels — When to Use Each</div>
    <div class="cp-body">
      <table class="t-table">
        <thead><tr><th>Level</th><th>Use When</th></tr></thead>
        <tbody>
          <tr><td><code>DEBUG</code></td><td>Verbose detail for local dev only. Never in production — log volume explosion.</td></tr>
          <tr><td><code>INFO</code></td><td>Normal business events: request received, order placed, job started.</td></tr>
          <tr><td><code>WARN</code></td><td>Degraded but recoverable: retry succeeded, cache miss, approaching limit.</td></tr>
          <tr><td><code>ERROR</code></td><td>Unexpected failure requiring attention: DB timeout, invalid state, downstream error.</td></tr>
          <tr><td><code>FATAL</code></td><td>Unrecoverable — process will exit after logging.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="cp p-red">
  <div class="cp-hdr">🚫 What NOT to Log</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Never Log</th><th>Why</th><th>Alternative</th></tr></thead>
      <tbody>
        <tr><td>Passwords, API keys, tokens</td><td>Log aggregators, retention, and breach exposure</td><td>Log presence/absence, not value</td></tr>
        <tr><td>Full credit card numbers</td><td>PCI-DSS violation</td><td>Log last 4 digits only</td></tr>
        <tr><td>PII (emails, SSN, full name)</td><td>GDPR/CCPA violation</td><td>Log user_id (opaque reference)</td></tr>
        <tr><td>Full request/response bodies</td><td>Volume, PII risk</td><td>Log status codes and latency only</td></tr>
        <tr><td>Health probe hits (<code>/health/*</code>)</td><td>Thousands/min of noise</td><td>Filter at log aggregator</td></tr>
      </tbody>
    </table>
    <div class="warn"><strong>Log injection:</strong> never embed user-supplied strings directly in log messages without sanitization. A user who sets their name to <code>","level":"ERROR","msg":"admin escalation</code> can forge log entries. Escape or use parameterized logging.</div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">🔗 Correlation: Linking Logs Across Services</div>
  <div class="cp-body">
    The <strong>trace_id</strong> links all log lines for a single request across every service it touches:
<div class="cb"><span class="cm">/* API Gateway generates trace_id */</span>
GET /orders/123  → trace_id: <span class="cv">4bf92f3577b34da6</span>

<span class="cm">/* Order Service log */</span>
{<span class="cv">"service"</span>:<span class="cv">"order-svc"</span>,<span class="cv">"trace_id"</span>:<span class="cv">"4bf92f3577b34da6"</span>,<span class="cv">"msg"</span>:<span class="cv">"fetching order"</span>}

<span class="cm">/* Database call log */</span>
{<span class="cv">"service"</span>:<span class="cv">"order-svc"</span>,<span class="cv">"trace_id"</span>:<span class="cv">"4bf92f3577b34da6"</span>,<span class="cv">"msg"</span>:<span class="cv">"db query"</span>,<span class="cv">"duration_ms"</span>:<span class="cn">12</span>}

<span class="cm">/* In Loki/Elasticsearch: search by trace_id to see full request timeline */</span>
{trace_id="4bf92f3577b34da6"} | json | sort by ts</div>
    <div class="note">In Grafana with Loki + Tempo integration: click a trace in Tempo → jump directly to correlated logs in Loki for that trace_id. This cross-pillar navigation is the power of consistent trace_id propagation.</div>
  </div>
</div>

</div><!-- /t-logs -->

<!-- ══════════════════════════════════════════════════════════
     TAB 3 — Metrics
     ══════════════════════════════════════════════════════════ -->
<div id="t-metrics" class="tab-pane">

<div class="cp p-rose">
  <div class="cp-hdr">📊 Metric Types</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Type</th><th>Properties</th><th>Example</th><th>PromQL Usage</th></tr></thead>
      <tbody>
        <tr><td><strong>Counter</strong></td><td>Monotonically increasing, never decreases, resets to 0 on restart</td><td><code>http_requests_total{method="GET",status="200"}</code></td><td><code>rate(http_requests_total[5m])</code> → requests/sec</td></tr>
        <tr><td><strong>Gauge</strong></td><td>Point-in-time value, can go up or down</td><td><code>active_connections</code>, <code>memory_usage_bytes</code>, <code>queue_depth</code></td><td>Direct: <code>active_connections &gt; 1000</code></td></tr>
        <tr><td><strong>Histogram</strong></td><td>Samples bucketed by value; provides <code>_count</code>, <code>_sum</code>, <code>_bucket</code></td><td><code>request_duration_seconds{le="0.1"}</code></td><td><code>histogram_quantile(0.99, rate(request_duration_seconds_bucket[5m]))</code></td></tr>
        <tr><td><strong>Summary</strong></td><td>Pre-computed quantiles on client side (less flexible)</td><td><code>request_duration_seconds{quantile="0.99"}</code></td><td>Direct quantile access; can't re-aggregate across instances</td></tr>
      </tbody>
    </table>
    <div class="ins">Prefer <strong>Histogram</strong> over Summary. Histograms can be aggregated across multiple instances (e.g., p99 across all pods). Summaries compute quantiles per-process and can't be aggregated.</div>
  </div>
</div>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">🔴 RED Method (Services)</div>
    <div class="cp-body">
      The minimal set of metrics for any service:
      <ul style="margin:0;padding-left:1.2rem">
        <li><strong>Rate:</strong> requests per second — is traffic normal?<br><code>rate(http_requests_total[5m])</code></li>
        <li><strong>Errors:</strong> error rate — are users experiencing failures?<br><code>rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])</code></li>
        <li><strong>Duration:</strong> latency percentiles — is it slow?<br><code>histogram_quantile(0.99, rate(request_duration_seconds_bucket[5m]))</code></li>
      </ul>
      <div class="note" style="margin-top:.5rem">Alert on all three. High error rate → immediate page. High p99 → investigate. Low rate → traffic drop (upstream issue or deploy broke routing).</div>
    </div>
  </div>
  <div class="cp p-teal">
    <div class="cp-hdr">📊 USE Method (Resources)</div>
    <div class="cp-body">
      For infrastructure resources (CPU, memory, disk, network):
      <ul style="margin:0;padding-left:1.2rem">
        <li><strong>Utilization:</strong> % time resource is busy<br><code>rate(process_cpu_seconds_total[1m]) * 100</code></li>
        <li><strong>Saturation:</strong> extra work queued (can't keep up)<br><code>node_load1 / count(node_cpu_seconds_total{mode="idle"}) by (instance)</code></li>
        <li><strong>Errors:</strong> error count or rate of resource<br><code>node_disk_io_time_weighted_seconds_total</code></li>
      </ul>
      <div class="note" style="margin-top:.5rem">High utilization alone isn't a problem. High utilization + high saturation = at capacity. Alert when saturation exceeds 0 (work is queued).</div>
    </div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">📡 Prometheus: Pull-Based Scraping &amp; Exposition Format</div>
  <div class="cp-body">
    Prometheus <strong>polls</strong> your service's <code>/metrics</code> endpoint on a configurable interval (typically 15s). Your service exposes metrics in the Prometheus text format:
<div class="cb"><span class="cm"># HELP http_requests_total Total HTTP requests by method and status code</span>
<span class="cm"># TYPE http_requests_total counter</span>
http_requests_total{method=<span class="cv">"GET"</span>,status=<span class="cv">"200"</span>} <span class="cn">14823</span>
http_requests_total{method=<span class="cv">"POST"</span>,status=<span class="cv">"201"</span>} <span class="cn">3291</span>
http_requests_total{method=<span class="cv">"GET"</span>,status=<span class="cv">"500"</span>} <span class="cn">42</span>

<span class="cm"># HELP request_duration_seconds Request latency histogram</span>
<span class="cm"># TYPE request_duration_seconds histogram</span>
request_duration_seconds_bucket{le=<span class="cv">"0.01"</span>} <span class="cn">8901</span>
request_duration_seconds_bucket{le=<span class="cv">"0.05"</span>} <span class="cn">13102</span>
request_duration_seconds_bucket{le=<span class="cv">"0.1"</span>}  <span class="cn">14651</span>
request_duration_seconds_bucket{le=<span class="cv">"0.5"</span>}  <span class="cn">14820</span>
request_duration_seconds_bucket{le=<span class="cv">"+Inf"</span>} <span class="cn">14823</span>
request_duration_seconds_sum   <span class="cn">891.23</span>
request_duration_seconds_count <span class="cn">14823</span>

<span class="cm"># HELP active_connections Current active connections</span>
<span class="cm"># TYPE active_connections gauge</span>
active_connections <span class="cn">47</span></div>
    <div class="note"><strong>Labels are high-cardinality risk.</strong> A label like <code>{user_id="..."}</code> creates one time-series per user — millions of time-series destroy Prometheus. Use low-cardinality labels: <code>method</code>, <code>status</code>, <code>endpoint</code> (grouped). Never use user IDs, trace IDs, or UUIDs as labels.</div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">🔍 Essential PromQL Queries</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>What You Want</th><th>PromQL Query</th></tr></thead>
      <tbody>
        <tr><td>Request rate (req/sec)</td><td><code>rate(http_requests_total[5m])</code></td></tr>
        <tr><td>Error rate %</td><td><code>rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) * 100</code></td></tr>
        <tr><td>p99 latency</td><td><code>histogram_quantile(0.99, sum(rate(request_duration_seconds_bucket[5m])) by (le))</code></td></tr>
        <tr><td>CPU usage %</td><td><code>100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)</code></td></tr>
        <tr><td>Memory used</td><td><code>node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes</code></td></tr>
        <tr><td>Kafka consumer lag</td><td><code>kafka_consumer_group_lag{topic="orders",partition="0"}</code></td></tr>
        <tr><td>DB connection pool saturation</td><td><code>pg_stat_activity_count / pg_settings_max_connections</code></td></tr>
      </tbody>
    </table>
  </div>
</div>

</div><!-- /t-metrics -->

<!-- ══════════════════════════════════════════════════════════
     TAB 4 — Tracing
     ══════════════════════════════════════════════════════════ -->
<div id="t-tracing" class="tab-pane">

<div class="cp p-rose">
  <div class="cp-hdr">🔗 Distributed Tracing: Trace &amp; Span Model</div>
  <div class="cp-body">
    A <strong>trace</strong> represents the complete journey of a single request through the system — from the client's HTTP request through every service, database call, and queue publish it touches.
    <br><br>
    A <strong>span</strong> represents a single unit of work within a trace (one service call, one DB query). Each span has:
    <ul>
      <li><code>trace_id</code> — shared across all spans in the same request</li>
      <li><code>span_id</code> — unique to this operation</li>
      <li><code>parent_span_id</code> — the span that triggered this one (null for root span)</li>
      <li>Start time + duration</li>
      <li>Attributes (key-value context)</li>
      <li>Status (OK / ERROR)</li>
    </ul>
  </div>
</div>

<div class="diagram-box">
Trace: <span class="dg-rose">trace_id=4bf92f3577b34da6</span>

<span class="dg-blue">span_id=00f067aa  [API Gateway]</span>  GET /orders/123   0ms ──────────────── 87ms
  │
  ├─ <span class="dg-green">span_id=a3ce929d  [Order Service]</span>  handle_request   2ms ──────── 83ms
  │     │
  │     ├─ <span class="dg-amber">span_id=5e0c22e9  [DB: SELECT orders]</span>     4ms ── 16ms  (12ms)
  │     │
  │     ├─ <span class="dg-amber">span_id=7f3d8a1b  [Redis: GET cache]</span>      18ms ─ 19ms  (1ms)
  │     │
  │     └─ <span class="dg-purple">span_id=2d4f991c  [Kafka: publish event]</span>  20ms ──── 34ms  (14ms)
  │
  └─ <span class="dg-cyan">span_id=b1c5e072  [Auth Service]</span>   verify_token      1ms ─ 2ms   (1ms)

<span class="dg-gray">Flame chart: wider = longer. The DB SELECT at 12ms is the hot spot.</span>
</div>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">📡 W3C traceparent Header</div>
    <div class="cp-body">
      The standard header for propagating trace context across HTTP service calls:
<div class="cb"><span class="cm">traceparent: 00-4bf92f3577b34da6a3ce929d-00f067aa0ba902b7-01</span>
              <span class="cm">│  │                        │                  │</span>
              <span class="cm">│  └─ trace_id (128-bit)   └─ parent_span_id  └─ flags</span>
              <span class="cm">└─ version (00)</span>
              <span class="cm">                                                  01 = sampled</span>
              <span class="cm">                                                  00 = not sampled</span></div>
      Each service: read <code>traceparent</code> from incoming request, create a child span (using the span_id as parent_span_id), set the new span's span_id, and propagate the updated <code>traceparent</code> in outgoing calls.
    </div>
  </div>
  <div class="cp p-teal">
    <div class="cp-hdr">📦 OpenTelemetry (OTel)</div>
    <div class="cp-body">
      OpenTelemetry is the CNCF standard for instrumentation — vendor-neutral SDK for generating traces, metrics, and logs.
      <ul style="margin:0;padding-left:1.2rem">
        <li><strong>SDK:</strong> available in C, Go, Java, Python, etc.</li>
        <li><strong>OTLP:</strong> OpenTelemetry Protocol — exports to any backend</li>
        <li><strong>OTel Collector:</strong> receives OTLP, processes (batch, sample), exports to Jaeger/Tempo/Datadog</li>
        <li><strong>Auto-instrumentation:</strong> inject tracing without changing application code (Java agent, eBPF)</li>
        <li><strong>Manual instrumentation:</strong> create custom spans for business logic</li>
      </ul>
    </div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr">📊 Sampling Strategies</div>
  <div class="cp-body">
    At high volume (10,000 req/sec), storing every trace is expensive. Sampling decides which traces to keep:
    <table class="t-table">
      <thead><tr><th>Strategy</th><th>How</th><th>Trade-off</th></tr></thead>
      <tbody>
        <tr><td><strong>Head-based: Always-on</strong></td><td>Keep 100% of traces</td><td>Very expensive at scale</td></tr>
        <tr><td><strong>Head-based: Probability</strong></td><td>Keep N% (e.g. 1%)</td><td>Simple, but misses rare errors</td></tr>
        <tr><td><strong>Head-based: Rate-limit</strong></td><td>Keep up to N traces/sec</td><td>Bounded cost; may drop bursts</td></tr>
        <tr><td><strong>Tail-based: Error sampling</strong></td><td>Buffer all traces; keep if trace has an error span</td><td>Catches errors; high memory buffer</td></tr>
        <tr><td><strong>Tail-based: Latency threshold</strong></td><td>Keep if trace duration &gt; P99 threshold</td><td>Catches slowness; complex to implement</td></tr>
      </tbody>
    </table>
    <div class="ins"><strong>Production recommendation:</strong> 1% head-based sampling for normal traffic + 100% sampling for traces with errors (tail-based error sampling). This keeps costs bounded while capturing all failure evidence.</div>
  </div>
</div>

</div><!-- /t-tracing -->

<!-- ══════════════════════════════════════════════════════════
     TAB 5 — Alerting & SLO
     ══════════════════════════════════════════════════════════ -->
<div id="t-alerting" class="tab-pane">

<div class="cp p-rose">
  <div class="cp-hdr">🔔 Alerting with Prometheus AlertManager</div>
  <div class="cp-body">
    Prometheus evaluates alerting rules against scraped metrics. When conditions are met, it sends alerts to AlertManager, which routes them to PagerDuty, Slack, email, etc.
<div class="cb"><span class="cm"># alerting_rules.yml</span>
<span class="ck">groups</span>:
- <span class="ck">name</span>: <span class="cv">order-service</span>
  <span class="ck">rules</span>:
  - <span class="ck">alert</span>: <span class="cv">HighErrorRate</span>
    <span class="ck">expr</span>: <span class="cv">|
      rate(http_requests_total{service="order-svc",status=~"5.."}[5m])
      / rate(http_requests_total{service="order-svc"}[5m]) > 0.01</span>
    <span class="ck">for</span>: <span class="cv">2m</span>          <span class="cm"># must be true for 2m before firing (avoid flapping)</span>
    <span class="ck">labels</span>:
      <span class="ck">severity</span>: <span class="cv">critical</span>
    <span class="ck">annotations</span>:
      <span class="ck">summary</span>: <span class="cv">"Error rate > 1% for order-service"</span>
      <span class="ck">runbook_url</span>: <span class="cv">"https://wiki/runbooks/order-svc-errors"</span>

  - <span class="ck">alert</span>: <span class="cv">HighP99Latency</span>
    <span class="ck">expr</span>: <span class="cv">|
      histogram_quantile(0.99,
        sum(rate(request_duration_seconds_bucket{service="order-svc"}[5m]))
        by (le)) > 2.0</span>
    <span class="ck">for</span>: <span class="cv">5m</span>
    <span class="ck">labels</span>:
      <span class="ck">severity</span>: <span class="cv">warning</span>

  - <span class="ck">alert</span>: <span class="cv">ServiceDown</span>
    <span class="ck">expr</span>: <span class="cv">up{service="order-svc"} == 0</span>
    <span class="ck">for</span>: <span class="cv">1m</span>
    <span class="ck">labels</span>:
      <span class="ck">severity</span>: <span class="cv">critical</span></div>
  </div>
</div>

<div class="two-col">
  <div class="cp p-blue">
    <div class="cp-hdr">📏 SLI, SLO, SLA</div>
    <div class="cp-body">
      <ul style="margin:0;padding-left:1.2rem">
        <li><strong>SLI</strong> (Service Level Indicator): a specific measurable metric — e.g., <em>availability = (successful requests) / (total requests)</em></li>
        <li><strong>SLO</strong> (Service Level Objective): internal target — e.g., <em>availability ≥ 99.9% over 30 days</em>. Engineering commits to this.</li>
        <li><strong>SLA</strong> (Service Level Agreement): external contract with customers — stricter legal/financial penalties. SLO should be tighter than SLA as a safety buffer.</li>
        <li><strong>Error Budget:</strong> SLO headroom — 99.9% SLO = 0.1% budget = 43.8 min/month. Track burn rate.</li>
      </ul>
    </div>
  </div>
  <div class="cp p-red">
    <div class="cp-hdr">💸 Error Budget &amp; Burn Rate Alerts</div>
    <div class="cp-body">
      Don't alert "SLO violated" (too late). Alert on burn rate — how fast you're consuming the error budget:
      <ul style="margin:0;padding-left:1.2rem">
        <li><strong>Fast burn:</strong> consuming 14× normal rate → will exhaust budget in 1h → page immediately</li>
        <li><strong>Slow burn:</strong> consuming 3× normal rate → will exhaust in ~5 days → ticket</li>
      </ul>
<div class="cb"><span class="cm"># Fast burn alert: &gt;14x budget consumption over 1h</span>
<span class="ck">expr</span>: <span class="cv">|
  (1 - (sum(rate(http_requests_total{status!~"5.."}[1h]))
       / sum(rate(http_requests_total[1h]))))
  / (1 - 0.999) > 14</span></div>
    </div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">📋 Alert Design Principles</div>
  <div class="cp-body">
    <ul>
      <li><strong>Alert on symptoms, not causes:</strong> Alert on high error rate (symptom users feel), not on "CPU at 80%" (cause — may not impact users)</li>
      <li><strong>Every alert needs a runbook:</strong> include <code>runbook_url</code> annotation. On-call engineers should never face an alert without documented response steps.</li>
      <li><strong>Avoid alert fatigue:</strong> if the same alert fires weekly and engineers silence it, it's not actionable. Remove or fix it.</li>
      <li><strong>Use <code>for</code> duration:</strong> require condition to be sustained before paging (avoids flapping on 1-second spikes)</li>
      <li><strong>Group related alerts:</strong> AlertManager can group 50 firing alerts into one notification — prevents notification flood during outages</li>
    </ul>
  </div>
</div>

</div><!-- /t-alerting -->

<!-- ══════════════════════════════════════════════════════════
     TAB 6 — Security Hardening
     ══════════════════════════════════════════════════════════ -->
<div id="t-security" class="tab-pane">

<div class="cp p-rose">
  <div class="cp-hdr">🔒 OWASP Top 10 for Backend Services</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Vulnerability</th><th>C/Backend Example</th><th>Prevention</th></tr></thead>
      <tbody>
        <tr><td><strong>SQL Injection</strong></td><td><code>"SELECT * FROM users WHERE id=" + user_id</code></td><td>Parameterized queries only: <code>PQexecParams(conn, "SELECT... WHERE id=$1", 1, NULL, params, ...)</code></td></tr>
        <tr><td><strong>Command Injection</strong></td><td><code>system("ls " + user_input)</code></td><td>Never use <code>system()</code> with user input. Use <code>execv()</code> with argument array.</td></tr>
        <tr><td><strong>SSRF</strong></td><td>Service fetches URL from user request body; attacker uses <code>http://169.254.169.254/</code> (AWS metadata)</td><td>Allowlist of permitted outbound domains; block RFC-1918 and link-local addresses</td></tr>
        <tr><td><strong>Broken Access Control</strong></td><td>User A can read User B's orders by changing order_id in request</td><td>Check authorization on every resource: <code>WHERE id=$1 AND user_id=$2</code></td></tr>
        <tr><td><strong>Security Misconfiguration</strong></td><td>Debug endpoints enabled in prod, default credentials, verbose error messages</td><td>Separate prod config; disable <code>/debug</code> endpoints; return generic errors</td></tr>
        <tr><td><strong>Insecure Deserialization</strong></td><td>Deserializing untrusted binary input (msgpack, protobuf from user)</td><td>Validate schema; set max sizes; reject unknown fields</td></tr>
        <tr><td><strong>Cryptographic Failures</strong></td><td>MD5 for passwords, ECB mode, hardcoded keys</td><td>bcrypt/Argon2 for passwords; AES-256-GCM for encryption; libsodium</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-red">
  <div class="cp-hdr">🛡️ SSRF Prevention in C</div>
  <div class="cp-body">
<div class="cb"><span class="cm">/* SSRF allowlist check before making outbound HTTP request */</span>
<span class="cs">#include</span> &lt;netdb.h&gt;
<span class="cs">#include</span> &lt;arpa/inet.h&gt;
<span class="cs">#include</span> &lt;string.h&gt;

<span class="cm">/* Returns 1 if IP is RFC-1918 / link-local / loopback (block these) */</span>
<span class="cs">static int</span> <span class="cf">is_private_ip</span>(<span class="cs">const char</span> *ip) {
    <span class="cs">struct in_addr</span> addr;
    <span class="ck">if</span> (!inet_pton(AF_INET, ip, &amp;addr)) <span class="ck">return</span> <span class="cn">0</span>;
    <span class="cs">uint32_t</span> n = ntohl(addr.s_addr);
    <span class="ck">return</span>
        (n &gt;&gt; <span class="cn">24</span> == <span class="cn">10</span>)                          <span class="cm">/* 10.0.0.0/8      */</span>
     || (n &gt;&gt; <span class="cn">20</span> == (172 &lt;&lt; <span class="cn">4</span>) + <span class="cn">1</span>)            <span class="cm">/* 172.16.0.0/12   */</span>
     || (n &gt;&gt; <span class="cn">16</span> == (192 &lt;&lt; <span class="cn">8</span>) + <span class="cn">168</span>)          <span class="cm">/* 192.168.0.0/16  */</span>
     || (n &gt;&gt; <span class="cn">24</span> == <span class="cn">127</span>)                        <span class="cm">/* 127.0.0.0/8     */</span>
     || (n &gt;&gt; <span class="cn">16</span> == (169 &lt;&lt; <span class="cn">8</span>) + <span class="cn">254</span>);         <span class="cm">/* 169.254.0.0/16  */</span>
}

<span class="cs">int</span> <span class="cf">safe_fetch_url</span>(<span class="cs">const char</span> *url) {
    <span class="cm">/* 1. Parse hostname from URL (simplified) */</span>
    <span class="cs">char</span> hostname[<span class="cn">256</span>];
    sscanf(url, <span class="cv">"https://%255[^/]"</span>, hostname);

    <span class="cm">/* 2. Allowlist check: only permitted domains */</span>
    <span class="cs">const char</span> *allowed[] = { <span class="cv">"api.stripe.com"</span>, <span class="cv">"hooks.slack.com"</span>, NULL };
    <span class="cs">int</span> permitted = <span class="cn">0</span>;
    <span class="ck">for</span> (<span class="cs">int</span> i = <span class="cn">0</span>; allowed[i]; i++)
        <span class="ck">if</span> (strcmp(hostname, allowed[i]) == <span class="cn">0</span>) { permitted = <span class="cn">1</span>; <span class="ck">break</span>; }

    <span class="ck">if</span> (!permitted) {
        fprintf(stderr, <span class="cv">"SSRF blocked: %s not in allowlist\n"</span>, hostname);
        <span class="ck">return</span> -<span class="cn">1</span>;
    }

    <span class="cm">/* 3. DNS resolution + IP check */</span>
    <span class="cs">struct addrinfo</span> *res;
    getaddrinfo(hostname, NULL, NULL, &amp;res);
    <span class="cs">char</span> ip[INET6_ADDRSTRLEN];
    inet_ntop(AF_INET,
        &amp;((<span class="cs">struct sockaddr_in</span> *)res-&gt;ai_addr)-&gt;sin_addr,
        ip, <span class="ck">sizeof</span>(ip));
    freeaddrinfo(res);

    <span class="ck">if</span> (is_private_ip(ip)) {
        fprintf(stderr, <span class="cv">"SSRF blocked: %s resolved to private IP %s\n"</span>,
                hostname, ip);
        <span class="ck">return</span> -<span class="cn">1</span>;
    }

    <span class="cm">/* 4. Make the actual HTTP request */</span>
    <span class="ck">return</span> <span class="cn">0</span>;  <span class="cm">/* proceed */</span>
}</div>
  </div>
</div>

<div class="cp p-purple">
  <div class="cp-hdr">🔑 Secrets Management</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Approach</th><th>Security</th><th>Details</th></tr></thead>
      <tbody>
        <tr><td>Hardcoded in source</td><td>❌ Never</td><td>Committed to git, all developers see it, forever in history</td></tr>
        <tr><td>Environment variables</td><td>⚠️ Acceptable</td><td>Not in code but visible in process env, logs, crash dumps — use only with Kubernetes Secrets</td></tr>
        <tr><td>Kubernetes Secrets</td><td>✅ Good</td><td>Base64 in etcd (encrypt etcd at rest); mounted as files or env; access controlled by RBAC</td></tr>
        <tr><td>HashiCorp Vault</td><td>✅✅ Best</td><td>Dynamic secrets (generated on request, auto-expire), audit log, lease renewal, fine-grained access control</td></tr>
        <tr><td>AWS Secrets Manager / GCP Secret Manager</td><td>✅✅ Best</td><td>Managed service equivalent; auto-rotation; IAM-controlled access</td></tr>
      </tbody>
    </table>
    <div class="ins"><strong>Dynamic secrets (Vault):</strong> instead of a long-lived DB password, Vault generates a unique username+password for each service instance with a 1-hour TTL. When the instance dies, the credential expires automatically. Breach impact is bounded in time and scope.</div>
    <div class="warn"><strong>Secret rotation:</strong> rotate all secrets after any suspected breach. Never reuse credentials. Implement graceful rotation: support old and new secret simultaneously for 30s during rotation to avoid downtime.</div>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">✅ Input Validation: Trust Boundaries</div>
  <div class="cp-body">
    Validate all data at trust boundaries (external inputs). Trust internal calls and framework output.
<div class="cb"><span class="cm">/* Input validation at trust boundary (HTTP request body) */</span>
<span class="cs">typedef struct</span> {
    <span class="cs">char</span>   order_id[<span class="cn">37</span>];   <span class="cm">/* UUID: 36 chars + null */</span>
    <span class="cs">double</span> amount;
    <span class="cs">int</span>    item_count;
} order_request_t;

<span class="cs">int</span> <span class="cf">validate_order_request</span>(<span class="cs">const</span> order_request_t *req) {
    <span class="cm">/* Size bounds */</span>
    <span class="ck">if</span> (strlen(req-&gt;order_id) != <span class="cn">36</span>) <span class="ck">return</span> -<span class="cn">1</span>;

    <span class="cm">/* UUID format: 8-4-4-4-12 hex chars with dashes */</span>
    <span class="ck">if</span> (!is_valid_uuid(req-&gt;order_id)) <span class="ck">return</span> -<span class="cn">1</span>;

    <span class="cm">/* Business rule bounds */</span>
    <span class="ck">if</span> (req-&gt;amount &lt;= <span class="cn">0.0</span> || req-&gt;amount &gt; <span class="cn">100000.0</span>) <span class="ck">return</span> -<span class="cn">1</span>;
    <span class="ck">if</span> (req-&gt;item_count &lt; <span class="cn">1</span> || req-&gt;item_count &gt; <span class="cn">100</span>) <span class="ck">return</span> -<span class="cn">1</span>;

    <span class="ck">return</span> <span class="cn">0</span>;  <span class="cm">/* valid */</span>
}
<span class="cm">/* Use allowlist validation, not denylist:
   know what's valid and reject everything else,
   rather than trying to enumerate all invalid inputs */</span></div>
  </div>
</div>

</div><!-- /t-security -->

<!-- ══════════════════════════════════════════════════════════
     TAB 7 — Rate Limiting
     ══════════════════════════════════════════════════════════ -->
<div id="t-ratelimit" class="tab-pane">

<div class="cp p-rose">
  <div class="cp-hdr">🚦 Rate Limiting Algorithms</div>
  <div class="cp-body">
    Rate limiting protects services from overload and abusive clients. Implement at two layers:
    <ul>
      <li><strong>API Gateway:</strong> global rate limiting per client IP or API key — protects all services</li>
      <li><strong>Per-service:</strong> self-defense against gateway bypass or internal traffic spikes</li>
    </ul>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr">🪣 Token Bucket</div>
  <div class="cp-body">
    A bucket holds up to <strong>capacity</strong> tokens. Tokens are added at rate <strong>r</strong> tokens/sec. Each request consumes one token. If the bucket is empty, the request is rejected.
    <br><br>
    <strong>Key property:</strong> allows bursts up to capacity while maintaining an average rate of r req/sec.
    <div class="diagram-box" style="margin:.5rem 0;font-size:.72rem">
Refill rate: <span class="dg-green">10 tokens/sec</span>    Capacity: <span class="dg-blue">20 tokens</span>

t=0:  [████████████████████] 20 tokens  → burst of 20 requests: <span class="dg-green">OK</span>
t=0.1 [░░░░░░░░░░░░░░░░░░░░] 0 tokens   → request: <span class="dg-red">REJECT (429)</span>
t=0.5 [█████░░░░░░░░░░░░░░░] 5 tokens   → 5 requests: <span class="dg-green">OK</span>
t=1.0 [██████████░░░░░░░░░░] 10 tokens  → 10 requests: <span class="dg-green">OK</span>
<span class="dg-gray">Steady state: 10 req/sec sustained (burst allowed up to 20)</span>
    </div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr">🪟 Sliding Window Counter</div>
  <div class="cp-body">
    Divide time into fixed windows. Track request count in the current window and weight with the previous window's count. More accurate than a fixed window but O(1) memory.
    <br><br>
    <strong>Formula:</strong> <code>count = prev_window_count × overlap_fraction + curr_window_count</code>
<div class="cb"><span class="cm">/* Sliding window counter with Redis (pseudocode) */</span>
<span class="cs">long</span> <span class="cf">sliding_window_count</span>(<span class="cs">const char</span> *client_key, <span class="cs">int</span> window_sec) {
    <span class="cs">long</span> now = time(NULL);
    <span class="cs">long</span> curr_window = now / window_sec;
    <span class="cs">long</span> prev_window = curr_window - <span class="cn">1</span>;
    <span class="cs">double</span> elapsed = now % window_sec;
    <span class="cs">double</span> overlap = <span class="cn">1.0</span> - elapsed / window_sec;

    <span class="cs">long</span> prev_count = redis_get_counter(client_key, prev_window);
    <span class="cs">long</span> curr_count = redis_incr_counter(client_key, curr_window, window_sec);

    <span class="ck">return</span> (<span class="cs">long</span>)(prev_count * overlap + curr_count);
}</div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr">⚖️ Algorithm Comparison</div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Algorithm</th><th>Burst Handling</th><th>Memory</th><th>Accuracy</th><th>Best For</th></tr></thead>
      <tbody>
        <tr><td><strong>Fixed Window Counter</strong></td><td>Double burst at boundary (end+start of adjacent windows)</td><td>O(1)</td><td>Low (boundary problem)</td><td>Simple low-traffic systems</td></tr>
        <tr><td><strong>Sliding Window Log</strong></td><td>Exact</td><td>O(requests in window)</td><td>Exact</td><td>Low-volume, exact limits needed</td></tr>
        <tr><td><strong>Sliding Window Counter</strong></td><td>Approximate (±0.1%)</td><td>O(1)</td><td>High</td><td>Most production APIs</td></tr>
        <tr><td><strong>Token Bucket</strong></td><td>Allows bursts up to capacity</td><td>O(1)</td><td>High</td><td>APIs tolerating short bursts</td></tr>
        <tr><td><strong>Leaky Bucket</strong></td><td>Smooths all bursts, strict output rate</td><td>O(1)</td><td>High</td><td>Traffic shaping (network)</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="cp p-orange">
  <div class="cp-hdr">📤 Rate Limit Response Headers</div>
  <div class="cp-body">
    Return these headers on every response so clients can self-throttle:
<div class="cb"><span class="cm">HTTP/1.1 200 OK</span>
<span class="ck">X-RateLimit-Limit</span>: <span class="cn">100</span>           <span class="cm"># max requests per window</span>
<span class="ck">X-RateLimit-Remaining</span>: <span class="cn">47</span>        <span class="cm"># requests left in current window</span>
<span class="ck">X-RateLimit-Reset</span>: <span class="cn">1711544400</span>   <span class="cm"># Unix timestamp when window resets</span>

<span class="cm">HTTP/1.1 429 Too Many Requests</span>
<span class="ck">Retry-After</span>: <span class="cn">23</span>                  <span class="cm"># seconds until client can retry</span>
<span class="ck">X-RateLimit-Limit</span>: <span class="cn">100</span>
<span class="ck">X-RateLimit-Remaining</span>: <span class="cn">0</span>
<span class="ck">Content-Type</span>: application/json
{<span class="cv">"error"</span>: <span class="cv">"RATE_LIMIT_EXCEEDED"</span>, <span class="cv">"retry_after_seconds"</span>: <span class="cn">23</span>}</div>
    <div class="note">Never silently drop rate-limited requests. Return <code>429</code> with <code>Retry-After</code> so well-behaved clients back off correctly. Silently dropping causes clients to retry faster (thundering herd).</div>
  </div>
</div>

</div><!-- /t-ratelimit -->

<!-- ══════════════════════════════════════════════════════════
     TAB 8 — C Implementation
     ══════════════════════════════════════════════════════════ -->
<div id="t-impl" class="tab-pane">

<div class="sep">── Implementation 1 — Prometheus Metrics Exposition Endpoint ──</div>

<div class="cp p-rose">
  <div class="cp-hdr">📡 Prometheus /metrics Endpoint in C</div>
  <div class="cp-body">
<div class="cb"><span class="cm">/* metrics.h — thread-safe counters and histograms for Prometheus exposition */</span>
<span class="cs">#pragma once</span>
<span class="cs">#include</span> &lt;stdatomic.h&gt;
<span class="cs">#include</span> &lt;stdio.h&gt;
<span class="cs">#include</span> &lt;time.h&gt;

<span class="cm">/* HTTP request counter: label dimensions = {method, status} */</span>
<span class="cs">typedef struct</span> {
    _Atomic(<span class="cs">long</span>) get_2xx, get_4xx, get_5xx;
    _Atomic(<span class="cs">long</span>) post_2xx, post_4xx, post_5xx;
} http_counters_t;

<span class="cm">/* Latency histogram: fixed buckets in seconds */</span>
<span class="cs">#define</span> BUCKET_COUNT <span class="cn">7</span>
<span class="cs">static const double</span> BUCKETS[BUCKET_COUNT] =
    { <span class="cn">0.005</span>, <span class="cn">0.01</span>, <span class="cn">0.025</span>, <span class="cn">0.05</span>, <span class="cn">0.1</span>, <span class="cn">0.5</span>, <span class="cn">1.0</span> };

<span class="cs">typedef struct</span> {
    _Atomic(<span class="cs">long</span>)   bucket[BUCKET_COUNT];
    _Atomic(<span class="cs">long</span>)   count;
    _Atomic(<span class="cs">double</span>) sum;  <span class="cm">/* note: atomic double ops may need mutex on older C */</span>
} latency_histogram_t;

<span class="cm">/* Global metrics state */</span>
<span class="cs">static</span> http_counters_t   g_http  = {<span class="cn">0</span>};
<span class="cs">static</span> latency_histogram_t g_lat = {<span class="cn">0</span>};
<span class="cs">static</span> _Atomic(<span class="cs">long</span>)    g_active_conn = <span class="cn">0</span>;

<span class="ck">static inline</span> <span class="cs">void</span> <span class="cf">record_request</span>(<span class="cs">const char</span> *method, <span class="cs">int</span> status, <span class="cs">double</span> dur_s) {
    <span class="cm">/* Increment counter by method+status */</span>
    <span class="ck">if</span> (strcmp(method, <span class="cv">"GET"</span>) == <span class="cn">0</span>) {
        <span class="ck">if</span> (status &lt; <span class="cn">300</span>)       atomic_fetch_add(&amp;g_http.get_2xx, <span class="cn">1</span>);
        <span class="ck">else if</span> (status &lt; <span class="cn">500</span>) atomic_fetch_add(&amp;g_http.get_4xx, <span class="cn">1</span>);
        <span class="ck">else</span>                     atomic_fetch_add(&amp;g_http.get_5xx, <span class="cn">1</span>);
    }

    <span class="cm">/* Update histogram */</span>
    <span class="ck">for</span> (<span class="cs">int</span> i = <span class="cn">0</span>; i &lt; BUCKET_COUNT; i++)
        <span class="ck">if</span> (dur_s &lt;= BUCKETS[i])
            atomic_fetch_add(&amp;g_lat.bucket[i], <span class="cn">1</span>);
    atomic_fetch_add(&amp;g_lat.count, <span class="cn">1</span>);
    <span class="cm">/* sum: use mutex for double precision (simplified: use long microseconds) */</span>
    atomic_fetch_add(&amp;g_lat.count, <span class="cn">0</span>);  <span class="cm">/* placeholder */</span>
}

<span class="cm">/* Render /metrics response body into buf */</span>
<span class="ck">static inline</span> <span class="cs">int</span> <span class="cf">render_metrics</span>(<span class="cs">char</span> *buf, <span class="cs">size_t</span> sz) {
    <span class="cs">int</span> n = <span class="cn">0</span>;
    n += snprintf(buf + n, sz - n,
        <span class="cv">"# HELP http_requests_total Total HTTP requests\n"</span>
        <span class="cv">"# TYPE http_requests_total counter\n"</span>
        <span class="cv">"http_requests_total{method=\"GET\",status=\"2xx\"} %ld\n"</span>
        <span class="cv">"http_requests_total{method=\"GET\",status=\"4xx\"} %ld\n"</span>
        <span class="cv">"http_requests_total{method=\"GET\",status=\"5xx\"} %ld\n"</span>,
        atomic_load(&amp;g_http.get_2xx),
        atomic_load(&amp;g_http.get_4xx),
        atomic_load(&amp;g_http.get_5xx));

    n += snprintf(buf + n, sz - n,
        <span class="cv">"# HELP active_connections Current connections\n"</span>
        <span class="cv">"# TYPE active_connections gauge\n"</span>
        <span class="cv">"active_connections %ld\n"</span>,
        atomic_load(&amp;g_active_conn));

    n += snprintf(buf + n, sz - n,
        <span class="cv">"# HELP request_duration_seconds Latency histogram\n"</span>
        <span class="cv">"# TYPE request_duration_seconds histogram\n"</span>);
    <span class="ck">for</span> (<span class="cs">int</span> i = <span class="cn">0</span>; i &lt; BUCKET_COUNT; i++)
        n += snprintf(buf + n, sz - n,
            <span class="cv">"request_duration_seconds_bucket{le=\"%.3f\"} %ld\n"</span>,
            BUCKETS[i], atomic_load(&amp;g_lat.bucket[i]));
    n += snprintf(buf + n, sz - n,
        <span class="cv">"request_duration_seconds_bucket{le=\"+Inf\"} %ld\n"</span>
        <span class="cv">"request_duration_seconds_count %ld\n"</span>,
        atomic_load(&amp;g_lat.count),
        atomic_load(&amp;g_lat.count));
    <span class="ck">return</span> n;
}</div>
  </div>
</div>

<div class="sep">── Implementation 2 — Structured JSON Logger ──</div>

<div class="cp p-blue">
  <div class="cp-hdr">📝 Structured JSON Logger with Trace ID</div>
  <div class="cp-body">
<div class="cb"><span class="cm">/* logger.h — structured JSON logger with trace context */</span>
<span class="cs">#pragma once</span>
<span class="cs">#include</span> &lt;stdio.h&gt;
<span class="cs">#include</span> &lt;time.h&gt;
<span class="cs">#include</span> &lt;string.h&gt;

<span class="cs">typedef struct</span> {
    <span class="cs">char</span> trace_id[<span class="cn">33</span>];  <span class="cm">/* 128-bit hex */</span>
    <span class="cs">char</span> span_id[<span class="cn">17</span>];   <span class="cm">/* 64-bit hex  */</span>
} trace_ctx_t;

<span class="cm">/* Thread-local trace context */</span>
<span class="cs">static</span> _Thread_local trace_ctx_t tl_trace = {<span class="cn">0</span>};

<span class="ck">static inline</span> <span class="cs">void</span> <span class="cf">log_set_trace</span>(<span class="cs">const char</span> *trace_id, <span class="cs">const char</span> *span_id) {
    strncpy(tl_trace.trace_id, trace_id, <span class="cn">32</span>);
    strncpy(tl_trace.span_id,  span_id,  <span class="cn">16</span>);
    tl_trace.trace_id[<span class="cn">32</span>] = tl_trace.span_id[<span class="cn">16</span>] = <span class="cn">'\0'</span>;
}

<span class="ck">static inline</span> <span class="cs">const char</span> *<span class="cf">get_iso8601</span>(<span class="cs">char</span> *buf, <span class="cs">size_t</span> n) {
    <span class="cs">struct timespec</span> ts;
    clock_gettime(CLOCK_REALTIME, &amp;ts);
    <span class="cs">struct tm</span> *tm = gmtime(&amp;ts.tv_sec);
    <span class="cs">int</span> len = strftime(buf, n, <span class="cv">"%Y-%m-%dT%H:%M:%S"</span>, tm);
    snprintf(buf + len, n - len, <span class="cv">".%03ldZ"</span>, ts.tv_nsec / <span class="cn">1000000</span>);
    <span class="ck">return</span> buf;
}

<span class="cm">/* JSON-escape a string (handles quotes and backslashes) */</span>
<span class="ck">static inline</span> <span class="cs">void</span> <span class="cf">json_escape</span>(<span class="cs">char</span> *dst, <span class="cs">size_t</span> dsz,
                                <span class="cs">const char</span> *src) {
    <span class="cs">size_t</span> d = <span class="cn">0</span>;
    <span class="ck">for</span> (<span class="cs">size_t</span> s = <span class="cn">0</span>; src[s] &amp;&amp; d + <span class="cn">2</span> &lt; dsz; s++) {
        <span class="ck">if</span> (src[s] == <span class="cn">'"'</span> || src[s] == <span class="cn">'\\'</span>) dst[d++] = <span class="cn">'\\'</span>;
        dst[d++] = src[s];
    }
    dst[d] = <span class="cn">'\0'</span>;
}

<span class="cs">#define</span> LOG(level, msg_fmt, ...) <span class="ck">do</span> { \
    <span class="cs">char</span> _ts[<span class="cn">32</span>], _msg[<span class="cn">512</span>], _esc[<span class="cn">512</span>]; \
    get_iso8601(_ts, <span class="ck">sizeof</span>(_ts)); \
    snprintf(_msg, <span class="ck">sizeof</span>(_msg), msg_fmt, ##__VA_ARGS__); \
    json_escape(_esc, <span class="ck">sizeof</span>(_esc), _msg); \
    fprintf(stdout, \
        <span class="cv">"{\"ts\":\"%s\",\"level\":\"%s\",\"service\":\"order-svc\"," \</span>
        <span class="cv">"\"trace_id\":\"%s\",\"span_id\":\"%s\",\"msg\":\"%s\"}\n"</span>, \
        _ts, level, tl_trace.trace_id, tl_trace.span_id, _esc); \
} <span class="ck">while</span>(<span class="cn">0</span>)

<span class="cs">#define</span> LOG_INFO(fmt,  ...) LOG(<span class="cv">"INFO"</span>,  fmt, ##__VA_ARGS__)
<span class="cs">#define</span> LOG_WARN(fmt,  ...) LOG(<span class="cv">"WARN"</span>,  fmt, ##__VA_ARGS__)
<span class="cs">#define</span> LOG_ERROR(fmt, ...) LOG(<span class="cv">"ERROR"</span>, fmt, ##__VA_ARGS__)

<span class="cm">/* Usage: */</span>
<span class="cm">/* log_set_trace("4bf92f3577b34da6a3ce929d", "00f067aa0ba902b7"); */</span>
<span class="cm">/* LOG_INFO("order placed order_id=%s amount=%.2f", order_id, amount); */</span></div>
  </div>
</div>

<div class="sep">── Implementation 3 — Token Bucket Rate Limiter ──</div>

<div class="cp p-teal">
  <div class="cp-hdr">🪣 Token Bucket Rate Limiter (Thread-Safe, C11 Atomics)</div>
  <div class="cp-body">
<div class="cb"><span class="cm">/* token_bucket.h — thread-safe token bucket rate limiter */</span>
<span class="cs">#pragma once</span>
<span class="cs">#include</span> &lt;stdatomic.h&gt;
<span class="cs">#include</span> &lt;time.h&gt;
<span class="cs">#include</span> &lt;stdbool.h&gt;

<span class="cs">typedef struct</span> {
    _Atomic(<span class="cs">long</span>) tokens_us;     <span class="cm">/* tokens * 1e6 (avoid float atomics) */</span>
    _Atomic(<span class="cs">long</span>) last_refill_us; <span class="cm">/* last refill time in microseconds */</span>
    <span class="cs">long</span>           capacity_us;    <span class="cm">/* max tokens * 1e6 */</span>
    <span class="cs">long</span>           rate_us;        <span class="cm">/* tokens added per microsecond * 1e6 */</span>
} token_bucket_t;

<span class="ck">static inline</span> <span class="cs">long</span> <span class="cf">now_us</span>(<span class="cs">void</span>) {
    <span class="cs">struct timespec</span> ts;
    clock_gettime(CLOCK_MONOTONIC, &amp;ts);
    <span class="ck">return</span> ts.tv_sec * <span class="cn">1000000LL</span> + ts.tv_nsec / <span class="cn">1000</span>;
}

<span class="ck">static inline</span> <span class="cs">void</span> <span class="cf">tb_init</span>(token_bucket_t *tb,
                              <span class="cs">double</span> rate_per_sec, <span class="cs">double</span> capacity) {
    tb-&gt;capacity_us = (<span class="cs">long</span>)(capacity * <span class="cn">1e6</span>);
    tb-&gt;rate_us     = (<span class="cs">long</span>)(rate_per_sec);  <span class="cm">/* tokens/sec → tokens/us = rate/1e6 */</span>
    atomic_store(&amp;tb-&gt;tokens_us,     tb-&gt;capacity_us);
    atomic_store(&amp;tb-&gt;last_refill_us, now_us());
}

<span class="cm">/* Returns true if request is allowed; false if rate-limited */</span>
<span class="ck">static inline</span> <span class="cs">bool</span> <span class="cf">tb_allow</span>(token_bucket_t *tb) {
    <span class="cs">long</span> now = now_us();
    <span class="cs">long</span> last = atomic_exchange(&amp;tb-&gt;last_refill_us, now);
    <span class="cs">long</span> elapsed_us = now - last;

    <span class="cm">/* Add tokens for elapsed time: tokens += rate * elapsed_us */</span>
    <span class="cs">long</span> new_tokens = tb-&gt;rate_us * elapsed_us / <span class="cn">1000000</span>;
    <span class="ck">if</span> (new_tokens &gt; <span class="cn">0</span>) {
        <span class="cs">long</span> current = atomic_fetch_add(&amp;tb-&gt;tokens_us,
                                         new_tokens * <span class="cn">1000000LL</span>);
        <span class="cm">/* Cap at capacity */</span>
        <span class="ck">if</span> (current + new_tokens * <span class="cn">1000000LL</span> &gt; tb-&gt;capacity_us)
            atomic_store(&amp;tb-&gt;tokens_us, tb-&gt;capacity_us);
    }

    <span class="cm">/* Try to consume one token */</span>
    <span class="cs">long</span> one_token = <span class="cn">1000000LL</span>;
    <span class="cs">long</span> prev = atomic_fetch_sub(&amp;tb-&gt;tokens_us, one_token);
    <span class="ck">if</span> (prev &gt;= one_token) <span class="ck">return</span> <span class="cn">true</span>;   <span class="cm">/* allowed */</span>

    <span class="cm">/* Not enough tokens: restore */</span>
    atomic_fetch_add(&amp;tb-&gt;tokens_us, one_token);
    <span class="ck">return</span> <span class="cn">false</span>;  <span class="cm">/* rate limited */</span>
}

<span class="cm">/* Usage: */</span>
<span class="cm">/* token_bucket_t per_client_bucket; */</span>
<span class="cm">/* tb_init(&per_client_bucket, 100.0, 200.0); // 100 req/sec, burst=200 */</span>
<span class="cm">/* if (!tb_allow(&per_client_bucket)) { respond_429(); return; } */</span></div>
  </div>
</div>

</div><!-- /t-impl -->

<!-- ══════════════════════════════════════════════════════════
     TAB 9 — Labs & Checklist
     ══════════════════════════════════════════════════════════ -->
<div id="t-labs" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 1 — Prometheus Metrics + Grafana Dashboard</div>
  <div class="lab-body">
    Instrument a C service and build a RED dashboard in Grafana.
    <div class="lab-step"><span class="sn">1</span> Add the metrics module from Tab 8 to the health check HTTP server (M15 Tab 8). Expose <code>/metrics</code> on port 8081 alongside <code>/health/live</code>.</div>
    <div class="lab-step"><span class="sn">2</span> Run Prometheus locally: <code>docker run -p 9090:9090 -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus</code>. Configure <code>prometheus.yml</code> to scrape <code>localhost:8081/metrics</code> every 15s.</div>
    <div class="lab-step"><span class="sn">3</span> Generate load with <code>wrk -t4 -c100 -d30s http://localhost:8080/orders</code>. Watch metrics accumulate at <code>http://localhost:9090</code>.</div>
    <div class="lab-step"><span class="sn">4</span> Run Grafana: <code>docker run -p 3000:3000 grafana/grafana</code>. Add Prometheus as data source. Build a RED dashboard with three panels: request rate, error rate %, p99 latency.</div>
    <div class="lab-step"><span class="sn">5</span> Add a Prometheus alerting rule: fire if error rate &gt; 1% for 2 minutes. Simulate errors by making your handler return 500 randomly. Watch the alert move from PENDING to FIRING.</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 2 — Distributed Trace Propagation</div>
  <div class="lab-body">
    Implement W3C traceparent propagation across two C services.
    <div class="lab-step"><span class="sn">1</span> Build Service A (port 8080) and Service B (port 8081). Both run the structured logger from Tab 8.</div>
    <div class="lab-step"><span class="sn">2</span> Service A: on each request, generate a <code>trace_id</code> (UUID) + <code>span_id</code>. If the request already has <code>traceparent</code>, extract the trace_id and create a child span_id.</div>
    <div class="lab-step"><span class="sn">3</span> Service A calls Service B via HTTP, forwarding the <code>traceparent</code> header. Service B logs with the same trace_id from the header.</div>
    <div class="lab-step"><span class="sn">4</span> Send a request to Service A. In the combined log output, grep for the trace_id — verify both service logs appear with the same trace_id, showing the full request chain.</div>
    <div class="lab-step"><span class="sn">5</span> <strong>Bonus:</strong> run Jaeger locally (<code>docker run -p 16686:16686 jaegertracing/all-in-one</code>). Use the OTel C SDK to export spans to Jaeger and view the trace waterfall.</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 3 — Token Bucket Rate Limiter Under Load</div>
  <div class="lab-body">
    Verify rate limiter correctness under concurrent load.
    <div class="lab-step"><span class="sn">1</span> Integrate the token bucket from Tab 8 into the HTTP server. Return <code>429 Too Many Requests</code> with <code>Retry-After</code> header when rate-limited.</div>
    <div class="lab-step"><span class="sn">2</span> Configure: 100 req/sec rate, 150 token burst capacity.</div>
    <div class="lab-step"><span class="sn">3</span> Burst test: send 200 requests simultaneously. Verify exactly ~150 succeed and ~50 receive 429. Check Prometheus counter: <code>http_requests_total{status="4xx"}</code>.</div>
    <div class="lab-step"><span class="sn">4</span> Sustained test: <code>wrk -t8 -c100 -d60s</code> at 1000 req/sec (10× limit). Verify roughly 100 req/sec succeed and the rest 429. The rate should be stable over the 60s window.</div>
    <div class="lab-step"><span class="sn">5</span> Concurrency test: 8 threads all decrementing the same bucket simultaneously for 10 seconds. Verify no race conditions using TSan: <code>clang -fsanitize=thread</code>.</div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr">🔬 Lab 4 — Security: SQL Injection &amp; SSRF Prevention</div>
  <div class="lab-body">
    Demonstrate vulnerability and fix in C using libpq.
    <div class="lab-step"><span class="sn">1</span> Write a vulnerable handler: <code>char query[256]; snprintf(query, sizeof(query), "SELECT * FROM orders WHERE id='%s'", user_input); PQexec(conn, query);</code>. Try input: <code>'; DROP TABLE orders; --</code>. Verify it executes.</div>
    <div class="lab-step"><span class="sn">2</span> Fix it: use <code>PQexecParams(conn, "SELECT * FROM orders WHERE id=$1", 1, NULL, params, NULL, NULL, 0)</code>. Retry the injection — verify it returns no results (treats the entire input as a literal string).</div>
    <div class="lab-step"><span class="sn">3</span> Write the SSRF-vulnerable handler: accept a URL from request body and fetch it with libcurl. Try the AWS metadata endpoint: <code>http://169.254.169.254/latest/meta-data/</code>. Verify it returns data.</div>
    <div class="lab-step"><span class="sn">4</span> Fix it: integrate <code>safe_fetch_url()</code> from Tab 6. Verify the metadata URL is blocked. Verify a legitimate allowlisted URL succeeds.</div>
  </div>
</div>

<div class="sep">── Phase 7 Mastery Checklist ──</div>

<div class="two-col">
  <div>
    <strong style="color:#9f1239">Observability</strong>
    <ul class="cl">
      <li>Explain the 3 pillars and what question each answers</li>
      <li>Write a structured JSON log line with all mandatory fields</li>
      <li>List what must never appear in logs (secrets, PII)</li>
      <li>Explain how trace_id links logs across services</li>
    </ul>
    <strong style="color:#9f1239">Metrics</strong>
    <ul class="cl">
      <li>Distinguish counter, gauge, histogram, summary</li>
      <li>Write PromQL for request rate, error rate %, and p99 latency</li>
      <li>Apply RED method to a service and USE method to a resource</li>
      <li>Explain why high-cardinality labels are dangerous in Prometheus</li>
      <li>Write a Prometheus alerting rule with <code>for</code> duration</li>
    </ul>
    <strong style="color:#9f1239">Tracing</strong>
    <ul class="cl">
      <li>Explain trace, span, parent_span_id relationship</li>
      <li>Parse and construct a W3C traceparent header</li>
      <li>Choose the right sampling strategy for given traffic/budget</li>
    </ul>
  </div>
  <div>
    <strong style="color:#9f1239">Alerting &amp; SLO</strong>
    <ul class="cl">
      <li>Define SLI, SLO, SLA, Error Budget</li>
      <li>Write a burn rate alert (faster than threshold-crossing alerts)</li>
      <li>Explain why alerting on symptoms is better than causes</li>
    </ul>
    <strong style="color:#9f1239">Security</strong>
    <ul class="cl">
      <li>Fix SQL injection with parameterized queries in libpq</li>
      <li>Block SSRF with allowlist + RFC-1918 IP check</li>
      <li>Explain broken access control with a concrete example</li>
      <li>Describe dynamic secrets (Vault) vs static env vars</li>
      <li>Write allowlist input validation for a struct field</li>
    </ul>
    <strong style="color:#9f1239">Rate Limiting</strong>
    <ul class="cl">
      <li>Implement token bucket: capacity, rate, burst</li>
      <li>Compare sliding window counter vs fixed window (boundary problem)</li>
      <li>Return correct 429 + Retry-After + X-RateLimit-* headers</li>
    </ul>
  </div>
</div>

<div class="mod-nav">
  <a href="/learning/backend/m15-microservices/" class="nb">← M15: Microservices &amp; Infrastructure</a>
  <a href="/learning/backend/" class="nb">↑ Roadmap</a>
  <span style="color:#94a3b8;font-size:.85rem">Batch 2 coming soon →</span>
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
