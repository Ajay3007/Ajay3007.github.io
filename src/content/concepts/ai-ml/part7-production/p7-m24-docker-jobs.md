---
title: "P7-M24 - Docker & Background Jobs"
description: "Part 7 — Production Deployment · Module 24 of 27 Docker Background Jobs Containerise your AI app, run background workers, and orchestrate with Docker Compose ⏱ 1 Week 🟡…"
domain: ai-ml
track: ai-ml-engineering
module: part7-production
order: 724
ownHeader: true
url: /learning/ai-ml/part7-production/p7-m24-docker-jobs/
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
.note{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
.note p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
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
<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 7 — Production &amp; Deployment &nbsp;·&nbsp; Module 24 of 27</div>
  <div class="mod-title">Docker &amp; Background Jobs</div>
  <div class="mod-subtitle">Containerise your AI app, run background workers, and orchestrate with Docker Compose</div>
  <div class="mod-pills">
<span class="mod-pill">⏱ 1 Week</span>
<span class="mod-pill">🟡 Intermediate</span>
<span class="mod-pill">🔧 Docker · Celery · Redis · Docker Compose</span>
<span class="mod-pill">📋 Prerequisite: P7-M23</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🐳 Dockerfile</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🗂 Docker Compose</button>
  <button class="tab-btn" onclick="vt(event,'t3')">🔄 Background Jobs</button>
  <button class="tab-btn" onclick="vt(event,'t4')">🌿 Celery</button>
  <button class="tab-btn" onclick="vt(event,'t5')">📬 Job Status API</button>
  <button class="tab-btn" onclick="vt(event,'t6')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t7')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">✅ Checklist</button>
</div>
<!-- ══════════ TAB 0 ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-navy">Container + Queue</span></div>
  <div class="cp-body">
<p>Two infrastructure skills that every production AI app needs: Docker to make your app portable and reproducible, and background job queues to handle long-running AI tasks without making users wait.</p>
<ul>
<li><strong>Dockerfile</strong> — production multi-stage build for a FastAPI + AI app</li>
<li><strong>Docker Compose</strong> — orchestrating API + worker + Redis + vector DB as a local stack</li>
<li><strong>Background jobs</strong> — when to offload to a queue vs handle in-request</li>
<li><strong>Celery</strong> — the standard Python task queue, with Redis as broker</li>
<li><strong>Job status API</strong> — polling endpoint so clients can track async job progress</li>
<li><strong>Retry and error handling</strong> — failed task retries, dead letter queues</li>
</ul>
  </div>
</div>
</div>
<!-- ══════════ TAB 1 — DOCKERFILE ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🐳</span><h3>Production Dockerfile — Multi-Stage Build</h3><span class="tag tag-navy">Container</span></div>
  <div class="cp-body">
    

```bash
# Dockerfile — production multi-stage build

# ── Stage 1: dependency builder ───────────────────────
FROM python:3.12-slim AS builder

WORKDIR /build
COPY requirements.txt .

# Install dependencies into /install — separate from app code
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ── Stage 2: production image ─────────────────────────
FROM python:3.12-slim AS production

# Create non-root user — never run as root in production
RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /install /usr/local

# Copy only app code — not tests, docs, or dev files
COPY app/ ./app/
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Health check — Docker monitors this
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3   CMD python -c "import httpx; httpx.get('http://localhost:8000/admin/health').raise_for_status()"

# Production command: gunicorn managing uvicorn workers
CMD ["gunicorn", "app.main:app",
     "--worker-class", "uvicorn.workers.UvicornWorker",
     "--workers", "4",
     "--bind", "0.0.0.0:8000",
     "--timeout", "120",
     "--graceful-timeout", "30"]
```


    

```bash
# .dockerignore — keep image small
__pycache__/
*.pyc
*.pyo
.env
.env.*
.git/
.pytest_cache/
tests/
*.md
chroma_db/         # mount as volume, not baked in
*.log
```


    

```bash
# Build and run
docker build -t ai-api:latest .
docker run -p 8000:8000   --env-file .env   -v $(pwd)/chroma_db:/app/chroma_db   ai-api:latest

# Inspect image layers (find what's making it large)
docker history ai-api:latest
# Or use dive: https://github.com/wagoodman/dive
```


<div class="ins"><p>💡 <strong>Multi-stage builds keep production images small.</strong> The builder stage installs all build tools and dependencies. The production stage copies only the compiled packages — no pip, no build-essentials, no compiler. A typical FastAPI app goes from ~800MB (single stage) to ~200MB (multi-stage) with this pattern.</p></div>
  </div>
</div>
</div><!-- end t1 -->
<!-- ══════════ TAB 2 — DOCKER COMPOSE ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🗂</span><h3>Docker Compose — Local Production Stack</h3><span class="tag tag-navy">Orchestration</span></div>
  <div class="cp-body">
    

```python
# docker-compose.yml — complete AI app stack
version: "3.9"

services:

  # ── FastAPI app ──────────────────────────────────────
  api:
    build: .
    ports:
      - "8000:8000"
    env_file: .env
    environment:
      REDIS_URL: redis://redis:6379
    volumes:
      - chroma_data:/app/chroma_db
    depends_on:
      redis:
        condition: service_healthy
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "python", "-c", "import httpx; httpx.get('http://localhost:8000/admin/health').raise_for_status()"]
      interval: 30s
      timeout: 10s
      retries: 3

  # ── Celery worker ────────────────────────────────────
  worker:
    build: .
    command: celery -A app.worker.celery_app worker --loglevel=info --concurrency=4
    env_file: .env
    environment:
      REDIS_URL: redis://redis:6379
    volumes:
      - chroma_data:/app/chroma_db
    depends_on:
      - redis
    restart: unless-stopped

  # ── Celery Beat (scheduled tasks) ────────────────────
  beat:
    build: .
    command: celery -A app.worker.celery_app beat --loglevel=info
    env_file: .env
    environment:
      REDIS_URL: redis://redis:6379
    depends_on:
      - redis
    restart: unless-stopped

  # ── Redis (message broker + result backend) ──────────
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes   # persist to disk
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

volumes:
  chroma_data:
  redis_data:

# Commands
# docker compose up --build -d    # start all services detached
# docker compose logs -f api      # follow api logs
# docker compose ps               # show service status
# docker compose down -v          # stop and remove volumes
```


  </div>
</div>
</div><!-- end t2 -->
<!-- ══════════ TAB 3 — BACKGROUND JOBS ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>When to Use Background Jobs</h3><span class="tag tag-navy">Architecture Decision</span></div>
  <div class="cp-body">
<p>Not all AI work belongs in the request-response cycle. Background jobs handle long-running, expensive, or retry-able work without blocking the API.</p>
<table style="width:100%;border-collapse:collapse;font-size:.84rem;margin:.8rem 0">
<thead><tr style="background:#0c1a40;color:#dbeafe"><th style="padding:.5rem .8rem;text-align:left">Handle In-Request</th><th style="padding:.5rem .8rem">Offload to Queue</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem">Simple Q&A (&lt; 5s)</td><td style="padding:.5rem .8rem">Document ingestion (minutes)</td></tr>
<tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem">Single-turn RAG query</td><td style="padding:.5rem .8rem">Batch embedding 10k documents</td></tr>
<tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem">Streaming chat response</td><td style="padding:.5rem .8rem">Running evaluation harness</td></tr>
<tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem">Short agent task (&lt; 30s)</td><td style="padding:.5rem .8rem">Long research agent (5+ min)</td></tr>
<tr><td style="padding:.5rem .8rem">Classification / routing</td><td style="padding:.5rem .8rem">Report generation, exports</td></tr>
</tbody>
</table>
    

```bash
# The async job pattern
#
# 1. Client POSTs request → API returns job_id immediately (202 Accepted)
# 2. Worker processes job in background
# 3. Client polls GET /jobs/{job_id} → {"status": "pending" | "running" | "done" | "failed"}
# 4. When done, result available in job response
#
# Alternative: webhooks (POST to client URL when done)
# Alternative: SSE endpoint client subscribes to for job updates
```


  </div>
</div>
</div><!-- end t3 -->
<!-- ══════════ TAB 4 — CELERY ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🌿</span><h3>Celery — Distributed Task Queue</h3><span class="tag tag-navy">Standard</span></div>
  <div class="cp-body">
    

```python
pip install celery redis

# app/worker.py — Celery app and task definitions
from celery import Celery
from celery.utils.log import get_task_logger
import anthropic, os

logger = get_task_logger(__name__)

# Celery app — Redis as broker AND result backend
celery_app = Celery(
    "ai_tasks",
    broker=os.environ.get("REDIS_URL", "redis://localhost:6379/0"),
    backend=os.environ.get("REDIS_URL", "redis://localhost:6379/0"),
)
celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    result_expires=3600,        # results expire after 1 hour
    task_soft_time_limit=300,   # raise SoftTimeLimitExceeded after 5 min
    task_time_limit=360,        # hard kill after 6 min
    worker_max_tasks_per_child=50  # restart worker after 50 tasks (memory leak prevention)
)

# ── Task: ingest documents ────────────────────────────
@celery_app.task(
    bind=True,
    max_retries=3,
    default_retry_delay=60,      # retry after 60s
    name="tasks.ingest_documents"
)
def ingest_documents(self, document_paths: list[str], collection: str) -> dict:
    logger.info(f"Ingesting {len(document_paths)} documents into {collection}")
    try:
        pipeline = DocumentIngestionPipeline(config=IngestionConfig(collection_name=collection))
        results  = pipeline.ingest_directory_files(document_paths)
        return {"status": "success", "chunks_added": results["chunks"], "files": results["files"]}
    except Exception as exc:
        logger.error(f"Ingestion failed: {exc}")
        raise self.retry(exc=exc, countdown=60)   # retry with 60s delay

# ── Task: run research agent ──────────────────────────
@celery_app.task(
    bind=True,
    max_retries=2,
    name="tasks.run_agent"
)
def run_agent_task(self, goal: str, session_id: str) -> dict:
    try:
        result = guarded_agent(goal)
        return result
    except Exception as exc:
        raise self.retry(exc=exc, countdown=30)

# ── Scheduled tasks (beat) ────────────────────────────
from celery.schedules import crontab

celery_app.conf.beat_schedule = {
    "daily-index-cleanup": {
        "task": "tasks.cleanup_stale_documents",
        "schedule": crontab(hour=2, minute=0),   # 2am daily
    },
    "hourly-cache-warm": {
        "task": "tasks.warm_embedding_cache",
        "schedule": crontab(minute=0),           # every hour
    },
}
```


  </div>
</div>
</div><!-- end t4 -->
<!-- ══════════ TAB 5 — JOB STATUS API ══════════ -->
<div id="t5" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">📬</span><h3>Job Status API — Async Job Pattern</h3><span class="tag tag-navy">Production Pattern</span></div>
  <div class="cp-body">
    

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from celery.result import AsyncResult
from typing import Any, Optional
import uuid

router = APIRouter(prefix="/jobs", tags=["jobs"])

class JobSubmitResponse(BaseModel):
    job_id:  str
    status:  str = "queued"
    message: str

class JobStatusResponse(BaseModel):
    job_id:   str
    status:   str       # queued | started | success | failure | revoked
    progress: Optional[float] = None   # 0.0 – 1.0
    result:   Optional[Any]  = None    # populated when status=success
    error:    Optional[str]  = None    # populated when status=failure

# ── Submit: returns job_id immediately ────────────────
class IngestRequest(BaseModel):
    document_paths: list[str]
    collection:     str = "default"

@router.post("/ingest", status_code=202, response_model=JobSubmitResponse)
async def submit_ingestion(request: IngestRequest):
    task = ingest_documents.delay(
        document_paths=request.document_paths,
        collection=request.collection
    )
    return JobSubmitResponse(
        job_id=task.id,
        status="queued",
        message=f"Ingestion job queued. Poll /jobs/{task.id} for status."
    )

# ── Poll: check job status ────────────────────────────
@router.get("/{job_id}", response_model=JobStatusResponse)
async def get_job_status(job_id: str):
    result = AsyncResult(job_id, app=celery_app)

    match result.state:
        case "PENDING":
            return JobStatusResponse(job_id=job_id, status="queued")
        case "STARTED":
            meta = result.info or {}
            return JobStatusResponse(job_id=job_id, status="running",
                                     progress=meta.get("progress"))
        case "SUCCESS":
            return JobStatusResponse(job_id=job_id, status="success",
                                     result=result.result)
        case "FAILURE":
            return JobStatusResponse(job_id=job_id, status="failed",
                                     error=str(result.info))
        case _:
            return JobStatusResponse(job_id=job_id, status=result.state.lower())

# ── Cancel a job ──────────────────────────────────────
@router.delete("/{job_id}")
async def cancel_job(job_id: str):
    celery_app.control.revoke(job_id, terminate=True)
    return {"message": f"Job {job_id} cancelled"}

# ── Report progress from inside a task ────────────────
@celery_app.task(bind=True)
def batch_embed_task(self, texts: list[str]) -> dict:
    total = len(texts)
    for i, text in enumerate(texts):
        embed_and_store(text)
        # Update progress — visible in /jobs/{id}
        self.update_state(
            state="STARTED",
            meta={"progress": (i + 1) / total, "current": i + 1, "total": total}
        )
    return {"embedded": total}
```


  </div>
</div>
</div><!-- end t5 -->
<!-- ══════════ TAB 6 — RESOURCES ══════════ -->
<div id="t6" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
<tr><td class="res-type">Docs</td><td><a href="https://docs.docker.com/develop/develop-images/multistage-build/" target="_blank" rel="noopener">Docker: Multi-Stage Builds — docs.docker.com</a></td><td>Official guide on multi-stage builds for smaller, secure production images.</td></tr>
<tr><td class="res-type">Docs</td><td><a href="https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html" target="_blank" rel="noopener">Celery: First Steps — docs.celeryq.dev</a></td><td>Official Celery quickstart. Covers tasks, workers, beat scheduler, and result backends.</td></tr>
<tr><td class="res-type">Docs</td><td><a href="https://docs.docker.com/compose/" target="_blank" rel="noopener">Docker Compose Documentation — docs.docker.com/compose</a></td><td>Complete Docker Compose reference including healthchecks, depends_on, and volumes.</td></tr>
<tr><td class="res-type">Article</td><td><a href="https://testdriven.io/blog/fastapi-and-celery/" target="_blank" rel="noopener">FastAPI + Celery Tutorial — testdriven.io</a></td><td>End-to-end tutorial combining FastAPI with Celery and Redis. Includes Docker Compose setup.</td></tr>
  </tbody>
</table>
</div>
<!-- ══════════ TAB 7 — PROJECTS ══════════ -->
<div id="t7" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr">
<span>🛠</span>
<span class="proj-title">Containerised AI Stack with Async Document Ingestion</span>
<span class="proj-dur">[Intermediate] 3–4 days</span>
  </div>
  <div class="proj-body">
<p>Containerise your M23 FastAPI app and add an async document ingestion pipeline using Celery.</p>
<h4>Requirements</h4>
<ul>
<li><strong>Dockerfile</strong> — multi-stage build, non-root user, HEALTHCHECK, gunicorn CMD</li>
<li><strong>docker-compose.yml</strong> — api, worker, beat, redis services with healthchecks and volumes</li>
<li><strong>Celery tasks</strong> — ingest_documents task with retry logic and progress reporting</li>
<li><strong>Job API</strong> — POST /jobs/ingest (202), GET /jobs/{id}, DELETE /jobs/{id}</li>
<li><strong>Progress</strong> — task updates state with progress 0.0–1.0; client polls /jobs/{id}</li>
<li><strong>Scheduled task</strong> — daily cleanup of stale embeddings via Celery Beat</li>
</ul>
<h4>Test It</h4>
<ul>
<li>docker compose up, submit 50-document ingestion job, poll until complete</li>
<li>Kill the worker mid-job. Restart it. Verify the job retries and completes.</li>
<li>Verify docker compose ps shows all services healthy</li>
</ul>
<p><strong>Skills:</strong> Multi-stage Docker, Docker Compose healthchecks, Celery tasks + retries + progress, job status polling API</p>
  </div>
</div>
</div>
<!-- ══════════ TAB 8 — LABS ══════════ -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Dockerfile — Build and Inspect</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Build a production Docker image and understand what's inside it.</p>
<div class="lab-step"><div class="sn">1</div><div>Write a single-stage Dockerfile for your FastAPI app. Build it: <code>docker build -t ai-api:single .</code>. Check the size: <code>docker image ls ai-api:single</code>.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Rewrite as a multi-stage build. Build: <code>docker build -t ai-api:multi .</code>. Compare sizes. The multi-stage version should be 30–60% smaller.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Add the non-root user (RUN useradd + USER appuser). Verify: <code>docker run ai-api:multi whoami</code> → prints "appuser" not "root".</div></div>
<div class="lab-step"><div class="sn">4</div><div>Add .dockerignore. Rebuild and verify chroma_db/, .git/, and __pycache__/ are not in the image: <code>docker run ai-api:multi ls -la</code>.</div></div>
<div class="lab-step"><div class="sn">5</div><div>Trigger the HEALTHCHECK: start the container without the app running (override CMD). Verify <code>docker ps</code> shows "unhealthy" after 3 failed checks.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Docker Compose Stack</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Bring up the full multi-service stack and verify all services communicate.</p>
<div class="lab-step"><div class="sn">1</div><div>Write docker-compose.yml with api, worker, redis. Run: <code>docker compose up --build -d</code>. Check all services: <code>docker compose ps</code>.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Verify service startup order: stop redis (<code>docker compose stop redis</code>). Does the api service fail to start? Verify depends_on with condition: service_healthy works.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Test volume persistence: ingest some documents. Stop and remove containers (<code>docker compose down</code> — NOT -v). Restart. Verify documents are still in ChromaDB.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Simulate a worker crash: <code>docker compose kill worker</code>. Submit an ingestion job via the API. Restart the worker: <code>docker compose start worker</code>. Verify the job eventually completes.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Celery Task — Retry and Progress</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Build and test a Celery task with retry logic and progress reporting.</p>
<div class="lab-step"><div class="sn">1</div><div>Write a batch_embed_task that embeds 20 texts. Report progress (0.0–1.0) after each. Poll the job status endpoint every second and print the progress.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Add deliberate failure on the 3rd attempt (raise Exception if self.request.retries < 2). Submit the task. Observe it fails twice then succeeds on retry 3. Check /jobs/{id} during each retry.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Test task time limit: add a deliberate time.sleep(400) in your task (beyond the 300s soft limit). Verify Celery raises SoftTimeLimitExceeded and the job shows as "failed" with a timeout error.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Add Celery Beat with a task that runs every minute (for testing). Verify it fires on schedule: <code>docker compose logs beat</code> should show it enqueuing each minute.</div></div>
  </div>
</div>
</div><!-- end t8 -->
<!-- ══════════ TAB 9 — CHECKLIST ══════════ -->
<div id="t9" class="tab-pane">
<p class="sep">P7-M24 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can write a multi-stage Dockerfile: builder stage for dependencies, production stage for the app</li>
  <li>Always run containers as non-root user (RUN useradd + USER appuser)</li>
  <li>Always include a .dockerignore to exclude .git, __pycache__, .env, chroma_db</li>
  <li>Can add Docker HEALTHCHECK that calls /admin/health</li>
  <li>Know the production CMD: gunicorn with UvicornWorker, not uvicorn directly</li>
  <li>Can write a docker-compose.yml with api, worker, redis services</li>
  <li>Can configure depends_on with condition: service_healthy for startup ordering</li>
  <li>Can configure named volumes for ChromaDB and Redis data persistence</li>
  <li>Know when to offload to a queue: any AI task over 30s or requiring retries</li>
  <li>Can create a Celery app with Redis as broker and result backend</li>
  <li>Can write a Celery task with bind=True, max_retries, and retry on exception</li>
  <li>Can configure task_soft_time_limit and task_time_limit to prevent runaway tasks</li>
  <li>Can report task progress via self.update_state(state="STARTED", meta={"progress": x})</li>
  <li>Can implement a job status API: POST returns 202 + job_id, GET polls AsyncResult</li>
  <li>Can configure Celery Beat for scheduled tasks using crontab</li>
  <li>Completed Lab 1: Dockerfile built with multi-stage, non-root, healthcheck</li>
  <li>Completed Lab 2: Docker Compose stack tested with volume persistence and crash recovery</li>
  <li>Completed Lab 3: Celery task with retry + progress + time limit verified</li>
  <li>Milestone project: containerised AI stack with async ingestion pushed to GitHub</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P7-M25 — Auth, Logging &amp; Observability</strong>. Your app is containerised and has async jobs. M25 covers what you need to see inside a running production system.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/ai-ml/part7-production/p7-m23-fastapi-prod/">← P7-M23: FastAPI Production</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part7-production/p7-m25-auth-logging/">Next: P7-M25 — Auth, Logging &amp; Observability →</a>
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
    const key = 'p7m24-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
