---
title: "Module C4: Observability & SRE"
description: "SYSTEM DESIGN MASTERY · TRACK C · MODULE C4 · WEEK 28 METRICS · LOGS · TRACES · SLO/SLI/SLA · INCIDENT RESPONSE · CHAOS // TRACK C · ADVANCED TOPICS · SITE RELIABILITY…"
domain: system-design
track: system-design-hld
order: 208
chrome: bare
ownHeader: true
url: /learning/system-design/hld/module-c4-observability/
---

<link rel="stylesheet" href="/assets/css/sd-module-c4.css">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=IBM+Plex+Mono:ital,wght@0,300;0,400;0,600;1,400&display=swap" rel="stylesheet">
<header>
  <div class="hdr-bar"></div>
  <div class="hdr-top">
    <span>SYSTEM DESIGN MASTERY · TRACK C · MODULE C4 · WEEK 28</span>
    <span>METRICS · LOGS · TRACES · SLO/SLI/SLA · INCIDENT RESPONSE · CHAOS</span>
  </div>
  <div class="hdr-main">
    <div>
      <div class="hdr-kicker">// TRACK C · ADVANCED TOPICS · SITE RELIABILITY ENGINEERING</div>
      <h1>Observability<br>& <span class="acc">SRE</span></h1>
      <div class="hdr-sub">THREE PILLARS · FOUR GOLDEN SIGNALS · SLO/SLI/SLA<br>ERROR BUDGETS · INCIDENT RESPONSE · CHAOS ENGINEERING</div>
    </div>
    <div class="hdr-stats">
      <div class="hs"><div class="hs-v">3</div><div class="hs-l">PILLARS</div></div>
      <div class="hs"><div class="hs-v">4</div><div class="hs-l">GOLDEN SIGNALS</div></div>
      <div class="hs"><div class="hs-v">99.9%</div><div class="hs-l">EXAMPLE SLO</div></div>
      <div class="hs"><div class="hs-v">C4</div><div class="hs-l">MODULE</div></div>
    </div>
  </div>
  <div class="tag-row">
    <div class="tg" style="color:var(--grn)">Metrics</div>
    <div class="tg" style="color:var(--yel)">Logs</div>
    <div class="tg" style="color:var(--cya)">Traces</div>
    <div class="tg" style="color:var(--bri)">SLI / SLO / SLA</div>
    <div class="tg" style="color:var(--ora)">Error Budget</div>
    <div class="tg" style="color:var(--red)">Alerting</div>
    <div class="tg" style="color:var(--pur)">Incident Response</div>
    <div class="tg" style="color:var(--grn)">Chaos Engineering</div>
  </div>
</header>
<nav class="nav">
  <div class="nt active" onclick="show('pillars',this)">3 Pillars</div>
  <div class="nt" onclick="show('metrics',this)">Metrics</div>
  <div class="nt" onclick="show('logs',this)">Logs</div>
  <div class="nt" onclick="show('traces',this)">Tracing</div>
  <div class="nt" onclick="show('slo',this)">SLI / SLO / SLA</div>
  <div class="nt" onclick="show('budget',this)">Error Budget</div>
  <div class="nt" onclick="show('alerting',this)">Alerting</div>
  <div class="nt" onclick="show('incident',this)">Incident Response</div>
  <div class="nt" onclick="show('chaos',this)">Chaos Engineering</div>
  <div class="nt" onclick="show('tasks',this)">Tasks</div>
  <div class="nt" onclick="show('checklist',this)">Checklist</div>
</nav>
<div class="content">
<!-- PILLARS -->
<div class="view active" id="view-pillars">
  <div class="sh">The Three Pillars of Observability</div>
  <div class="sr">Each pillar answers a different question — you need all three</div>
  <div class="pillars">
    <div class="pil" style="background:rgba(0,200,64,.03)">
      <div class="pil-icon">📊</div>
      <div class="pil-name" style="color:var(--grn)">Metrics</div>
      <div class="pil-q" style="color:var(--grn)">"WHAT IS THE SYSTEM DOING?"</div>
      <div class="pil-body">Aggregated numeric measurements over time. Low storage cost. Excellent for dashboards and alerting. Cannot tell you WHY something is wrong — only THAT something is wrong.</div>
      <div class="pil-tools">Tools: Prometheus, Datadog,<br>CloudWatch, Graphite, VictoriaMetrics</div>
    </div>
    <div class="pil" style="background:rgba(216,192,64,.03)">
      <div class="pil-icon">📋</div>
      <div class="pil-name" style="color:var(--yel)">Logs</div>
      <div class="pil-q" style="color:var(--yel)">"WHAT HAPPENED IN DETAIL?"</div>
      <div class="pil-body">Timestamped records of discrete events. High storage cost. Rich per-event context. Hard to query at scale. Essential for debugging specific incidents once you know where to look.</div>
      <div class="pil-tools">Tools: ELK (Elasticsearch+Kibana),<br>Splunk, Loki+Grafana, CloudWatch Logs</div>
    </div>
    <div class="pil" style="background:rgba(48,200,176,.03)">
      <div class="pil-icon">🔍</div>
      <div class="pil-name" style="color:var(--cya)">Traces</div>
      <div class="pil-q" style="color:var(--cya)">"WHERE IN THE SYSTEM IS IT SLOW?"</div>
      <div class="pil-body">End-to-end journey of a single request across all microservices. Shows latency waterfall. Answers: "Which service is slow?" and "Which dependency is the bottleneck?"</div>
      <div class="pil-tools">Tools: Jaeger, Zipkin, AWS X-Ray,<br>Datadog APM, OpenTelemetry</div>
    </div>
  </div>
  <div class="al grn"><em>The key rule:</em> Metrics tell you SOMETHING is wrong. Logs tell you WHAT happened in a specific component. Traces tell you WHERE in the distributed system the problem lives. An on-call engineer uses all three in sequence: metric alert fires → trace shows which service → logs reveal the root cause.</div>
</div>
<!-- METRICS -->
<div class="view" id="view-metrics">
  <div class="sh">Metrics — The Four Golden Signals</div>
  <div class="sr">Google SRE Book — the four metrics that matter most for any service</div>
  <div class="signals">
    <div class="sig" style="border-top-color:var(--cya)">
      <div class="sig-num" style="color:var(--cya)">1</div>
      <div class="sig-name" style="color:var(--cya)">LATENCY</div>
      <div class="sig-body">How long does a request take? Track p50, p95, p99, p999 — never average (hides outliers). Separate successful latency from error latency.</div>
      <div class="sig-ex">→ p99 API response time<br>→ p999 DB query duration<br>→ Error latency tracked separately</div>
    </div>
    <div class="sig" style="border-top-color:var(--grn)">
      <div class="sig-num" style="color:var(--grn)">2</div>
      <div class="sig-name" style="color:var(--grn)">TRAFFIC</div>
      <div class="sig-body">How much demand is the system receiving? Know your peak — design for 2–3× current peak to handle traffic spikes safely.</div>
      <div class="sig-ex">→ HTTP requests/sec per endpoint<br>→ Messages/sec through Kafka<br>→ Bytes/sec read from disk</div>
    </div>
    <div class="sig" style="border-top-color:var(--red)">
      <div class="sig-num" style="color:var(--red)">3</div>
      <div class="sig-name" style="color:var(--red)">ERRORS</div>
      <div class="sig-body">What fraction of requests are failing? Track error RATE not raw count. Distinguish 4xx (client) from 5xx (server) errors.</div>
      <div class="sig-ex">→ HTTP 5xx rate per endpoint<br>→ Failed Kafka consumer events<br>→ DB transaction rollback rate</div>
    </div>
    <div class="sig" style="border-top-color:var(--ora)">
      <div class="sig-num" style="color:var(--ora)">4</div>
      <div class="sig-name" style="color:var(--ora)">SATURATION</div>
      <div class="sig-body">How "full" is the system? The resource closest to capacity. Saturation predicts problems before they cause errors or timeouts.</div>
      <div class="sig-ex">→ DB connection pool utilization %<br>→ CPU / memory utilization<br>→ Kafka consumer lag</div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">Metric types — Prometheus data model<span class="cb-l">PROMETHEUS</span></div>
<pre class="c"><span class="cm">// COUNTER — monotonically increasing. Use rate() to get per-second rate.</span>
http_requests_total{method="GET", status="200"} 145231
<span class="kw">rate</span>(http_requests_total[<span class="str">5m</span>])  <span class="cm">→ requests/sec over 5-min window</span>
<span class="cm">// GAUGE — current value, can go up or down. Query directly.</span>
process_memory_bytes 524288000          <span class="cm">→ 500MB currently in use</span>
db_connection_pool_active 45            <span class="cm">→ 45 of 100 connections in use</span>
<span class="cm">// HISTOGRAM — distribution in buckets. Enables percentile calculation.</span>
http_request_duration_seconds_bucket{le=<span class="str">"0.05"</span>}  8920   <span class="cm">≤50ms: 8920 requests</span>
http_request_duration_seconds_bucket{le=<span class="str">"0.1"</span>}   9543   <span class="cm">≤100ms: 9543 requests</span>
http_request_duration_seconds_bucket{le=<span class="str">"0.5"</span>}   9981   <span class="cm">≤500ms: 9981 requests</span>
http_request_duration_seconds_bucket{le=<span class="str">"Inf"</span>}  10000   <span class="cm">total: 10000 requests</span>
<span class="cm">// p99: histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))</span>
<span class="cm">// USE method (for resources): Utilization, Saturation, Errors</span>
<span class="cm">// RED method (for services): Rate, Errors, Duration</span></pre>
  </div>
</div>
<!-- LOGS -->
<div class="view" id="view-logs">
  <div class="sh">Logs — Structured & Searchable</div>
  <div class="sr">JSON structured logs beat unstructured text at every scale</div>
  <div class="cb"><div class="cb-top">Structured log — the correct format<span class="cb-l">JSON LOG</span></div>
<pre class="c">{
  <span class="str">"timestamp"</span>:   <span class="str">"2025-03-07T14:23:45.123Z"</span>,
  <span class="str">"level"</span>:        <span class="str">"ERROR"</span>,
  <span class="str">"service"</span>:      <span class="str">"payment-service"</span>,
  <span class="str">"version"</span>:      <span class="str">"v2.4.1"</span>,
  <span class="str">"trace_id"</span>:     <span class="str">"abc123def456"</span>,    <span class="cm">← links to distributed trace</span>
  <span class="str">"span_id"</span>:      <span class="str">"7890abcd"</span>,
  <span class="str">"user_id"</span>:      <span class="str">"u_98765"</span>,          <span class="cm">← hashed if GDPR-sensitive</span>
  <span class="str">"order_id"</span>:     <span class="str">"ord_12345"</span>,
  <span class="str">"message"</span>:      <span class="str">"Payment processing failed"</span>,
  <span class="str">"error_code"</span>:   <span class="str">"CARD_DECLINED"</span>,
  <span class="str">"amount_cents"</span>: 9999,
  <span class="str">"duration_ms"</span>:  234,
  <span class="str">"host"</span>:         <span class="str">"payment-pod-7d4b9c"</span>
}
 
<span class="cm">// log levels: DEBUG (dev) → INFO (business events) → WARN (recoverable)</span>
<span class="cm">//             → ERROR (needs investigation) → FATAL (immediate action)</span>
<span class="cm">// Log pipeline: App → Fluentd/Logstash → Kafka (buffer) → Elasticsearch → Kibana</span>
<span class="cm">// Cheaper alternative: App → Promtail → Loki (label-based) → Grafana</span>
<span class="cm">// TAIL-BASED SAMPLING (preferred):</span>
<span class="cm">// Keep 100% of ERROR/WARN logs. Sample 1% of INFO. Discard DEBUG.</span>
<span class="cm">// Preserves signal, reduces storage cost by ~50x on high-traffic services.</span>
<span class="cm">// Retention tiers:</span>
<span class="cm">// Hot  (Elasticsearch):  7 days   → fast full-text search, recent incidents</span>
<span class="cm">// Warm (S3-backed):      30 days  → slower queries, post-incident review</span>
<span class="cm">// Cold (S3 Glacier):     90 days  → compliance only, rarely queried</span></pre>
  </div>
</div>
<!-- TRACES -->
<div class="view" id="view-traces">
  <div class="sh">Distributed Tracing</div>
  <div class="sr">Follow a single request end-to-end across every service it touches</div>
  <div class="cb"><div class="cb-top">Trace waterfall — spotting the bottleneck at a glance<span class="cb-l">TRACE EXAMPLE</span></div>
<pre class="c"><span class="cm">// Trace: place_order request (trace_id: abc123)</span>
<span class="cm">// Each bar = one span (one service's processing time)</span>
 
Span 1: API Gateway          |████████████████████████| 95ms total
  Span 2: Auth Service         |██| 3ms
  Span 3: Order Service          |████████████████| 80ms total
    Span 4: Feature Store call     |████| 8ms
    Span 5: MySQL write            |████████████| <span class="er">60ms  ← BOTTLENECK</span>
    Span 6: Kafka publish          |██| 4ms
  Span 7: Notification Service   |████| 8ms
 
<span class="cm">// Without tracing: "order service is slow" — check all of its dependencies</span>
<span class="cm">// With tracing: "MySQL write is taking 60ms" — go check DB explain plan, indexes</span>
<span class="cm">// Context propagation via HTTP headers (B3 format, used by Zipkin/Jaeger):</span>
X-B3-TraceId:    <span class="str">abc123def456789</span>   <span class="cm">← same for all spans in this trace</span>
X-B3-SpanId:     <span class="str">7890abcd</span>           <span class="cm">← unique per span</span>
X-B3-ParentSpanId: <span class="str">1234efgh</span>         <span class="cm">← parent span's ID</span>
X-B3-Sampled:    <span class="str">1</span>                  <span class="cm">← 1=sample this trace, 0=don't</span>
<span class="cm">// OpenTelemetry (OTel): vendor-neutral standard</span>
<span class="cm">// Write instrumentation once → export to Jaeger, Datadog, or any backend</span>
<span class="cm">// SDK: Java, Python, Go, Node.js — all supported</span>
<span class="cm">// Sampling strategy:</span>
<span class="cm">// Head-based: decide at trace root (random 1%) — simple but misses rare errors</span>
<span class="cm">// Tail-based: decide after trace completes — keep 100% of errors/slow traces</span>
<span class="cm">// Preferred: tail-based with head-based as fallback</span></pre>
  </div>
</div>
<!-- SLO -->
<div class="view" id="view-slo">
  <div class="sh">SLI / SLO / SLA</div>
  <div class="sr">Define what "reliable" means before you can measure or improve it</div>
  <div class="slo-stack">
    <div class="sl">
      <div class="sl-abbr" style="color:var(--cya)">SLI</div>
      <div class="sl-name"><div class="sl-n">Service Level Indicator</div><div class="sl-s">THE MEASURED METRIC</div></div>
      <div class="sl-body">The actual number you track. A ratio of good events to total events.
Example: <span class="gr">SLI = (requests returning &lt;200ms) / total_requests × 100%</span>
Good SLIs: availability %, latency %, freshness %, correctness %
Bad SLIs: raw request count, uptime of a single server</div>
    </div>
    <div class="sl">
      <div class="sl-abbr" style="color:var(--grn)">SLO</div>
      <div class="sl-name"><div class="sl-n">Service Level Objective</div><div class="sl-s">YOUR INTERNAL TARGET</div></div>
      <div class="sl-body">Your target for the SLI. Set based on what users need, not what's technically easy.
Example: <span class="gr">"99.9% of homepage requests complete in &lt;200ms over a 28-day window"</span>
SLOs are internal — no contracts, no penalties. Drives engineering decisions.</div>
    </div>
    <div class="sl">
      <div class="sl-abbr" style="color:var(--yel)">SLA</div>
      <div class="sl-name"><div class="sl-n">Service Level Agreement</div><div class="sl-s">THE CONTRACT</div></div>
      <div class="sl-body">Contractual commitment to customers. With penalties (credits, refunds) if breached.
SLA MUST be weaker than SLO — leave a buffer for incidents + measurement gaps.
<span class="ye">Rule: if SLO = 99.9%, set SLA = 99.5%</span>. Never set SLA = SLO.</div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">Error budget calculation — the math behind the policy<span class="cb-l">MATH</span></div>
<pre class="c"><span class="cm">// Error budget = 100% - SLO = allowed failure rate</span>
 
SLO = <span class="hl">99.9%</span>  →  error budget = <span class="hl">0.1%</span> of requests may fail
  Over 30 days: 0.001 × 30d × 24h × 60m = <span class="gr">43.2 minutes</span> total downtime allowed
 
SLO = <span class="hl">99.99%</span> →  error budget = <span class="hl">0.01%</span>
  Over 30 days: <span class="ye">4.38 minutes</span> total downtime allowed
 
SLO = <span class="hl">99.5%</span>  →  error budget = <span class="hl">0.5%</span>
  Over 30 days: <span class="gr">3.6 hours</span> total downtime allowed
 
<span class="cm">// Choose SLO based on tier, not ambition:</span>
Critical path (payment, auth login):  <span class="ye">99.99%</span>  →  4.38 min/month
Core product (feed, search, API):     <span class="gr">99.9%</span>   → 43.2 min/month
Non-critical (analytics, recs, admin):<span class="gr">99.5%</span>   →  3.6 hr/month
 
<span class="cm">// Tighter SLO = fewer feature deployments = slower iteration</span>
<span class="cm">// Setting 99.99% for everything = no deploys ever = engineering paralysis</span></pre>
  </div>
</div>
<!-- BUDGET -->
<div class="view" id="view-budget">
  <div class="sh">Error Budget Policy</div>
  <div class="sr">Turns reliability into an objective, data-driven conversation between product and engineering</div>
  <div class="eb-rows">
    <div class="eb">
      <div class="eb-dot" style="color:var(--grn)">●</div>
      <div class="eb-range" style="border-top:2px solid var(--grn)"><div class="eb-rng" style="color:var(--grn)">&gt; 50%</div><div class="eb-lbl" style="color:var(--grn)">GREEN — HEALTHY</div></div>
      <div class="eb-policy">Deploy freely. Take calculated risks. Ship experimental features. Iterate fast. The budget is there to be spent on innovation.</div>
    </div>
    <div class="eb">
      <div class="eb-dot" style="color:var(--yel)">●</div>
      <div class="eb-range" style="border-top:2px solid var(--yel)"><div class="eb-rng" style="color:var(--yel)">10–50%</div><div class="eb-lbl" style="color:var(--yel)">YELLOW — CAUTION</div></div>
      <div class="eb-policy">Proceed with caution. Extra review on all deployments. No risky or experimental changes. Fix known reliability issues in next sprint.</div>
    </div>
    <div class="eb">
      <div class="eb-dot" style="color:var(--red)">●</div>
      <div class="eb-range" style="border-top:2px solid var(--red)"><div class="eb-rng" style="color:var(--red)">&lt; 10%</div><div class="eb-lbl" style="color:var(--red)">RED — DANGER</div></div>
      <div class="eb-policy">Freeze all non-critical feature deployments. Full reliability focus. All engineering effort on reducing error rate and technical debt.</div>
    </div>
    <div class="eb">
      <div class="eb-dot" style="color:#888">●</div>
      <div class="eb-range" style="border-top:2px solid #888"><div class="eb-rng" style="color:#ccc">EXHAUSTED</div><div class="eb-lbl" style="color:#888">SLA AT RISK</div></div>
      <div class="eb-policy">Escalate to leadership. Full incident mode until budget resets. Customer credits may be triggered. Post-mortem required before any new deploys.</div>
    </div>
  </div>
  <div class="al grn"><em>Why error budgets work:</em> Without them, product says "ship faster" and engineering says "we need reliability." Both are right but can't agree. With an error budget, the conversation becomes objective: "We have 12 minutes of budget left this month. Your feature has a 20% chance of causing a 5-minute incident. The math says no." Product can accept math — they can't always accept "engineering intuition."</div>
</div>
<!-- ALERTING -->
<div class="view" id="view-alerting">
  <div class="sh">Alerting Design</div>
  <div class="sr">Alert on symptoms, not causes — every alert must be actionable and urgent</div>
  <table class="alert-table">
    <thead><tr><th>LEVEL</th><th>WHEN TO USE</th><th>RESPONSE</th><th>EXAMPLE</th></tr></thead>
    <tbody>
      <tr><td style="color:var(--red)">PAGE</td><td>SLO breach occurring or imminent. Users impacted NOW.</td><td>Wake someone up immediately. Drop everything.</td><td>Error rate &gt;1% for 5 min on payments</td></tr>
      <tr><td style="color:var(--yel)">TICKET</td><td>Degraded performance, not yet breaching SLO. Trend concerning.</td><td>Address next business day. No 3am wake-up.</td><td>p99 latency +30% (still within SLO)</td></tr>
      <tr><td style="color:var(--grn)">LOG</td><td>Informational. No action needed. Useful for dashboards only.</td><td>Review weekly. No alert sent.</td><td>Cache hit rate dropped 5%</td></tr>
    </tbody>
  </table>
  <div class="cb"><div class="cb-top">Burn rate alerting — the Google SRE recommended approach<span class="cb-l">PROMETHEUS ALERT RULES</span></div>
<pre class="c"><span class="cm">// Burn rate = how fast you're consuming the error budget</span>
<span class="cm">// Burn rate 1.0 = consuming at exactly the SLO rate (budget depletes at month end)</span>
<span class="cm">// Burn rate 14.4 = consuming 14.4× faster → 1hr window consumes 2% of 30-day budget</span>
<span class="cm">// FAST BURN — page immediately (short window catches acute outage)</span>
<span class="kw">alert</span>: ErrorBudgetBurnFast
<span class="kw">expr</span>: <span class="fn">rate</span>(http_errors[<span class="str">1h</span>]) / <span class="fn">rate</span>(http_requests[<span class="str">1h</span>]) > (<span class="hl">14.4</span> * 0.001)
<span class="cm">       ^^ error rate            ^^ burns budget 14.4× faster than allowed</span>
<span class="kw">for</span>: 2m
<span class="kw">severity</span>: <span class="er">page</span>
<span class="kw">message</span>: <span class="str">"Fast error budget burn — action required immediately"</span>
<span class="cm">// SLOW BURN — urgent ticket (longer window catches gradual degradation)</span>
<span class="kw">alert</span>: ErrorBudgetBurnSlow
<span class="kw">expr</span>: <span class="fn">rate</span>(http_errors[<span class="str">6h</span>]) / <span class="fn">rate</span>(http_requests[<span class="str">6h</span>]) > (<span class="hl">6</span> * 0.001)
<span class="kw">for</span>: 15m
<span class="kw">severity</span>: <span class="ye">ticket</span>
<span class="cm">// BAD ALERT — avoid "CPU > 80%"</span>
<span class="er">// CPU can be high while system is healthy (batch job running)</span>
<span class="er">// CPU can be low while system is broken (stuck waiting for DB)</span>
<span class="cm">// Alert on what users experience, not what internal resources are doing</span>
<span class="cm">// Alert fatigue rule: if alert fires &gt;1/shift → raise threshold, add duration, or demote</span></pre>
  </div>
</div>
<!-- INCIDENT -->
<div class="view" id="view-incident">
  <div class="sh">Incident Response</div>
  <div class="sr">A structured process ensures fast mitigation and organizational learning</div>
  <div class="sev-grid">
    <div class="sv" style="border-top-color:var(--red)">
      <div class="sv-level" style="color:var(--red)">SEV1</div>
      <div class="sv-name" style="color:var(--red)">CRITICAL</div>
      <div class="sv-body">Complete outage. All customers impacted. C-suite aware. All hands on deck. Revenue loss per minute.</div>
    </div>
    <div class="sv" style="border-top-color:var(--ora)">
      <div class="sv-level" style="color:var(--ora)">SEV2</div>
      <div class="sv-name" style="color:var(--ora)">MAJOR</div>
      <div class="sv-body">Core feature broken. Large % of customers impacted. Urgent escalation. Primary on-call leads.</div>
    </div>
    <div class="sv" style="border-top-color:var(--yel)">
      <div class="sv-level" style="color:var(--yel)">SEV3</div>
      <div class="sv-name" style="color:var(--yel)">MINOR</div>
      <div class="sv-body">Partial degradation. Workaround available. Small % impacted. Address during business hours.</div>
    </div>
    <div class="sv" style="border-top-color:var(--sub)">
      <div class="sv-level" style="color:var(--sub)">SEV4</div>
      <div class="sv-name" style="color:var(--sub)">LOW</div>
      <div class="sv-body">Minor issue. No immediate impact. Tracked in backlog. Fix in next sprint.</div>
    </div>
  </div>
  <div class="timeline">
    <div class="tl-label">// INCIDENT LIFECYCLE — SEV1 example</div>
    <div class="tl-row"><div class="tl-time">T+0m</div><div class="tl-dot" style="background:var(--red)"></div><div class="tl-body" style="color:var(--red)">Alert fires. On-call pages. SEV1 declared. IC assigned.</div></div>
    <div class="tl-row"><div class="tl-time">T+5m</div><div class="tl-dot" style="background:var(--ora)"></div><div class="tl-body">IC assembles team. Scribe opens incident doc. Comms updates status page: "Investigating."</div></div>
    <div class="tl-row"><div class="tl-time">T+12m</div><div class="tl-dot" style="background:var(--yel)"></div><div class="tl-body">TL identifies root cause: bad deploy at T-3m. New model causing OOM on payment pods.</div></div>
    <div class="tl-row"><div class="tl-time">T+15m</div><div class="tl-dot" style="background:var(--yel)"></div><div class="tl-body" style="color:var(--yel)">MITIGATION: rollback deploy. Error rate begins dropping. IC: "Stop the bleeding first."</div></div>
    <div class="tl-row"><div class="tl-time">T+22m</div><div class="tl-dot" style="background:var(--grn)"></div><div class="tl-body" style="color:var(--grn)">Error rate returns to baseline. Service restored. Status page updated: "Resolved."</div></div>
    <div class="tl-row"><div class="tl-time">T+48h</div><div class="tl-dot" style="background:var(--cya)"></div><div class="tl-body" style="color:var(--cya)">Blameless postmortem published. 5 action items filed. No personal blame. 5 Whys completed.</div></div>
  </div>
  <div class="al cya"><em>Blameless postmortem structure:</em> (1) Impact — who affected, for how long, user experience. (2) Timeline — minute-by-minute. (3) Root cause — technical cause using 5 Whys. (4) Contributing factors — systemic issues. (5) Action items — specific, assigned, time-bound. Never write "human error" as root cause — humans made reasonable decisions with available information. Fix the system so the same decision doesn't cause the same failure.</div>
</div>
<!-- CHAOS -->
<div class="view" id="view-chaos">
  <div class="sh">Chaos Engineering</div>
  <div class="sr">Break things deliberately in a controlled way — before production breaks them for you</div>
  <div class="al yel"><em>Chaos Engineering principle:</em> Define a steady state (your SLI baseline). Inject a realistic failure. Observe whether the system maintains steady state. If it does — resilience confirmed. If it doesn't — you found a weakness before your users did. Fix it. Then experiment again.</div>
  <div class="chaos-grid">
    <div class="ce" style="border-left-color:var(--red)">
      <div class="ce-name">Pod Kill</div>
      <div class="ce-body">Terminate a random pod mid-traffic. Does the deployment self-heal? Does the load balancer route around it? How fast?</div>
      <div class="ce-test">Expected: new pod starts in &lt;30s<br>Alert: if error rate spikes &gt;1%<br>Tool: Chaos Monkey, LitmusChaos</div>
    </div>
    <div class="ce" style="border-left-color:var(--ora)">
      <div class="ce-name">AZ Failure</div>
      <div class="ce-body">Cut all traffic to one Availability Zone. Does the system reroute to the other AZs? Does health check remove the AZ?</div>
      <div class="ce-test">Expected: &lt;30s reroute, &lt;1% errors<br>Alert: latency increase during switch<br>Tool: AWS FIS, network rules</div>
    </div>
    <div class="ce" style="border-left-color:var(--yel)">
      <div class="ce-name">Latency Injection</div>
      <div class="ce-body">Add 500ms to all DB calls. Do timeouts fire correctly? Do circuit breakers open? Does the UI show degraded state?</div>
      <div class="ce-test">Expected: timeout after 1s, circuit opens<br>Alert: p99 latency alert fires correctly<br>Tool: TC netem, Toxiproxy</div>
    </div>
    <div class="ce" style="border-left-color:var(--blu)">
      <div class="ce-name">Dependency Down</div>
      <div class="ce-body">Take down a non-critical service (notifications). Does the core path (payment) continue working? Is graceful degradation implemented?</div>
      <div class="ce-test">Expected: core path unaffected<br>Notification failures logged but ignored<br>Tool: iptables, AWS FIS</div>
    </div>
    <div class="ce" style="border-left-color:var(--pur)">
      <div class="ce-name">Resource Exhaustion</div>
      <div class="ce-body">Fill disk to 95% on a node. Does the system alert? Does it continue serving? Does log rotation prevent full disk?</div>
      <div class="ce-test">Expected: alert at 85%, graceful at 95%<br>No data loss from full disk<br>Tool: dd, stress-ng</div>
    </div>
    <div class="ce" style="border-left-color:var(--cya)">
      <div class="ce-name">CPU Spike</div>
      <div class="ce-body">Max out CPU on one node. Does the HPA (Horizontal Pod Autoscaler) kick in? Does load balancer route less traffic to overloaded pod?</div>
      <div class="ce-test">Expected: scale-out in &lt;2 min<br>p99 latency increase &lt;50%<br>Tool: stress-ng, k6 load test</div>
    </div>
  </div>
</div>
<!-- TASKS -->
<div class="view" id="view-tasks">
  <div class="task-list">
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">1</div><div class="t-lbl">SLO Design for E-Commerce Checkout</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>Define 3 SLIs for checkout: availability (% success), latency (% under threshold), and freshness (cart data staleness). Write each as a measurable formula.</li>
          <li>Set SLOs for each. Checkout is revenue-critical; users expect &lt;2s page loads. What SLOs are appropriate?</li>
          <li>Calculate error budgets (minutes/month) for each SLO you chose.</li>
          <li>A deployment causes checkout errors for 8 minutes. How much of the availability budget is consumed? What budget level does that leave? What policy applies?</li>
          <li>Product wants to ship a major checkout redesign with 10% risk of incident. Current error budget consumed: 70%. Make and justify your recommendation.</li>
        </ol>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">2</div><div class="t-lbl">Alerting Strategy for URL Shortener (B5)</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>Define all four golden signals for the URL shortener. What specific metric represents each signal for this service?</li>
          <li>Write 3 alert rules with thresholds and duration windows: one for availability (error rate), one for latency (p99), one for saturation (Redis memory).</li>
          <li>The redirect endpoint returns 404 for 2% of short URLs. Is this a page, ticket, or log? At what 404 rate would it become a page?</li>
          <li>An on-call engineer receives 15 alerts per shift. What is wrong? Name three specific fixes to reduce noise without losing signal.</li>
        </ol>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">3</div><div class="t-lbl">Distributed Tracing for WhatsApp (B7)</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>Define the spans for a message send flow: client → WebSocket server → Kafka → router → chat server → recipient. What is the parent-child relationship?</li>
          <li>Where do you propagate trace context? What HTTP headers? How do you pass trace context through Kafka (hint: Kafka message headers)?</li>
          <li>A user reports "my message took 10 seconds to deliver." Without tracing, how would you debug? With tracing, what specifically do you look for in the waterfall?</li>
          <li>You're sampling 1% of traces. The slow 10-second delivery is in the other 99%. How do you ensure this specific trace was captured? What sampling strategy?</li>
        </ol>
      </div>
    </div>
    <div class="task-card" style="border-top:2px solid var(--grn)">
      <div class="task-hd" onclick="tt(this)"><div class="t-num" style="color:var(--grn)">★</div><div class="t-lbl">Design a Self-Hosted Observability Platform</div><div class="t-meta">~3 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>500 engineers, 5000 microservices, 10 TB/day logs, 1M metrics series, millions of traces/day.</p>
        <ol>
          <li>Metrics pipeline: instrumentation → collection → storage → alerting. Technology choices, scale numbers, retention strategy.</li>
          <li>Log pipeline: ingestion → buffering → indexing → tiered retention. How do you handle 10 TB/day economically? What does the Elasticsearch cluster look like?</li>
          <li>Trace pipeline: instrumentation (OTel) → sampling strategy → storage → query backend. What's your storage choice for traces and why?</li>
          <li>Unified correlation: when an alert fires, how does the on-call engineer navigate from metric → relevant logs → relevant trace in under 60 seconds?</li>
          <li>SLO management at scale: storing, tracking, and alerting on error budgets for 5000 services. Can you use Prometheus for this? What's the schema?</li>
          <li>Top 3 cost optimization strategies for logs and traces without sacrificing observability for incidents.</li>
        </ol>
      </div>
    </div>
  </div>
</div>
<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 24 completed</span><span style="font-family:'Share Tech Mono',monospace">MODULE C4 · OBSERVABILITY & SRE</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Three pillars: metrics (what), logs (what happened), traces (where)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Four golden signals: latency, traffic, errors, saturation</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Track p99 not average — average hides tail latency outliers</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Metric types: counter (rate()), gauge (current), histogram (percentiles)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">RED method (services): Rate, Errors, Duration</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">USE method (resources): Utilization, Saturation, Errors</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Structured JSON logs: trace_id field links logs to traces</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Tail-based log sampling: keep 100% errors, sample 1% normal</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Log retention tiers: hot (7d Elasticsearch), warm (30d), cold (90d Glacier)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Distributed tracing: trace, span, parent-child structure, trace_id propagation</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">B3 headers: X-B3-TraceId, X-B3-SpanId, X-B3-ParentSpanId</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">OpenTelemetry: vendor-neutral, SDK + Collector architecture</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">SLI: measured ratio of good events to total events</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">SLO: internal target — set based on user need, not technical ease</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">SLA: contractual commitment, always weaker than SLO with buffer</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Error budget math: 99.9% SLO → 43.2 min/month budget</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Error budget policy: green/yellow/red/exhausted — what each means for deploys</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Alert on symptoms not causes — actionable + urgent</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Burn rate alerting: fast (1h, 14.4×) = page; slow (6h, 6×) = ticket</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Alert fatigue: &gt;1 page/shift = alert needs tuning</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Incident roles: IC (coordinates), TL (debugs), comms, scribe</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Blameless postmortem: 5 sections, no personal blame, 5 Whys</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Chaos engineering: steady state → inject failure → observe → validate</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Tasks 1–4 completed (SLO design, alerting, tracing, observability platform)</div></div>
  </div>
  <div style="margin-top:28px;background:var(--panel);border:1px solid var(--bord2);padding:22px;border-top:2px solid var(--grn)">
    <div style="font-family:'Share Tech Mono',monospace;font-size:8px;color:var(--muted);letter-spacing:2px;margin-bottom:8px">// NEXT MODULE</div>
    <div style="font-family:'Rajdhani',sans-serif;font-size:26px;font-weight:700;color:var(--white);margin-bottom:6px">C5 — Security Architecture</div>
    <div style="font-family:'Share Tech Mono',monospace;font-size:9.5px;color:var(--sub);line-height:2">
      OAuth2 / OIDC · JWT deep dive · Zero-Trust architecture<br>
      Secrets management · mTLS · API security · OWASP Top 10<br>
      Rate limiting for abuse prevention · DDoS mitigation
    </div>
  </div>
</div>
</div>
<div class="mb-nav">
  <a href="/learning/system-design/hld/module-b13-ml-systems/">← C3 ML Systems</a>
  <a href="/learning/system-design/hld/module-c4-notes/">📄 Study Notes</a>
  <a href="/learning/system-design/system-design-roadmap/">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-c5-security/" class="primary">C5 Security →</a>
</div>
<script src="/assets/js/sd-module-c4.js"></script>
