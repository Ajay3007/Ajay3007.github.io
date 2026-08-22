---
title: "P7-M23 - FastAPI Production Patterns"
description: "Part 7 — Production Deployment · Module 23 of 27 FastAPI Production Patterns Structure, middleware, dependency injection, and async patterns for AI-powered APIs ⏱ 1 Week 🟡…"
domain: ai-ml
track: ai-ml-engineering
module: part7-production
order: 723
ownHeader: true
url: /learning/ai-ml/part7-production/p7-m23-fastapi-prod/
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
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.p-red .cp-hdr{background:#faeaea}[data-theme=dark] .p-red .cp-hdr{background:#2a0808}
.p-amber .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber .cp-hdr{background:#2a1e00}
.p-navy .cp-hdr{background:#eff6ff}[data-theme=dark] .p-navy .cp-hdr{background:#0c1a40}
.tag-blue{background:#dbeafe;color:#1e40af}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}.tag-red{background:#f4d0d0;color:#6c1a1a}
.tag-amber{background:#fae8a0;color:#5a3800}.tag-navy{background:#dbeafe;color:#1e3a5f}
.cb{background:#0c1a40;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1d4ed8}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#dbeafe;white-space:pre}
.ck{color:#93c5fd}.cv{color:#f0c080}.cs{color:#60a5fa}
.ins{background:#eff6ff;border:1.5px solid #1d4ed8;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0c1a40;border-color:#1d4ed8}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#1e3a5f}[data-theme=dark] .ins strong{color:#60a5fa}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
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
<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 7 — Production &amp; Deployment &nbsp;·&nbsp; Module 23 of 27</div>
  <div class="mod-title">FastAPI Production Patterns</div>
  <div class="mod-subtitle">Structure, middleware, dependency injection, and async patterns for AI-powered APIs</div>
  <div class="mod-pills">
<span class="mod-pill">⏱ 1 Week</span>
<span class="mod-pill">🟡 Intermediate</span>
<span class="mod-pill">🔧 FastAPI · Pydantic v2 · uvicorn · gunicorn</span>
<span class="mod-pill">📋 Prerequisite: P4-M14</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🏗 App Structure</button>
  <button class="tab-btn" onclick="vt(event,'t2')">⚙️ Dependency Injection</button>
  <button class="tab-btn" onclick="vt(event,'t3')">🛡 Middleware</button>
  <button class="tab-btn" onclick="vt(event,'t4')">⚡ Async Patterns</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🔐 Auth & API Keys</button>
  <button class="tab-btn" onclick="vt(event,'t6')">🚀 Deployment</button>
  <button class="tab-btn" onclick="vt(event,'t7')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t9')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t10')">✅ Checklist</button>
</div>
<!-- ══════════ TAB 0 ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-navy">Part 7 Start</span></div>
  <div class="cp-body">
<p>Parts 1–6 taught you to build AI systems. Part 7 teaches you to ship them. FastAPI is the standard Python framework for AI APIs — it is async-native, type-safe, and generates OpenAPI docs automatically. This module covers the production patterns that take a working FastAPI app to a deployable service.</p>
<ul>
<li><strong>App structure</strong> — routers, lifespan events, settings, project layout for production</li>
<li><strong>Dependency injection</strong> — sharing LLM clients, DB connections, and config across endpoints</li>
<li><strong>Middleware</strong> — request logging, rate limiting, CORS, error handling</li>
<li><strong>Async patterns</strong> — background tasks, concurrent requests, avoiding blocking calls</li>
<li><strong>Authentication</strong> — API key validation, JWT tokens, per-user rate limiting</li>
<li><strong>Deployment</strong> — uvicorn + gunicorn, health checks, graceful shutdown</li>
</ul>
  </div>
</div>
</div>
<!-- ══════════ TAB 1 — APP STRUCTURE ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🏗</span><h3>Production App Structure</h3><span class="tag tag-navy">Layout</span></div>
  <div class="cp-body">
    

```python
# Production FastAPI project layout
#
# app/
# ├── main.py          ← app factory, lifespan, mount routers
# ├── config.py        ← settings from environment variables
# ├── dependencies.py  ← shared clients (LLM, DB, cache)
# ├── middleware.py     ← logging, rate limiting, CORS
# ├── routers/
# │   ├── chat.py      ← /chat endpoints
# │   ├── rag.py       ← /search, /ask endpoints
# │   └── admin.py     ← /health, /metrics
# ├── models/
# │   ├── requests.py  ← Pydantic request models
# │   └── responses.py ← Pydantic response models
# └── services/
#     ├── llm.py       ← LLM call wrappers
#     └── rag.py       ← retrieval pipeline

# config.py — all settings from environment
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    anthropic_api_key: str
    openai_api_key:    str = ""
    database_url:      str = "sqlite:///./app.db"
    redis_url:         str = "redis://localhost:6379"
    api_key_secret:    str = "change-me-in-production"
    max_requests_per_minute: int = 60
    environment:       str = "development"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()

# main.py — app factory with lifespan
from contextlib import asynccontextmanager
from fastapi import FastAPI
import anthropic, chromadb

app_state = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: initialise shared resources once
    settings = get_settings()
    app_state["llm_client"]  = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)
    app_state["vector_db"]   = chromadb.PersistentClient(path="./chroma_db")
    print("✓ App started")
    yield
    # Shutdown: clean up
    await app_state["llm_client"].close()
    print("✓ App stopped")

app = FastAPI(title="AI API", version="1.0.0", lifespan=lifespan)

# Mount routers
from routers import chat, rag, admin
app.include_router(chat.router,  prefix="/chat",  tags=["chat"])
app.include_router(rag.router,   prefix="/rag",   tags=["rag"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
```


  </div>
</div>
</div><!-- end t1 -->
<!-- ══════════ TAB 2 — DEPENDENCY INJECTION ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">⚙️</span><h3>Dependency Injection — Share Without Global State</h3><span class="tag tag-navy">Core Pattern</span></div>
  <div class="cp-body">
    

```python
from fastapi import Depends, Request
import anthropic

# dependencies.py — all shared resource providers

def get_llm_client(request: Request) -> anthropic.AsyncAnthropic:
    """Provide the shared LLM client initialised at startup."""
    return request.app.state.llm_client   # stored in lifespan

def get_settings_dep() -> Settings:
    return get_settings()

def get_vector_db(request: Request):
    return request.app.state.vector_db

# Alternative: use app_state dict from lifespan
def get_llm(request: Request) -> anthropic.AsyncAnthropic:
    return app_state["llm_client"]

# In routers — inject dependencies cleanly
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Annotated

router = APIRouter()

class ChatRequest(BaseModel):
    message:    str
    session_id: str = ""
    max_tokens: int = 1024

class ChatResponse(BaseModel):
    reply:      str
    session_id: str
    tokens_used: int

# Type-aliased dependency for cleaner signatures
LLMDep      = Annotated[anthropic.AsyncAnthropic, Depends(get_llm_client)]
SettingsDep = Annotated[Settings, Depends(get_settings_dep)]

@router.post("/message", response_model=ChatResponse)
async def send_message(
    request: ChatRequest,
    client:  LLMDep,         # injected — no global state
    settings: SettingsDep,   # injected — type-safe settings
) -> ChatResponse:
    response = await client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=request.max_tokens,
        messages=[{"role": "user", "content": request.message}]
    )
    return ChatResponse(
        reply=response.content[0].text,
        session_id=request.session_id or "anon",
        tokens_used=response.usage.input_tokens + response.usage.output_tokens
    )
```


<div class="ins"><p>💡 <strong>Never create LLM clients inside endpoint functions.</strong> Creating a new <code>anthropic.AsyncAnthropic()</code> on every request means creating a new HTTP connection pool on every request — a significant performance penalty. Always initialise clients once at startup via lifespan and share via dependency injection.</p></div>
  </div>
</div>
</div><!-- end t2 -->
<!-- ══════════ TAB 3 — MIDDLEWARE ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🛡</span><h3>Middleware — Request Lifecycle Hooks</h3><span class="tag tag-navy">Cross-Cutting</span></div>
  <div class="cp-body">
    

```python
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import time, uuid, structlog

logger = structlog.get_logger()

# ── 1. Request ID + Timing middleware ─────────────────
class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        request_id = str(uuid.uuid4())[:8]
        start      = time.perf_counter()

        # Attach request_id to context for all logs in this request
        structlog.contextvars.bind_contextvars(request_id=request_id)

        response = await call_next(request)

        elapsed = round((time.perf_counter() - start) * 1000, 1)
        logger.info("http_request",
                    method=request.method,
                    path=request.url.path,
                    status=response.status_code,
                    latency_ms=elapsed,
                    request_id=request_id)

        response.headers["X-Request-ID"] = request_id
        structlog.contextvars.clear_contextvars()
        return response

# ── 2. Rate limiting middleware ───────────────────────
import asyncio
from collections import defaultdict

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, calls_per_minute: int = 60):
        super().__init__(app)
        self.calls_per_minute = calls_per_minute
        self._counts: dict[str, list] = defaultdict(list)

    def _get_client_id(self, request: Request) -> str:
        return request.headers.get("X-API-Key", request.client.host)

    async def dispatch(self, request: Request, call_next) -> Response:
        client_id = self._get_client_id(request)
        now       = time.time()
        window    = [t for t in self._counts[client_id] if now - t 60]

        if len(window) >= self.calls_per_minute:
            return Response(
                content='{"detail":"Rate limit exceeded. Try again in 60 seconds."}',
                status_code=429,
                headers={"Retry-After": "60",
                         "Content-Type": "application/json"}
            )
        self._counts[client_id] = window + [now]
        return await call_next(request)

# ── 3. Global exception handler ───────────────────────
from fastapi import HTTPException
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error("unhandled_exception", path=request.url.path, error=str(exc))
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error",
                 "request_id": request.headers.get("X-Request-ID")}
    )

# ── Register all middleware ────────────────────────────
app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(RateLimitMiddleware, calls_per_minute=60)
app.add_middleware(CORSMiddleware,
    allow_origins=["https://yourdomain.com"],   # never "*" in production
    allow_methods=["GET", "POST"],
    allow_headers=["*"])
```


  </div>
</div>
</div><!-- end t3 -->
<!-- ══════════ TAB 4 — ASYNC PATTERNS ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Async Patterns for AI APIs</h3><span class="tag tag-navy">Performance</span></div>
  <div class="cp-body">
    

```python
from fastapi import BackgroundTasks
import asyncio

# ── Background tasks — fire and forget ───────────────
# Use for: logging, analytics, cache warming, notifications
# Do NOT use for: work the user needs to see in the response

async def log_usage_async(user_id: str, tokens: int, cost: float):
    """Run after response is sent — user doesn't wait for this."""
    await asyncio.sleep(0)   # yield to event loop
    await db.insert_usage(user_id, tokens, cost)

@router.post("/chat")
async def chat_with_logging(
    request: ChatRequest,
    background_tasks: BackgroundTasks,
    client: LLMDep
):
    response = await client.messages.create(...)
    reply    = response.content[0].text

    # Schedule logging AFTER response is sent
    background_tasks.add_task(
        log_usage_async,
        user_id=request.session_id,
        tokens=response.usage.output_tokens,
        cost=response.usage.output_tokens * 15e-6
    )
    return {"reply": reply}   # returned immediately; logging runs after

# ── Never block the event loop ────────────────────────
import asyncio

# BAD: blocks the entire event loop — other requests wait
@router.get("/bad")
async def bad_endpoint():
    import time
    time.sleep(5)   # blocks! no other requests can run during this
    return {"ok": True}

# GOOD: yields to event loop
@router.get("/good")
async def good_endpoint():
    await asyncio.sleep(5)   # other requests run while waiting
    return {"ok": True}

# For CPU-bound work: run in thread pool
import functools

@router.post("/embed")
async def embed_text(text: str):
    loop  = asyncio.get_event_loop()
    # Run sync embedding model in thread pool — doesn't block event loop
    embed = await loop.run_in_executor(
        None,
        functools.partial(sync_embedding_model.encode, text)
    )
    return {"embedding": embed.tolist()}
```


<div class="warn"><p>⚠️ <strong>Every <code>time.sleep()</code>, synchronous DB call, or CPU-heavy operation inside an <code>async def</code> blocks the entire FastAPI event loop.</strong> While your endpoint sleeps, every other concurrent request waits. Use <code>asyncio.sleep()</code> for delays, <code>run_in_executor()</code> for CPU work, and async DB drivers (asyncpg, motor) for database calls.</p></div>
  </div>
</div>
</div><!-- end t4 -->
<!-- ══════════ TAB 5 — AUTH & API KEYS ══════════ -->
<div id="t5" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🔐</span><h3>Authentication — API Keys and JWT</h3><span class="tag tag-navy">Security</span></div>
  <div class="cp-body">
    

```python
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
import secrets, hashlib

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)

# ── Simple API key validation ─────────────────────────
VALID_KEYS = {  # in prod, store hashed keys in DB
    hashlib.sha256("sk-dev-key-1".encode()).hexdigest(): {"user_id": "user_1", "tier": "free"},
    hashlib.sha256("sk-prod-key-1".encode()).hexdigest(): {"user_id": "user_2", "tier": "pro"},
}

async def require_api_key(api_key: str = Security(API_KEY_HEADER)):
    if not api_key:
        raise HTTPException(status_code=401, detail="API key required")
    key_hash = hashlib.sha256(api_key.encode()).hexdigest()
    user = VALID_KEYS.get(key_hash)
    if not user:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return user

# Type alias for clean signatures
AuthUser = Annotated[dict, Security(require_api_key)]

@router.post("/ask")
async def ask(request: RAGRequest, user: AuthUser, client: LLMDep):
    # user = {"user_id": "user_2", "tier": "pro"}
    if user["tier"] == "free" and len(request.question) > 500:
        raise HTTPException(status_code=402, detail="Upgrade to Pro for longer questions")
    ...

# ── JWT with python-jose ──────────────────────────────
pip install python-jose[cryptography]

from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-256-bit-secret"   # from environment in prod
ALGORITHM  = "HS256"

def create_access_token(user_id: str, expires_minutes: int = 60) -> str:
    payload = {"sub": user_id,
               "exp": datetime.utcnow() + timedelta(minutes=expires_minutes)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user_jwt(token: str = Security(oauth2_scheme)) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
```


  </div>
</div>
</div><!-- end t5 -->
<!-- ══════════ TAB 6 — DEPLOYMENT ══════════ -->
<div id="t6" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🚀</span><h3>Deployment — uvicorn + gunicorn + Health Checks</h3><span class="tag tag-navy">Ship It</span></div>
  <div class="cp-body">
    

```python
# ── Development server ────────────────────────────────
uvicorn app.main:app --reload --port 8000

# ── Production: gunicorn manages uvicorn workers ──────
# workers = (2 × CPU cores) + 1 is the standard formula
gunicorn app.main:app   --worker-class uvicorn.workers.UvicornWorker   --workers 4   --bind 0.0.0.0:8000   --timeout 120   --graceful-timeout 30   --access-logfile -   --error-logfile -

# ── Health check endpoints ────────────────────────────
# /health — fast liveness check (load balancer uses this)
# /ready  — readiness check (DB connected, model loaded)

@router.get("/health")
async def health():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}

@router.get("/ready")
async def readiness(client: LLMDep, request: Request):
    checks = {}
    # Check LLM API reachable
    try:
        await client.messages.count_tokens(
            model="claude-3-haiku-20240307",
            messages=[{"role": "user", "content": "ping"}]
        )
        checks["llm"] = "ok"
    except Exception as e:
        checks["llm"] = f"error: {e}"

    # Check vector DB
    try:
        vdb = request.app.state.vector_db
        vdb.heartbeat()
        checks["vector_db"] = "ok"
    except Exception as e:
        checks["vector_db"] = f"error: {e}"

    all_ok = all(v == "ok" for v in checks.values())
    return JSONResponse(
        status_code=200 if all_ok else 503,
        content={"status": "ready" if all_ok else "degraded", "checks": checks}
    )
```


  </div>
</div>
</div><!-- end t6 -->
<!-- ══════════ TAB 7 — RESOURCES ══════════ -->
<div id="t7" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
<tr><td class="res-type">Docs</td><td><a href="https://fastapi.tiangolo.com/tutorial/bigger-applications/" target="_blank" rel="noopener">FastAPI: Bigger Applications — fastapi.tiangolo.com</a></td><td>Official guide on routers, dependencies, and project structure for production apps.</td></tr>
<tr><td class="res-type">Docs</td><td><a href="https://fastapi.tiangolo.com/tutorial/dependencies/" target="_blank" rel="noopener">FastAPI: Dependencies — fastapi.tiangolo.com</a></td><td>Complete dependency injection documentation including yield dependencies and lifespan.</td></tr>
<tr><td class="res-type">Docs</td><td><a href="https://www.uvicorn.org/deployment/" target="_blank" rel="noopener">Uvicorn Deployment Guide — uvicorn.org/deployment</a></td><td>Production deployment with gunicorn workers, systemd, and supervisor.</td></tr>
<tr><td class="res-type">Library</td><td><a href="https://docs.pydantic.dev/latest/concepts/pydantic_settings/" target="_blank" rel="noopener">Pydantic Settings — docs.pydantic.dev</a></td><td>Environment variable management with type safety. Essential for production config.</td></tr>
  </tbody>
</table>
</div>
<!-- ══════════ TAB 8 — PROJECTS ══════════ -->
<div id="t8" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr">
<span>🛠</span>
<span class="proj-title">Production-Ready AI API — Full FastAPI App</span>
<span class="proj-dur">[Intermediate] 3–4 days</span>
  </div>
  <div class="proj-body">
<p>Wrap your M18 RAG system and M21 agent in a production-grade FastAPI application.</p>
<h4>Requirements</h4>
<ul>
<li><strong>Structure</strong> — routers, models, services, config using pydantic-settings</li>
<li><strong>Lifespan</strong> — LLM client and vector DB initialised once at startup, cleaned up on shutdown</li>
<li><strong>Dependency injection</strong> — no global state; all resources injected via Depends()</li>
<li><strong>Middleware</strong> — request logging (request_id, path, latency), rate limiting (60 req/min)</li>
<li><strong>CORS</strong> — configured for your frontend domain only</li>
<li><strong>Auth</strong> — API key validation via X-API-Key header</li>
<li><strong>Endpoints</strong> — POST /rag/ask, POST /chat/message (streaming), GET /admin/health, GET /admin/ready</li>
<li><strong>Deployment</strong> — gunicorn config, .env file, Procfile for cloud deployment</li>
</ul>
<p><strong>Skills:</strong> pydantic-settings, lifespan, dependency injection, BaseHTTPMiddleware, APIKeyHeader, gunicorn</p>
  </div>
</div>
</div>
<!-- ══════════ TAB 9 — LABS ══════════ -->
<div id="t9" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Lifespan and Dependency Injection</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Verify that shared resources are initialised once and injected correctly.</p>
<div class="lab-step"><div class="sn">1</div><div>Build the lifespan function that creates an anthropic.AsyncAnthropic client. Add a print statement with an ID (id(client)) to confirm it is the same object across requests.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Create a dependency get_llm_client() and inject it into 3 endpoints. Add the same id() print. Verify all 3 print the same ID — proving the client is shared.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Load all settings from a .env file using pydantic-settings. Verify a missing required variable raises a clear ValidationError at startup (not at request time).</div></div>
<div class="lab-step"><div class="sn">4</div><div>Test graceful shutdown: send a request, then Ctrl+C while it is in progress. Does the lifespan cleanup run? Does the in-progress request complete or get cut off?</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Middleware Stack</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Build and verify the middleware stack works correctly in combination.</p>
<div class="lab-step"><div class="sn">1</div><div>Add RequestLoggingMiddleware. Verify every request produces one JSON log line with method, path, status, latency_ms, and request_id. Verify the X-Request-ID header appears in the response.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Add RateLimitMiddleware (5 req/minute for testing). Send 6 requests in rapid succession. Verify the 6th returns 429 with a Retry-After header.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Trigger the global exception handler: add a route that raises an unhandled ValueError. Verify the response is 500 JSON (not an HTML traceback) and the error is logged.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Test CORS: use a browser fetch() from a different origin. Verify that allowed origins work and blocked origins get a CORS error.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Async Safety</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Verify that blocking code kills concurrency and fix it.</p>
<div class="lab-step"><div class="sn">1</div><div>Create two endpoints: /slow-sync (time.sleep(3) inside async def) and /slow-async (await asyncio.sleep(3)). Send 3 concurrent requests to each using httpx.AsyncClient with asyncio.gather.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Measure total time for 3 concurrent requests to /slow-sync vs /slow-async. /slow-sync should take ~9s (sequential). /slow-async should take ~3s (parallel).</div></div>
<div class="lab-step"><div class="sn">3</div><div>Fix /slow-sync using run_in_executor(). Re-measure. Verify it now takes ~3s for 3 concurrent requests.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Add a background task to an endpoint. Verify: the response arrives before the background task completes (add asyncio.sleep(2) in the task and confirm response arrives in &lt;1s).</div></div>
  </div>
</div>
</div><!-- end t9 -->
<!-- ══════════ TAB 10 — CHECKLIST ══════════ -->
<div id="t10" class="tab-pane">
<p class="sep">P7-M23 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can describe the production FastAPI project layout: main.py, config.py, dependencies.py, middleware.py, routers/, models/, services/</li>
  <li>Can implement pydantic-settings with env_file=".env" and required field validation at startup</li>
  <li>Can implement a lifespan context manager that creates shared clients at startup and cleans up on shutdown</li>
  <li>Know never to create LLM clients inside endpoint functions — always initialise once at startup</li>
  <li>Can implement dependency providers (get_llm_client, get_settings) and inject via Depends()</li>
  <li>Can use Annotated type aliases for clean endpoint signatures</li>
  <li>Can implement RequestLoggingMiddleware with request_id, latency_ms, and structlog</li>
  <li>Can implement RateLimitMiddleware with per-client sliding window and 429 response</li>
  <li>Can configure CORSMiddleware with specific origins (never allow_origins=["*"] in production)</li>
  <li>Can register a global exception_handler that returns JSON 500 (not HTML tracebacks)</li>
  <li>Know that time.sleep() in async def blocks the event loop — always use asyncio.sleep()</li>
  <li>Can offload CPU-bound work to run_in_executor() to avoid blocking the event loop</li>
  <li>Can use BackgroundTasks for fire-and-forget work that runs after the response is sent</li>
  <li>Can implement API key validation with hashed key storage and HTTPException 401/403</li>
  <li>Can run production server: gunicorn with UvicornWorker, correct worker count, graceful timeout</li>
  <li>Can implement /health (fast liveness) and /ready (full dependency check, returns 503 if degraded)</li>
  <li>Completed Lab 1: lifespan + dependency injection verified</li>
  <li>Completed Lab 2: middleware stack built and tested</li>
  <li>Completed Lab 3: async safety verified with timing measurements</li>
  <li>Milestone project pushed to GitHub: production AI API with all patterns</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P7-M24 — Docker &amp; Background Jobs</strong>. Your API is production-structured. M24 covers containerisation and offloading heavy work to background workers.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/ai-ml/part6-agents/p6-m22-evaluation/">← P6-M22: Evaluation</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part7-production/p7-m24-docker-jobs/">Next: P7-M24 — Docker &amp; Background Jobs →</a>
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
    const key = 'p7m23-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
