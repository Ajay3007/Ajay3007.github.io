---
layout: learning
title: "P3-M10 - Unsupervised Learning: K-Means, PCA & t-SNE"
permalink: /learning/ai-ml/part3-classical-ml/p3-m10-unsupervised/
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
.part3-complete{background:linear-gradient(135deg,#0a1a30,#be185d);border-radius:10px;padding:1.5rem 2rem;color:#fff;margin:2rem 0;text-align:center}
.part3-complete h3{color:#fff;border:none;margin:0 0 .5rem;font-size:1.3rem}
.part3-complete p{color:#fce7f3;margin:0;font-size:.9rem}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">Part 3 — Classical ML &nbsp;·&nbsp; Module 10 of 28</div>
  <div class="mod-title">Unsupervised Learning: K-Means, PCA &amp; t-SNE</div>
  <div class="mod-subtitle">Find hidden structure — clustering, dimensionality reduction, and visual exploration</div>
  <div class="mod-pills">
    <span class="mod-pill">⏱ 2 Weeks</span>
    <span class="mod-pill">🟡 Intermediate</span>
    <span class="mod-pill">🔧 scikit-learn · umap-learn · plotly</span>
    <span class="mod-pill">📋 Prerequisite: P3-M09</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">📋 Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">🎯 K-Means</button>
  <button class="tab-btn" onclick="vt(event,'t2')">🏔 DBSCAN</button>
  <button class="tab-btn" onclick="vt(event,'t3')">📉 PCA</button>
  <button class="tab-btn" onclick="vt(event,'t4')">🌀 t-SNE & UMAP</button>
  <button class="tab-btn" onclick="vt(event,'t5')">📊 Cluster Evaluation</button>
  <button class="tab-btn" onclick="vt(event,'t6')">🏢 Segmentation Pipeline</button>
  <button class="tab-btn" onclick="vt(event,'t7')">📚 Resources</button>
  <button class="tab-btn" onclick="vt(event,'t8')">🛠 Projects</button>
  <button class="tab-btn" onclick="vt(event,'t9')">🔬 Labs</button>
  <button class="tab-btn" onclick="vt(event,'t10')">✅ Checklist</button>
</div>

<div id="t0" class="tab-pane active">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>What This Module Covers</h3><span class="tag tag-pink">Part 3 Finale</span></div>
  <div class="cp-body">
    <p>Unsupervised learning finds structure in data without labels. It powers customer segmentation, anomaly detection, data compression, and visualisation of high-dimensional datasets. These techniques are used both standalone and as preprocessing steps for supervised models.</p>
    <ul>
      <li><strong>K-Means clustering</strong> — centroid-based, elbow method, silhouette score, cluster profiling</li>
      <li><strong>DBSCAN</strong> — density-based clustering, handles non-spherical clusters, detects noise</li>
      <li><strong>PCA (Principal Component Analysis)</strong> — dimensionality reduction, explained variance, noise removal</li>
      <li><strong>t-SNE</strong> — non-linear dimensionality reduction for visualisation</li>
      <li><strong>UMAP</strong> — faster than t-SNE, preserves global structure, good for production</li>
      <li><strong>Customer segmentation pipeline</strong> — full RFM analysis and business interpretation</li>
    </ul>
    <div class="ins"><p>💡 <strong>Unsupervised learning results are only as good as your interpretation.</strong> K-Means will always find K clusters — whether or not K clusters truly exist in the data. The hard work is validating that the clusters are meaningful, stable, and actionable for the business.</p></div>
  </div>
</div>
</div>

<div id="t1" class="tab-pane">
<div class="cp p-pink">
  <div class="cp-hdr"><span class="ico">🎯</span><h3>K-Means Clustering — From Basics to Production</h3><span class="tag tag-pink">Foundation</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import pandas as pd, numpy as np

# ── K-Means algorithm ─────────────────────────────────
# 1. Randomly initialise K centroids
# 2. Assign each point to the nearest centroid
# 3. Recompute centroids as mean of assigned points
# 4. Repeat 2-3 until convergence (centroids don't move)
# CRITICAL: K-Means requires feature scaling!

df_seg = pd.read_csv("mall_customers.csv")
features = ["Annual Income (k$)", "Spending Score (1-100)", "Age"]
X = df_seg[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ── Finding optimal K ─────────────────────────────────
# Method 1: Elbow method — plot inertia (WCSS) vs K
inertias = []
sil_scores = []
K_range = range(2, 11)

for k in K_range:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    km.fit(X_scaled)
    inertias.append(km.inertia_)                    # Within-Cluster Sum of Squares
    sil_scores.append(silhouette_score(X_scaled, km.labels_))  # silhouette

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(K_range, inertias, marker="o")
axes[0].set(xlabel="K", ylabel="Inertia (WCSS)", title="Elbow Method")
axes[0].axvline(5, color="red", linestyle="--", label="Chosen K")
axes[1].plot(K_range, sil_scores, marker="o", color="green")
axes[1].set(xlabel="K", ylabel="Silhouette Score", title="Silhouette (higher=better)")
# Silhouette: -1 to 1; near 1 = well separated; near 0 = overlapping

# ── Final model ───────────────────────────────────────
best_k = 5
km_final = KMeans(n_clusters=best_k, n_init=20, random_state=42)
df_seg["Cluster"] = km_final.fit_predict(X_scaled)

# ── Cluster profiling ─────────────────────────────────
cluster_profile = df_seg.groupby("Cluster")[features].mean().round(1)
cluster_sizes   = df_seg["Cluster"].value_counts().sort_index()
cluster_profile["Size"] = cluster_sizes
print(cluster_profile)

# Visualise clusters in 2D (Income vs Spending)
plt.figure(figsize=(8, 6))
for cluster_id in range(best_k):
    mask = df_seg["Cluster"] == cluster_id
    plt.scatter(df_seg.loc[mask, "Annual Income (k$)"],
                df_seg.loc[mask, "Spending Score (1-100)"],
                label=f"Cluster {cluster_id}", s=60, alpha=0.7)
# Plot centroids
centroids = scaler.inverse_transform(km_final.cluster_centers_)
plt.scatter(centroids[:, 0], centroids[:, 1],
            c="black", s=200, marker="X", label="Centroids", zorder=5)
plt.legend()
plt.title(f"K-Means Clusters (K={best_k})")</pre></div>
    <div class="warn"><p>⚠️ <strong>K-Means assumptions:</strong> clusters are spherical (equal shape), have similar sizes, and similar densities. Real-world clusters are often none of these. If your scatter plot shows elongated or irregular clusters, use DBSCAN or Gaussian Mixture Models instead. Always visualise before trusting K-Means results.</p></div>
  </div>
</div>
</div>

<div id="t2" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏔</span><h3>DBSCAN — Density-Based Clustering</h3><span class="tag tag-blue">Arbitrary Shapes</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

# ── DBSCAN concept ────────────────────────────────────
# A point is a "core point" if it has at least min_samples
# neighbours within radius eps
# Clusters grow by connecting core points within eps
# Points that can't be reached: noise (label = -1)
# Advantages: finds arbitrary-shaped clusters, detects noise
# Parameters: eps (neighbourhood radius), min_samples (density threshold)

X_scaled = StandardScaler().fit_transform(X)

# ── Find optimal eps: k-distance plot ────────────────
# For each point, find its 4th nearest neighbour distance
# eps = knee of the sorted distance plot
k = 4  # min_samples - 1
nbrs = NearestNeighbors(n_neighbors=k).fit(X_scaled)
distances, _ = nbrs.kneighbors(X_scaled)
k_distances = np.sort(distances[:, k-1])[::-1]

plt.figure(figsize=(8, 4))
plt.plot(k_distances)
plt.ylabel("4th Nearest Neighbour Distance")
plt.xlabel("Points sorted by distance")
plt.title("K-Distance Plot: Knee = optimal eps")
# Knee of the curve ≈ optimal eps value

# ── Fit DBSCAN ────────────────────────────────────────
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X_scaled)

n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise    = list(labels).count(-1)
print(f"Clusters: {n_clusters}")
print(f"Noise points: {n_noise} ({n_noise/len(labels):.1%})")

# Visualise
plt.figure(figsize=(8, 6))
unique_labels = set(labels)
colours = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colours):
    if k == -1: col = "black"  # noise = black
    mask = labels == k
    plt.scatter(X_scaled[mask, 0], X_scaled[mask, 1],
                c=[col], s=15, alpha=0.7,
                label=f"{'Noise' if k == -1 else f'Cluster {k}'}")
plt.legend(fontsize=8)
plt.title(f"DBSCAN: {n_clusters} clusters, {n_noise} noise points")</pre></div>
  </div>
</div>
</div>

<div id="t3" class="tab-pane">
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📉</span><h3>PCA — Dimensionality Reduction</h3><span class="tag tag-teal">Linear DR</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

# ── PCA concept ───────────────────────────────────────
# Finds directions (principal components) of maximum variance
# PC1: direction of highest variance in the data
# PC2: direction of second highest variance, orthogonal to PC1
# Each PC is a linear combination of original features
# Use cases:
#   1. Visualisation: reduce to 2D for scatter plots
#   2. Noise removal: drop low-variance components
#   3. Feature compression: fewer features before SVM or kNN
#   4. Multicollinearity removal for linear models

X = df.select_dtypes("number").dropna()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ── Fit PCA ───────────────────────────────────────────
pca = PCA()  # keep all components to see explained variance
pca.fit(X_scaled)

# ── Explained variance plot ──────────────────────────
explained_var = pca.explained_variance_ratio_
cumulative_var = np.cumsum(explained_var)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].bar(range(1, len(explained_var)+1), explained_var)
axes[0].set(xlabel="Principal Component", ylabel="Explained Variance Ratio",
             title="Variance per Component")
axes[1].plot(range(1, len(cumulative_var)+1), cumulative_var, marker="o")
axes[1].axhline(0.95, color="red", linestyle="--", label="95% threshold")
axes[1].set(xlabel="N Components", ylabel="Cumulative Explained Variance",
             title="How many components for 95% variance?")
axes[1].legend()

# How many components to retain 95% variance?
n_components_95 = np.argmax(cumulative_var >= 0.95) + 1
print(f"Components for 95% variance: {n_components_95} / {X_scaled.shape[1]}")

# ── Apply PCA reduction ───────────────────────────────
pca_2 = PCA(n_components=2)
X_2d = pca_2.fit_transform(X_scaled)

pca_95 = PCA(n_components=0.95)  # keep 95% variance automatically
X_95 = pca_95.fit_transform(X_scaled)
print(f"Reduced from {X_scaled.shape[1]} to {X_95.shape[1]} features (95% variance)")

# ── Visualise in 2D ───────────────────────────────────
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_2d[:, 0], X_2d[:, 1],
                      c=df["SalePrice"], cmap="viridis", s=10, alpha=0.5)
plt.colorbar(scatter, label="SalePrice")
plt.xlabel(f"PC1 ({explained_var[0]:.1%} variance)")
plt.ylabel(f"PC2 ({explained_var[1]:.1%} variance)")
plt.title("House Prices: 2D PCA Projection")

# ── Feature loadings ──────────────────────────────────
loadings = pd.DataFrame(pca.components_.T,
                         index=X.columns,
                         columns=[f"PC{i+1}" for i in range(len(X.columns))])
print("Top features for PC1 (high |loading| = strong contributor):")
print(loadings["PC1"].abs().sort_values(ascending=False).head(5))</pre></div>
    <div class="ins"><p>💡 <strong>PCA is linear — it only captures linear relationships.</strong> If your data has non-linear structure (spiral, ring, Swiss roll), PCA will distort it. In that case, use t-SNE or UMAP for visualisation, and kernel PCA for preprocessing.</p></div>
  </div>
</div>
</div>

<div id="t4" class="tab-pane">
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🌀</span><h3>t-SNE and UMAP — Non-Linear Visualisation</h3><span class="tag tag-purple">Visualisation</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.manifold import TSNE
import umap  # pip install umap-learn
import matplotlib.pyplot as plt
import numpy as np

# ── t-SNE ─────────────────────────────────────────────
# Converts high-dimensional distances to probabilities
# Places points in 2D to match those probability distributions
# PRESERVES LOCAL structure (nearby points stay nearby)
# Does NOT preserve global distances (far points are unreliable)
# Main parameter: perplexity (5-50; ~= number of neighbours considered)
# WARNING: every run looks different! Set random_state for reproducibility
# WARNING: slow for N > 10,000. Apply PCA first.

# Best practice: PCA to 50 dims first (faster, denoises)
pca50 = PCA(n_components=50)
X_pca50 = pca50.fit_transform(X_scaled)

tsne = TSNE(
    n_components=2,
    perplexity=30,          # 5-50; higher = more global
    learning_rate="auto",
    n_iter=1000,
    init="pca",             # better initialisation than random
    random_state=42,
)
X_tsne = tsne.fit_transform(X_pca50)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1],
                      c=y_clusters, cmap="tab10", s=8, alpha=0.7)
plt.title("t-SNE Visualisation (perplexity=30)")
plt.colorbar(scatter, label="Cluster")

# ── UMAP (faster + preserves global structure better) ─
# Pros over t-SNE:
#   - Much faster (10-100× on large datasets)
#   - Preserves both local AND global structure
#   - Deterministic with random_state
#   - Can transform new data (transform method, unlike t-SNE)
# Main parameters:
#   n_neighbors: local neighbourhood size (5-50)
#   min_dist: how tightly to pack clusters (0.0-1.0)

reducer = umap.UMAP(
    n_components=2,
    n_neighbors=15,     # 5=local, 50=global structure
    min_dist=0.1,       # 0.0=tighter clusters, 1.0=more spread
    random_state=42,
    n_jobs=-1,
)
X_umap = reducer.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_umap[:, 0], X_umap[:, 1],
                      c=y_clusters, cmap="tab10", s=8, alpha=0.7)
plt.title("UMAP Visualisation")

# UMAP can transform new data (t-SNE cannot)
new_data_2d = reducer.transform(X_test_scaled)  # project test set</pre></div>
    <div class="warn"><p>⚠️ <strong>t-SNE and UMAP are for visualisation only.</strong> The 2D coordinates have no absolute meaning — distances between cluster groups are not interpretable. Cluster A appearing "close" to cluster B in t-SNE does not mean they are similar. Use these only to verify that clusters exist visually, not to measure cluster similarity.</p></div>
  </div>
</div>
</div>

<div id="t5" class="tab-pane">
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Cluster Evaluation Metrics</h3><span class="tag tag-green">Evaluation</span></div>
  <div class="cp-body">
    <div class="cb"><pre>from sklearn.metrics import (silhouette_score, davies_bouldin_score,
                             calinski_harabasz_score, adjusted_rand_score)
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# ── Internal metrics (no labels needed) ──────────────

# 1. Silhouette Score: -1 to +1
# a(i) = mean distance to own cluster members
# b(i) = mean distance to nearest OTHER cluster members
# silhouette(i) = (b(i) - a(i)) / max(a(i), b(i))
# Near +1: point is well-separated from other clusters
# Near  0: point is on the boundary between clusters
# Near -1: point may be in the wrong cluster
sil = silhouette_score(X_scaled, labels)
print(f"Silhouette Score: {sil:.4f}  (higher is better, max 1.0)")

# 2. Davies-Bouldin Index: lower is better
# Average ratio of intra-cluster to inter-cluster distance
db = davies_bouldin_score(X_scaled, labels)
print(f"Davies-Bouldin:   {db:.4f}  (lower is better)")

# 3. Calinski-Harabasz (Variance Ratio): higher is better
ch = calinski_harabasz_score(X_scaled, labels)
print(f"Calinski-Harabasz: {ch:.1f}  (higher is better)")

# ── External metrics (need true labels) ───────────────
# Use when you KNOW the true clusters (e.g. from a ground truth)
# Adjusted Rand Index: -0.5 to 1.0 (1.0 = perfect agreement)
ari = adjusted_rand_score(y_true, labels)
print(f"Adjusted Rand Index: {ari:.4f}")

# ── Plot silhouette scores per cluster ────────────────
from sklearn.metrics import silhouette_samples
sample_sil = silhouette_samples(X_scaled, labels)
fig, ax = plt.subplots(figsize=(8, 5))
y_lower = 10
for k in range(n_clusters):
    cluster_sil = np.sort(sample_sil[labels == k])
    y_upper = y_lower + len(cluster_sil)
    ax.fill_betweenx(np.arange(y_lower, y_upper), 0, cluster_sil)
    y_lower = y_upper + 5
ax.axvline(sil, color="red", linestyle="--", label=f"Mean = {sil:.3f}")
ax.set(xlabel="Silhouette Coefficient", title="Silhouette Plot per Cluster")
ax.legend()</pre></div>
  </div>
</div>
</div>

<div id="t6" class="tab-pane">
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏢</span><h3>RFM Customer Segmentation Pipeline</h3><span class="tag tag-blue">Real-World Application</span></div>
  <div class="cp-body">
    <div class="cb"><pre>import pandas as pd, numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# ── RFM Analysis — standard segmentation framework ───
# R (Recency):   How recently did the customer purchase?
# F (Frequency): How often do they purchase?
# M (Monetary):  How much do they spend?

df_orders = pd.read_csv("online_retail.csv")
df_orders["InvoiceDate"] = pd.to_datetime(df_orders["InvoiceDate"])
df_orders["Revenue"] = df_orders["Quantity"] * df_orders["UnitPrice"]

# Reference date: day after last transaction
reference = df_orders["InvoiceDate"].max() + pd.Timedelta(days=1)

rfm = df_orders.groupby("CustomerID").agg(
    Recency   = ("InvoiceDate", lambda x: (reference - x.max()).days),
    Frequency = ("InvoiceNo", "nunique"),
    Monetary  = ("Revenue", "sum")
).reset_index()

# Remove outliers
rfm = rfm[(rfm["Monetary"] > 0) & (rfm["Frequency"] > 0)]

# ── Scale and cluster ─────────────────────────────────
scaler = StandardScaler()
X_rfm = scaler.fit_transform(rfm[["Recency", "Frequency", "Monetary"]])

# Find K using elbow + silhouette
silhouettes = []
for k in range(2, 8):
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(X_rfm)
    silhouettes.append(silhouette_score(X_rfm, labels))

best_k = silhouettes.index(max(silhouettes)) + 2
print(f"Best K: {best_k}")

km = KMeans(n_clusters=best_k, n_init=20, random_state=42)
rfm["Cluster"] = km.fit_predict(X_rfm)

# ── Profile clusters ──────────────────────────────────
profile = rfm.groupby("Cluster")[["Recency", "Frequency", "Monetary"]].mean().round(1)
profile["Size"] = rfm["Cluster"].value_counts().sort_index()
print(profile)

# Interpret:
# Cluster A: Low Recency, High Freq, High Monetary → Champions
# Cluster B: High Recency, Low Freq, Low Monetary  → At Risk
# Cluster C: Medium Recency, Medium Freq            → Potential Loyalists

# ── PCA visualisation of RFM clusters ────────────────
pca2 = PCA(n_components=2)
X_2d = pca2.fit_transform(X_rfm)
plt.figure(figsize=(8, 6))
for c in rfm["Cluster"].unique():
    mask = rfm["Cluster"] == c
    plt.scatter(X_2d[mask, 0], X_2d[mask, 1], label=f"Cluster {c}", s=10, alpha=0.5)
plt.legend()
plt.title(f"RFM Clusters (K={best_k}, PCA 2D)")</pre></div>
  </div>
</div>
</div>

<div id="t7" class="tab-pane">
<p class="sep">FREE LEARNING RESOURCES</p>
<table class="res-table">
  <thead><tr><th>Type</th><th>Resource</th><th>Best For</th></tr></thead>
  <tbody>
    <tr><td class="res-type">Video</td><td><a href="https://www.youtube.com/c/joshstarmer" target="_blank" rel="noopener">StatQuest — K-Means, PCA, t-SNE (YouTube)</a></td><td>Best visual explanations of how each algorithm works. Highly recommended for building intuition.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://scikit-learn.org/stable/modules/clustering.html" target="_blank" rel="noopener">Scikit-learn Clustering Guide — scikit-learn.org/stable/modules/clustering.html</a></td><td>All sklearn clustering algorithms with comparison table, parameters, and use cases.</td></tr>
    <tr><td class="res-type">Docs</td><td><a href="https://umap-learn.readthedocs.io/" target="_blank" rel="noopener">UMAP Documentation — umap-learn.readthedocs.io</a></td><td>UMAP parameters, comparison to t-SNE, and production use cases.</td></tr>
    <tr><td class="res-type">Dataset</td><td><a href="https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python" target="_blank" rel="noopener">Mall Customers — Kaggle</a></td><td>Classic customer segmentation dataset. Small, visual, perfect for K-Means exploration.</td></tr>
    <tr><td class="res-type">Dataset</td><td><a href="https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce" target="_blank" rel="noopener">Olist Brazilian E-Commerce — Kaggle</a></td><td>Real e-commerce data for full RFM analysis. Multiple tables to join and explore.</td></tr>
  </tbody>
</table>
</div>

<div id="t8" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr"><span>🛠</span><span class="proj-title">Customer Segmentation + Churn Prediction</span><span class="proj-dur">[Advanced] 6–7 days</span></div>
  <div class="proj-body">
    <p>A two-part project combining unsupervised and supervised ML.</p>
    <h4>Part A — Customer Segmentation (3–4 days)</h4>
    <ul>
      <li>Load Telco Churn or Mall Customers dataset</li>
      <li>Compute RFM features (or use existing features)</li>
      <li>Use elbow + silhouette to find optimal K</li>
      <li>Profile each cluster with mean feature values</li>
      <li>Visualise with PCA + t-SNE side by side</li>
      <li>Name each segment: "High-Value Loyalists", "At-Risk Churners", etc.</li>
    </ul>
    <h4>Part B — Churn Prediction (2–3 days)</h4>
    <ul>
      <li>Add cluster labels as a feature to the churn prediction dataset</li>
      <li>Train XGBoost with and without cluster feature</li>
      <li>Does the cluster feature improve ROC-AUC?</li>
      <li>Which cluster has the highest churn rate?</li>
    </ul>
    <p><strong>Deliverable:</strong> Jupyter notebook with all plots + 1-paragraph business recommendation per segment.</p>
  </div>
</div>

<div class="part3-complete">
  <h3>🎉 Part 3 Complete!</h3>
  <p>You've completed all 6 Classical ML modules (P2-M05 through P3-M10). You can now EDA any dataset, build regression and classification models, use gradient boosting, tune hyperparameters, and find hidden structure. Next: <strong>Part 4 — LLM APIs</strong>, where the AI Engineering path begins.</p>
</div>
</div>

<div id="t9" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Finding the Right K</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>On Mall Customers, plot elbow curve (inertia) and silhouette score for K=2 to 10. Do both methods agree on the best K? What happens when K is too large?</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Fit K-Means with the optimal K. Profile each cluster: what is the mean Income, Spending Score, and Age? Give each cluster a descriptive name (e.g., "Budget Conscious Young Adults").</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Run K-Means 5 times with different random_state values (same K). Do the cluster assignments change? Does the silhouette score change? What does this tell you about K-Means stability?</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>PCA for Preprocessing</h4></div>
  <div class="lab-body">
    <div class="lab-step"><div class="sn">1</div><div>Apply PCA to House Prices numeric features. How many components are needed to explain 95% variance? How many for 99%?</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Train Ridge regression on: (a) all original features, (b) PCA 95% components, (c) PCA 50% components. Compare CV RMSE. Does PCA improve or hurt performance?</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Plot the loadings for PC1 and PC2. Which original features contribute most to each component? Does this match your intuition from the EDA (M05)?</div></div>
  </div>
</div>
</div>

<div id="t10" class="tab-pane">
<p class="sep">P3-M10 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can explain K-Means: centroid initialisation, assignment step, update step, convergence</li>
  <li>Know that K-Means requires feature scaling and assumes spherical clusters</li>
  <li>Can use elbow method and silhouette score to find optimal K</li>
  <li>Can profile and name clusters with groupby().mean() and visualisations</li>
  <li>Can explain DBSCAN parameters: eps and min_samples</li>
  <li>Know DBSCAN handles non-spherical clusters and detects noise points</li>
  <li>Can explain PCA: principal components are directions of maximum variance</li>
  <li>Can create and interpret an explained variance plot</li>
  <li>Can reduce to 2D for visualisation and to 95% variance for preprocessing</li>
  <li>Know t-SNE preserves local structure but not global; use only for visualisation</li>
  <li>Know UMAP is faster than t-SNE and can transform new data</li>
  <li>Can compute silhouette, Davies-Bouldin, and Calinski-Harabasz scores</li>
  <li>Can implement a full RFM segmentation pipeline: feature engineering → scale → cluster → profile</li>
  <li>Completed project: Customer segmentation with cluster profiling and business interpretation</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>Part 3 Complete!</strong> You have all the Classical ML foundations. Move to <strong>Part 4 — LLM APIs</strong> to start the AI Engineering path: prompting, structured outputs, streaming, and reliability.</p>
</div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/ai-ml/part3-classical-ml/p3-m09-ensembles/' | relative_url }}">← P3-M09: Ensembles</a>
  <a href="{{ '/learning/ai-ml/ai-ml-roadmap/' | relative_url }}">🗺️ All Modules</a>
  <a class="nb" href="{{ '/learning/ai-ml/part4-llm-apis/p4-m11-prompting/' | relative_url }}">Next: P4-M11 — Prompting →</a>
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
    const key = 'p3m10_ck_' + i;
    if (localStorage.getItem(key) === '1') li.classList.add('done');
    li.addEventListener('click', () => {
      li.classList.toggle('done');
      localStorage.setItem(key, li.classList.contains('done') ? '1' : '0');
    });
  });
});
</script>
