---
layout: default
title: "P3-M08 - Classification: Decision Trees, Random Forest & SVM"
permalink: /learning/ai-ml/part3-classical-ml/p3-m08-classification/
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
  <div class="mod-eyebrow">Part 3 — Classical ML &nbsp;·&nbsp; Module 8 of 28</div>
  <div class="mod-title">Classification: Decision Trees, Random Forest &amp; SVM</div>
  <div class="mod-subtitle">Predict discrete categories — algorithms, metrics, thresholds, and imbalanced data</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 2 Weeks</span>
    <span class="mod-pill">🟡 Intermediate</span>
    <span class="mod-pill">🔧 scikit-learn · imbalanced-learn · shap</span>
    <span class="mod-pill">📋 Prerequisite: P3-M07</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🌳 Decision Trees</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🌲 Random Forest</button>
  <button class="tab-btn" onclick="vt(event,'t3')">📏 SVM</button>
  <button class="tab-btn" onclick="vt(event,'t4')">📊 Metrics</button>
  <button class="tab-btn" onclick="vt(event,'t5')">⚖ Imbalanced Data</button>
  <button class="tab-btn" onclick="vt(event,'t6')">🔍 Feature Importance</button>
  <button class="tab-btn" onclick="vt(event,'t7')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t9')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t10')">✅ Checklist</button>
</div>

<div id="t0" class="tab-pane active">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-pink">Part 3</span></div>
  <div class="cp-body">
    <p>Classification predicts which discrete category an input belongs to: spam or not spam, disease or healthy, which product category. This module covers the most important classical classification algorithms and — critically — how to evaluate them correctly.</p>
    <ul>
      <li><strong>Decision Trees</strong> — splitting logic, Gini vs entropy, depth control, overfitting</li>
      <li><strong>Random Forest</strong> — bagging, feature subsampling, out-of-bag score, tuning</li>
      <li><strong>SVM (Support Vector Machine)</strong> — maximum margin classifier, kernels, C parameter</li>
      <li><strong>Classification metrics</strong> — accuracy, precision, recall, F1, ROC-AUC, confusion matrix</li>
      <li><strong>Imbalanced data</strong> — class weights, SMOTE, threshold tuning, F1 vs accuracy</li>
      <li><strong>Feature importance</strong> — tree-based, permutation importance, SHAP values</li>
    </ul>
    <div class="ins"><p>💡 <strong>Accuracy is almost never the right metric.</strong> If 99% of transactions are legitimate and 1% are fraud, a model that predicts "legitimate" for everything gets 99% accuracy — and catches zero fraud. Use precision, recall, F1, and ROC-AUC for imbalanced problems.</p></div>
  </div>
</div>
</div>

<div id="t1" class="tab-pane">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">🌳</span><h3>Decision Trees — Interpretable Splitting</h3><span class="tag tag-pink">Foundation</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import numpy as np

X, y = load_breast_cancer(return_X_y=True, as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                      stratify=y, random_state=42)

# ── Basic decision tree ───────────────────────────────
# criterion="gini": Gini impurity (default, slightly faster)
# criterion="entropy": information gain (often similar results)
# max_depth: most important hyperparameter. None = overfit!
# min_samples_split: minimum samples needed to split a node
# min_samples_leaf: minimum samples required in a leaf node

dt = DecisionTreeClassifier(
    max_depth=4,           # limit depth to prevent overfitting
    min_samples_leaf=5,    # at least 5 samples per leaf
    criterion="gini",
    random_state=42
)
dt.fit(X_train, y_train)
print(f"Train accuracy: {dt.score(X_train, y_train):.4f}")
print(f"Test accuracy:  {dt.score(X_test, y_test):.4f}")

# ── Visualise the tree ────────────────────────────────
fig, ax = plt.subplots(figsize=(20, 8))
plot_tree(dt, feature_names=X.columns, class_names=["malignant", "benign"],
          filled=True, rounded=True, ax=ax, fontsize=8)
plt.tight_layout()
plt.savefig("decision_tree.png", dpi=100)

# Text representation (shareable without plot)
print(export_text(dt, feature_names=list(X.columns)))

# ── Overfitting demonstration ─────────────────────────
train_scores, test_scores = [], []
depths = range(1, 20)
for d in depths:
    dt_d = DecisionTreeClassifier(max_depth=d, random_state=42)
    dt_d.fit(X_train, y_train)
    train_scores.append(dt_d.score(X_train, y_train))
    test_scores.append(dt_d.score(X_test, y_test))

plt.figure(figsize=(8, 4))
plt.plot(depths, train_scores, label="Train", marker="o", markersize=4)
plt.plot(depths, test_scores,  label="Test",  marker="s", markersize=4)
plt.xlabel("Max Depth")
plt.ylabel("Accuracy")
plt.title("Decision Tree: Depth vs Accuracy (Bias-Variance Tradeoff)")
plt.legend()
plt.axvline(depths[np.argmax(test_scores)], color="red", linestyle="--",
            label=f"Best depth={depths[np.argmax(test_scores)]}")</pre></div>
    <div class="ins"><p>💡 <strong>Decision trees with no depth limit overfit perfectly.</strong> They memorise every training example. The tree depth is the primary bias-variance dial: shallow = high bias (underfitting), deep = high variance (overfitting). max_depth=4 is a good starting point. Always compare train vs test accuracy — a gap of more than 5% suggests overfitting.</p></div>
  </div>
</div>
</div>

<div id="t2" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🌲</span><h3>Random Forest — Ensemble of Trees</h3><span class="tag tag-blue">Ensemble</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
import pandas as pd

# ── How Random Forest works ───────────────────────────
# 1. Bootstrap: sample N rows WITH replacement (bagging)
# 2. Feature subsampling: at each split, only consider sqrt(n_features) features
# 3. Train one deep tree per bootstrap sample
# 4. Predict: majority vote of all trees (reduces variance)
# Result: lower variance than single tree, still low bias

rf = RandomForestClassifier(
    n_estimators=100,      # number of trees (more = better until diminishing returns)
    max_depth=None,        # trees are grown deep (bagging reduces variance)
    max_features="sqrt",   # sqrt(n_features) features per split (default for clf)
    min_samples_leaf=1,    # default for RF (deep trees are fine)
    n_jobs=-1,             # use all CPU cores
    random_state=42,
    oob_score=True         # out-of-bag evaluation (free validation!)
)
rf.fit(X_train, y_train)

print(f"OOB Score:    {rf.oob_score_:.4f}")   # no held-out set needed!
print(f"Train Acc:    {rf.score(X_train, y_train):.4f}")
print(f"Test Acc:     {rf.score(X_test, y_test):.4f}")

# Cross-validation
cv_scores = cross_val_score(rf, X, y, cv=5, scoring="f1")
print(f"CV F1: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

# ── Hyperparameter tuning ─────────────────────────────
# Key hyperparameters to tune:
# n_estimators: 100-500 (more is almost always better, just slower)
# max_depth: None or 10-30 (deep is OK for RF due to averaging)
# max_features: "sqrt", "log2", or float (0.3 = 30% of features)
# min_samples_leaf: 1-10 (increasing reduces overfitting)

param_grid = {
    "n_estimators": [100, 200],
    "max_features": ["sqrt", 0.3],
    "min_samples_leaf": [1, 3, 5],
}
gs = GridSearchCV(RandomForestClassifier(random_state=42, n_jobs=-1),
                  param_grid, cv=3, scoring="f1", n_jobs=-1, verbose=1)
gs.fit(X_train, y_train)
print(f"Best params: {gs.best_params_}")
print(f"Best CV F1:  {gs.best_score_:.4f}")</pre></div>
    <div class="ins"><p>💡 <strong>oob_score=True gives you a free validation score.</strong> Each tree in the forest is trained on ~63% of rows (bootstrap sample). The remaining ~37% (out-of-bag samples) are used to evaluate that tree's predictions — without any held-out set. The OOB score is a reliable estimate of generalisation performance and is fast to compute.</p></div>
  </div>
</div>
</div>

<div id="t3" class="tab-pane">
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📏</span><h3>Support Vector Machine (SVM)</h3><span class="tag tag-teal">Maximum Margin</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, RandomizedSearchCV
from scipy.stats import loguniform

# ── SVM concept ───────────────────────────────────────
# Finds the hyperplane that maximises the margin between classes
# Support vectors: the training points closest to the decision boundary
# C parameter: tradeoff between margin width and misclassification
#   Small C: wide margin, allows more misclassification (regularised)
#   Large C: narrow margin, fewer misclassifications (overfit risk)
# Kernel: maps data to higher-dimensional space for non-linear boundaries

# ── CRITICAL: SVM requires feature scaling ────────────
svm_pipe = Pipeline([
    ("scaler", StandardScaler()),   # SVM is NOT scale-invariant
    ("svm",    SVC(kernel="rbf", C=1.0, gamma="scale",
                   probability=True, random_state=42)),
])
svm_pipe.fit(X_train, y_train)

print(f"Test Accuracy: {svm_pipe.score(X_test, y_test):.4f}")

# Get probabilities for ROC-AUC
proba = svm_pipe.predict_proba(X_test)[:, 1]

# ── Kernel choice ─────────────────────────────────────
# "linear": good for high-dimensional sparse data (text)
# "rbf": good default for most tabular data (radial basis function)
# "poly": polynomial kernel (degree parameter)

# ── Hyperparameter search ─────────────────────────────
# C and gamma interact — tune together with log-uniform distribution
param_dist = {
    "svm__C":     loguniform(0.01, 1000),  # 0.01 to 1000
    "svm__gamma": loguniform(1e-4, 1.0),   # 1e-4 to 1.0
}
rs = RandomizedSearchCV(svm_pipe, param_dist, n_iter=20, cv=3,
                        scoring="f1", random_state=42)
rs.fit(X_train, y_train)
print(f"Best C:     {rs.best_params_['svm__C']:.4f}")
print(f"Best gamma: {rs.best_params_['svm__gamma']:.6f}")
print(f"Best CV F1: {rs.best_score_:.4f}")</pre></div>
    <div class="ins"><p>💡 <strong>SVM with RBF kernel is often competitive with Random Forest on small-to-medium datasets.</strong> It is a strong default when: dataset &lt; 10,000 rows, features are dense (tabular), you need probabilistic outputs. Its weakness: does not scale well to large datasets (O(n²) memory), slow to tune. For &gt;50,000 rows, use tree-based models.</p></div>
  </div>
</div>
</div>

<div id="t4" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Classification Metrics — Beyond Accuracy</h3><span class="tag tag-purple">Critical</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score, confusion_matrix,
                             classification_report, RocCurveDisplay,
                             PrecisionRecallDisplay)
import matplotlib.pyplot as plt
import seaborn as sns

y_pred  = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

# ── The four classification outcomes ─────────────────
# True Positive  (TP): predicted positive, actually positive
# True Negative  (TN): predicted negative, actually negative
# False Positive (FP): predicted positive, actually negative (Type I error)
# False Negative (FN): predicted negative, actually positive (Type II error)

# ── Core metrics ──────────────────────────────────────
accuracy  = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)  # TP / (TP + FP)
recall    = recall_score(y_test, y_pred)     # TP / (TP + FN) = sensitivity
f1        = f1_score(y_test, y_pred)         # harmonic mean of precision & recall
roc_auc   = roc_auc_score(y_test, y_proba)  # area under ROC curve

print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}   (when I say positive, how often am I right?)")
print(f"Recall:    {recall:.4f}   (how many actual positives did I catch?)")
print(f"F1 Score:  {f1:.4f}   (harmonic mean of precision and recall)")
print(f"ROC-AUC:   {roc_auc:.4f}  (probability correct positive ranked above negative)")

# ── Confusion matrix ──────────────────────────────────
cm = confusion_matrix(y_test, y_pred)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Pred Neg", "Pred Pos"],
            yticklabels=["Actual Neg", "Actual Pos"], ax=axes[0])
axes[0].set_title("Confusion Matrix")

# ROC curve
RocCurveDisplay.from_estimator(model, X_test, y_test, ax=axes[1])
axes[1].set_title(f"ROC Curve (AUC={roc_auc:.3f})")
plt.tight_layout()

# Full classification report
print(classification_report(y_test, y_pred, target_names=["Neg", "Pos"]))

# ── Threshold tuning ──────────────────────────────────
# Default threshold = 0.5. Adjust based on business need.
# Lower threshold (e.g. 0.3): catch more positives (higher recall, lower precision)
# Higher threshold (e.g. 0.7): more confident positives (higher precision, lower recall)

thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]
for t in thresholds:
    y_t = (y_proba >= t).astype(int)
    print(f"t={t:.1f}: precision={precision_score(y_test, y_t):.3f}, "
          f"recall={recall_score(y_test, y_t):.3f}, "
          f"f1={f1_score(y_test, y_t):.3f}")</pre></div>
    <div class="warn"><p>⚠️ <strong>When to use each metric:</strong> Accuracy — only for balanced classes. Precision — when false positives are costly (spam filter: don't block real emails). Recall — when false negatives are costly (cancer screening: don't miss actual cancer). F1 — when both FP and FN matter. ROC-AUC — when you need threshold-independent comparison across models.</p></div>
  </div>
</div>
</div>

<div id="t5" class="tab-pane">
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚖</span><h3>Imbalanced Data — When Classes Are Skewed</h3><span class="tag tag-red">Critical for Real Data</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.utils.class_weight import compute_class_weight
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, classification_report
import numpy as np

# ── Detect class imbalance ────────────────────────────
print(pd.Series(y_train).value_counts())
print(pd.Series(y_train).value_counts(normalize=True))
# If 95% negative, 5% positive → severe imbalance

# ── Solution 1: class_weight="balanced" (easiest) ────
# Adjusts sample weights so each class contributes equally to loss
# No data modification, no SMOTE complexity
rf_balanced = RandomForestClassifier(
    class_weight="balanced",  # automatically weights minority class higher
    n_estimators=100,
    random_state=42, n_jobs=-1
)
rf_balanced.fit(X_train, y_train)
print(f"F1 (balanced weights): {f1_score(y_test, rf_balanced.predict(X_test)):.4f}")

# Compute weights manually
classes = np.unique(y_train)
weights = compute_class_weight("balanced", classes=classes, y=y_train)
weight_dict = dict(zip(classes, weights))
print(f"Class weights: {weight_dict}")

# ── Solution 2: SMOTE — Synthetic Minority Oversampling ──
# Generates synthetic minority-class samples by interpolating between
# existing minority samples in feature space
# USE: when minority class has <10% representation

smote = SMOTE(random_state=42, k_neighbors=5)
X_res, y_res = smote.fit_resample(X_train, y_train)
print(f"Before SMOTE: {pd.Series(y_train).value_counts().to_dict()}")
print(f"After SMOTE:  {pd.Series(y_res).value_counts().to_dict()}")

# SMOTE MUST be inside a pipeline (not applied to test data)
imb_pipe = ImbPipeline([
    ("smote", SMOTE(random_state=42)),
    ("rf",    RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1))
])
from sklearn.model_selection import cross_val_score
cv_f1 = cross_val_score(imb_pipe, X_train, y_train, cv=5, scoring="f1")
print(f"SMOTE Pipeline CV F1: {cv_f1.mean():.3f}")

# ── Solution 3: Threshold tuning ─────────────────────
# Default 0.5 threshold biased toward majority class
# For imbalanced data, optimal threshold is often lower
proba = rf_balanced.predict_proba(X_test)[:, 1]
from sklearn.metrics import precision_recall_curve
prec, rec, thresholds = precision_recall_curve(y_test, proba)
f1_scores = 2 * (prec * rec) / (prec + rec + 1e-9)
best_threshold = thresholds[np.argmax(f1_scores)]
print(f"Optimal threshold: {best_threshold:.3f}")</pre></div>
  </div>
</div>
</div>

<div id="t6" class="tab-pane">
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Feature Importance and SHAP Values</h3><span class="tag tag-green">Interpretability</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import shap
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.inspection import permutation_importance

# ── Method 1: Tree-based feature importance ───────────
# Built into sklearn tree models
# Based on total reduction in Gini impurity due to each feature
# WARNING: biased toward high-cardinality features
importances = pd.Series(rf.feature_importances_, index=X.columns)
importances.sort_values(ascending=False).head(15).plot(kind="barh")
plt.title("Random Forest Feature Importance")

# ── Method 2: Permutation Importance ─────────────────
# Shuffle each feature independently, measure performance drop
# More reliable than built-in importance, not biased by cardinality
# SLOW on large datasets

result = permutation_importance(rf, X_test, y_test, n_repeats=10,
                                 random_state=42, scoring="f1")
perm_df = pd.DataFrame({"importance": result.importances_mean,
                          "std": result.importances_std},
                         index=X.columns).sort_values("importance", ascending=False)
print(perm_df.head(10))

# ── Method 3: SHAP Values ─────────────────────────────
# SHapley Additive exPlanations — game-theory-based feature contributions
# Explains EACH individual prediction (not just global importance)
# For tree models: exact (fast); for others: approximation

explainer = shap.TreeExplainer(rf)
shap_values = explainer.shap_values(X_test)

# Summary plot: global feature importance + direction
shap.summary_plot(shap_values[:, :, 1], X_test, plot_type="bar")    # bar
shap.summary_plot(shap_values[:, :, 1], X_test)                      # beeswarm (better)

# Individual prediction explanation
idx = 0  # first test sample
shap.waterfall_plot(shap.Explanation(values=shap_values[1][idx],
                                     base_values=explainer.expected_value[1],
                                     data=X_test.iloc[idx]))</pre></div>
  </div>
</div>
</div>

<div id="t7" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Video</td><td><a href="https://www.youtube.com/c/joshstarmer" target="_blank" rel="noopener">StatQuest — Decision Trees, Random Forest, ROC-AUC (YouTube)</a></td><td>Best visual explanation of how trees split, bagging works, and what ROC-AUC measures.</td></tr>
    <tr><td class="res-type">Course</td><td><a href="https://www.kaggle.com/learn/machine-learning-explainability" target="_blank" rel="noopener">Kaggle ML Explainability Course — kaggle.com/learn/machine-learning-explainability</a></td><td>SHAP values, permutation importance, partial dependence plots. Free, interactive.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://scikit-learn.org/stable/supervised_learning.html" target="_blank" rel="noopener">Scikit-learn Supervised Learning — scikit-learn.org/stable/supervised_learning.html</a></td><td>Complete parameters for all classifiers. Authoritative reference.</td></tr>
    <tr><td class="res-type">Dataset</td><td><a href="https://archive.ics.uci.edu/dataset/45/heart+disease" target="_blank" rel="noopener">Heart Disease Dataset — UCI ML Repository</a></td><td>Binary classification, medical features, real clinical relevance. Great for recall/precision analysis.</td></tr>
    <tr><td class="res-type">Dataset</td><td><a href="https://www.kaggle.com/c/titanic" target="_blank" rel="noopener">Titanic — Kaggle</a></td><td>Classic binary classification benchmark with a well-documented competitive leaderboard.</td></tr>
  </tbody>
</table>
</div>

<div id="t8" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">Heart Disease Classifier with SHAP Analysis</span><span class="proj-dur">[Intermediate] 5–6 days</span></div>
  <div class="proj-body">
    <p>Build a medical classification pipeline with full interpretability.</p>
    <h4>Requirements</h4>
    <ul>
      <li><strong>EDA</strong> — class balance, feature distributions by class, correlation matrix</li>
      <li><strong>Baseline</strong> — Logistic Regression with StandardScaler. Report accuracy, precision, recall, F1, ROC-AUC.</li>
      <li><strong>Decision Tree</strong> — tune max_depth with cross-validation. Visualise tree with plot_tree.</li>
      <li><strong>Random Forest</strong> — tune n_estimators, max_features. Use oob_score. Report feature importances.</li>
      <li><strong>Class imbalance</strong> — apply class_weight="balanced". Compare F1 with and without.</li>
      <li><strong>SHAP analysis</strong> — summary plot, waterfall plot for a correctly and incorrectly classified patient</li>
      <li><strong>Results table</strong> — compare all models on accuracy, F1, ROC-AUC</li>
    </ul>
    <p><strong>Goal:</strong> Achieve ROC-AUC &gt; 0.90. What clinical insight do the SHAP values provide?</p>
  </div>
</div>
</div>

<div id="t9" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Classification Metrics Deep Dive</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>Build a Random Forest on Titanic. Calculate TP, FP, FN, TN manually from the confusion matrix. Verify they match precision_score() and recall_score() outputs.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Plot the ROC curve. What does the curve represent? Where is the point corresponding to threshold=0.5? Try threshold=0.3 and 0.7 — add those points to the ROC plot.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Using the precision-recall curve, find the threshold that maximises F1. How does this threshold differ from 0.5? In a medical context (predicting disease), would you prefer higher precision or recall?</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Bias-Variance with Decision Trees</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>Train Decision Trees at depths 1, 2, 3, 5, 10, 20, None on Heart Disease. Plot train F1 and test F1 vs depth. Identify the elbow — what depth gives best bias-variance tradeoff?</div></div>
    <div class="lab-step"><div class="sn">2</div><div>For the best depth, visualise the tree with plot_tree. Can you explain a single prediction path in plain English? ("For a 65-year-old male with chest pain type X...")</div></div>
  </div>
</div>
</div>

<div id="t10" class="tab-pane">
<p class="sep">P3-M08 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain how a decision tree splits: Gini impurity, information gain</li>
  <li>Can visualise a trained decision tree and trace a single prediction path</li>
  <li>Know max_depth is the primary overfitting control for trees</li>
  <li>Can explain Random Forest: bagging + feature subsampling + majority vote</li>
  <li>Can use oob_score=True as a free validation metric</li>
  <li>Know SVM requires feature scaling and that C controls margin width</li>
  <li>Can compute TP, FP, FN, TN from a confusion matrix</li>
  <li>Can compute accuracy, precision, recall, F1, ROC-AUC and know when to use each</li>
  <li>Know that accuracy is misleading for imbalanced datasets</li>
  <li>Can use class_weight="balanced" and SMOTE for imbalanced data</li>
  <li>Can tune the classification threshold using the precision-recall curve</li>
  <li>Can extract and visualise tree feature importances and permutation importances</li>
  <li>Can generate and interpret SHAP summary and waterfall plots</li>
  <li>Completed project: Heart Disease classifier with SHAP analysis and model comparison table</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>P3-M09 — Ensembles</strong>: XGBoost, LightGBM, SMOTE, Optuna hyperparameter tuning.</p>
</div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/ai-ml/part3-classical-ml/p3-m07-regression/' | relative_url }}">← P3-M07: Regression</a>
  <a href="{{ '/learning/ai-ml/ai-ml-roadmap/' | relative_url }}">🗺️ All Modules</a>
  <a class="nb" href="{{ '/learning/ai-ml/part3-classical-ml/p3-m09-ensembles/' | relative_url }}">Next: P3-M09 — Ensembles →</a>
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
    const key = 'p3m08_ck_' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
