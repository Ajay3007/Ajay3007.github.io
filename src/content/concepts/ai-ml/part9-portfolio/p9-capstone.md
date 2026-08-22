---
title: "P9 - Capstone, Portfolio & Job-Readiness"
description: "Part 9 — Portfolio Launch · Final Module Capstone, Portfolio Job-Readiness Package everything you've built into a portfolio that gets you hired as an AI engineer ⏱ 2–4 Weeks 🏆…"
domain: ai-ml
track: ai-ml-engineering
module: part9-portfolio
order: 99
ownHeader: true
url: /learning/ai-ml/part9-portfolio/p9-capstone/
---

<style>
.mod-header{background:linear-gradient(135deg,#0f0a1e 0%,#1a1200 40%,#78350f 70%,#f59e0b 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#fcd34d;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#fef3c7;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#fef3c7}
.tab-bar{display:flex;flex-wrap:wrap;background:#1a1200;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#fcd34d;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#fbbf24;border-bottom-color:#fbbf24}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee);background:#fef3c7}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700;background:#fef3c7;color:#78350f}
.cp-body{padding:1.1rem 1.2rem}
.cp-body p,.cp-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.cp-body ul{margin:.4rem 0;padding-left:1.4rem}
.cp-body li{margin-bottom:.3rem}
.cp-body h4{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin:.9rem 0 .3rem}
.cb{background:#1a1200;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #f59e0b}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#fef3c7;white-space:pre}
.ins{background:#fef3c7;border:1.5px solid #f59e0b;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.warn{background:#fffbeb;border:1.5px solid #fbbf24;border-left:4px solid #d97706;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.sep{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--light-text,#888);border-bottom:1px solid var(--border-color,#e4e4e4);padding-bottom:.4rem;margin:2rem 0 1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin:2.5rem 0 1rem;padding-top:1.2rem;border-top:1.5px solid var(--border-color,#e4e4e4)}
.mod-nav a{font-size:.85rem;font-weight:600;color:#b45309;text-decoration:none;padding:.4rem .9rem;border-radius:6px;border:1.5px solid #b45309;transition:all .15s}
.mod-nav a:hover{background:#b45309;color:#fff}
/* project cards */
.proj-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1rem;margin:1rem 0}
.proj-card{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);padding:1.1rem;overflow:hidden}
.proj-card h4{font-size:.95rem;font-weight:700;color:var(--text-color,#111);margin:0 0 .5rem;border:none}
.proj-card p{font-size:.84rem;line-height:1.6;color:var(--text-color,#555);margin:0 0 .5rem}
.proj-card .tags{display:flex;flex-wrap:wrap;gap:.3rem}
.proj-card .tag{font-size:.7rem;font-family:monospace;font-weight:700;padding:2px 7px;border-radius:4px}
.tc-purple{border-color:#c4b5fd;background:#f5f0ff}.tc-purple h4{color:#5b21b6}.tc-purple .tag{background:#ede9fe;color:#4c1d95}
.tc-red{border-color:#fca5a5;background:#fff5f5}.tc-red h4{color:#991b1b}.tc-red .tag{background:#fee2e2;color:#991b1b}
.tc-amber{border-color:#fcd34d;background:#fffdf0}.tc-amber h4{color:#92400e}.tc-amber .tag{background:#fef3c7;color:#78350f}
.tc-green{border-color:#6ee7b7;background:#f0fff4}.tc-green h4{color:#065f46}.tc-green .tag{background:#d1fae5;color:#065f46}
.tc-blue{border-color:#93c5fd;background:#eff6ff}.tc-blue h4{color:#1e3a5f}.tc-blue .tag{background:#dbeafe;color:#1e40af}
/* GitHub README template */
.readme-box{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;overflow:hidden;margin:1rem 0}
.readme-hdr{background:#24292e;color:#fff;padding:.6rem 1rem;font-family:monospace;font-size:.8rem;display:flex;align-items:center;gap:.5rem}
.readme-body{padding:1rem 1.2rem;font-size:.84rem;line-height:1.7}
/* roadmap complete */
.complete-banner{background:linear-gradient(135deg,#0f0a1e,#1a1200,#78350f,#f59e0b);border-radius:14px;padding:2rem;color:#fff;text-align:center;margin:2rem 0}
.complete-banner h2{font-size:1.8rem;font-weight:900;margin-bottom:.5rem;border:none;color:#fff}
.complete-banner p{font-size:.95rem;color:#fef3c7;margin:0 0 1.5rem;max-width:600px;margin-inline:auto}
.complete-stats{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:.8rem;margin-top:1.5rem}
.cs-box{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:10px;padding:1rem}
.cs-box .num{font-size:1.8rem;font-weight:900;color:#fbbf24;font-family:monospace}
.cs-box .label{font-size:.75rem;color:#fef3c7;margin-top:.2rem}
/* cl */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem 0;border-bottom:1px solid var(--border-color,#eee);font-size:.88rem;line-height:1.6;cursor:pointer}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";font-size:1rem;flex-shrink:0;margin-top:.05rem;color:#b45309}
.cl li.done::before{content:"☑";color:#059669}
.cl li.done{color:var(--light-text,#888);text-decoration:line-through}
</style>
<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 9 — Portfolio &amp; Launch &nbsp;·&nbsp; Final Module</div>
  <div class="mod-title">Capstone, Portfolio &amp; Job-Readiness</div>
  <div class="mod-subtitle">Package everything you've built into a portfolio that gets you hired as an AI engineer</div>
  <div class="mod-pills">
<span class="mod-pill">⏱ 2–4 Weeks</span>
<span class="mod-pill">🏆 Capstone</span>
<span class="mod-pill">📂 GitHub Portfolio · Resume · LinkedIn · Outreach</span>
<span class="mod-pill">🎯 Goal: AI Engineering Job</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">🗺 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">📂 Portfolio Projects</button>
  <button class="tab-btn" onclick="vt(event,'t2')">📋 GitHub READMEs</button>
  <button class="tab-btn" onclick="vt(event,'t3')">📄 Resume</button>
  <button class="tab-btn" onclick="vt(event,'t4')">💼 LinkedIn & Outreach</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🎙 Technical Interviews</button>
  <button class="tab-btn" onclick="vt(event,'t6')">🚀 Capstone Project</button>
  <button class="tab-btn" onclick="vt(event,'t7')">✅ Launch Checklist</button>
</div>
<!-- ══════════ TAB 0 — OVERVIEW ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What Part 9 Is About</h3><span class="tag">Final Stage</span></div>
  <div class="cp-body">
<p>You have built everything. Parts 1–8 gave you 27 modules of AI engineering skills — RAG systems, agents, production APIs, prompt engineering, containerisation, observability, and a specialisation track. Now you need to make those skills visible to employers.</p>
<p>Most engineers underinvest in the presentation layer. They build great things privately and expect recruiters to read their minds. This module teaches you to build the signal that gets you conversations: a curated GitHub portfolio, a metrics-driven resume, targeted outreach, and the ability to talk through your work technically.</p>
<h4>The Job Search Stack</h4>
<ul>
<li><strong>Portfolio</strong> — 3 public GitHub repos with excellent READMEs and live demos</li>
<li><strong>Resume</strong> — quantified impact, AI keywords, 1 page unless 10+ years experience</li>
<li><strong>LinkedIn</strong> — posts showcasing what you built, searchable by recruiters</li>
<li><strong>Outreach</strong> — warm DMs to engineers at target companies, not cold applications</li>
<li><strong>Technical interview prep</strong> — system design for AI, coding, and ML fundamentals</li>
</ul>
<div class="ins"><p>💡 <strong>Three deployed projects beat fifty tutorial certificates.</strong> Employers in AI engineering hire for demonstrated capability. A live RAG API, a deployed SaaS app, and a fine-tuned model on HuggingFace Hub signal more than any course completion badge.</p></div>
  </div>
</div>
</div>
<!-- ══════════ TAB 1 — PORTFOLIO PROJECTS ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp">
  <div class="cp-hdr"><span class="ico">📂</span><h3>Your Portfolio: 3 Pinned Projects</h3><span class="tag">Selection</span></div>
  <div class="cp-body">
<p>GitHub lets you pin 6 repos. Pin 3 AI engineering projects. Everything else is secondary. Each pinned project should demonstrate a different layer of the stack.</p>
<div class="proj-grid">
<div class="proj-card tc-blue">
<h4>Project 1 — Production RAG API</h4>
<p>Your M18 "Chat With Your Docs" built to production standard: ChromaDB + Cohere reranker + grounded answers + citations + streaming FastAPI.</p>
<div class="tags"><span class="tag">RAG</span><span class="tag">FastAPI</span><span class="tag">Anthropic</span><span class="tag">Deployed</span></div>
</div>
<div class="proj-card tc-purple">
<h4>Project 2 — Agent System</h4>
<p>Your M21 hardened research agent: LangGraph, human-in-the-loop, cost circuit breaker, structured logging. Or your track specialisation capstone.</p>
<div class="tags"><span class="tag">LangGraph</span><span class="tag">Agents</span><span class="tag">Production</span></div>
</div>
<div class="proj-card tc-amber">
<h4>Project 3 — Your Track Capstone</h4>
<p>Track A: deployed SaaS with Stripe. Track B: fine-tuned model + eval report. Track C: enterprise automation. Track D: analysis pipeline with report generation.</p>
<div class="tags"><span class="tag">Specialisation</span><span class="tag">Deployed</span><span class="tag">Domain</span></div>
</div>
</div>
<h4>What Makes a Project Portfolio-Ready</h4>
<ul>
<li><strong>Deployed and live</strong> — a URL you can click during an interview. Not "see the screenshots."</li>
<li><strong>Excellent README</strong> — architecture diagram, problem statement, demo GIF or screenshot, tech stack badges (see Tab 2)</li>
<li><strong>Quantified results</strong> — "RAG faithfulness: 0.91 on 30-question eval set" beats "good accuracy"</li>
<li><strong>Production code quality</strong> — type hints, tests, .env.example, no hardcoded API keys, no 500-line main.py</li>
<li><strong>Commit history</strong> — evidence of iteration, not a single "initial commit + everything"</li>
</ul>
<div class="warn"><p>⚠️ <strong>Never put real API keys, credentials, or personal data in a public repo.</strong> Use a .env.example file showing required environment variables. Add .env to .gitignore before your first commit — it is very difficult to remove secrets from git history after the fact.</p></div>
  </div>
</div>
</div><!-- end t1 -->
<!-- ══════════ TAB 2 — GITHUB READMES ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp">
  <div class="cp-hdr"><span class="ico">📋</span><h3>Writing READMEs That Get You Interviews</h3><span class="tag">Signal</span></div>
  <div class="cp-body">
<p>The README is your project's cover letter. Most engineers write one paragraph. A great README takes 2 hours and generates 10x more recruiter interest.</p>
<div class="readme-box">
<div class="readme-hdr">📄 README.md — Template Structure</div>
<div class="readme-body">
<pre style="font-family:monospace;font-size:.83rem;line-height:1.8;color:var(--text-color,#222);white-space:pre-wrap">
# Project Name — One-Line Value Proposition
 
[`![Deploy](badge-url)`](live-demo-url) [`![Python](badge-url)`](pypi) [`![License](badge-url)`](license)
 
> **[Live Demo](https://your-demo-url.com)** | Built with Claude + FastAPI + ChromaDB
 
## What It Does
2–3 sentences. What problem does it solve? Who is it for? What's the result?
"A production-ready RAG API that lets you query your private documents in plain English,
with grounded answers and citations. Faithfulness: 0.91 on 30-question eval set."
 
## Demo
[GIF or screenshot of the app working — this is the most important element]
 
## Architecture
[Simple ASCII or Mermaid diagram showing: User → API → LLM/Vector DB → Response]
 
## Tech Stack
- **LLM**: Claude 3.5 Sonnet via Anthropic API
- **Retrieval**: ChromaDB + Cohere reranker (two-stage, retrieve-50 → rerank-5)
- **Backend**: FastAPI + Celery + Redis
- **Deployment**: Docker + Railway
 
## Results
| Metric | Score |
|--------|-------|
| RAG Faithfulness | 0.91 |
| Context Recall @5 | 0.84 |
| p95 Query Latency | 1.2s |
 
## Quick Start
```bash
git clone https://github.com/you/project
cp .env.example .env  # add your API keys
docker compose up
# Open http://localhost:8000/docs
```
 
## Key Technical Decisions
- Used two-stage retrieval (vector → reranker) because baseline hit_rate@5 was 0.65; improved to 0.84
- Chose ChromaDB over Pinecone for self-hosting cost control at this scale
- Added Anthropic prompt caching for system prompt (90% cost reduction on repeated queries)
</pre>
</div>
</div>
    <div class="cb"><pre># Generate a demo GIF with terminalizer or vhs
pip install terminalizer
terminalizer record demo
terminalizer render demo -o demo.gif
 
# Or use asciinema for terminal demos
pip install asciinema
asciinema rec demo.cast
asciinema upload demo.cast  # get a shareable URL
 
# Add shields.io badges to README
# https://img.shields.io/badge/Python-3.12-blue
# https://img.shields.io/badge/FastAPI-0.109-green
# https://img.shields.io/badge/Live_Demo-Click_Here-orange
 
# Pin your best repos on GitHub profile:
# Profile → Customize profile → Pin repositories → select 3</pre></div>
  </div>
</div>
</div><!-- end t2 -->
<!-- ══════════ TAB 3 — RESUME ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp">
  <div class="cp-hdr"><span class="ico">📄</span><h3>AI Engineering Resume — Principles</h3><span class="tag">Job Search</span></div>
  <div class="cp-body">
<h4>Structure (1 page, no exceptions under 10 years experience)</h4>
<ul>
<li><strong>Name + contact</strong> — email, GitHub URL, LinkedIn URL, portfolio/demo URL</li>
<li><strong>Summary</strong> (2 sentences) — role target + top 3 skills + years experience</li>
<li><strong>Skills</strong> — grouped: LLM APIs (Anthropic, OpenAI) | Frameworks (FastAPI, LangGraph, LlamaIndex) | Infrastructure (Docker, Redis, Prometheus) | Languages (Python, TypeScript)</li>
<li><strong>Projects</strong> — 3 bullet points each. Lead with impact, not description.</li>
<li><strong>Experience</strong> — reverse chronological. Reframe existing work using AI engineering language.</li>
</ul>
<h4>The STAR-Metric Formula for Each Bullet</h4>
    <div class="cb"><pre># BAD — describes what you did
"Built a RAG system using ChromaDB and the Anthropic API"
 
# GOOD — leads with impact, shows measurement
"Built production RAG API serving 500+ queries/day: 0.91 faithfulness score,
1.2s p95 latency, 90% cost reduction via Anthropic prompt caching"
 
# BAD — vague agent project
"Developed an AI agent using LangGraph"
 
# GOOD — quantified with production details
"Shipped LangGraph research agent with circuit breaker (capped at $0.50/session),
human-in-the-loop approval for sensitive tools, structured logging — reduced
manual research time by 60% for 3 team members"
 
# BAD — generic Python experience
"Used Python for backend development"
 
# GOOD — specific AI engineering context
"Led migration of 4 microservices to async FastAPI with LLM integration;
added Prometheus metrics and Grafana dashboards reducing MTTD from 2h to 8min"</pre></div>
<h4>Keywords That Get Past ATS Filters</h4>
<p>Include these naturally in your bullets and skills section:</p>
    <div class="cb"><pre># AI/LLM keywords (pick the ones you actually know)
RAG · Retrieval-Augmented Generation · LLM · Large Language Models
Anthropic Claude · OpenAI GPT · prompt engineering · fine-tuning
LangChain · LangGraph · LlamaIndex · vector database · embeddings
ChromaDB · Pinecone · Qdrant · pgvector · semantic search · reranking
 
# Infrastructure keywords
FastAPI · async Python · Docker · Docker Compose · Celery · Redis
Prometheus · Grafana · structlog · distributed tracing · OpenTelemetry
GitHub Actions · CI/CD · blue-green deployment
 
# ML/Eval keywords (if Track B)
HuggingFace · PEFT · LoRA · QLoRA · Unsloth · vLLM · GGUF
SHAP · model evaluation · evals · DeepEval · Ragas</pre></div>
  </div>
</div>
</div><!-- end t3 -->
<!-- ══════════ TAB 4 — LINKEDIN & OUTREACH ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp">
  <div class="cp-hdr"><span class="ico">💼</span><h3>LinkedIn Content That Generates Inbound</h3><span class="tag">Visibility</span></div>
  <div class="cp-body">
<p>Post 2–3 times per week during your job search. Share what you built, what you learned, what failed. AI engineering content gets 3–5x more engagement than generic tech content right now. One viral post generates more recruiter messages than 100 cold applications.</p>
<h4>Content Formats That Work</h4>
<ul>
<li><strong>Build in public</strong> — "Built a production RAG system this week. Here's what surprised me about chunking..." [screenshot]</li>
<li><strong>Lessons learned</strong> — "3 things I got wrong in my first agent loop and how I fixed them"</li>
<li><strong>Quantified results</strong> — "Compared Cohere reranker vs no reranker on my test set. Faithfulness went from 0.65 to 0.91. Chart:"</li>
<li><strong>Technical takes</strong> — "Agents are overused. 70% of 'agent' use cases I've seen would be better as simple chains. Here's the decision framework I use..."</li>
</ul>
<h4>Warm Outreach Template (DM to AI engineer at target company)</h4>
    <div class="cb"><pre>Hi [Name],
 
I've been following [Company]'s work on [specific thing — blog post, open source project, paper].
I noticed [specific observation showing you did your research].
 
I'm an AI engineer with [X years] background in [your domain — networking, distributed systems].
I've been building RAG systems and LangGraph agents this year and published a few things:
[link to best project].
 
I'd love to hear how [Company] is approaching [specific technical problem they work on].
Happy to share what I've learned from my production RAG work if that's useful.
 
[Name]</pre></div>
<div class="ins"><p>💡 <strong>Warm outreach (specific, researched DM) converts 10-20% of the time. Cold applications convert 1-3%.</strong> Find engineers at target companies on LinkedIn. Read what they post. Comment thoughtfully for a week before DM-ing. When you DM, reference something specific about their work — not a generic "I'm interested in your company."</p></div>
<h4>Job Boards That Work for AI Engineering</h4>
<ul>
<li>Anthropic Careers (careers.anthropic.com)</li>
<li>AIJobs.net — AI-specific job board</li>
<li>Levels.fyi — for compensation research before negotiating</li>
<li>LinkedIn Jobs filtered by "AI Engineer" + "LLM" + location</li>
<li>Twitter/X "hiring AI engineer" — many startups hire this way</li>
</ul>
  </div>
</div>
</div><!-- end t4 -->
<!-- ══════════ TAB 5 — TECHNICAL INTERVIEWS ══════════ -->
<div id="t5" class="tab-pane">
<div class="cp">
  <div class="cp-hdr"><span class="ico">🎙</span><h3>AI Engineering Interview Preparation</h3><span class="tag">Get Hired</span></div>
  <div class="cp-body">
<h4>System Design for AI — Common Questions</h4>
<ul>
<li>"Design a document Q&A system for 10 million documents" → talk about chunking, vector DB selection, retrieval quality, caching, cost</li>
<li>"Design an AI customer support system" → routing, RAG, escalation, human handoff, evaluation</li>
<li>"How would you reduce LLM API costs by 50%?" → model routing, prompt caching, response caching, batching, smaller max_tokens</li>
<li>"How do you evaluate a RAG system?" → faithfulness, context recall, hit rate, LLM-as-judge, eval datasets</li>
<li>"How do you handle an agent that gets stuck in a loop?" → fingerprinting, max_turns, circuit breaker, structured recovery</li>
</ul>
    <div class="cb"><pre># Framework for AI system design answers:
 
# 1. Clarify requirements
# "How many queries/day? What latency SLA? What's the document corpus size?
#  Is accuracy or speed more important? What's the budget?"
 
# 2. High-level architecture (draw boxes)
# User → API → [Retrieval: embed query → vector search → rerank] → [LLM: generate] → Response
 
# 3. Deep dive on the interesting parts
# "For retrieval, I'd use two-stage: ChromaDB top-50 then Cohere reranker to top-5.
#  Baseline hit_rate@5 is ~0.65; with reranking it's ~0.84 in my experience."
 
# 4. Scale and reliability
# "For 1M+ documents I'd use Qdrant or Pinecone. For cost, I'd cache
#  embeddings and responses. For reliability, retries with exponential backoff."
 
# 5. Evaluation
# "I'd run Ragas on a 50-question ground truth set. Monitor faithfulness drift in prod."</pre></div>
<h4>Coding Questions You'll Actually See</h4>
<ul>
<li>Implement a retry decorator with exponential backoff and jitter</li>
<li>Write a sliding window rate limiter</li>
<li>Implement a simple embedding cache with LRU eviction</li>
<li>Write async code: asyncio.gather for parallel API calls, return_exceptions=True</li>
<li>Implement cosine similarity and explain why it's used for embeddings</li>
</ul>
<h4>Behavioural Questions with AI Framing</h4>
<ul>
<li>"Tell me about a time you had to make a tradeoff between accuracy and cost in an AI system" — your cost monitoring and model routing work</li>
<li>"How do you keep up with the rapidly changing AI landscape?" — your learning journal, the roadmap you built</li>
<li>"Describe a production issue you've diagnosed" — your observability work, structured logging, Grafana alerts</li>
</ul>
  </div>
</div>
</div><!-- end t5 -->
<!-- ══════════ TAB 6 — CAPSTONE ══════════ -->
<div id="t6" class="tab-pane">
<div class="cp">
  <div class="cp-hdr"><span class="ico">🚀</span><h3>The Grand Capstone — Your Signature Project</h3><span class="tag">Showpiece</span></div>
  <div class="cp-body">
<p>Your grand capstone is a project that combines multiple Parts of this roadmap into one cohesive system specific to your professional domain. For you, that means networking / DPDK / telecom infrastructure — the domain where you have 4+ years of professional experience and can build something genuinely useful.</p>
<h4>Suggested Capstone: Intelligent DPDK/VPP Documentation Assistant</h4>
<p>A production AI system that lets network engineers query DPDK and VPP documentation, analyze configurations, and get code-level advice.</p>
<ul>
<li><strong>RAG backend</strong> — index official DPDK/VPP docs, DPDK programmer's guide, API references, community mailing list archives</li>
<li><strong>Agent layer</strong> — research agent that can search docs, retrieve code examples, compare versions, generate configuration snippets</li>
<li><strong>Production API</strong> — FastAPI with auth, rate limiting, streaming, Prometheus metrics, Grafana dashboard</li>
<li><strong>CI/CD</strong> — GitHub Actions: lint → eval → Docker build → deploy on push to main</li>
<li><strong>Evaluation</strong> — 30-question eval set covering mempool, ring buffer, PMD, DPDK EAL, VPP node graph</li>
<li><strong>Cost monitoring</strong> — per-query cost tracking, prompt caching for large doc system prompt</li>
</ul>
<div class="ins"><p>💡 <strong>Domain expertise is your moat.</strong> A generic "chat with PDFs" app has 10,000 competitors. An AI assistant for DPDK/VPP network engineers, built by someone who works professionally with these systems, has almost none. Your 4+ years of distributed systems and DPDK experience makes your AI product qualitatively better than anything a generalist could build.</p></div>
<h4>Alternative Capstone Ideas</h4>
<ul>
<li>Network configuration assistant: parse and explain complex DPDK/VPP configs with error detection</li>
<li>Performance analysis pipeline: ingest benchmark results, generate reports, suggest optimisations via AI</li>
<li>Telecom infrastructure knowledge base: RAG over 3GPP specs, ITU documents, and vendor documentation</li>
</ul>
<h4>Capstone Deliverables</h4>
<ul>
<li>Public GitHub repo with excellent README, architecture diagram, and eval results</li>
<li>Live demo URL (Railway, Render, or DigitalOcean — all have free/cheap tiers)</li>
<li>Blog post or LinkedIn series: "How I built a production AI assistant for network engineers"</li>
<li>HuggingFace Space demo (if Track B — fine-tuned model)</li>
</ul>
  </div>
</div>
</div><!-- end t6 -->
<!-- ══════════ TAB 7 — CHECKLIST ══════════ -->
<div id="t7" class="tab-pane">
<p class="sep">LAUNCH CHECKLIST — DO ALL OF THESE</p>
<p class="sep" style="margin-top:.5rem">PORTFOLIO</p>
<ul class="cl">
  <li>3 pinned GitHub repos — each with live demo URL in the repo description</li>
  <li>Each repo has: GIF/screenshot, architecture diagram, quantified results table, quick start instructions</li>
  <li>All repos have .env.example — no real credentials anywhere in git history</li>
  <li>Production code quality: type hints, tests, structured imports, no 500-line single files</li>
  <li>At least one project shows observability (Prometheus metrics or structured logs)</li>
  <li>At least one project shows evaluation methodology (faithfulness score, task success rate, or similar)</li>
</ul>
<p class="sep">RESUME</p>
<ul class="cl">
  <li>1 page (unless 10+ years experience)</li>
  <li>Every project bullet leads with impact metric, not description</li>
  <li>AI keywords included: RAG, LLM, embeddings, FastAPI, LangGraph, ChromaDB, Anthropic</li>
  <li>GitHub URL and portfolio/demo URL in header</li>
  <li>Had at least 2 other engineers review it for clarity and technical accuracy</li>
</ul>
<p class="sep">LINKEDIN</p>
<ul class="cl">
  <li>Headline mentions AI/LLM engineering and your background domain</li>
  <li>About section includes the specific AI systems you've built and deployed</li>
  <li>Featured section shows links to your best 2 projects</li>
  <li>At least 5 posts published showcasing your work (screenshots, results, lessons)</li>
</ul>
<p class="sep">OUTREACH</p>
<ul class="cl">
  <li>List of 20 target companies built — prioritised by domain fit and team quality</li>
  <li>Identified 2–3 engineers or hiring managers at each target company on LinkedIn</li>
  <li>Sent at least 10 warm, personalised DMs referencing specific work of the recipient</li>
  <li>Applied to at least 20 positions (warm outreach + direct applications)</li>
</ul>
<p class="sep">INTERVIEW PREP</p>
<ul class="cl">
  <li>Can whiteboard a RAG system design including retrieval, reranking, generation, and evaluation</li>
  <li>Can implement retry with exponential backoff from memory in Python</li>
  <li>Can explain LoRA in one paragraph for a non-ML interviewer</li>
  <li>Can articulate the cost/quality tradeoff in choosing a retrieval strategy</li>
  <li>Have done at least 3 mock system design interviews (with peers or on Pramp)</li>
</ul>
<p class="sep">CAPSTONE</p>
<ul class="cl">
  <li>Grand capstone project deployed and publicly accessible</li>
  <li>Evaluation report published (not just "it works" — actual metrics)</li>
  <li>At least one blog post or LinkedIn post explaining what you built and why</li>
</ul>
</div>
<!-- COMPLETION BANNER -->
<div class="complete-banner">
  <h2>🎉 AI/ML Roadmap Complete</h2>
  <p>You have built the complete AI engineering skill stack — from Python fundamentals to production-grade RAG systems, agents, and deployment. You are ready to build real AI products and compete for senior AI engineering roles.</p>
  <div class="complete-stats">
<div class="cs-box">
<div class="num">9</div>
<div class="label">Parts completed</div>
</div>
<div class="cs-box">
<div class="num">28</div>
<div class="label">Modules built</div>
</div>
<div class="cs-box">
<div class="num">3+</div>
<div class="label">Deployed projects</div>
</div>
<div class="cs-box">
<div class="num">1</div>
<div class="label">Specialisation track</div>
</div>
  </div>
</div>
<div class="mod-nav">
  <a href="/learning/ai-ml/part8-specialisation/">← Part 8: Specialisation</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ Full Roadmap</a>
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
    const key = 'p9_launch_ck_' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
