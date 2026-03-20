---
layout: default
title: "P2-M06 - ML Workflow & Feature Engineering"
permalink: /learning/ai-ml/part2-stats-eda/p2-m06-ml-workflow/
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
  <div class="mod-eyebrow">Part 2 — ML Workflow &amp; Feature Engineering &nbsp;·&nbsp; Module 6 of 28</div>
  <div class="mod-title">ML Workflow &amp; Feature Engineering</div>
  <div class="mod-subtitle">Scale, encode, transform, and build your first sklearn Pipeline — the foundation of every ML project</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 2 Weeks</span>
    <span class="mod-pill">🟡 Intermediate</span>
    <span class="mod-pill">🔧 scikit-learn · pandas · numpy · Pipeline</span>
    <span class="mod-pill">📋 Prerequisite: P2-M05</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🔧 Feature Engineering</button>
  <button class="tab-btn" onclick="vt(event,'t2')">📏 Scaling</button>
  <button class="tab-btn" onclick="vt(event,'t3')">🔢 Encoding</button>
  <button class="tab-btn" onclick="vt(event,'t4')">✂ Train-Test Split</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🔁 Cross-Validation</button>
  <button class="tab-btn" onclick="vt(event,'t6')">🏗 sklearn Pipeline</button>
  <button class="tab-btn" onclick="vt(event,'t7')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t9')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t10')">✅ Checklist</button>
</div>

<div id="t0" class="tab-pane active">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-pink">Part 2</span></div>
  <div class="cp-body">
    <p>Raw data can rarely be fed directly into a model. This module covers the preprocessing and engineering steps that transform your DataFrame into model-ready features — and the sklearn Pipeline that makes these steps reproducible, leak-free, and composable.</p>
    <ul>
      <li><strong>Feature engineering</strong> — creating new features that capture domain knowledge</li>
      <li><strong>Scaling</strong> — StandardScaler, MinMaxScaler, RobustScaler — when and why</li>
      <li><strong>Encoding</strong> — label encoding, one-hot encoding, ordinal encoding, target encoding</li>
      <li><strong>Train-test split</strong> — stratified split, data leakage, the golden rule</li>
      <li><strong>Cross-validation</strong> — K-Fold, StratifiedKFold, leave-one-out</li>
      <li><strong>sklearn Pipeline</strong> — chaining preprocessing and model into a single reusable object</li>
    </ul>
    <div class="ins"><p>💡 <strong>The Pipeline is the most important sklearn abstraction.</strong> It guarantees that your scaler is fit only on training data (not test data), that your encoder handles unseen categories, and that your entire preprocessing stack can be serialised, deployed, and reloaded in production.</p></div>
  </div>
</div>
</div>

<div id="t1" class="tab-pane">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>Feature Engineering — Creating Better Inputs</h3><span class="tag tag-pink">Domain Knowledge</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import pandas as pd, numpy as np

df = pd.read_csv("house_prices.csv")

# ── Numeric transformations ─────────────────────────
# Log transform: compress right-skewed features
df["SalePrice_log"]   = np.log1p(df["SalePrice"])
df["GrLivArea_log"]   = np.log1p(df["GrLivArea"])
df["LotArea_log"]     = np.log1p(df["LotArea"])

# Square root: lighter compression than log
df["LotFrontage_sqrt"] = np.sqrt(df["LotFrontage"].fillna(0))

# Polynomial features: capture non-linear relationships
df["GrLivArea_sq"] = df["GrLivArea"] ** 2   # quadratic term

# ── Combining features ───────────────────────────────
# Domain insight: total bathrooms = full + half*0.5
df["TotalBath"] = (df["FullBath"] + df["BsmtFullBath"].fillna(0)
                   + 0.5 * (df["HalfBath"] + df["BsmtHalfBath"].fillna(0)))

# Total square footage
df["TotalSF"] = (df["TotalBsmtSF"].fillna(0) +
                 df["1stFlrSF"] + df["2ndFlrSF"])

# House age and remodel age
df["HouseAge"]  = df["YrSold"] - df["YearBuilt"]
df["RemodelAge"] = df["YrSold"] - df["YearRemodAdd"]

# Has garage? (binary from numeric)
df["HasGarage"] = (df["GarageArea"] > 0).astype(int)
df["HasPool"]   = (df["PoolArea"]   > 0).astype(int)
df["HasBsmt"]   = (df["TotalBsmtSF"].fillna(0) > 0).astype(int)

# ── Interaction features ─────────────────────────────
# Quality × Size: premium-size product captures luxury segment
df["QualArea"] = df["OverallQual"] * df["GrLivArea"]

# ── Binning continuous into ordinal ──────────────────
df["AgeBin"] = pd.cut(df["HouseAge"],
    bins=[0, 10, 20, 40, 80, 200],
    labels=["New", "Recent", "Middle", "Old", "Very Old"])

# ── Missing value handling ───────────────────────────
# Numeric: fill with median (robust to outliers)
for col in ["LotFrontage", "GarageYrBlt", "MasVnrArea"]:
    df[col].fillna(df[col].median(), inplace=True)

# Categorical: fill with most frequent or "None" string
for col in ["BsmtQual", "BsmtCond", "GarageType", "FireplaceQu"]:
    df[col].fillna("None", inplace=True)

print(f"Features created. Shape: {df.shape}")</pre></div>
    <div class="ins"><p>💡 <strong>Feature engineering is where domain expertise translates to model performance.</strong> TotalSF (total square footage) outperforms individual floor areas because it captures what buyers actually care about — total usable space. The best features come from asking "what would a human expert look at to value this house?"</p></div>
  </div>
</div>
</div>

<div id="t2" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📏</span><h3>Feature Scaling — When, Why, and Which</h3><span class="tag tag-blue">Preprocessing</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
import numpy as np

# ── StandardScaler: z-score normalisation ────────────
# Transforms each feature to mean=0, std=1
# x_new = (x - mean) / std
# USE WHEN: logistic regression, SVM, neural networks, PCA
# AVOID: tree-based models (Random Forest, XGBoost) — trees don't need scaling

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit AND transform
X_test_scaled  = scaler.transform(X_test)        # transform ONLY (never fit on test!)

# ── MinMaxScaler: scale to [0, 1] range ──────────────
# x_new = (x - min) / (max - min)
# USE WHEN: neural networks (bounded activations), KNN
# AVOID: when test data may exceed training range (extrapolation issues)

mm_scaler = MinMaxScaler(feature_range=(0, 1))
X_train_mm = mm_scaler.fit_transform(X_train)

# ── RobustScaler: median + IQR (outlier-robust) ───────
# x_new = (x - median) / IQR
# USE WHEN: data has significant outliers (medical, financial)
# Better than StandardScaler when outliers are present

rob = RobustScaler()
X_robust = rob.fit_transform(X_train)

# ── CRITICAL: fit on train, transform on test ─────────
# WRONG — causes data leakage:
# scaler.fit_transform(X_full)  # scaler sees test statistics!

# RIGHT:
scaler.fit(X_train)           # learn statistics from training data only
X_train_s = scaler.transform(X_train)
X_test_s  = scaler.transform(X_test)  # apply those statistics to test

# ── Do tree models need scaling? ──────────────────────
# NO. Decision trees split on thresholds — scale doesn't matter.
# Random Forest, XGBoost, LightGBM: no scaling needed.
# Logistic Regression, SVM, KNN, Neural Nets: MUST scale.

print(f"Before scaling: mean={X_train[:, 0].mean():.1f}, std={X_train[:, 0].std():.1f}")
print(f"After scaling:  mean={X_train_scaled[:, 0].mean():.4f}, std={X_train_scaled[:, 0].std():.4f}")</pre></div>
    <div class="ins"><p>💡 <strong>The most common preprocessing mistake is fitting the scaler on the entire dataset before splitting.</strong> If you scale using the test set's statistics, the model has implicitly "seen" the test data — this inflates your validation metrics and your real-world performance will be worse. Always fit preprocessing objects only on training data.</p></div>
  </div>
</div>
</div>

<div id="t3" class="tab-pane">
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔢</span><h3>Categorical Encoding</h3><span class="tag tag-teal">Encoding Strategies</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, OneHotEncoder
from sklearn.preprocessing import TargetEncoder  # sklearn >= 1.3

# ── 1. One-Hot Encoding (OHE) ─────────────────────────
# Creates N binary columns (or N-1 to avoid multicollinearity)
# USE FOR: nominal categories (no natural order): color, city, genre
# AVOID FOR: high cardinality (>20 categories) — too many columns

ohe = OneHotEncoder(handle_unknown="ignore", sparse_output=False, drop="first")
X_ohe = ohe.fit_transform(df[["MSZoning", "SaleType"]])
print(f"OHE output shape: {X_ohe.shape}")
print(f"Feature names: {ohe.get_feature_names_out()[:5]}")

# With pandas (simpler for exploration)
df_ohe = pd.get_dummies(df[["MSZoning", "SaleType"]], drop_first=True)

# ── 2. Ordinal Encoding ───────────────────────────────
# Maps categories to integers preserving order
# USE FOR: categories with natural ranking: poor<fair<good<excellent

quality_order = ["None", "Po", "Fa", "TA", "Gd", "Ex"]
ord_enc = OrdinalEncoder(categories=[quality_order], handle_unknown="use_encoded_value",
                          unknown_value=-1)
df["ExterQual_enc"] = ord_enc.fit_transform(df[["ExterQual"]])

# Manual ordinal mapping (most explicit)
qual_map = {"None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5}
for col in ["BsmtQual", "KitchenQual", "GarageQual"]:
    df[f"{col}_ord"] = df[col].map(qual_map).fillna(0)

# ── 3. Target Encoding (mean encoding) ────────────────
# Replace each category with the mean target value for that category
# USE FOR: high-cardinality categoricals (Neighborhood: 25 values)
# MUST use cross-validation to avoid target leakage

from sklearn.preprocessing import TargetEncoder  # sklearn >= 1.3
te = TargetEncoder(cv=5, smooth="auto")  # cv=5 prevents leakage
X_te = te.fit_transform(df[["Neighborhood"]], df["SalePrice"])

# Manual with K-fold (scikit-learn < 1.3)
from sklearn.model_selection import KFold

def target_encode_kfold(df, cat_col, target_col, n_splits=5):
    result = df[cat_col].copy()
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    for train_idx, val_idx in kf.split(df):
        means = df.iloc[train_idx].groupby(cat_col)[target_col].mean()
        result.iloc[val_idx] = df.iloc[val_idx][cat_col].map(means)
    return result.fillna(df[target_col].mean())

df["Neighborhood_te"] = target_encode_kfold(df, "Neighborhood", "SalePrice")

# ── Summary: when to use what ─────────────────────────
# OHE:    nominal, low cardinality (<20 categories)
# Ordinal: ordered categories (quality ratings)
# Target:  high cardinality when tree models are used</pre></div>
  </div>
</div>
</div>

<div id="t4" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">✂</span><h3>Train-Test Split and Data Leakage</h3><span class="tag tag-purple">Critical Concept</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.model_selection import train_test_split
import pandas as pd

# ── Basic split ───────────────────────────────────────
X = df.drop(columns=["SalePrice"])
y = df["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,     # 80% train, 20% test
    random_state=42    # reproducible split
)
print(f"Train: {len(X_train)}, Test: {len(X_test)}")

# ── Stratified split for classification ──────────────
# Ensures class distribution is preserved in both sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y_class,
    test_size=0.2,
    stratify=y_class,  # preserve class proportions
    random_state=42
)
# Check class balance is preserved:
print("Train:", y_train.value_counts(normalize=True))
print("Test: ", y_test.value_counts(normalize=True))

# ── Data leakage — THE most important concept ─────────
# Leakage: test-set information contaminating training
# Sources:
#   1. Scaling on full dataset before split
#   2. Imputing with full-dataset statistics before split
#   3. Feature engineering using future data
#   4. Selecting features based on test-set correlation

# ── How to check for leakage ──────────────────────────
# Suspiciously high train accuracy (>99%) with low test accuracy
# Features with correlation >0.95 to target (might be derived from target)
# Model performance "too good to be true"

# Check for suspicious correlations
corr = df.corr(numeric_only=True)["SalePrice"].sort_values(ascending=False)
suspicious = corr[corr > 0.95].drop("SalePrice")
if len(suspicious):
    print("WARNING: Potentially leaky features:")
    print(suspicious)</pre></div>
    <div class="warn"><p>⚠️ <strong>The Golden Rule: your test set is a time capsule from the future.</strong> You are not allowed to look at it until final evaluation. Never fit your scaler, imputer, or encoder on the full dataset — always fit on training data only, then apply to test. Using the test set at any point during preprocessing inflates your estimates of generalisation performance.</p></div>
  </div>
</div>
</div>

<div id="t5" class="tab-pane">
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔁</span><h3>Cross-Validation — Reliable Model Evaluation</h3><span class="tag tag-green">Evaluation</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.model_selection import (cross_val_score, KFold,
                                     StratifiedKFold, cross_validate)
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np

model = Ridge(alpha=1.0)

# ── K-Fold cross-validation ───────────────────────────
# Train/eval k times on different non-overlapping folds
# Final score = mean ± std over k folds
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kf, scoring="neg_root_mean_squared_error")
rmse_scores = -scores   # negate back to positive
print(f"CV RMSE: {rmse_scores.mean():.0f} ± {rmse_scores.std():.0f}")

# ── Multiple metrics at once ──────────────────────────
results = cross_validate(model, X_num, y, cv=5, scoring={
    "r2":   "r2",
    "rmse": "neg_root_mean_squared_error",
    "mae":  "neg_mean_absolute_error",
}, return_train_score=True)
print(f"CV R²:   {results['test_r2'].mean():.3f}")
print(f"CV RMSE: {-results['test_rmse'].mean():.0f}")
# Compare train vs test: if train >> test, you are overfitting

# ── StratifiedKFold for classification ────────────────
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(classifier, X, y_class, cv=skf, scoring="f1_macro")
print(f"Stratified CV F1: {scores.mean():.3f} ± {scores.std():.3f}")

# ── CV INSIDE a Pipeline (correct) ────────────────────
# Pipeline ensures scaler is fit on training folds ONLY
pipe = Pipeline([("scaler", StandardScaler()), ("model", Ridge(alpha=1.0))])
cv_scores = cross_val_score(pipe, X_num, y, cv=5, scoring="r2")
print(f"Pipeline CV R²: {cv_scores.mean():.3f}")</pre></div>
    <div class="ins"><p>💡 <strong>K=5 is the standard choice.</strong> K=5 gives 5x fewer training samples than the full dataset — acceptable bias. K=10 gives slightly better estimates but takes 2× longer. K=3 is faster but noisier. For small datasets (&lt;500 rows), consider leave-one-out (LOOCV). Always look at the standard deviation — a mean of 0.85 ± 0.01 is far more reliable than 0.85 ± 0.12.</p></div>
  </div>
</div>
</div>

<div id="t6" class="tab-pane">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">🏗</span><h3>sklearn Pipeline — The Production Pattern</h3><span class="tag tag-pink">Best Practice</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, RobustScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
import pandas as pd
import joblib

# ── Define column types ───────────────────────────────
numeric_cols = ["GrLivArea", "TotalBsmtSF", "OverallQual", "HouseAge", "TotalBath"]
low_card_cat = ["MSZoning", "SaleType", "HeatingQC"]
high_card_cat = ["Neighborhood"]

# ── Numeric pipeline: impute then scale ───────────────
numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),   # fill NaN with column median
    ("scaler",  RobustScaler()),                     # scale robust to outliers
])

# ── Categorical pipeline: impute then encode ─────────
categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),  # fill NaN with mode
    ("ohe",     OneHotEncoder(handle_unknown="ignore", sparse_output=False, drop="first")),
])

# ── Combine with ColumnTransformer ────────────────────
preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer, numeric_cols),
    ("cat", categorical_transformer, low_card_cat),
], remainder="drop")

# ── Full Pipeline: preprocessing + model ─────────────
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model",        Ridge(alpha=10.0)),
])

# ── Train the whole thing ─────────────────────────────
pipeline.fit(X_train, y_train)    # fits preprocessors on X_train, trains model

# ── Evaluate ──────────────────────────────────────────
from sklearn.metrics import root_mean_squared_error, r2_score
y_pred = pipeline.predict(X_test)
print(f"RMSE: {root_mean_squared_error(y_test, y_pred):,.0f}")
print(f"R²:   {r2_score(y_test, y_pred):.4f}")

# ── Cross-validate the whole Pipeline ─────────────────
from sklearn.model_selection import cross_val_score
cv_r2 = cross_val_score(pipeline, X_train, y_train, cv=5, scoring="r2")
print(f"CV R²: {cv_r2.mean():.3f} ± {cv_r2.std():.3f}")

# ── Save and reload ───────────────────────────────────
joblib.dump(pipeline, "house_price_pipeline.pkl")
loaded = joblib.load("house_price_pipeline.pkl")
print(f"Loaded pipeline prediction: {loaded.predict(X_test[:1])[0]:,.0f}")</pre></div>
    <div class="ins"><p>💡 <strong>A Pipeline is not just convenience — it is correctness.</strong> Without a Pipeline, you will accidentally leak preprocessing statistics. With a Pipeline, calling pipeline.fit(X_train, y_train) fits your scaler, imputer, and encoder only on X_train. Calling pipeline.predict(X_test) applies those learned transformations without refitting. This is the only correct way to build a preprocessing + model stack.</p></div>
  </div>
</div>
</div>

<div id="t7" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Course</td><td><a href="https://www.kaggle.com/learn/intermediate-machine-learning" target="_blank" rel="noopener">Kaggle Intermediate ML Course (Free) — kaggle.com/learn/intermediate-machine-learning</a></td><td>Best coverage of Pipelines, missing values, categorical encoding, and data leakage.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://scikit-learn.org/stable/modules/preprocessing.html" target="_blank" rel="noopener">Scikit-learn Preprocessing Guide — scikit-learn.org/stable/modules/preprocessing.html</a></td><td>Complete reference for all sklearn scalers, encoders, and transformers with examples.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://scikit-learn.org/stable/modules/compose.html" target="_blank" rel="noopener">Scikit-learn ColumnTransformer — scikit-learn.org/stable/modules/compose.html</a></td><td>Official guide on combining multiple transformers with ColumnTransformer and Pipeline.</td></tr>
    <tr><td class="res-type">Course</td><td><a href="https://www.kaggle.com/learn/feature-engineering" target="_blank" rel="noopener">Kaggle Feature Engineering Course — kaggle.com/learn/feature-engineering</a></td><td>Mutual information, target encoding, and creating features. Practical exercises.</td></tr>
    <tr><td class="res-type">Video</td><td><a href="https://www.youtube.com/c/joshstarmer" target="_blank" rel="noopener">StatQuest — Cross-Validation and Pipeline (YouTube)</a></td><td>Visual explanation of K-Fold cross-validation and why it matters. Clear and memorable.</td></tr>
    <tr><td class="res-type">Article</td><td><a href="https://machinelearningmastery.com/data-leakage-machine-learning/" target="_blank" rel="noopener">Data Leakage in Machine Learning — machinelearningmastery.com</a></td><td>Comprehensive guide to all types of data leakage with examples. Essential reading.</td></tr>
  </tbody>
</table>
</div>

<div id="t8" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">House Prices — Full Preprocessing Pipeline</span><span class="proj-dur">[Intermediate] 4–5 days</span></div>
  <div class="proj-body">
    <p>Build a complete preprocessing + Ridge regression pipeline for the House Prices dataset.</p>
    <h4>Requirements</h4>
    <ul>
      <li><strong>Feature engineering</strong> — create TotalSF, HouseAge, TotalBath, HasGarage, QualArea</li>
      <li><strong>Missing values</strong> — impute numeric with median, categorical with "None" or mode</li>
      <li><strong>Encoding</strong> — OHE for low-cardinality nominals, ordinal encoding for quality columns</li>
      <li><strong>Scaling</strong> — RobustScaler on numeric features</li>
      <li><strong>Pipeline</strong> — ColumnTransformer + Ridge(alpha=10) in a single Pipeline object</li>
      <li><strong>Evaluation</strong> — 5-fold CV reporting mean RMSE ± std</li>
      <li><strong>Target transform</strong> — fit on log(SalePrice), invert with np.expm1() for final predictions</li>
    </ul>
    <p>Expected CV RMSE: ~$25,000–$30,000 on raw price. Compare: what RMSE do you get on log price?</p>
  </div>
</div>
</div>

<div id="t9" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Scaling Comparison</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>Take GrLivArea with its outliers. Apply StandardScaler, MinMaxScaler, and RobustScaler. Plot all 3 resulting distributions. How does each handle the outliers at GrLivArea &gt; 4000?</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Intentionally leak: fit a StandardScaler on X_full (before split), then use those statistics to scale X_train and X_test. Compare the mean/std of X_test — they should be non-zero with leaked scaler. With correct pipeline, they should be ~0/1.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Train a Ridge regression with correctly scaled vs leaked scaled data. Compare test R² scores. Does leakage always inflate performance on this dataset?</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Encoding Comparison</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>Encode the Neighborhood column (25 categories) three ways: OHE, label encoding, target encoding (K-fold). Train Ridge regression with each. Which gives the best cross-validated R²?</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Apply OHE to all nominal columns. How many columns does the feature matrix become? Use get_feature_names_out() to list all OHE features.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Apply ordinal encoding to ExterQual, KitchenQual, BsmtQual using the order Po &lt; Fa &lt; TA &lt; Gd &lt; Ex. Compute Spearman correlation with SalePrice for each encoded column. Compare to raw OHE.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Pipeline Build</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>Build the full ColumnTransformer pipeline (numeric: impute+scale; categorical: impute+OHE). Print the pipeline structure with pipeline.named_steps and check the output shape after fit_transform.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Run 5-fold CV on the full pipeline with Ridge. Print mean RMSE and std. Then change to alpha=0.1 and alpha=100. Which alpha gives the best CV RMSE?</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Save the pipeline with joblib.dump(). Reload it and make a prediction on a manually constructed row (dict of feature values). Verify the prediction matches what the un-saved pipeline produces.</div></div>
  </div>
</div>
</div>

<div id="t10" class="tab-pane">
<p class="sep">P2-M06 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can create new numeric features: log transforms, square root, polynomial, interaction terms</li>
  <li>Can combine columns to create domain-meaningful features (TotalSF, TotalBath, HouseAge)</li>
  <li>Can apply SimpleImputer with median (numeric) and most_frequent (categorical) strategies</li>
  <li>Know when to use StandardScaler vs MinMaxScaler vs RobustScaler</li>
  <li>Know that tree models (Random Forest, XGBoost) do NOT need scaling</li>
  <li>Know the Golden Rule: fit preprocessing ONLY on training data, never on full dataset</li>
  <li>Can apply OHE for nominal and ordinal encoding for ordered categories</li>
  <li>Can apply target encoding with K-fold to avoid leakage on high-cardinality columns</li>
  <li>Can perform stratified train-test split with correct random_state for reproducibility</li>
  <li>Can run K-Fold cross-validation and report mean ± std for multiple metrics</li>
  <li>Can build a Pipeline combining ColumnTransformer preprocessor + model</li>
  <li>Can save a Pipeline with joblib.dump() and reload with joblib.load()</li>
  <li>Can cross-validate the entire Pipeline (guarantees leak-free evaluation)</li>
  <li>Completed project: House Prices preprocessing pipeline with 5-fold CV RMSE reported</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P3-M07 — Regression</strong>: linear, ridge, lasso, and polynomial regression — your first predictive models.</p>
</div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/ai-ml/part2-stats-eda/p2-m05-stats-viz/' | relative_url }}">← P2-M05: Stats &amp; Viz</a>
  <a href="{{ '/learning/ai-ml/ai-ml-roadmap/' | relative_url }}">🗺️ All Modules</a>
  <a class="nb" href="{{ '/learning/ai-ml/part3-classical-ml/p3-m07-regression/' | relative_url }}">Next: P3-M07 — Regression →</a>
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
    const key = 'p2m06_ck_' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
