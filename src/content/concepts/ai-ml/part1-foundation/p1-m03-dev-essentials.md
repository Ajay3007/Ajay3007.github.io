---
title: "P1-M03 - Developer Essentials: Git, CLI, APIs & Async"
description: "Part 1 — Universal Foundation · Module 03 of 04 Developer Essentials Git, CLI, HTTP APIs and Async Python — the tools every AI engineer uses daily ⏱ 2 Weeks 🟢 Beginner 🔧 Git…"
domain: ai-ml
track: ai-ml-engineering
module: part1-foundation
order: 103
ownHeader: true
url: /learning/ai-ml/part1-foundation/p1-m03-dev-essentials/
---

<style>
.mod-header{background:linear-gradient(135deg,#0f0a1e 0%,#1a0a3a 45%,#4c1d95 80%,#7c3aed 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#c4b5fd;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#ddd6fe;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#ede9fe}
.tab-bar{display:flex;flex-wrap:wrap;background:#0f0a1e;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#c4b5fd;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#a78bfa;border-bottom-color:#a78bfa}
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
.p-blue .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue .cp-hdr{background:#0d2030}
.p-teal .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.p-red .cp-hdr{background:#faeaea}[data-theme=dark] .p-red .cp-hdr{background:#2a0808}
.p-amber .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber .cp-hdr{background:#2a1e00}
.tag-blue{background:#d0e8f8;color:#1a4a7c}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}.tag-red{background:#f4d0d0;color:#6c1a1a}
.tag-amber{background:#fae8a0;color:#5a3800}
.cb{background:#0f0a1e;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #7c3aed}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#ddd6fe;white-space:pre}
.cm{color:#6d6875}.ck{color:#c4b5fd}.cv{color:#f0c080}.cs{color:#a78bfa}
.ins{background:#f5f0ff;border:1.5px solid #7c3aed;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#1a0a3a;border-color:#7c3aed}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#5b21b6}[data-theme=dark] .ins strong{color:#a78bfa}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.wk-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.85rem}
.wk-table th{background:#1a0a3a;color:#ddd6fe;padding:.7rem 1rem;text-align:left;font-weight:700;font-size:.75rem;text-transform:uppercase;letter-spacing:.06em}
.wk-table td{padding:.65rem 1rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top;line-height:1.6}
.wk-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.wk-num{font-family:monospace;font-weight:700;color:#7c3aed;white-space:nowrap}
.res-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.84rem}
.res-table th{background:#4a5568;color:#fff;padding:.6rem .9rem;text-align:left;font-weight:600;font-size:.74rem;text-transform:uppercase;letter-spacing:.06em}
.res-table td{padding:.6rem .9rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top}
.res-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.res-table a{color:#7c3aed;font-weight:500;text-decoration:none}
.res-table a:hover{text-decoration:underline}
.res-type{font-family:monospace;font-size:.74rem;font-weight:700;color:#4a5568}
.lab-box{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;margin:1.2rem 0;overflow:hidden}
.lab-hdr{background:#1a0a3a;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-n{background:#7c3aed;color:#fff;font-size:.72rem;font-family:monospace;font-weight:700;padding:2px 10px;border-radius:12px}
.lab-hdr h4{margin:0;font-size:.95rem;font-weight:700;color:#ddd6fe;border:none}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.8rem;font-size:.88rem;line-height:1.65}
.sn{background:#7c3aed;color:#fff;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem 0;border-bottom:1px solid var(--border-color,#eee);font-size:.88rem;line-height:1.6;cursor:pointer}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";font-size:1rem;flex-shrink:0;margin-top:.05rem;color:#7c3aed}
.cl li.done::before{content:"☑";color:#059669}
.cl li.done{color:var(--light-text,#888);text-decoration:line-through}
.sep{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--light-text,#888);border-bottom:1px solid var(--border-color,#e4e4e4);padding-bottom:.4rem;margin:2rem 0 1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin:2.5rem 0 1rem;padding-top:1.2rem;border-top:1.5px solid var(--border-color,#e4e4e4)}
.mod-nav a{font-size:.85rem;font-weight:600;color:#7c3aed;text-decoration:none;padding:.4rem .9rem;border-radius:6px;border:1.5px solid #7c3aed;transition:all .15s}
.mod-nav a:hover{background:#7c3aed;color:#fff}
.mod-nav .nb{background:#7c3aed;color:#fff}
.mod-nav .nb:hover{background:#5b21b6;border-color:#5b21b6}
.skip-box{background:#f5f0ff;border-left:4px solid #7c3aed;border-radius:0 8px 8px 0;padding:.85rem 1rem;margin:1rem 0;font-size:.87rem;line-height:1.65}
.skip-box strong{color:#5b21b6}
.proj-box{background:#f0fdf4;border:1.5px solid #86efac;border-radius:10px;overflow:hidden;margin:1.2rem 0}
.proj-hdr{background:#15803d;color:#fff;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem;flex-wrap:wrap}
.proj-title{font-weight:700;font-size:.92rem}
.proj-dur{font-size:.78rem;opacity:.85;margin-left:auto;font-family:monospace}
.proj-body{padding:.9rem 1.2rem;font-size:.88rem;line-height:1.7}
.proj-body strong{color:#15803d}
/* HTTP status grid */
.status-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:.6rem;margin:.8rem 0}
.sc{border-radius:8px;padding:.6rem .9rem;font-size:.83rem}
.sc .code{font-family:monospace;font-weight:800;font-size:1rem;display:block;margin-bottom:.2rem}
.sc .meaning{font-size:.78rem;line-height:1.4}
.sc-2xx{background:#dcfce7;border:1px solid #86efac}.sc-2xx .code{color:#15803d}
.sc-3xx{background:#dbeafe;border:1px solid #93c5fd}.sc-3xx .code{color:#1d4ed8}
.sc-4xx{background:#fef9c3;border:1px solid #fde047}.sc-4xx .code{color:#854d0e}
.sc-5xx{background:#fee2e2;border:1px solid #fca5a5}.sc-5xx .code{color:#991b1b}
/* Git flow diagram */
.git-flow{display:flex;align-items:center;gap:.3rem;flex-wrap:wrap;margin:.8rem 0;font-size:.8rem;font-family:monospace}
.gf-box{background:#1a0a3a;color:#ddd6fe;padding:.35rem .8rem;border-radius:6px;border:1px solid #7c3aed;font-weight:600}
.gf-arrow{color:#7c3aed;font-weight:700;font-size:1rem}
</style>
<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 1 — Universal Foundation &nbsp;·&nbsp; Module 03 of 04</div>
  <div class="mod-title">Developer Essentials</div>
  <div class="mod-subtitle">Git, CLI, HTTP APIs and Async Python — the tools every AI engineer uses daily</div>
  <div class="mod-pills">
<span class="mod-pill">⏱ 2 Weeks</span>
<span class="mod-pill">🟢 Beginner</span>
<span class="mod-pill">🔧 Git · Terminal · requests · httpx</span>
<span class="mod-pill">📋 Prerequisite: P1-M01</span>
  </div>
</div>
<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🌿 Git & GitHub</button>
  <button class="tab-btn" onclick="vt(event,'t2')">💻 CLI & Terminal</button>
  <button class="tab-btn" onclick="vt(event,'t3')">🌐 HTTP & APIs</button>
  <button class="tab-btn" onclick="vt(event,'t4')">⚡ Async/Await</button>
  <button class="tab-btn" onclick="vt(event,'t5')">📅 Week Plan</button>
  <button class="tab-btn" onclick="vt(event,'t6')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t7')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">✅ Checklist</button>
</div>
<!-- ══════════ TAB 0 — OVERVIEW ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-purple">Foundation</span></div>
  <div class="cp-body">
<p>This module covers the developer tooling every AI engineer uses every single day — version control, terminal navigation, calling web APIs, and asynchronous Python. These are not optional extras — being slow or uncomfortable with any of them is a real bottleneck when building AI systems.</p>
<ul>
<li><strong>Git &amp; GitHub</strong> — version control, branching, merging, pushing to remote, writing good READMEs</li>
<li><strong>CLI / Terminal</strong> — navigation, file operations, environment variables, running scripts, PATH</li>
<li><strong>HTTP &amp; REST APIs</strong> — GET/POST requests, status codes, headers, API keys, JSON parsing</li>
<li><strong>Python requests library</strong> — calling any web API from Python with error handling</li>
<li><strong>JSON handling</strong> — loading, dumping, nested structures, serialisation edge cases</li>
<li><strong>Async/await</strong> — what coroutines are, why LLM APIs use them, how to write and run async code</li>
</ul>
  </div>
</div>
<div class="skip-box">
  <strong>⚡ SKIP IF:</strong> You already use Git daily and understand HTTP — focus only on the async/await tab (Tab 4) and JSON handling patterns, which are essential for LLM API work. If you know curl and REST APIs from other languages, the Python requests library will take you 30 minutes.
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Why These Skills Matter for AI Engineering</h3><span class="tag tag-green">Context</span></div>
  <div class="cp-body">
<ul>
<li><strong>Git</strong> — every AI project lives in a repo. Your GitHub profile is your resume. Every module project from here goes on GitHub.</li>
<li><strong>CLI</strong> — you will run Python scripts, start servers, install packages, and manage containers entirely from the terminal. Being slow here is a daily tax on your productivity.</li>
<li><strong>HTTP/APIs</strong> — calling the OpenAI or Anthropic API is just an HTTP POST request. Understanding what happens under the hood makes you a better debugger when things go wrong.</li>
<li><strong>Async</strong> — LLM API calls are I/O-bound. The Anthropic and OpenAI Python SDKs are async-first. FastAPI (which you use in M04) runs async handlers. You cannot build production AI apps without understanding this.</li>
</ul>
  </div>
</div>
</div><!-- end t0 -->
<!-- ══════════ TAB 1 — GIT & GITHUB ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🌿</span><h3>Git Mental Model — What Problem It Solves</h3><span class="tag tag-purple">Concept First</span></div>
  <div class="cp-body">
<p>Git is confusing when you try to memorise commands before understanding the model. Understand this first: Git tracks <strong>snapshots</strong> of your project at points in time (commits). Every commit is a full snapshot, not a diff. Branches are just lightweight pointers to commits.</p>
<div class="git-flow">
<div class="gf-box">Working Directory</div><div class="gf-arrow">→ git add →</div>
<div class="gf-box">Staging Area</div><div class="gf-arrow">→ git commit →</div>
<div class="gf-box">Local Repo</div><div class="gf-arrow">→ git push →</div>
<div class="gf-box">Remote (GitHub)</div>
</div>
<p>The staging area is Git's unique feature — it lets you carefully choose exactly which changes to include in the next commit, even if you have made 10 unrelated changes across files.</p>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⌨️</span><h3>Core Git Commands</h3><span class="tag tag-blue">Daily Use</span></div>
  <div class="cp-body">
    

```bash
# ── SETUP (once per machine) ──────────────────────────
git config --global user.name  "Ajay Kumar Gupt"
git config --global user.email "your@email.com"
git config --global core.editor "code --wait"  # VS Code as editor

# ── START A PROJECT ───────────────────────────────────
git init                        # initialise new repo in current dir
git clone <url>                 # clone existing repo from GitHub

# ── DAILY WORKFLOW ────────────────────────────────────
git status                      # what changed? (run this constantly)
git add .                       # stage all changes
git add src/main.py             # stage specific file
git commit -m "feat: add streaming response handler"
git push origin main            # push to GitHub
git pull origin main            # get latest changes

# ── HISTORY ───────────────────────────────────────────
git log --oneline               # compact commit history
git log --oneline --graph       # visualise branch graph
git diff                        # unstaged changes
git diff --staged               # staged changes (what will be committed)

# ── UNDO ──────────────────────────────────────────────
git restore <file>              # discard unstaged changes to a file
git restore --staged <file>     # unstage a file
git revert <commit-hash>        # undo a commit safely (creates new commit)
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🌳</span><h3>Branching and Merging</h3><span class="tag tag-teal">Collaboration</span></div>
  <div class="cp-body">
    

```bash
# Create and switch to a new branch
git checkout -b feature/add-rag-pipeline   # create + switch
git switch -c feature/add-rag-pipeline     # modern equivalent

# List branches
git branch          # local branches
git branch -a       # local + remote branches

# Switch between branches
git switch main
git switch feature/add-rag-pipeline

# Merge feature branch into main
git switch main
git merge feature/add-rag-pipeline

# Delete merged branch
git branch -d feature/add-rag-pipeline        # local
git push origin --delete feature/add-rag-pipeline  # remote

# Push new branch to GitHub for first time
git push -u origin feature/add-rag-pipeline
```


<div class="ins"><p>💡 <strong>Branch naming convention for AI projects:</strong> <code>feat/rag-pipeline</code>, <code>fix/token-overflow</code>, <code>docs/module-p4</code>. Keep branch names short, lowercase, hyphenated. Delete branches after merging — a clean branch list is a healthy repo.</p></div>
  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">📄</span><h3>.gitignore and Repository Hygiene</h3><span class="tag tag-orange">Essential Habit</span></div>
  <div class="cp-body">
<p>A well-maintained .gitignore prevents secrets, large files, and generated artifacts from entering your repo.</p>
    

```bash
# .gitignore for a Python AI project
# Virtual environment
.venv/
venv/
env/

# Secrets — NEVER commit these
.env
.env.local
*.key
*_secret*

# Python artifacts
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/

# Jupyter
.ipynb_checkpoints/
*.ipynb   # optional — commit notebooks if they are documentation

# Data and models — too large for Git
data/raw/
*.csv     # if large; keep small sample CSVs
*.pkl
*.pt      # PyTorch model weights
*.bin     # HuggingFace model files
chroma_db/
*.faiss

# OS files
.DS_Store
Thumbs.db
```


<div class="warn"><p>⚠️ <strong>If you accidentally commit a secret (API key), treat it as compromised immediately.</strong> Rotate the key with the provider. Remove it from history using <code>git filter-branch</code> or BFG Repo Cleaner. Git history is public — even after deletion, the key may have been scraped.</p></div>
  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📝</span><h3>Writing a Good README</h3><span class="tag tag-green">Portfolio</span></div>
  <div class="cp-body">
<p>Your README is the first thing a recruiter, collaborator, or future-you sees. Every project from this roadmap needs one.</p>
    

```bash
# README.md template for AI/ML projects

# Project Title
One compelling sentence describing what it does and why it matters.

## Problem Statement
What real problem does this solve? One paragraph.

## Demo
`![screenshot or gif](assets/demo.gif)`
Live demo: https://your-deployed-app.com

## Tech Stack
Python · FastAPI · LangChain · ChromaDB · Docker

## Quick Start
```bash
git clone https://github.com/you/project.git
cd project
cp .env.example .env          # add your API keys
pip install -r requirements.txt
python main.py
```

## Approach
- Brief description of your methodology (3–5 bullet points)

## Results
Key metrics achieved (e.g. RAG retrieval accuracy: 87%, latency: 340ms)

## Project Structure
```
project/
├── main.py          # entry point
├── src/             # core logic
├── data/            # sample data only
└── tests/           # test suite
```
```


  </div>
</div>
</div><!-- end t1 -->
<!-- ══════════ TAB 2 — CLI & TERMINAL ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">💻</span><h3>Essential Terminal Commands</h3><span class="tag tag-purple">Daily Use</span></div>
  <div class="cp-body">
    

```bash
# ── NAVIGATION ────────────────────────────────────────
pwd                    # print working directory — where am I?
ls                     # list files in current directory
ls -la                 # list all files including hidden, with details
cd /path/to/dir        # change directory (absolute path)
cd ..                  # go up one level
cd ~                   # go to home directory
cd -                   # go back to previous directory

# ── FILES AND DIRECTORIES ─────────────────────────────
mkdir my-project       # create directory
mkdir -p a/b/c         # create nested dirs in one command
touch main.py          # create empty file
cp source.py dest.py   # copy file
mv old.py new.py       # rename or move file
rm file.py             # delete file (no recycle bin!)
rm -rf directory/      # delete directory recursively (irreversible)

# ── READING FILES ─────────────────────────────────────
cat config.py          # print file contents
less large_file.log    # page through large file (q to quit)
head -20 data.csv      # first 20 lines
tail -50 app.log       # last 50 lines (great for log monitoring)
tail -f app.log        # follow — stream new lines in real time
grep "ERROR" app.log   # search for pattern in file
grep -r "api_key" .    # search recursively in all files

# ── RUNNING PYTHON ────────────────────────────────────
python main.py                          # run script
python -m uvicorn main:app --reload     # run FastAPI dev server
python -c "import sys; print(sys.path)" # one-liner
python -m pytest tests/                 # run tests
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🌍</span><h3>Environment Variables and PATH</h3><span class="tag tag-blue">Critical for AI</span></div>
  <div class="cp-body">
<p>Every API key you use — OpenAI, Anthropic, HuggingFace — should live in an environment variable, never in your source code. Understanding how environment variables work is non-negotiable.</p>
    

```python
# Set an environment variable in the shell (temporary)
export OPENAI_API_KEY="sk-proj-..."
export ANTHROPIC_API_KEY="sk-ant-..."

# Read it back
echo $OPENAI_API_KEY

# Permanent — add to ~/.bashrc or ~/.zshrc
echo 'export OPENAI_API_KEY="sk-proj-..."' >> ~/.bashrc
source ~/.bashrc    # reload without restarting terminal

# In Python — the secure pattern for all AI projects
import os
from dotenv import load_dotenv

load_dotenv()   # reads .env file from project root
api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not set. Check your .env file.")

# .env file (in project root, never committed to Git)
# OPENAI_API_KEY=sk-proj-...
# ANTHROPIC_API_KEY=sk-ant-...
# DATABASE_URL=postgresql://...
```


    

```bash
# PATH — tells your shell where to find executables
echo $PATH     # colon-separated list of directories

# If 'python' command not found, your Python install dir is missing from PATH
which python   # where is Python installed?
which pip      # where is pip?

# Add a directory to PATH (in ~/.bashrc)
export PATH=$PATH:/home/user/.local/bin
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Process Management and Pipes</h3><span class="tag tag-teal">Productivity</span></div>
  <div class="cp-body">
    

```bash
# Run process in background
python server.py &        # & sends to background
jobs                      # list background jobs
fg                        # bring last job to foreground
Ctrl+C                    # kill foreground process
Ctrl+Z                    # suspend foreground process

# Find and kill a process using a port (e.g. port 8000)
lsof -ti:8000             # find PID using port 8000
kill -9 $(lsof -ti:8000)  # kill it

# Pipes — chain commands together
cat data.csv | grep "2024" | head -20    # filter and preview
ps aux | grep python                    # find Python processes
cat requirements.txt | wc -l            # count dependencies

# Redirect output to file
python train.py > train.log 2>&1        # stdout + stderr to file
python train.py 2>&1 | tee train.log    # write to file AND print to terminal
```


  </div>
</div>
</div><!-- end t2 -->
<!-- ══════════ TAB 3 — HTTP & APIS ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🌐</span><h3>How HTTP Works — The Mental Model</h3><span class="tag tag-purple">Concept First</span></div>
  <div class="cp-body">
<p>Every LLM API call is an HTTP request. Understanding the request/response cycle makes you a far better debugger when calls fail, return unexpected results, or hit rate limits.</p>
    

```python
# An HTTP request has:
# METHOD   — what action: GET (read), POST (create/send), PUT (update), DELETE
# URL      — where to send it: https://api.anthropic.com/v1/messages
# HEADERS  — metadata: Content-Type, Authorization, x-api-key
# BODY     — data to send (POST/PUT only): usually JSON

# Example: what happens when you call the Anthropic API
# POST https://api.anthropic.com/v1/messages
# Headers:
#   x-api-key: sk-ant-...
#   anthropic-version: 2023-06-01
#   content-type: application/json
# Body:
#   {"model":"claude-3-5-sonnet","max_tokens":1024,"messages":[...]}

# An HTTP response has:
# STATUS CODE — 200 OK, 400 Bad Request, 401 Unauthorised, 429 Rate Limited, 500 Server Error
# HEADERS     — Content-Type, rate limit remaining, request ID
# BODY        — the actual response, usually JSON
```


<div class="status-grid">
<div class="sc sc-2xx"><span class="code">200 OK</span><span class="meaning">Success — request processed</span></div>
<div class="sc sc-2xx"><span class="code">201 Created</span><span class="meaning">Resource created successfully</span></div>
<div class="sc sc-3xx"><span class="code">301 Moved</span><span class="meaning">Permanent redirect to new URL</span></div>
<div class="sc sc-4xx"><span class="code">400 Bad Request</span><span class="meaning">Malformed request — your fault</span></div>
<div class="sc sc-4xx"><span class="code">401 Unauthorised</span><span class="meaning">Missing or invalid API key</span></div>
<div class="sc sc-4xx"><span class="code">403 Forbidden</span><span class="meaning">Authenticated but not allowed</span></div>
<div class="sc sc-4xx"><span class="code">404 Not Found</span><span class="meaning">Resource does not exist</span></div>
<div class="sc sc-4xx"><span class="code">429 Too Many Requests</span><span class="meaning">Rate limit hit — back off and retry</span></div>
<div class="sc sc-5xx"><span class="code">500 Internal Error</span><span class="meaning">Server-side failure — not your fault</span></div>
<div class="sc sc-5xx"><span class="code">503 Unavailable</span><span class="meaning">Service temporarily down</span></div>
</div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🐍</span><h3>Python requests Library</h3><span class="tag tag-blue">Core Skill</span></div>
  <div class="cp-body">
    

```python
import requests
import json

# GET request — read data
response = requests.get("https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": 19.07,
        "longitude": 72.87,
        "daily": "temperature_2m_max",
        "timezone": "Asia/Kolkata"
    }
)

print(response.status_code)   # 200
data = response.json()         # parse JSON body

# POST request — send data (how LLM APIs work)
response = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    },
    json={   # json= param auto-sets Content-Type and serialises
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": "Hello!"}]
    }
)

# Always check status before using response
response.raise_for_status()   # raises HTTPError for 4xx/5xx
result = response.json()
print(result["content"][0]["text"])
```


    

```python
# Robust request with timeout and error handling
def call_api(url: str, payload: dict, headers: dict) -> dict:
    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=30   # always set a timeout — never wait forever
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timed out after 30s")
        return {}
    except requests.exceptions.HTTPError as e:
        print(f"HTTP {e.response.status_code}: {e.response.text}")
        return {}
    except requests.exceptions.ConnectionError:
        print("Cannot connect — check network / URL")
        return {}
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📦</span><h3>JSON Deep Dive</h3><span class="tag tag-teal">Critical for LLM Responses</span></div>
  <div class="cp-body">
    

```python
import json

# Serialise Python → JSON string
data = {"name": "Ajay", "scores": [85, 92], "active": True, "meta": None}
json_str = json.dumps(data)              # compact
json_str = json.dumps(data, indent=2)   # pretty-printed

# Deserialise JSON string → Python
parsed = json.loads(json_str)

# File I/O
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json") as f:
    loaded = json.load(f)

# Python ↔ JSON type mapping
# Python dict  → JSON object   {}
# Python list  → JSON array    []
# Python str   → JSON string   ""
# Python int/float → JSON number
# Python True  → JSON true
# Python None  → JSON null

# Navigating nested LLM API responses
response = {
    "id": "msg_01",
    "content": [{"type": "text", "text": "Hello! How can I help?"}],
    "usage": {"input_tokens": 10, "output_tokens": 8}
}
text    = response["content"][0]["text"]          # direct access
tokens  = response.get("usage", {}).get("output_tokens", 0)  # safe get
```


  </div>
</div>
</div><!-- end t3 -->
<!-- ══════════ TAB 4 — ASYNC/AWAIT ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Why Async — The Problem It Solves</h3><span class="tag tag-purple">Concept First</span></div>
  <div class="cp-body">
<p>LLM API calls take 1–10 seconds each. If you make 10 calls sequentially, you wait 10–100 seconds. Async Python lets you start all 10 calls, then handle them as they complete — total wait ≈ the slowest single call.</p>
    

```python
# Synchronous — sequential, blocks on each call
import time

def slow_api_call(n):
    time.sleep(2)         # simulates 2s LLM API call
    return f"result_{n}"

start = time.time()
results = [slow_api_call(i) for i in range(5)]
print(f"Sync: {time.time()-start:.1f}s")  # ~10.0s

# Asynchronous — concurrent, all run simultaneously
import asyncio

async def slow_api_call_async(n):
    await asyncio.sleep(2)   # yields control while waiting
    return f"result_{n}"

async def main():
    start = time.time()
    results = await asyncio.gather(
        *[slow_api_call_async(i) for i in range(5)]
    )
    print(f"Async: {time.time()-start:.1f}s")  # ~2.0s
    return results

asyncio.run(main())
```


<div class="ins"><p>💡 <strong>Async does NOT make code faster for CPU-bound work</strong> — it only helps for I/O-bound work (network calls, file reads, database queries). LLM API calls are I/O-bound. Matrix multiplications are CPU-bound. Know the difference.</p></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>Async Syntax and Patterns</h3><span class="tag tag-blue">Core Syntax</span></div>
  <div class="cp-body">
    

```python
import asyncio, httpx

# async def — defines a coroutine (NOT a regular function)
async def fetch_weather(city: str) -> dict:
    async with httpx.AsyncClient() as client:   # async HTTP client
        response = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": 19.07, "longitude": 72.87}
        )
        return response.json()

# await — pauses current coroutine until awaitable completes
# Can only use await INSIDE an async def function

# asyncio.gather — run multiple coroutines concurrently
async def fetch_all_cities():
    results = await asyncio.gather(
        fetch_weather("Mumbai"),
        fetch_weather("Delhi"),
        fetch_weather("Bangalore"),
    )
    return results

# asyncio.run — entry point for top-level async code
if __name__ == "__main__":
    results = asyncio.run(fetch_all_cities())
```


    

```python
# Async context managers — async with
async with httpx.AsyncClient() as client:
    # client is available here, closed automatically after block
    response = await client.get(url)

# Async iteration — async for
async def stream_response():
    async with anthropic_client.messages.stream(...) as stream:
        async for text in stream.text_stream:
            print(text, end="", flush=True)

# asyncio.create_task — fire and forget (don't wait immediately)
async def main():
    task1 = asyncio.create_task(fetch_weather("Mumbai"))
    task2 = asyncio.create_task(fetch_weather("Delhi"))
    # ... do other work here ...
    result1 = await task1   # now wait for results
    result2 = await task2
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🚨</span><h3>Common Async Mistakes</h3><span class="tag tag-teal">Pitfalls</span></div>
  <div class="cp-body">
    

```python
# MISTAKE 1 — forgetting await (most common)
async def bad():
    result = fetch_weather("Mumbai")   # returns coroutine object, not result!
    print(result)                       # prints <coroutine object ...>

async def good():
    result = await fetch_weather("Mumbai")   # correct

# MISTAKE 2 — calling async function without await at top level
fetch_weather("Mumbai")        # creates coroutine but never runs it
asyncio.run(fetch_weather("Mumbai"))   # correct

# MISTAKE 3 — using time.sleep instead of asyncio.sleep in async code
async def bad_sleep():
    time.sleep(2)       # BLOCKS the entire event loop — kills concurrency

async def good_sleep():
    await asyncio.sleep(2)   # yields control to event loop

# MISTAKE 4 — using requests (sync) in async code
# Use httpx.AsyncClient() or aiohttp instead of requests in async functions
```


<div class="ins"><p>💡 <strong>Rule of thumb:</strong> If you are inside an <code>async def</code> function, any blocking I/O call (requests, time.sleep, file reads with slow storage) must be replaced with its async equivalent. Mixing sync blocking calls into async code defeats the entire purpose.</p></div>
  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Async in FastAPI and LLM SDKs — Preview</h3><span class="tag tag-orange">Month 2 Preview</span></div>
  <div class="cp-body">
    

```python
# FastAPI — all route handlers can be async
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/chat")
async def chat(message: str):
    # await the LLM call — non-blocking
    response = await llm_client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": message}]
    )
    return {"reply": response.content[0].text}

# Anthropic SDK — async client
import anthropic

async def ask_claude(prompt: str) -> str:
    client = anthropic.AsyncAnthropic()   # async client
    message = await client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text
```


  </div>
</div>
</div><!-- end t4 -->
<!-- ══════════ TAB 5 — WEEK PLAN ══════════ -->
<div id="t5" class="tab-pane">
<p class="sep">2-WEEK STRUCTURED PLAN</p>
<table class="wk-table">
  <thead><tr><th>Week</th><th>Topics</th><th>Daily Task / Mini-Project</th></tr></thead>
  <tbody>
<tr>
<td class="wk-num">Week 1<br><em>Git + CLI</em></td>
<td>Install Git. Configure user.name and user.email. git init, add, commit, push, pull. Branching and merging. .gitignore for Python/AI projects. Terminal navigation: pwd, ls, cd, mkdir, rm, cp, mv. cat, less, grep, head, tail. Environment variables and .env files. Running Python scripts from terminal.</td>
<td>Day 1: Push all previous module projects to GitHub with proper READMEs. Day 2–3: Create a feature branch, make changes, merge back — practice the full branch→PR→merge workflow. Day 4–5: Write a shell one-liner that finds all Python files modified in the last 24 hours. Day 6–7: Set up .env file and load API keys using python-dotenv in a test script.</td>
</tr>
<tr>
<td class="wk-num">Week 2<br><em>APIs + Async</em></td>
<td>HTTP fundamentals: GET vs POST, status codes, headers, request/response structure. Python requests library: GET, POST, params, json=, headers, timeout, error handling. JSON: json.loads/dumps, nested navigation, file I/O. Async/await: asyncio.run, asyncio.gather, asyncio.sleep. httpx.AsyncClient for async HTTP. Common async mistakes.</td>
<td>Day 1–2: Write a weather CLI tool using Open-Meteo API (no key needed) — print 7-day forecast formatted nicely. Day 3–4: Rewrite the weather tool using async httpx to fetch 5 cities simultaneously. Day 5–7: Milestone project — Public API Script (see Projects tab).</td>
</tr>
  </tbody>
</table>
</div><!-- end t5 -->
<!-- ══════════ TAB 6 — RESOURCES ══════════ -->
<div id="t6" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
<tr><td class="res-type">Interactive</td><td><a href="https://skills.github.com/" target="_blank" rel="noopener">GitHub Skills — skills.github.com</a></td><td>Official interactive Git courses built inside GitHub. Start here for Git.</td></tr>
<tr><td class="res-type">Interactive</td><td><a href="https://learngitbranching.js.org/" target="_blank" rel="noopener">Learn Git Branching — learngitbranching.js.org</a></td><td>Best visual tool for understanding branches and merges. Do all levels.</td></tr>
<tr><td class="res-type">Book</td><td><a href="https://git-scm.com/book/en/v2" target="_blank" rel="noopener">Pro Git Book (Free online) — git-scm.com</a></td><td>Comprehensive reference. Read Ch 1–3 then use as lookup.</td></tr>
<tr><td class="res-type">Docs</td><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview" target="_blank" rel="noopener">MDN Web Docs: HTTP Overview</a></td><td>Best explanation of how HTTP requests and responses work.</td></tr>
<tr><td class="res-type">Docs</td><td><a href="https://requests.readthedocs.io/" target="_blank" rel="noopener">Python requests library docs — requests.readthedocs.io</a></td><td>Comprehensive reference for calling web APIs in Python.</td></tr>
<tr><td class="res-type">Course</td><td><a href="https://realpython.com/async-io-python/" target="_blank" rel="noopener">Real Python: Async IO in Python — realpython.com</a></td><td>Best async/await tutorial. Read after Week 2 Day 3.</td></tr>
<tr><td class="res-type">Course</td><td><a href="https://missing.csail.mit.edu/" target="_blank" rel="noopener">MIT Missing Semester — missing.csail.mit.edu</a></td><td>Shell scripting, terminal tools, and CLI fluency. Best for experienced engineers.</td></tr>
  </tbody>
</table>
</div><!-- end t6 -->
<!-- ══════════ TAB 7 — PROJECTS ══════════ -->
<div id="t7" class="tab-pane">
<p class="sep">MILESTONE PROJECT</p>
<div class="proj-box">
  <div class="proj-hdr">
<span>🛠</span>
<span class="proj-title">Public API Script — Weather + Async</span>
<span class="proj-dur">[Beginner] 2–3 days · Week 2</span>
  </div>
  <div class="proj-body">
<p>Build a Python script that calls real public APIs, handles errors robustly, uses async for concurrent requests, and is pushed to GitHub as a proper project.</p>
<h4>Requirements</h4>
<ul>
<li>Calls the Open-Meteo API to fetch a 7-day weather forecast (no API key needed)</li>
<li>Accepts a list of 5 cities as input — fetches all 5 concurrently using asyncio.gather</li>
<li>Parses the JSON response and formats output as a clean table (city, date, max temp, min temp)</li>
<li>Handles errors: invalid city, timeout (30s), HTTP errors — never crashes</li>
<li>Saves raw JSON responses to a <code>data/</code> folder with timestamp in filename</li>
<li>Proper .gitignore, .env.example, requirements.txt, and README</li>
</ul>
<h4>Stretch Goals</h4>
<ul>
<li>Add a <code>--cache</code> flag that reads from saved JSON if file is less than 1 hour old</li>
<li>Accept cities as CLI arguments using argparse</li>
<li>Add a simple retry mechanism: if a request fails, retry up to 3 times with 1s backoff</li>
</ul>
    

```python
# Starter structure
import asyncio, httpx, json
from pathlib import Path
from datetime import datetime

BASE_URL = "https://api.open-meteo.com/v1/forecast"
CITIES = {
    "Mumbai":    (19.07, 72.87),
    "Delhi":     (28.67, 77.22),
    "Bangalore": (12.97, 77.59),
    "Chennai":   (13.08, 80.27),
    "Kolkata":   (22.57, 88.36),
}

async def fetch_city(client: httpx.AsyncClient, city: str, lat: float, lon: float) -> dict:
    # Your implementation here
    ...
```


  </div>
</div>
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">GitHub Portfolio Push</span><span class="proj-dur">1 day · Week 1</span></div>
  <div class="proj-body">
<p>Push all three projects from P1-M01 and P1-M02 to GitHub. Each must have: a proper README (problem, tech stack, how to run, example output), requirements.txt, .gitignore, and at least 3 commits with meaningful commit messages (not just "update" or "fix"). This is your portfolio foundation — start it right.</p>
  </div>
</div>
</div><!-- end t7 -->
<!-- ══════════ TAB 8 — LABS ══════════ -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Git — The Full Branch, Conflict, and Merge Workflow</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Experience a real merge conflict and resolve it — this is something every developer encounters and many find intimidating the first time.</p>
<div class="lab-step"><div class="sn">1</div><div>Create a new repo: <code>mkdir git-lab && cd git-lab && git init</code>. Create <code>main.py</code> with one function. Add, commit with message "feat: initial main function".</div></div>
<div class="lab-step"><div class="sn">2</div><div>Create two branches from main: <code>git checkout -b feature-a</code>. Edit line 3 of main.py to say "Version A". Commit. Switch back to main: <code>git switch main</code>.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Create <code>git checkout -b feature-b</code>. Edit the SAME line 3 to say "Version B". Commit. Switch back to main: <code>git switch main</code>.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Merge feature-a into main: <code>git merge feature-a</code>. Then try to merge feature-b: <code>git merge feature-b</code>. Git reports a conflict.</div></div>
<div class="lab-step"><div class="sn">5</div><div>Open main.py — you will see conflict markers: <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD</code>, <code>=======</code>, <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt; feature-b</code>. Edit the file to keep the version you want (or combine both). Remove all conflict markers.</div></div>
<div class="lab-step"><div class="sn">6</div><div><code>git add main.py</code> then <code>git commit -m "merge: resolve conflict between feature-a and feature-b"</code>. Run <code>git log --oneline --graph</code> to see the merge commit in the branch graph.</div></div>
<div class="lab-step"><div class="sn">7</div><div><strong>Bonus:</strong> Push this repo to GitHub. Create a Pull Request from feature-b into main on GitHub instead of merging locally. Review the PR diff UI.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>HTTP Debugging — Inspect Every Layer of an API Call</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> See exactly what bytes travel over the network when you call an API — building intuition for debugging production failures.</p>
<div class="lab-step"><div class="sn">1</div><div>Install httpie: <code>pip install httpie</code>. Run: <code>http GET "https://api.open-meteo.com/v1/forecast?latitude=19.07&longitude=72.87&daily=temperature_2m_max&timezone=Asia/Kolkata"</code>. Observe: status line, response headers, JSON body.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Now trigger each error code intentionally: (a) 404: request a non-existent endpoint. (b) 400: send invalid parameters. (c) Use <code>httpbin.org/status/429</code> to see a rate limit response. Document the full response for each.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Write a Python script using requests that calls the Open-Meteo API. Before processing the response, print: <code>response.status_code</code>, <code>response.headers["Content-Type"]</code>, <code>len(response.content)</code> (bytes), and <code>response.elapsed.total_seconds()</code> (latency).</div></div>
<div class="lab-step"><div class="sn">4</div><div>Add a requests Session with retry logic: use <code>requests.adapters.HTTPAdapter</code> with <code>max_retries=3</code>. Test that it retries on connection errors by pointing to a non-existent host.</div></div>
<div class="lab-step"><div class="sn">5</div><div><strong>Bonus:</strong> Use <code>curl -v</code> from the terminal to make the same API call. Identify: the TLS handshake, the HTTP request headers sent, and the response headers received. Compare with what requests sends.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Async Concurrency — Measure Real Speedup</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Empirically measure the async speedup on real network requests — so the performance benefit is concrete, not theoretical.</p>
<div class="lab-step"><div class="sn">1</div><div>Install httpx: <code>pip install httpx</code>. Create a list of 10 different city coordinates for the Open-Meteo API.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Write a <strong>synchronous</strong> version using requests: loop over all 10 cities, make one request at a time. Time the total with <code>time.perf_counter()</code>.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Write an <strong>async</strong> version using httpx.AsyncClient and asyncio.gather. Run all 10 requests concurrently. Time it the same way.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Print both times and compute the speedup ratio. Record: (a) sync time, (b) async time, (c) ratio, (d) individual request latency.</div></div>
<div class="lab-step"><div class="sn">5</div><div>Now deliberately add <code>await asyncio.sleep(0)</code> inside the async function to simulate yielding. Does performance change? Why or why not?</div></div>
<div class="lab-step"><div class="sn">6</div><div><strong>Bonus:</strong> Add error handling: if any city request fails, continue with the others and report which cities succeeded vs failed. Use <code>asyncio.gather(..., return_exceptions=True)</code>.</div></div>
  </div>
</div>
</div><!-- end t8 -->
<!-- ══════════ TAB 9 — CHECKLIST ══════════ -->
<div id="t9" class="tab-pane">
<p class="sep">P1-M03 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain the Git working directory → staging area → local repo → remote flow in your own words</li>
  <li>Know the difference between git merge and git rebase — and when to use each</li>
  <li>Can resolve a merge conflict without using a GUI tool</li>
  <li>Have a .gitignore that covers Python artifacts, virtual environments, .env files, and model weights</li>
  <li>Can navigate the terminal without hesitation: cd, ls, mkdir, rm, grep, find, cat, tail -f</li>
  <li>Know what PATH is and can diagnose a "command not found" error</li>
  <li>Can load API keys from environment variables — never hardcode secrets in source code</li>
  <li>Know all HTTP methods (GET, POST, PUT, DELETE) and when each is used</li>
  <li>Can identify what went wrong from HTTP status codes: 400, 401, 403, 404, 429, 500, 503</li>
  <li>Can make a GET and POST request in Python using requests with proper timeout and error handling</li>
  <li>Can parse a deeply nested JSON response and safely access values with .get()</li>
  <li>Can explain what async def and await do in plain English</li>
  <li>Know the difference between asyncio.gather and sequential awaits — and when each is right</li>
  <li>Know never to use time.sleep or requests inside an async function — and what to use instead</li>
  <li>Can run asyncio.run() at the top level and write a coroutine that calls an async HTTP client</li>
  <li>Completed Lab 1: full branch, conflict, and merge workflow</li>
  <li>Completed Lab 2: HTTP debugging — inspected all layers of a real API call</li>
  <li>Completed Lab 3: measured real async speedup on concurrent HTTP requests</li>
  <li>Milestone project pushed to GitHub with README, .gitignore, requirements.txt</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P1-M04 — SQL Basics &amp; FastAPI</strong>. Everything you built here — async functions, HTTP knowledge, JSON handling — feeds directly into building your first API server and database queries.</p>
</div>
</div><!-- end t9 -->
<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/ai-ml/part1-foundation/p1-m02-numpy-pandas/">← P1-M02: NumPy &amp; Pandas</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part1-foundation/p1-m04-sql-fastapi/">Next: P1-M04 — SQL &amp; FastAPI →</a>
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
    const key = 'p1m03-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
