---
title: "P1-M01 - Python Programming Fundamentals"
description: "Part 1 — Universal Foundation · Module 01 of 04 Python Programming Fundamentals Master Python from scratch — the language of AI engineering ⏱ 3 Weeks 🟢 Beginner 🐍 Python 3 📋…"
domain: ai-ml
track: ai-ml-engineering
module: part1-foundation
order: 101
ownHeader: true
url: /learning/ai-ml/part1-foundation/p1-m01-python/
---

<style>
/* ── Base ─────────────────────────────────────────── */
.mod-header{
  background:linear-gradient(135deg,#0f0a1e 0%,#1a0a3a 45%,#4c1d95 80%,#7c3aed 100%);
  border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;
  color:#fff;margin-bottom:0;
}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#c4b5fd;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#ddd6fe;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#ede9fe}

/* Tabs */
.tab-bar{display:flex;flex-wrap:wrap;background:#0f0a1e;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#c4b5fd;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#a78bfa;border-bottom-color:#a78bfa}
.tab-pane{display:none}
.tab-pane.active{display:block}

/* Concept panels */
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

/* Panel colour variants */
.p-blue  .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue  .cp-hdr{background:#0d2030}
.p-teal  .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal  .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.p-green  .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green  .cp-hdr{background:#0a2018}
.p-red    .cp-hdr{background:#faeaea}[data-theme=dark] .p-red    .cp-hdr{background:#2a0808}
.p-amber  .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber  .cp-hdr{background:#2a1e00}

.tag-blue  {background:#d0e8f8;color:#1a4a7c}
.tag-teal  {background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}
.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green {background:#c8e8d4;color:#0e4a28}
.tag-red   {background:#f4d0d0;color:#6c1a1a}
.tag-amber {background:#fae8a0;color:#5a3800}

/* Code blocks */
.cb{background:#0f0a1e;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #7c3aed}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#ddd6fe;white-space:pre}
.cm{color:#6d6875}.ck{color:#c4b5fd}.cv{color:#f0c080}.cs{color:#a78bfa}

/* Insight + warning boxes */
.ins{background:#f5f0ff;border:1.5px solid #7c3aed;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#1a0a3a;border-color:#7c3aed}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#5b21b6}
[data-theme=dark] .ins strong{color:#a78bfa}

.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}

/* Week table */
.wk-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.85rem}
.wk-table th{background:#1a0a3a;color:#ddd6fe;padding:.7rem 1rem;text-align:left;font-weight:700;font-size:.75rem;text-transform:uppercase;letter-spacing:.06em}
.wk-table td{padding:.65rem 1rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top;line-height:1.6}
.wk-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.wk-num{font-family:monospace;font-weight:700;color:#7c3aed;white-space:nowrap}

/* Resource table */
.res-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.84rem}
.res-table th{background:#4a5568;color:#fff;padding:.6rem .9rem;text-align:left;font-weight:600;font-size:.74rem;text-transform:uppercase;letter-spacing:.06em}
.res-table td{padding:.6rem .9rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top}
.res-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.res-table a{color:#7c3aed;font-weight:500;text-decoration:none}
.res-table a:hover{text-decoration:underline}
.res-type{font-family:monospace;font-size:.74rem;font-weight:700;color:#4a5568}

/* Lab boxes */
.lab-box{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;margin:1.2rem 0;overflow:hidden}
.lab-hdr{background:#1a0a3a;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-n{background:#7c3aed;color:#fff;font-size:.72rem;font-family:monospace;font-weight:700;padding:2px 10px;border-radius:12px}
.lab-hdr h4{margin:0;font-size:.95rem;font-weight:700;color:#ddd6fe;border:none}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.8rem;font-size:.88rem;line-height:1.65}
.sn{background:#7c3aed;color:#fff;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.1rem}

/* Checklist */
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem 0;border-bottom:1px solid var(--border-color,#eee);font-size:.88rem;line-height:1.6;cursor:pointer}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";font-size:1rem;flex-shrink:0;margin-top:.05rem;color:#7c3aed}
.cl li.done::before{content:"☑";color:#059669}
.cl li.done{color:var(--light-text,#888);text-decoration:line-through}

/* Sep + nav */
.sep{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--light-text,#888);border-bottom:1px solid var(--border-color,#e4e4e4);padding-bottom:.4rem;margin:2rem 0 1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin:2.5rem 0 1rem;padding-top:1.2rem;border-top:1.5px solid var(--border-color,#e4e4e4)}
.mod-nav a{font-size:.85rem;font-weight:600;color:#7c3aed;text-decoration:none;padding:.4rem .9rem;border-radius:6px;border:1.5px solid #7c3aed;transition:all .15s}
.mod-nav a:hover{background:#7c3aed;color:#fff}
.mod-nav .nb{background:#7c3aed;color:#fff}
.mod-nav .nb:hover{background:#5b21b6;border-color:#5b21b6}

/* Skip-if box */
.skip-box{background:#f5f0ff;border-left:4px solid #7c3aed;border-radius:0 8px 8px 0;padding:.85rem 1rem;margin:1rem 0;font-size:.87rem;line-height:1.65}
.skip-box strong{color:#5b21b6}

/* Project box */
.proj-box{background:#f0fdf4;border:1.5px solid #86efac;border-radius:10px;overflow:hidden;margin:1.2rem 0}
.proj-hdr{background:#15803d;color:#fff;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem;flex-wrap:wrap}
.proj-title{font-weight:700;font-size:.92rem}
.proj-dur{font-size:.78rem;opacity:.85;margin-left:auto;font-family:monospace}
.proj-body{padding:.9rem 1.2rem;font-size:.88rem;line-height:1.7}
.proj-body strong{color:#15803d}
</style>
<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 1 — Universal Foundation &nbsp;·&nbsp; Module 01 of 04</div>
  <div class="mod-title">Python Programming Fundamentals</div>
  <div class="mod-subtitle">Master Python from scratch — the language of AI engineering</div>
  <div class="mod-pills">
<span class="mod-pill">⏱ 3 Weeks</span>
<span class="mod-pill">🟢 Beginner</span>
<span class="mod-pill">🐍 Python 3</span>
<span class="mod-pill">📋 Prerequisites: None</span>
<span class="mod-pill">🛠 VS Code / Jupyter / Colab</span>
  </div>
</div>
<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🧠 Core Concepts</button>
  <button class="tab-btn" onclick="vt(event,'t2')">⚡ Deep Dive</button>
  <button class="tab-btn" onclick="vt(event,'t3')">📅 Week Plan</button>
  <button class="tab-btn" onclick="vt(event,'t4')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t6')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t7')">✅ Checklist</button>
</div>
<!-- ══════════ TAB 0 — OVERVIEW ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-purple">Foundation</span></div>
  <div class="cp-body">
<p>Python is the language of AI engineering. Full stop. Almost every library, API, and tutorial you will encounter over the next six months is in Python. This module takes you from zero to functional Python developer — able to write clean programs, handle files and APIs, and manage a codebase.</p>
<ul>
<li><strong>Core syntax</strong> — variables, data types, operators, strings, f-strings</li>
<li><strong>Data structures</strong> — lists, tuples, dictionaries, sets and their use-cases</li>
<li><strong>Control flow</strong> — if/elif/else, for loops, while loops, break/continue</li>
<li><strong>Functions</strong> — parameters, return values, *args/**kwargs, lambda, list comprehensions</li>
<li><strong>File I/O</strong> — reading and writing text and CSV files</li>
<li><strong>Error handling</strong> — try/except/finally for robust production code</li>
<li><strong>OOP basics</strong> — classes, objects, __init__, methods, encapsulation</li>
<li><strong>Environment management</strong> — venv, pip, requirements.txt</li>
</ul>
  </div>
</div>
<div class="skip-box">
  <strong>⚡ SKIP IF:</strong> You already program in C/C++/Java — Python syntax for variables, loops, conditionals, functions, and basic OOP will feel very familiar. Spend 2–3 days scanning the syntax differences (no semicolons, indentation-based blocks, dynamic typing) and jump straight to the data structures section. The venv and pip section is worth reading regardless.
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🗺️</span><h3>Why Python for AI Engineering</h3><span class="tag tag-blue">Context</span></div>
  <div class="cp-body">
<p>Python dominates AI/ML for concrete reasons — not just popularity:</p>
<ul>
<li><strong>Library ecosystem</strong> — NumPy, Pandas, Scikit-learn, PyTorch, LangChain, FastAPI are all Python-first</li>
<li><strong>API SDKs</strong> — OpenAI, Anthropic, HuggingFace all ship Python SDKs as their primary interface</li>
<li><strong>Rapid prototyping</strong> — interactive Jupyter notebooks let you experiment and iterate faster than compiled languages</li>
<li><strong>Glue language</strong> — Python is the orchestration layer that connects your LLM, vector DB, REST API, and deployment pipeline</li>
<li><strong>Job market</strong> — 90%+ of AI/ML job postings require Python as the primary language</li>
</ul>
<p>The goal this month is not to become a Python expert — it is to stop Googling basic syntax and be able to build simple programs confidently.</p>
  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Module Connections</h3><span class="tag tag-green">Dependencies</span></div>
  <div class="cp-body">
<h4>This module feeds directly into:</h4>
<ul>
<li><strong>P1-M02 (NumPy &amp; Pandas)</strong> — requires list comprehensions, classes, and file I/O</li>
<li><strong>P1-M03 (Dev Essentials)</strong> — requires understanding of pip, venv, and JSON handling</li>
<li><strong>P1-M04 (FastAPI)</strong> — requires OOP, type hints, and async/await understanding</li>
<li><strong>P4 (LLM APIs)</strong> — every API call is Python. Structured outputs use Pydantic (Python classes)</li>
</ul>
<h4>C/C++/Java background? Here is what maps directly:</h4>
<ul>
<li>Java classes → Python classes (simpler syntax, no access modifiers)</li>
<li>C arrays → Python lists (dynamic, mixed types)</li>
<li>C++ STL map → Python dict</li>
<li>Java try/catch → Python try/except</li>
</ul>
  </div>
</div>
</div><!-- end t0 -->
<!-- ══════════ TAB 1 — CORE CONCEPTS ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📦</span><h3>Variables, Types and Operators</h3><span class="tag tag-purple">Week 1</span></div>
  <div class="cp-body">
<p>Python is dynamically typed — you do not declare types. The interpreter infers them at runtime.</p>
    

```python
# Basic types
name    = "Ajay"          # str
age     = 28              # int
salary  = 85000.50        # float
active  = True            # bool
nothing = None            # NoneType

# Type checking and conversion
print(type(name))          # <class 'str'>
print(int("42"))           # 42  — explicit cast
print(str(100))            # "100"

# f-strings — the professional way to format
print(f"Hello {name}, age {age}")   # Hello Ajay, age 28
print(f"{salary:.2f}")              # 85000.50
```


<div class="ins"><p>💡 <strong>Unlike C/C++, Python variables are references, not memory slots.</strong> When you write <code>x = 5</code>, Python creates an integer object with value 5 and binds the name <code>x</code> to it. This matters for understanding mutability later.</p></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🗂️</span><h3>Core Data Structures</h3><span class="tag tag-blue">Week 1–2</span></div>
  <div class="cp-body">
<h4>List — ordered, mutable, allows duplicates</h4>
    

```python
items = ["apple", "banana", "cherry"]
items.append("date")          # add to end
items.insert(1, "avocado")     # insert at index
items.pop()                    # remove last
print(items[0])               # "apple" — 0-indexed
print(items[-1])              # last element
print(items[1:3])             # slice [1,3) = ["avocado","banana"]

# List comprehension — Pythonic and fast
squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```


<h4>Dictionary — key-value store, O(1) lookup</h4>
    

```python
user = {"name": "Ajay", "age": 28, "city": "Mumbai"}
user["email"] = "ajay@example.com"   # add key
user.get("phone", "N/A")            # safe get with default

# Dict comprehension
word_len = {w: len(w) for w in ["python", "java", "c++"]}
# {"python": 6, "java": 4, "c++": 3}

# Iterating
for key, val in user.items():
    print(f"{key}: {val}")
```


<h4>Tuple — ordered, immutable</h4>
    

```bash
coords = (19.07, 72.87)          # lat, lon of Mumbai
lat, lon = coords                  # tuple unpacking

# Use tuples for fixed data that should not change
# e.g. HTTP status codes, RGB colours, database records
HTTP_OK = (200, "OK")
```


<h4>Set — unordered, unique elements</h4>
    

```python
tags = {"python", "ml", "llm", "python"}  # duplicates removed
print(tags)  # {"python", "ml", "llm"}

# Set operations — fast membership testing O(1)
a = {1,2,3,4}
b = {3,4,5,6}
print(a & b)   # {3, 4}  — intersection
print(a | b)   # {1,2,3,4,5,6} — union
print(a - b)   # {1, 2}  — difference
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Functions and Error Handling</h3><span class="tag tag-teal">Week 2–3</span></div>
  <div class="cp-body">
    

```python
# Basic function with type hints (good practice)
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# *args — variable positional arguments
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))   # 10

# **kwargs — variable keyword arguments
def create_profile(**fields):
    return {k: v for k, v in fields.items()}

profile = create_profile(name="Ajay", role="engineer")

# Lambda — one-line anonymous function
square = lambda x: x ** 2
print(sorted([3,1,4], key=lambda x: -x))  # [4, 3, 1]
```


    

```python
# Error handling — always handle specific exceptions
def read_config(path: str) -> dict:
    try:
        with open(path, "r") as f:
            import json
            return json.load(f)
    except FileNotFoundError:
        print(f"Config not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return {}
    finally:
        print("Config read attempted")   # always runs
```


  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🏗️</span><h3>Object-Oriented Programming</h3><span class="tag tag-orange">Week 3</span></div>
  <div class="cp-body">
    

```python
# Class definition — blueprint for objects
class BankAccount:
    # Class variable (shared by all instances)
    bank_name = "PyBank"

    def __init__(self, owner: str, balance: float = 0.0):
        # Instance variables (unique per object)
        self.owner = owner
        self._balance = balance    # _prefix = convention for private

    def deposit(self, amount: float) -> None:
        if amount 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> float:
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return amount

    @property
    def balance(self) -> float:        # getter — access like attribute
        return self._balance

    def __repr__(self) -> str:
        return f"BankAccount({self.owner!r}, {self._balance})"

# Usage
acc = BankAccount("Ajay", 1000)
acc.deposit(500)
print(acc.balance)   # 1500
```


<div class="ins"><p>💡 <strong>Python OOP is simpler than Java/C++</strong> — no access modifiers, no header files. Convention: single underscore <code>_name</code> means "please don't touch this" (not enforced). Double underscore <code>__name</code> triggers name-mangling for true privacy.</p></div>
  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📁</span><h3>File I/O and JSON</h3><span class="tag tag-green">Week 3</span></div>
  <div class="cp-body">
    

```python
import json, csv
from pathlib import Path

# Writing and reading JSON (critical for LLM API work)
data = {"model": "claude-3", "temperature": 0.7, "tokens": [100, 200]}
Path("config.json").write_text(json.dumps(data, indent=2))
loaded = json.loads(Path("config.json").read_text())

# CSV reading — used constantly in data work
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    students = list(reader)   # list of dicts, one per row

# CSV writing
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows([{"name": "Ajay", "score": 95}])
```


  </div>
</div>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">🌍</span><h3>Virtual Environments and Package Management</h3><span class="tag tag-amber">Essential</span></div>
  <div class="cp-body">
<p>Every project must have its own virtual environment. This is non-negotiable — it prevents dependency conflicts between projects.</p>
    

```bash
# Create and activate virtual environment
python -m venv .venv                 # create
source .venv/bin/activate            # Linux/Mac
.venv\Scripts\activate              # Windows

# Install packages
pip install requests pandas numpy    # install
pip install openai anthropic         # AI SDKs

# Freeze and restore dependencies
pip freeze > requirements.txt        # save exact versions
pip install -r requirements.txt      # restore on new machine

# Deactivate
deactivate
```


<div class="warn"><p>⚠️ <strong>Never install packages globally</strong> — always activate your venv first. Global installs create conflicts that are painful to debug. Add <code>.venv/</code> to your <code>.gitignore</code> — never commit the venv folder.</p></div>
  </div>
</div>
</div><!-- end t1 -->
<!-- ══════════ TAB 2 — DEEP DIVE ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Mutable vs Immutable — The Most Common Bug Source</h3><span class="tag tag-purple">Critical</span></div>
  <div class="cp-body">
<p>Understanding mutability prevents an entire class of bugs that trip up engineers coming from C/C++/Java.</p>
    

```python
# Immutable — int, str, tuple, float, bool
x = 5
y = x
y = 10
print(x)   # Still 5 — y got a new object

# Mutable — list, dict, set
a = [1, 2, 3]
b = a              # b points to SAME list as a
b.append(4)
print(a)           # [1, 2, 3, 4]  ← a changed!

# Fix: explicit copy
b = a.copy()       # shallow copy
b = a[:]           # slice copy — same result
import copy
b = copy.deepcopy(a)   # deep copy for nested structures

# Dangerous default argument anti-pattern
def add_item(item, lst=[]):    # BAD — lst shared across calls!
    lst.append(item)
    return lst

# Correct pattern
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Comprehensions and Functional Patterns</h3><span class="tag tag-blue">Pythonic Code</span></div>
  <div class="cp-body">
    

```python
# List comprehension — replaces most for loops
even_squares = [x**2 for x in range(20) if x % 2 == 0]

# Dict comprehension — used constantly with API responses
response_data = [{"id": 1, "name": "alice"}, {"id": 2, "name": "bob"}]
id_map = {item["id"]: item["name"] for item in response_data}
# {1: "alice", 2: "bob"}

# Generator — lazy evaluation, memory efficient for large data
def token_chunks(text: str, size: int):
    words = text.split()
    for i in range(0, len(words), size):
        yield " ".join(words[i:i+size])

# Use with large LLM context windows
for chunk in token_chunks(long_document, 500):
    process(chunk)   # never loads full doc into memory

# zip and enumerate — essential for pairing data
names  = ["alice", "bob", "charlie"]
scores = [85, 92, 78]
for i, (name, score) in enumerate(zip(names, scores)):
    print(f"{i}: {name} = {score}")
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔌</span><h3>Modules, Imports and Project Structure</h3><span class="tag tag-teal">Production Habit</span></div>
  <div class="cp-body">
    

```python
# Standard imports
import os, sys, json, csv
from pathlib import Path
from typing import Optional, List, Dict, Any

# Third-party imports (installed via pip)
import requests
from openai import OpenAI

# Relative imports in your own package
from .utils import format_response
from ..config import API_KEY

# Typical project structure
# my-ai-app/
# ├── main.py          ← entry point
# ├── config.py        ← constants, env vars
# ├── models/          ← Pydantic schemas
# │   └── __init__.py
# ├── services/        ← business logic
# │   ├── __init__.py
# │   └── llm.py
# ├── requirements.txt
# └── .env             ← secrets (never commit!)

# Reading environment variables (secrets pattern)
import os
from dotenv import load_dotenv
load_dotenv()                                 # loads .env file
api_key = os.environ.get("OPENAI_API_KEY")   # never hardcode keys
```


  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">⏳</span><h3>Async/Await — Critical for LLM APIs</h3><span class="tag tag-orange">Month 2 Preview</span></div>
  <div class="cp-body">
<p>LLM API calls are I/O-bound — they wait for network responses. Async Python lets your program do other work while waiting, instead of blocking.</p>
    

```python
import asyncio

# Sync version — blocks for 3 seconds total
import time
def fetch_sync():
    time.sleep(1)   # simulates API call
    return "result"

# Async version — runs concurrently, total ~1 second
async def fetch_async():
    await asyncio.sleep(1)   # yields control while waiting
    return "result"

async def main():
    # Run 3 API calls concurrently
    results = await asyncio.gather(
        fetch_async(),
        fetch_async(),
        fetch_async()
    )
    return results

asyncio.run(main())   # entry point for async code

# Anthropic async client pattern (Month 2)
# async with anthropic.AsyncAnthropic() as client:
#     response = await client.messages.create(...)
```


<div class="ins"><p>💡 <strong>You do not need to master async now.</strong> The key insight is: <code>async def</code> defines a coroutine (a function that can pause), and <code>await</code> is where it pauses to let other work run. You will use this constantly when calling LLM APIs and building FastAPI endpoints.</p></div>
  </div>
</div>
</div><!-- end t2 -->
<!-- ══════════ TAB 3 — WEEK PLAN ══════════ -->
<div id="t3" class="tab-pane">
<p class="sep">3-WEEK STRUCTURED PLAN</p>
<table class="wk-table">
  <thead><tr><th>Week</th><th>Topics</th><th>Daily Task / Mini-Project</th></tr></thead>
  <tbody>
<tr>
<td class="wk-num">Week 1</td>
<td>Install Python 3.10+ and VS Code. Variables, data types, type casting, string methods and f-strings. Lists — indexing, slicing, list methods. Tuples vs lists. Control flow: if/elif/else, for loops, while loops, break/continue/pass.</td>
<td>Day 1–2: Unit converter (km↔miles, °C↔°F). Day 3: String palindrome checker. Day 4–5: Shopping list CLI using lists (add, remove, display). Day 6–7: Number guessing game with while loop + score tracker.</td>
</tr>
<tr>
<td class="wk-num">Week 2</td>
<td>Dictionaries — CRUD operations, nested dicts, dict comprehensions. Sets — union, intersection, difference. Functions — defining, default args, *args/**kwargs, lambda, list comprehensions. Modules and import system.</td>
<td>Day 1–2: Phone book CLI using dictionaries (add, search, delete, update). Day 3–4: Grade classifier using if/elif (A/B/C/D/F with GPA). Day 5–7: Word frequency counter — takes a text file, returns top-10 words using dicts + sorted + lambda.</td>
</tr>
<tr>
<td class="wk-num">Week 3</td>
<td>File I/O — open(), read(), write() with text and CSV. JSON — json.loads(), json.dumps(), working with nested structures. Error handling — try/except/finally, custom exceptions. OOP — classes, __init__, methods, @property. venv + pip + requirements.txt.</td>
<td>Day 1–2: CSV reader/writer for student grade data. Day 3–4: Bank Account class with deposit, withdraw, balance property. Day 5–7: Full milestone project — CLI Student Grade Management System (see Projects tab).</td>
</tr>
  </tbody>
</table>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">⚙️</span><h3>Environment Setup — Do This First</h3><span class="tag tag-purple">Day 1</span></div>
  <div class="cp-body">
    

```bash
# 1. Install Python 3.10+ from python.org
# 2. Install VS Code + Python extension (Microsoft)
# 3. Or use Google Colab — zero setup, free GPU
#    https://colab.research.google.com/

# Verify installation
python --version    # Python 3.10.x or higher
pip --version       # pip 23.x

# Install core packages you will use throughout Part 1
pip install jupyter numpy pandas matplotlib requests python-dotenv
```


  </div>
</div>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">💡</span><h3>The Most Important Learning Habit</h3><span class="tag tag-amber">Meta-Skill</span></div>
  <div class="cp-body">
<p>The most common beginner mistake is consuming content passively — reading along, nodding, and never opening a code editor. Every concept in this module must be typed out and run. Not copy-pasted. Typed. Your fingers need to know the syntax before your brain does.</p>
<ul>
<li>Open a Python REPL (<code>python</code> in terminal) and experiment immediately after each concept</li>
<li>Every error message is a learning opportunity — read it fully before searching</li>
<li>Push every mini-project to GitHub, even if it is 20 lines</li>
<li>If something works but you don't know why — break it intentionally and observe</li>
</ul>
  </div>
</div>
</div><!-- end t3 -->
<!-- ══════════ TAB 4 — RESOURCES ══════════ -->
<div id="t4" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
<tr><td class="res-type">Course</td><td><a href="https://cs50.harvard.edu/python/" target="_blank" rel="noopener">CS50P — Introduction to Programming with Python (Harvard, Free)</a></td><td>Best free Python course. Structured problem sets. Certificate on completion.</td></tr>
<tr><td class="res-type">Video</td><td><a href="https://www.youtube.com/watch?v=rfscVS0vtbw" target="_blank" rel="noopener">Python for Beginners — freeCodeCamp (YouTube, 4.5 hrs)</a></td><td>Single video covering all fundamentals. Watch at 1.5x after Week 1.</td></tr>
<tr><td class="res-type">Course</td><td><a href="https://www.coursera.org/specializations/python" target="_blank" rel="noopener">Python for Everybody — Coursera (Free to audit)</a></td><td>Best for absolute beginners. Dr. Chuck is exceptionally clear.</td></tr>
<tr><td class="res-type">Docs</td><td><a href="https://docs.python.org/3/tutorial/" target="_blank" rel="noopener">Official Python Tutorial — python.org</a></td><td>Authoritative reference. Dry but precise. Use as lookup, not primary resource.</td></tr>
<tr><td class="res-type">Course</td><td><a href="https://www.kaggle.com/learn/python" target="_blank" rel="noopener">Kaggle Python Course (Free, Interactive)</a></td><td>Hands-on exercises with instant feedback. Great for Week 1–2.</td></tr>
<tr><td class="res-type">Book</td><td><a href="https://automatetheboringstuff.com/" target="_blank" rel="noopener">Automate the Boring Stuff with Python (Free online)</a></td><td>Project-oriented. Best book for building real scripts in Week 3.</td></tr>
<tr><td class="res-type">Video</td><td><a href="https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU" target="_blank" rel="noopener">Corey Schafer — Python OOP Tutorials (YouTube Playlist)</a></td><td>Best OOP explanation for engineers coming from Java/C++.</td></tr>
<tr><td class="res-type">Tool</td><td><a href="https://colab.research.google.com/" target="_blank" rel="noopener">Google Colab — Free Cloud Jupyter Notebooks</a></td><td>Zero setup. Free GPU. Use if local setup is painful.</td></tr>
  </tbody>
</table>
<p class="sep">PRACTICE DATASET</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Used In</th></tr></thead>
  <tbody>
<tr><td class="res-type">Dataset</td><td><a href="https://archive.ics.uci.edu/dataset/320/student+performance" target="_blank" rel="noopener">UCI Student Performance Dataset</a></td><td>Milestone project — CLI Grade Management System</td></tr>
  </tbody>
</table>
</div><!-- end t4 -->
<!-- ══════════ TAB 5 — PROJECTS ══════════ -->
<div id="t5" class="tab-pane">
<p class="sep">MILESTONE PROJECT</p>
<div class="proj-box">
  <div class="proj-hdr">
<span>🛠</span>
<span class="proj-title">CLI Student Grade Management System</span>
<span class="proj-dur">[Beginner] 3–4 days · Week 3</span>
  </div>
  <div class="proj-body">
<p>Build a command-line application that manages student grade data using Python fundamentals. This project tests every concept from the module in a cohesive real-world context.</p>
<h4>Requirements</h4>
<ul>
<li>Reads student data from a CSV file (name, subject scores)</li>
<li>Calculates grade (A/B/C/D/F), GPA, and class rank for each student</li>
<li>Supports filtering by subject or grade range</li>
<li>Sorts students by any column (name, GPA, specific subject)</li>
<li>Handles invalid input gracefully with try/except (missing file, bad data)</li>
<li>Writes a cleaned summary CSV as output</li>
<li>CLI menu: view all / search by name / filter / sort / export / quit</li>
</ul>
<h4>Stretch Goals</h4>
<ul>
<li>Add a Student class with methods (calculate_gpa, get_grade, __repr__)</li>
<li>Store data in JSON format as an alternative to CSV</li>
<li>Add a simple stats report: class average, highest/lowest scorer, grade distribution</li>
</ul>
<p><strong>Skills demonstrated:</strong> File I/O, CSV handling, dictionaries, lists, functions, error handling, OOP basics, sorting with lambda, string formatting</p>
<p><strong>Dataset:</strong> <a href="https://archive.ics.uci.edu/dataset/320/student+performance" target="_blank" rel="noopener">UCI Student Performance Dataset</a> or create your own CSV</p>
<p><strong>Push to GitHub</strong> with a README describing what the tool does and how to run it.</p>
  </div>
</div>
<p class="sep">MINI-PROJECTS (WEEKLY)</p>
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">Week 1 — Unit Converter CLI</span><span class="proj-dur">1–2 days</span></div>
  <div class="proj-body">
<p>Build a CLI tool that converts between: km↔miles, °C↔°F, kg↔lbs. Menu-driven loop. Handles invalid input. Demonstrates: variables, type casting, f-strings, conditionals, while loop.</p>
  </div>
</div>
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">Week 2 — Word Frequency Analyser</span><span class="proj-dur">2–3 days</span></div>
  <div class="proj-body">
<p>Takes a .txt file as input. Returns the top-10 most frequent words (excluding common stop words). Uses: file I/O, dicts, sorted() with lambda, set for stop words. Try it on a book chapter from Project Gutenberg.</p>
  </div>
</div>
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">Week 3 — Public API Script</span><span class="proj-dur">1–2 days</span></div>
  <div class="proj-body">
<p>Call the Open-Meteo weather API (no API key needed) using the <code>requests</code> library. Format and print a 7-day forecast. Save the raw JSON response to a file. Push to GitHub with README. This is a preview of Month 2's API work.</p>
    

```python
import requests, json
url = "https://api.open-meteo.com/v1/forecast?latitude=19.07&longitude=72.87&daily=temperature_2m_max&timezone=Asia/Kolkata"
r = requests.get(url)
data = r.json()
print(json.dumps(data, indent=2))
```


  </div>
</div>
</div><!-- end t5 -->
<!-- ══════════ TAB 6 — LABS ══════════ -->
<div id="t6" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Python REPL Exploration — Types and Mutability</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Build intuition for Python's type system and mutability through hands-on exploration in the REPL.</p>
<div class="lab-step"><div class="sn">1</div><div>Open a terminal and run <code>python3</code> (or <code>python</code> on Windows). You are now in the interactive REPL (Read-Eval-Print Loop). Type expressions and see results immediately.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Run these lines one by one and note the output: <code>x = [1, 2, 3]</code>, then <code>y = x</code>, then <code>y.append(4)</code>, then <code>print(x)</code>. Did x change? Why?</div></div>
<div class="lab-step"><div class="sn">3</div><div>Now try: <code>a = "hello"</code>, then <code>b = a</code>, then <code>b = b + " world"</code>, then <code>print(a)</code>. Did a change? Why not? What is the key difference between strings and lists?</div></div>
<div class="lab-step"><div class="sn">4</div><div>Run <code>import sys</code> then <code>sys.getsizeof([])</code> vs <code>sys.getsizeof([1,2,3,4,5])</code>. See memory usage grow. Try the same with a string of different lengths.</div></div>
<div class="lab-step"><div class="sn">5</div><div>Test the mutable default argument bug: define <code>def add(x, lst=[]): lst.append(x); return lst</code>. Call it three times: <code>add(1)</code>, <code>add(2)</code>, <code>add(3)</code>. What happens? Fix the function.</div></div>
<div class="lab-step"><div class="sn">6</div><div><strong>Bonus:</strong> Use <code>id()</code> to see object identity: <code>a = [1,2,3]; b = a; print(id(a) == id(b))</code>. Then do <code>b = a.copy(); print(id(a) == id(b))</code>. What changes?</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Build a JSON Config Reader with Error Handling</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Write production-quality Python that reads configuration files robustly — a pattern you will use in every AI project.</p>
<div class="lab-step"><div class="sn">1</div><div>Create a file called <code>config.json</code> with this content: <code>{"model": "gpt-4", "temperature": 0.7, "max_tokens": 1000, "api_key": "sk-test"}</code></div></div>
<div class="lab-step"><div class="sn">2</div><div>Write a function <code>load_config(path: str) -> dict</code> that reads this file. Use try/except to handle: FileNotFoundError (return empty dict), json.JSONDecodeError (print error, return empty dict), PermissionError (print error, return empty dict).</div></div>
<div class="lab-step"><div class="sn">3</div><div>Add a <code>validate_config(config: dict) -> bool</code> function that checks: "model" key exists, "temperature" is between 0 and 2, "max_tokens" is a positive integer. Return True only if all pass.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Test with: valid config, missing file, invalid JSON (break the JSON manually), missing required key, temperature = 3.0. Confirm each error is handled cleanly.</div></div>
<div class="lab-step"><div class="sn">5</div><div>Add a <code>save_config(config: dict, path: str) -> None</code> function that writes back to JSON with 2-space indentation. Add a timestamp field: <code>config["last_updated"] = datetime.now().isoformat()</code></div></div>
<div class="lab-step"><div class="sn">6</div><div><strong>Extension:</strong> Use <code>os.environ.get()</code> to override the api_key from an environment variable instead of reading it from the file. This is the secure pattern used in all production AI projects.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>OOP — Build a Student Registry Class</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Apply OOP concepts to build a reusable data class — a preview of the Pydantic models you will use in Part 4.</p>
<div class="lab-step"><div class="sn">1</div><div>Create a <code>Student</code> class with: <code>__init__(self, name, scores: dict)</code> where scores is a dict of subject→score pairs. Store both as instance variables.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Add a <code>gpa</code> property that calculates the average of all scores. Add a <code>grade</code> property that returns "A" if gpa >= 90, "B" if >= 80, etc.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Add <code>__repr__</code> and <code>__str__</code> methods. <code>__repr__</code> should be unambiguous (useful for debugging). <code>__str__</code> should be human-readable.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Create a <code>StudentRegistry</code> class that holds a list of Student objects. Add methods: <code>add(student)</code>, <code>find(name)</code>, <code>top_n(n)</code> (returns top n by GPA), <code>class_average()</code>.</div></div>
<div class="lab-step"><div class="sn">5</div><div>Add <code>to_csv(path)</code> and <code>from_csv(path)</code> class methods to the registry for persistence. Test the full round-trip: create → save → load → query.</div></div>
  </div>
</div>
</div><!-- end t6 -->
<!-- ══════════ TAB 7 — CHECKLIST ══════════ -->
<div id="t7" class="tab-pane">
<p class="sep">P1-M01 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain the difference between mutable and immutable types and give one real bug this causes</li>
  <li>Can write a list comprehension that filters and transforms a list in one line</li>
  <li>Can define a function with default arguments, *args, and **kwargs and explain when to use each</li>
  <li>Know the difference between a list, tuple, set, and dict — and when to use each</li>
  <li>Can read and write JSON and CSV files using the standard library</li>
  <li>Can handle FileNotFoundError, json.JSONDecodeError, and ValueError cleanly with try/except</li>
  <li>Can create a class with __init__, instance variables, properties, and __repr__</li>
  <li>Know what a virtual environment is, can create one, activate it, and install packages</li>
  <li>Can read an API key from environment variables (not hardcoded in source)</li>
  <li>Know what async def and await mean conceptually and why LLM APIs use them</li>
  <li>Completed Lab 1: REPL exploration of types and mutability</li>
  <li>Completed Lab 2: JSON config reader with full error handling</li>
  <li>Completed Lab 3: Student class with OOP patterns</li>
  <li>Milestone project pushed to GitHub with README</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P1-M02 — NumPy &amp; Pandas Data Toolkit</strong>. The list/dict/CSV skills you built here directly underpin everything in NumPy array indexing and Pandas DataFrame operations.</p>
</div>
</div>
<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/ai-ml/ai-ml-roadmap/">← AI/ML Roadmap</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part1-foundation/p1-m02-numpy-pandas/">Next: P1-M02 — NumPy &amp; Pandas →</a>
</div>
<script>
function vt(e, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  e.target.classList.add('active');
  document.getElementById(id).classList.add('active');
}
// Persist completed checklist items in localStorage
document.addEventListener('DOMContentLoaded', () => {
  const items = document.querySelectorAll('.cl li');
  items.forEach((li, i) => {
    const key = 'p1m01-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
