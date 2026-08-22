---
title: "P3-M07 - Regression: Linear, Ridge, Lasso & Polynomial"
description: "Part 3 — Classical ML · Module 7 of 28 Regression: Linear, Ridge, Lasso Polynomial Predict continuous outcomes — from first principles to regularised production models ⏱ 2…"
domain: ai-ml
track: ai-ml-engineering
module: part3-classical-ml
order: 307
ownHeader: true
url: /learning/ai-ml/part3-classical-ml/p3-m07-regression/
---

<style>
.mod-header{background:linear-gradient(135deg,#0f0a1e 0%,#0a1a30 40%,#1a3060 70%,#be185d 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#f9a8d4;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#fce7f3;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#fce7f3}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1a30;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#f9a8d4;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#f472b6;border-bottom-color:#f472b6}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee)}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700}
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
.cb{background:#0a1a30;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #be185d}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#fce7f3;white-space:pre}
.ins{background:#fdf2f8;border:1.5px solid #be185d;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#1e0a18;border-color:#be185d}
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
.lab-hdr{background:#0a1a30;padding:.7rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-n{background:#be185d;color:#fff;font-size:.72rem;font-family:monospace;font-weight:700;padding:2px 10px;border-radius:12px}
.lab-hdr h4{margin:0;font-size:.95rem;font-weight:700;color:#fce7f3;border:none}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.8rem;font-size:.88rem;line-height:1.65}
.sn{background:#be185d;color:#fff;width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem 0;border-bottom:1px solid var(--border-color,#eee);font-size:.88rem;line-height:1.6;cursor:pointer}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐";font-size:1rem;flex-shrink:0;margin-top:.05rem;color:#be185d}
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
</style>

<div class="mod-header">
  <div class="mod-eyebrow">Part 3 — Classical ML &nbsp;·&nbsp; Module 7 of 28</div>
  <div class="mod-title">Regression: Linear, Ridge, Lasso &amp; Polynomial</div>
  <div class="mod-subtitle">Predict continuous outcomes — from first principles to regularised production models</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 2 Weeks</span>
    <span class="mod-pill">🟡 Intermediate</span>
    <span class="mod-pill">🔧 scikit-learn · numpy · statsmodels</span>
    <span class="mod-pill">📋 Prerequisite: P2-M06</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">📐 Linear Regression</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🛡 Ridge (L2)</button>
  <button class="tab-btn" onclick="vt(event,'t3')">✂ Lasso (L1)</button>
  <button class="tab-btn" onclick="vt(event,'t4')">🔀 Elastic Net</button>
  <button class="tab-btn" onclick="vt(event,'t5')">📈 Polynomial</button>
  <button class="tab-btn" onclick="vt(event,'t6')">📊 Metrics</button>
  <button class="tab-btn" onclick="vt(event,'t7')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t9')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t10')">✅ Checklist</button>
</div>

<div id="t0" class="tab-pane active">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-pink">Part 3 Start</span></div>
  <div class="cp-body">
    <p>Regression predicts a continuous output (price, temperature, sales). Linear regression is the foundation — it is interpretable, fast, and a powerful baseline. Regularised variants (Ridge, Lasso) prevent overfitting on high-dimensional data and remain competitive with tree models when features are well-engineered.</p>
    <ul>
      <li><strong>Linear Regression</strong> — ordinary least squares, the normal equation, assumptions, residual analysis</li>
      <li><strong>Ridge (L2 regularisation)</strong> — shrinks coefficients, handles multicollinearity, keeps all features</li>
      <li><strong>Lasso (L1 regularisation)</strong> — automatic feature selection, drives irrelevant features to zero</li>
      <li><strong>Elastic Net</strong> — combines L1 and L2, best for correlated feature groups</li>
      <li><strong>Polynomial Regression</strong> — capturing non-linear relationships with linear models</li>
      <li><strong>Regression metrics</strong> — MAE, MSE, RMSE, R², MAPE — when to use each</li>
    </ul>
    <div class="ins"><p>💡 <strong>Always start with linear regression.</strong> It is your baseline. If a linear model gets R²=0.85, you need a very good reason to use a complex model. If R²=0.40, explore feature engineering or non-linear models. Linear models are also fully interpretable — you can explain every prediction to a non-technical stakeholder.</p></div>
  </div>
</div>
</div>

<div id="t1" class="tab-pane">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">📐</span><h3>Linear Regression — First Principles to sklearn</h3><span class="tag tag-pink">Foundation</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
 
# ── Concept: linear regression minimises SSR ─────────
# ŷ = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
# OLS finds β values that minimise Σ(y - ŷ)²
# Normal equation: β = (XᵀX)⁻¹Xᵀy (closed form for small n)
# Gradient descent: update β iteratively (used for large datasets)
 
# ── sklearn implementation ────────────────────────────
X = df[["GrLivArea", "OverallQual", "YearBuilt", "TotalBath"]].fillna(0)
y = df["SalePrice"]
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model",  LinearRegression()),
])
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
 
rmse = root_mean_squared_error(y_test, y_pred)
r2   = r2_score(y_test, y_pred)
print(f"Test RMSE: {rmse:,.0f}")
print(f"Test R²:   {r2:.4f}")
 
# CV score
cv_r2 = cross_val_score(pipe, X, y, cv=5, scoring="r2")
print(f"CV R²: {cv_r2.mean():.3f} ± {cv_r2.std():.3f}")
 
# ── Coefficients — interpretability ──────────────────
lr = pipe.named_steps["model"]
coef_df = pd.DataFrame({
    "feature": X.columns,
    "coefficient": lr.coef_
}).sort_values("coefficient", ascending=False)
print(coef_df)
# Each coefficient: "holding all other features constant,
# increasing this feature by 1 (scaled unit) changes price by X dollars"
 
# ── Residual analysis ─────────────────────────────────
residuals = y_test - y_pred
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].scatter(y_pred, residuals, alpha=0.3, s=10)
axes[0].axhline(0, color="red", linewidth=1)
axes[0].set(xlabel="Predicted", ylabel="Residual", title="Residuals vs Fitted")
axes[1].hist(residuals, bins=40)
axes[1].set(xlabel="Residual", title="Residual Distribution")
# Ideal: residuals randomly scattered around zero, normally distributed</pre></div>
    <h4>Linear Regression Assumptions</h4>
    <ul>
      <li><strong>Linearity</strong> — relationship between features and target is linear</li>
      <li><strong>Independence</strong> — observations are independent (violated in time series)</li>
      <li><strong>Homoscedasticity</strong> — residuals have constant variance (fan-shaped residuals = violated)</li>
      <li><strong>Normality of residuals</strong> — for inference/confidence intervals (not needed for just prediction)</li>
      <li><strong>No perfect multicollinearity</strong> — no feature is a perfect linear combination of others</li>
    </ul>
  </div>
</div>
</div>

<div id="t2" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🛡</span><h3>Ridge Regression (L2) — Tame Multicollinearity</h3><span class="tag tag-blue">Regularisation</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.linear_model import Ridge, RidgeCV
from sklearn.model_selection import cross_val_score
import numpy as np
 
# ── Ridge adds L2 penalty to OLS ─────────────────────
# Minimises: Σ(y - ŷ)² + α * Σβᵢ²
# α (alpha): regularisation strength
#   α = 0: same as linear regression (no regularisation)
#   α → ∞: all coefficients shrink toward zero
# Effect: coefficients shrink proportionally (none become exactly zero)
# Best for: multicollinear features, more features than samples
 
alphas = [0.01, 0.1, 1.0, 10, 100, 1000]
 
# Manual grid search with cross-validation
results = []
for alpha in alphas:
    pipe = Pipeline([("scaler", StandardScaler()),
                     ("model", Ridge(alpha=alpha))])
    cv_r2 = cross_val_score(pipe, X_train, y_train, cv=5, scoring="r2")
    results.append({"alpha": alpha, "r2_mean": cv_r2.mean(), "r2_std": cv_r2.std()})
 
import pandas as pd
results_df = pd.DataFrame(results)
print(results_df)
best_alpha = results_df.loc[results_df["r2_mean"].idxmax(), "alpha"]
print(f"Best alpha: {best_alpha}")
 
# Built-in CV (faster)
alphas_to_try = np.logspace(-3, 4, 50)  # log-spaced from 0.001 to 10,000
ridge_cv = RidgeCV(alphas=alphas_to_try, cv=5, scoring="r2")
ridge_cv.fit(StandardScaler().fit_transform(X_train), y_train)
print(f"RidgeCV best alpha: {ridge_cv.alpha_:.4f}")
print(f"RidgeCV R²: {ridge_cv.score(StandardScaler().fit_transform(X_test), y_test):.4f}")
 
# ── Visualise coefficient shrinkage ──────────────────
fig, ax = plt.subplots(figsize=(10, 5))
coefs = []
for alpha in np.logspace(-3, 4, 100):
    r = Ridge(alpha=alpha)
    r.fit(StandardScaler().fit_transform(X_train), y_train)
    coefs.append(r.coef_)
coefs = np.array(coefs)
for i, name in enumerate(X.columns):
    ax.plot(np.logspace(-3, 4, 100), coefs[:, i], label=name)
ax.set_xscale("log")
ax.set(xlabel="Alpha (log scale)", ylabel="Coefficient Value",
       title="Ridge: Coefficient Shrinkage")
ax.axvline(best_alpha, color="red", linestyle="--", label="Best alpha")
ax.legend()
plt.tight_layout()</pre></div>
    <div class="ins"><p>💡 <strong>Ridge is the default choice for linear regression with many features.</strong> When your features include correlated columns (which they always do in real datasets), OLS produces unstable, high-variance coefficients. Ridge's L2 penalty distributes the coefficient weight across correlated features, producing stable predictions even when features are collinear.</p></div>
  </div>
</div>
</div>

<div id="t3" class="tab-pane">
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">✂</span><h3>Lasso Regression (L1) — Built-In Feature Selection</h3><span class="tag tag-teal">Sparse Models</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.linear_model import Lasso, LassoCV
import matplotlib.pyplot as plt
import numpy as np
 
# ── Lasso adds L1 penalty ────────────────────────────
# Minimises: Σ(y - ŷ)² + α * Σ|βᵢ|
# Key property: L1 penalty drives SOME coefficients to EXACTLY zero
# This is automatic feature selection — irrelevant features are zeroed out
# Drawback: when features are correlated, Lasso picks one arbitrarily
 
# Find best alpha via cross-validation
alphas_lasso = np.logspace(-4, 1, 50)
 
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler
 
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)
 
lasso_cv = LassoCV(alphas=alphas_lasso, cv=5, max_iter=10000, random_state=42)
lasso_cv.fit(X_train_s, y_train)
print(f"Best alpha: {lasso_cv.alpha_:.6f}")
print(f"Test R²: {lasso_cv.score(X_test_s, y_test):.4f}")
 
# ── Feature selection: which features were zeroed? ────
coefs = pd.Series(lasso_cv.coef_, index=X.columns)
selected = coefs[coefs != 0].sort_values(ascending=False)
zeroed   = coefs[coefs == 0]
print(f"Selected features: {len(selected)} / {len(coefs)}")
print(f"Zeroed features:   {len(zeroed)}")
print("\nTop 10 selected features:")
print(selected.head(10))
 
# ── Visualise Lasso path ──────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
 
coef_path = []
for alpha in alphas_lasso:
    l = Lasso(alpha=alpha, max_iter=10000)
    l.fit(X_train_s, y_train)
    coef_path.append(l.coef_)
 
coef_path = np.array(coef_path)
for i, name in enumerate(X.columns[:10]):
    axes[0].plot(alphas_lasso, coef_path[:, i], label=name)
axes[0].set_xscale("log")
axes[0].axvline(lasso_cv.alpha_, color="red", linestyle="--")
axes[0].set(xlabel="Alpha", ylabel="Coefficient", title="Lasso Path (top 10 features)")
axes[0].legend(fontsize=7)
 
# Non-zero coefficients
selected.plot(kind="barh", ax=axes[1])
axes[1].set(title="Lasso Selected Features (non-zero coefficients)")
plt.tight_layout()</pre></div>
    <h4>Ridge vs Lasso: Decision Guide</h4>
    <div style="overflow-x:auto">
      <table style="width:100%;border-collapse:collapse;font-size:.84rem">
        <thead><tr style="background:#0a1a30;color:#fce7f3"><th style="padding:.5rem .8rem;text-align:left">Property</th><th style="padding:.5rem .8rem">Ridge (L2)</th><th style="padding:.5rem .8rem">Lasso (L1)</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem;font-weight:600">Penalty</td><td style="padding:.5rem .8rem">β² (squared)</td><td style="padding:.5rem .8rem">|β| (absolute)</td></tr>
          <tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem;font-weight:600">Coefficients</td><td style="padding:.5rem .8rem">Shrink toward zero, none exactly zero</td><td style="padding:.5rem .8rem">Some become exactly zero (sparse)</td></tr>
          <tr style="border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem;font-weight:600">Feature selection</td><td style="padding:.5rem .8rem">No (keeps all features)</td><td style="padding:.5rem .8rem">Yes (automatic)</td></tr>
          <tr style="background:var(--bg-color,#f8f8f8);border-bottom:1px solid var(--border-color,#e4e4e4)"><td style="padding:.5rem .8rem;font-weight:600">Correlated features</td><td style="padding:.5rem .8rem">Shares weight across correlated group</td><td style="padding:.5rem .8rem">Picks one, zeros others</td></tr>
          <tr><td style="padding:.5rem .8rem;font-weight:600">Best for</td><td style="padding:.5rem .8rem">All features likely relevant, multicollinearity</td><td style="padding:.5rem .8rem">Many irrelevant features, need interpretability</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</div>

<div id="t4" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔀</span><h3>Elastic Net and Logistic Regression</h3><span class="tag tag-purple">Best of Both</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.linear_model import ElasticNet, ElasticNetCV, LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
 
# ── Elastic Net: combines L1 + L2 ────────────────────
# Penalty: α * [l1_ratio * Σ|βᵢ| + (1 - l1_ratio) * Σβᵢ²]
# l1_ratio = 1.0: pure Lasso
# l1_ratio = 0.0: pure Ridge
# l1_ratio = 0.5: equal mix (default starting point)
#
# Use Elastic Net when: features are correlated AND you want sparsity
# It produces sparse models but handles correlated groups better than Lasso
 
en_cv = ElasticNetCV(l1_ratio=[0.1, 0.3, 0.5, 0.7, 0.9, 1.0],
                      cv=5, max_iter=10000, random_state=42)
en_cv.fit(X_train_scaled, y_train)
print(f"Best alpha: {en_cv.alpha_:.6f}")
print(f"Best l1_ratio: {en_cv.l1_ratio_}")
print(f"Non-zero features: {(en_cv.coef_ != 0).sum()}")
 
# ── Logistic Regression: binary classification ────────
# Despite the name, this is a classification model
# Uses sigmoid function to output probabilities in [0, 1]
# P(y=1|x) = 1 / (1 + e^(-xβ))
# Decision boundary: predict class 1 if P(y=1|x) > 0.5
# Naturally regularised: C = 1/α (higher C = less regularisation)
 
from sklearn.datasets import load_breast_cancer
X_c, y_c = load_breast_cancer(return_X_y=True)
 
lr_pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model",  LogisticRegression(C=1.0, max_iter=1000, random_state=42))
])
lr_pipe.fit(X_train_c, y_train_c)
 
# Probabilities (not just class labels)
proba = lr_pipe.predict_proba(X_test_c)[:, 1]  # P(class=1)
print(f"Test Accuracy: {lr_pipe.score(X_test_c, y_test_c):.4f}")
 
# Multi-class: multinomial or one-vs-rest
lr_multi = LogisticRegression(multi_class="multinomial",
                               solver="lbfgs", max_iter=1000)
 
# ── Regularisation for Logistic Regression ────────────
# penalty="l2" (default): Ridge regularisation
# penalty="l1" (need solver="liblinear" or "saga"): Lasso = feature selection
# penalty="elasticnet" (need solver="saga"): Elastic Net</pre></div>
  </div>
</div>
</div>

<div id="t5" class="tab-pane">
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📈</span><h3>Polynomial Regression — Non-Linear Relationships</h3><span class="tag tag-green">Extensions</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
import numpy as np
import matplotlib.pyplot as plt
 
# ── Polynomial features expand input space ────────────
# For 1 feature x: degree=2 adds [1, x, x²]
# For 2 features x, y: degree=2 adds [1, x, y, x², xy, y²]
# The model is still LINEAR in parameters (just in a higher-dim space)
 
# Example: 1D regression to visualise
np.random.seed(42)
X_1d = np.linspace(0, 10, 100).reshape(-1, 1)
y_curve = np.sin(X_1d).ravel() + 0.2 * np.random.randn(100)
 
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for i, degree in enumerate([1, 3, 10]):
    pipe = Pipeline([
        ("poly",  PolynomialFeatures(degree=degree, include_bias=False)),
        ("ridge", Ridge(alpha=0.01)),
    ])
    pipe.fit(X_1d, y_curve)
    y_fit = pipe.predict(X_1d)
    axes[i].scatter(X_1d, y_curve, s=10, alpha=0.5)
    axes[i].plot(X_1d, y_fit, color="red", linewidth=2)
    axes[i].set_title(f"Degree {degree}")
plt.suptitle("Polynomial Regression: Underfitting → Overfitting")
 
# ── For tabular data: selective polynomial features ───
# Adding degree=2 to ALL features: explodes dimensionality
# n features → n + n*(n+1)/2 features with degree=2
# 50 features → 1325 features (often too many)
# Better: add polynomial terms only for key features
 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.compose import ColumnTransformer
 
# Add squared term for GrLivArea only
poly_features = ["GrLivArea", "TotalBsmtSF"]
poly_pipe = Pipeline([
    ("poly", PolynomialFeatures(degree=2, include_bias=False)),
    ("ridge", Ridge(alpha=10.0))
])
 
cv_linear = cross_val_score(
    Pipeline([("scale", StandardScaler()), ("model", Ridge(alpha=10.0))]),
    X_train, y_train, cv=5, scoring="r2"
).mean()
 
cv_poly = cross_val_score(
    Pipeline([("poly", PolynomialFeatures(degree=2)), ("scale", StandardScaler()),
              ("model", Ridge(alpha=10.0))]),
    X_train[poly_features], y_train, cv=5, scoring="r2"
).mean()
 
print(f"Linear R²:     {cv_linear:.4f}")
print(f"Polynomial R²: {cv_poly:.4f}")</pre></div>
    <div class="warn"><p>⚠️ <strong>Polynomial features are a double-edged sword.</strong> Degree=2 on 50 features creates 1,325 features; degree=3 creates 23,426. This causes extreme overfitting unless you add strong regularisation (Ridge with large alpha). Always validate with cross-validation and compare to the linear baseline before committing to polynomial expansion.</p></div>
  </div>
</div>
</div>

<div id="t6" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Regression Metrics — Choosing the Right Score</h3><span class="tag tag-blue">Evaluation</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.metrics import (mean_absolute_error, mean_squared_error,
                             root_mean_squared_error, r2_score,
                             mean_absolute_percentage_error)
import numpy as np
 
y_true = y_test
y_pred = pipeline.predict(X_test)
 
# ── MAE: Mean Absolute Error ──────────────────────────
# Average absolute difference. Same units as target.
# Robust to outliers (vs MSE/RMSE which square errors)
# Easy to explain: "on average, predictions are off by $X"
mae = mean_absolute_error(y_true, y_pred)
print(f"MAE:  ${mae:,.0f}")
 
# ── MSE: Mean Squared Error ───────────────────────────
# Squares errors → large errors penalised more heavily
# NOT in target units (hard to interpret directly)
# Used as training loss (differentiable)
mse = mean_squared_error(y_true, y_pred)
print(f"MSE:  ${mse:,.0f}")
 
# ── RMSE: Root Mean Squared Error ────────────────────
# sqrt(MSE) — back in target units
# Most common metric for regression
# More sensitive to large errors than MAE
rmse = root_mean_squared_error(y_true, y_pred)
print(f"RMSE: ${rmse:,.0f}")
 
# ── R²: Coefficient of Determination ─────────────────
# Proportion of variance explained: R² = 1 - SS_res/SS_tot
# R² = 1.0: perfect prediction
# R² = 0.0: as good as predicting the mean (useless model)
# R² < 0.0: WORSE than predicting the mean (seriously bad)
r2 = r2_score(y_true, y_pred)
print(f"R²:   {r2:.4f}")
 
# ── MAPE: Mean Absolute Percentage Error ─────────────
# Percentage error. Intuitive but problematic near zero.
# "Predictions are X% off on average"
mape = mean_absolute_percentage_error(y_true, y_pred)
print(f"MAPE: {mape:.2%}")
 
# ── When to use each ──────────────────────────────────
print("""
MAE:  Use when outliers exist and you want robust metric
      Use to communicate to stakeholders ("off by $X")
RMSE: Use when large errors are unacceptable (safety, medical)
      Standard metric for Kaggle regression competitions
R²:   Use to compare models on same dataset
      Useful relative metric: 0.85 >> 0.70
MAPE: Use for business reporting when % errors matter
      AVOID when target can be near zero
""")</pre></div>
  </div>
</div>
</div>

<div id="t7" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Video</td><td><a href="https://www.youtube.com/c/joshstarmer" target="_blank" rel="noopener">StatQuest — Linear Regression, Ridge, Lasso (YouTube)</a></td><td>Best visual intuition for what regularisation actually does to coefficients. Highly recommended.</td></tr>
    <tr><td class="res-type">Course</td><td><a href="https://www.kaggle.com/learn/intro-to-machine-learning" target="_blank" rel="noopener">Kaggle Intro to ML Course — kaggle.com/learn/intro-to-machine-learning</a></td><td>Practical sklearn regression from scratch. Includes real Kaggle competition exercises.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://scikit-learn.org/stable/supervised_learning.html" target="_blank" rel="noopener">Scikit-learn Supervised Learning Guide — scikit-learn.org/stable/supervised_learning.html</a></td><td>Complete reference for all linear models, decision trees, SVMs with parameters explained.</td></tr>
    <tr><td class="res-type">Book</td><td><a href="https://github.com/ageron/handson-ml3" target="_blank" rel="noopener">Hands-On ML (Free Chapter 4) — github.com/ageron/handson-ml3</a></td><td>Chapter 4 covers linear regression, polynomial, regularisation with excellent visualisations.</td></tr>
    <tr><td class="res-type">Dataset</td><td><a href="https://www.kaggle.com/c/house-prices-advanced-regression-techniques" target="_blank" rel="noopener">House Prices — Kaggle</a></td><td>Standard regression benchmark. Compare your model against the public leaderboard.</td></tr>
  </tbody>
</table>
</div>

<div id="t8" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">House Price Predictor — From Linear to Ridge to Lasso</span><span class="proj-dur">[Intermediate] 5–6 days</span></div>
  <div class="proj-body">
    <p>Build a progression of regression models and compare them systematically.</p>
    <h4>Requirements</h4>
    <ul>
      <li><strong>Baseline</strong> — Linear Regression with raw features. 5-fold CV R² and RMSE.</li>
      <li><strong>Engineered features</strong> — add TotalSF, HouseAge, TotalBath, QualArea. Does CV R² improve?</li>
      <li><strong>Ridge</strong> — use RidgeCV to find optimal alpha. Compare to baseline.</li>
      <li><strong>Lasso</strong> — use LassoCV. How many features are zeroed? Are the zeroed features meaningful?</li>
      <li><strong>Target transform</strong> — predict log(SalePrice), compare RMSE after expm1() inversion</li>
      <li><strong>Results table</strong> — DataFrame comparing all models: CV R², CV RMSE, n_features used</li>
      <li><strong>Leaderboard</strong> — submit to Kaggle and report your score</li>
    </ul>
  </div>
</div>
</div>

<div id="t9" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Linear Regression Internals</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>Implement linear regression from scratch using the normal equation β = (XᵀX)⁻¹Xᵀy with numpy. Apply to a 2-feature subset. Compare coefficients to sklearn's output.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Plot residuals vs fitted values. Do residuals show a fan shape (heteroscedasticity)? What does this mean for the validity of your p-values?</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Apply log transform to SalePrice. Refit the model. Compare: raw RMSE vs RMSE after converting log predictions back to price. Which model has better absolute dollar accuracy?</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Ridge vs Lasso Comparison</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>Build both RidgeCV and LassoCV models with the same 50-feature set. Compare: CV R², number of non-zero features, and the 5 most important features in each model.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Plot coefficient values for both models side-by-side on a bar chart. Which features does Lasso zero out that Ridge keeps? Are they the most correlated features (multicollinear)?</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Add 20 random noise features (np.random.randn) to the dataset. Refit Ridge and Lasso. Does Lasso zero out the noise features? Does Ridge shrink them or keep them?</div></div>
  </div>
</div>
</div>

<div id="t10" class="tab-pane">
<p class="sep">P3-M07 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain what OLS minimises (sum of squared residuals) and why</li>
  <li>Can interpret regression coefficients: "holding all else constant, 1-unit increase in X changes y by β"</li>
  <li>Can plot and interpret residuals vs fitted values (checking homoscedasticity)</li>
  <li>Know Ridge adds L2 (β²) penalty: shrinks all coefficients, none to zero</li>
  <li>Know Lasso adds L1 (|β|) penalty: drives some coefficients to exactly zero (feature selection)</li>
  <li>Can use RidgeCV and LassoCV to find optimal alpha via cross-validation</li>
  <li>Can visualise coefficient shrinkage path across alpha values</li>
  <li>Know Elastic Net combines L1+L2 and when to prefer it over Ridge or Lasso</li>
  <li>Can apply PolynomialFeatures and understand the dimensionality explosion risk</li>
  <li>Can compute MAE, RMSE, R², and MAPE and know when to use each</li>
  <li>Know that R² &lt; 0 means the model is worse than predicting the mean</li>
  <li>Can build and evaluate a Pipeline with preprocessing + regularised regression</li>
  <li>Completed project: House Prices with Linear, Ridge, Lasso compared in a results table</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P3-M08 — Classification</strong>: logistic regression, decision trees, random forest, and SVM.</p>
</div>
</div>

<div class="mod-nav">
  <a href="/learning/ai-ml/part2-stats-eda/p2-m06-ml-workflow/">← P2-M06: ML Workflow</a>
  <a href="/learning/ai-ml/ai-ml-roadmap/">🗺️ All Modules</a>
  <a class="nb" href="/learning/ai-ml/part3-classical-ml/p3-m08-classification/">Next: P3-M08 — Classification →</a>
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
    const key = 'p3m07_ck_' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
