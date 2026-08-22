---
layout: default
title: "Module B13: ML Systems Design — Study Notes"
permalink: /learning/system-design/hld/module-b13-notes/
custom_css: dsa-chapter
---

<div style="margin-bottom:24px;padding:14px 20px;background:#f0f4ff;border-left:4px solid #a060ff;border-radius:0 4px 4px 0;font-family:'IBM Plex Mono',monospace;font-size:13px;">
  <strong>Module B13 · Week 23 · Track B — HLD</strong><br>
  <span style="color:#666;">Prerequisites: B1–B12 &nbsp;|&nbsp; Goal: Production ML systems, feature stores, model serving, two-tower retrieval, A/B testing, drift</span>
</div>

<a href="/learning/system-design/hld/module-b13-ml-systems/" style="display:inline-block;margin-bottom:32px;padding:10px 20px;background:#a060ff;color:#fff;border-radius:4px;text-decoration:none;font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;">⚡ Interactive Visual Version</a>

# Module B13 — ML Systems Design
## System Design Mastery Course | Track B: HLD | Week 23

---

## 🎯 Module Overview

**Duration:** 1 Week | **Track:** B — HLD
**Prerequisites:** B1–B12
**Goal:** ML systems are increasingly asked in FAANG interviews — especially at Meta, Google, and Netflix. Even for non-ML roles, you'll be asked how you'd serve a recommendation model or build a feature pipeline. This module covers the full stack: feature stores, training pipelines, model serving, A/B testing, and feedback loops.

---

## 1. The ML System Stack

```
OFFLINE (batch)                    ONLINE (real-time)
─────────────────────────────────────────────────────
Raw Data Sources                   User Request
    ↓                                  ↓
Feature Engineering Pipeline       Feature Retrieval (Feature Store)
    ↓                                  ↓
Feature Store (offline)            Model Inference (Serving Layer)
    ↓                                  ↓
Training Pipeline                  Ranking / Post-processing
    ↓                                  ↓
Model Registry                     Response to User
    ↓
Model Deployment → Serving Layer

Three core problems:
1. Feature consistency: training features must match serving features exactly
   (training-serving skew = #1 cause of model degradation in production)
2. Latency: inference must be fast enough for the user-facing SLA
3. Freshness: features must be recent enough to be predictive
```

---

## 2. Feature Stores

```
Problem: ML features are expensive to compute. Without a feature store:
  - Same feature computed independently by every model team
  - Training uses one computation path, serving uses another → skew
  - No sharing, no discovery, no versioning

Feature store = centralized repository for computed features.
  Offline store: batch-computed features (Hive, S3, BigQuery)
    → High volume, historical data, used for training
  Online store: low-latency feature lookups (Redis, DynamoDB, Cassandra)
    → Millisecond latency, current features, used for serving

Key operations:
  Write path: batch job computes feature_value for (entity_id, feature_name, timestamp)
              → writes to both offline store (all history) and online store (latest)
  Read path (training): retrieve feature values at historical timestamps for training examples
  Read path (serving): retrieve latest feature values for entity_id in <10ms

Feature freshness tiers:
  Real-time features (< 1 second old):
    Computed from streaming events (Kafka → Flink → Redis)
    Example: "user's last 5 clicks in past 60 seconds"

  Near-real-time features (minutes old):
    Micro-batch (Spark Structured Streaming, every 5 minutes)
    Example: "user's click-through rate in past hour"

  Batch features (hours/days old):
    Daily or hourly Spark/Hive jobs
    Example: "user's average session duration over past 30 days"

Point-in-time correctness (critical for training):
  When training on historical data, must use feature values AS OF the training example's timestamp.
  Cannot use future feature values to predict the past (data leakage).
  Feature store must support: get_features(entity_id, as_of=timestamp)
```

---

## 3. Training Pipelines

```
Components of a production training pipeline:

1. Data Ingestion
   Pull labeled examples from data warehouse (BigQuery, Hive, Redshift)
   Join with feature store to get feature values at correct timestamps
   Output: training dataset (features + labels)

2. Data Validation
   Schema validation: expected features present, correct types
   Distribution checks: feature values within expected range
   Label distribution: check for class imbalance
   Tools: TFX (TensorFlow Extended), Great Expectations

3. Feature Preprocessing
   Normalization, encoding, imputation of missing values
   Must be IDENTICAL between training and serving (same code path)
   Saved as a preprocessing artifact that travels with the model

4. Model Training
   Distributed training for large models (Horovod, PyTorch DDP)
   Hyperparameter tuning (Optuna, Ray Tune)
   Experiment tracking (MLflow, Weights & Biases)

5. Model Evaluation
   Offline metrics: AUC, NDCG, precision@K, RMSE
   Slice evaluation: performance across demographic groups
   Comparison against champion model (must beat current prod)

6. Model Registration
   Version model in model registry (MLflow, Vertex AI Model Registry)
   Tag with: dataset version, training code version, offline metrics
   Approval gate: human review before promotion to serving

Pipeline orchestration: Airflow (batch), Kubeflow Pipelines, Vertex AI Pipelines

Retraining triggers:
  Scheduled: daily retraining on fresh data (most common)
  Drift-triggered: data distribution shifts beyond threshold
  Performance-triggered: online metrics (CTR, conversion) drop
```

---

## 4. Model Serving

```
Two serving paradigms:

BATCH INFERENCE (offline scoring):
  Run model on large dataset of entities, store results
  Scores retrieved at serving time — no model loaded in hot path
  Latency: ~0ms (just a DB lookup)
  Freshness: stale by hours/days

  Example: pre-compute top-1000 recommended videos per user nightly
  Good for: email recommendations, non-time-sensitive personalization

REAL-TIME INFERENCE (online serving):
  Model loaded in serving process, inference on each request
  Latency: ~10–100ms depending on model size
  Freshness: real-time features, fresh prediction

  Example: ranking the 100 candidate videos at search time
  Good for: search ranking, ad serving, fraud detection

Serving infrastructure:
  Model server: TensorFlow Serving, TorchServe, Triton Inference Server
  Batching: group multiple requests → single forward pass → lower latency per request
  Hardware: CPU (simple models), GPU (deep learning), TPU (Google-scale)
  Autoscaling: scale on GPU utilization, request queue depth

Model versioning in serving:
  Traffic splitting: 90% → model v1, 10% → model v2 (canary)
  Shadow mode: v2 runs alongside v1, predictions logged but not shown to user
  Blue-green: keep v1 hot, switch all traffic to v2 instantly on validation
```

---

## 5. Two-Tower Model (Recommendation at Scale)

```
The dominant architecture for large-scale retrieval (YouTube, Spotify, TikTok).

Problem: rank 10 million items for a user in < 100ms.
  Naive: score all 10M items with a full model → too slow.
  Solution: two-stage pipeline (retrieval + ranking).

STAGE 1 — RETRIEVAL (candidate generation):
  Two-tower model: user tower + item tower.
  Each tower produces an embedding (dense vector, ~64–256 dimensions).
  Similarity: dot product or cosine similarity between user and item embeddings.

  Training: user and item embeddings trained jointly.
  Serving: pre-compute embeddings for all items (offline).
           At query time: compute user embedding, search for nearest items.
  ANN search: Approximate Nearest Neighbor (FAISS, ScaNN, Milvus).
              Find top-100 similar items in < 10ms from 10M items.

  Output: ~100–1000 candidate items.

STAGE 2 — RANKING:
  Larger, more complex model (deep neural net, gradient boosted trees).
  Takes candidate item + user context + cross-features as input.
  Scores each candidate precisely.
  Can use features unavailable to retrieval tower (real-time context, freshness).
  Output: ranked list of top-K items.

STAGE 3 — POST-PROCESSING:
  Business rules: don't show already-watched content.
  Diversity: enforce genre/topic diversity (not 10 Taylor Swift videos).
  Freshness boost: boost newer content.
  Safety filters: remove policy-violating content.
  Output: final ranked list shown to user.

Latency budget (100ms total):
  Feature retrieval: 10ms
  User embedding computation: 5ms
  ANN search (1M items): 10ms
  Ranking (100 candidates): 30ms
  Post-processing: 5ms
  Network + overhead: 40ms
```

---

## 6. A/B Testing at Scale

```
Purpose: measure causal impact of a model change on business metrics.
  Correlation != causation. Better model offline ≠ better metrics online.
  A/B test isolates the effect of one change.

Setup:
  Control group (A): existing model (champion)
  Treatment group (B): new model (challenger)
  Split: random assignment per user (not per request — same user always sees same model)
  Duration: long enough for statistical significance + novelty effect to wear off

Key metrics:
  Primary metric: the one you're optimizing (CTR, watch time, conversion rate)
  Guardrail metrics: must not regress (latency, crash rate, revenue)
  Secondary metrics: informative but not decision-making

Statistical significance:
  p-value < 0.05: 5% chance of seeing this result if null hypothesis is true
  Power: probability of detecting a real effect (typically 80%)
  Sample size calculation: depends on baseline rate, minimum detectable effect, power
  t-test for means, z-test for proportions, Mann-Whitney for non-normal

Common pitfalls:
  Peeking: stopping early when results look significant → inflated false positive rate
  Novelty effect: users click new UI just because it's new → wait 2+ weeks
  Network effects: users in A interact with users in B (social networks) → use cluster-based splitting
  Multiple testing: running 20 A/B tests → 1 will be "significant" by chance → Bonferroni correction

Experiment lifecycle:
  Ramp: 1% → 5% → 10% → 50% → 100% traffic to treatment
  Kill switch: automated rollback if guardrail metric regresses > threshold

At scale (Meta, Google):
  Millions of A/B tests running simultaneously
  CUPED (Controlled-experiment Using Pre-Experiment Data) to reduce variance
  Interleaving: show results from both models in same response, measure which gets more clicks
  Holdout groups: permanent 1% holdout not receiving any experiments (true baseline)
```

---

## 7. Feature & Concept Drift

```
Model performance degrades over time because the world changes.

Types of drift:
  Data drift (covariate shift):
    Input feature distribution changes.
    Example: user ages in training data were 18–35, now 13–50.
    Detection: KL divergence, Population Stability Index (PSI) on feature distributions.

  Concept drift:
    Relationship between features and labels changes.
    Example: "free shipping" used to predict high purchase intent, but now it's expected by all users.
    Detection: online metrics (CTR, conversion) compared to offline eval set.

  Label drift:
    Distribution of labels changes.
    Example: fraud rate increases after a new attack vector.
    Detection: monitor label frequency in production feedback.

Response strategies:
  1. Scheduled retraining: retrain daily/weekly regardless
     Simple, catches gradual drift, may miss sudden shifts
  2. Triggered retraining: monitor PSI, retrain when PSI > threshold
     More responsive, but needs monitoring infrastructure
  3. Online learning: update model weights continuously from new data
     Most responsive, but hard to validate, risk of poisoning

Monitoring stack:
  Feature drift: compute PSI/KL divergence on feature distributions daily
  Prediction drift: track prediction score distribution
  Outcome metrics: track business metrics (CTR, conversion, revenue) with alerts
  Data quality: null rates, schema violations, out-of-range values
```

---

## 8. ML System Design — Full Example: YouTube Recommendations

```
Problem: 2B users, 800M DAU, recommend 20 videos per homepage.
Goal: maximize watch time and user satisfaction.

OFFLINE PIPELINE (runs daily):
  1. Feature computation:
     User features: watch history (past 30 days), search history, demographics
     Video features: view count, like/dislike ratio, average watch duration, transcript embeddings
     Context features: time of day, device type
     → Written to feature store (BigQuery offline + Bigtable online)

  2. Training data generation:
     Positive examples: (user, video) pairs where user watched > 50% of video
     Negative examples: (user, video) pairs where video was shown but not clicked
     Sample 10 negatives per positive (negative sampling)
     Join with feature store at point-in-time correct timestamps

  3. Two-tower retrieval model training:
     User tower: embed watch history, search history → 256-dim user embedding
     Video tower: embed video metadata, transcript → 256-dim video embedding
     Loss: softmax cross-entropy over sampled negatives
     Evaluation: Recall@100 (are the ground-truth videos in the top-100 retrieved?)

  4. Ranking model training:
     Input: (user, candidate video, context) features
     Output: predicted watch time
     Model: deep neural net (Wide & Deep, DCN, DLRM)
     Evaluation: NDCG@20 on held-out test set

  5. Model registration:
     If Recall@100 > current prod AND NDCG@20 > current prod:
     Register in model registry, mark as candidate for A/B test.

ONLINE PIPELINE (< 100ms per request):
  1. User request arrives at recommendation service.
  2. Feature retrieval: fetch user's 256-dim embedding from Bigtable (~5ms).
     (Or compute fresh from last 5 clicks using lightweight model)
  3. ANN retrieval: ScaNN search over 10M video embeddings → top 500 candidates (~15ms).
     (Pre-indexed nightly. 10M embeddings × 256 dims × 4 bytes = ~10 GB, fits in RAM)
  4. Ranking: score each of 500 candidates with ranking model → sort by predicted watch time (~40ms).
  5. Post-processing: filter watched, enforce diversity, freshness boost, safety filter.
  6. Return top 20 videos.

A/B testing:
  New ranking model → 5% traffic to treatment.
  Primary metric: watch time per session.
  Guardrail: latency p99 must not increase > 10%.
  Run for 2 weeks → evaluate → ramp or rollback.
```

---

## 📝 Tasks

### Task 1 — Feature Store Design
Design a feature store for a fraud detection model at a payments company:
1. What features are needed? List 10 features across user, transaction, and merchant dimensions.
2. Which features are batch (daily), near-real-time (5-min), and real-time (< 1s)?
3. Design the online store schema. What key structure? What TTL?
4. A transaction arrives. Walk through the full feature retrieval path end-to-end.
5. Training time: how do you retrieve feature values at the exact timestamp of a historical transaction without leaking future data?

### Task 2 — A/B Test Design
You've trained a new recommendation model. Design the A/B test:
1. What is your primary metric? Why not offline AUC?
2. How do you calculate required sample size? (baseline CTR=2%, MDE=0.2%, power=80%)
3. Should you split by user, by session, or by request? Why does it matter?
4. Your test runs 3 days and shows p=0.03 (significant!). Should you ship? Why or why not?
5. The treatment group shows +3% CTR but -1% session duration. What do you decide?

### Task 3 — Drift Detection
Your fraud model was trained 6 months ago. Design a drift monitoring system:
1. Which features are most likely to drift? Why?
2. Define PSI and write the formula. What threshold triggers retraining?
3. You detect label drift: fraud rate increased from 0.1% to 0.3%. What do you do?
4. How do you distinguish data drift from a data pipeline bug?
5. Design the full monitoring dashboard: what 6 metrics do you track daily?

### ⭐ Task 4 — Design a News Feed Ranking System
Design the ML system for ranking a social media news feed (like LinkedIn or Facebook):
1. What is the objective function? (Engagement? Time well spent? A combination?)
2. Design the two-stage pipeline: retrieval model + ranking model.
3. Feature store: 10 key features, their freshness tier, and storage backend.
4. How do you handle the cold-start problem for new users and new posts?
5. A/B test design: primary metric, guardrail metrics, duration, and what split to use.
6. The model learns to maximize clicks, leading to clickbait. How do you fix this?

---

## ✅ Completion Checklist

- [ ] ML system stack: offline pipeline vs online pipeline, training-serving skew problem
- [ ] Feature store: offline store (batch, training) vs online store (low-latency, serving)
- [ ] Point-in-time correctness: no data leakage in historical feature retrieval
- [ ] Feature freshness tiers: real-time (<1s), near-real-time (minutes), batch (hours)
- [ ] Training pipeline: 6 stages from data ingestion to model registration
- [ ] Retraining triggers: scheduled, drift-triggered, performance-triggered
- [ ] Batch vs real-time inference: trade-offs in latency and freshness
- [ ] Model versioning: canary, shadow mode, blue-green deployment
- [ ] Two-tower model: user tower + item tower, embedding similarity, ANN retrieval
- [ ] Two-stage pipeline: retrieval (100s of candidates) → ranking → post-processing
- [ ] ANN search: FAISS, ScaNN — ~10ms for 10M items
- [ ] A/B testing: p-value, power, sample size, peeking problem, novelty effect
- [ ] A/B pitfalls: network effects → cluster-based splitting
- [ ] Data drift vs concept drift vs label drift — detection methods
- [ ] PSI for feature drift detection, online metrics for concept drift
- [ ] YouTube recommendations: full offline + online pipeline
- [ ] Latency budget: 100ms breakdown across feature retrieval, ANN, ranking
- [ ] Completed Task 1 — feature store for fraud detection
- [ ] Completed Task 2 — A/B test design
- [ ] Completed Task 3 — drift monitoring system
- [ ] Completed Task 4 — news feed ranking ML system (capstone)

**→ Next: Module B14 — Observability & SRE (Metrics, Tracing, SLOs, Incident Response)**

---

<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid #ddd;padding-top:20px;">
  <a href="/learning/system-design/hld/module-b12-notes/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">← B12 Interview Framework Notes</a>
  <a href="/learning/system-design/hld/module-b13-ml-systems/" style="padding:12px 24px;border:1px solid #a060ff;color:#a060ff;border-radius:4px;text-decoration:none;font-weight:600;">⚡ Interactive Module</a>
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-b14-kubernetes/" style="padding:12px 24px;background:#a060ff;color:#fff;border-radius:4px;text-decoration:none;font-weight:600;">NEXT: B14 Kubernetes →</a>
</div>
