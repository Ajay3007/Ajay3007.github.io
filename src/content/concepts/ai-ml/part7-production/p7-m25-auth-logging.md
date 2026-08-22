---
title: "P7-M25 - Auth, Logging & Observability"
description: "Part 7 — Production Deployment · Module 25 of 27 Auth, Logging Observability See inside your running AI system — metrics, traces, alerts, and proper auth ⏱ 1 Week 🟡…"
domain: ai-ml
track: ai-ml-engineering
module: part7-production
order: 725
ownHeader: true
url: /learning/ai-ml/part7-production/p7-m25-auth-logging/
---

<style>
.mod-header{background:linear-gradient(135deg,#0f0a1e 0%,#0c1a40 40%,#1e3a5f 70%,#1d4ed8 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#93c5fd;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#dbeafe;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#dbeafe}
.tab-bar{display:flex;flex-wrap:wrap;background:#0c1a40;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#93c5fd;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#60a5fa;border-bottom-color:#60a5fa}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee)}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700;letter-spacing:.04em}
.cp-body{padding:1.1rem 1.2rem}
.cp-body p,.cp-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.cp-body ul{margin:.4rem 0;padding-left:1.4rem}
.cp-body li{margin-bottom:.3rem}
.cp-body h4{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin:.9rem 0 .3rem}
.p-blue .cp-hdr{background:#eff6ff}[data-theme=dark] .p-blue .cp-hdr{background:#0c1a40}
.p-teal .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.p-red .cp-hdr{background:#faeaea}[data-theme=dark] .p-red .cp-hdr{background:#2a0808}
.p-amber .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber .cp-hdr{background:#2a1e00}
.p-navy .cp-hdr{background:#eff6ff}[data-theme=dark] .p-navy .cp-hdr{background:#0c1a40}
.tag-blue{background:#dbeafe;color:#1e40af}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-green{background:#c8e8d4;color:#0e4a28}
.tag-red{background:#f4d0d0;color:#6c1a1a}.tag-amber{background:#fae8a0;color:#5a3800}
.tag-navy{background:#dbeafe;color:#1e3a5f}
.cb{background:#0c1a40;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1d4ed8}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#dbeafe;white-space:pre}
.ck{color:#93c5fd}.cv{color:#f0c080}.cs{color:#60a5fa}
.ins{background:#eff6ff;border:1.5px solid #1d4ed8;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0c1a40;border-color:#1d4ed8}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#1e3a5f}[data-theme=dark] .ins strong{color:#60a5fa}
.warn{background:#faeaea;border:1.5px solid #fca5a5;border-left:4px solid #dc2626;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.res-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.84rem}
.res-table th{background:#4a5568;color:#fff;padding:.6rem .9rem;text-align:left;font-weight:600;font-size:.74rem;text-transform:uppercase;letter-spacing:.06em}
.res-table td{padding:.6rem .9rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top}
.res-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.res-table a{color:#1d4ed8;font-weight:500;text-decoration:none}
.res-table a:hover{text-decoration:underline}
.res-type{font-family:monospace;font-size:.74rem;font-weight:700;color:#4a5568}
.lab-box{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;margin:1.2rem 0;overflow:hidden}
.lab-hdr{background:#0c1a40;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-n{background:#1d4ed8;color:#fff;font-size:.72rem;font-family:monospace;font-weight:700;padding:2px 10px;border-radius:12px}
.lab-hdr h4{margin:0;font-size:.95rem;font-weight:700;color:#dbeafe;border:none}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.8rem;font-size:.88rem;line-height:1.65}
.sn{background:#1d4ed8;color:#fff;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem 0;border-bottom:1px solid var(--border-color,#eee);font-size:.88rem;line-height:1.6;cursor:pointer}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";font-size:1rem;flex-shrink:0;margin-top:.05rem;color:#1d4ed8}
.cl li.done::before{content:"☑";color:#059669}
.cl li.done{color:var(--light-text,#888);text-decoration:line-through}
.sep{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--light-text,#888);border-bottom:1px solid var(--border-color,#e4e4e4);padding-bottom:.4rem;margin:2rem 0 1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin:2.5rem 0 1rem;padding-top:1.2rem;border-top:1.5px solid var(--border-color,#e4e4e4)}
.mod-nav a{font-size:.85rem;font-weight:600;color:#1d4ed8;text-decoration:none;padding:.4rem .9rem;border-radius:6px;border:1.5px solid #1d4ed8;transition:all .15s}
.mod-nav a:hover{background:#1d4ed8;color:#fff}
.mod-nav .nb{background:#1d4ed8;color:#fff}
.mod-nav .nb:hover{background:#1e3a8a;border-color:#1e3a8a}
.proj-box{background:#eff6ff;border:1.5px solid #93c5fd;border-radius:10px;overflow:hidden;margin:1.2rem 0}
.proj-hdr{background:#1e40af;color:#fff;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem;flex-wrap:wrap}
.proj-title{font-weight:700;font-size:.92rem}
.proj-dur{font-size:.78rem;opacity:.85;margin-left:auto;font-family:monospace}
.proj-body{padding:.9rem 1.2rem;font-size:.88rem;line-height:1.7}
.proj-body strong{color:#1e40af}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">Part 7 — Production &amp; Deployment &nbsp;·&nbsp; Module 25 of 27</div>
  <div class="mod-title">Auth, Logging &amp; Observability</div>
  <div class="mod-subtitle">See inside your running AI system — metrics, traces, alerts, and proper auth</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 1 Week</span>
    <span class="mod-pill">🟡 Intermediate</span>
    <span class="mod-pill">🔧 Prometheus · Grafana · structlog · Sentry</span>
    <span class="mod-pill">📋 Prerequisite: P7-M24</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">📊 Metrics</button>
  <button class="tab-btn" onclick="vt(event,'t2')">📋 Structured Logs</button>
  <button class="tab-btn" onclick="vt(event,'t3')">🔍 Distributed Tracing</button>
  <button class="tab-btn" onclick="vt(event,'t4')">🚨 Alerting</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🔐 Auth Deep Dive</button>
  <button class="tab-btn" onclick="vt(event,'t6')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t7')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">✅ Checklist</button>
</div>
<!-- ══════════ TAB 0 ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-navy">See Everything</span></div>
  <div class="cp-body">
    <p>A deployed AI system you can't see inside is a liability. When the LLM API starts returning 500 errors at 2am, or a user complains the chatbot is slow, you need instrumentation to diagnose it within seconds — not hours. This module covers the full observability stack.</p>
    <ul>
      <li><strong>Metrics with Prometheus</strong> — request rates, latency histograms, LLM token counters, error rates</li>
      <li><strong>Dashboards with Grafana</strong> — visualising metrics, setting up standard AI API panels</li>
      <li><strong>Structured logging</strong> — production log pipeline, correlation IDs, log aggregation</li>
      <li><strong>Distributed tracing</strong> — tracing requests across API + worker + LLM calls</li>
      <li><strong>Error tracking with Sentry</strong> — capturing exceptions with context in production</li>
      <li><strong>Alerting</strong> — alert rules for error rate, p95 latency, and LLM cost spikes</li>
    </ul>
  </div>
</div>
</div>
<!-- ══════════ TAB 1 — METRICS ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Prometheus Metrics for AI APIs</h3><span class="tag tag-navy">Measure Everything</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install prometheus-client prometheus-fastapi-instrumentator
 
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI, Response
 
<span class="ck"># ── Standard HTTP metrics (auto-instrumented) ─────────</span>
Instrumentator().instrument(app).expose(app)
<span class="ck"># Provides: http_requests_total, http_request_duration_seconds</span>
<span class="ck"># ── Custom AI-specific metrics ────────────────────────</span>
<span class="ck"># Token usage counter — track cost per model per endpoint</span>
llm_tokens = Counter(
    <span class="cs">"llm_tokens_total"</span>,
    <span class="cs">"Total LLM tokens used"</span>,
    labelnames=[<span class="cs">"model"</span>, <span class="cs">"endpoint"</span>, <span class="cs">"token_type"</span>]   <span class="ck"># input | output</span>
)
 
<span class="ck"># LLM call latency histogram</span>
llm_latency = Histogram(
    <span class="cs">"llm_call_duration_seconds"</span>,
    <span class="cs">"LLM API call duration"</span>,
    labelnames=[<span class="cs">"model"</span>, <span class="cs">"endpoint"</span>],
    buckets=[<span class="cv">0.5</span>, <span class="cv">1.0</span>, <span class="cv">2.0</span>, <span class="cv">5.0</span>, <span class="cv">10.0</span>, <span class="cv">30.0</span>]
)
 
<span class="ck"># RAG retrieval quality gauge</span>
rag_avg_score = Gauge(
    <span class="cs">"rag_retrieval_score_avg"</span>,
    <span class="cs">"Rolling average RAG retrieval similarity score"</span>
)
 
<span class="ck"># Active agent sessions</span>
active_agents = Gauge(
    <span class="cs">"agent_sessions_active"</span>,
    <span class="cs">"Number of currently running agent sessions"</span>
)
 
<span class="ck"># Usage example inside an endpoint</span>
import time
 
async def call_llm_instrumented(prompt: str, model: str, endpoint: str) -> str:
    start = time.perf_counter()
    try:
        response = await llm_client.messages.create(
            model=model, max_tokens=<span class="cv">1024</span>,
            messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: prompt}]
        )
        reply = response.content[<span class="cv">0</span>].text
        llm_tokens.labels(model=model, endpoint=endpoint, token_type=<span class="cs">"input"</span>).inc(response.usage.input_tokens)
        llm_tokens.labels(model=model, endpoint=endpoint, token_type=<span class="cs">"output"</span>).inc(response.usage.output_tokens)
        return reply
    finally:
        llm_latency.labels(model=model, endpoint=endpoint).observe(time.perf_counter() - start)
 
<span class="ck"># Expose metrics endpoint</span>
@app.get(<span class="cs">"/metrics"</span>)
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)</pre></div>
    <div class="ins"><p>💡 <strong>Four AI-specific metrics to always instrument:</strong> (1) LLM token counts by model — directly maps to cost. (2) LLM call latency histogram — detect when the API is slow. (3) RAG retrieval scores — quality degradation over time. (4) Agent session count — detect runaway loops. Standard HTTP metrics (request rate, latency, error rate) come free from the Instrumentator.</p></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📈</span><h3>Grafana Dashboard Setup</h3><span class="tag tag-blue">Visualise</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Add Prometheus + Grafana to docker-compose.yml</span>
<span class="ck"># prometheus service</span>
<span class="cs">  prometheus:</span>
<span class="cs">    image: prom/prometheus:latest</span>
<span class="cs">    ports:</span>
<span class="cs">      - "9090:9090"</span>
<span class="cs">    volumes:</span>
<span class="cs">      - ./prometheus.yml:/etc/prometheus/prometheus.yml</span>
<span class="ck"># grafana service</span>
<span class="cs">  grafana:</span>
<span class="cs">    image: grafana/grafana:latest</span>
<span class="cs">    ports:</span>
<span class="cs">      - "3000:3000"</span>
<span class="cs">    environment:</span>
<span class="cs">      GF_SECURITY_ADMIN_PASSWORD: admin</span>
<span class="cs">    volumes:</span>
<span class="cs">      - grafana_data:/var/lib/grafana</span>
<span class="ck"># prometheus.yml — scrape your FastAPI app</span>
<span class="cs">global:</span>
<span class="cs">  scrape_interval: 15s</span>
<span class="cs">scrape_configs:</span>
<span class="cs">  - job_name: "ai-api"</span>
<span class="cs">    static_configs:</span>
<span class="cs">      - targets: ["api:8000"]</span>   <span class="ck"># Docker service name</span>
<span class="ck"># Key Grafana panels for an AI API:</span>
<span class="ck"># 1. Request rate: rate(http_requests_total[5m])</span>
<span class="ck"># 2. p95 latency: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))</span>
<span class="ck"># 3. Error rate: rate(http_requests_total{status=~"5.."}[5m])</span>
<span class="ck"># 4. LLM tokens/hour: rate(llm_tokens_total[1h]) * 3600</span>
<span class="ck"># 5. LLM p95 latency: histogram_quantile(0.95, rate(llm_call_duration_seconds_bucket[5m]))</span></pre></div>
  </div>
</div>
</div><!-- end t1 -->
<!-- ══════════ TAB 2 — STRUCTURED LOGS ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">📋</span><h3>Production Log Pipeline</h3><span class="tag tag-navy">Queryable Logs</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install structlog python-json-logger
 
import structlog, logging, sys
from pythonjsonlogger import jsonlogger
 
<span class="ck"># ── Production structlog configuration ────────────────</span>
def configure_logging(environment: str = <span class="cs">"production"</span>):
    if environment == <span class="cs">"development"</span>:
        <span class="ck"># Human-readable console output for dev</span>
        structlog.configure(
            processors=[
                structlog.contextvars.merge_contextvars,
                structlog.processors.add_log_level,
                structlog.processors.TimeStamper(fmt=<span class="cs">"%H:%M:%S"</span>),
                structlog.dev.ConsoleRenderer(colors=<span class="cv">True</span>)
            ]
        )
    else:
        <span class="ck"># JSON output for production — queryable by log aggregators</span>
        structlog.configure(
            processors=[
                structlog.contextvars.merge_contextvars,
                structlog.processors.add_log_level,
                structlog.processors.TimeStamper(fmt=<span class="cs">"iso"</span>),
                structlog.processors.format_exc_info,
                structlog.processors.JSONRenderer()
            ]
        )
 
logger = structlog.get_logger()
 
<span class="ck"># ── Request correlation — trace a request through all logs</span>
import uuid
from starlette.middleware.base import BaseHTTPMiddleware
 
class CorrelationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        <span class="ck"># Use incoming X-Request-ID or generate new one</span>
        request_id = request.headers.get(<span class="cs">"X-Request-ID"</span>, str(uuid.uuid4())[:8])
        user_id    = getattr(request.state, <span class="cs">"user"</span>, {}).get(<span class="cs">"user_id"</span>, <span class="cs">"anon"</span>)
 
        <span class="ck"># Bind to context — all logs in this request include these fields</span>
        structlog.contextvars.bind_contextvars(
            request_id=request_id,
            user_id=user_id,
            path=request.url.path
        )
        response = await call_next(request)
        structlog.contextvars.clear_contextvars()
        response.headers[<span class="cs">"X-Request-ID"</span>] = request_id
        return response
 
<span class="ck"># All logs now include request_id and user_id automatically</span>
<span class="ck"># Output: {"event":"llm_called","model":"claude...","request_id":"a3f7b2","user_id":"user_1",...}</span>
<span class="ck"># Query in CloudWatch/Datadog/Loki: request_id="a3f7b2" → all logs for that request</span></pre></div>
  </div>
</div>
</div><!-- end t2 -->
<!-- ══════════ TAB 3 — DISTRIBUTED TRACING ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Distributed Tracing with OpenTelemetry</h3><span class="tag tag-navy">End-to-End</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install opentelemetry-api opentelemetry-sdk             opentelemetry-instrumentation-fastapi             opentelemetry-exporter-otlp
 
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
 
<span class="ck"># Setup tracing — sends to Jaeger or any OTLP-compatible backend</span>
provider = TracerProvider()
provider.add_span_processor(
    BatchSpanProcessor(OTLPSpanExporter(endpoint=<span class="cs">"http://jaeger:4317"</span>))
)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)
 
<span class="ck"># Auto-instrument FastAPI and all HTTPX calls (LLM API calls)</span>
FastAPIInstrumentor.instrument_app(app)
HTTPXClientInstrumentor().instrument()
<span class="ck"># Every FastAPI request and every LLM API call now has a trace span</span>
<span class="ck"># Manual spans for custom work</span>
async def rag_pipeline(question: str) -> dict:
    with tracer.start_as_current_span(<span class="cs">"rag.retrieve"</span>) as span:
        span.set_attribute(<span class="cs">"query.length"</span>, len(question))
        chunks = await retrieve(question)
        span.set_attribute(<span class="cs">"chunks.count"</span>, len(chunks))
 
    with tracer.start_as_current_span(<span class="cs">"rag.generate"</span>) as span:
        span.set_attribute(<span class="cs">"model"</span>, <span class="cs">"claude-3-5-sonnet-20241022"</span>)
        answer = await generate(question, chunks)
        span.set_attribute(<span class="cs">"answer.length"</span>, len(answer))
 
    return {<span class="cs">"answer"</span>: answer, <span class="cs">"chunks"</span>: chunks}
 
<span class="ck"># Trace view in Jaeger UI:</span>
<span class="ck"># [GET /rag/ask 450ms]</span>
<span class="ck">#   └─ [rag.retrieve 120ms] chunks=5</span>
<span class="ck">#   └─ [rag.generate 320ms] model=claude-3-5-sonnet</span>
<span class="ck">#        └─ [POST api.anthropic.com/v1/messages 310ms]</span></pre></div>
  </div>
</div>
</div><!-- end t3 -->
<!-- ══════════ TAB 4 — ALERTING ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🚨</span><h3>Alerting — Know Before Your Users Do</h3><span class="tag tag-navy">Proactive</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Sentry for exception tracking</span>
pip install sentry-sdk[fastapi]
 
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.celery import CeleryIntegration
 
sentry_sdk.init(
    dsn=os.environ[<span class="cs">"SENTRY_DSN"</span>],
    environment=os.environ.get(<span class="cs">"ENVIRONMENT"</span>, <span class="cs">"production"</span>),
    integrations=[FastApiIntegration(), CeleryIntegration()],
    traces_sample_rate=<span class="cv">0.1</span>,   <span class="ck"># 10% of requests traced</span>
    profiles_sample_rate=<span class="cv">0.1</span>,
)
<span class="ck"># Any unhandled exception now appears in Sentry with full context:
# stack trace, request headers, user ID, environment, breadcrumbs</span>
<span class="ck"># Add user context so Sentry shows which user triggered the error</span>
from sentry_sdk import set_user, set_extra
 
async def call_with_sentry_context(user: dict, func, *args):
    set_user({<span class="cs">"id"</span>: user[<span class="cs">"user_id"</span>], <span class="cs">"email"</span>: user.get(<span class="cs">"email"</span>)})
    set_extra(<span class="cs">"request_tier"</span>, user.get(<span class="cs">"tier"</span>))
    return await func(*args)
 
<span class="ck"># Prometheus alert rules (prometheus-alerts.yml)</span>
<span class="ck"># Copy into Alertmanager for PagerDuty / Slack / email alerts</span>
 
ALERT_RULES = <span class="cs">"""
groups:
  - name: ai_api_alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Error rate above 5% for 2 minutes"
 
      - alert: HighLLMLatency
        expr: histogram_quantile(0.95, rate(llm_call_duration_seconds_bucket[5m])) > 15
        for: 3m
        labels:
          severity: warning
        annotations:
          summary: "LLM p95 latency above 15s"
 
      - alert: TokenCostSpike
        expr: rate(llm_tokens_total[1h]) * 3600 > 500000
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Token usage spike: >500k tokens/hour"
"""</span></pre></div>
  </div>
</div>
</div><!-- end t4 -->
<!-- ══════════ TAB 5 — AUTH DEEP DIVE ══════════ -->
<div id="t5" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🔐</span><h3>Auth Patterns — OAuth2 and API Key Management</h3><span class="tag tag-navy">Security</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># ── Rotating API keys — never embed keys in clients ───</span>
import secrets, hashlib, sqlite3
from datetime import datetime
 
def generate_api_key() -> tuple[str, str]:
    """Returns (raw_key, hashed_key). Store only the hash."""
    raw = <span class="cs">f"sk-{secrets.token_urlsafe(32)}"</span>
    hsh = hashlib.sha256(raw.encode()).hexdigest()
    return raw, hsh
 
def create_user_api_key(user_id: str, name: str = <span class="cs">"default"</span>) -> str:
    raw, hsh = generate_api_key()
    with sqlite3.connect(<span class="cs">"keys.db"</span>) as conn:
        conn.execute(<span class="cs">"""CREATE TABLE IF NOT EXISTS api_keys (
            hash TEXT PRIMARY KEY, user_id TEXT, name TEXT,
            created_at TEXT, last_used TEXT, is_active INTEGER DEFAULT 1)"""</span>)
        conn.execute(<span class="cs">"INSERT INTO api_keys VALUES (?,?,?,?,?,1)"</span>,
                     (hsh, user_id, name, datetime.utcnow().isoformat(), None))
    return raw   <span class="ck"># show raw key to user ONCE — never store it</span>
 
async def validate_api_key(raw_key: str) -> dict | None:
    hsh = hashlib.sha256(raw_key.encode()).hexdigest()
    with sqlite3.connect(<span class="cs">"keys.db"</span>) as conn:
        row = conn.execute(
            <span class="cs">"SELECT user_id, name FROM api_keys WHERE hash=? AND is_active=1"</span>,
            (hsh,)).fetchone()
        if row:
            conn.execute(<span class="cs">"UPDATE api_keys SET last_used=? WHERE hash=?"</span>,
                         (datetime.utcnow().isoformat(), hsh))
    return {<span class="cs">"user_id"</span>: row[<span class="cv">0</span>], <span class="cs">"key_name"</span>: row[<span class="cv">1</span>]} if row else None
 
def revoke_api_key(hsh: str):
    with sqlite3.connect(<span class="cs">"keys.db"</span>) as conn:
        conn.execute(<span class="cs">"UPDATE api_keys SET is_active=0 WHERE hash=?"</span>, (hsh,))
 
<span class="ck"># ── OAuth2 with Google (social login) ─────────────────</span>
pip install authlib httpx
 
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
 
config = Config(<span class="cs">".env"</span>)
oauth = OAuth(config)
oauth.register(
    name=<span class="cs">"google"</span>,
    server_metadata_url=<span class="cs">"https://accounts.google.com/.well-known/openid-configuration"</span>,
    client_id=config(<span class="cs">"GOOGLE_CLIENT_ID"</span>),
    client_secret=config(<span class="cs">"GOOGLE_CLIENT_SECRET"</span>),
    client_kwargs={<span class="cs">"scope"</span>: <span class="cs">"openid email profile"</span>},
)
 
@router.get(<span class="cs">"/auth/google"</span>)
async def google_login(request: Request):
    redirect_uri = request.url_for(<span class="cs">"google_callback"</span>)
    return await oauth.google.authorize_redirect(request, redirect_uri)
 
@router.get(<span class="cs">"/auth/google/callback"</span>, name=<span class="cs">"google_callback"</span>)
async def google_callback(request: Request):
    token   = await oauth.google.authorize_access_token(request)
    user    = token[<span class="cs">"userinfo"</span>]
    api_key = create_user_api_key(user[<span class="cs">"sub"</span>], name=<span class="cs">"google-oauth"</span>)
    return {<span class="cs">"api_key"</span>: api_key, <span class="cs">"email"</span>: user[<span class="cs">"email"</span>]}</pre></div>
  </div>
</div>
</div><!-- end t5 -->
<!-- ══════════ TAB 6 — RESOURCES ══════════ -->
<div id="t6" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Library</td><td><a href="https://github.com/trallnag/prometheus-fastapi-instrumentator" target="_blank" rel="noopener">Prometheus FastAPI Instrumentator — github.com/trallnag</a></td><td>Zero-config HTTP metrics for FastAPI. Auto-instruments all routes.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://opentelemetry.io/docs/instrumentation/python/" target="_blank" rel="noopener">OpenTelemetry Python — opentelemetry.io/docs</a></td><td>Complete Python OTel instrumentation guide for tracing and metrics.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://docs.sentry.io/platforms/python/integrations/fastapi/" target="_blank" rel="noopener">Sentry FastAPI Integration — docs.sentry.io</a></td><td>Setting up Sentry error tracking with FastAPI and Celery.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://prometheus.io/docs/alerting/latest/alertmanager/" target="_blank" rel="noopener">Prometheus Alertmanager — prometheus.io/docs</a></td><td>Setting up alert rules and routing to Slack, PagerDuty, or email.</td></tr>
  </tbody>
</table>
</div>
<!-- ══════════ TAB 7 — PROJECTS ══════════ -->
<div id="t7" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr">
    <span>🛠</span>
    <span class="proj-title">Full Observability Stack for Your AI API</span>
    <span class="proj-dur">[Intermediate] 3–4 days</span>
  </div>
  <div class="proj-body">
    <p>Add the complete observability layer to your M24 containerised app.</p>
    <h4>Requirements</h4>
    <ul>
      <li><strong>Metrics</strong> — Prometheus scraping /metrics; custom counters for LLM tokens, latency histogram, active agents gauge</li>
      <li><strong>Grafana</strong> — 5 panels: request rate, p95 latency, error rate, tokens/hour, LLM p95 latency</li>
      <li><strong>Structured logs</strong> — JSON in production, request_id + user_id in every log line via CorrelationMiddleware</li>
      <li><strong>Sentry</strong> — exception tracking with user context and environment tag</li>
      <li><strong>Alerts</strong> — 3 Prometheus alert rules: high error rate, high LLM latency, token spike</li>
      <li><strong>API keys</strong> — full DB-backed key management: create, validate, revoke, track last_used</li>
    </ul>
    <p><strong>Skills:</strong> Prometheus, Grafana, structlog, OpenTelemetry, Sentry, API key management</p>
  </div>
</div>
</div>
<!-- ══════════ TAB 8 — LABS ══════════ -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Metrics — Instrument and Dashboard</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Instrument your API and build a Grafana dashboard that answers: is the system healthy right now?</p>
    <div class="lab-step"><div class="sn">1</div><div>Add prometheus-fastapi-instrumentator. Start your app + Prometheus in Docker Compose. Verify /metrics returns data.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Add 3 custom metrics: llm_tokens_total (Counter), llm_call_duration_seconds (Histogram), active_agent_sessions (Gauge). Instrument your LLM calls to update them.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Open Grafana (localhost:3000). Add Prometheus as data source. Create a dashboard with 4 panels: request rate, error rate, p95 HTTP latency, LLM tokens/minute.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Generate load: send 100 requests via a simple script. Watch your dashboard update in real-time. Deliberately trigger some 500 errors and watch the error rate panel spike.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Structured Logs — Trace a Request</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Add correlation IDs and trace a single request through all your logs.</p>
    <div class="lab-step"><div class="sn">1</div><div>Add CorrelationMiddleware that binds request_id and user_id to structlog context. Send a request and verify the JSON log includes both fields.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Add log statements at 3 levels: middleware (request received), service (LLM called), endpoint (response sent). Verify all 3 logs share the same request_id.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Parse your JSONL log file with Python: group all log lines by request_id. For one specific request, print the full trace — every log event in order.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Find all requests with status=500 in your logs. Extract their request_ids. For each, reconstruct what happened leading up to the error using correlated logs.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>API Key Lifecycle</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build and test the complete API key management lifecycle.</p>
    <div class="lab-step"><div class="sn">1</div><div>Implement create_user_api_key(), validate_api_key(), revoke_api_key(). Create 2 keys for the same user.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Make 5 API calls with key 1. Query the database and verify last_used updated correctly for key 1 but not key 2.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Revoke key 1. Verify subsequent API calls with key 1 return 403. Verify key 2 still works.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Try to reconstruct the raw key from the database hash. Verify it's impossible — only SHA-256 is stored. This is the key security property: even database access doesn't expose user keys.</div></div>
  </div>
</div>
</div><!-- end t8 -->
<!-- ══════════ TAB 9 — CHECKLIST ══════════ -->
<div id="t9" class="tab-pane">
<p class="sep">P7-M25 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can add prometheus-fastapi-instrumentator for zero-config HTTP metrics</li>
  <li>Can define custom Prometheus metrics: Counter (tokens), Histogram (latency), Gauge (active sessions)</li>
  <li>Know the 4 AI-specific metrics to always instrument: token counts, LLM latency, RAG scores, agent sessions</li>
  <li>Can expose /metrics endpoint and configure Prometheus to scrape it</li>
  <li>Can add Prometheus + Grafana to docker-compose.yml</li>
  <li>Can write PromQL for: request rate, p95 latency, error rate, token usage</li>
  <li>Can configure structlog for JSON output in production and ColourConsoleRenderer in development</li>
  <li>Can implement CorrelationMiddleware that binds request_id + user_id to all log lines</li>
  <li>Know that all logs for a request should share the same request_id — enabling full request tracing</li>
  <li>Can set up OpenTelemetry auto-instrumentation for FastAPI and HTTPX</li>
  <li>Can add manual spans with tracer.start_as_current_span() and set_attribute()</li>
  <li>Can initialise Sentry with FastAPI and Celery integrations and set_user() context</li>
  <li>Know the 3 critical alert rules: high error rate (&gt;5%), LLM p95 latency (&gt;15s), token spike</li>
  <li>Can implement DB-backed API key management: generate (show once), hash-store, validate, revoke</li>
  <li>Know to store only SHA-256 hash of API keys — raw keys are never recoverable from the database</li>
  <li>Completed Lab 1: metrics instrumented, Grafana dashboard with 4 panels</li>
  <li>Completed Lab 2: structured logs with request tracing via correlation IDs</li>
  <li>Completed Lab 3: API key lifecycle including revocation and security verification</li>
  <li>Milestone project pushed to GitHub: full observability stack</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P7-M26 — Prompt Versioning, Cost Monitoring &amp; Caching</strong>. With observability in place, M26 covers the AI-specific production layer: managing prompt changes safely, tracking costs, and caching LLM calls.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/ai-ml/part7-production/p7-m24-docker-jobs/">← P7-M24: Docker &amp; Jobs</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part7-production/p7-m26-prompt-versioning/">Next: P7-M26 — Prompt Versioning →</a>
</div>
<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.cl li').forEach((li, i) => {
    const key = 'p7m25-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
