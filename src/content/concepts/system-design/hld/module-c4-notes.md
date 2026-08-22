---
title: "Module C4: Observability & SRE — Study Notes"
description: "Module C4 · Week 28 · Track C — Advanced Topics Prerequisites: B1–B14, C1–C3 Goal: Metrics, tracing, logging, SLOs/SLAs, incident response, SRE practices ⚡ Interactive Visual…"
domain: system-design
track: system-design-hld
order: 209
chrome: bare
ownHeader: true
url: /learning/system-design/hld/module-c4-notes/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<div style="margin-bottom:24px;padding:14px 20px;background:#e0f8e6;border-left:4px solid #00c840;border-radius:0 4px 4px 0;font-family:'IBM Plex Mono',monospace;font-size:13px;">
  <strong>Module C4 · Week 28 · Track C — Advanced Topics</strong><br>
  <span style="color:#666;">Prerequisites: B1–B14, C1–C3 &nbsp;|&nbsp; Goal: Metrics, tracing, logging, SLOs/SLAs, incident response, SRE practices</span>
</div>

<a href="/learning/system-design/hld/module-c4-observability/" style="display:inline-block;margin-bottom:32px;padding:10px 20px;background:#00c840;color:#000;border-radius:4px;text-decoration:none;font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;">⚡ Interactive Visual Version</a>

# Module C4 — Observability & SRE
## System Design Mastery Course | Track C: Advanced Topics | Week 28

---

## 🎯 Module Overview

**Duration:** 1 Week | **Track:** C — Advanced Topics
**Prerequisites:** B1–B12, C1–C3
**Goal:** Observability is what separates systems that can be debugged from systems that are black boxes. SRE practices are what keep those systems reliable at scale. This module covers the three pillars (metrics, logs, traces), SLO/SLI/SLA design, alerting, incident response, and chaos engineering — all topics that appear in both behavioral and system design interviews.

---

## 1. The Three Pillars of Observability

```
METRICS — "What is the system doing right now, numerically?"
  Aggregated numeric measurements over time.
  Low storage cost. Good for dashboards and alerting.
  Cannot tell you WHY something is wrong.
  Tools: Prometheus, Datadog, CloudWatch, Graphite

LOGS — "What happened, in detail?"
  Timestamped records of discrete events.
  High storage cost. Rich context per event.
  Hard to query at scale. Essential for debugging specific incidents.
  Tools: Elasticsearch + Kibana (ELK), Splunk, Loki + Grafana

TRACES — "How did this specific request flow through the system?"
  End-to-end journey of a single request across services.
  Correlates latency breakdown across microservices.
  Answers: "Which service is slow?" and "Why did this request fail?"
  Tools: Jaeger, Zipkin, AWS X-Ray, Datadog APM

The key insight:
  Metrics tell you SOMETHING is wrong.
  Logs tell you WHAT happened in a specific component.
  Traces tell you WHERE in the distributed system the problem is.
  You need all three. Each answers a different question.
```

---

## 2. Metrics Deep Dive

### The Four Golden Signals (Google SRE Book)
```
1. LATENCY — how long does a request take?
   Track p50, p95, p99, p999 — NOT average (hides outliers)
   Separate successful latency from error latency (errors can be fast but wrong)
   Example: p99 API response time

2. TRAFFIC — how much demand is the system receiving?
   Requests per second, messages per second, bytes per second
   Know your peak — design for 2–3× current peak
   Example: HTTP requests/sec per endpoint

3. ERRORS — what fraction of requests are failing?
   Error rate = errors / total requests (not raw count)
   Distinguish: 4xx (client errors) vs 5xx (server errors)
   Example: HTTP 5xx error rate per endpoint

4. SATURATION — how "full" is the system?
   The resource closest to capacity: CPU, memory, disk I/O, queue depth
   Saturation predicts problems before they cause errors
   Example: database connection pool utilization %
```

### Metrics Types
```
Counter: monotonically increasing value. Never decreases. Resets on restart.
  Use for: request count, error count, bytes sent
  Query: rate(http_requests_total[5m]) — per-second rate over 5-min window

Gauge: current value. Can go up or down.
  Use for: active connections, memory usage, queue depth, temperature
  Query: process_memory_bytes — current value

Histogram: distribution of values in configurable buckets.
  Use for: latency distribution, request size distribution
  Stores: count of observations per bucket + total sum + total count
  Enables: calculate percentiles (p50, p99) at query time
  Example: http_request_duration_seconds_bucket{le="0.1"} = 9543 (9543 requests ≤ 100ms)

Summary: pre-calculated quantiles. Less flexible than histogram.
  Use when: client-side percentile calculation preferred
  Limitation: cannot aggregate across instances (each calculates own quantiles)
```

### RED Method (for services)
```
Rate:   requests per second (throughput)
Errors: error rate (% of requests failing)
Duration: latency distribution (p50/p95/p99)

USE Method (for resources/infrastructure):
Utilization: % of time resource is busy
Saturation:  queue depth, wait time (how much more work than it can handle)
Errors:      error count per resource
```

---

## 3. Logs Deep Dive

```
Structured logging (JSON) — machine-parseable, queryable:
{
  "timestamp": "2025-03-07T14:23:45.123Z",
  "level": "ERROR",
  "service": "payment-service",
  "trace_id": "abc123def456",   ← links to distributed trace
  "span_id": "7890abcd",
  "user_id": "u_98765",
  "order_id": "ord_12345",
  "message": "Payment processing failed",
  "error_code": "CARD_DECLINED",
  "amount_cents": 9999,
  "duration_ms": 234
}

Why structured > unstructured:
  grep on unstructured: slow, brittle, requires regex
  SQL on structured: fast, aggregatable, joinable

Log levels (use consistently):
  DEBUG:   verbose, development only. Never in production by default.
  INFO:    significant business events (order created, user logged in)
  WARN:    unexpected but recoverable (retry succeeded, cache miss)
  ERROR:   operation failed, requires investigation
  FATAL:   service cannot continue, immediate attention required

Sampling logs at scale:
  Logging every request at Google/Meta = petabytes/day
  Head-based sampling: randomly sample X% of all requests
  Tail-based sampling: sample 100% of requests with errors or high latency
  Preferred: tail-based (keeps interesting requests, discards normal ones)

Log pipeline:
  Application → Fluentd/Logstash (collect + parse) → Kafka (buffer)
  → Elasticsearch (index + store) → Kibana (query + dashboard)
  Or: Application → Loki (label-based, cheaper) → Grafana

Retention policy:
  Hot: 7 days in Elasticsearch (fast query)
  Warm: 30 days in cheaper storage (S3-backed)
  Cold: 90 days in S3 Glacier (compliance, rarely queried)
```

---

## 4. Distributed Tracing

```
Problem: a user request in microservices hits 8 services. It's slow. Which one?
  Without tracing: check 8 dashboards, correlate timestamps manually.
  With tracing: single waterfall diagram shows each service's contribution.

Concepts:
  Trace:  the entire journey of one request end-to-end. Has a unique trace_id.
  Span:   one unit of work within a trace (one service's processing). Has span_id.
  Parent span → child spans: tree structure representing call graph.

Example trace for "place order":
  Span 1: API Gateway (12ms total)
    Span 2: Auth Service (3ms)
    Span 3: Order Service (8ms total)
      Span 4: Feature Service call (2ms)
      Span 5: DB write (5ms) ← SLOW, investigate this
    Span 6: Kafka publish (1ms)

Instrumentation:
  HTTP: inject trace_id and span_id into headers (B3 propagation format)
    X-B3-TraceId: abc123
    X-B3-SpanId: def456
    X-B3-ParentSpanId: 789ghi
  Each service: reads headers, creates child span, propagates to downstream calls.

OpenTelemetry (OTel):
  Vendor-neutral instrumentation standard. Write once, send anywhere.
  SDK available for Java, Python, Go, Node.js, etc.
  Collector: receives OTel data, transforms, sends to backend (Jaeger, Datadog, etc.)
  Replacing: OpenCensus + OpenTracing (now merged into OTel)

Trace sampling:
  100% sampling = huge volume + latency overhead from instrumentation
  Typical: 1% head-based sampling + 100% of errors (tail-based)
  Adaptive sampling: increase rate for slow or error requests automatically
```

---

## 5. SLI, SLO, SLA

```
SLI (Service Level Indicator):
  The actual measured metric. Quantifies what you're tracking.
  "What fraction of homepage requests returned in < 200ms?"
  SLI = (good_requests / total_requests) × 100%

SLO (Service Level Objective):
  Your internal target for the SLI. What you aim to achieve.
  "99.9% of homepage requests should return in < 200ms over a 28-day window"
  SLOs are set based on what users need, not what's technically easy.

SLA (Service Level Agreement):
  The contractual commitment to a customer. With penalties if breached.
  "99.5% uptime guaranteed, else 10% credit on monthly bill."
  SLA is always WEAKER than SLO (leave a buffer):
    SLO: 99.9% → SLA: 99.5% (buffer for incidents + measurement)

Error Budget:
  Error budget = 100% - SLO
  For SLO = 99.9%:  error budget = 0.1% of requests allowed to fail
  For 30 days:       0.1% × 30 × 24 × 60 = 43.2 minutes downtime allowed

Error budget policy:
  Budget > 50% remaining: deploy freely, take risks, iterate fast
  Budget 10–50% remaining: proceed with caution, extra review on deployments
  Budget < 10% remaining: freeze non-critical deployments, focus on reliability
  Budget exhausted:        stop all features, full reliability focus until reset

SLO examples by service tier:
  Critical path (payment, auth): SLO = 99.99% → 4.38 min/month budget
  Core product (feed, search):   SLO = 99.9%  → 43.2 min/month budget
  Non-critical (analytics, recs):SLO = 99.5%  → 3.6 hrs/month budget

Good SLI selection:
  Availability SLI: % of requests that returned success (non-5xx)
  Latency SLI:      % of requests completed in < threshold (e.g., 200ms)
  Freshness SLI:    % of data reads returning data < X minutes old
  Correctness SLI:  % of responses returning correct output (sampling + validation)
```

---

## 6. Alerting Design

```
Alert on symptoms, not causes.
  Bad alert:  "CPU > 80%" — CPU can be high and system fine; can be low and broken.
  Good alert: "Error rate > 1% for 5 minutes" — users are experiencing failures.

Alert principles (Rob Ewaschuk, Google):
  Every alert must be ACTIONABLE — if you can't do anything about it, don't alert.
  Every alert must be URGENT — if it can wait until morning, don't page at 3am.
  Alert on user-visible symptoms: error rate, latency, availability.
  Alert on causes only when they predict symptoms before they occur.

Alerting levels:
  PAGE (immediate, wake someone up): SLO breach imminent or occurring.
    Example: error rate > 1% for 5 minutes on payment service.
  TICKET (next business day): degraded performance, not yet breaching SLO.
    Example: p99 latency increased 30% (still within SLO, but concerning).
  LOG (informational, no action): automated report.

Alert fatigue:
  Too many alerts → on-call ignores them → real incidents missed.
  Rule: if an alert fires more than once per shift, it needs tuning.
  Fix: raise threshold, add duration condition, or convert to ticket-level.

Alerting on error budget burn rate:
  Burn rate = how fast you're consuming the error budget.
  Burn rate 1 = consuming budget at exactly the SLO rate.
  Burn rate 14.4 = consuming budget 14.4× faster than sustainable.
    → At this rate, 1-hour window consumes 2% of 30-day budget.
    → Page immediately.
  Multi-window, multi-burn-rate alerts (Google SRE recommendation):
    Fast burn (1h window, rate≥14.4): page immediately
    Slow burn (6h window, rate≥6):    page urgently
    Very slow (3-day window, rate≥1): ticket
```

---

## 7. Incident Response

```
Incident severity levels:
  SEV1 (Critical):   Complete service outage. All hands. C-suite aware.
                     All customers impacted. Escalate immediately.
  SEV2 (Major):      Significant degradation. Core feature broken.
                     Large % of customers impacted.
  SEV3 (Minor):      Partial degradation. Workaround exists.
                     Small % of customers impacted.
  SEV4 (Low):        Minor issue. Tracked in backlog.

Incident response roles:
  Incident Commander (IC): owns the incident. Makes decisions. Delegates.
                            Does NOT debug. Coordinates communication.
  Technical Lead (TL):      leads the technical investigation and fix.
  Communications Lead:      updates status page, internal stakeholders.
  Scribe:                   records timeline, decisions, actions taken.

Incident lifecycle:
  1. Detection: alert fires, customer report, or internal monitoring.
  2. Response: on-call acknowledges alert, assesses severity.
  3. Mitigation: restore service ASAP. Rollback, failover, scaling.
     "Stop the bleeding first. Root cause later."
  4. Resolution: confirm service restored, error rate normal.
  5. Postmortem: within 48 hours.

The OODA loop for incidents:
  Observe: look at metrics, logs, traces.
  Orient:  form a hypothesis about the cause.
  Decide:  choose a mitigation action.
  Act:     execute, then observe again.
  Repeat until mitigated.

Blameless postmortem:
  Goal: learn, not punish. People make good decisions with the information they have.
  Structure:
    1. Impact: who was affected, for how long, what was the user experience?
    2. Timeline: minute-by-minute what happened and who did what?
    3. Root cause: the actual technical cause(s). Use 5 Whys.
    4. Contributing factors: systemic issues that enabled the root cause.
    5. Action items: specific, assigned, time-bound follow-up tasks.
  What NOT to include: personal blame, "human error" as root cause.
```

---

## 8. Error Budget & Chaos Engineering

```
Error Budget Policy (formalized):
  At each weekly reliability review:
    If error budget > 50%: green light for all deployments.
    If error budget 10–50%: yellow — extra review, no risky deploys.
    If error budget < 10%: red — freeze feature deployments, reliability work only.
    If budget exhausted: SLO at risk — escalate to leadership.

  Benefit: objective, data-driven conversation between product and engineering.
  "Can we ship this risky feature?" → "We have 35 min budget remaining this month. No."

Chaos Engineering:
  Deliberately inject failures to find weaknesses before they occur in production.
  "Break things intentionally in a controlled way so real failures don't break you."

Principles:
  1. Define a steady state: what does "normal" look like? (SLI baseline)
  2. Hypothesize that steady state continues during the experiment.
  3. Inject realistic failure: kill a pod, add latency, corrupt a response.
  4. Observe: does the system maintain steady state (within SLO)?
  5. Validate or reject: if state is maintained → resilience confirmed.
                         If disrupted → found a weakness, fix it.

Common chaos experiments:
  Pod kill:          kill a random pod. Does the deployment recover?
  Zone failure:      cut traffic to one AZ. Does the system reroute?
  Latency injection: add 500ms to DB calls. Do timeouts/circuit breakers fire?
  Dependency down:   take down a non-critical service. Does the system degrade gracefully?
  Resource exhaustion: fill disk to 95%. Does the system alert and continue?
  CPU spike:         max out CPU on one node. Does autoscaling kick in?

Tools: Chaos Monkey (Netflix), LitmusChaos (k8s native), AWS Fault Injection Simulator (FIS)

GameDay: scheduled chaos experiment with full team.
  Pick a failure scenario, announce it, run it during business hours.
  Run on production only when you trust your recovery mechanisms.
  Start on staging. Graduate to production over time.
```

---

## 9. On-Call Best Practices

```
Sustainable on-call:
  Target: < 2 pages per shift (anything more = toil).
  Target: no more than 25% of on-call time spent on incidents.
  If exceeded: reduce alert noise, improve automation, fix recurring issues.

Toil: repetitive, manual, automatable work that grows with service scale.
  Example: manually restarting a service every time it runs out of memory.
  SRE principle: eliminate toil. If you do something twice, automate it.

Runbooks:
  Pre-written procedures for known failure modes.
  "When alert X fires, do steps 1, 2, 3."
  Good runbook = new on-call engineer can resolve without tribal knowledge.
  Automate the runbook when possible (auto-remediation).

Escalation policy:
  Primary on-call → 5 min → Secondary on-call → 10 min → Team lead → 15 min → Manager

Post-incident hygiene:
  File follow-up tickets immediately after postmortem.
  Track: reliability debt, toil items, action items from postmortem.
  Review at each sprint: are we making progress on reliability?
```

---

## 📝 Tasks

### Task 1 — SLO Design
Design SLOs for an e-commerce checkout flow:
1. Define 3 SLIs for: availability, latency, and data freshness.
2. Set SLOs for each, given: checkout is revenue-critical, users expect < 2s page loads.
3. Calculate error budgets (in minutes per 30 days) for each SLO.
4. A deployment causes checkout errors for 8 minutes. How much of the error budget is consumed? What policy applies after?
5. Product wants to ship a major checkout redesign (10% risk of incident). Current error budget consumed: 70%. What is your recommendation?

### Task 2 — Alerting Design
Design an alerting strategy for the URL shortener from B5:
1. Define the 4 golden signals for this service. What does each measure specifically?
2. Write 3 alert rules: one for availability, one for latency, one for saturation. Include thresholds and duration windows.
3. Your redirect endpoint is returning 404 for 2% of requests. Is this a page, ticket, or log? At what threshold would it become a page?
4. An on-call engineer receives 15 alerts per shift. What is wrong and how do you fix it?

### Task 3 — Distributed Tracing Design
Add distributed tracing to the WhatsApp system from B7:
1. Define the spans for a message send flow: client → chat server → Kafka → router → recipient.
2. Where do you propagate trace context? What HTTP headers? What Kafka headers?
3. A user reports "my message took 10 seconds to deliver." Without tracing, how would you debug? With tracing, what do you look for?
4. You're sampling 1% of traces. The slow delivery is in the other 99%. How do you ensure this trace was captured?

### ⭐ Task 4 — Design an Observability Platform
Design a self-hosted observability platform for a 500-engineer company (5000 services):
1. Metrics pipeline: from application instrumentation → storage → alerting. Technology choices and scale numbers.
2. Log pipeline: ingestion → buffering → indexing → retention tiers. How do you handle 10 TB/day of logs?
3. Trace pipeline: instrumentation → sampling → storage → query. What storage backend for traces?
4. Unified correlation: how does an on-call engineer go from a metric alert to the relevant logs and trace in one click?
5. SLO management: how do you store, track, and alert on error budgets across 5000 services?
6. Cost optimization: logs and traces are expensive. What are your top 3 strategies to reduce cost without losing observability?

---

## ✅ Completion Checklist

- [ ] Three pillars: metrics (what), logs (what happened), traces (where in the system)
- [ ] Four golden signals: latency, traffic, errors, saturation
- [ ] Metric types: counter (rate), gauge (current), histogram (distribution), summary
- [ ] RED method for services, USE method for infrastructure/resources
- [ ] Structured logging: JSON format, log levels, why structured > unstructured
- [ ] Tail-based log sampling: keep errors and slow requests, discard normal ones
- [ ] Distributed tracing: trace, span, parent-child structure, trace_id propagation
- [ ] OpenTelemetry: vendor-neutral standard, SDK + Collector architecture
- [ ] SLI: measured metric (% of requests meeting threshold)
- [ ] SLO: internal target (99.9% of requests < 200ms over 28 days)
- [ ] SLA: contractual commitment, always weaker than SLO with buffer
- [ ] Error budget: 100% - SLO, policy for green/yellow/red/exhausted
- [ ] Alert on symptoms not causes — actionable + urgent
- [ ] Burn rate alerting: fast burn (page) vs slow burn (ticket)
- [ ] Alert fatigue: > 1 page per shift = alert needs tuning
- [ ] Incident severity: SEV1–SEV4 definitions
- [ ] Incident roles: IC (coordinates), TL (debugs), comms, scribe
- [ ] Blameless postmortem: 5 sections, no personal blame, 5 Whys
- [ ] Chaos engineering: steady state → inject → observe → validate
- [ ] On-call toil: < 2 pages/shift target, automate runbooks
- [ ] Completed Task 1 — SLO design for checkout
- [ ] Completed Task 2 — alerting strategy for URL shortener
- [ ] Completed Task 3 — distributed tracing for WhatsApp
- [ ] Completed Task 4 — observability platform design (capstone)

**→ Next: Module C5 — Security Architecture (OAuth2/OIDC, Zero-Trust, Secrets Management)**

---

<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid #ddd;padding-top:20px;">
  <a href="/learning/system-design/hld/module-b13-notes/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">← C3 ML Systems Notes</a>
  <a href="/learning/system-design/hld/module-c4-observability/" style="padding:12px 24px;border:1px solid #00c840;color:#00c840;border-radius:4px;text-decoration:none;font-weight:600;">⚡ Interactive Module</a>
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-c5-notes/" style="padding:12px 24px;background:#00c840;color:#000;border-radius:4px;text-decoration:none;font-weight:600;">NEXT: C5 Security →</a>
</div>
