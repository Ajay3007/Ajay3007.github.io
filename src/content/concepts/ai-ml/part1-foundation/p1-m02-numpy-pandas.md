---
title: "P1-M02 - NumPy & Pandas Data Toolkit"
description: "Part 1 — Universal Foundation · Module 02 of 04 NumPy Pandas Data Toolkit Vectorised computing and data wrangling — the backbone of all ML work ⏱ 3 Weeks 🟡…"
domain: ai-ml
track: ai-ml-engineering
module: part1-foundation
order: 102
ownHeader: true
url: /learning/ai-ml/part1-foundation/p1-m02-numpy-pandas/
---

<style>
/* ── Base ─────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#0f0a1e 0%,#1a0a3a 45%,#4c1d95 80%,#7c3aed 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0;
}
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
.p-blue  .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue  .cp-hdr{background:#0d2030}
.p-teal  .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal  .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.p-green  .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green  .cp-hdr{background:#0a2018}
.p-red    .cp-hdr{background:#faeaea}[data-theme=dark] .p-red    .cp-hdr{background:#2a0808}
.p-amber  .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber  .cp-hdr{background:#2a1e00}
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
/* Comparison table */
.cmp-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.84rem}
.cmp-table th{background:#1a0a3a;color:#ddd6fe;padding:.6rem .9rem;text-align:left;font-weight:700;font-size:.75rem}
.cmp-table td{padding:.6rem .9rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top;line-height:1.55}
.cmp-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.cmp-table .good{color:#15803d;font-weight:600}
.cmp-table .bad{color:#dc2626;font-weight:600}
</style>
<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 1 — Universal Foundation &nbsp;·&nbsp; Module 02 of 04</div>
  <div class="mod-title">NumPy &amp; Pandas Data Toolkit</div>
  <div class="mod-subtitle">Vectorised computing and data wrangling — the backbone of all ML work</div>
  <div class="mod-pills">
<span class="mod-pill">⏱ 3 Weeks</span>
<span class="mod-pill">🟡 Beginner–Intermediate</span>
<span class="mod-pill">🔢 NumPy · Pandas</span>
<span class="mod-pill">📋 Prerequisite: P1-M01</span>
<span class="mod-pill">🛠 Jupyter / Colab</span>
  </div>
</div>
<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🔢 NumPy</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🐼 Pandas</button>
  <button class="tab-btn" onclick="vt(event,'t3')">⚡ Power Patterns</button>
  <button class="tab-btn" onclick="vt(event,'t4')">📅 Week Plan</button>
  <button class="tab-btn" onclick="vt(event,'t5')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t6')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t7')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">✅ Checklist</button>
</div>
<!-- ══════════ TAB 0 — OVERVIEW ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-purple">Foundation</span></div>
  <div class="cp-body">
<p>NumPy and Pandas are the two libraries you will use in literally every AI/ML project. NumPy provides fast vectorised numerical computing — the engine under PyTorch, Scikit-learn, and NumPy arrays. Pandas provides the DataFrame — the universal data table for loading, cleaning, and transforming real-world data.</p>
<ul>
<li><strong>NumPy</strong> — ndarray creation, indexing, slicing, broadcasting, vectorised operations, statistical functions</li>
<li><strong>Pandas Series</strong> — one-dimensional labelled array, the column of a DataFrame</li>
<li><strong>Pandas DataFrame</strong> — the core data structure: reading CSVs, inspecting data, indexing with .loc/.iloc</li>
<li><strong>Data cleaning</strong> — handling NaN values, removing duplicates, type conversion</li>
<li><strong>Data manipulation</strong> — filtering, sorting, groupby, aggregation, merge/join, pivot tables</li>
<li><strong>String operations</strong> — .str accessor for text data cleaning</li>
<li><strong>Datetime handling</strong> — pd.to_datetime(), .dt accessor, time-series operations</li>
</ul>
  </div>
</div>
<div class="skip-box">
  <strong>⚡ SKIP IF:</strong> You know Java/C++ arrays and ArrayLists — NumPy arrays are conceptually similar but with vectorised operations (no explicit loops needed). Pandas DataFrame is like a database table or Excel spreadsheet. Skim NumPy basics and focus on Pandas, which is uniquely Python/data-focused with no direct equivalent in compiled languages.
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Why These Two Libraries</h3><span class="tag tag-blue">Context</span></div>
  <div class="cp-body">
<table class="cmp-table">
<thead><tr><th>Library</th><th>What it does</th><th>Used in</th></tr></thead>
<tbody>
<tr><td><strong>NumPy</strong></td><td>N-dimensional arrays, vectorised math, linear algebra. C-backed — 10–100× faster than Python loops.</td><td>Scikit-learn internals, PyTorch tensors, image processing, embedding vectors</td></tr>
<tr><td><strong>Pandas</strong></td><td>DataFrame for tabular data. Read CSVs, clean messy data, group/aggregate, merge datasets.</td><td>Every ML project for data loading and EDA. Feature engineering pipeline.</td></tr>
</tbody>
</table>
<div class="ins"><p>💡 <strong>NumPy array vs Python list:</strong> A Python list can hold mixed types and is stored as pointers to objects. A NumPy array holds a single type in contiguous memory — like a C array. This is why <code>np.sum(arr)</code> is 50× faster than <code>sum(list)</code> for large data.</p></div>
  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Module Connections</h3><span class="tag tag-green">Dependencies</span></div>
  <div class="cp-body">
<ul>
<li><strong>P1-M03 (Dev Essentials)</strong> — JSON/API responses are converted to DataFrames constantly</li>
<li><strong>P2 (Stats &amp; EDA)</strong> — all statistical analysis uses Pandas + NumPy directly</li>
<li><strong>P3 (Classical ML)</strong> — Scikit-learn expects NumPy arrays as input (X, y)</li>
<li><strong>P5 (RAG)</strong> — document metadata stored as DataFrames before ingestion into vector DBs</li>
<li><strong>P7 (Production)</strong> — log analysis and monitoring data processed with Pandas</li>
</ul>
  </div>
</div>
</div><!-- end t0 -->
<!-- ══════════ TAB 1 — NUMPY ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔢</span><h3>NumPy Array Fundamentals</h3><span class="tag tag-purple">Week 1</span></div>
  <div class="cp-body">
    

```python
import numpy as np

# Creating arrays
a = np.array([1, 2, 3, 4, 5])              # from Python list
b = np.zeros((3, 4))                      # 3×4 matrix of zeros
c = np.ones((2, 3), dtype=np.float32)     # with dtype
d = np.arange(0, 10, 2)                   # [0, 2, 4, 6, 8]
e = np.linspace(0, 1, 5)                  # [0, 0.25, 0.5, 0.75, 1.0]
f = np.random.randn(3, 3)                # 3×3 standard normal

# Key attributes
print(a.shape)    # (5,)     — 1D with 5 elements
print(b.shape)    # (3, 4)   — 2D: 3 rows, 4 cols
print(b.dtype)    # float64  — default numeric type
print(b.ndim)     # 2        — number of dimensions
print(b.size)     # 12       — total elements
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">✂️</span><h3>Indexing, Slicing and Boolean Masking</h3><span class="tag tag-blue">Essential</span></div>
  <div class="cp-body">
    

```python
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Indexing — [row, col]
print(arr[0, 1])       # 2  — row 0, col 1
print(arr[-1, -1])     # 9  — last row, last col

# Slicing — [row_start:row_end, col_start:col_end]
print(arr[0:2, 1:])    # [[2,3],[5,6]]  — rows 0-1, cols 1+
print(arr[:, 0])        # [1, 4, 7]  — entire first column
print(arr[1, :])         # [4, 5, 6]  — entire second row

# Boolean masking — critical for data filtering
scores = np.array([55, 72, 88, 43, 95, 61])
mask   = scores > 70
print(mask)             # [F, T, T, F, T, F]
print(scores[mask])     # [72, 88, 95]  — fancy indexing
print(scores[scores > 70])  # same — inline

# Combine conditions
print(scores[(scores > 60) & (scores < 90)])  # [72, 88, 61]
```


<div class="warn"><p>⚠️ <strong>NumPy slices are VIEWS, not copies.</strong> Modifying a slice modifies the original array. Always use <code>arr.copy()</code> when you need an independent copy. This is the single most common NumPy bug.</p></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Vectorised Operations and Broadcasting</h3><span class="tag tag-teal">Performance</span></div>
  <div class="cp-body">
<p>Vectorised operations apply element-wise without Python loops — this is where NumPy's speed comes from.</p>
    

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# Element-wise — no loops needed
print(a + b)          # [11, 22, 33, 44]
print(a * b)          # [10, 40, 90, 160]
print(a ** 2)         # [1, 4, 9, 16]
print(np.sqrt(a))     # [1.0, 1.41, 1.73, 2.0]

# Statistical functions
print(np.mean(a))     # 2.5
print(np.std(a))      # 1.118...
print(np.sum(a))      # 10
print(np.min(a), np.max(a), np.argmax(a))  # 1  4  3

# Broadcasting — smaller array stretches to match larger
matrix = np.ones((3, 4))
row    = np.array([1, 2, 3, 4])    # shape (4,)
result = matrix + row               # row broadcast across 3 rows
print(result)
# [[2,3,4,5],
#  [2,3,4,5],
#  [2,3,4,5]]
```


  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">📐</span><h3>Reshape, Stack and Linear Algebra</h3><span class="tag tag-orange">ML Prep</span></div>
  <div class="cp-body">
    

```python
# Reshape — change shape without changing data
a = np.arange(12)
print(a.reshape(3, 4))    # 3 rows, 4 cols
print(a.reshape(2, -1))    # -1 = infer (becomes 2×6)
print(a.flatten())           # back to 1D

# Transpose — swap rows and cols
m = np.array([[1,2,3],[4,5,6]])
print(m.T)    # shape (2,3) → (3,2)

# Stacking arrays
x = np.array([1,2,3])
y = np.array([4,5,6])
print(np.vstack([x, y]))    # [[1,2,3],[4,5,6]]  vertical
print(np.hstack([x, y]))    # [1,2,3,4,5,6]  horizontal

# Matrix multiplication — critical for ML
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(A @ B)          # matrix multiply: [[19,22],[43,50]]
print(np.dot(A, B))   # equivalent
print(A * B)          # element-wise (NOT matrix multiply)
```


<div class="ins"><p>💡 <strong>Remember:</strong> <code>@</code> is matrix multiplication (dot product). <code>*</code> is element-wise. This distinction is critical — using the wrong one in ML code produces silently wrong results.</p></div>
  </div>
</div>
</div><!-- end t1 -->
<!-- ══════════ TAB 2 — PANDAS ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Series and DataFrame Basics</h3><span class="tag tag-purple">Week 2</span></div>
  <div class="cp-body">
    

```python
import pandas as pd
import numpy as np

# Series — 1D labelled array (a single column)
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s["b"])    # 20
print(s.dtype)   # int64

# DataFrame — 2D table (rows × columns)
df = pd.DataFrame({
    "name":  ["Alice", "Bob", "Charlie"],
    "score": [85, 92, 78],
    "grade": ["B", "A", "C"]
})

# Loading from files
df = pd.read_csv("students.csv")
df = pd.read_json("data.json")
df = pd.read_excel("report.xlsx")

# First look at a dataset
print(df.head(5))      # first 5 rows
print(df.tail(3))      # last 3 rows
print(df.shape)         # (rows, cols)
print(df.dtypes)        # column types
print(df.info())        # types + non-null counts
print(df.describe())    # count, mean, std, min, quartiles, max
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>Indexing — .loc vs .iloc</h3><span class="tag tag-blue">Essential</span></div>
  <div class="cp-body">
    

```bash
# .loc — label-based indexing (use column names, index labels)
df.loc[0]                       # row with index label 0
df.loc[0, "name"]               # cell: row 0, column "name"
df.loc[0:2, ["name","score"]]   # rows 0-2, two columns (INCLUSIVE)

# .iloc — position-based indexing (like NumPy)
df.iloc[0]            # first row
df.iloc[0, 1]         # row 0, column 1 (exclusive end)
df.iloc[0:3, :2]      # first 3 rows, first 2 cols
df.iloc[-1]           # last row

# Boolean filtering — the most common pattern
high_scores = df[df["score"] > 80]
top_students = df[(df["score"] > 80) & (df["grade"] == "A")]

# Selecting columns
df["name"]             # returns Series
df[["name", "score"]]  # returns DataFrame with 2 cols
```


<div class="warn"><p>⚠️ <strong>.loc endpoint is INCLUSIVE, .iloc endpoint is EXCLUSIVE.</strong> <code>df.loc[0:3]</code> returns rows 0,1,2,3. <code>df.iloc[0:3]</code> returns rows 0,1,2. This trips up everyone coming from Python slicing.</p></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🧹</span><h3>Data Cleaning — The Real Work</h3><span class="tag tag-teal">Week 2–3</span></div>
  <div class="cp-body">
<p>Real-world data is always messy. Expect 60–70% of your time on any ML project to be data cleaning. Pandas has excellent tools for it.</p>
    

```python
# Detecting and handling NaN (missing values)
print(df.isnull().sum())          # count NaN per column
print(df.isnull().sum() / len(df))  # percentage missing

df.dropna()                       # drop rows with ANY NaN
df.dropna(subset=["score"])       # drop only if score is NaN
df.dropna(thresh=3)              # keep rows with at least 3 non-NaN
df.fillna(0)                     # fill all NaN with 0
df["score"].fillna(df["score"].mean())  # fill with column mean
df["score"].ffill()              # forward fill (time series)

# Duplicates
df.duplicated().sum()             # count duplicate rows
df.drop_duplicates()              # remove all duplicates
df.drop_duplicates(subset=["name"])  # based on specific cols

# Type conversion
df["score"] = df["score"].astype(float)
df["date"]  = pd.to_datetime(df["date"])
df["grade"] = df["grade"].astype("category")  # saves memory

# String cleaning
df["name"] = df["name"].str.strip().str.lower()
df["email"] = df["email"].str.contains("@")  # returns bool Series
```


<div class="ins"><p>💡 <strong>Always use .copy() when creating a subset DataFrame.</strong> <code>df_clean = df[df["score"] > 0].copy()</code> — without .copy() you get a SettingWithCopyWarning and changes to df_clean may or may not affect the original. This is Pandas' most confusing behaviour.</p></div>
  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>GroupBy — Split, Apply, Combine</h3><span class="tag tag-orange">Week 3</span></div>
  <div class="cp-body">
    

```bash
# groupby() — the most powerful Pandas operation
# Pattern: split data into groups → apply function → combine results

df = pd.DataFrame({
    "city":  ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai"],
    "sales": [100, 200, 150, 180, 120],
    "month": ["Jan", "Jan", "Feb", "Feb", "Mar"]
})

# Basic aggregations
df.groupby("city")["sales"].mean()     # mean sales per city
df.groupby("city")["sales"].sum()      # total sales per city
df.groupby("city")["sales"].count()    # number of records per city

# Multiple aggregations at once
df.groupby("city").agg({
    "sales": ["sum", "mean", "count"]
})

# Group by multiple columns
df.groupby(["city", "month"])["sales"].sum()

# transform — adds group stat back to original rows
df["city_avg"] = df.groupby("city")["sales"].transform("mean")
df["pct_of_city"] = df["sales"] / df["city_avg"]
```


  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔀</span><h3>Merge, Join and Concat</h3><span class="tag tag-green">Week 3</span></div>
  <div class="cp-body">
    

```bash
# merge — SQL-style join on a key column
users  = pd.DataFrame({"id": [1,2,3], "name": ["Alice","Bob","Charlie"]})
orders = pd.DataFrame({"user_id": [1,1,2], "amount": [50,75,30]})

pd.merge(orders, users, left_on="user_id", right_on="id", how="left")
# how: "inner"(default), "left", "right", "outer"

# concat — stack DataFrames vertically or horizontally
train = pd.read_csv("train.csv")
test  = pd.read_csv("test.csv")
full  = pd.concat([train, test], ignore_index=True)   # vertical stack

# pivot_table — Excel-style pivot
pivot = df.pivot_table(
    values="sales",
    index="city",
    columns="month",
    aggfunc="sum",
    fill_value=0
)
```


  </div>
</div>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">📅</span><h3>Datetime Handling</h3><span class="tag tag-amber">Time Series</span></div>
  <div class="cp-body">
    

```bash
# Parse dates on read
df = pd.read_csv("data.csv", parse_dates=["date"])

# Convert string column to datetime
df["date"] = pd.to_datetime(df["date"])

# .dt accessor — extract components
df["year"]    = df["date"].dt.year
df["month"]   = df["date"].dt.month
df["weekday"] = df["date"].dt.day_name()    # "Monday", "Tuesday"...
df["quarter"] = df["date"].dt.quarter

# Rolling window — used for moving averages (COVID 7-day rolling avg)
df["rolling_7"] = df["cases"].rolling(window=7).mean()

# Resample — aggregate by time period
df.set_index("date").resample("M")["sales"].sum()  # monthly totals
```


  </div>
</div>
</div><!-- end t2 -->
<!-- ══════════ TAB 3 — POWER PATTERNS ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>The Pandas Power Patterns — Memorise These</h3><span class="tag tag-purple">Must Know</span></div>
  <div class="cp-body">
<p>These patterns appear in virtually every data science and ML project. Learn them until they are automatic.</p>
    

```bash
# 1. Boolean masking — most common filtering pattern
df[df["age"] > 30]
df[(df["age"] > 30) & (df["city"] == "Mumbai")]
df[df["name"].isin(["Alice", "Bob"])]
df[~df["score"].isna()]   # ~ inverts boolean

# 2. Chain operations — readable pipeline
result = (df
    .dropna(subset=["score"])
    .query("score > 60")
    .groupby("city")["sales"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# 3. apply() with lambda — transform column values
df["score_normalised"] = df["score"].apply(lambda x: (x - 50) / 50)
df["grade"] = df["score"].apply(lambda x: "A" if x>=90 else "B" if x>=80 else "C")

# 4. Always .copy() on subsets
df_clean = df[df["score"] > 0].copy()

# 5. pd.get_dummies — one-hot encoding (used in every ML project)
df_encoded = pd.get_dummies(df, columns=["city", "grade"])

# 6. value_counts — quick frequency distribution
df["city"].value_counts()
df["city"].value_counts(normalize=True)  # proportions

# 7. nunique — number of unique values per column
df.nunique()   # quick cardinality check before one-hot encoding
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>NumPy ↔ Pandas Interoperability</h3><span class="tag tag-blue">Integration</span></div>
  <div class="cp-body">
    

```python
# DataFrame → NumPy array (for Scikit-learn, PyTorch)
X = df[["age", "score", "income"]].values   # .values returns ndarray
y = df["target"].to_numpy()                   # explicit and preferred
print(X.shape)   # (n_samples, n_features)

# NumPy array → DataFrame
arr = np.random.randn(100, 3)
df2 = pd.DataFrame(arr, columns=["x1", "x2", "x3"])

# Apply NumPy functions to Pandas columns
df["log_income"] = np.log(df["income"] + 1)  # log transform
df["z_score"]   = (df["score"] - df["score"].mean()) / df["score"].std()

# The full ML data prep pipeline
# 1. Load with pd.read_csv
# 2. Clean with Pandas (drop NaN, fix types, remove duplicates)
# 3. Engineer features with Pandas + NumPy
# 4. Encode categoricals with pd.get_dummies or LabelEncoder
# 5. Convert to NumPy with .values or to_numpy()
# 6. Pass to Scikit-learn / PyTorch
```


  </div>
</div>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">🐌</span><h3>Performance — When Pandas Gets Slow</h3><span class="tag tag-amber">Production</span></div>
  <div class="cp-body">
<ul>
<li><strong>Never iterate with for loops</strong> over DataFrame rows — use vectorised operations, .apply(), or .map()</li>
<li><strong>Use categorical dtype</strong> for string columns with low cardinality (e.g. city, grade) — cuts memory 10×</li>
<li><strong>Read large CSVs in chunks</strong> — <code>pd.read_csv(..., chunksize=10000)</code> for files that don't fit in RAM</li>
<li><strong>Use .query() for complex filters</strong> — often faster than boolean indexing on large DataFrames</li>
<li><strong>Avoid object dtype</strong> — mixed types in a column cause it to use object dtype (slow). Always fix types on load.</li>
</ul>
    

```python
# Slow — Python loop over rows (never do this)
for i, row in df.iterrows():
    df.at[i, "new_col"] = row["score"] * 2

# Fast — vectorised (1000× faster)
df["new_col"] = df["score"] * 2

# Check memory usage
df.memory_usage(deep=True).sum() / 1024**2   # MB
```


  </div>
</div>
</div><!-- end t3 -->
<!-- ══════════ TAB 4 — WEEK PLAN ══════════ -->
<div id="t4" class="tab-pane">
<p class="sep">3-WEEK STRUCTURED PLAN</p>
<table class="wk-table">
  <thead><tr><th>Week</th><th>Topics</th><th>Daily Task / Mini-Project</th></tr></thead>
  <tbody>
<tr>
<td class="wk-num">Week 1<br><em>NumPy</em></td>
<td>Install NumPy. ndarray creation: np.array, np.zeros, np.ones, np.arange, np.linspace, np.random. Array indexing, slicing (2D), boolean masking. Vectorised arithmetic — why no loops needed. Broadcasting rules. NumPy math: mean, std, sum, dot, reshape, transpose.</td>
<td>Day 1–2: Compute statistics on a random student score array without any Python loops. Day 3–4: Implement matrix multiplication using np.dot — verify against manual calculation. Day 5–7: Reshape a 1D sensor data array into a 2D time-series matrix and extract windows.</td>
</tr>
<tr>
<td class="wk-num">Week 2<br><em>Pandas Basics</em></td>
<td>Pandas Series vs DataFrame. pd.read_csv(), .head(), .info(), .describe(), .shape. Indexing: .loc[], .iloc[], boolean filtering. Handling NaN: .isnull(), .dropna(), .fillna(). Removing duplicates. Type conversion with .astype() and pd.to_datetime().</td>
<td>Day 1–2: Load the COVID-19 dataset — write a 10-line "data health report" (shape, dtypes, null counts, value ranges). Day 3–4: Find and handle all missing values — document your strategy (drop vs fill) with justification. Day 5–7: Filter a real DataFrame matching multiple conditions — export result to new CSV.</td>
</tr>
<tr>
<td class="wk-num">Week 3<br><em>Pandas Advanced</em></td>
<td>groupby() — split-apply-combine pattern. .agg(), .transform(). Merging DataFrames: merge(), join(), concat(). Pivot tables: pd.pivot_table(). String operations: .str.lower(), .str.contains(), .str.replace(). Datetime: pd.to_datetime(), .dt.year, .dt.month. Rolling windows.</td>
<td>Day 1–2: Find top 5 countries by total COVID cases using groupby + sort. Day 3–4: Merge two datasets on a common key — verify row counts before and after. Day 5–7: Full milestone project — COVID-19 Global Data Analysis (see Projects tab).</td>
</tr>
  </tbody>
</table>
</div><!-- end t4 -->
<!-- ══════════ TAB 5 — RESOURCES ══════════ -->
<div id="t5" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
<tr><td class="res-type">Course</td><td><a href="https://www.kaggle.com/learn/pandas" target="_blank" rel="noopener">Kaggle Pandas Course (Free, Interactive)</a></td><td>Best hands-on Pandas. Exercises with instant feedback. Complete in Week 2.</td></tr>
<tr><td class="res-type">Video</td><td><a href="https://www.youtube.com/watch?v=QUT1VHiLmmI" target="_blank" rel="noopener">NumPy for Beginners — freeCodeCamp (YouTube)</a></td><td>Complete NumPy from scratch. Watch at start of Week 1.</td></tr>
<tr><td class="res-type">Docs</td><td><a href="https://pandas.pydata.org/docs/user_guide/index.html" target="_blank" rel="noopener">Pandas Official Documentation — User Guide</a></td><td>Authoritative reference. "10 Minutes to Pandas" is a must-read in Week 2.</td></tr>
<tr><td class="res-type">Video</td><td><a href="https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS" target="_blank" rel="noopener">Corey Schafer — Pandas Tutorials (YouTube Playlist)</a></td><td>Deep Pandas tutorials. Best for groupby and merge concepts.</td></tr>
<tr><td class="res-type">Course</td><td><a href="https://www.kaggle.com/learn/intro-to-programming" target="_blank" rel="noopener">Kaggle NumPy Course (Free)</a></td><td>NumPy fundamentals with practice exercises.</td></tr>
<tr><td class="res-type">Cheatsheet</td><td><a href="https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python" target="_blank" rel="noopener">Pandas Cheat Sheet — DataCamp (Free PDF)</a></td><td>Quick reference. Print and keep beside you during Week 2–3.</td></tr>
  </tbody>
</table>
<p class="sep">FREE DATASETS FOR PRACTICE</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Dataset</th><th>Practice Focus</th></tr></thead>
  <tbody>
<tr><td class="res-type">Dataset</td><td><a href="https://www.kaggle.com/datasets/josephassaker/covid19-global-dataset" target="_blank" rel="noopener">COVID-19 Global Dataset — Kaggle</a></td><td>Time-series, rolling averages, groupby, datetime handling — Milestone project</td></tr>
<tr><td class="res-type">Dataset</td><td><a href="https://www.kaggle.com/c/titanic/data" target="_blank" rel="noopener">Titanic Dataset — Kaggle (Classic)</a></td><td>Missing values, groupby, boolean filtering practice</td></tr>
<tr><td class="res-type">Dataset</td><td><a href="https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset" target="_blank" rel="noopener">World Population Dataset — Kaggle</a></td><td>Merging, pivoting, multi-column groupby</td></tr>
<tr><td class="res-type">Dataset</td><td><a href="https://www.kaggle.com/datasets/shivamb/netflix-shows" target="_blank" rel="noopener">Netflix Shows Dataset — Kaggle</a></td><td>String operations, datetime handling, value_counts</td></tr>
  </tbody>
</table>
</div><!-- end t5 -->
<!-- ══════════ TAB 6 — PROJECTS ══════════ -->
<div id="t6" class="tab-pane">
<p class="sep">MILESTONE PROJECT</p>
<div class="proj-box">
  <div class="proj-hdr">
<span>🛠</span>
<span class="proj-title">COVID-19 Global Data Analysis</span>
<span class="proj-dur">[Beginner] 4–5 days · Week 3</span>
  </div>
  <div class="proj-body">
<p>Use the COVID-19 global dataset to demonstrate the full NumPy + Pandas data pipeline. This project is your first real data analysis — the same workflow you will use on every ML project.</p>
<h4>Requirements</h4>
<ul>
<li>Load and inspect: shape, dtypes, null counts, value ranges per column</li>
<li>Clean: handle NaN values, fix date column to datetime, remove duplicates</li>
<li>Compute rolling 7-day average of daily cases per country</li>
<li>Find top 10 countries by total deaths-per-million (merge population data if needed)</li>
<li>Identify months with the highest case surges using groupby + datetime</li>
<li>Export a cleaned summary CSV with one row per country: total_cases, total_deaths, peak_month, rolling_avg_peak</li>
</ul>
<h4>Stretch Goals</h4>
<ul>
<li>Compare case trajectories of 5 countries using a pivot table (country vs month)</li>
<li>Detect the date of peak cases for each country programmatically</li>
<li>Add a simple bar chart using Matplotlib (preview of Part 2 visualisation)</li>
</ul>
<p><strong>Skills:</strong> NumPy operations, Pandas cleaning, groupby, datetime, merge, rolling windows, export</p>
<p><strong>Dataset:</strong> <a href="https://www.kaggle.com/datasets/josephassaker/covid19-global-dataset" target="_blank" rel="noopener">COVID-19 Global Dataset — Kaggle</a></p>
  </div>
</div>
<p class="sep">MINI-PROJECTS</p>
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">Week 1 — NumPy Statistics Without Loops</span><span class="proj-dur">1–2 days</span></div>
  <div class="proj-body">
<p>Generate a random 100×5 array of student scores (np.random.randint). Without any Python for/while loops: compute mean, std, min, max per subject; find students scoring above class average in every subject; normalise all scores to 0–1 range using vectorised operations only.</p>
  </div>
</div>
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">Week 2 — Titanic Data Health Report</span><span class="proj-dur">2–3 days</span></div>
  <div class="proj-body">
<p>Load the Titanic dataset. Produce a printed report covering: (1) overall shape and column types, (2) null percentage per column with fill strategy recommendation, (3) survival rate by sex, class, and embarked port using groupby, (4) age distribution statistics, (5) output a cleaned version with nulls handled.</p>
  </div>
</div>
</div><!-- end t6 -->
<!-- ══════════ TAB 7 — LABS ══════════ -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>NumPy Vectorisation — Measure the Speedup</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Directly measure why NumPy vectorised operations replace Python loops in all ML code.</p>
<div class="lab-step"><div class="sn">1</div><div>Create a Python list and NumPy array, both containing 1 million random numbers: <code>import random; py_list = [random.random() for _ in range(1_000_000)]</code> and <code>np_arr = np.array(py_list)</code>.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Time squaring every element using a Python loop: <code>import time; t = time.time(); result = [x**2 for x in py_list]; print(time.time() - t)</code>.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Time the same operation with NumPy: <code>t = time.time(); result = np_arr ** 2; print(time.time() - t)</code>. Record the ratio — it should be 10–100× faster.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Now benchmark: (a) Python loop sum, (b) built-in sum(), (c) np.sum(). Print all three times. Explain why the results differ.</div></div>
<div class="lab-step"><div class="sn">5</div><div>Test the view vs copy behaviour: create <code>a = np.arange(10)</code>, then <code>b = a[2:5]</code>. Modify b[0] = 99. Print a. Now do the same with <code>b = a[2:5].copy()</code> and repeat. Document what you observe.</div></div>
<div class="lab-step"><div class="sn">6</div><div><strong>Bonus:</strong> Use np.where() as a vectorised if-else: <code>np.where(arr > 0.5, "high", "low")</code>. Apply this to classify 1000 random scores as pass/fail without any Python loop.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Pandas Data Investigation Pipeline</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Build a reusable function that generates a data quality report for any DataFrame — a tool you will use on every future project.</p>
<div class="lab-step"><div class="sn">1</div><div>Download the Titanic dataset from Kaggle or use: <code>import pandas as pd; df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")</code></div></div>
<div class="lab-step"><div class="sn">2</div><div>Write a function <code>data_report(df: pd.DataFrame) -> None</code> that prints: shape, dtypes, null count + percentage per column, numeric column statistics (mean, std, min, max), categorical column value_counts (top 5 per column).</div></div>
<div class="lab-step"><div class="sn">3</div><div>Run data_report on the Titanic dataset. Identify: which columns have missing values, which columns should be dropped, what the survival rate is.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Clean the dataset: fill Age NaN with median, drop the Cabin column (too many nulls), fill Embarked NaN with mode. Use .copy() throughout. Verify with isnull().sum() that all nulls are handled.</div></div>
<div class="lab-step"><div class="sn">5</div><div>Answer these questions using groupby: (a) What is the survival rate by Sex? (b) What is the survival rate by Pclass? (c) What is the average fare by Pclass and Sex combined?</div></div>
<div class="lab-step"><div class="sn">6</div><div><strong>Extension:</strong> Add a correlation matrix to your data_report — <code>df.select_dtypes(include=np.number).corr()</code>. Print the top 5 feature pairs with highest absolute correlation.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>The SettingWithCopyWarning — Understand It Once and For All</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Understand Pandas' most confusing behaviour — the difference between views and copies — so it never silently breaks your code.</p>
<div class="lab-step"><div class="sn">1</div><div>Create: <code>df = pd.DataFrame({"a": [1,2,3,4,5], "b": [10,20,30,40,50]})</code>. Then: <code>subset = df[df["a"] > 2]</code>. Try <code>subset["b"] = 99</code>. Observe the warning.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Now do: <code>subset = df[df["a"] > 2].copy()</code>. Repeat <code>subset["b"] = 99</code>. Check df — did it change? Confirm that .copy() creates an independent object.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Use .loc for safe in-place modification on the original: <code>df.loc[df["a"] > 2, "b"] = 99</code>. This modifies df directly without warnings. Print df to confirm.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Write the rule in your own words: when do you use .copy(), when do you use .loc[]? Document this in a comment block you can paste into future projects.</div></div>
  </div>
</div>
</div><!-- end t7 -->
<!-- ══════════ TAB 8 — CHECKLIST ══════════ -->
<div id="t8" class="tab-pane">
<p class="sep">P1-M02 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can create NumPy arrays using np.array, np.zeros, np.ones, np.arange, np.linspace, np.random.randn</li>
  <li>Know the difference between array view and array copy — and when each is created</li>
  <li>Can perform element-wise operations on arrays without any Python loops</li>
  <li>Can explain broadcasting with a concrete example (adding a row vector to a matrix)</li>
  <li>Know the difference between @ (matrix multiply) and * (element-wise) — and why it matters</li>
  <li>Can load a CSV into a DataFrame and immediately inspect it with .head(), .info(), .describe()</li>
  <li>Know the difference between .loc[] (label-based) and .iloc[] (position-based) — including endpoint behaviour</li>
  <li>Can filter a DataFrame with boolean masking using AND (&amp;) and OR (|) conditions</li>
  <li>Can handle NaN values — know when to drop vs fill and which fill strategy to use</li>
  <li>Can perform a groupby aggregation and describe what split-apply-combine means</li>
  <li>Can merge two DataFrames on a key column using inner, left, right, and outer joins</li>
  <li>Can parse a date column with pd.to_datetime and extract year, month, weekday using .dt accessor</li>
  <li>Always use .copy() when creating a subset DataFrame to avoid SettingWithCopyWarning</li>
  <li>Can convert a clean DataFrame to a NumPy array with .values or .to_numpy() for Scikit-learn input</li>
  <li>Completed Lab 1: NumPy vectorisation speedup measurement</li>
  <li>Completed Lab 2: Pandas data investigation pipeline on Titanic dataset</li>
  <li>Completed Lab 3: Understood SettingWithCopyWarning</li>
  <li>Milestone project pushed to GitHub with README</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P1-M03 — Developer Essentials (Git, CLI, APIs &amp; Async)</strong>. The JSON and CSV skills you built here connect directly to calling REST APIs and parsing their responses in M03.</p>
</div>
</div><!-- end t8 -->
<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/ai-ml/part1-foundation/p1-m01-python/">← P1-M01: Python</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part1-foundation/p1-m03-dev-essentials/">Next: P1-M03 — Dev Essentials →</a>
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
    const key = 'p1m02-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
