---
layout: default
title: "P3-M09 - Ensembles: XGBoost, LightGBM, SMOTE & Optuna"
permalink: /learning/ai-ml/part3-classical-ml/p3-m09-ensembles/
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
  <div class="mod-eyebrow">Part 3 — Classical ML &nbsp;·&nbsp; Module 9 of 28</div>
  <div class="mod-title">Ensembles: XGBoost, LightGBM, SMOTE &amp; Optuna</div>
  <div class="mod-subtitle">Gradient boosting, stacking, imbalanced data strategies, and automated hyperparameter optimisation</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 2 Weeks</span>
    <span class="mod-pill">🟡 Intermediate–Advanced</span>
    <span class="mod-pill">🔧 xgboost · lightgbm · optuna · imbalanced-learn</span>
    <span class="mod-pill">📋 Prerequisite: P3-M08</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🚀 XGBoost</button>
  <button class="tab-btn" onclick="vt(event,'t2')">💡 LightGBM</button>
  <button class="tab-btn" onclick="vt(event,'t3')">🎯 Optuna</button>
  <button class="tab-btn" onclick="vt(event,'t4')">⚗ SMOTE</button>
  <button class="tab-btn" onclick="vt(event,'t5')">🔗 Stacking</button>
  <button class="tab-btn" onclick="vt(event,'t6')">📊 SHAP Advanced</button>
  <button class="tab-btn" onclick="vt(event,'t7')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t9')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t10')">✅ Checklist</button>
</div>

<div id="t0" class="tab-pane active">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-pink">Part 3</span></div>
  <div class="cp-body">
    <p>Gradient boosting models (XGBoost, LightGBM, CatBoost) dominate Kaggle structured-data competitions. This module covers these industry-standard tools, automated hyperparameter tuning with Optuna, advanced imbalanced-data strategies, and ensemble stacking.</p>
    <ul>
      <li><strong>XGBoost</strong> — gradient boosting, regularisation, early stopping, sklearn API</li>
      <li><strong>LightGBM</strong> — leaf-wise growth, categorical support, faster than XGBoost</li>
      <li><strong>Optuna</strong> — automated hyperparameter search with Bayesian optimisation</li>
      <li><strong>SMOTE variants</strong> — SMOTE, ADASYN, SMOTETomek, BorderlineSMOTE</li>
      <li><strong>Stacking and blending</strong> — combining model predictions as meta-features</li>
      <li><strong>Advanced SHAP</strong> — interaction values, dependence plots, force plots</li>
    </ul>
    <div class="ins"><p>💡 <strong>XGBoost is the starting model for nearly every structured-data ML problem.</strong> It handles missing values natively, is robust to outliers, requires minimal preprocessing (no scaling needed), and is fast. If XGBoost doesn't beat your baseline significantly, your problem may need feature engineering rather than a more complex model.</p></div>
  </div>
</div>
</div>

<div id="t1" class="tab-pane">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">🚀</span><h3>XGBoost — Gradient Boosting Deep Dive</h3><span class="tag tag-pink">Industry Standard</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import xgboost as xgb
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import root_mean_squared_error, roc_auc_score
import pandas as pd, numpy as np

# ── How gradient boosting works ───────────────────────
# 1. Fit a shallow tree (weak learner) to the data
# 2. Compute residuals: where did the model err?
# 3. Fit NEXT tree to the residuals (learns from mistakes)
# 4. Add this tree to the ensemble with a learning rate
# 5. Repeat N times (n_estimators)
# Final prediction = sum of all tree outputs

# ── XGBoost sklearn API (easier) ─────────────────────
from xgboost import XGBClassifier, XGBRegressor

# Regression
model = XGBRegressor(
    n_estimators=500,       # number of boosting rounds
    learning_rate=0.05,     # how much each tree contributes (smaller = needs more trees)
    max_depth=5,            # depth of each tree (shallower = more regularisation)
    subsample=0.8,          # fraction of rows per tree (row sampling)
    colsample_bytree=0.8,   # fraction of features per tree (feature sampling)
    reg_alpha=0.1,          # L1 regularisation (Lasso-like)
    reg_lambda=1.0,         # L2 regularisation (Ridge-like)
    min_child_weight=5,     # minimum sum of weights in a leaf (controls overfitting)
    random_state=42,
    n_jobs=-1,
    # Missing values: XGBoost handles natively — no imputation needed!
)

# ── Early stopping: prevent overfitting automatically ─
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train,
                                              test_size=0.15, random_state=42)
model.fit(
    X_tr, y_tr,
    eval_set=[(X_val, y_val)],
    verbose=50  # print every 50 rounds
)
# Training stops when validation metric hasn't improved for N rounds
# model.best_ntree_limit: optimal number of trees found

print(f"Best iteration: {model.best_iteration}")
print(f"Test RMSE: {root_mean_squared_error(y_test, model.predict(X_test)):,.0f}")

# ── Cross-validation with early stopping ─────────────
import xgboost as xgb

dtrain = xgb.DMatrix(X_train, label=y_train)
params = {
    "max_depth": 5,
    "learning_rate": 0.05,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "reg_lambda": 1.0,
    "objective": "reg:squarederror",
    "eval_metric": "rmse",
    "seed": 42,
}
cv_results = xgb.cv(params, dtrain, num_boost_round=500,
                    nfold=5, early_stopping_rounds=30, verbose_eval=50)
print(f"Best CV RMSE: {cv_results['test-rmse-mean'].min():,.1f}")</pre></div>
    <h4>Key XGBoost Parameters to Tune</h4>
    <ul>
      <li><strong>n_estimators + learning_rate</strong> — always tune together. Lower lr needs more trees. Start: lr=0.1, trees=300. Then lr=0.01, trees=3000.</li>
      <li><strong>max_depth</strong> — 3-8. Deeper = more complex interactions. Default=6 is usually good.</li>
      <li><strong>subsample + colsample_bytree</strong> — 0.6-0.9. Stochastic sampling reduces overfitting.</li>
      <li><strong>min_child_weight</strong> — 1-20. Higher = more conservative splits. Tune for imbalanced data.</li>
      <li><strong>scale_pos_weight</strong> — for classification: sum(neg)/sum(pos). Critical for imbalanced classes.</li>
    </ul>
  </div>
</div>
</div>

<div id="t2" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">💡</span><h3>LightGBM — Faster, Leaf-Wise Boosting</h3><span class="tag tag-blue">Production Choice</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import lightgbm as lgb
from sklearn.model_selection import cross_val_score

# ── LightGBM vs XGBoost ───────────────────────────────
# LightGBM: leaf-wise tree growth (vs XGBoost level-wise)
# → faster training, better accuracy on large datasets
# → more prone to overfitting with small datasets (use num_leaves carefully)
# Native categorical feature support (no OHE needed!)
# Much faster on datasets > 100k rows

model_lgb = lgb.LGBMRegressor(
    n_estimators=1000,
    learning_rate=0.05,
    max_depth=-1,           # -1 = no limit (use num_leaves instead)
    num_leaves=31,          # key LightGBM parameter (≈2^max_depth)
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.1,
    reg_lambda=1.0,
    min_child_samples=20,   # equivalent to min_child_weight in XGBoost
    n_jobs=-1,
    random_state=42,
    verbose=-1,
)

# Native categorical support
# Specify categorical columns — LightGBM handles them without OHE
cat_features = ["MSZoning", "Neighborhood", "SaleType"]
df[cat_features] = df[cat_features].astype("category")

model_lgb.fit(
    X_tr, y_tr,
    eval_set=[(X_val, y_val)],
    callbacks=[lgb.early_stopping(50), lgb.log_evaluation(100)]
)
print(f"Best iteration: {model_lgb.best_iteration_}")

# ── LightGBM cross-validation ─────────────────────────
lgb_train = lgb.Dataset(X_train, label=y_train)
params = {
    "learning_rate": 0.05,
    "num_leaves": 31,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "objective": "regression",
    "metric": "rmse",
    "verbose": -1,
}
cv_result = lgb.cv(params, lgb_train, num_boost_round=1000,
                   nfold=5, callbacks=[lgb.early_stopping(50)])
best_round = len(cv_result["valid rmse-mean"])
print(f"Best round: {best_round}, CV RMSE: {min(cv_result['valid rmse-mean']):,.1f}")</pre></div>
    <div class="ins"><p>💡 <strong>Use LightGBM when your dataset has &gt; 50,000 rows or &gt; 100 features.</strong> It trains 5-20× faster than XGBoost on large datasets. Use XGBoost when you want the most well-documented, stable gradient boosting library with the largest community. Both are excellent — pick LightGBM for speed, XGBoost for documentation.</p></div>
  </div>
</div>
</div>

<div id="t3" class="tab-pane">
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>Optuna — Automated Hyperparameter Tuning</h3><span class="tag tag-teal">Bayesian Optimisation</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import optuna
from sklearn.model_selection import cross_val_score
from xgboost import XGBRegressor
import numpy as np

# ── Why Optuna beats GridSearchCV ─────────────────────
# GridSearch: exhaustively tries all combinations (exponential time)
# RandomSearch: random sampling (efficient but dumb)
# Optuna/Bayesian: uses past trials to guess promising regions
# → finds good params in far fewer trials than GridSearch

optuna.logging.set_verbosity(optuna.logging.WARNING)

def objective(trial):
    """Called by Optuna for each trial. Returns the metric to optimise."""
    params = {
        "n_estimators": trial.suggest_int("n_estimators", 100, 1000),
        "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.3, log=True),
        "max_depth": trial.suggest_int("max_depth", 3, 9),
        "subsample": trial.suggest_float("subsample", 0.5, 1.0),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.5, 1.0),
        "reg_alpha": trial.suggest_float("reg_alpha", 1e-4, 10.0, log=True),
        "reg_lambda": trial.suggest_float("reg_lambda", 1e-4, 10.0, log=True),
        "min_child_weight": trial.suggest_int("min_child_weight", 1, 20),
        "random_state": 42,
        "n_jobs": -1,
    }
    model = XGBRegressor(**params)
    # CV with 3 folds (faster for tuning — use 5 for final evaluation)
    scores = cross_val_score(model, X_train, y_train, cv=3,
                             scoring="neg_root_mean_squared_error")
    return -scores.mean()  # Optuna minimises by default, so negate RMSE

# ── Run Optuna study ──────────────────────────────────
study = optuna.create_study(direction="minimize",
                             sampler=optuna.samplers.TPESampler(seed=42))
study.optimize(objective, n_trials=50, show_progress_bar=True)

best_params = study.best_params
print(f"Best RMSE: {study.best_value:,.0f}")
print(f"Best params: {best_params}")

# ── Use best params for final model ───────────────────
best_model = XGBRegressor(**best_params)
best_model.fit(X_train, y_train)
print(f"Test RMSE: {root_mean_squared_error(y_test, best_model.predict(X_test)):,.0f}")

# ── Visualise Optuna results ──────────────────────────
from optuna.visualization import (plot_optimization_history,
                                   plot_param_importances,
                                   plot_slice)
# Shows how RMSE improved over trials
fig = plot_optimization_history(study)
fig.show()

# Shows which hyperparameters had the most impact
fig = plot_param_importances(study)
fig.show()</pre></div>
    <div class="ins"><p>💡 <strong>For production models, use 100-200 Optuna trials.</strong> The first 20-30 trials explore randomly; subsequent trials exploit the most promising regions. Set a timeout if you need time-bounded tuning: study.optimize(objective, timeout=3600) for 1 hour of tuning.</p></div>
  </div>
</div>
</div>

<div id="t4" class="tab-pane">
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚗</span><h3>SMOTE Variants for Imbalanced Data</h3><span class="tag tag-red">Imbalanced</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from imblearn.over_sampling import SMOTE, ADASYN, BorderlineSMOTE
from imblearn.combine import SMOTETomek, SMOTEENN
from imblearn.pipeline import Pipeline as ImbPipeline
from xgboost import XGBClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import classification_report

# ── SMOTE — Synthetic Minority Oversampling ───────────
# Creates synthetic minority class samples by interpolating between
# k nearest neighbours of existing minority samples
# Result: balanced classes (50/50 by default)
smote = SMOTE(random_state=42, k_neighbors=5, sampling_strategy=1.0)

# ── ADASYN — Adaptive Synthetic Sampling ─────────────
# Like SMOTE but creates MORE synthetic samples near the decision boundary
# (where the classifier struggles most)
adasyn = ADASYN(random_state=42, n_neighbors=5)

# ── BorderlineSMOTE ───────────────────────────────────
# Only oversamples minority points near the decision boundary
# More targeted than vanilla SMOTE
bl_smote = BorderlineSMOTE(random_state=42, kind="borderline-1")

# ── SMOTETomek: oversample + undersample ──────────────
# Apply SMOTE to create synthetic minority samples
# Then remove Tomek links (ambiguous majority samples near boundary)
# Best of both: less noisy than pure SMOTE
smote_tomek = SMOTETomek(random_state=42)

# ── XGBoost alternative: scale_pos_weight ─────────────
# For binary classification: no resampling needed
# scale_pos_weight = sum(negative) / sum(positive)
neg = (y_train == 0).sum()
pos = (y_train == 1).sum()
scale = neg / pos
print(f"scale_pos_weight: {scale:.2f}")

xgb_imb = XGBClassifier(scale_pos_weight=scale, n_estimators=300,
                          random_state=42, n_jobs=-1)

# ── Compare strategies with CV ────────────────────────
strategies = {
    "XGB no correction":   ImbPipeline([("xgb", XGBClassifier(n_estimators=300, random_state=42))]),
    "XGB scale_pos":       ImbPipeline([("xgb", XGBClassifier(scale_pos_weight=scale, n_estimators=300, random_state=42))]),
    "SMOTE + XGB":         ImbPipeline([("smote", SMOTE(random_state=42)), ("xgb", XGBClassifier(n_estimators=300, random_state=42))]),
    "SMOTETomek + XGB":    ImbPipeline([("smote", SMOTETomek(random_state=42)), ("xgb", XGBClassifier(n_estimators=300, random_state=42))]),
}
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for name, pipe in strategies.items():
    f1 = cross_val_score(pipe, X_train, y_train, cv=skf, scoring="f1").mean()
    print(f"{name:30s}: F1 = {f1:.3f}")</pre></div>
  </div>
</div>
</div>

<div id="t5" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Stacking and Blending</h3><span class="tag tag-purple">Advanced Ensembles</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.ensemble import StackingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score

# ── Voting Ensemble ───────────────────────────────────
# Simplest ensemble: combine predictions from multiple models
# hard voting: majority class vote
# soft voting: average of predicted probabilities (better)
voting = VotingClassifier(estimators=[
    ("rf",  RandomForestClassifier(n_estimators=100, random_state=42)),
    ("xgb", XGBClassifier(n_estimators=200, random_state=42)),
    ("lr",  LogisticRegression(max_iter=1000)),
], voting="soft", n_jobs=-1)

cv_voting = cross_val_score(voting, X_train, y_train, cv=5, scoring="roc_auc")
print(f"Voting CV AUC: {cv_voting.mean():.3f}")

# ── Stacking ──────────────────────────────────────────
# Level-0 estimators: base models, trained on K-fold subsets
# Level-1 estimator: meta-learner trained on base model predictions
# Stacking uses cross-validation to generate level-0 predictions
# to avoid the meta-learner overfitting to training data

stacking = StackingClassifier(
    estimators=[
        ("rf",  RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=42)),
        ("xgb", XGBClassifier(n_estimators=200, random_state=42)),
        ("gb",  GradientBoostingClassifier(n_estimators=100, random_state=42)),
    ],
    final_estimator=LogisticRegression(C=0.1, max_iter=1000),
    cv=5,           # K-folds for generating level-0 predictions
    stack_method="predict_proba",  # use probabilities as meta-features
    n_jobs=-1,
    passthrough=False,  # True: also pass original features to meta-learner
)
cv_stacking = cross_val_score(stacking, X_train, y_train, cv=5, scoring="roc_auc")
print(f"Stacking CV AUC: {cv_stacking.mean():.3f}")

# ── Manual blending (simpler, less rigorous than stacking) ──
# Train models on train split, blend predictions on val split
X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.2)
proba_rf  = RandomForestClassifier(n_estimators=100).fit(X_tr, y_tr).predict_proba(X_val)[:, 1]
proba_xgb = XGBClassifier(n_estimators=200).fit(X_tr, y_tr).predict_proba(X_val)[:, 1]
blend = 0.5 * proba_rf + 0.5 * proba_xgb  # simple average
print(f"Blend AUC: {roc_auc_score(y_val, blend):.3f}")</pre></div>
  </div>
</div>
</div>

<div id="t6" class="tab-pane">
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Advanced SHAP — Deep Interpretability</h3><span class="tag tag-green">Interpretability</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import shap
import matplotlib.pyplot as plt
import numpy as np

# ── SHAP for tree models (exact, fast) ────────────────
explainer = shap.TreeExplainer(xgb_model)
shap_values = explainer(X_test)

# shap_values.values: shape (n_samples, n_features)
# shap_values.base_values: baseline prediction (average model output)
# shap_values.data: feature values

# ── Summary plot (global feature importance + direction) ─
shap.summary_plot(shap_values, X_test)
# Each row = one feature. Points = individual samples.
# Red = high feature value, Blue = low feature value
# x-axis: SHAP value (positive = pushes prediction higher)

# ── Bar plot (average |SHAP| per feature) ────────────
shap.summary_plot(shap_values, X_test, plot_type="bar")

# ── Dependence plot: how one feature interacts with another ──
# Shows: SHAP(GrLivArea) vs GrLivArea, coloured by OverallQual
shap.dependence_plot("GrLivArea", shap_values.values, X_test,
                      interaction_index="OverallQual")

# ── Waterfall plot for a single prediction ────────────
# Why did the model predict $250k for this specific house?
idx = 0
shap.plots.waterfall(shap_values[idx])

# ── Force plot: interactive individual prediction ─────
shap.force_plot(explainer.expected_value, shap_values.values[idx],
                X_test.iloc[idx], matplotlib=True)

# ── SHAP for non-tree models (KernelExplainer - slow) ─
# Use when you need SHAP for non-tree models
# KernelSHAP approximates SHAP values using a weighted linear model
explainer_lr = shap.KernelExplainer(lr_model.predict, shap.kmeans(X_train, 50))
shap_lr = explainer_lr.shap_values(X_test[:100])  # small batch (slow)</pre></div>
  </div>
</div>
</div>

<div id="t7" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Docs</td><td><a href="https://xgboost.readthedocs.io/en/stable/" target="_blank" rel="noopener">XGBoost Documentation — xgboost.readthedocs.io</a></td><td>Complete XGBoost reference. Parameter explanations, tutorials, Python API. Authoritative.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://lightgbm.readthedocs.io/en/latest/" target="_blank" rel="noopener">LightGBM Documentation — lightgbm.readthedocs.io</a></td><td>Parameters, performance tips, categorical feature support, full Python API.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://optuna.readthedocs.io/" target="_blank" rel="noopener">Optuna Documentation — optuna.readthedocs.io</a></td><td>Bayesian hyperparameter optimisation. Tutorials, samplers, pruners, visualisation.</td></tr>
    <tr><td class="res-type">Course</td><td><a href="https://www.kaggle.com/learn/intermediate-machine-learning" target="_blank" rel="noopener">Kaggle Intermediate ML — XGBoost section — kaggle.com/learn/intermediate-machine-learning</a></td><td>Hands-on XGBoost with Kaggle exercises. Covers missing values, cross-validation integration.</td></tr>
    <tr><td class="res-type">Dataset</td><td><a href="https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud" target="_blank" rel="noopener">Credit Card Fraud — Kaggle</a></td><td>Severe class imbalance (0.17% fraud). Perfect for SMOTE, scale_pos_weight, and F1 vs AUC comparison.</td></tr>
    <tr><td class="res-type">Dataset</td><td><a href="https://www.kaggle.com/c/porto-seguro-safe-driver-prediction" target="_blank" rel="noopener">Porto Seguro Safe Driver — Kaggle</a></td><td>Industry-standard XGBoost/LightGBM benchmark. Kaggle competition with public discussion.</td></tr>
  </tbody>
</table>
</div>

<div id="t8" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">Credit Card Fraud Detection — Full Pipeline</span><span class="proj-dur">[Advanced] 6–7 days</span></div>
  <div class="proj-body">
    <p>Build a production-ready fraud detection system with all the techniques from this module.</p>
    <h4>Requirements</h4>
    <ul>
      <li><strong>EDA</strong> — class imbalance analysis (only 0.17% fraud), feature distributions by class</li>
      <li><strong>Baseline</strong> — Logistic Regression. Report: accuracy, precision, recall, F1, ROC-AUC. Note that accuracy is misleading.</li>
      <li><strong>XGBoost with scale_pos_weight</strong> — tune with Optuna (50 trials). Report CV F1.</li>
      <li><strong>SMOTE + XGBoost</strong> — use ImbPipeline, compare to scale_pos_weight approach</li>
      <li><strong>Threshold tuning</strong> — find optimal threshold on validation set using PR curve</li>
      <li><strong>SHAP analysis</strong> — which features drive fraud predictions? Surprise any you?</li>
      <li><strong>Final results table</strong> — all models, all metrics, final chosen model with justification</li>
    </ul>
    <p><strong>Target:</strong> F1 &gt; 0.85 on test set. Report both F1 and ROC-AUC (both matter for fraud).</p>
  </div>
</div>
</div>

<div id="t9" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>XGBoost Early Stopping</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>Train XGBoost on House Prices with n_estimators=2000 and learning_rate=0.01. Use early stopping on a 15% validation split. What is the optimal number of rounds? Compare to n_estimators=200 without early stopping.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Plot train RMSE and validation RMSE vs boosting round. At what round does overfitting begin? Annotate on the plot with plt.axvline().</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Run XGBoost CV using xgb.cv(). Compare the best CV RMSE to the early stopping result. Which finds the better model?</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Optuna Tuning</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>Run Optuna with 50 trials on XGBoost for House Prices. Plot the optimisation history. At what trial does the curve flatten? What does this tell you about when to stop searching?</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Run plot_param_importances(study). Which hyperparameter has the most impact on RMSE? Is it what you expected?</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Compare: default XGBoost, manually tuned XGBoost, and Optuna-tuned XGBoost on 5-fold CV RMSE. How much does Optuna improve over manual tuning?</div></div>
  </div>
</div>
</div>

<div id="t10" class="tab-pane">
<p class="sep">P3-M09 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain gradient boosting: sequential trees, residual fitting, learning rate</li>
  <li>Can train XGBoost with early stopping and find the optimal number of boosting rounds</li>
  <li>Know the key XGBoost hyperparameters: n_estimators, learning_rate, max_depth, subsample, colsample_bytree</li>
  <li>Know when to use LightGBM vs XGBoost (large datasets → LightGBM)</li>
  <li>Can set up an Optuna study with suggest_int, suggest_float, and suggest_float(log=True)</li>
  <li>Can interpret Optuna plot_optimization_history and plot_param_importances</li>
  <li>Know at least 3 SMOTE variants and when to use each</li>
  <li>Can use scale_pos_weight for imbalanced XGBoost classification</li>
  <li>Can compare SMOTE vs class weighting vs no correction with StratifiedKFold CV</li>
  <li>Can build a StackingClassifier with sklearn and understand why K-fold is needed</li>
  <li>Can generate SHAP summary plot, dependence plot, and waterfall plot</li>
  <li>Completed project: Credit Card Fraud Detection with Optuna tuning and SHAP analysis</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P3-M10 — Unsupervised Learning</strong>: K-Means, PCA, t-SNE, and customer segmentation.</p>
</div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/ai-ml/part3-classical-ml/p3-m08-classification/' | relative_url }}">← P3-M08: Classification</a>
  <a href="{{ '/learning/ai-ml/ai-ml-roadmap/' | relative_url }}">🗺️ All Modules</a>
  <a class="nb" href="{{ '/learning/ai-ml/part3-classical-ml/p3-m10-unsupervised/' | relative_url }}">Next: P3-M10 — Unsupervised →</a>
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
    const key = 'p3m09_ck_' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
