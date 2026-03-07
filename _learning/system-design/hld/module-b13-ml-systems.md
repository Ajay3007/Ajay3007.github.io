---
layout: default
title: "Module B13: ML Systems Design"
permalink: /learning/system-design/hld/module-b13-ml-systems/
---

<link rel="stylesheet" href="{{ "/assets/css/sd-module-b13.css" | relative_url }}">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">

<div class="sd-module-b13">

<header>
  <div class="hdr-stamp">
    <span>SYSTEM DESIGN MASTERY · TRACK B · MODULE B13 · WEEK 15</span>
    <span>ML SYSTEMS DESIGN · FEATURE STORES · MLOPS</span>
  </div>
  <div class="hdr-main">
    <div>
      <div class="hdr-kicker">TRAINING & INFERENCE · CONTINUOUS LEARNING</div>
      <h1>ML SYSTEMS<br>DESIGN</h1>
      <div class="hdr-sub">Moving beyond notebook models to production-grade distributed machine learning. Master the architecture for feature engineering, low-latency model serving, continuous training, and recommender systems at internet scale.</div>
    </div>
    <div class="hdr-stats">
      <div class="hs"><div class="hs-v">4</div><div class="hs-l">CORE PIPELINES</div></div>
      <div class="hs"><div class="hs-v">&lt;20ms</div><div class="hs-l">P99 INFERENCE</div></div>
      <div class="hs"><div class="hs-v">1</div><div class="hs-l">MINI PROJECT</div></div>
      <div class="hs"><div class="hs-v">B13</div><div class="hs-l">ML TRACK</div></div>
    </div>
  </div>
</header>

<nav class="nav">
  <div class="nt active" onclick="mb13_show('lifecycle', this)">ML Lifecycle</div>
  <div class="nt" onclick="mb13_show('features', this)">Feature Stores</div>
  <div class="nt" onclick="mb13_show('serving', this)">Training & Serving</div>
  <div class="nt" onclick="mb13_show('recsys', this)">RecSys Design</div>
  <div class="nt" onclick="mb13_show('qa', this)">Quick Answers</div>
  <div class="nt" onclick="mb13_show('checklist', this)">Checklist</div>
</nav>

<div class="content">

<!-- LIFECYCLE -->
<div class="view active" id="view-lifecycle">
  <div class="sh">The Production ML Lifecycle</div>
  <div class="sr">Software Engineering creates systems; ML Engineering creates systems that create themselves.</div>
  
  <div class="al"><em>Paradigm Shift:</em> In traditional software, `Code + Data = Output`. In ML systems, `Data + Expected Output = Code (Model)`. This makes data the primary driver of system behavior, requiring entirely new monitoring and deployment patterns.</div>

  <div class="pipe-grid">
    <div class="pipe">
      <div class="pipe-title">1. Data Ingestion & Storage</div>
      <div class="pipe-desc">Streaming (Kafka/Kinesis) and batch (S3/HDFS) ingestion. Creating data lakes and data warehouses (Snowflake/BigQuery). <span class="pipe-hl">Focus: Throughput & Schema Validation</span></div>
    </div>
    <div class="pipe">
      <div class="pipe-title">2. Feature Engineering</div>
      <div class="pipe-desc">Transforming raw data into predictive signals. Handled by processing engines (Spark, Flink). Output is materialized into a Feature Store. <span class="pipe-hl">Focus: Training-Serving Skew Prevention</span></div>
    </div>
    <div class="pipe">
      <div class="pipe-title">3. Model Training</div>
      <div class="pipe-desc">Distributed training jobs via Kubernetes (Kubeflow, Ray). Hyperparameter tuning. Tracking experiments (MLflow/Weights & Biases). <span class="pipe-hl">Focus: Reproducibility & Resource Management (GPUs)</span></div>
    </div>
    <div class="pipe">
      <div class="pipe-title">4. Model Serving</div>
      <div class="pipe-desc">Deploying the artifact. Batch inference (airflow jobs), real-time RPC/HTTP inference (TFServing, NVIDIA Triton), or edge deployment. <span class="pipe-hl">Focus: Low Latency & High Availability</span></div>
    </div>
    <div class="pipe">
      <div class="pipe-title">5. Monitoring & Retraining</div>
      <div class="pipe-desc">Shadow deployments. A/B testing framework. Monitoring for data drift and concept drift to trigger pipeline reruns. <span class="pipe-hl">Focus: Continuous Learning (CT)</span></div>
    </div>
  </div>
</div>

<!-- FEATURE STORES -->
<div class="view" id="view-features">
  <div class="sh">Feature Store Architecture</div>
  <div class="sr">The bridge between data engineering and machine learning.</div>

  <div class="al warn"><em>The Problem:</em> "Training-Serving Skew." You calculate features differently in Pandas during training than you do in Java/Go during real-time serving. This degrades model performance silently in production.</div>

  <div class="card-grid">
    <div class="card">
      <div class="card-ht">Offline Store (Training)</div>
      <div class="card-bd">Backed by column-oriented storage (S3 + Parquet, BigQuery, Snowflake). Optimized for massive point-in-time correct queries. When training, the model needs to see the user's click-rate exactly as it was *at the time* of the historical interaction, preventing data leakage from the future.</div>
    </div>
    <div class="card">
      <div class="card-ht">Online Store (Serving)</div>
      <div class="card-bd">Backed by ultra-fast in-memory/NoSQL DBs (Redis, DynamoDB, Cassandra). Optimized for low-latency, single-entity lookups. When an inference request arrives, the serving layer queries the Key-Value store with a `user_id` to get the latest pre-computed feature vectors in &lt;5ms.</div>
    </div>
  </div>

  <div class="sh">Standard Flow</div>
  <div class="sr">How features propagate in modern ML architectures</div>
  <div style="font-family: 'JetBrains Mono', monospace; font-size: 13px; line-height: 2; padding: 20px; background: var(--panel); border: 1px solid var(--bord);">
    1. Batch Jobs (Spark) → Offline Store<br>
    2. Streaming Jobs (Flink) + Batch sync → Online Store<br>
    3. Training Pipeline → Queries Offline Store (Point-in-time join)<br>
    4. Inference Service → Queries Online Store (Latest values)
  </div>
</div>

<!-- SERVING -->
<div class="view" id="view-serving">
  <div class="sh">Training & Serving Infrastructure</div>
  <div class="sr">Delivering predictions to the end user under strict SLAs.</div>

  <div class="card-grid">
    <div class="card">
      <div class="card-ht">Real-time Inference</div>
      <div class="card-bd">The model runs as a microservice (e.g., REST/gRPC on Kubernetes). Challenge: Models (especially deep learning) are computationally heavy. Solutions involve batching multiple incoming requests to fully utilize GPU memory (e.g., Nvidia Triton Dynamic Batching), and model quantization (FP16/INT8).</div>
    </div>
    <div class="card">
      <div class="card-ht">Batch Inference</div>
      <div class="card-bd">The model runs on a schedule against a vast dataset. Results are saved directly to a database, and the web backend simply performs a DB lookup. Excellent for recommender systems where recommendations can be pre-computed nightly. Massive cost savings compared to real-time.</div>
    </div>
  </div>

  <div class="sh">Safe Deployment Strategies</div>
  <div class="pipe-grid">
    <div class="pipe">
      <div class="pipe-title">Shadow Mode</div>
      <div class="pipe-desc">New model receives live production traffic, makes predictions asynchronously, but outputs are discarded. Used to monitor latency, error rates, and compare predictions with the current model without user impact.</div>
    </div>
    <div class="pipe">
      <div class="pipe-title">Canary Deploy</div>
      <div class="pipe-desc">Roll out new model to 1% of users. Monitor strictly for crashes and response latency. Incrementally increase to 100%.</div>
    </div>
    <div class="pipe">
      <div class="pipe-title">A/B Testing</div>
      <div class="pipe-desc">Roll out to 10% of users. Evaluate business metrics (e.g., Click-Through Rate) over weeks. Essential because better offline validation metrics don't always translate to better online business metrics.</div>
    </div>
  </div>
</div>

<!-- RECSYS -->
<div class="view" id="view-recsys">
  <div class="sh">Recommender System Architecture</div>
  <div class="sr">The canonical ML system design interview (YouTube, Netflix, TikTok)</div>

  <div class="al"><em>The Goal:</em> Select 10 highly relevant items for a user out of a corpus of 1 Billion items in under 200 milliseconds. Doing this via brute force requires running a neural network 1 Billion times per request — completely impossible.</div>

  <div class="pipe-grid" style="counter-reset: recsys;">
    <div class="pipe">
      <div class="pipe-title">1. Candidate Generation</div>
      <div class="pipe-desc">Reduce 1,000,000,000 items to ~1,000 items. Fast, coarse-grained models (e.g., Two-Tower Network, Matrix Factorization, collaborative filtering). Output is often cached or computed via fast Nearest Neighbor search (FAISS, Annoy, HNSW).</div>
    </div>
    <div class="pipe">
      <div class="pipe-title">2. Scoring (Ranking)</div>
      <div class="pipe-desc">Reduce 1,000 items to 50 items. A heavy, complex model (e.g., Deep & Cross Networks, Transformer) predicts the probability of click/watch for each of the 1,000 items. Because N is small, we can afford heavy computation per item here.</div>
    </div>
    <div class="pipe">
      <div class="pipe-title">3. Re-Ranking (Policy & Logic)</div>
      <div class="pipe-desc">Apply business rules to the top 50 items to get the final 10. Rules include: removing previously clicked items, enforcing diversity (not all videos from same creator), injecting sponsored/promoted content, filtering NSFW content.</div>
    </div>
  </div>
</div>

<!-- QA -->
<div class="view" id="view-qa">
  <div class="sh">Quick Answers</div>
  <div class="sr">Crucial concepts you must be able to explain in 30 seconds.</div>

  <div class="qa-list">
    <div class="qa">
      <div class="qa-hd" onclick="mb13_qa(this)">
        <div class="qa-q">What is Concept Drift vs Data Drift?</div>
        <div class="qa-arr">▶</div>
      </div>
      <div class="qa-bd"><strong>Data Drift:</strong> The distribution of incoming data changes over time (e.g., a sensor degrades and records higher temperatures). <br><br><strong>Concept Drift:</strong> The relationship between the input and the target changes (e.g., a pandemic changes consumer buying habits; what constituted a "fraudulent transaction" yesterday is normal today). Both require retraining the model with recent data.</div>
    </div>
    
    <div class="qa">
      <div class="qa-hd" onclick="mb13_qa(this)">
        <div class="qa-q">How do you scale approximate nearest neighbor (ANN) search?</div>
        <div class="qa-arr">▶</div>
      </div>
      <div class="qa-bd">ANN algorithms (like HNSW or FAISS) pre-index high-dimensional vectors. To scale to billions of vectors, you shard the vector index across multiple machines. A query goes to an aggregator, which scatters the query to all shards, gathers the top-K from each, and returns the global top-K. Use an in-memory vector database like Milvus or Pinecone.</div>
    </div>

    <div class="qa">
      <div class="qa-hd" onclick="mb13_qa(this)">
        <div class="qa-q">What is the "Point-in-Time Join" problem?</div>
        <div class="qa-arr">▶</div>
      </div>
      <div class="qa-bd">When creating training data, you must merge historical events with features exactly as they existed at the timestamp of the event. If you use the *latest* feature value instead of the historical one, the model "sees the future" (Data Leakage). Feature stores handle this by maintaining temporal logs and providing an "AS OF" join capability.</div>
    </div>
  </div>
</div>

<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 6 completed</span><span>MODULE B13 PROGRESS</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>

  <div class="chk-grid">
    <div class="chk" onclick="mb13_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can explain the 5 stages of the ML lifecycle.</div></div>
    <div class="chk" onclick="mb13_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Understand the difference between Offline and Online feature stores.</div></div>
    <div class="chk" onclick="mb13_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can articulate the funnel for Recommender Systems: Generation -> Ranking -> Reranking.</div></div>
    <div class="chk" onclick="mb13_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Grasp the deployment strategies: Shadow, Canary, A/B Testing.</div></div>
    <div class="chk" onclick="mb13_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Familiar with Real-time inference challenges (Dynamic Batching, GPU utilization).</div></div>
    <div class="chk" onclick="mb13_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Mini Project: Architected a Recommendation System (YouTube/Netflix style).</div></div>
  </div>
</div>

</div>

<div class="mb-nav">
  <a href="/learning/system-design/hld/module-b12-interview-framework/" class="btn">← B12 INTERVIEW FRAMEWORK</a>
  <a href="/learning/system-design/hld/module-b14-kubernetes/" class="btn">B14 KUBERNETES →</a>
</div>

</div>
<script src="{{ "/assets/js/sd-module-b13.js" | relative_url }}"></script>
