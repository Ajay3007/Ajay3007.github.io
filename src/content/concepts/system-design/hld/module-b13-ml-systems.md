---
title: "Module B13: ML Systems Design"
description: "SYSTEM DESIGN MASTERY · TRACK B · MODULE B13 · WEEK 23 FEATURE STORES · MODEL SERVING · TWO-TOWER · A/B TESTING · DRIFT // TRACK B · HLD · ML INFRASTRUCTURE ML Systems Design…"
domain: system-design
track: system-design-hld
order: 126
chrome: bare
ownHeader: true
url: /learning/system-design/hld/module-b13-ml-systems/
---

<link rel="stylesheet" href="/assets/css/sd-module-b13.css">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=IBM+Plex+Mono:ital,wght@0,300;0,400;0,600;1,400&family=Syne+Mono&display=swap" rel="stylesheet">
<header>
  <div class="hdr-bar"></div>
  <div class="hdr-top">
<span>SYSTEM DESIGN MASTERY · TRACK B · MODULE B13 · WEEK 23</span>
<span>FEATURE STORES · MODEL SERVING · TWO-TOWER · A/B TESTING · DRIFT</span>
  </div>
  <div class="hdr-main">
<div>
<div class="hdr-kicker">// TRACK B · HLD · ML INFRASTRUCTURE</div>
<h1>ML Systems<br><span class="acc">Design</span></h1>
<div class="hdr-sub">FEATURE STORES · TRAINING PIPELINES · MODEL SERVING<br>TWO-TOWER RETRIEVAL · A/B TESTING · DRIFT DETECTION</div>
</div>
<div class="hdr-stats">
<div class="hs"><div class="hs-v">2-stage</div><div class="hs-l">RETRIEVAL+RANK</div></div>
<div class="hs"><div class="hs-v">100ms</div><div class="hs-l">LATENCY BUDGET</div></div>
<div class="hs"><div class="hs-v">3</div><div class="hs-l">DRIFT TYPES</div></div>
<div class="hs"><div class="hs-v">B13</div><div class="hs-l">MODULE</div></div>
</div>
  </div>
  <div class="tag-row">
<div class="tg" style="color:var(--vio)">Feature Store</div>
<div class="tg" style="color:var(--grn)">Training Pipeline</div>
<div class="tg" style="color:var(--cya)">Model Serving</div>
<div class="tg" style="color:var(--yel)">Two-Tower Model</div>
<div class="tg" style="color:var(--ora)">A/B Testing</div>
<div class="tg" style="color:var(--red)">Drift Detection</div>
<div class="tg" style="color:var(--bri)">YouTube Recs</div>
  </div>
</header>
<nav class="nav">
  <div class="nt active" onclick="show('stack',this)">ML Stack</div>
  <div class="nt" onclick="show('featurestore',this)">Feature Store</div>
  <div class="nt" onclick="show('training',this)">Training Pipeline</div>
  <div class="nt" onclick="show('serving',this)">Model Serving</div>
  <div class="nt" onclick="show('twotower',this)">Two-Tower Model</div>
  <div class="nt" onclick="show('abtest',this)">A/B Testing</div>
  <div class="nt" onclick="show('drift',this)">Drift Detection</div>
  <div class="nt" onclick="show('youtube',this)">YouTube Recs</div>
  <div class="nt" onclick="show('tasks',this)">Tasks</div>
  <div class="nt" onclick="show('checklist',this)">Checklist</div>
</nav>
<div class="content">
<!-- STACK -->
<div class="view active" id="view-stack">
  <div class="sh">The ML System Stack</div>
  <div class="sr">Offline pipeline builds the model — online pipeline serves it</div>
  <div class="stack">
<div class="stack-col">
<div class="sc-hdr" style="color:var(--vio)">// OFFLINE PIPELINE (batch)</div>
<div class="sc-step"><div class="sc-arrow">↓</div><div><div class="sc-label">Raw Data Sources</div><div class="sc-sub">data warehouse, event logs, user actions</div></div></div>
<div class="sc-step"><div class="sc-arrow">↓</div><div><div class="sc-label">Feature Engineering</div><div class="sc-sub">Spark/Flink jobs computing features from raw data</div></div></div>
<div class="sc-step"><div class="sc-arrow">↓</div><div><div class="sc-label">Feature Store (offline)</div><div class="sc-sub">Hive / BigQuery / S3 — full history, training data</div></div></div>
<div class="sc-step"><div class="sc-arrow">↓</div><div><div class="sc-label">Training Pipeline</div><div class="sc-sub">data validation → train → eval → register</div></div></div>
<div class="sc-step"><div class="sc-arrow">↓</div><div><div class="sc-label">Model Registry</div><div class="sc-sub">versioned artifacts, metrics, approval gate</div></div></div>
<div class="sc-step"><div class="sc-arrow">↓</div><div><div class="sc-label">Deploy to Serving Layer</div><div class="sc-sub">canary → shadow → full rollout</div></div></div>
</div>
<div class="stack-col">
<div class="sc-hdr" style="color:var(--grn)">// ONLINE PIPELINE (real-time)</div>
<div class="sc-step"><div class="sc-arrow">↓</div><div><div class="sc-label">User Request</div><div class="sc-sub">API call → recommendation service</div></div></div>
<div class="sc-step"><div class="sc-arrow">↓</div><div><div class="sc-label">Feature Retrieval</div><div class="sc-sub">Feature Store (online) — Redis / Bigtable, &lt;10ms</div></div></div>
<div class="sc-step"><div class="sc-arrow">↓</div><div><div class="sc-label">Candidate Retrieval</div><div class="sc-sub">ANN search — top-500 from 10M items, ~15ms</div></div></div>
<div class="sc-step"><div class="sc-arrow">↓</div><div><div class="sc-label">Model Inference</div><div class="sc-sub">Ranking model scores each candidate, ~40ms</div></div></div>
<div class="sc-step"><div class="sc-arrow">↓</div><div><div class="sc-label">Post-processing</div><div class="sc-sub">diversity, safety filters, business rules</div></div></div>
<div class="sc-step"><div class="sc-arrow">↓</div><div><div class="sc-label">Response</div><div class="sc-sub">top-K results returned to user</div></div></div>
</div>
  </div>
  <div class="al red"><em>Training-serving skew</em> — the #1 cause of silent model degradation. If the features computed for training differ even slightly from features computed during serving (different code paths, different data sources, different timestamp handling), the model will perform worse in production than it did offline. The feature store's job is to ensure identical computation for both paths.</div>
</div>
<!-- FEATURE STORE -->
<div class="view" id="view-featurestore">
  <div class="sh">Feature Stores</div>
  <div class="sr">Centralized feature repository — eliminates skew, enables sharing and versioning</div>
  <div class="freshness">
<div class="ft" style="border-top-color:var(--red)">
<div class="ft-tier" style="color:var(--red)">REAL-TIME</div>
<div class="ft-time" style="color:var(--red)">&lt; 1 second</div>
<div class="ft-body">Computed from streaming events. Kafka → Flink → Redis. Reflects user's most recent actions within the current session.</div>
<div class="ft-examples">→ last 5 clicks (60s window)<br>→ current session duration<br>→ live cart contents</div>
<div class="ft-store" style="color:var(--red)">Store: Redis (TTL 1hr)</div>
</div>
<div class="ft" style="border-top-color:var(--yel)">
<div class="ft-tier" style="color:var(--yel)">NEAR-REAL-TIME</div>
<div class="ft-time" style="color:var(--yel)">1–60 min</div>
<div class="ft-body">Micro-batch jobs (Spark Structured Streaming). Aggregate windows computed every few minutes. Balances freshness and compute cost.</div>
<div class="ft-examples">→ CTR in past hour<br>→ purchase intent score (1h)<br>→ trending items right now</div>
<div class="ft-store" style="color:var(--yel)">Store: Redis / DynamoDB</div>
</div>
<div class="ft" style="border-top-color:var(--grn)">
<div class="ft-tier" style="color:var(--grn)">BATCH</div>
<div class="ft-time" style="color:var(--grn)">Hours / Days</div>
<div class="ft-body">Daily or hourly Spark / Hive jobs. Historical aggregates over large windows. Cheap to compute at scale, but stale by hours.</div>
<div class="ft-examples">→ avg session duration (30d)<br>→ lifetime purchase value<br>→ user age / demographics</div>
<div class="ft-store" style="color:var(--grn)">Store: BigQuery / Cassandra</div>
</div>
  </div>
  <div class="cb"><div class="cb-top">Point-in-time correctness — preventing data leakage in training<span class="cb-l">CRITICAL</span></div>


```python
// Training on historical data: label occurred at time T
// Must retrieve feature values AS OF time T, not current values
// Using future features to predict the past = data leakage = inflated offline metrics

// WRONG — uses today's feature value to predict a past label:
features = feature_store.get(entity_id=user_123, feature="avg_session_30d")
// This returns the feature as it is TODAY — but the label was from 6 months ago
// The feature includes 6 months of future data. Model appears great offline, fails in prod.

// CORRECT — point-in-time correct retrieval:
features = feature_store.get(
    entity_id=user_123,
    feature="avg_session_30d",
    as_of=label_timestamp  ← retrieve value AS OF when the label occurred
)

// Feature store must store full history of feature values with timestamps
// Offline store schema:
// (entity_id, feature_name, value, event_timestamp, created_timestamp)
// Query: SELECT value WHERE entity_id=X AND feature_name=Y
//        AND event_timestamp
```


</div>
<!-- TRAINING -->
<div class="view" id="view-training">
  <div class="sh">Training Pipeline</div>
  <div class="sr">Six stages from raw data to a registered model artifact</div>
  <div class="cb"><div class="cb-top">Production training pipeline — all six stages<span class="cb-l">PIPELINE</span></div>


```python
// Stage 1: DATA INGESTION
// Pull labeled examples from data warehouse, join with feature store
data = bigquery.query("SELECT user_id, item_id, label, event_time FROM interactions WHERE date=?")
features = feature_store.batch_get(entity_ids=data.user_ids, as_of=data.event_times)
dataset = join(data, features)

// Stage 2: DATA VALIDATION
// Catch data quality issues before training (fail fast)
validator.check_schema(dataset)           // expected columns present?
validator.check_distributions(dataset)    // feature values in expected range?
validator.check_null_rates(dataset)       // null rate < threshold per feature?
validator.check_label_balance(dataset)    // not extreme class imbalance?

// Stage 3: FEATURE PREPROCESSING (saved as artifact → identical at serving time)
preprocessor = Pipeline([
    StandardScaler(cols=["age", "session_duration"]),
    OneHotEncoder(cols=["device_type", "country"]),
    MeanImputer(cols=["avg_purchase_value"])
])
preprocessor.fit_transform(train_data)    // saved as artifact, applied at serving

// Stage 4: MODEL TRAINING
model = TwoTowerModel(user_dim=256, item_dim=256)
trainer = DistributedTrainer(model, gpus=8)   // Horovod / PyTorch DDP
trainer.train(train_data, epochs=10)

// Stage 5: EVALUATION (must beat champion model)
metrics = evaluator.eval(model, test_data)
if metrics.recall_at_100 <= champion.recall_at_100:
    pipeline.fail("New model does not beat champion. Stopping.")

// Stage 6: MODEL REGISTRATION
registry.register(model, {
    "recall@100": metrics.recall_at_100,
    "dataset_version": dataset.version,
    "training_code_hash": git.sha(),
    "status": "candidate"   // awaiting A/B test
})
```


  <div class="al vio"><em>Retraining triggers — three strategies:</em> (1) Scheduled: retrain daily regardless. Simple, catches gradual drift, may miss sudden shifts. (2) Drift-triggered: monitor PSI on feature distributions, retrain when PSI &gt; 0.2. More responsive, requires monitoring infra. (3) Performance-triggered: online business metrics (CTR, conversion) drop &gt; X% — immediate retrain. Most responsive, but online metrics lag by hours.</div>
</div>
<!-- SERVING -->
<div class="view" id="view-serving">
  <div class="sh">Model Serving</div>
  <div class="sr">Batch inference vs real-time inference — and how to deploy safely</div>
  <div class="ab-grid">
<div class="ab-col" style="border-top:2px solid var(--grn)">
<div class="ab-name" style="color:var(--white)">Batch Inference</div>
<div class="ab-sub" style="color:var(--grn)">PRE-COMPUTED SCORES · DB LOOKUP AT SERVING</div>
<div class="ab-body">Run model on large dataset of entities offline. Store results. Serving time = just a DB lookup. No model in hot path.</div>
<div class="ab-code" style="color:var(--sub)">Latency:  ~0ms (DB lookup)<br>Freshness: stale by hours/days<br>Cost:      cheap at serving time<br>Good for:  email recs, non-urgent personalization<br><br>Example: pre-compute top-1000 videos<br>per user nightly → Redis hash</div>
</div>
<div class="ab-col" style="border-top:2px solid var(--vio)">
<div class="ab-name" style="color:var(--white)">Real-Time Inference</div>
<div class="ab-sub" style="color:var(--vio)">LIVE MODEL · INFERENCE ON EVERY REQUEST</div>
<div class="ab-body">Model loaded in serving process. Inference runs on each request. Uses real-time features for freshest predictions.</div>
<div class="ab-code" style="color:var(--sub)">Latency:  10–100ms (model size-dependent)<br>Freshness: real-time features<br>Cost:      GPU/CPU for every request<br>Good for:  search ranking, ads, fraud detection<br><br>Server: TensorFlow Serving, Triton,<br>TorchServe — with request batching</div>
</div>
  </div>
  <div class="cb"><div class="cb-top">Model deployment strategies — safe rollout without downtime<span class="cb-l">DEPLOYMENT</span></div>


```python
// 1. SHADOW MODE — new model runs alongside old, results NOT shown to users
//    Log new model's predictions for offline analysis. Zero user impact.
user_response = champion_model.predict(features)    ← shown to user
shadow_result  = challenger_model.predict(features)  ← logged only
logger.log({"shadow_prediction": shadow_result, "actual_label": label})

// 2. CANARY — small % of real traffic to new model
if hash(user_id) % 100 < 5:    ← 5% canary
    return challenger_model.predict(features)
else:
    return champion_model.predict(features)

// 3. BLUE-GREEN — both versions hot, instant traffic switch
//    Keep v1 (blue) running. Deploy v2 (green). Validate green.
//    Switch load balancer: 100% → green. Keep blue for 1hr (fast rollback).
load_balancer.set_backend("green")   ← instant switch

// Automated rollback trigger:
if metrics.p99_latency > champion.p99_latency * 1.1:   ← 10% regression
    load_balancer.set_backend("blue")  ← instant rollback
    alerting.page("Challenger model rolled back: latency regression")
```


</div>
<!-- TWO TOWER -->
<div class="view" id="view-twotower">
  <div class="sh">Two-Tower Model</div>
  <div class="sr">The dominant architecture for large-scale recommendation retrieval</div>
  <div class="tower">
<div class="tw-label">// TWO-TOWER ARCHITECTURE — rank 10M items in &lt;100ms</div>
<div class="tw-cols">
<div class="tw-box" style="border-color:var(--vio)">
<div class="tw-title" style="color:var(--vio)">User Tower</div>
<div class="tw-input">Input features:<br>→ watch history (ids)<br>→ search queries<br>→ demographics<br>→ real-time context</div>
<div class="tw-output" style="color:var(--vio)">Output:<br>256-dim user embedding<br>computed at query time</div>
</div>
<div class="tw-center">⊙<br><span style="font-size:11px;font-family:'IBM Plex Mono',monospace;color:var(--sub)">dot<br>product</span></div>
<div class="tw-box" style="border-color:var(--cya)">
<div class="tw-title" style="color:var(--cya)">Item Tower</div>
<div class="tw-input">Input features:<br>→ video metadata<br>→ transcript embedding<br>→ view/like ratios<br>→ category / tags</div>
<div class="tw-output" style="color:var(--cya)">Output:<br>256-dim item embedding<br>pre-computed offline</div>
</div>
</div>
  </div>
  <div class="cb"><div class="cb-top">Two-stage pipeline — retrieval then ranking<span class="cb-l">SERVING FLOW</span></div>


```python
// STAGE 1: RETRIEVAL — find top-500 from 10M items in ~25ms
user_emb = user_tower.embed(user_features)     // 256-dim vector, ~5ms
candidates = ann_index.search(user_emb, k=500)  // ScaNN ANN search, ~15ms
// ANN index: 10M items × 256 dims × 4 bytes = ~10 GB → fits in RAM
// ScaNN achieves ~95% recall@100 at 10ms for 10M items

// STAGE 2: RANKING — score each of 500 candidates precisely
for item_id in candidates:
    item_features = feature_store.get(item_id)    // Redis batch fetch
    cross_features = compute_cross(user, item)    // interaction features
    score = ranking_model.predict(user_features, item_features, cross_features)

ranked = sorted(candidates, key=score, reverse=True)

// STAGE 3: POST-PROCESSING — business rules on top-100
final = post_processor.apply(ranked[:100], rules=[
    FilterWatched(user_id),         // don't show already-watched
    EnforceDiversity(max_per_topic=3), // not 10 Taylor Swift videos
    FreshnessBoost(hours=24),         // boost content <24h old
    SafetyFilter()                    // remove policy violations
])
return final[:20]  // top 20 to user
```


</div>
<!-- AB TEST -->
<div class="view" id="view-abtest">
  <div class="sh">A/B Testing at Scale</div>
  <div class="sr">The only way to measure causal impact — offline metrics are necessary but not sufficient</div>
  <div class="cb"><div class="cb-top">A/B test setup — the decisions that determine validity<span class="cb-l">DESIGN</span></div>


```python
// Split by USER (not by request) — same user always sees same model
// Splitting by request = same user gets both models = contamination
def get_model(user_id):
    bucket = hash(user_id) % 100
    if bucket < 5:   ← 5% treatment
        return challenger_model
    else:              ← 95% control
        return champion_model

// Sample size calculation:
// baseline CTR = 2%, minimum detectable effect = 0.2% (10% relative lift)
// power = 80%, significance = 0.05
n_per_group = sample_size(
    baseline=0.02, mde=0.002, power=0.8, alpha=0.05
)  → ~156,000 users per group → ~312K total

// Primary metric: business metric (CTR, watch time, conversion rate)
// NOT offline AUC — model can improve AUC while hurting business metrics
// Guardrail metrics: must not regress (latency p99, revenue, crash rate)

// Peeking problem: DO NOT stop early because p < 0.05 after 3 days
// Each time you check, you increase false positive rate.
// Fix: pre-commit to run duration (2 weeks), use sequential testing if early stopping needed
```


  <div class="drift-grid" style="margin-top:14px">
<div class="dg" style="border-left-color:var(--red)">
<div class="dg-name" style="color:var(--white)">Peeking</div>
<div class="dg-type" style="color:var(--red)">FALSE POSITIVES</div>
<div class="dg-body">Stopping when p&lt;0.05 after 3 days inflates false positive rate. Each check is another chance to see a "significant" result by chance.</div>
<div class="dg-detect" style="color:var(--sub)">Fix: pre-commit to duration.<br>Use sequential testing (always-valid p-values) if must check early.</div>
</div>
<div class="dg" style="border-left-color:var(--yel)">
<div class="dg-name" style="color:var(--white)">Novelty Effect</div>
<div class="dg-type" style="color:var(--yel)">INFLATED SHORT-TERM</div>
<div class="dg-body">Users click new UI just because it's new. Effect fades after 1–2 weeks. Short tests overestimate long-term impact.</div>
<div class="dg-detect" style="color:var(--sub)">Fix: run for minimum 2 weeks.<br>Check if effect is stable in week 2 vs week 1.</div>
</div>
<div class="dg" style="border-left-color:var(--vio)">
<div class="dg-name" style="color:var(--white)">Network Effects</div>
<div class="dg-type" style="color:var(--vio)">INTERFERENCE</div>
<div class="dg-body">On social networks, user A (control) interacts with user B (treatment). A is contaminated by B's treatment. Standard splits invalid.</div>
<div class="dg-detect" style="color:var(--sub)">Fix: cluster-based splitting.<br>Split by social clusters, not individual users.</div>
</div>
  </div>
</div>
<!-- DRIFT -->
<div class="view" id="view-drift">
  <div class="sh">Feature & Concept Drift</div>
  <div class="sr">Models degrade silently — active monitoring is mandatory in production</div>
  <div class="drift-grid">
<div class="dg" style="border-left-color:var(--ora)">
<div class="dg-name" style="color:var(--white)">Data Drift</div>
<div class="dg-type" style="color:var(--ora)">COVARIATE SHIFT</div>
<div class="dg-body">Input feature distribution changes. Training users were 18–35, now 13–60. Model was never trained on this input range.</div>
<div class="dg-detect" style="color:var(--sub)">Detection: PSI, KL divergence<br>on feature distributions daily.<br>PSI &gt; 0.2 = significant drift → retrain.</div>
</div>
<div class="dg" style="border-left-color:var(--red)">
<div class="dg-name" style="color:var(--white)">Concept Drift</div>
<div class="dg-type" style="color:var(--red)">LABEL RELATIONSHIP CHANGES</div>
<div class="dg-body">Feature → label relationship changes. "Free shipping" used to predict high intent; now it's table stakes and non-predictive.</div>
<div class="dg-detect" style="color:var(--sub)">Detection: online metrics (CTR,<br>conversion) vs offline eval baseline.<br>Drop &gt; threshold → triggered retrain.</div>
</div>
<div class="dg" style="border-left-color:var(--yel)">
<div class="dg-name" style="color:var(--white)">Label Drift</div>
<div class="dg-type" style="color:var(--yel)">LABEL DISTRIBUTION SHIFTS</div>
<div class="dg-body">Distribution of labels changes. Fraud rate increases from 0.1% to 0.3% due to a new attack vector. Model calibration is off.</div>
<div class="dg-detect" style="color:var(--sub)">Detection: monitor label frequency<br>in production feedback pipeline.<br>Retrain immediately on label drift.</div>
</div>
  </div>
  <div class="cb"><div class="cb-top">PSI — Population Stability Index — the standard drift metric<span class="cb-l">FORMULA</span></div>


```python
// PSI = Population Stability Index
// Compares distribution of a feature between training (baseline) and production (current)
// Higher PSI = more drift

// Formula:
PSI = Σ (P_current_i - P_baseline_i) × ln(P_current_i / P_baseline_i)

// Where P_i = proportion of observations in bucket i (e.g., 10 equal-frequency buckets)

// Thresholds (industry standard):
PSI < 0.1   → No significant change, model stable
PSI 0.1–0.2 → Minor shift, investigate further
PSI > 0.2   → Significant shift, retrain model

// Monitoring stack (6 daily metrics to track):
1. PSI per feature           ← data drift
2. Prediction score dist     ← model output drift
3. Null / missing rate       ← pipeline health
4. Business metric (CTR)     ← concept drift proxy
5. Label distribution        ← label drift
6. Inference latency p99     ← serving health
```


</div>
<!-- YOUTUBE -->
<div class="view" id="view-youtube">
  <div class="sh">YouTube Recommendations — Full ML System</div>
  <div class="sr">Connecting all concepts: 2B users, 800M DAU, 100ms budget</div>
  <div class="budget">
<div class="bg-label">// ONLINE LATENCY BUDGET — 100ms total</div>
<div class="bg-row">
<div class="bg-name">Feature retrieval</div>
<div class="bg-bar-wrap"><div class="bg-bar" style="width:10%;background:var(--grn)"></div></div>
<div class="bg-val">10ms</div>
</div>
<div class="bg-row">
<div class="bg-name">User embedding compute</div>
<div class="bg-bar-wrap"><div class="bg-bar" style="width:5%;background:var(--grn)"></div></div>
<div class="bg-val">5ms</div>
</div>
<div class="bg-row">
<div class="bg-name">ANN retrieval (10M items)</div>
<div class="bg-bar-wrap"><div class="bg-bar" style="width:15%;background:var(--yel)"></div></div>
<div class="bg-val">15ms</div>
</div>
<div class="bg-row">
<div class="bg-name">Ranking (500 candidates)</div>
<div class="bg-bar-wrap"><div class="bg-bar" style="width:40%;background:var(--vio)"></div></div>
<div class="bg-val">40ms</div>
</div>
<div class="bg-row">
<div class="bg-name">Post-processing</div>
<div class="bg-bar-wrap"><div class="bg-bar" style="width:5%;background:var(--grn)"></div></div>
<div class="bg-val">5ms</div>
</div>
<div class="bg-row">
<div class="bg-name">Network + overhead</div>
<div class="bg-bar-wrap"><div class="bg-bar" style="width:25%;background:var(--ora)"></div></div>
<div class="bg-val">25ms</div>
</div>
  </div>
  <div class="cb"><div class="cb-top">Offline pipeline — daily batch training cycle<span class="cb-l">OFFLINE</span></div>


```python
// FEATURE COMPUTATION (daily Spark jobs):
user_features  = compute(watch_history_30d, search_history_7d, demographics)
video_features = compute(view_count, like_ratio, avg_watch_pct, transcript_emb)
// → Written to BigQuery (offline) + Bigtable (online, low-latency lookup)

// TRAINING DATA GENERATION:
positives = events WHERE watch_pct > 0.5        // user watched >50% of video
negatives = sample(shown_but_not_clicked, n=10) // 10 negatives per positive
dataset   = join_pit_correct(positives + negatives, feature_store)

// TWO-TOWER RETRIEVAL TRAINING:
// Goal: Recall@100 (are ground-truth videos in top-100 from 10M?)
// Pre-index: all 10M video embeddings → ScaNN index (~10 GB in RAM)

// RANKING MODEL TRAINING:
// Input: (user_emb, video_emb, cross_features, context)
// Output: predicted watch time (regression)
// Eval: NDCG@20 on held-out test set

// A/B TEST PROMOTION:
// New model → 5% canary → primary metric: watch time per session
// Guardrail: p99 latency must not exceed 110ms
// Run 2 weeks → evaluate → ramp 5% → 10% → 50% → 100%
```


</div>
<!-- TASKS -->
<div class="view" id="view-tasks">
  <div class="task-list">
<div class="task-card">
<div class="task-hd" onclick="tt(this)"><div class="t-num">1</div><div class="t-lbl">Feature Store for Fraud Detection</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
<div class="task-bd">
<ol>
<li>List 10 features across user, transaction, and merchant dimensions needed for fraud detection.</li>
<li>Classify each as batch (daily), near-real-time (5-min), or real-time (&lt;1s). Justify each classification.</li>
<li>Design the online store schema. What is the key structure (entity_id + feature_name)? What TTL for each tier?</li>
<li>A transaction arrives. Walk through the full feature retrieval path end-to-end, including which store each feature comes from and estimated latency per call.</li>
<li>Training time: you have historical transactions from 6 months ago. How do you retrieve the user's "transactions in past hour" feature as it was at the time of each historical transaction? What schema makes this possible?</li>
</ol>
</div>
</div>
<div class="task-card">
<div class="task-hd" onclick="tt(this)"><div class="t-num">2</div><div class="t-lbl">A/B Test Design for New Ranking Model</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
<div class="task-bd">
<ol>
<li>What is your primary metric? Why not use offline AUC or NDCG as the decision metric?</li>
<li>Baseline CTR = 2%, minimum detectable effect = 0.2% (absolute), power = 80%, α = 0.05. How many users do you need per group?</li>
<li>Should you split by user, by session, or by request? What goes wrong with each wrong choice?</li>
<li>Your test shows p = 0.03 after 3 days. Should you ship? What are the two reasons not to?</li>
<li>After 2 weeks: treatment shows +3% CTR but −1% average session duration. What do you decide, and what does this tell you about the model?</li>
</ol>
</div>
</div>
<div class="task-card">
<div class="task-hd" onclick="tt(this)"><div class="t-num">3</div><div class="t-lbl">Drift Monitoring System</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
<div class="task-bd">
<ol>
<li>Your fraud model was trained 6 months ago. Which 3 features are most likely to have drifted? Why?</li>
<li>Write the PSI formula. What does each bucket represent? What threshold triggers retraining?</li>
<li>You detect label drift: fraud rate increased from 0.1% to 0.3%. Is this data drift or concept drift? What's your immediate response?</li>
<li>PSI is high on the "transaction_amount" feature. Before triggering a retrain, how do you determine if this is a real distribution shift vs a data pipeline bug (upstream schema change, null injection)?</li>
<li>Design the full monitoring dashboard: 6 metrics, alert thresholds, and escalation policy.</li>
</ol>
</div>
</div>
<div class="task-card" style="border-top:2px solid var(--vio)">
<div class="task-hd" onclick="tt(this)"><div class="t-num" style="color:var(--vio)">★</div><div class="t-lbl">Design a News Feed Ranking System</div><div class="t-meta">~3 hrs</div><div class="t-arr">›</div></div>
<div class="task-bd">
<p>Design the complete ML system for ranking a social media news feed (LinkedIn or Facebook scale).</p>
<ol>
<li>Objective function: engagement maximization leads to clickbait. How do you define an objective that balances engagement, time-well-spent, and content quality?</li>
<li>Two-stage pipeline: retrieval model (what towers?) + ranking model (what input features?).</li>
<li>Feature store: define 10 key features with their freshness tier and storage backend.</li>
<li>Cold-start problem: new user has no history. New post was created 5 minutes ago. How does your system handle both?</li>
<li>A/B test: primary metric, guardrail metrics, duration, and what split level (user/social cluster)?</li>
<li>You ship the model, and after 2 weeks users complain the feed feels addictive and manipulative. The model learned to maximize clicks by surfacing outrage. How do you fix this at the ML system level?</li>
</ol>
</div>
</div>
  </div>
</div>
<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 21 completed</span><span style="font-family:'IBM Plex Mono',monospace">MODULE C3 · ML SYSTEMS</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">ML stack: offline pipeline vs online pipeline, training-serving skew</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Feature store: offline (training) vs online (serving), point-in-time correctness</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Feature freshness tiers: real-time (&lt;1s Redis), near-RT (minutes), batch (hours)</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Point-in-time correctness: as_of=timestamp prevents data leakage</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Training pipeline: 6 stages from ingestion to model registration</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Retraining triggers: scheduled, drift-triggered, performance-triggered</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Batch vs real-time inference: latency vs freshness trade-off</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Deployment: shadow mode → canary → blue-green with automated rollback</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Two-tower model: user tower + item tower, dot product similarity</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Two-stage pipeline: ANN retrieval (500 candidates) → ranking → post-processing</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">ANN search: FAISS/ScaNN — ~15ms for 10M items in RAM</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">A/B testing: split by user, p-value, power, sample size calculation</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">A/B pitfalls: peeking, novelty effect, network effects → cluster splitting</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Primary metric = business metric, not offline AUC</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Data drift vs concept drift vs label drift — definitions and detection</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">PSI formula, thresholds: &lt;0.1 stable, 0.1-0.2 monitor, &gt;0.2 retrain</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">6 monitoring metrics: PSI, prediction dist, null rate, CTR, label dist, latency</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">YouTube recs: offline pipeline + 100ms online budget breakdown</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 1: feature store for fraud detection</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 2: A/B test design with sample size calculation</div></div>
<div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 4 (capstone): news feed ranking ML system</div></div>
  </div>
  <div style="margin-top:28px;background:var(--panel);border:1px solid var(--bord2);padding:22px;border-top:2px solid var(--vio)">
<div style="font-family:'IBM Plex Mono',monospace;font-size:8px;color:var(--muted);letter-spacing:2px;margin-bottom:8px">// NEXT MODULE</div>
<div style="font-family:'Syne',sans-serif;font-size:24px;font-weight:700;color:var(--white);margin-bottom:6px">C4 — Observability & SRE</div>
<div style="font-family:'IBM Plex Mono',monospace;font-size:9.5px;color:var(--sub);line-height:2">
      Metrics, logs, traces — the three pillars · SLO/SLI/SLA<br>
      Distributed tracing (Jaeger, Zipkin) · Alerting design<br>
      Incident response · On-call · Error budgets · Chaos engineering
</div>
  </div>
</div>
</div>
<div class="mb-nav">
  <a href="/learning/system-design/hld/module-b12-interview-framework/">← B12 Interview Framework</a>
  <a href="/learning/system-design/hld/module-b13-notes/">📄 Study Notes</a>
  <a href="/learning/system-design/system-design-roadmap/">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-b14-kubernetes/" class="primary">B14 Kubernetes →</a>
</div>
<script src="/assets/js/sd-module-b13.js"></script>
