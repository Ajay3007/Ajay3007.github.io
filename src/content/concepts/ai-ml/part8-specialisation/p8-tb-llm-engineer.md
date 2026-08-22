---
title: "Track B - Applied ML / LLM Engineer"
description: "Part 8 — Specialisation · Track B of 4 Track B — Applied ML / LLM Engineer Fine-tune models, build rigorous evals, and work at the model layer ⏱ 2–3 Weeks 🔴 Advanced 🔧…"
domain: ai-ml
track: ai-ml-engineering
module: part8-specialisation
order: 99
ownHeader: true
url: /learning/ai-ml/part8-specialisation/p8-tb-llm-engineer/
---

<style>
.mod-header{background:linear-gradient(135deg,#0f0a1e 0%,#1a0808 40%,#7f1d1d 70%,#dc2626 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:rgba(255,255,255,.8);text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:rgba(255,255,255,.88);font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:rgba(255,255,255,.9)}
.tab-bar{display:flex;flex-wrap:wrap;background:#1a0808;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:rgba(255,255,255,.55);background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#f87171;border-bottom-color:#f87171}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee);background:#fee2e2}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700;background:#fee2e2;color:#991b1b}
.cp-body{padding:1.1rem 1.2rem}
.cp-body p,.cp-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.cp-body ul{margin:.4rem 0;padding-left:1.4rem}
.cp-body li{margin-bottom:.3rem}
.cp-body h4{font-size:.9rem;font-weight:700;margin:.9rem 0 .3rem}
.cb{background:#1a0808;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #dc2626}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:rgba(255,255,255,.88);white-space:pre}
.ins{background:#fee2e2;border:1.5px solid #dc2626;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.sep{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--light-text,#888);border-bottom:1px solid var(--border-color,#e4e4e4);padding-bottom:.4rem;margin:2rem 0 1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin:2.5rem 0 1rem;padding-top:1.2rem;border-top:1.5px solid var(--border-color,#e4e4e4)}
.mod-nav a{font-size:.85rem;font-weight:600;color:#dc2626;text-decoration:none;padding:.4rem .9rem;border-radius:6px;border:1.5px solid #dc2626;transition:all .15s}
.mod-nav a:hover{background:#dc2626;color:#fff}
.mod-nav .nb{background:#dc2626;color:#fff}
.proj-box{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;overflow:hidden;margin:1.2rem 0}
.proj-hdr{background:#dc2626;color:#fff;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem;flex-wrap:wrap}
.proj-title{font-weight:700;font-size:.92rem}
.proj-dur{font-size:.78rem;opacity:.85;margin-left:auto;font-family:monospace}
.proj-body{padding:.9rem 1.2rem;font-size:.88rem;line-height:1.7}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem 0;border-bottom:1px solid var(--border-color,#eee);font-size:.88rem;line-height:1.6;cursor:pointer}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";font-size:1rem;flex-shrink:0;margin-top:.05rem;color:#dc2626}
.cl li.done::before{content:"☑";color:#059669}
.cl li.done{color:var(--light-text,#888);text-decoration:line-through}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">Part 8 — Specialisation &nbsp;·&nbsp; Track B of 4</div>
  <div class="mod-title">Track B — Applied ML / LLM Engineer</div>
  <div class="mod-subtitle">Fine-tune models, build rigorous evals, and work at the model layer</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 2–3 Weeks</span>
    <span class="mod-pill">🔴 Advanced</span>
    <span class="mod-pill">🔧 Unsloth · HuggingFace · PEFT · vLLM</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🤗 HuggingFace</button>
  <button class="tab-btn" onclick="vt(event,'t2')">⚡ Fine-tuning</button>
  <button class="tab-btn" onclick="vt(event,'t3')">📊 PEFT & LoRA</button>
  <button class="tab-btn" onclick="vt(event,'t4')">🚀 vLLM Serving</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🛠 Capstone</button>
  <button class="tab-btn" onclick="vt(event,'t6')">✅ Checklist</button>
</div>


<div id="t0" class="tab-pane active">
<div class="cp">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>Track Overview</h3><span class="tag">Specialisation B</span></div>
  <div class="cp-body">
    <p>Go deep on the model layer: fine-tuning open-source LLMs, building rigorous eval frameworks, and serving models in production. This track is for engineers who want to work at AI labs, research teams, or companies that run their own models rather than using third-party APIs.</p>
    <h4>Skills You Will Build</h4>
    <ul>
      <li>HuggingFace ecosystem: datasets, transformers, hub, evaluate</li>
      <li>QLoRA fine-tuning with Unsloth — 2x faster, 70% less VRAM</li>
      <li>PEFT LoRA — train 0.1% of parameters, get 80% of the quality gain</li>
      <li>vLLM for high-throughput PagedAttention-based model serving</li>
      <li>GGUF quantisation for local CPU deployment with llama.cpp</li>
      <li>Rigorous LLM evaluation: domain accuracy, fluency, cost comparison</li>
    </ul>
  </div>
</div>
</div>


<div id="t1" class="tab-pane">
<div class="cp">
  <div class="cp-hdr"><span class="ico">🤗</span><h3>HuggingFace Ecosystem</h3><span class="tag">Infrastructure</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install transformers datasets huggingface_hub accelerate evaluate trl
 
from datasets import load_dataset, Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
 
# Load any open-source model
model_id = "meta-llama/Llama-3.2-3B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype="auto", device_map="auto"
)
 
# Inference pipeline
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
result = pipe("Explain DPDK mempool:", max_new_tokens=200)
print(result[0]["generated_text"])
 
# Build a fine-tuning dataset from domain text
training_data = [
    {"prompt": "What is DPDK?",
     "completion": "DPDK is a set of libraries and drivers for fast packet processing..."},
    {"prompt": "How does rte_ring work?",
     "completion": "rte_ring is a lock-free FIFO queue implementation in DPDK..."},
    # ... 100-1000 examples
]
 
# Format for instruction fine-tuning (Llama chat template)
def format_prompt(example):
    return {"text": f"&lt;|user|&gt;\n{example['prompt']}&lt;|assistant|&gt;\n{example['completion']}"}
 
dataset = Dataset.from_list(training_data).map(format_prompt)
dataset.push_to_hub("your-username/domain-qa-dataset")</pre></div>
  </div>
</div>
</div>


<div id="t2" class="tab-pane">
<div class="cp">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Fine-tuning with Unsloth QLoRA</h3><span class="tag">Core Skill</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install unsloth
 
from unsloth import FastLanguageModel
import torch
 
# Load model in 4-bit quantised form — fits in 8GB VRAM
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/llama-3.2-3b-instruct-bnb-4bit",
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True,
)
 
# Add LoRA adapters — only 0.1% of parameters are trainable
model = FastLanguageModel.get_peft_model(
    model,
    r=16,              # LoRA rank — higher = more capacity, more params
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0,
    bias="none",
    use_gradient_checkpointing=True,
)
model.print_trainable_parameters()
# trainable params: 41,943,040 || all params: 3,254,702,080 || 1.29%
 
# Training with SFTTrainer (TRL library)
from trl import SFTTrainer
from transformers import TrainingArguments
 
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=formatted_dataset,
    dataset_text_field="text",
    max_seq_length=2048,
    args=TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        num_train_epochs=3,
        learning_rate=2e-4,
        fp16=not torch.cuda.is_bf16_supported(),
        bf16=torch.cuda.is_bf16_supported(),
        logging_steps=10,
        output_dir="./output",
    ),
)
trainer.train()
 
# Save LoRA adapter and push to hub
model.save_pretrained("lora_adapter")
model.push_to_hub("your-username/domain-llama-lora")
 
# Merge adapter into base model for standalone deployment
merged = model.merge_and_unload()
merged.save_pretrained("merged_model")</pre></div>
  </div>
</div>
</div>


<div id="t3" class="tab-pane">
<div class="cp">
  <div class="cp-hdr"><span class="ico">📊</span><h3>PEFT & LoRA — The Math That Matters</h3><span class="tag">Concepts</span></div>
  <div class="cp-body">
    <p>LoRA adds small trainable matrices to frozen model weights. Instead of training W (d x d, billions of params), you train A (d x r) and B (r x d) where r is typically 8-64. The effective weight update is A times B, which is added to the frozen W.</p>
    <div class="cb"><pre># LoRA: W_update = A x B, where rank r &lt;&lt; d
# At r=16 on a 7B model: 0.1% of parameters trained
# Quality: typically 80-95% of full fine-tune quality at 1% the cost
 
from peft import LoraConfig, get_peft_model, TaskType
 
# Manual PEFT config (without Unsloth)
config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,
    lora_alpha=32,           # scaling factor — usually 2x r
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
)
peft_model = get_peft_model(base_model, config)
peft_model.print_trainable_parameters()
 
# Convert to GGUF for local CPU deployment (llama.cpp)
# 1. Save merged model:  merged.save_pretrained("merged")
# 2. Convert: python llama.cpp/convert_hf_to_gguf.py merged --outfile model.gguf
# 3. Quantise: ./llama.cpp/quantize model.gguf model.q4_k_m.gguf Q4_K_M
# 4. Run: ./llama.cpp/main -m model.q4_k_m.gguf -p "What is DPDK?"
 
# Quantisation comparison:
# Q8_0:   ~8GB,  highest quality local
# Q4_K_M: ~4GB,  good quality/size balance — recommended default
# Q3_K_M: ~3GB,  noticeable quality drop
# Q2_K:   ~2GB,  significant quality loss, emergency only</pre></div>
  </div>
</div>
</div>


<div id="t4" class="tab-pane">
<div class="cp">
  <div class="cp-hdr"><span class="ico">🚀</span><h3>vLLM — Production Model Serving</h3><span class="tag">Serving</span></div>
  <div class="cp-body">
    <div class="cb"><pre>pip install vllm
 
# Start server (OpenAI-compatible API)
# vllm serve your-username/domain-llama --port 8000 --max-model-len 4096
 
# Python client — same as OpenAI API
from openai import OpenAI
 
client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")
response = client.chat.completions.create(
    model="your-username/domain-llama",
    messages=[{"role": "user", "content": "How does rte_mempool_create work?"}],
    max_tokens=512
)
print(response.choices[0].message.content)
 
# vLLM advantages over transformers.generate():
# - PagedAttention: manages KV cache in pages, 3-5x higher throughput
# - Continuous batching: batches requests dynamically, no padding waste
# - CUDA kernels: fused attention, faster than naive PyTorch
# - OpenAI-compatible: drop-in replacement for OpenAI API calls
 
# Benchmark your fine-tuned model vs base model vs Claude-3-Haiku
import anthropic, time
 
def eval_model(questions: list[str], answers: list[str]) -> dict:
    """Compare fine-tuned vs base vs Claude on domain Q&A."""
    results = {"fine_tuned": [], "base": [], "claude": []}
 
    for q, expected in zip(questions, answers):
        # Fine-tuned (via vLLM)
        ft_resp = client.chat.completions.create(
            model="fine-tuned", messages=[{"role":"user","content":q}], max_tokens=256
        )
        # Claude as baseline
        cl_resp = anthropic.Anthropic().messages.create(
            model="claude-3-haiku-20240307", max_tokens=256,
            messages=[{"role":"user","content":q}]
        )
        # Score both with LLM judge
        ft_score = judge_answer(q, expected, ft_resp.choices[0].message.content)
        cl_score = judge_answer(q, expected, cl_resp.content[0].text)
        results["fine_tuned"].append(ft_score)
        results["claude"].append(cl_score)
 
    return {k: sum(v)/len(v) for k, v in results.items()}</pre></div>
  </div>
</div>
</div>


<div id="t5" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr">
    <span>🛠</span>
    <span class="proj-title">Capstone: Domain Fine-Tuned Model with Evaluation Report</span>
    <span class="proj-dur">2–3 weeks</span>
  </div>
  <div class="proj-body">
    <p>Fine-tune a 3B parameter open-source model on a domain-specific dataset from your professional area (DPDK documentation, network engineering, telecom). Evaluate it rigorously and serve it in production.</p>
    <h4>Requirements</h4>
    <ul>
      <li>Build a dataset of 200+ Q&A pairs from your domain</li>
      <li>Fine-tune using Unsloth QLoRA on Google Colab T4 (free) or local GPU</li>
      <li>Serve the merged model with vLLM on a $5/mo cloud VM</li>
      <li>Evaluation report on 50 domain questions: fine-tuned vs base model vs Claude-3-Haiku</li>
      <li>Metrics: accuracy (LLM-judged), latency, cost per query</li>
      <li>GGUF version for local deployment — verify it runs on CPU</li>
    </ul>
    <p>Push dataset, training code, evaluation results, and model to HuggingFace Hub.</p>
  </div>
</div>
</div>


<div id="t6" class="tab-pane">
<p class="sep">MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can load any HuggingFace model and run inference with the pipeline API</li>
  <li>Can build a formatted instruction fine-tuning dataset and push to HuggingFace Hub</li>
  <li>Can fine-tune a 3B model with Unsloth QLoRA in 4-bit on a single GPU</li>
  <li>Can explain LoRA: low-rank matrices A and B trained, 0.1% of parameters</li>
  <li>Can merge LoRA adapters into base model: merge_and_unload() then save</li>
  <li>Can convert a merged model to GGUF and quantise to Q4_K_M</li>
  <li>Can serve a fine-tuned model with vLLM: OpenAI-compatible API on port 8000</li>
  <li>Can build an eval harness comparing fine-tuned vs base model vs Claude on 50 questions</li>
  <li>Capstone: evaluation report showing improvement on domain questions published to GitHub</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>When complete: move to <strong>Part 9 — Portfolio and Launch</strong>.</p>
</div>
</div>


<div class="mod-nav">
  <a href="/learning/ai-ml/part8-specialisation/p8-ta-ai-product-engineer/">← Track A: AI Product</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">All Modules</a>
  <a class="nb" href="/learning/ai-ml/part8-specialisation/p8-tc-automation-engineer/">Next: Track C — Automation →</a>
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
    const key = 'p8tb_ck_' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
