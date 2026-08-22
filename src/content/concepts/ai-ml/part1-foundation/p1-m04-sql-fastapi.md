---
title: "P1-M04 - SQL Basics & FastAPI"
description: "Part 1 — Universal Foundation · Module 04 of 04 SQL Basics FastAPI Query databases and build your first production API server ⏱ 2 Weeks 🟡 Beginner–Intermediate 🗄 SQLite ·…"
domain: ai-ml
track: ai-ml-engineering
module: part1-foundation
order: 104
ownHeader: true
url: /learning/ai-ml/part1-foundation/p1-m04-sql-fastapi/
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
/* milestone banner */
.milestone-banner{background:linear-gradient(135deg,#1a0a3a,#4c1d95);border-radius:12px;padding:1.5rem 1.8rem;color:#fff;margin:2rem 0;text-align:center}
.milestone-banner h3{font-size:1.3rem;font-weight:800;margin-bottom:.5rem;border:none;color:#fff}
.milestone-banner p{font-size:.9rem;color:#ddd6fe;margin:0}
.milestone-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:.8rem;margin-top:1rem}
.mg-item{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:8px;padding:.7rem 1rem;font-size:.83rem;color:#ede9fe;text-align:left}
.mg-item::before{content:"✓  ";color:#a78bfa;font-weight:700}
</style>
<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 1 — Universal Foundation &nbsp;·&nbsp; Module 04 of 04</div>
  <div class="mod-title">SQL Basics &amp; FastAPI</div>
  <div class="mod-subtitle">Query databases and build your first production API server</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 2 Weeks</span>
    <span class="mod-pill">🟡 Beginner–Intermediate</span>
    <span class="mod-pill">🗄 SQLite · FastAPI · Pydantic</span>
    <span class="mod-pill">📋 Prerequisite: P1-M01, P1-M03</span>
  </div>
</div>
<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🗄 SQL Fundamentals</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🔗 SQL Joins & Aggregations</button>
  <button class="tab-btn" onclick="vt(event,'t3')">⚡ FastAPI Basics</button>
  <button class="tab-btn" onclick="vt(event,'t4')">📐 Pydantic & Validation</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🔄 FastAPI + SQLite</button>
  <button class="tab-btn" onclick="vt(event,'t6')">📅 Week Plan</button>
  <button class="tab-btn" onclick="vt(event,'t7')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t9')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t10')">✅ Checklist</button>
</div>
<!-- ══════════ TAB 0 — OVERVIEW ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-purple">Final Foundation Module</span></div>
  <div class="cp-body">
    <p>This is the final module of Part 1 — and the payoff. SQL and FastAPI are the two tools you use to store data and expose it as an API. Every AI application you build — RAG pipelines, agent backends, model serving — will use both. By the end of this module you will have built and run your first real API server.</p>
    <ul>
      <li><strong>SQL</strong> — SELECT, WHERE, GROUP BY, JOIN, ORDER BY, aggregations with SQLite</li>
      <li><strong>Pandas + SQL</strong> — reading SQL query results directly into DataFrames</li>
      <li><strong>FastAPI basics</strong> — GET and POST endpoints, path parameters, query parameters, request bodies</li>
      <li><strong>Pydantic</strong> — data validation and schema definition with type hints</li>
      <li><strong>Running a server</strong> — uvicorn dev server, the /docs interface, testing endpoints</li>
      <li><strong>FastAPI + SQLite</strong> — connecting a database to your API for persistent storage</li>
    </ul>
  </div>
</div>
<div class="skip-box">
  <strong>⚡ SKIP IF:</strong> You know SQL from databases experience — jump directly to the FastAPI tab (Tab 3). If you know Spring Boot or Express.js, FastAPI will feel immediately familiar; spend your time on Pydantic validation and async endpoints, which are FastAPI-specific.
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Where These Skills Lead</h3><span class="tag tag-green">Forward Connections</span></div>
  <div class="cp-body">
    <ul>
      <li><strong>P1-M04 → P4 (LLM APIs)</strong> — FastAPI is how you expose LLM endpoints. Pydantic models are how you define structured output schemas.</li>
      <li><strong>P1-M04 → P5 (RAG)</strong> — pgvector extends PostgreSQL with vector search. SQLite stores document metadata alongside embeddings.</li>
      <li><strong>P1-M04 → P7 (Production)</strong> — production FastAPI uses async DB sessions, connection pooling, and all the patterns you learn here.</li>
      <li><strong>SQL fluency</strong> — used for log analysis, querying ML experiment results in MLflow, and reading data from feature stores.</li>
    </ul>
  </div>
</div>
</div><!-- end t0 -->
<!-- ══════════ TAB 1 — SQL FUNDAMENTALS ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🗄</span><h3>SQL Mental Model</h3><span class="tag tag-purple">Concept First</span></div>
  <div class="cp-body">
    <p>SQL (Structured Query Language) is a declarative language — you describe <em>what</em> data you want, not <em>how</em> to fetch it. The database engine figures out the how. Think of a SQL table like a Pandas DataFrame: rows are records, columns are fields, and SQL is the query language.</p>
    <div class="cb"><pre><span class="ck">-- SQL is not case-sensitive for keywords, but convention is UPPERCASE</span>
<span class="ck">-- Single-line comment: --</span>
<span class="ck">-- Multi-line: /* ... */</span>
<span class="ck">-- Create a table</span>
CREATE TABLE students (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT    NOT NULL,
    score   REAL    DEFAULT 0.0,
    grade   TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
 
<span class="ck">-- Insert rows</span>
INSERT INTO students (name, score, grade) VALUES ('Alice', 92.5, 'A');
INSERT INTO students (name, score, grade) VALUES ('Bob',   78.0, 'C');
INSERT INTO students (name, score, grade) VALUES ('Charlie',85.5, 'B');</pre></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>SELECT — The Core Query</h3><span class="tag tag-blue">Most Used</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck">-- Basic SELECT</span>
SELECT * FROM students;                     <span class="ck">-- all columns, all rows</span>
SELECT name, score FROM students;           <span class="ck">-- specific columns</span>
SELECT DISTINCT grade FROM students;        <span class="ck">-- unique values only</span>
<span class="ck">-- WHERE — filter rows</span>
SELECT * FROM students WHERE score > 80;
SELECT * FROM students WHERE grade = 'A' AND score >= 90;
SELECT * FROM students WHERE grade IN ('A', 'B');
SELECT * FROM students WHERE name LIKE 'A%';   <span class="ck">-- starts with A</span>
SELECT * FROM students WHERE score BETWEEN 70 AND 90;
SELECT * FROM students WHERE grade IS NULL;    <span class="ck">-- NULL check</span>
<span class="ck">-- ORDER BY — sort results</span>
SELECT * FROM students ORDER BY score DESC;        <span class="ck">-- highest first</span>
SELECT * FROM students ORDER BY grade ASC, score DESC;  <span class="ck">-- multi-column</span>
<span class="ck">-- LIMIT and OFFSET — pagination</span>
SELECT * FROM students ORDER BY score DESC LIMIT 10;          <span class="ck">-- top 10</span>
SELECT * FROM students ORDER BY score DESC LIMIT 10 OFFSET 20; <span class="ck">-- page 3</span>
<span class="ck">-- Computed columns and aliases</span>
SELECT name,
       score,
       score * 0.1  AS bonus_points,
       UPPER(name)  AS name_upper
FROM students;</pre></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Aggregations — COUNT, SUM, AVG, MIN, MAX</h3><span class="tag tag-teal">Analytics</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck">-- Aggregate functions</span>
SELECT COUNT(*)          AS total_students FROM students;
SELECT COUNT(grade)      AS graded_count   FROM students;  <span class="ck">-- skips NULLs</span>
SELECT AVG(score)        AS class_average  FROM students;
SELECT MAX(score)        AS highest        FROM students;
SELECT MIN(score)        AS lowest         FROM students;
SELECT SUM(score)        AS total_points   FROM students;
 
<span class="ck">-- GROUP BY — aggregate per group</span>
SELECT grade,
       COUNT(*)    AS student_count,
       AVG(score)  AS avg_score,
       MAX(score)  AS top_score
FROM students
GROUP BY grade
ORDER BY avg_score DESC;
 
<span class="ck">-- HAVING — filter AFTER grouping (WHERE filters before)</span>
SELECT grade, AVG(score) AS avg_score
FROM students
GROUP BY grade
HAVING AVG(score) > 80;    <span class="ck">-- only grades with class avg > 80</span>
<span class="ck">-- Rule: WHERE filters rows BEFORE grouping</span>
<span class="ck">--       HAVING filters groups AFTER aggregation</span></pre></div>
    <div class="ins"><p>💡 <strong>SQL execution order</strong> (not the same as write order): FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT. Understanding this prevents "column not found in WHERE" errors when using aliases.</p></div>
  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🐍</span><h3>SQL from Python — sqlite3 and Pandas</h3><span class="tag tag-orange">Integration</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import sqlite3
import pandas as pd
 
<span class="ck"># ── sqlite3 — standard library, no install needed ──</span>
conn = sqlite3.connect(<span class="cs">"students.db"</span>)    <span class="ck"># creates file if not exists</span>
cursor = conn.cursor()
 
<span class="ck"># Execute SQL</span>
cursor.execute(<span class="cs">"""
    CREATE TABLE IF NOT EXISTS students (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        name  TEXT    NOT NULL,
        score REAL
    )
"""</span>)
conn.commit()
 
<span class="ck"># Insert with parameterised query (NEVER use f-strings for SQL!)</span>
cursor.execute(<span class="cs">"INSERT INTO students (name, score) VALUES (?, ?)"</span>,
               (<span class="cs">"Alice"</span>, <span class="cv">92.5</span>))
conn.commit()
 
<span class="ck"># Bulk insert</span>
students = [(<span class="cs">"Bob"</span>, <span class="cv">78</span>), (<span class="cs">"Charlie"</span>, <span class="cv">85</span>), (<span class="cs">"Diana"</span>, <span class="cv">91</span>)]
cursor.executemany(<span class="cs">"INSERT INTO students (name, score) VALUES (?, ?)"</span>, students)
conn.commit()
 
<span class="ck"># Query results → Python list of tuples</span>
cursor.execute(<span class="cs">"SELECT * FROM students WHERE score > 80 ORDER BY score DESC"</span>)
rows = cursor.fetchall()
for row in rows:
    print(row)   <span class="ck"># (1, "Alice", 92.5)</span>
<span class="ck"># Query results → Pandas DataFrame (most useful pattern)</span>
df = pd.read_sql_query(
    <span class="cs">"SELECT name, score FROM students ORDER BY score DESC"</span>,
    conn
)
print(df.head())
 
conn.close()   <span class="ck"># always close when done</span></pre></div>
    <div class="warn"><p>⚠️ <strong>Never use string formatting or f-strings to build SQL queries.</strong> <code>f"SELECT * FROM users WHERE name = '{user_input}'"</code> is a SQL injection vulnerability. Always use parameterised queries with <code>?</code> placeholders. This is the most critical SQL security rule.</p></div>
  </div>
</div>
</div><!-- end t1 -->
<!-- ══════════ TAB 2 — SQL JOINS & AGGREGATIONS ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>JOINs — Combining Tables</h3><span class="tag tag-purple">Essential</span></div>
  <div class="cp-body">
    <p>JOINs combine rows from two tables based on a related column. The same four join types exist in Pandas merge — understanding them once applies to both.</p>
    <div class="cb"><pre><span class="ck">-- Sample tables</span>
<span class="ck">-- students: id, name, score, dept_id</span>
<span class="ck">-- departments: id, name, building</span>
<span class="ck">-- INNER JOIN — only rows that match in BOTH tables</span>
SELECT s.name, s.score, d.name AS department
FROM   students     s
JOIN   departments  d ON s.dept_id = d.id;
 
<span class="ck">-- LEFT JOIN — all students, even those with no department</span>
SELECT s.name, s.score, d.name AS department
FROM   students     s
LEFT JOIN departments d ON s.dept_id = d.id;
<span class="ck">-- d.name will be NULL for students with no matching dept_id</span>
<span class="ck">-- RIGHT JOIN (SQLite doesn't support — use LEFT JOIN with tables swapped)</span>
<span class="ck">-- Self-join — join a table to itself</span>
<span class="ck">-- Find all students who scored higher than Alice</span>
SELECT b.name, b.score
FROM   students a
JOIN   students b ON b.score > a.score
WHERE  a.name = 'Alice';</pre></div>
    <div class="cp p-teal" style="margin:0">
      <div class="cp-hdr"><span class="ico">📊</span><h3>JOIN Type Reference</h3><span class="tag tag-teal">Quick Lookup</span></div>
      <div class="cp-body">
        <table style="width:100%;border-collapse:collapse;font-size:.85rem">
          <thead><tr style="background:#1a0a3a;color:#ddd6fe"><th style="padding:.5rem .8rem;text-align:left">Join Type</th><th style="padding:.5rem .8rem">Returns</th><th style="padding:.5rem .8rem">Pandas Equivalent</th></tr></thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem"><strong>INNER JOIN</strong></td><td style="padding:.5rem .8rem">Only rows matching in both tables</td><td style="padding:.5rem .8rem"><code>how="inner"</code></td></tr>
            <tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem"><strong>LEFT JOIN</strong></td><td style="padding:.5rem .8rem">All left rows + matched right rows (NULL if no match)</td><td style="padding:.5rem .8rem"><code>how="left"</code></td></tr>
            <tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem"><strong>RIGHT JOIN</strong></td><td style="padding:.5rem .8rem">All right rows + matched left rows</td><td style="padding:.5rem .8rem"><code>how="right"</code></td></tr>
            <tr style="background:var(--bg-color,#f8f8f8)"><td style="padding:.5rem .8rem"><strong>FULL OUTER</strong></td><td style="padding:.5rem .8rem">All rows from both, NULL where no match</td><td style="padding:.5rem .8rem"><code>how="outer"</code></td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📈</span><h3>Subqueries and CTEs</h3><span class="tag tag-blue">Advanced Patterns</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck">-- Subquery in WHERE — students above class average</span>
SELECT name, score
FROM   students
WHERE  score > (SELECT AVG(score) FROM students);
 
<span class="ck">-- Subquery in FROM — treat query result as a table</span>
SELECT grade, avg_score
FROM (
    SELECT grade, AVG(score) AS avg_score
    FROM   students
    GROUP  BY grade
) AS grade_stats
WHERE avg_score > 75;
 
<span class="ck">-- CTE (Common Table Expression) — readable named subquery</span>
WITH above_avg AS (
    SELECT name, score
    FROM   students
    WHERE  score > (SELECT AVG(score) FROM students)
),
top_dept AS (
    SELECT dept_id, COUNT(*) AS count
    FROM   above_avg a
    JOIN   students s ON a.name = s.name
    GROUP  BY dept_id
    ORDER  BY count DESC
    LIMIT  1
)
SELECT d.name AS top_department
FROM   departments d
JOIN   top_dept t ON d.id = t.dept_id;</pre></div>
    <div class="ins"><p>💡 <strong>Use CTEs over nested subqueries whenever possible.</strong> CTEs are named, reusable, and read top-to-bottom like a story. Deeply nested subqueries become impossible to maintain. The <code>WITH name AS (...)</code> pattern is the professional SQL standard.</p></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>UPDATE, DELETE and Indexes</h3><span class="tag tag-teal">Data Management</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck">-- UPDATE — modify existing rows</span>
UPDATE students SET grade = 'A' WHERE score >= 90;
UPDATE students SET score = score * 1.05 WHERE grade = 'B';  <span class="ck">-- 5% bonus</span>
<span class="ck">-- DELETE — remove rows</span>
DELETE FROM students WHERE score < 40;
DELETE FROM students WHERE name = 'Bob';
 
<span class="ck">-- TRUNCATE equivalent in SQLite</span>
DELETE FROM students;   <span class="ck">-- removes all rows, table structure remains</span>
<span class="ck">-- Indexes — speed up queries on large tables</span>
CREATE INDEX idx_students_score ON students(score);
CREATE INDEX idx_students_grade ON students(grade);
CREATE UNIQUE INDEX idx_students_email ON students(email);
 
<span class="ck">-- When to create an index:</span>
<span class="ck">-- Columns frequently used in WHERE, ORDER BY, or JOIN conditions</span>
<span class="ck">-- Foreign key columns</span>
<span class="ck">-- High-cardinality columns (many unique values)</span>
<span class="ck">-- NOT on columns with very few unique values (e.g. boolean flag)</span>
<span class="ck">-- Check query plan (does it use the index?)</span>
EXPLAIN QUERY PLAN SELECT * FROM students WHERE score > 80;</pre></div>
  </div>
</div>
</div><!-- end t2 -->
<!-- ══════════ TAB 3 — FASTAPI BASICS ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>FastAPI — Why It Is the Standard for AI APIs</h3><span class="tag tag-purple">Context</span></div>
  <div class="cp-body">
    <p>FastAPI is the dominant Python framework for building AI APIs. It is fast (ASGI, async-first), automatically generates interactive docs, and uses Pydantic for validation — the same library used by LangChain, OpenAI SDK, and Anthropic SDK under the hood.</p>
    <div class="cb"><pre>pip install fastapi uvicorn[standard]
 
<span class="ck"># Minimal FastAPI app — save as main.py</span>
from fastapi import FastAPI
 
app = FastAPI(title=<span class="cs">"My AI API"</span>, version=<span class="cs">"1.0.0"</span>)
 
@app.get(<span class="cs">"/"</span>)
def root():
    return {<span class="cs">"message"</span>: <span class="cs">"AI API is running"</span>}
 
@app.get(<span class="cs">"/health"</span>)
def health():
    return {<span class="cs">"status"</span>: <span class="cs">"ok"</span>}
 
<span class="ck"># Run the server</span>
<span class="ck"># uvicorn main:app --reload</span>
<span class="ck"># Open http://127.0.0.1:8000/docs  ← interactive Swagger UI</span>
<span class="ck"># Open http://127.0.0.1:8000/redoc ← alternative docs</span></pre></div>
    <div class="ins"><p>💡 <strong>The <code>/docs</code> endpoint is one of FastAPI's killer features.</strong> It auto-generates an interactive Swagger UI from your code — you can test every endpoint directly in the browser without writing a client or using curl. Use it constantly while developing.</p></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🛤</span><h3>Path Parameters, Query Parameters and Request Bodies</h3><span class="tag tag-blue">Core Patterns</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional
 
app = FastAPI()
 
<span class="ck"># PATH PARAMETER — part of the URL path</span>
<span class="ck"># GET /students/42</span>
@app.get(<span class="cs">"/students/{student_id}"</span>)
def get_student(student_id: int):   <span class="ck"># FastAPI validates type automatically</span>
    return {<span class="cs">"student_id"</span>: student_id}
 
<span class="ck"># QUERY PARAMETER — after the ? in URL</span>
<span class="ck"># GET /students?min_score=80&limit=10</span>
@app.get(<span class="cs">"/students"</span>)
def list_students(
    min_score: float = <span class="cv">0.0</span>,                   <span class="ck"># optional with default</span>
    limit: int = Query(default=<span class="cv">20</span>, le=<span class="cv">100</span>),   <span class="ck"># with constraint: max 100</span>
    grade: Optional[str] = None               <span class="ck"># truly optional</span>
):
    return {<span class="cs">"min_score"</span>: min_score, <span class="cs">"limit"</span>: limit, <span class="cs">"grade"</span>: grade}
 
<span class="ck"># REQUEST BODY — JSON in POST/PUT body</span>
class CreateStudentRequest(BaseModel):
    name:  str
    score: float
    grade: Optional[str] = None
 
<span class="ck"># POST /students</span>
@app.post(<span class="cs">"/students"</span>, status_code=<span class="cv">201</span>)
def create_student(student: CreateStudentRequest):
    <span class="ck"># FastAPI auto-parses JSON body into the Pydantic model</span>
    <span class="ck"># Validation happens automatically — wrong types return 422</span>
    return {<span class="cs">"created"</span>: student.model_dump()}</pre></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🚨</span><h3>Error Handling and HTTP Exceptions</h3><span class="tag tag-teal">Production Pattern</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from fastapi import FastAPI, HTTPException, status
 
app = FastAPI()
 
STUDENTS_DB = {<span class="cv">1</span>: {<span class="cs">"name"</span>: <span class="cs">"Alice"</span>, <span class="cs">"score"</span>: <span class="cv">92</span>}}
 
@app.get(<span class="cs">"/students/{student_id}"</span>)
def get_student(student_id: int):
    student = STUDENTS_DB.get(student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=<span class="cs">f"Student {student_id} not found"</span>
        )
    return student
 
<span class="ck"># Custom exception handler</span>
from fastapi import Request
from fastapi.responses import JSONResponse
 
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=<span class="cv">400</span>,
        content={<span class="cs">"error"</span>: <span class="cs">"validation_error"</span>, <span class="cs">"detail"</span>: str(exc)}
    )
 
<span class="ck"># Health check endpoint — essential for production</span>
@app.get(<span class="cs">"/health"</span>, tags=[<span class="cs">"monitoring"</span>])
def health_check():
    return {
        <span class="cs">"status"</span>: <span class="cs">"healthy"</span>,
        <span class="cs">"version"</span>: app.version,
    }</pre></div>
  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Async Endpoints and Background Tasks</h3><span class="tag tag-orange">AI-Specific Pattern</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from fastapi import FastAPI, BackgroundTasks
import asyncio, anthropic
 
app = FastAPI()
client = anthropic.AsyncAnthropic()
 
<span class="ck"># Async endpoint — non-blocking LLM call</span>
@app.post(<span class="cs">"/chat"</span>)
async def chat(message: str):
    response = await client.messages.create(
        model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
        max_tokens=<span class="cv">1024</span>,
        messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: message}]
    )
    return {<span class="cs">"reply"</span>: response.content[<span class="cv">0</span>].text}
 
<span class="ck"># Streaming endpoint — sends tokens as they arrive</span>
from fastapi.responses import StreamingResponse
 
@app.post(<span class="cs">"/chat/stream"</span>)
async def chat_stream(message: str):
    async def generate():
        async with client.messages.stream(
            model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
            max_tokens=<span class="cv">1024</span>,
            messages=[{<span class="cs">"role"</span>: <span class="cs">"user"</span>, <span class="cs">"content"</span>: message}]
        ) as stream:
            async for text in stream.text_stream:
                yield text
    return StreamingResponse(generate(), media_type=<span class="cs">"text/plain"</span>)
 
<span class="ck"># Background task — fire and forget</span>
def log_request(message: str):
    with open(<span class="cs">"requests.log"</span>, <span class="cs">"a"</span>) as f:
        f.write(<span class="cs">f"{message}\n"</span>)
 
@app.post(<span class="cs">"/chat/logged"</span>)
async def chat_logged(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(log_request, message)  <span class="ck"># runs after response</span>
    return {<span class="cs">"reply"</span>: <span class="cs">"Processing..."</span>}</pre></div>
  </div>
</div>
</div><!-- end t3 -->
<!-- ══════════ TAB 4 — PYDANTIC ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📐</span><h3>Pydantic — Python's Data Validation Library</h3><span class="tag tag-purple">Critical for AI</span></div>
  <div class="cp-body">
    <p>Pydantic is used everywhere in the AI ecosystem — FastAPI, LangChain, OpenAI SDK, Anthropic SDK, and the Instructor library for structured LLM outputs. Learning it here pays dividends in every future module.</p>
    <div class="cb"><pre>from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime
 
<span class="ck"># Basic model — define schema with type annotations</span>
class Student(BaseModel):
    name:  str
    score: float
    grade: Optional[str] = None
 
s = Student(name=<span class="cs">"Alice"</span>, score=<span class="cv">92.5</span>)
print(s.model_dump())          <span class="ck"># {"name":"Alice","score":92.5,"grade":null}</span>
print(s.model_dump_json())     <span class="ck"># JSON string</span>
<span class="ck"># Validation — Pydantic raises ValidationError on wrong types</span>
try:
    bad = Student(name=<span class="cs">"Bob"</span>, score=<span class="cs">"not-a-number"</span>)
except Exception as e:
    print(e)   <span class="ck"># score: Input should be a valid number</span>
<span class="ck"># Field — add constraints and documentation</span>
class LLMRequest(BaseModel):
    model:       str   = Field(default=<span class="cs">"claude-3-5-sonnet-20241022"</span>)
    prompt:      str   = Field(min_length=<span class="cv">1</span>, max_length=<span class="cv">100000</span>)
    max_tokens:  int   = Field(default=<span class="cv">1024</span>, ge=<span class="cv">1</span>, le=<span class="cv">8192</span>)
    temperature: float = Field(default=<span class="cv">0.7</span>, ge=<span class="cv">0.0</span>, le=<span class="cv">2.0</span>)
    tags: List[str]    = Field(default_factory=list)
 
<span class="ck"># Custom validator</span>
class RegistrationForm(BaseModel):
    username: str
    email:    str
    age:      int
 
    @field_validator('email')
    @classmethod
    def email_must_contain_at(cls, v: str) -> str:
        if <span class="cs">'@'</span> not in v:
            raise ValueError(<span class="cs">'must be a valid email address'</span>)
        return v.lower()
 
    @field_validator('age')
    @classmethod
    def age_must_be_adult(cls, v: int) -> int:
        if v < <span class="cv">18</span>:
            raise ValueError(<span class="cs">'must be 18 or older'</span>)
        return v</pre></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🤖</span><h3>Pydantic for LLM Structured Outputs — Preview</h3><span class="tag tag-blue">Part 4 Preview</span></div>
  <div class="cp-body">
    <p>In Part 4 you will use Pydantic models to force LLMs to return structured JSON. Here is a preview of what that looks like with the Instructor library.</p>
    <div class="cb"><pre>from pydantic import BaseModel
from typing import List
import instructor, anthropic
 
<span class="ck"># Define the structure you want the LLM to return</span>
class InvoiceLineItem(BaseModel):
    description: str
    quantity:    int
    unit_price:  float
    total:       float
 
class Invoice(BaseModel):
    invoice_number: str
    customer_name:  str
    line_items:     List[InvoiceLineItem]
    subtotal:       float
    tax:            float
    total:          float
 
<span class="ck"># Instructor patches the client to enforce the schema</span>
client = instructor.from_anthropic(anthropic.Anthropic())
 
<span class="ck"># The LLM MUST return data matching the Invoice schema</span>
invoice = client.messages.create(
    model=<span class="cs">"claude-3-5-sonnet-20241022"</span>,
    max_tokens=<span class="cv">1024</span>,
    messages=[{
        <span class="cs">"role"</span>: <span class="cs">"user"</span>,
        <span class="cs">"content"</span>: <span class="cs">"Extract invoice data: INV-001, Alice Corp, 3×widgets $45, 1×service $100, tax 10%"</span>
    }],
    response_model=Invoice,   <span class="ck"># ← Pydantic model as schema</span>
)
print(invoice.total)   <span class="ck"># 214.5  — a proper float, not a string</span></pre></div>
    <div class="ins"><p>💡 <strong>This is why Pydantic matters for AI engineering.</strong> Without it, you get raw text back and must parse it manually — fragile and error-prone. With Pydantic + Instructor, you get a validated Python object with the exact structure you defined. This pattern is used in every serious AI application.</p></div>
  </div>
</div>
</div><!-- end t4 -->
<!-- ══════════ TAB 5 — FASTAPI + SQLITE ══════════ -->
<div id="t5" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Connecting FastAPI to SQLite</h3><span class="tag tag-purple">Full Stack</span></div>
  <div class="cp-body">
    <p>Connecting a database to your API is the final step before you have a complete backend. This is the pattern used in production AI apps for storing conversation history, user data, and ML metadata.</p>
    <div class="cb"><pre>from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import sqlite3
from contextlib import contextmanager
 
app = FastAPI(title=<span class="cs">"Student API"</span>)
 
<span class="ck"># Database connection context manager</span>
@contextmanager
def get_db():
    conn = sqlite3.connect(<span class="cs">"students.db"</span>)
    conn.row_factory = sqlite3.Row   <span class="ck"># access cols by name: row["name"]</span>
    try:
        yield conn
    finally:
        conn.close()
 
<span class="ck"># Create table on startup</span>
@app.on_event(<span class="cs">"startup"</span>)
def startup():
    with get_db() as conn:
        conn.execute(<span class="cs">"""
            CREATE TABLE IF NOT EXISTS students (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT    NOT NULL,
                score REAL    NOT NULL,
                grade TEXT
            )
        """</span>)
        conn.commit()
 
<span class="ck"># Pydantic models</span>
class StudentCreate(BaseModel):
    name:  str
    score: float
    grade: Optional[str] = None
 
class StudentResponse(BaseModel):
    id:    int
    name:  str
    score: float
    grade: Optional[str]
 
<span class="ck"># POST /students — create</span>
@app.post(<span class="cs">"/students"</span>, response_model=StudentResponse, status_code=<span class="cv">201</span>)
def create_student(student: StudentCreate):
    with get_db() as conn:
        cursor = conn.execute(
            <span class="cs">"INSERT INTO students (name, score, grade) VALUES (?, ?, ?)"</span>,
            (student.name, student.score, student.grade)
        )
        conn.commit()
        row = conn.execute(
            <span class="cs">"SELECT * FROM students WHERE id = ?"</span>, (cursor.lastrowid,)
        ).fetchone()
    return dict(row)
 
<span class="ck"># GET /students — list all</span>
@app.get(<span class="cs">"/students"</span>, response_model=List[StudentResponse])
def list_students(min_score: float = <span class="cv">0.0</span>):
    with get_db() as conn:
        rows = conn.execute(
            <span class="cs">"SELECT * FROM students WHERE score >= ? ORDER BY score DESC"</span>,
            (min_score,)
        ).fetchall()
    return [dict(row) for row in rows]
 
<span class="ck"># GET /students/{id} — get one</span>
@app.get(<span class="cs">"/students/{student_id}"</span>, response_model=StudentResponse)
def get_student(student_id: int):
    with get_db() as conn:
        row = conn.execute(
            <span class="cs">"SELECT * FROM students WHERE id = ?"</span>, (student_id,)
        ).fetchone()
    if not row:
        raise HTTPException(status_code=<span class="cv">404</span>, detail=<span class="cs">"Student not found"</span>)
    return dict(row)
 
<span class="ck"># DELETE /students/{id}</span>
@app.delete(<span class="cs">"/students/{student_id}"</span>, status_code=<span class="cv">204</span>)
def delete_student(student_id: int):
    with get_db() as conn:
        result = conn.execute(
            <span class="cs">"DELETE FROM students WHERE id = ?"</span>, (student_id,)
        )
        conn.commit()
    if result.rowcount == <span class="cv">0</span>:
        raise HTTPException(status_code=<span class="cv">404</span>, detail=<span class="cs">"Student not found"</span>)</pre></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🧪</span><h3>Testing Your API</h3><span class="tag tag-blue">Essential Skill</span></div>
  <div class="cp-body">
    <div class="cb"><pre><span class="ck"># Option 1 — FastAPI /docs (Swagger UI)</span>
<span class="ck"># Go to http://127.0.0.1:8000/docs in browser</span>
<span class="ck"># Click any endpoint → "Try it out" → fill fields → Execute</span>
<span class="ck"># Option 2 — curl from terminal</span>
<span class="ck"># Create a student</span>
curl -X POST http://localhost:8000/students   -H "Content-Type: application/json"   -d '{"name": "Alice", "score": 92.5, "grade": "A"}'
 
<span class="ck"># Get all students with score > 80</span>
curl "http://localhost:8000/students?min_score=80"
 
<span class="ck"># Get specific student</span>
curl http://localhost:8000/students/1
 
<span class="ck"># Option 3 — Python test client (best for automated tests)</span>
from fastapi.testclient import TestClient
from main import app   <span class="ck"># import your FastAPI app</span>
 
client = TestClient(app)
 
def test_create_student():
    response = client.post(<span class="cs">"/students"</span>,
        json={<span class="cs">"name"</span>: <span class="cs">"Alice"</span>, <span class="cs">"score"</span>: <span class="cv">92.5</span>})
    assert response.status_code == <span class="cv">201</span>
    assert response.json()[<span class="cs">"name"</span>] == <span class="cs">"Alice"</span>
 
def test_get_missing_student():
    response = client.get(<span class="cs">"/students/999"</span>)
    assert response.status_code == <span class="cv">404</span></pre></div>
  </div>
</div>
</div><!-- end t5 -->
<!-- ══════════ TAB 6 — WEEK PLAN ══════════ -->
<div id="t6" class="tab-pane">
<p class="sep">2-WEEK STRUCTURED PLAN</p>
<table class="wk-table">
  <thead><tr><th>Week</th><th>Topics</th><th>Daily Task / Mini-Project</th></tr></thead>
  <tbody>
    <tr>
      <td class="wk-num">Week 1<br><em>SQL</em></td>
      <td>Install SQLite (built into Python). CREATE TABLE, INSERT, SELECT with WHERE, ORDER BY, LIMIT. Aggregate functions: COUNT, AVG, MAX, MIN, SUM. GROUP BY and HAVING. INNER JOIN and LEFT JOIN. Subqueries and CTEs. UPDATE and DELETE. Parameterised queries — never SQL injection. pd.read_sql_query() to load results into DataFrames.</td>
      <td>Day 1–2: SQLBolt interactive exercises — complete all 18 lessons. Day 3: Build the students.db schema from scratch, insert 20 rows, write 5 query exercises. Day 4–5: Answer these from the DB: top 3 students per grade, class average per department, students above class average. Day 6–7: Load your COVID-19 CSV from M02 into SQLite and reproduce the top-10 query using SQL instead of Pandas groupby.</td>
    </tr>
    <tr>
      <td class="wk-num">Week 2<br><em>FastAPI</em></td>
      <td>Install FastAPI and uvicorn. First endpoint, /docs interface. Path parameters, query parameters, request bodies with Pydantic. HTTP status codes and HTTPException. Async endpoints. BackgroundTasks. Response models. Connecting SQLite to FastAPI — full CRUD. Testing with TestClient.</td>
      <td>Day 1–2: Build and run the minimal FastAPI app. Add health, version, and echo endpoints. Test via /docs. Day 3–4: Add Pydantic request and response models. Test validation — try sending wrong types and observe the 422 error. Day 5–7: Full milestone project — Student CRUD API with SQLite backend (see Projects tab).</td>
    </tr>
  </tbody>
</table>
</div><!-- end t6 -->
<!-- ══════════ TAB 7 — RESOURCES ══════════ -->
<div id="t7" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Interactive</td><td><a href="https://sqlbolt.com/" target="_blank" rel="noopener">SQLBolt — sqlbolt.com — 20 short SQL lessons with in-browser exercises</a></td><td>Fastest way to learn SQL from scratch. Complete all lessons in Day 1.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://fastapi.tiangolo.com/tutorial/" target="_blank" rel="noopener">FastAPI Official Tutorial — fastapi.tiangolo.com/tutorial/</a></td><td>One of the best framework docs ever written. Work through start to finish.</td></tr>
    <tr><td class="res-type">Course</td><td><a href="https://www.kaggle.com/learn/intro-to-sql" target="_blank" rel="noopener">Kaggle Intro to SQL (Free) — kaggle.com/learn/intro-to-sql</a></td><td>SQL with real BigQuery datasets. Hands-on with immediate feedback.</td></tr>
    <tr><td class="res-type">Video</td><td><a href="https://www.youtube.com/watch?v=7t2alSnE2-I" target="_blank" rel="noopener">FastAPI Full Tutorial — Sebastián Ramírez (YouTube)</a></td><td>FastAPI from the creator. Comprehensive walkthrough of all features.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://docs.pydantic.dev/latest/" target="_blank" rel="noopener">Pydantic v2 Documentation — docs.pydantic.dev</a></td><td>Complete reference for validation, field constraints, and custom validators.</td></tr>
  </tbody>
</table>
</div><!-- end t7 -->
<!-- ══════════ TAB 8 — PROJECTS ══════════ -->
<div id="t8" class="tab-pane">
<p class="sep">MILESTONE PROJECT</p>
<div class="proj-box">
  <div class="proj-hdr">
    <span>🛠</span>
    <span class="proj-title">Student CRUD API — FastAPI + SQLite</span>
    <span class="proj-dur">[Intermediate] 3–4 days · Week 2</span>
  </div>
  <div class="proj-body">
    <p>Build a complete REST API for managing student data — your first real backend application. This is the template pattern for every AI API you will build in Parts 4–7.</p>
    <h4>Requirements</h4>
    <ul>
      <li><strong>POST /students</strong> — create a student (name, score, grade, email). Validate: score 0–100, email format, name min 2 chars.</li>
      <li><strong>GET /students</strong> — list all students. Query params: min_score, max_score, grade filter, limit (max 100), offset (for pagination).</li>
      <li><strong>GET /students/{id}</strong> — get one student by ID. Return 404 if not found.</li>
      <li><strong>PUT /students/{id}</strong> — update a student. Partial update — only fields provided are updated.</li>
      <li><strong>DELETE /students/{id}</strong> — delete a student. Return 404 if not found.</li>
      <li><strong>GET /students/stats</strong> — return: total count, class average, grade distribution (A/B/C/D/F count), top student.</li>
      <li>All endpoints have Pydantic request and response models</li>
      <li>SQLite database persists between server restarts</li>
      <li>Test all endpoints via /docs interface</li>
    </ul>
    <h4>Stretch Goals</h4>
    <ul>
      <li>Add a <strong>GET /students/export</strong> endpoint that returns a downloadable CSV of all students</li>
      <li>Add a <strong>POST /students/bulk</strong> endpoint that accepts a list of students and inserts them in one transaction</li>
      <li>Write pytest tests for all 6 endpoints using FastAPI TestClient</li>
      <li>Add a <code>created_at</code> timestamp to each student record</li>
    </ul>
    <p><strong>Skills:</strong> FastAPI, Pydantic, SQLite, CRUD operations, HTTP status codes, query parameters, pagination, error handling</p>
  </div>
</div>
<p class="sep">MINI-PROJECTS</p>
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">SQL Analytics on COVID Data</span><span class="proj-dur">1–2 days · Week 1</span></div>
  <div class="proj-body">
    <p>Load your M02 COVID-19 CSV into SQLite using <code>df.to_sql()</code>. Then reproduce all 5 analyses from M02 (top 10 by deaths, rolling average, monthly groupby) using pure SQL queries instead of Pandas. Compare the SQL and Pandas approaches — when is each cleaner?</p>
  </div>
</div>
</div><!-- end t8 -->
<!-- ══════════ TAB 9 — LABS ══════════ -->
<div id="t9" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>SQL — Write 10 Queries Against a Real Dataset</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Develop SQL fluency by writing non-trivial queries against a real dataset — not toy examples.</p>
    <div class="lab-step"><div class="sn">1</div><div>Download the Titanic CSV and load it into SQLite: <code>import pandas as pd, sqlite3; df = pd.read_csv("titanic.csv"); conn = sqlite3.connect("titanic.db"); df.to_sql("passengers", conn, if_exists="replace", index=False)</code></div></div>
    <div class="lab-step"><div class="sn">2</div><div>Write and run these queries using Python sqlite3: (1) Total passengers and survival rate. (2) Survival rate by Sex. (3) Survival rate by Pclass. (4) Average fare by Pclass. (5) Top 5 passengers by fare paid.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Write these harder queries: (6) Passengers whose fare was above the average fare for their class (correlated subquery). (7) Count of survivors per Embarked port. (8) The youngest and oldest survivor in each Pclass. (9) Passengers who traveled alone (SibSp=0 AND Parch=0) — their survival rate. (10) Use a CTE to find the survival rate for each cabin letter prefix.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>For each query, also write the equivalent Pandas code. Compare line count and readability. Note which problems feel more natural in SQL vs Pandas.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>FastAPI — Build and Stress-Test an Endpoint</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build a real FastAPI endpoint from scratch, test every failure mode, and observe how FastAPI handles errors.</p>
    <div class="lab-step"><div class="sn">1</div><div>Create a new FastAPI app with a single <code>POST /analyse</code> endpoint. It accepts: <code>{"text": "...", "max_words": 100}</code> and returns: <code>{"word_count": N, "unique_words": N, "most_common": [...]}</code></div></div>
    <div class="lab-step"><div class="sn">2</div><div>Add Pydantic validation: text must be non-empty string, max_words must be between 10 and 1000. Run the server and test via /docs.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Now test every failure mode via /docs or curl: (a) Missing required field. (b) Wrong type for max_words (send a string). (c) max_words = 0 (violates constraint). (d) Empty text string. Note the exact error structure FastAPI returns for each.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Add a <code>GET /analyse/history</code> endpoint that returns the last 10 requests processed (store them in an in-memory list). This tests that you understand how FastAPI handles state between requests.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Write 4 TestClient tests: happy path, missing field, invalid type, and constraint violation. Run with <code>python -m pytest test_api.py -v</code>.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Full Stack — FastAPI + SQLite Todo API</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build the classic Todo API in 60 minutes — internalising the full CRUD + database pattern that every AI backend uses.</p>
    <div class="lab-step"><div class="sn">1</div><div>Create a <code>Todo</code> Pydantic model with: id (int), title (str, min 3 chars), completed (bool, default False), created_at (str). Create a corresponding SQLite table on startup.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Implement: <code>POST /todos</code> (create), <code>GET /todos</code> (list, filter by completed=true/false), <code>GET /todos/{id}</code> (get one), <code>PATCH /todos/{id}/complete</code> (mark done), <code>DELETE /todos/{id}</code> (delete).</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Test the entire flow via /docs: create 5 todos, complete 2, list all, list only incomplete, delete one, get a non-existent todo (expect 404).</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Add a <code>GET /todos/stats</code> endpoint returning: total, completed count, pending count, completion percentage. Use a single SQL query with conditional aggregation: <code>SELECT COUNT(*), SUM(CASE WHEN completed=1 THEN 1 ELSE 0 END) FROM todos</code></div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Bonus:</strong> Push this to GitHub. In your README, add a curl one-liner for each endpoint so anyone can test your API without reading the code.</div></div>
  </div>
</div>
</div><!-- end t9 -->
<!-- ══════════ TAB 10 — CHECKLIST ══════════ -->
<div id="t10" class="tab-pane">
<p class="sep">P1-M04 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can write SELECT queries with WHERE, ORDER BY, LIMIT and explain each clause's purpose</li>
  <li>Know the difference between WHERE and HAVING — and when each is used</li>
  <li>Can use all five aggregate functions: COUNT, SUM, AVG, MIN, MAX</li>
  <li>Can write an INNER JOIN and a LEFT JOIN and explain when each is appropriate</li>
  <li>Can write a CTE and explain why it is preferable to a nested subquery</li>
  <li>Always use parameterised queries — never string interpolation for SQL</li>
  <li>Can load a SQL query result directly into a Pandas DataFrame with pd.read_sql_query()</li>
  <li>Can create a FastAPI app with GET and POST endpoints and run it with uvicorn</li>
  <li>Know the difference between path parameters, query parameters, and request bodies</li>
  <li>Can define a Pydantic BaseModel with field constraints and a custom validator</li>
  <li>Know what happens when a request fails Pydantic validation — what status code, what error body</li>
  <li>Can raise an HTTPException with the correct status code and detail message</li>
  <li>Can connect a SQLite database to FastAPI and implement full CRUD (Create, Read, Update, Delete)</li>
  <li>Can test all endpoints via the /docs Swagger UI without writing a client</li>
  <li>Can write a FastAPI TestClient test for a happy path and an error case</li>
  <li>Completed Lab 1: 10 SQL queries against Titanic dataset</li>
  <li>Completed Lab 2: FastAPI endpoint with full validation testing</li>
  <li>Completed Lab 3: Full CRUD Todo API with SQLite</li>
  <li>Milestone project pushed to GitHub with README, requirements.txt, .gitignore</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>Part 1 Complete!</strong> You now have all the foundation skills needed to build AI systems. Move to <strong>Part 4 — LLM API Mastery</strong> if you are on the AI/GenAI Engineer path, or <strong>Part 2 — Statistics &amp; EDA</strong> if you are following the Data Scientist/ML Engineer path.</p>
</div>
</div><!-- end t10 -->
<!-- ── PART 1 COMPLETION BANNER ── -->
<div class="milestone-banner">
  <h3>🎉 Part 1 — Universal Foundation Complete!</h3>
  <p>You have completed all 4 modules of the foundation. Here is what you can now do:</p>
  <div class="milestone-grid">
    <div class="mg-item">Write Python programs that read/write files, call APIs, and handle errors</div>
    <div class="mg-item">Version code with Git and push projects to GitHub</div>
    <div class="mg-item">Navigate the terminal and manage environment variables</div>
    <div class="mg-item">Make async HTTP requests and parse JSON responses</div>
    <div class="mg-item">Manipulate data with NumPy vectorised operations</div>
    <div class="mg-item">Load, clean, and aggregate data with Pandas</div>
    <div class="mg-item">Query databases with SQL — joins, aggregations, CTEs</div>
    <div class="mg-item">Build and run a FastAPI server with Pydantic validation</div>
  </div>
</div>
<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/ai-ml/part1-foundation/p1-m03-dev-essentials/">← P1-M03: Dev Essentials</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part4-llm-apis/p4-m11-prompting/">Next: P4-M11 — Prompting →</a>
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
    const key = 'p1m04-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
