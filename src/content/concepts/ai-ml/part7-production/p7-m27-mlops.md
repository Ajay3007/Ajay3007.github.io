---
title: "P7-M27 - MLOps Foundations"
description: "Part 7 — Production Deployment · Module 27 of 27 MLOps Foundations CI/CD for AI, data drift detection, model versioning, and the operational patterns for long-running AI…"
domain: ai-ml
track: ai-ml-engineering
module: part7-production
order: 727
ownHeader: true
url: /learning/ai-ml/part7-production/p7-m27-mlops/
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
/* part7 complete banner */
.part-complete{background:linear-gradient(135deg,#0c1a40,#1e3a5f);border-radius:12px;padding:1.5rem 1.8rem;color:#fff;margin:2rem 0;text-align:center}
.part-complete h3{font-size:1.3rem;font-weight:800;margin-bottom:.5rem;border:none;color:#fff}
.part-complete p{font-size:.9rem;color:#93c5fd;margin:0 0 1rem}
.part-skills{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:.6rem;margin-top:1rem}
.ps-item{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:8px;padding:.6rem .9rem;font-size:.82rem;color:#dbeafe}
.ps-item::before{content:"✓  ";color:#60a5fa;font-weight:700}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">Part 7 — Production &amp; Deployment &nbsp;·&nbsp; Module 27 of 27</div>
  <div class="mod-title">MLOps Foundations</div>
  <div class="mod-subtitle">CI/CD for AI, data drift detection, model versioning, and the operational patterns for long-running AI products</div>
  <div class="mod-pills">
<span class="mod-pill">⏱ 1 Week</span>
<span class="mod-pill">🟡 Intermediate</span>
<span class="mod-pill">🔧 GitHub Actions · DVC · MLflow · Evidently</span>
<span class="mod-pill">📋 Prerequisite: P7-M26</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🔄 CI/CD for AI</button>
  <button class="tab-btn" onclick="vt(event,'t2')">📦 Data Versioning</button>
  <button class="tab-btn" onclick="vt(event,'t3')">📈 Experiment Tracking</button>
  <button class="tab-btn" onclick="vt(event,'t4')">📉 Data Drift</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🚀 Deployment Patterns</button>
  <button class="tab-btn" onclick="vt(event,'t6')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t7')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">✅ Checklist</button>
</div>
<!-- TAB 0 -->
<div id="t0" class="tab-pane active">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-navy">Part 7 Complete</span></div>
  <div class="cp-body">
<p>MLOps for AI engineers — not traditional ML practitioners. Your "models" are LLM APIs, your "training" is prompt engineering and RAG index updates, your "drift" is the distribution of user queries shifting away from your indexed documents. This module covers the operational disciplines that make AI products reliable over months and years.</p>
<ul>
<li><strong>CI/CD for AI</strong> — GitHub Actions pipeline: lint, test, eval, deploy gates</li>
<li><strong>Data versioning with DVC</strong> — track document corpus versions alongside code</li>
<li><strong>Experiment tracking with MLflow</strong> — logging prompt variants, eval scores, cost metrics</li>
<li><strong>Data/query drift detection</strong> — detecting when user queries shift out of distribution</li>
<li><strong>Deployment patterns</strong> — blue-green, canary, feature flags for AI apps</li>
</ul>
  </div>
</div>
</div>
<!-- TAB 1 — CI/CD FOR AI -->
<div id="t1" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>GitHub Actions CI/CD Pipeline for AI Apps</h3><span class="tag tag-navy">Automate</span></div>
  <div class="cp-body">
    

```python
# .github/workflows/ai-ci.yml
name: AI App CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

jobs:

  # ── 1. Fast checks (no LLM calls) ─────────────────────
  lint-and-type:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: {python-version: "3.12"}
      - run: pip install ruff mypy
      - run: ruff check app/
      - run: mypy app/ --ignore-missing-imports

  # ── 2. Unit + integration tests (mocked LLM) ─────────
  test:
    needs: lint-and-type
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt pytest pytest-asyncio
      - run: pytest tests/unit/ tests/integration/ -v --tb=short

  # ── 3. Prompt regression tests (real LLM calls) ───────
  prompt-eval:
    needs: test
    runs-on: ubuntu-latest
    # Only run on PRs that touch prompts/ or src/
    if: |
      github.event_name == 'pull_request' &&
      contains(github.event.pull_request.changed_files, 'prompts/')
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt pytest
      - name: Run prompt eval suite
        run: pytest tests/test_prompts.py -v --tb=long
      - name: Post eval results as PR comment
        uses: actions/github-script@v7
        with:
          script: |
            const body = `## Prompt Eval Results
✅ All grounding tests passed
✅ Faithfulness: 0.91 >= 0.85`
            github.rest.issues.createComment({...context.repo, issue_number: context.issue.number, body})

  # ── 4. Build and push Docker image ────────────────────
  build:
    needs: [test, prompt-eval]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v5
        with:
          push: true
          tags: ghcr.io/${{ github.repository }}:${{ github.sha }}

  # ── 5. Deploy (blue-green, see Tab 5) ─────────────────
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Deploy new image
        run: |
          ssh deploy@$SERVER "docker pull ghcr.io/$IMAGE:$SHA &&             docker service update --image ghcr.io/$IMAGE:$SHA ai_api"
```


  </div>
</div>
</div><!-- end t1 -->
<!-- TAB 2 — DATA VERSIONING -->
<div id="t2" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">📦</span><h3>DVC — Version Your Document Corpus</h3><span class="tag tag-navy">Reproducibility</span></div>
  <div class="cp-body">
<p>Your RAG index is data. When you add, remove, or update documents, the retrieval behaviour changes. DVC (Data Version Control) tracks your document corpus alongside your code so you can always reproduce any system state.</p>
    

```python
pip install dvc dvc-s3   # or dvc-gcs, dvc-azure

# Initialise DVC in your repo
git init && dvc init

# Add remote storage (S3, GCS, Azure, or local)
dvc remote add -d storage s3://my-bucket/dvc-store
# Or local for dev:
dvc remote add -d storage /tmp/dvc-store

# Track your document corpus
dvc add docs/corpus/          # creates docs/corpus.dvc (pointer file)
git add docs/corpus.dvc .gitignore
git commit -m "Add corpus v1: initial DPDK documentation"
dvc push                      # upload to remote storage

# Update the corpus
# ... add new PDF files to docs/corpus/ ...
dvc add docs/corpus/
git add docs/corpus.dvc
git commit -m "Update corpus v2: add VPP documentation"
dvc push

# On another machine or in CI: reproduce exact corpus version
git checkout "v1-tag"
dvc pull       # downloads the exact corpus for that commit

# DVC pipeline: define reproducible ingestion pipeline
# dvc.yaml
stages:
  ingest:
    cmd: python scripts/ingest.py --input docs/corpus/ --output chroma_db/
    deps:
      - scripts/ingest.py
      - docs/corpus/
    outs:
      - chroma_db/

# Run: dvc repro — reruns only stages where inputs changed
# dvc dag — visualise the pipeline
```


<div class="ins"><p>💡 <strong>The DVC pointer file (<code>corpus.dvc</code>) is tiny and goes in Git. The actual data goes in remote storage.</strong> This means your Git repo stays fast while your data is versioned and reproducible. Every commit of your code has a matching commit of your data — you can reproduce any system state from history.</p></div>
  </div>
</div>
</div><!-- end t2 -->
<!-- TAB 3 — EXPERIMENT TRACKING -->
<div id="t3" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">📈</span><h3>MLflow — Track Prompt Experiments</h3><span class="tag tag-navy">Compare Everything</span></div>
  <div class="cp-body">
    

```python
pip install mlflow

import mlflow

# MLflow tracks: parameters, metrics, artifacts, tags
# For AI/LLM work: prompt versions, eval scores, cost metrics

mlflow.set_tracking_uri("http://localhost:5000")   # or file:./mlruns
mlflow.set_experiment("rag-prompt-iterations")

def evaluate_prompt_variant(prompt_name: str, prompt_version: int,
                             test_cases: list) -> dict:
    with mlflow.start_run(run_name=f"{prompt_name}-v{prompt_version}"):
        # Log parameters
        mlflow.log_param("prompt_name", prompt_name)
        mlflow.log_param("prompt_version", prompt_version)
        mlflow.log_param("model", "claude-3-5-sonnet-20241022")
        mlflow.log_param("n_test_cases", len(test_cases))

        # Run evaluation
        prompt_content = get_prompt_version(prompt_name, prompt_version)
        faithfulness_scores, relevancy_scores, costs = [], [], []

        for case in test_cases:
            result = rag_pipeline(case["question"], prompt_content)
            faith  = judge_faithfulness(result["context"], result["answer"])
            faithfulness_scores.append(faith.score)
            costs.append(result["cost_usd"])

        # Log metrics
        mlflow.log_metric("faithfulness_mean",  sum(faithfulness_scores)/len(faithfulness_scores))
        mlflow.log_metric("faithfulness_min",   min(faithfulness_scores))
        mlflow.log_metric("cost_per_query_usd", sum(costs)/len(costs))
        mlflow.log_metric("total_cost_usd",     sum(costs))

        # Log the prompt as an artifact
        with open("prompt.txt", "w") as f:
            f.write(prompt_content)
        mlflow.log_artifact("prompt.txt")

        return {"faithfulness": sum(faithfulness_scores)/len(faithfulness_scores),
                "cost": sum(costs)/len(costs)}

# Compare runs in MLflow UI
# mlflow ui --port 5000
# → parallel coordinates plot shows which params produce best faithfulness
# → compare v1, v2, v3 side-by-side on all metrics
```


  </div>
</div>
</div><!-- end t3 -->
<!-- TAB 4 — DATA DRIFT -->
<div id="t4" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">📉</span><h3>Query Drift Detection — When Users Stop Asking What You Indexed</h3><span class="tag tag-navy">Production Health</span></div>
  <div class="cp-body">
<p>For RAG systems, "data drift" means user queries are shifting toward topics not covered by your indexed documents. Retrieval scores drop, but nothing crashes — users just get worse answers. You need to detect this proactively.</p>
    

```python
import numpy as np
from datetime import datetime, timedelta

# ── Track retrieval scores over time ──────────────────
# Log the top-1 similarity score for every query
# Degrading average = queries moving out of distribution

def log_retrieval_score(query: str, top_score: float, session_id: str):
    with sqlite3.connect("drift.db") as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS retrieval_log
            (ts TEXT, query TEXT, score REAL, session_id TEXT)""")
        conn.execute("INSERT INTO retrieval_log VALUES (?,?,?,?)",
                     (datetime.utcnow().isoformat(), query, top_score, session_id))

def check_retrieval_drift(window_days: int = 7, baseline_days: int = 30) -> dict:
    """Compare recent avg score vs baseline avg score."""
    now     = datetime.utcnow().isoformat()
    recent  = (datetime.utcnow() - timedelta(days=window_days)).isoformat()
    old     = (datetime.utcnow() - timedelta(days=baseline_days)).isoformat()

    with sqlite3.connect("drift.db") as conn:
        recent_avg = conn.execute(
            "SELECT AVG(score) FROM retrieval_log WHERE ts > ?", (recent,)).fetchone()[0]
        baseline_avg = conn.execute(
            "SELECT AVG(score) FROM retrieval_log WHERE ts BETWEEN ? AND ?",
            (old, recent)).fetchone()[0]

    if not baseline_avg:
        return {"status": "insufficient_data"}

    delta = recent_avg - baseline_avg
    return {
        "recent_avg_score":   round(recent_avg, 4),
        "baseline_avg_score": round(baseline_avg, 4),
        "delta":              round(delta, 4),
        "drifting":          delta 0.05,   # >5% drop = significant drift
        "action":            "Re-index new documents" if delta 0.05 else "Monitor"
    }

# ── Topic clustering — find what users are asking about ──
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize

def identify_drift_topics(n_clusters: int = 5) -> list[dict]:
    """Cluster low-scoring queries to find coverage gaps."""
    with sqlite3.connect("drift.db") as conn:
        rows = conn.execute(
            "SELECT query FROM retrieval_log WHERE score 
        ).fetchall()

    if len(rows) 10:
        return []

    queries = [r[0] for r in rows]
    embeddings = embed_batch(queries)   # your embedding function
    X = normalize(np.array(embeddings))

    km = KMeans(n_clusters=n_clusters, random_state=42)
    km.fit(X)

    # Find representative query for each cluster
    clusters = []
    for cluster_id in range(n_clusters):
        mask = km.labels_ == cluster_id
        cluster_queries = [queries[i] for i, m in enumerate(mask) if m]
        clusters.append({
            "cluster_id":  cluster_id,
            "count":       len(cluster_queries),
            "sample_queries": cluster_queries[:3]
        })
    return sorted(clusters, key=lambda x: -x["count"])
```


<div class="ins"><p>💡 <strong>Query drift is how you know what to index next.</strong> When <code>identify_drift_topics()</code> shows 200 low-scoring queries clustering around "VPP DPDK integration", that's your signal to add VPP documentation to your corpus. Drift detection turns reactive support into proactive documentation improvement.</p></div>
  </div>
</div>
</div><!-- end t4 -->
<!-- TAB 5 — DEPLOYMENT PATTERNS -->
<div id="t5" class="tab-pane">
<div class="cp p-navy">
  <div class="cp-hdr"><span class="ico">🚀</span><h3>Safe Deployment Patterns</h3><span class="tag tag-navy">Zero Downtime</span></div>
  <div class="cp-body">
    

```python
# ── Blue-Green Deployment ─────────────────────────────
# Run two identical environments. Switch traffic between them.
# Zero downtime. Instant rollback (switch traffic back).

# docker-compose.prod.yml style blue-green
# Blue = current live version, Green = new version
#
# 1. Deploy green alongside blue
# 2. Run health checks on green
# 3. Switch load balancer: 100% → green
# 4. Keep blue running for 5 min (easy rollback)
# 5. Tear down blue

# ── Canary Deployment ─────────────────────────────────
# Route small % of traffic to new version first
# Monitor metrics. If good → increase %. If bad → 0%.

import random

class CanaryRouter:
    def __init__(self, canary_pct: float = 0.05):  # 5% to new version
        self.canary_pct = canary_pct

    def route(self, request) -> str:
        # Sticky routing: same user always gets same version
        user_hash = hash(request.headers.get("X-User-ID", "")) % 100
        if user_hash 100:
            return "green"   # canary version
        return "blue"       # stable version

# ── Feature flags — safest for AI changes ─────────────
# Toggle behaviour without deploying new code
# Perfect for A/B testing prompt variants in production

FEATURE_FLAGS = {
    "use_reranker":        True,
    "use_hyde":            False,
    "contextual_retrieval": False,
    "new_prompt_v3":       False,   # flip to True after testing
}

def is_enabled(flag: str, user_id: str = "", rollout_pct: float = 1.0) -> bool:
    """Check if feature flag is enabled. Supports percentage rollout."""
    if not FEATURE_FLAGS.get(flag):
        return False
    if rollout_pct 1.0 and user_id:
        return (hash(user_id + flag) % 100) 100)
    return True

# In endpoint:
# if is_enabled("use_reranker", user_id, rollout_pct=0.2):
#     results = retrieve_and_rerank(query)
# else:
#     results = basic_retrieve(query)

# ── Index hot-swap ────────────────────────────────────
# Update the vector DB index without downtime

class IndexSwapper:
    def __init__(self):
        self.active = "index_a"   # current live index
        self.staging = "index_b"  # being rebuilt

    def rebuild_in_background(self, new_documents: list):
        # Build into staging index while live index serves traffic
        pipeline = DocumentIngestionPipeline(
            config=IngestionConfig(collection_name=self.staging)
        )
        pipeline.ingest_directory(new_documents)
        self.swap()

    def swap(self):
        self.active, self.staging = self.staging, self.active
        print(f"Swapped to {self.active}")
```


  </div>
</div>
</div><!-- end t5 -->
<!-- TAB 6 — RESOURCES -->
<div id="t6" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
<tr><td class="res-type">Docs</td><td><a href="https://dvc.org/doc/start" target="_blank" rel="noopener">DVC: Getting Started — dvc.org/doc/start</a></td><td>Version control for data and ML pipelines. Covers remote storage, pipelines, and experiments.</td></tr>
<tr><td class="res-type">Docs</td><td><a href="https://mlflow.org/docs/latest/quickstart.html" target="_blank" rel="noopener">MLflow Quickstart — mlflow.org/docs/latest</a></td><td>Experiment tracking, model registry, and artifacts. Run mlflow ui to see the dashboard.</td></tr>
<tr><td class="res-type">Docs</td><td><a href="https://docs.evidentlyai.com/user-guide/getting-started" target="_blank" rel="noopener">Evidently AI: Getting Started — docs.evidentlyai.com</a></td><td>Data drift and ML monitoring. Good for query distribution monitoring.</td></tr>
<tr><td class="res-type">Course</td><td><a href="https://github.com/actions/starter-workflows" target="_blank" rel="noopener">GitHub Actions Starter Workflows — github.com/actions/starter-workflows</a></td><td>Production-ready GitHub Actions workflow templates for Python, Docker, and deployment.</td></tr>
  </tbody>
</table>
</div>
<!-- TAB 7 — PROJECTS -->
<div id="t7" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span>
<span class="proj-title">Full MLOps Pipeline — CI/CD + Drift Detection + Feature Flags</span>
<span class="proj-dur">[Intermediate–Advanced] 4–5 days</span>
  </div>
  <div class="proj-body">
<p>Add the full MLOps layer to your production AI system.</p>
<h4>Requirements</h4>
<ul>
<li><strong>GitHub Actions</strong> — 5-stage pipeline: lint → test → prompt-eval → build → deploy; prompt-eval runs only when prompts/ changes</li>
<li><strong>DVC</strong> — version your document corpus; create v1 and v2 with different documents; verify git checkout + dvc pull restores exact corpus</li>
<li><strong>MLflow</strong> — track 3 prompt variants with faithfulness and cost metrics; compare in UI; identify winning variant</li>
<li><strong>Drift detection</strong> — log retrieval scores for 7 days of simulated queries; compute drift; identify top 3 under-covered topics via clustering</li>
<li><strong>Feature flags</strong> — implement is_enabled() for new_prompt_v3 and use_reranker; set up A/B test at 20% rollout</li>
</ul>
<p><strong>Skills:</strong> GitHub Actions, DVC, MLflow, KMeans clustering, canary deployment, feature flags</p>
  </div>
</div>
</div>
<!-- TAB 8 — LABS -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>GitHub Actions — End-to-End CI Pipeline</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Build and trigger a real CI pipeline that gates deployment on eval quality.</p>
<div class="lab-step"><div class="sn">1</div><div>Create .github/workflows/ci.yml with 3 jobs: lint (ruff), test (pytest unit tests with mocked LLM), prompt-eval (pytest tests/test_prompts.py with real API calls). Make prompt-eval only trigger when prompts/ directory changes.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Push a deliberate bad prompt (remove grounding instructions). Observe prompt-eval job fail. Check the Actions UI — you should see which test failed and why.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Fix the prompt. Push again. Verify all 3 jobs pass. Merge is now allowed (in a real setup you'd add branch protection rules).</div></div>
<div class="lab-step"><div class="sn">4</div><div>Add a 4th job: cost-check. It runs cost_report() and fails the pipeline if the average cost per query in the eval run exceeds $0.01. Verify this gate works by temporarily using an expensive model.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>MLflow — Compare Prompt Variants</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Use MLflow to make a data-driven decision between 3 prompt variants.</p>
<div class="lab-step"><div class="sn">1</div><div>Create 3 prompt variants: V1 (current), V2 (more specific grounding instructions), V3 (adds output format requirements). Run evaluate_prompt_variant() for each on your 20-case test set.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Open MLflow UI (mlflow ui --port 5000). In the experiments view, compare all 3 runs on faithfulness_mean and cost_per_query_usd.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Use MLflow's "Compare Runs" feature to view a parallel coordinates plot. Which variant achieves the best faithfulness-to-cost ratio?</div></div>
<div class="lab-step"><div class="sn">4</div><div>Register the winning prompt version in the MLflow Model Registry (even though it's a prompt, not a model). Tag it as "production". Document the decision in the run description.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Drift Detection — Simulate and Detect</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Simulate query drift and verify your detection catches it.</p>
<div class="lab-step"><div class="sn">1</div><div>Populate your drift.db with 100 simulated "baseline" queries from your indexed domain (high retrieval scores ~0.75–0.90). Set their timestamps 15 days ago.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Add 50 "recent" queries about an uncovered topic (e.g. VPP if you only indexed DPDK). These should get low retrieval scores (~0.20–0.40). Set their timestamps to the last 7 days.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Call check_retrieval_drift(). Verify it correctly identifies drift (delta < -0.05) and suggests "Re-index new documents".</div></div>
<div class="lab-step"><div class="sn">4</div><div>Call identify_drift_topics(n_clusters=3). Verify the largest cluster corresponds to VPP queries. This is your indexing backlog: a prioritised list of topics to add to your corpus.</div></div>
  </div>
</div>
</div><!-- end t8 -->
<!-- TAB 9 — CHECKLIST -->
<div id="t9" class="tab-pane">
<p class="sep">P7-M27 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can write a multi-job GitHub Actions workflow: lint → test → prompt-eval → build → deploy</li>
  <li>Can make a job conditional (only run when specific directories change)</li>
  <li>Can add a quality gate job that fails CI if eval metrics are below threshold</li>
  <li>Can initialise DVC in a repo, track a data directory, and push to remote storage</li>
  <li>Know the DVC workflow: dvc add → git commit → dvc push (to sync data and code versions)</li>
  <li>Can reproduce any past system state: git checkout + dvc pull</li>
  <li>Can define a DVC pipeline (dvc.yaml) for reproducible ingestion</li>
  <li>Can log prompt experiments to MLflow with parameters, metrics, and artifacts</li>
  <li>Can compare multiple MLflow runs side-by-side to choose a prompt variant</li>
  <li>Can detect query drift by comparing recent vs baseline average retrieval scores</li>
  <li>Know that delta < -0.05 (5% drop in retrieval score) is a significant drift signal</li>
  <li>Can cluster low-scoring queries with KMeans to identify under-covered topics</li>
  <li>Can implement canary deployment with sticky user routing (same user always gets same version)</li>
  <li>Can implement feature flags with percentage rollout based on user_id hash</li>
  <li>Can implement index hot-swap: rebuild in staging while live index serves traffic, then swap</li>
  <li>Completed Lab 1: GitHub Actions CI pipeline with quality gate</li>
  <li>Completed Lab 2: MLflow experiment comparison for prompt variant selection</li>
  <li>Completed Lab 3: drift detection simulated and verified end-to-end</li>
  <li>Milestone project: full MLOps pipeline pushed to GitHub</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>Part 7 Complete!</strong> Move to <strong>Part 8 — Specialisation Tracks</strong>. You now have the full production engineering foundation. Part 8 lets you go deep in one of four AI engineering specialisations.</p>
</div>
</div>
<!-- PART 7 COMPLETE BANNER -->
<div class="part-complete">
  <h3>🎉 Part 7 — Production &amp; Deployment Complete!</h3>
  <p>You can now ship, operate, and evolve production-grade AI systems.</p>
  <div class="part-skills">
<div class="ps-item">Structure FastAPI apps for production with DI and middleware</div>
<div class="ps-item">Containerise with multi-stage Docker + Docker Compose</div>
<div class="ps-item">Run background jobs with Celery + Redis, with job status polling</div>
<div class="ps-item">Instrument with Prometheus, Grafana, structlog, and Sentry</div>
<div class="ps-item">Version and test prompts before deployment with regression gates</div>
<div class="ps-item">Monitor costs per user/model/endpoint and optimise with caching</div>
<div class="ps-item">Detect query drift and maintain index coverage over time</div>
<div class="ps-item">Deploy safely with blue-green, canary, and feature flags</div>
  </div>
</div>
<div class="mod-nav">
  <a href="/learning/ai-ml/part7-production/p7-m26-prompt-versioning/">← P7-M26: Prompt Versioning</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/ai-ml-roadmap/#s8">Next: Part 8 — Specialisation →</a>
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
    const key = 'p7m27-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
