---
title: "P2-M05 - Statistics, EDA & Visualisation"
description: "Part 2 — Statistics, EDA Visualisation · Module 5 of 28 Statistics, EDA Visualisation Understand your data before modelling it — distributions, correlations, and visual…"
domain: ai-ml
track: ai-ml-engineering
module: part2-stats-eda
order: 205
url: /learning/ai-ml/part2-stats-eda/p2-m05-stats-viz/
---

<style>
.mod-header{background:linear-gradient(135deg,#0f0a1e 0%,#0c1830 40%,#1a3a5f 70%,#ec4899 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#f9a8d4;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#fce7f3;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#fce7f3}
.tab-bar{display:flex;flex-wrap:wrap;background:#0c1830;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#f9a8d4;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#f472b6;border-bottom-color:#f472b6}
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
.p-pink .cp-hdr{background:#fdf2f8}[data-theme=dark] .p-pink .cp-hdr{background:#1e0a18}
.p-blue .cp-hdr{background:#eff6ff}[data-theme=dark] .p-blue .cp-hdr{background:#0c1a40}
.p-teal .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal .cp-hdr{background:#0a2420}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.p-red .cp-hdr{background:#faeaea}[data-theme=dark] .p-red .cp-hdr{background:#2a0808}
.tag-pink{background:#fce7f3;color:#9d174d}.tag-blue{background:#dbeafe;color:#1e40af}
.tag-teal{background:#c8e8e4;color:#0e5248}.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}.tag-red{background:#f4d0d0;color:#6c1a1a}
.cb{background:#0c1830;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #ec4899}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#fce7f3;white-space:pre}
.ck{color:#f9a8d4}.cv{color:#f0c080}.cs{color:#86efac}
.ins{background:#fdf2f8;border:1.5px solid #ec4899;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#1e0a18;border-color:#ec4899}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.res-table{width:100%;border-collapse:collapse;margin:1rem 0;font-size:.84rem}
.res-table th{background:#4a5568;color:#fff;padding:.6rem .9rem;text-align:left;font-weight:600;font-size:.74rem;text-transform:uppercase;letter-spacing:.06em}
.res-table td{padding:.6rem .9rem;border:1px solid var(--border-color,#e4e4e4);vertical-align:top}
.res-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.res-table a{color:#9d174d;font-weight:500;text-decoration:none}
.res-table a:hover{text-decoration:underline}
.res-type{font-family:monospace;font-size:.74rem;font-weight:700;color:#4a5568}
.lab-box{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;margin:1.2rem 0;overflow:hidden}
.lab-hdr{background:#0c1830;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-n{background:#ec4899;color:#fff;font-size:.72rem;font-family:monospace;font-weight:700;padding:2px 10px;border-radius:12px}
.lab-hdr h4{margin:0;font-size:.95rem;font-weight:700;color:#fce7f3;border:none}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.8rem;font-size:.88rem;line-height:1.65}
.sn{background:#ec4899;color:#fff;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem 0;border-bottom:1px solid var(--border-color,#eee);font-size:.88rem;line-height:1.6;cursor:pointer}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";font-size:1rem;flex-shrink:0;margin-top:.05rem;color:#ec4899}
.cl li.done::before{content:"☑";color:#059669}
.cl li.done{color:var(--light-text,#888);text-decoration:line-through}
.sep{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--light-text,#888);border-bottom:1px solid var(--border-color,#e4e4e4);padding-bottom:.4rem;margin:2rem 0 1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin:2.5rem 0 1rem;padding-top:1.2rem;border-top:1.5px solid var(--border-color,#e4e4e4)}
.mod-nav a{font-size:.85rem;font-weight:600;color:#9d174d;text-decoration:none;padding:.4rem .9rem;border-radius:6px;border:1.5px solid #9d174d;transition:all .15s}
.mod-nav a:hover{background:#9d174d;color:#fff}
.mod-nav .nb{background:#9d174d;color:#fff}
.proj-box{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;overflow:hidden;margin:1.2rem 0}
.proj-hdr{background:#9d174d;color:#fff;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem;flex-wrap:wrap}
.proj-title{font-weight:700;font-size:.92rem}
.proj-dur{font-size:.78rem;opacity:.85;margin-left:auto;font-family:monospace}
.proj-body{padding:.9rem 1.2rem;font-size:.88rem;line-height:1.7}
.viz-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:.7rem;margin:.8rem 0}
.viz-card{border:1.5px solid var(--border-color,#e4e4e4);border-radius:8px;padding:.7rem;background:var(--card-bg,#fff)}
.viz-card h5{margin:0 0 .3rem;font-size:.83rem;font-weight:700;color:var(--text-color,#111)}
.viz-card p{margin:0;font-size:.79rem;line-height:1.5;color:var(--text-color,#555)}
.viz-when{font-size:.7rem;font-family:monospace;color:#9d174d;font-weight:700;margin-top:.3rem}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">Part 2 — Statistics, EDA &amp; Visualisation &nbsp;·&nbsp; Module 5 of 28</div>
  <div class="mod-title">Statistics, EDA &amp; Visualisation</div>
  <div class="mod-subtitle">Understand your data before modelling it — distributions, correlations, and visual storytelling</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 2 Weeks</span>
    <span class="mod-pill">🟡 Intermediate</span>
    <span class="mod-pill">🔧 matplotlib · seaborn · scipy · pandas</span>
    <span class="mod-pill">📋 Prerequisite: P1-M02</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">📊 Descriptive Stats</button>
  <button class="tab-btn" onclick="vt(event,'t2')">📈 Distributions</button>
  <button class="tab-btn" onclick="vt(event,'t3')">🔗 Correlations</button>
  <button class="tab-btn" onclick="vt(event,'t4')">🎨 Visualisation</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🔍 EDA Workflow</button>
  <button class="tab-btn" onclick="vt(event,'t6')">🚨 Outliers</button>
  <button class="tab-btn" onclick="vt(event,'t7')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t9')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t10')">✅ Checklist</button>
</div>

<div id="t0" class="tab-pane active">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-pink">Part 2 Start</span></div>
  <div class="cp-body">
    <p>Before building any model, you must understand your data. EDA (Exploratory Data Analysis) is the process of summarising, visualising, and questioning a dataset to find patterns, anomalies, and relationships. Skipping EDA is the most common cause of bad ML models.</p>
    <ul>
      <li><strong>Descriptive statistics</strong> — mean, median, mode, variance, std, percentiles, IQR</li>
      <li><strong>Distributions</strong> — normal, skewed, bimodal; what shape tells you about transformations</li>
      <li><strong>Correlation analysis</strong> — Pearson, Spearman, heatmaps, scatter matrix, multicollinearity</li>
      <li><strong>Visualisation toolkit</strong> — choosing the right plot for each question and data type</li>
      <li><strong>Full EDA workflow</strong> — from raw CSV to insight report in a systematic process</li>
      <li><strong>Outlier detection</strong> — Z-score, IQR method, Isolation Forest; treatment strategies</li>
    </ul>
    <div class="ins"><p>💡 <strong>EDA answers "what is the data?" before you ask "what should the model predict?"</strong> The most valuable EDA insight is often unexpected: a corrupted column, a leaky feature, or a distributional shift that invalidates your entire modelling approach. One hour of EDA saves ten hours of debugging a bad model.</p></div>
  </div>
</div>
</div>

<div id="t1" class="tab-pane">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Descriptive Statistics — The Complete Toolkit</h3><span class="tag tag-pink">Foundation</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv(<span class="cs">"house_prices.csv"</span>)

<span class="ck"># ── Phase 1: First Pass ────────────────────────────────</span>
print(df.shape)               <span class="ck"># (1460, 81) → rows, columns</span>
print(df.dtypes.value_counts()) <span class="ck"># how many numeric vs object cols</span>
print(df.isnull().sum().sort_values(ascending=<span class="cv">False</span>)[:10])
print(df.nunique().sort_values())   <span class="ck"># columns with few unique = likely categorical</span>

<span class="ck"># ── Phase 2: Summary Statistics ───────────────────────</span>
df.describe()         <span class="ck"># count, mean, std, min, 25%, 50%, 75%, max</span>
df.describe(include=<span class="cs">"all"</span>)  <span class="ck"># also shows top/freq for object cols</span>

<span class="ck"># ── Phase 3: Individual column statistics ─────────────</span>
col = df[<span class="cs">"SalePrice"</span>]

mean   = col.mean()       <span class="ck"># arithmetic mean — sensitive to outliers</span>
median = col.median()     <span class="ck"># middle value — robust to outliers</span>
mode   = col.mode()[<span class="cv">0</span>]   <span class="ck"># most frequent value</span>
std    = col.std()        <span class="ck"># standard deviation</span>
var    = col.var()        <span class="ck"># variance = std²</span>
q1     = col.quantile(<span class="cv">0.25</span>)
q3     = col.quantile(<span class="cv">0.75</span>)
iqr    = q3 - q1         <span class="ck"># interquartile range</span>
cv     = std / mean       <span class="ck"># coefficient of variation (relative spread)</span>

print(<span class="cs">f"Mean: {mean:,.0f}  Median: {median:,.0f}  Diff: {mean-median:,.0f}"</span>)
print(<span class="cs">f"IQR: {iqr:,.0f}  CV: {cv:.3f}"</span>)

<span class="ck"># ── Phase 4: Shape statistics ─────────────────────────</span>
skewness = col.skew()           <span class="ck"># 0=symmetric, >0=right tail, <0=left tail</span>
kurtosis = col.kurtosis()       <span class="ck"># 0=normal tails, >0=heavy tails</span>
print(<span class="cs">f"Skewness: {skewness:.3f}  Kurtosis: {kurtosis:.3f}"</span>)

<span class="ck"># ── Phase 5: Value counts for categoricals ────────────</span>
print(df[<span class="cs">"Neighborhood"</span>].value_counts())
print(df[<span class="cs">"Neighborhood"</span>].value_counts(normalize=<span class="cv">True</span>).round(<span class="cv">3</span>))

<span class="ck"># ── Automation: stats for ALL numeric columns ─────────</span>
numeric_cols = df.select_dtypes(<span class="cs">"number"</span>).columns
stats_df = df[numeric_cols].agg([<span class="cs">"mean"</span>, <span class="cs">"median"</span>, <span class="cs">"std"</span>,
    lambda x: x.skew(), lambda x: x.isnull().mean()]).T
stats_df.columns = [<span class="cs">"mean"</span>, <span class="cs">"median"</span>, <span class="cs">"std"</span>, <span class="cs">"skewness"</span>, <span class="cs">"null_pct"</span>]
print(stats_df.sort_values(<span class="cs">"skewness"</span>, ascending=<span class="cv">False</span>).head(<span class="cv">10</span>))</pre></div>
    <div class="ins"><p>💡 <strong>Mean vs Median tells you about skew.</strong> If mean &gt; median, the distribution has a right tail (outliers pulling the mean up). For house prices: mean=$180k, median=$163k — a few luxury homes inflate the mean. The median is more representative of the "typical" house. Always report both for financial or demographic data.</p></div>
  </div>
</div>
</div>

<div id="t2" class="tab-pane">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">📈</span><h3>Distributions — Shape Tells You Everything</h3><span class="tag tag-pink">Core Concept</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

<span class="ck"># ── Visualise distribution ────────────────────────────</span>
fig, axes = plt.subplots(<span class="cv">1</span>, <span class="cv">3</span>, figsize=(<span class="cv">15</span>, <span class="cv">4</span>))

<span class="ck"># Histogram + KDE</span>
sns.histplot(df[<span class="cs">"SalePrice"</span>], bins=<span class="cv">40</span>, kde=<span class="cv">True</span>, ax=axes[<span class="cv">0</span>])
axes[<span class="cv">0</span>].set_title(<span class="cs">f"SalePrice (skew={df['SalePrice'].skew():.2f})"</span>)

<span class="ck"># QQ-plot: if points lie on diagonal line → normal distribution</span>
stats.probplot(df[<span class="cs">"SalePrice"</span>].dropna(), plot=axes[<span class="cv">1</span>])
axes[<span class="cv">1</span>].set_title(<span class="cs">"QQ-Plot: Deviation from Normal"</span>)

<span class="ck"># Log transform: right-skewed → more symmetric</span>
log_price = np.log1p(df[<span class="cs">"SalePrice"</span>])
sns.histplot(log_price, bins=<span class="cv">40</span>, kde=<span class="cv">True</span>, ax=axes[<span class="cv">2</span>])
axes[<span class="cv">2</span>].set_title(<span class="cs">f"log(SalePrice) (skew={log_price.skew():.2f})"</span>)
plt.tight_layout()

<span class="ck"># ── Formal normality test ─────────────────────────────</span>
<span class="ck"># H0: data is normally distributed. p > 0.05 = fail to reject</span>
stat, p = stats.shapiro(df[<span class="cs">"SalePrice"</span>].dropna().sample(<span class="cv">500</span>, random_state=<span class="cv">42</span>))
print(<span class="cs">f"Shapiro-Wilk: stat={stat:.4f}, p={p:.6f}"</span>)
<span class="ck"># Very small p → strongly non-normal (expected for house prices)</span>

<span class="ck"># ── Box-Cox optimal transformation ───────────────────</span>
<span class="ck"># lambda ~0 = log, ~0.5 = sqrt, ~1 = no transform</span>
pos = df[<span class="cs">"SalePrice"</span>].dropna()
transformed, lam = stats.boxcox(pos)
print(<span class="cs">f"Optimal lambda: {lam:.3f} → "
      f"{'log' if abs(lam) < 0.1 else 'sqrt' if abs(lam-0.5) < 0.1 else f'x^{lam:.2f}'}"</span>)

<span class="ck"># ── Find all highly skewed columns ────────────────────</span>
skewed = df.select_dtypes(<span class="cs">"number"</span>).skew().sort_values(ascending=<span class="cv">False</span>)
high_skew = skewed[abs(skewed) > <span class="cv">1</span>]
print(<span class="cs">f"{len(high_skew)} columns with |skewness| > 1"</span>)
print(high_skew.head(<span class="cv">10</span>))</pre></div>
    <h4>Distribution Types and Actions</h4>
    <div class="viz-grid">
      <div class="viz-card"><h5>Normal</h5><p>Symmetric bell. Mean=median. 68-95-99.7 rule. Heights, errors.</p><div class="viz-when">✅ No transform needed</div></div>
      <div class="viz-card"><h5>Right-Skewed</h5><p>Long right tail, mean &gt; median. Prices, salaries, counts.</p><div class="viz-when">→ Apply log1p or Box-Cox</div></div>
      <div class="viz-card"><h5>Left-Skewed</h5><p>Long left tail, mean &lt; median. Test scores near maximum.</p><div class="viz-when">→ Apply square or reflect</div></div>
      <div class="viz-card"><h5>Bimodal</h5><p>Two peaks = two subpopulations. Always investigate before modelling.</p><div class="viz-when">⚠ Segment the data</div></div>
      <div class="viz-card"><h5>Zero-Inflated</h5><p>Many zeros + positive tail. Spend, transaction amount, counts.</p><div class="viz-when">→ log1p or separate zero/nonzero</div></div>
      <div class="viz-card"><h5>Uniform</h5><p>Flat. All values equally likely. IDs, random numbers. Often useless as a feature.</p><div class="viz-when">⚠ Check if meaningful</div></div>
    </div>
  </div>
</div>
</div>

<div id="t3" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Correlation Analysis — Finding Feature Relationships</h3><span class="tag tag-blue">Feature Selection</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

<span class="ck"># ── Pearson correlation ───────────────────────────────</span>
<span class="ck"># Measures LINEAR relationship. Assumes both variables are continuous.</span>
<span class="ck"># Range: -1 (perfect negative) to +1 (perfect positive)</span>
<span class="ck"># Sensitive to outliers. Assumes roughly normal distributions.</span>

corr = df.corr(numeric_only=<span class="cv">True</span>)

<span class="ck"># Most correlated with target</span>
target_corr = corr[<span class="cs">"SalePrice"</span>].drop(<span class="cs">"SalePrice"</span>).sort_values(ascending=<span class="cv">False</span>)
print(<span class="cs">"Top 10 positive correlations:"</span>)
print(target_corr.head(<span class="cv">10</span>))
print(<span class="cs">"\nTop 5 negative correlations:"</span>)
print(target_corr.tail(<span class="cv">5</span>))

<span class="ck"># Heatmap of top correlated features</span>
top_feats = target_corr.abs().nlargest(<span class="cv">12</span>).index.tolist() + [<span class="cs">"SalePrice"</span>]
plt.figure(figsize=(<span class="cv">10</span>, <span class="cv">8</span>))
sns.heatmap(df[top_feats].corr(), annot=<span class="cv">True</span>, fmt=<span class="cs">".2f"</span>,
            cmap=<span class="cs">"RdBu_r"</span>, center=<span class="cv">0</span>, vmin=-<span class="cv">1</span>, vmax=<span class="cv">1</span>, square=<span class="cv">True</span>)
plt.title(<span class="cs">"Top Features — Correlation Matrix"</span>)
plt.tight_layout()

<span class="ck"># ── Pearson statistical significance ─────────────────</span>
r, p = stats.pearsonr(df[<span class="cs">"GrLivArea"</span>], df[<span class="cs">"SalePrice"</span>])
print(<span class="cs">f"GrLivArea vs SalePrice: r={r:.3f}, p={p:.4f}"</span>)
<span class="ck"># p < 0.001 = highly significant</span>

<span class="ck"># ── Spearman correlation ──────────────────────────────</span>
<span class="ck"># Measures MONOTONIC (not just linear) relationship</span>
<span class="ck"># More robust to outliers and non-normal distributions</span>
<span class="ck"># Better for ordinal data (OverallQual: 1-10 ratings)</span>
spearman = df.corr(method=<span class="cs">"spearman"</span>, numeric_only=<span class="cv">True</span>)
print(<span class="cs">"Spearman top 5:"</span>, spearman[<span class="cs">"SalePrice"</span>].nlargest(<span class="cv">6</span>))

<span class="ck"># ── Multicollinearity detection ───────────────────────</span>
<span class="ck"># Features with r > 0.8 cause instability in linear models</span>
def find_multicollinear_pairs(corr_matrix, threshold=<span class="cv">0.8</span>):
    pairs = []
    cols = corr_matrix.columns
    for i in range(len(cols)):
        for j in range(i+<span class="cv">1</span>, len(cols)):
            r = abs(corr_matrix.iloc[i, j])
            if r > threshold:
                pairs.append((cols[i], cols[j], round(r, <span class="cv">3</span>)))
    return sorted(pairs, key=lambda x: -x[<span class="cv">2</span>])

pairs = find_multicollinear_pairs(corr)
for a, b, r in pairs:
    print(<span class="cs">f"  {a} ↔ {b}: r={r}"</span>)</pre></div>
    <div class="warn"><p>⚠️ <strong>Correlation ≠ causation.</strong> Ice cream sales and drowning deaths correlate (both peak in summer) but neither causes the other. Always ask "is there a plausible causal mechanism?" before treating correlation as meaningful. Also: Pearson measures linear relationships only — two variables can be strongly associated but r=0 if the relationship is non-linear (e.g. U-shaped).</p></div>
  </div>
</div>
</div>

<div id="t4" class="tab-pane">
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🎨</span><h3>Visualisation Toolkit — Right Plot for Every Question</h3><span class="tag tag-teal">Seaborn + Matplotlib</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style(<span class="cs">"whitegrid"</span>)
sns.set_context(<span class="cs">"notebook"</span>)

<span class="ck"># ── 1. Single distribution ────────────────────────────</span>
sns.histplot(df[<span class="cs">"SalePrice"</span>], bins=<span class="cv">40</span>, kde=<span class="cv">True</span>, color=<span class="cs">"steelblue"</span>)

<span class="ck"># ── 2. Distribution by group ─────────────────────────</span>
<span class="ck"># Boxplot: median, IQR, whiskers (1.5*IQR), outlier dots</span>
sns.boxplot(data=df, x=<span class="cs">"OverallQual"</span>, y=<span class="cs">"SalePrice"</span>)

<span class="ck"># Violinplot: boxplot + KDE density (shows bimodal shapes)</span>
sns.violinplot(data=df, x=<span class="cs">"OverallQual"</span>, y=<span class="cs">"SalePrice"</span>, inner=<span class="cs">"box"</span>)

<span class="ck"># ── 3. Two continuous variables ───────────────────────</span>
sns.scatterplot(data=df, x=<span class="cs">"GrLivArea"</span>, y=<span class="cs">"SalePrice"</span>,
                hue=<span class="cs">"OverallQual"</span>, palette=<span class="cs">"YlOrRd"</span>, alpha=<span class="cv">0.6</span>)

<span class="ck"># Regression line + confidence interval</span>
sns.regplot(data=df, x=<span class="cs">"GrLivArea"</span>, y=<span class="cs">"SalePrice"</span>,
            scatter_kws={<span class="cs">"alpha"</span>: <span class="cv">0.3</span>}, line_kws={<span class="cs">"color"</span>: <span class="cs">"red"</span>})

<span class="ck"># ── 4. All pairwise relationships ────────────────────</span>
<span class="ck"># Slow on >10 cols. Subset to key features first.</span>
key = [<span class="cs">"SalePrice"</span>, <span class="cs">"GrLivArea"</span>, <span class="cs">"OverallQual"</span>, <span class="cs">"YearBuilt"</span>, <span class="cs">"TotalBsmtSF"</span>]
sns.pairplot(df[key], diag_kind=<span class="cs">"kde"</span>, plot_kws={<span class="cs">"alpha"</span>: <span class="cv">0.4</span>})

<span class="ck"># ── 5. Categorical frequency ─────────────────────────</span>
order = df[<span class="cs">"MSZoning"</span>].value_counts().index
sns.countplot(data=df, x=<span class="cs">"MSZoning"</span>, order=order)

<span class="ck"># ── 6. Categorical vs numeric ────────────────────────</span>
order = df.groupby(<span class="cs">"Neighborhood"</span>)[<span class="cs">"SalePrice"</span>].median().sort_values(ascending=<span class="cv">False</span>).index
fig, ax = plt.subplots(figsize=(<span class="cv">14</span>, <span class="cv">5</span>))
sns.barplot(data=df, x=<span class="cs">"Neighborhood"</span>, y=<span class="cs">"SalePrice"</span>, order=order, ax=ax)
ax.tick_params(axis=<span class="cs">"x"</span>, rotation=<span class="cv">45</span>)

<span class="ck"># ── 7. Multi-panel summary ────────────────────────────</span>
fig, axes = plt.subplots(<span class="cv">2</span>, <span class="cv">3</span>, figsize=(<span class="cv">16</span>, <span class="cv">10</span>))
sns.histplot(df[<span class="cs">"SalePrice"</span>], kde=<span class="cv">True</span>, ax=axes[<span class="cv">0</span>, <span class="cv">0</span>]).set_title(<span class="cs">"Price Distribution"</span>)
sns.boxplot(data=df, x=<span class="cs">"OverallQual"</span>, y=<span class="cs">"SalePrice"</span>, ax=axes[<span class="cv">0</span>, <span class="cv">1</span>]).set_title(<span class="cs">"Quality vs Price"</span>)
sns.scatterplot(data=df, x=<span class="cs">"GrLivArea"</span>, y=<span class="cs">"SalePrice"</span>, alpha=<span class="cv">0.3</span>, ax=axes[<span class="cv">0</span>, <span class="cv">2</span>]).set_title(<span class="cs">"Area vs Price"</span>)
corr_top = df[key].corr()
sns.heatmap(corr_top, annot=<span class="cv">True</span>, fmt=<span class="cs">".2f"</span>, cmap=<span class="cs">"RdBu_r"</span>, center=<span class="cv">0</span>, ax=axes[<span class="cv">1</span>, <span class="cv">0</span>])
sns.countplot(data=df, x=<span class="cs">"MSZoning"</span>, ax=axes[<span class="cv">1</span>, <span class="cv">1</span>]).set_title(<span class="cs">"Zoning Distribution"</span>)
sns.histplot(df[<span class="cs">"YearBuilt"</span>], bins=<span class="cv">40</span>, ax=axes[<span class="cv">1</span>, <span class="cv">2</span>]).set_title(<span class="cs">"Year Built"</span>)
plt.tight_layout()
plt.savefig(<span class="cs">"eda_summary.png"</span>, dpi=<span class="cv">150</span>, bbox_inches=<span class="cs">"tight"</span>)</pre></div>
    <h4>Plot Selection Guide</h4>
    <div class="viz-grid">
      <div class="viz-card"><h5>histplot / kdeplot</h5><p>Single continuous distribution with optional smoothing.</p><div class="viz-when">Q: "What does this column look like?"</div></div>
      <div class="viz-card"><h5>boxplot</h5><p>Continuous vs categorical. Shows median, IQR, outliers.</p><div class="viz-when">Q: "How does price vary by quality?"</div></div>
      <div class="viz-card"><h5>violinplot</h5><p>Boxplot + density. Reveals bimodal distributions.</p><div class="viz-when">Q: "Is the distribution symmetric within each group?"</div></div>
      <div class="viz-card"><h5>scatterplot</h5><p>Two continuous variables. Add hue= for 3rd dimension.</p><div class="viz-when">Q: "Is there a relationship between X and Y?"</div></div>
      <div class="viz-card"><h5>pairplot</h5><p>All pairwise relationships. Comprehensive but slow.</p><div class="viz-when">Q: "Explore all feature interactions"</div></div>
      <div class="viz-card"><h5>heatmap</h5><p>Correlation matrix. Best with annot=True for &lt;15 features.</p><div class="viz-when">Q: "Which features are correlated?"</div></div>
    </div>
  </div>
</div>
</div>

<div id="t5" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Systematic EDA Workflow</h3><span class="tag tag-purple">Process</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import pandas as pd, numpy as np
import matplotlib.pyplot as plt, seaborn as sns
from scipy import stats

<span class="ck"># ════════════════════════════════════════════════════</span>
<span class="ck"># STEP 1: DATA INVENTORY</span>
<span class="ck"># ════════════════════════════════════════════════════</span>
print(<span class="cs">f"Shape: {df.shape}"</span>)
print(<span class="cs">"Dtypes:"</span>, df.dtypes.value_counts().to_dict())
null_pct = df.isnull().mean().sort_values(ascending=<span class="cv">False</span>)
print(<span class="cs">"Columns with nulls:\n"</span>, null_pct[null_pct > <span class="cv">0</span>])

numeric_cols     = df.select_dtypes(<span class="cs">"number"</span>).columns.tolist()
categorical_cols = df.select_dtypes(<span class="cs">"object"</span>).columns.tolist()

<span class="ck"># Missing value heatmap</span>
plt.figure(figsize=(<span class="cv">14</span>, <span class="cv">5</span>))
sns.heatmap(df.isnull(), yticklabels=<span class="cv">False</span>, cbar=<span class="cv">False</span>, cmap=<span class="cs">"viridis"</span>)
plt.title(<span class="cs">"Missing Values (yellow = missing)"</span>)

<span class="ck"># ════════════════════════════════════════════════════</span>
<span class="ck"># STEP 2: TARGET VARIABLE ANALYSIS</span>
<span class="ck"># ════════════════════════════════════════════════════</span>
TARGET = <span class="cs">"SalePrice"</span>
fig, axes = plt.subplots(<span class="cv">1</span>, <span class="cv">3</span>, figsize=(<span class="cv">15</span>, <span class="cv">4</span>))
sns.histplot(df[TARGET], kde=<span class="cv">True</span>, ax=axes[<span class="cv">0</span>]).set_title(<span class="cs">f"Raw (skew={df[TARGET].skew():.2f})"</span>)
stats.probplot(df[TARGET].dropna(), plot=axes[<span class="cv">1</span>]); axes[<span class="cv">1</span>].set_title(<span class="cs">"QQ Plot"</span>)
log_t = np.log1p(df[TARGET])
sns.histplot(log_t, kde=<span class="cv">True</span>, ax=axes[<span class="cv">2</span>]).set_title(<span class="cs">f"log() (skew={log_t.skew():.2f})"</span>)
plt.tight_layout()

<span class="ck"># ════════════════════════════════════════════════════</span>
<span class="ck"># STEP 3: NUMERIC FEATURES</span>
<span class="ck"># ════════════════════════════════════════════════════</span>
<span class="ck"># Distribution overview</span>
df[numeric_cols].hist(figsize=(<span class="cv">20</span>, <span class="cv">16</span>), bins=<span class="cv">30</span>)
plt.tight_layout()

<span class="ck"># Correlation with target</span>
tc = df[numeric_cols].corr()[TARGET].drop(TARGET).sort_values(ascending=<span class="cv">False</span>)
plt.figure(figsize=(<span class="cv">10</span>, <span class="cv">8</span>))
tc.plot(kind=<span class="cs">"barh"</span>, color=[<span class="cs">"green"</span> if x > <span class="cv">0</span> else <span class="cs">"red"</span> for x in tc])
plt.title(<span class="cs">"Feature Correlation with SalePrice"</span>)
plt.axvline(<span class="cv">0</span>, color=<span class="cs">"black"</span>, linewidth=<span class="cv">1</span>)

<span class="ck"># Scatter plots for top 6 features</span>
top6 = tc.abs().nlargest(<span class="cv">6</span>).index
fig, axes = plt.subplots(<span class="cv">2</span>, <span class="cv">3</span>, figsize=(<span class="cv">15</span>, <span class="cv">10</span>))
for ax, feat in zip(axes.flat, top6):
    r, _ = stats.pearsonr(df[feat].dropna(), df[TARGET][df[feat].notna()])
    ax.scatter(df[feat], df[TARGET], alpha=<span class="cv">0.3</span>, s=<span class="cv">10</span>)
    ax.set(xlabel=feat, ylabel=TARGET, title=<span class="cs">f"r={r:.3f}"</span>)
plt.tight_layout()

<span class="ck"># ════════════════════════════════════════════════════</span>
<span class="ck"># STEP 4: CATEGORICAL FEATURES</span>
<span class="ck"># ════════════════════════════════════════════════════</span>
for col in categorical_cols[:6]:
    n_cats = df[col].nunique()
    if n_cats > <span class="cv">15</span>: continue      <span class="ck"># skip high-cardinality</span>
    fig, ax = plt.subplots(figsize=(<span class="cv">10</span>, <span class="cv">4</span>))
    order = df.groupby(col)[TARGET].median().sort_values(ascending=<span class="cv">False</span>).index
    sns.boxplot(data=df, x=col, y=TARGET, order=order, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=<span class="cv">45</span>, ha=<span class="cs">"right"</span>)
    ax.set_title(<span class="cs">f"{col} vs {TARGET} (n_cats={n_cats})"</span>)
    plt.tight_layout()</pre></div>
  </div>
</div>
</div>

<div id="t6" class="tab-pane">
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🚨</span><h3>Outlier Detection and Treatment</h3><span class="tag tag-red">Data Quality</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import numpy as np
from scipy import stats
from sklearn.ensemble import IsolationForest

<span class="ck"># ── Method 1: IQR (most robust, skew-tolerant) ────────</span>
def iqr_outlier_mask(series):
    q1, q3 = series.quantile(0.25), series.quantile(0.75)
    iqr = q3 - q1
    return (series < q1 - 1.5 * iqr) | (series > q3 + 1.5 * iqr)

price_outliers = iqr_outlier_mask(df["SalePrice"])
area_outliers  = iqr_outlier_mask(df["GrLivArea"])
print(f"Price IQR outliers: {price_outliers.sum()}")
print(f"Area  IQR outliers:  {area_outliers.sum()}")

# Visualise with scatter: outliers in red
fig, ax = plt.subplots(figsize=(8, 5))
both_outliers = price_outliers | area_outliers
ax.scatter(df.loc[~both_outliers, "GrLivArea"], df.loc[~both_outliers, "SalePrice"],
           alpha=0.4, s=10, label="Normal")
ax.scatter(df.loc[both_outliers, "GrLivArea"],  df.loc[both_outliers, "SalePrice"],
           color="red", s=30, label="Outlier")
ax.set(xlabel="GrLivArea", ylabel="SalePrice", title="IQR Outliers Flagged")
ax.legend()

<span class="ck"># ── Method 2: Z-score (assumes normal distribution) ──</span>
z = np.abs(stats.zscore(df[["SalePrice", "GrLivArea"]].dropna()))
z_outliers = (z > 3).any(axis=1)
print(f"Z-score outliers (|z|>3): {z_outliers.sum()}")

<span class="ck"># ── Method 3: Isolation Forest (multivariate) ────────</span>
numeric = df.select_dtypes("number").dropna()
iso = IsolationForest(contamination=0.05, random_state=42)
labels = iso.fit_predict(numeric)
multi_outliers = labels == -1
print(f"Isolation Forest: {multi_outliers.sum()} outliers")

<span class="ck"># ── Treatment options ─────────────────────────────────</span>
<span class="ck"># Option 1: Remove — only if clearly erroneous, not just extreme</span>
df_clean = df[~(area_outliers & price_outliers)].copy()
print(f"After removal: {len(df_clean)} rows (was {len(df)})")

<span class="ck"># Option 2: Winsorise (cap at percentile) — preserves all rows</span>
lo, hi = df["SalePrice"].quantile([0.01, 0.99])
df["SalePrice_w"] = df["SalePrice"].clip(lo, hi)

<span class="ck"># Option 3: Log transform — mathematically compresses tails</span>
df["SalePrice_log"] = np.log1p(df["SalePrice"])</pre></div>
    <div class="ins"><p>💡 <strong>Before removing outliers, always inspect them individually.</strong> In the House Prices dataset, there are two houses with GrLivArea &gt; 4000 sqft but low SalePrice — these are partial sales, not data errors. Removing them changes model behaviour significantly. Check the Kaggle competition discussion before deleting rows.</p></div>
  </div>
</div>
</div>

<div id="t7" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Course</td><td><a href="https://www.kaggle.com/learn/data-visualization" target="_blank" rel="noopener">Kaggle Data Visualisation Course (Free) — kaggle.com/learn/data-visualization</a></td><td>Best hands-on Seaborn & Matplotlib exercises. Interactive notebooks, immediate feedback.</td></tr>
    <tr><td class="res-type">Video</td><td><a href="https://www.youtube.com/c/joshstarmer" target="_blank" rel="noopener">StatQuest — Statistics Fundamentals (YouTube) — youtube.com/c/joshstarmer</a></td><td>Best visual explanations of distributions, p-values, correlation, and statistical tests. No maths anxiety.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://seaborn.pydata.org/tutorial.html" target="_blank" rel="noopener">Seaborn Official Tutorial — seaborn.pydata.org/tutorial.html</a></td><td>Complete Seaborn reference with examples for every plot type. The authoritative source.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://matplotlib.org/stable/gallery/index.html" target="_blank" rel="noopener">Matplotlib Gallery — matplotlib.org/stable/gallery</a></td><td>Hundreds of example plots with full copy-paste source code. Start from a working example.</td></tr>
    <tr><td class="res-type">Dataset</td><td><a href="https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data" target="_blank" rel="noopener">House Prices — Kaggle</a></td><td>Best EDA dataset: 79 features, interesting distributions, real-world messy data, Kaggle community.</td></tr>
    <tr><td class="res-type">Dataset</td><td><a href="https://www.kaggle.com/c/titanic/data" target="_blank" rel="noopener">Titanic — Kaggle</a></td><td>Classic EDA dataset for categorical analysis and survival patterns. Well-documented community notebooks.</td></tr>
    <tr><td class="res-type">Course</td><td><a href="https://www.kaggle.com/learn/feature-engineering" target="_blank" rel="noopener">Kaggle Feature Engineering Course — kaggle.com/learn/feature-engineering</a></td><td>Extends EDA into feature creation. Covers mutual information, encoding strategies.</td></tr>
  </tbody>
</table>
</div>

<div id="t8" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">House Prices EDA Report</span><span class="proj-dur">[Intermediate] 5–6 days</span></div>
  <div class="proj-body">
    <p>Conduct a full EDA on the House Prices dataset and produce a polished visual report.</p>
    <h4>10 Required Visualisations</h4>
    <ul>
      <li>Target distribution: histogram + QQ plot of SalePrice, log-transformed version, skewness comparison</li>
      <li>Missing values: heatmap with percentage annotations</li>
      <li>Correlation: heatmap of top 15 features, bar chart of r-values with target</li>
      <li>Scatter with colour: GrLivArea vs SalePrice coloured by OverallQual</li>
      <li>Categorical analysis: boxplots of SalePrice by Neighborhood (sorted by median), OverallQual</li>
      <li>Distributions: histograms of top 5 right-skewed features before and after log transform</li>
      <li>Outlier plot: GrLivArea vs SalePrice with outliers highlighted in red</li>
    </ul>
    <p><strong>Deliverable:</strong> Jupyter notebook with all plots + 5 written insights that would guide modelling decisions.</p>
  </div>
</div>
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">Titanic Survival EDA</span><span class="proj-dur">[Beginner] 3–4 days</span></div>
  <div class="proj-body">
    <p>EDA focused on categorical patterns and survival rate analysis.</p>
    <ul>
      <li>Survival rates by: Sex, Pclass, Embarked, Age group (10-year bins)</li>
      <li>Age distribution by survival status (overlapping histograms with alpha)</li>
      <li>Fare distribution — detect and annotate outliers</li>
      <li>Correlation heatmap for numeric features</li>
      <li>Conclusion: "Which 3 features would you include in a model and why?"</li>
    </ul>
  </div>
</div>
</div>

<div id="t9" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Descriptive Statistics Deep Dive</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>Load House Prices. For SalePrice compute mean, median, std, skewness, kurtosis. Verify they match df.describe() and col.skew(). Print: "Mean exceeds median by X%, indicating right skew."</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Find all numeric columns with |skewness| &gt; 1. Apply log1p transform. Re-compute. How many now have |skewness| &lt; 0.5? Print a before/after comparison table.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Compute coefficient of variation (std/mean) for all numeric columns. Find the 3 with highest CV. What does high CV mean for model sensitivity?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Run Shapiro-Wilk on SalePrice (n=500). Then on log(SalePrice). Compare p-values and conclude: which version is more suitable for linear regression?</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Correlation and Multicollinearity</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>Compute Pearson correlation matrix. Find the 10 features most correlated with SalePrice. For each, compute the statistical significance (scipy.stats.pearsonr). Are all 10 significant?</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Find all pairs with |r| &gt; 0.8. Visualise one such pair with a scatter plot. Explain in one sentence why having both features in a linear model would be problematic.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Compare Pearson vs Spearman for OverallQual vs SalePrice. OverallQual is ordinal (integers 1–10). Which correlation is more appropriate and why?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Build a publication-quality correlation heatmap: top 12 features + SalePrice, annot=True, fmt=".2f", centre=0, square=True, title. Save as PNG at 150 DPI.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Outlier Detection Comparison</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>Apply IQR outlier detection to GrLivArea. Plot them as red points on a GrLivArea vs SalePrice scatter. How many outliers are flagged?</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Inspect the 2 points with GrLivArea &gt; 4000 but SalePrice &lt; $300k. Look at their other features (MSZoning, SaleType, SaleCondition). Are these data errors or partial sales?</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Apply Isolation Forest (contamination=0.05). Compare its outlier list vs IQR. Calculate: what % of IQR outliers are also flagged by Isolation Forest?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Create 3 versions of SalePrice: raw, Winsorised (1st/99th pct), log. Plot all 3 histograms side by side with their skewness annotated. Which version would you use for linear regression?</div></div>
  </div>
</div>
</div>

<div id="t10" class="tab-pane">
<p class="sep">P2-M05 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can compute mean, median, mode, std, IQR, skewness, kurtosis for any pandas Series</li>
  <li>Know when mean &gt; median signals right skew and what treatment to apply</li>
  <li>Can interpret distribution shape from histogram: normal, right-skewed, left-skewed, bimodal</li>
  <li>Can apply log1p transform and verify it reduces skewness</li>
  <li>Can run Shapiro-Wilk normality test and interpret the p-value</li>
  <li>Can compute Pearson correlation matrix and identify the features most correlated with target</li>
  <li>Can find multicollinear feature pairs (|r| &gt; 0.8) and understand why they are problematic</li>
  <li>Know the difference between Pearson and Spearman and when to use each</li>
  <li>Can produce: histplot, boxplot, violinplot, scatterplot, regplot, pairplot, heatmap, barplot, countplot</li>
  <li>Can choose the right plot for a given question and data type combination</li>
  <li>Can save publication-quality plots with savefig(dpi=150, bbox_inches='tight')</li>
  <li>Can follow the 4-phase EDA workflow: inventory → target → numeric → categorical</li>
  <li>Can detect outliers with IQR method, Z-score, and Isolation Forest</li>
  <li>Can choose between removing, capping (Winsorising), and log-transforming outliers</li>
  <li>Completed project: House Prices EDA report with 10 visualisations and written conclusions</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P2-M06 — ML Workflow</strong>: feature engineering, scaling, encoding, train/test split, and sklearn Pipelines.</p>
</div>
</div>

<div class="mod-nav">
  <a href="/learning/ai-ml/part1-foundation/p1-m04-sql-fastapi/">← P1-M04: SQL &amp; FastAPI</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part2-stats-eda/p2-m06-ml-workflow/">Next: P2-M06 — ML Workflow →</a>
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
    const key = 'p2m05_ck_' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
