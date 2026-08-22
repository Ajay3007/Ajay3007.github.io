---
title: "P4-M12 - Structured Outputs & Tool Calling"
description: "Part 4 — LLM API Mastery · Module 12 of 14 Structured Outputs Tool Calling Get typed Python objects back from LLMs — and make them call your functions ⏱ 1 Week 🟡 Intermediate…"
domain: ai-ml
track: ai-ml-engineering
module: part4-llm-apis
order: 412
ownHeader: true
url: /learning/ai-ml/part4-llm-apis/p4-m12-structured-outputs/
---

<style>
.mod-header{background:linear-gradient(135deg,#0f0a1e 0%,#1a0a3a 40%,#312e81 70%,#4f46e5 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#a5b4fc;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#e0e7ff;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#e0e7ff}
.tab-bar{display:flex;flex-wrap:wrap;background:#0f0a1e;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#a5b4fc;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#818cf8;border-bottom-color:#818cf8}
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
.p-indigo .cp-hdr{background:#eef2ff}[data-theme=dark] .p-indigo .cp-hdr{background:#1e1a3a}
.tag-blue{background:#d0e8f8;color:#1a4a7c}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}.tag-red{background:#f4d0d0;color:#6c1a1a}
.tag-amber{background:#fae8a0;color:#5a3800}.tag-indigo{background:#e0e7ff;color:#3730a3}
.cb{background:#0f0a1e;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #4f46e5}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#e0e7ff;white-space:pre}
.cm{color:#6d6875}.ck{color:#a5b4fc}.cv{color:#f0c080}.cs{color:#818cf8}
.ins{background:#eef2ff;border:1.5px solid #4f46e5;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#1e1a3a;border-color:#4f46e5}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#3730a3}[data-theme=dark] .ins strong{color:#818cf8}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.wk-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.85rem}
.wk-table th{background:#1e1a3a;color:#e0e7ff;padding:.7rem 1rem;text-align:left;font-weight:700;font-size:.75rem;text-transform:uppercase;letter-spacing:.06em}
.wk-table td{padding:.65rem 1rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top;line-height:1.6}
.wk-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.wk-num{font-family:monospace;font-weight:700;color:#4f46e5;white-space:nowrap}
.res-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.84rem}
.res-table th{background:#4a5568;color:#fff;padding:.6rem .9rem;text-align:left;font-weight:600;font-size:.74rem;text-transform:uppercase;letter-spacing:.06em}
.res-table td{padding:.6rem .9rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top}
.res-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.res-table a{color:#4f46e5;font-weight:500;text-decoration:none}
.res-table a:hover{text-decoration:underline}
.res-type{font-family:monospace;font-size:.74rem;font-weight:700;color:#4a5568}
.lab-box{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;margin:1.2rem 0;overflow:hidden}
.lab-hdr{background:#1e1a3a;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-n{background:#4f46e5;color:#fff;font-size:.72rem;font-family:monospace;font-weight:700;padding:2px 10px;border-radius:12px}
.lab-hdr h4{margin:0;font-size:.95rem;font-weight:700;color:#e0e7ff;border:none}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.8rem;font-size:.88rem;line-height:1.65}
.sn{background:#4f46e5;color:#fff;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem 0;border-bottom:1px solid var(--border-color,#eee);font-size:.88rem;line-height:1.6;cursor:pointer}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";font-size:1rem;flex-shrink:0;margin-top:.05rem;color:#4f46e5}
.cl li.done::before{content:"☑";color:#059669}
.cl li.done{color:var(--light-text,#888);text-decoration:line-through}
.sep{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--light-text,#888);border-bottom:1px solid var(--border-color,#e4e4e4);padding-bottom:.4rem;margin:2rem 0 1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin:2.5rem 0 1rem;padding-top:1.2rem;border-top:1.5px solid var(--border-color,#e4e4e4)}
.mod-nav a{font-size:.85rem;font-weight:600;color:#4f46e5;text-decoration:none;padding:.4rem .9rem;border-radius:6px;border:1.5px solid #4f46e5;transition:all .15s}
.mod-nav a:hover{background:#4f46e5;color:#fff}
.mod-nav .nb{background:#4f46e5;color:#fff}
.mod-nav .nb:hover{background:#3730a3;border-color:#3730a3}
.proj-box{background:#f0fdf4;border:1.5px solid #86efac;border-radius:10px;overflow:hidden;margin:1.2rem 0}
.proj-hdr{background:#15803d;color:#fff;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem;flex-wrap:wrap}
.proj-title{font-weight:700;font-size:.92rem}
.proj-dur{font-size:.78rem;opacity:.85;margin-left:auto;font-family:monospace}
.proj-body{padding:.9rem 1.2rem;font-size:.88rem;line-height:1.7}
.proj-body strong{color:#15803d}
/* tool flow diagram */
.tool-flow{display:flex;align-items:center;flex-wrap:wrap;gap:.3rem;margin:.8rem 0;font-size:.8rem}
.tf-box{padding:.4rem .9rem;border-radius:8px;font-family:monospace;font-weight:700;border:1.5px solid;text-align:center}
.tf-arrow{color:#4f46e5;font-size:1.1rem;font-weight:700}
.tf-you{background:#eef2ff;border-color:#818cf8;color:#3730a3}
.tf-llm{background:#fdf4dc;border-color:#fcd34d;color:#92400e}
.tf-exec{background:#f0fdf4;border-color:#86efac;color:#15803d}
</style>
<!-- ── MODULE HEADER ── -->
<div class="mod-header">
  <div class="mod-eyebrow">Part 4 — LLM API Mastery &nbsp;·&nbsp; Module 12 of 14</div>
  <div class="mod-title">Structured Outputs &amp; Tool Calling</div>
  <div class="mod-subtitle">Get typed Python objects back from LLMs — and make them call your functions</div>
  <div class="mod-pills">
<span class="mod-pill">⏱ 1 Week</span>
<span class="mod-pill">🟡 Intermediate</span>
<span class="mod-pill">🔧 Pydantic · Instructor · OpenAI · Anthropic</span>
<span class="mod-pill">📋 Prerequisite: P4-M11</span>
  </div>
</div>
<!-- ── TAB BAR ── -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">📐 Structured Outputs</button>
  <button class="tab-btn" onclick="vt(event,'t2')">📦 Instructor Library</button>
  <button class="tab-btn" onclick="vt(event,'t3')">🔧 Tool Calling</button>
  <button class="tab-btn" onclick="vt(event,'t4')">🔁 Tool Loop Patterns</button>
  <button class="tab-btn" onclick="vt(event,'t5')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t6')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t7')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">✅ Checklist</button>
</div>
<!-- ══════════ TAB 0 — OVERVIEW ══════════ -->
<div id="t0" class="tab-pane active">
<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-indigo">Core AI Engineering</span></div>
  <div class="cp-body">
<p>In real applications you almost never want raw text from an LLM — you want structured data you can parse, store, validate, and use in your code. This module covers two critical techniques for getting reliable structure out of LLMs:</p>
<ul>
<li><strong>Structured outputs</strong> — forcing the model to return data that matches a Pydantic schema you define. Never parse free-text JSON again.</li>
<li><strong>Tool calling (function calling)</strong> — giving the model the ability to call your Python functions. This is what transforms an LLM from a text generator into a system that can take real actions.</li>
</ul>
<p>These two techniques are the foundation of agents, RAG pipelines, and any AI system that needs to interact with the real world. Master them here before building anything complex.</p>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Why Structured Outputs Matter</h3><span class="tag tag-blue">Motivation</span></div>
  <div class="cp-body">
    

```python
# The problem with raw text output
response = call_claude("Extract the name, age, and city from: 'John is 28, lives in Mumbai'")
# Response might be:
#   "The name is John, he is 28 years old, and he lives in Mumbai."
#   "Name: John
Age: 28
City: Mumbai"
#   {"name": "John", "age": "28", "city": "Mumbai"}  ← age is a string, not int!
#   {"name": "John", "age": 28}  ← city missing!
# You cannot reliably parse any of these

# With structured outputs (Pydantic + Instructor)
class Person(BaseModel):
    name: str
    age:  int
    city: str

person = extract(text, Person)
print(person.age + 1)   # 29 — it's always an int. Always present.
```


<div class="ins"><p>💡 <strong>Structured outputs solve three problems at once:</strong> type safety (age is always an int), completeness (required fields are always present), and consistency (same schema every time, regardless of how the model phrases its response).</p></div>
  </div>
</div>
</div><!-- end t0 -->
<!-- ══════════ TAB 1 — STRUCTURED OUTPUTS ══════════ -->
<div id="t1" class="tab-pane">
<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">📐</span><h3>OpenAI Native Structured Outputs</h3><span class="tag tag-indigo">OpenAI Only</span></div>
  <div class="cp-body">
<p>OpenAI (gpt-4o and later) supports native structured outputs via <code>response_format</code> with a JSON schema. The model is guaranteed to return valid JSON matching your schema — it cannot deviate.</p>
    

```python
from openai import OpenAI
from pydantic import BaseModel
from typing import List, Optional

client = OpenAI()

class CalendarEvent(BaseModel):
    name:       str
    date:       str         # ISO format: YYYY-MM-DD
    participants: List[str]
    location:   Optional[str] = None

# Method 1: parse() helper — simplest approach
completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[{
        "role": "user",
        "content": "Extract event: 'Meeting with Alice and Bob on 2024-03-15 at Bangalore office'"
    }],
    response_format=CalendarEvent,
)

event = completion.choices[0].message.parsed
print(event.name)           # "Meeting"
print(event.participants)   # ["Alice", "Bob"]
print(event.date)           # "2024-03-15"
print(type(event))          # <class 'CalendarEvent'> — a real Python object

# Handle refusal (model refuses to comply with the request)
if completion.choices[0].message.refusal:
    print(f"Model refused: {completion.choices[0].message.refusal}")
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>JSON Mode vs Structured Outputs</h3><span class="tag tag-blue">Know the Difference</span></div>
  <div class="cp-body">
<table style="width:100%;border-collapse:collapse;font-size:.85rem;margin:.8rem 0">
<thead><tr style="background:#1e1a3a;color:#e0e7ff"><th style="padding:.6rem .9rem;text-align:left">Feature</th><th style="padding:.6rem .9rem">JSON Mode</th><th style="padding:.6rem .9rem">Structured Outputs</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.6rem .9rem">Guarantees</td><td style="padding:.6rem .9rem">Valid JSON only — no schema enforcement</td><td style="padding:.6rem .9rem">Valid JSON matching exact schema</td></tr>
<tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.6rem .9rem">Missing fields</td><td style="padding:.6rem .9rem">Can still omit required fields</td><td style="padding:.6rem .9rem">Required fields always present</td></tr>
<tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.6rem .9rem">Wrong types</td><td style="padding:.6rem .9rem">age can be "28" (string)</td><td style="padding:.6rem .9rem">age is always int</td></tr>
<tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.6rem .9rem">Extra fields</td><td style="padding:.6rem .9rem">Can add unexpected fields</td><td style="padding:.6rem .9rem">Only schema fields returned</td></tr>
<tr><td style="padding:.6rem .9rem">Use when</td><td style="padding:.6rem .9rem">Quick prototyping, flexible schema</td><td style="padding:.6rem .9rem">Production — any time you parse the output</td></tr>
</tbody>
</table>
    

```bash
# JSON mode — just ensures valid JSON, not schema compliance
response = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},   # JSON mode
    messages=[{"role": "user", "content": "Extract name and age as JSON"}]
)
data = json.loads(response.choices[0].message.content)
# data["age"] might be "28" or 28 — you don't know
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🧩</span><h3>Complex Pydantic Schemas</h3><span class="tag tag-teal">Real-World Patterns</span></div>
  <div class="cp-body">
    

```python
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from enum import Enum

# Nested models
class Address(BaseModel):
    street: str
    city:   str
    country: str
    postal_code: Optional[str] = None

class Contact(BaseModel):
    name:    str
    email:   str
    phone:   Optional[str] = None
    address: Optional[Address] = None   # nested model

# Enums for controlled vocabularies
class Priority(str, Enum):
    LOW    = "low"
    MEDIUM = "medium"
    HIGH   = "high"
    URGENT = "urgent"

class Ticket(BaseModel):
    title:    str
    priority: Priority               # must be one of 4 values
    tags:     List[str] = []
    assignee: Optional[Contact] = None

# Discriminated unions — different schema per type
class TextContent(BaseModel):
    type: Literal["text"]
    text: str

class ImageContent(BaseModel):
    type: Literal["image"]
    url:  str
    alt:  Optional[str] = None

from typing import Union, Annotated
Content = Annotated[Union[TextContent, ImageContent], Field(discriminator="type")]

class Post(BaseModel):
    title:    str
    contents: List[Content]   # can be text or image blocks
```


  </div>
</div>
</div><!-- end t1 -->
<!-- ══════════ TAB 2 — INSTRUCTOR ══════════ -->
<div id="t2" class="tab-pane">
<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">📦</span><h3>Instructor — Structured Outputs for Every Provider</h3><span class="tag tag-indigo">Production Standard</span></div>
  <div class="cp-body">
<p>Instructor is the cleanest way to get structured outputs from any LLM provider using Pydantic models. It works with OpenAI, Anthropic, Google, HuggingFace, and 15+ others using the same code interface — and adds automatic retries when validation fails.</p>
    

```python
pip install instructor anthropic openai

import instructor
import anthropic
from openai import OpenAI
from pydantic import BaseModel
from typing import List

# ── With Anthropic (Claude) ────────────────────────────
claude_client = instructor.from_anthropic(anthropic.Anthropic())

class MovieReview(BaseModel):
    title:       str
    rating:      float   # 1.0 to 10.0
    pros:        List[str]
    cons:        List[str]
    recommended: bool

review = claude_client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": "Review the movie Interstellar"
    }],
    response_model=MovieReview,   # ← Pydantic model as schema
)

print(review.title)       # "Interstellar"
print(review.rating)      # 9.2  — always a float
print(review.recommended) # True — always a bool

# ── With OpenAI (GPT-4o) ───────────────────────────────
oai_client = instructor.from_openai(OpenAI())

review = oai_client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Review Interstellar"}],
    response_model=MovieReview,   # ← exact same code
)
# Same API regardless of provider — easy to switch
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>Automatic Retries and Partial Extraction</h3><span class="tag tag-blue">Reliability</span></div>
  <div class="cp-body">
    

```python
import instructor
from instructor import Mode
from pydantic import BaseModel, field_validator

# Instructor retries automatically when validation fails
client = instructor.from_anthropic(
    anthropic.Anthropic(),
    mode=Mode.ANTHROPIC_JSON,
    max_retries=3   # retry up to 3 times if schema not satisfied
)

class StrictRating(BaseModel):
    score: float
    label: str

    @field_validator("score")
    @classmethod
    def must_be_in_range(cls, v: float) -> float:
        if not (1.0 10.0):
            raise ValueError(f"Score {v} must be between 1.0 and 10.0")
        return round(v, 1)

    @field_validator("label")
    @classmethod
    def must_be_valid_label(cls, v: str) -> str:
        valid = {"excellent", "good", "average", "poor"}
        if v.lower() not in valid:
            raise ValueError(f"Label must be one of {valid}")
        return v.lower()

# If model returns score=11.0, Instructor catches the validation error,
# tells the model what went wrong, and asks it to try again

# Partial extraction — stream partial objects as they are generated
from instructor import Partial

class LargeReport(BaseModel):
    executive_summary: str
    key_findings:      List[str]
    recommendations:   List[str]
    conclusion:        str

# Stream partial object — UI can update progressively
for partial_report in client.messages.create_partial(
    model="claude-3-5-sonnet-20241022",
    max_tokens=4096,
    messages=[{"role": "user", "content": "Generate a quarterly report"}],
    response_model=Partial[LargeReport],
):
    if partial_report.executive_summary:
        print(partial_report.executive_summary, end="")
```


<div class="ins"><p>💡 <strong>Automatic retries are Instructor's killer feature.</strong> When a field validator raises a ValueError, Instructor sends the model a message saying "Your previous response failed validation: [error]. Please fix and try again." The model almost always succeeds on the second attempt. This makes structured extraction production-ready.</p></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🏭</span><h3>Real-World Extraction Patterns</h3><span class="tag tag-teal">Production Use Cases</span></div>
  <div class="cp-body">
    

```python
# 1. Invoice parser
class LineItem(BaseModel):
    description: str
    quantity:    int
    unit_price:  float
    total:       float

class Invoice(BaseModel):
    invoice_number: str
    vendor:         str
    line_items:     List[LineItem]
    subtotal:       float
    tax_rate:       float
    total:          float
    due_date:       str   # YYYY-MM-DD

# 2. Meeting notes → action items
class ActionItem(BaseModel):
    task:      str
    owner:     str
    due_date:  Optional[str]
    priority:  Literal["high", "medium", "low"]

class MeetingNotes(BaseModel):
    summary:     str
    decisions:   List[str]
    action_items: List[ActionItem]
    next_meeting: Optional[str]

# 3. Job description parser
class JobDescription(BaseModel):
    role:             str
    company:          str
    location:         str
    salary_min:       Optional[int]
    salary_max:       Optional[int]
    required_skills:  List[str]
    preferred_skills: List[str]
    years_experience: Optional[int]
    remote:           bool

# 4. Support ticket classifier
class SupportTicket(BaseModel):
    category:    Literal["billing", "technical", "account", "general"]
    priority:    Literal["p1", "p2", "p3"]
    sentiment:   Literal["frustrated", "neutral", "positive"]
    summary:     str
    needs_human: bool
```


  </div>
</div>
</div><!-- end t2 -->
<!-- ══════════ TAB 3 — TOOL CALLING ══════════ -->
<div id="t3" class="tab-pane">
<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>Tool Calling — The Mental Model</h3><span class="tag tag-indigo">Critical Concept</span></div>
  <div class="cp-body">
<p>Tool calling is what transforms an LLM from a text generator into something that can <strong>take actions</strong> — search the web, query a database, call your API, run code. Before writing any code, understand what actually happens:</p>
<div class="tool-flow">
<div class="tf-box tf-you">You define tools<br>(JSON schemas)</div>
<div class="tf-arrow">→</div>
<div class="tf-box tf-llm">LLM decides<br>which tool to call</div>
<div class="tf-arrow">→</div>
<div class="tf-box tf-you">LLM returns<br>tool_call object</div>
<div class="tf-arrow">→</div>
<div class="tf-box tf-exec">YOUR code executes<br>the actual function</div>
<div class="tf-arrow">→</div>
<div class="tf-box tf-llm">LLM sees result,<br>generates response</div>
</div>
<div class="warn"><p>⚠️ <strong>The model does NOT execute your functions.</strong> It only returns a structured object saying "I want to call get_weather with city='Mumbai'". Your code reads that object and actually calls the function. This distinction is critical for security — you control what runs.</p></div>
    

```bash
# What a tool call response looks like (Anthropic)
{
    "type": "tool_use",
    "id":   "toolu_01A09q90qw90lq917835lq9",
    "name": "get_weather",
    "input": {
        "city": "Mumbai",
        "units": "celsius"
    }
}
# YOUR code then calls: get_weather(city="Mumbai", units="celsius")
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📝</span><h3>Defining Tools — The 5-Step Pattern</h3><span class="tag tag-blue">Core Pattern</span></div>
  <div class="cp-body">
    

```python
import anthropic
import json

client = anthropic.Anthropic()

# STEP 1: Define your Python functions
def get_weather(city: str, units: str = "celsius") -> dict:
    # In production: call a real weather API
    return {"city": city, "temp": 28, "condition": "sunny", "units": units}

def calculate(expression: str) -> dict:
    try:
        result = eval(expression, {"__builtins__": {}})  # safe eval
        return {"result": result, "expression": expression}
    except Exception as e:
        return {"error": str(e)}

# STEP 2: Describe the tools in JSON Schema
tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a specific city. Use this when the user asks about weather, temperature, or conditions in a location.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city name, e.g. 'Mumbai', 'Delhi', 'Bangalore'"
                },
                "units": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "Temperature unit. Default: celsius"
                }
            },
            "required": ["city"]
        }
    },
    {
        "name": "calculate",
        "description": "Evaluate a mathematical expression. Use this for any arithmetic, percentage, or numeric calculation. Do NOT use this for non-math questions.",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "A valid Python math expression, e.g. '(100 * 1.15) + 50'"
                }
            },
            "required": ["expression"]
        }
    }
]

# STEP 3: Send request with tools
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in Mumbai? Also, what is 15% of 2500?"}]
)

# STEP 4: Execute the tool calls
tool_results = []
for block in response.content:
    if block.type == "tool_use":
        if block.name == "get_weather":
            result = get_weather(**block.input)
        elif block.name == "calculate":
            result = calculate(**block.input)
        tool_results.append({
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": json.dumps(result)
        })

# STEP 5: Send results back to get final response
final_response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    tools=tools,
    messages=[
        {"role": "user",      "content": "What's the weather in Mumbai? Also, 15% of 2500?"},
        {"role": "assistant", "content": response.content},
        {"role": "user",      "content": tool_results}
    ]
)
print(final_response.content[0].text)
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>Writing Tool Descriptions That Work</h3><span class="tag tag-teal">Critical Skill</span></div>
  <div class="cp-body">
<p>The tool description is the model's user manual. A vague description leads to wrong tool selection. Be explicit about <em>when</em> to use the tool, not just <em>what</em> it does.</p>
    

```python
# BAD tool description — vague
{
    "name": "search",
    "description": "Search for information",
    "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}}
}

# GOOD tool description — specific when/what/not
{
    "name": "search_knowledge_base",
    "description": """Search the internal company knowledge base for product documentation,
FAQs, and policy documents. Use this when the user asks about:
- Product features or specifications
- Company policies or procedures
- Troubleshooting steps

Do NOT use this for: general knowledge questions, math calculations,
or anything not related to company products and policies.""",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Natural language search query, e.g. 'How do I reset my password?'"
            },
            "category": {
                "type": "string",
                "enum": ["products", "policies", "support"],
                "description": "Filter results by category. Optional."
            }
        },
        "required": ["query"]
    }
}
```


<ul>
<li><strong>Name</strong> — self-explanatory verb: <code>search_knowledge_base</code> not <code>search</code></li>
<li><strong>Description</strong> — explain WHEN to call (not just what), give examples, and state when NOT to use it</li>
<li><strong>Parameters</strong> — include examples in descriptions: <code>"e.g. 'Mumbai', 'Delhi'"</code></li>
<li><strong>Required vs optional</strong> — mark truly optional params as optional with sensible defaults</li>
</ul>
  </div>
</div>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">⚙️</span><h3>OpenAI Tool Calling</h3><span class="tag tag-orange">Syntax Differences</span></div>
  <div class="cp-body">
    

```python
from openai import OpenAI
client = OpenAI()

# OpenAI uses slightly different field names
tools = [{
    "type": "function",                # required wrapper
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "parameters": {              # "parameters" not "input_schema"
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    }
}]

response = client.chat.completions.create(
    model="gpt-4o",
    tools=tools,
    tool_choice="auto",     # "auto" | "required" | "none" | specific tool
    messages=[{"role": "user", "content": "Weather in Mumbai?"}]
)

# Parse tool calls
message = response.choices[0].message
if message.tool_calls:
    for tool_call in message.tool_calls:
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        # Execute function based on name...
```


  </div>
</div>
</div><!-- end t3 -->
<!-- ══════════ TAB 4 — TOOL LOOP PATTERNS ══════════ -->
<div id="t4" class="tab-pane">
<div class="cp p-indigo">
  <div class="cp-hdr"><span class="ico">🔁</span><h3>The Complete Tool Loop — Production Pattern</h3><span class="tag tag-indigo">Production</span></div>
  <div class="cp-body">
    

```python
import anthropic, json
from typing import Any

client = anthropic.Anthropic()

# Tool registry — maps name → function
TOOL_REGISTRY = {
    "get_weather":    get_weather,
    "calculate":      calculate,
    "search_notes":   search_notes,
}

def run_tool_loop(user_message: str, tools: list, max_turns: int = 10) -> str:
    """Run a complete tool loop until the model produces a final text response."""
    messages = [{"role": "user", "content": user_message}]

    for turn in range(max_turns):
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            tools=tools,
            messages=messages
        )

        # Check stop reason
        if response.stop_reason == "end_turn":
            # Model finished — return text response
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text
            return ""

        if response.stop_reason != "tool_use":
            break   # unexpected stop reason

        # Append assistant message
        messages.append({"role": "assistant", "content": response.content})

        # Execute all tool calls
        tool_results = []
        for block in response.content:
            if block.type != "tool_use":
                continue

            func = TOOL_REGISTRY.get(block.name)
            if func is None:
                result = {"error": f"Unknown tool: {block.name}"}
            else:
                try:
                    result = func(**block.input)
                except Exception as e:
                    result = {"error": str(e), "tool": block.name}

            tool_results.append({
                "type":        "tool_result",
                "tool_use_id": block.id,
                "content":     json.dumps(result)
            })

        messages.append({"role": "user", "content": tool_results})

    return "Max turns reached without final response"

# Usage
answer = run_tool_loop(
    "What's the weather in Mumbai and Delhi? Which city is warmer?",
    tools=tools
)
print(answer)
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚙️</span><h3>tool_choice — Controlling Which Tool Gets Called</h3><span class="tag tag-blue">Control</span></div>
  <div class="cp-body">
    

```python
# Anthropic tool_choice options

# "auto" (default) — model decides whether to use a tool or respond directly
tool_choice={"type": "auto"}

# "any" — model MUST call a tool (useful to force structured extraction)
tool_choice={"type": "any"}

# Specific tool — model MUST call this exact tool
tool_choice={"type": "tool", "name": "extract_invoice"}

# When to use each:
# "auto"     — conversational agents where tool use is optional
# "any"      — when you always need structured output (extraction pipelines)
# specific   — when you know exactly which tool to force (single-purpose endpoints)

# OpenAI equivalents
tool_choice = "auto"       # let model decide
tool_choice = "required"   # must use a tool (= Anthropic "any")
tool_choice = "none"       # never use tools
tool_choice = {"type": "function", "function": {"name": "get_weather"}}  # force specific
```


  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Parallel Tool Calls</h3><span class="tag tag-teal">Performance</span></div>
  <div class="cp-body">
<p>Modern models can call multiple tools in a single turn. This is dramatically faster than sequential calls — instead of 3 round trips to the API, you do 1.</p>
    

```python
# The model may return multiple tool_use blocks in one response
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user",
               "content": "Get weather for Mumbai, Delhi, and Bangalore"}]
)

# response.content may contain 3 tool_use blocks simultaneously
# Execute all of them, then send all results back at once

import asyncio

async def execute_tool_calls_parallel(tool_calls: list) -> list:
    """Execute multiple tool calls concurrently."""
    async def execute_one(block) -> dict:
        func = TOOL_REGISTRY.get(block.name)
        result = await asyncio.to_thread(func, **block.input)
        return {
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": json.dumps(result)
        }
    return await asyncio.gather(*[execute_one(b) for b in tool_calls])
```


<div class="ins"><p>💡 <strong>Parallel tool calls matter for agents.</strong> An agent researching 5 topics simultaneously via search tools is 5× faster than one that searches sequentially. Always process all tool_use blocks in a single response together, not one by one.</p></div>
  </div>
</div>
</div><!-- end t4 -->
<!-- ══════════ TAB 5 — RESOURCES ══════════ -->
<div id="t5" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
<tr><td class="res-type">Docs</td><td><a href="https://platform.openai.com/docs/guides/structured-outputs" target="_blank" rel="noopener">OpenAI Structured Outputs Guide — platform.openai.com</a></td><td>Covers the feature that ensures models always generate responses adhering to your JSON Schema.</td></tr>
<tr><td class="res-type">Library</td><td><a href="https://python.useinstructor.com/" target="_blank" rel="noopener">Instructor library — python.useinstructor.com</a></td><td>The cleanest way to get structured outputs from any LLM provider. Production standard.</td></tr>
<tr><td class="res-type">Docs</td><td><a href="https://platform.openai.com/docs/guides/function-calling" target="_blank" rel="noopener">OpenAI Function Calling Guide — platform.openai.com</a></td><td>Definitive reference for tool calling with OpenAI models.</td></tr>
<tr><td class="res-type">Docs</td><td><a href="https://docs.anthropic.com/en/docs/build-with-claude/tool-use" target="_blank" rel="noopener">Anthropic Tool Use Docs — docs.anthropic.com</a></td><td>Anthropic's complete guide to tool calling with Claude.</td></tr>
<tr><td class="res-type">Notebook</td><td><a href="https://github.com/openai/openai-cookbook/blob/main/examples/How_to_call_functions_with_chat_models.ipynb" target="_blank" rel="noopener">OpenAI Cookbook: How to Call Functions — github.com/openai/openai-cookbook</a></td><td>Complete runnable notebook walking through the full tool-calling loop with real examples.</td></tr>
  </tbody>
</table>
</div><!-- end t5 -->
<!-- ══════════ TAB 6 — PROJECTS ══════════ -->
<div id="t6" class="tab-pane">
<p class="sep">MILESTONE PROJECT</p>
<div class="proj-box">
  <div class="proj-hdr">
<span>🛠</span>
<span class="proj-title">Invoice Parser + 3-Tool Assistant</span>
<span class="proj-dur">[Intermediate] 3–4 days</span>
  </div>
  <div class="proj-body">
<p><strong>Part A — Invoice Parser:</strong> Use Instructor to extract structured data from raw invoice text.</p>
<ul>
<li>Define a full Invoice Pydantic model: invoice_number, vendor, line_items (list), subtotal, tax_rate, total, due_date</li>
<li>Test on 5 different invoice text formats (different layouts, missing fields, different currencies)</li>
<li>Add field validators: total must equal subtotal * (1 + tax_rate), due_date must be valid ISO date</li>
<li>Observe Instructor's automatic retry behaviour when validation fails</li>
</ul>
<p><strong>Part B — 3-Tool Assistant:</strong> Build a conversational assistant with three callable tools.</p>
<ul>
<li><code>get_weather(city)</code> — calls Open-Meteo API (no key needed)</li>
<li><code>calculate(expression)</code> — evaluates math expressions safely</li>
<li><code>search_notes(query)</code> — searches a hardcoded dict of notes by keyword</li>
<li>Implement the full 5-step tool loop with parallel execution</li>
<li>Test with: "What's the weather in Mumbai?", "What is 15% of 8500?", "Find notes about Python", "What's the weather in Delhi and Mumbai, and which is warmer?" (parallel)</li>
</ul>
<p><strong>Skills:</strong> Pydantic, Instructor, field validators, Anthropic/OpenAI SDK, tool calling loop, parallel tool execution</p>
  </div>
</div>
</div><!-- end t6 -->
<!-- ══════════ TAB 7 — LABS ══════════ -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Structured Extraction — Compare JSON Mode vs Instructor</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Directly observe what structured outputs guarantee vs what JSON mode does not.</p>
<div class="lab-step"><div class="sn">1</div><div>Build a Contact extractor: name (str), email (str), phone (Optional[str]), company (Optional[str]). Use the same 10 test inputs: some with all fields, some with missing fields, one with malformed email, one with phone in different formats.</div></div>
<div class="lab-step"><div class="sn">2</div><div><strong>Version A:</strong> JSON mode only — parse the response text with json.loads(). Run all 10 inputs. Count: how many parsed successfully? How many had wrong types? How many were missing required fields?</div></div>
<div class="lab-step"><div class="sn">3</div><div><strong>Version B:</strong> Instructor with Pydantic model. Run the same 10 inputs. Count the same metrics. Compare.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Add a validator that normalises phone numbers to E.164 format (+91XXXXXXXXXX). Watch Instructor retry when the model returns "9876543210" (not E.164). Count how many retries occurred across all 10 inputs.</div></div>
<div class="lab-step"><div class="sn">5</div><div><strong>Document:</strong> What failure modes did JSON mode have that Instructor caught? When is JSON mode "good enough"?</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Tool Description Quality — See How It Affects Selection</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Empirically measure how tool description quality affects which tool the model selects.</p>
<div class="lab-step"><div class="sn">1</div><div>Create 3 tools: get_weather, search_docs, calculate. Write <strong>Version A</strong> with minimal descriptions (just the tool name and one line).</div></div>
<div class="lab-step"><div class="sn">2</div><div>Test 10 ambiguous messages that could fit multiple tools: "How much is 28 degrees in Fahrenheit?", "Find information about temperature limits in the docs", "What is the current temperature in Mumbai?" Record which tool was selected each time.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Write <strong>Version B</strong> with full descriptions including "Use when:", "Do NOT use when:", examples in parameter descriptions. Run the same 10 messages.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Compare selections. How many changed? Which changes were improvements? Document the 3 most impactful improvements you made to descriptions.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Build and Test the Complete Tool Loop</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Build the complete production tool loop and test every edge case.</p>
<div class="lab-step"><div class="sn">1</div><div>Implement the <code>run_tool_loop()</code> function from Tab 4 with the 3 tools (weather, calculate, search_notes).</div></div>
<div class="lab-step"><div class="sn">2</div><div>Test happy path: "What's 20% tip on a ₹2400 bill?" — should call calculate and return a clear answer.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Test no-tool path: "What is the capital of France?" — model should answer directly without calling any tool. Verify stop_reason == "end_turn" on the first turn.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Test parallel calls: "What is the weather in Mumbai, Delhi, and Bangalore?" — should trigger 3 simultaneous tool_use blocks in one response. Verify all 3 are executed before the next API call.</div></div>
<div class="lab-step"><div class="sn">5</div><div>Test error handling: make get_weather() raise an exception for "InvalidCity". Does the model gracefully handle the error in the tool_result? What does it tell the user?</div></div>
<div class="lab-step"><div class="sn">6</div><div>Test max_turns: give the model a tool that always returns "try again" and verify the loop terminates at max_turns rather than running forever.</div></div>
  </div>
</div>
</div><!-- end t7 -->
<!-- ══════════ TAB 8 — CHECKLIST ══════════ -->
<div id="t8" class="tab-pane">
<p class="sep">P4-M12 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain the difference between JSON mode and structured outputs — and when each is appropriate</li>
  <li>Can define a Pydantic model with nested objects, enums, Optional fields, and List fields</li>
  <li>Can use Instructor with both Anthropic and OpenAI clients using the same Pydantic model</li>
  <li>Can add field validators to Pydantic models and understand how Instructor handles validation failures</li>
  <li>Understand the tool calling mental model: the model does NOT execute functions — it returns structured call objects</li>
  <li>Can write a tool definition with a description that clearly states when to use and when not to use it</li>
  <li>Can implement the complete 5-step tool calling loop for Anthropic (Claude)</li>
  <li>Can implement the equivalent for OpenAI (note the different field names)</li>
  <li>Know what tool_choice options exist and when to use "auto" vs "any" vs specific tool</li>
  <li>Can handle parallel tool calls — processing all tool_use blocks before the next API call</li>
  <li>Can implement a production tool loop with max_turns, error handling, and tool registry</li>
  <li>Know that better tool descriptions (with when/when-not-to examples) produce more reliable tool selection</li>
  <li>Completed Lab 1: JSON mode vs Instructor comparison</li>
  <li>Completed Lab 2: tool description quality experiment</li>
  <li>Completed Lab 3: complete tool loop with all edge cases tested</li>
  <li>Milestone project pushed to GitHub with README</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P4-M13 — Streaming &amp; Conversation State</strong>. The tool calling patterns you built here are the foundation of agents in Part 6 — agents are just tool loops with more sophisticated decision logic.</p>
</div>
</div><!-- end t8 -->
<!-- ── MODULE NAV ── -->
<div class="mod-nav">
  <a href="/learning/ai-ml/part4-llm-apis/p4-m11-prompting/">← P4-M11: Prompting</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part4-llm-apis/p4-m13-streaming-state/">Next: P4-M13 — Streaming →</a>
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
    const key = 'p4m12-ck-' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
