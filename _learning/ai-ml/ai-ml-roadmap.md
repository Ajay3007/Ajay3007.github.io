---
layout: default
title: AI & Machine Learning Roadmap
permalink: /learning/ai-ml/ai-ml-roadmap/
custom_css: ai-ml-roadmap
custom_js: ai-ml-roadmap
---

<!-- Breadcrumb -->
<div class="aiml-breadcrumb">
  <a href="{{ '/roadmap/' | relative_url }}">🗺️ All Roadmaps</a>
  <span>›</span>
  <span>AI & Machine Learning</span>
</div>

<!-- Hero -->
<div class="aiml-hero">
  <h1>🤖 AI & Machine Learning Roadmap</h1>
  <p>A complete, project-based curriculum — from Python fundamentals to production-ready GenAI systems. 9 modules, 30+ weeks, 4 career tracks.</p>
  <div class="aiml-hero-stats">
    <div class="aiml-stat"><span class="aiml-stat-val">9</span><span class="aiml-stat-lbl">Modules</span></div>
    <div class="aiml-stat"><span class="aiml-stat-val">30+</span><span class="aiml-stat-lbl">Weeks</span></div>
    <div class="aiml-stat"><span class="aiml-stat-val">4</span><span class="aiml-stat-lbl">Career Paths</span></div>
    <div class="aiml-stat"><span class="aiml-stat-val">Python</span><span class="aiml-stat-lbl">Primary Lang</span></div>
  </div>
</div>

<!-- Overall Progress -->
<div class="aiml-overall-progress">
  <span class="aiml-op-label">📊 Your Progress</span>
  <div class="aiml-op-bar-wrap"><div class="aiml-op-bar"></div></div>
  <span class="aiml-op-pct">0%</span>
  <span class="aiml-op-count">Loading…</span>
</div>

<!-- Career Path Selector -->
<p class="aiml-section-title">🎯 Choose Your Career Track <small style="font-size:0.75rem;font-weight:400;color:var(--light-text);">— click to highlight relevant modules</small></p>
<div class="career-grid">
  <div class="career-card" data-role="analyst">
    <div class="career-card-icon">📊</div>
    <div class="career-card-title">Data Analyst</div>
    <div class="career-card-salary">₹8–18 LPA · $65–90K</div>
    <div class="career-card-modules">M1 · M2 · M3</div>
  </div>
  <div class="career-card" data-role="scientist">
    <div class="career-card-icon">🔬</div>
    <div class="career-card-title">Data Scientist</div>
    <div class="career-card-salary">₹12–25 LPA · $90–130K</div>
    <div class="career-card-modules">M1 → M5.5</div>
  </div>
  <div class="career-card" data-role="engineer">
    <div class="career-card-icon">⚙️</div>
    <div class="career-card-title">ML Engineer</div>
    <div class="career-card-salary">₹15–30 LPA · $110–160K</div>
    <div class="career-card-modules">M1–M5.5 · M8</div>
  </div>
  <div class="career-card" data-role="aigenai">
    <div class="career-card-icon">🧠</div>
    <div class="career-card-title">AI / GenAI Engineer</div>
    <div class="career-card-salary">₹18–40 LPA · $120–180K</div>
    <div class="career-card-modules">M1–M3 · M5.5 · M6 · M8</div>
  </div>
</div>

<!-- Math Prerequisites (collapsed) -->
<div class="prereq-accordion">
  <div class="prereq-header">
    <div class="prereq-header-left">
      <span>📐</span>
      <h3>Math & Statistics Prerequisites</h3>
      <span class="prereq-badge">Optional — can study alongside modules</span>
    </div>
    <span class="prereq-chevron">▼</span>
  </div>
  <div class="prereq-body">
    <p style="font-size:0.85rem;color:var(--light-text);margin:0.75rem 0;">You do NOT need to master all of this before starting. Study these in parallel with Modules 1–3. Engineering graduates (IIT/NIT/B.Tech) can skip straight to the Stats section.</p>
    <div class="prereq-grid">
      <div class="prereq-card">
        <h4>1. Linear Algebra</h4>
        <ul>
          <li><strong>Vectors & Matrices</strong> — data is stored as matrices, weights are vectors (Module 3, 4)</li>
          <li><strong>Matrix Multiplication</strong> — forward pass in neural networks (Module 5.5, 6)</li>
          <li><strong>Dot Product</strong> — similarity scores, attention mechanism (Module 6)</li>
          <li><strong>Eigenvalues/Eigenvectors</strong> — PCA dimensionality reduction (Module 5)</li>
          <li><strong>Transpose & Inverse</strong> — feature transformations (Module 3, 4)</li>
        </ul>
      </div>
      <div class="prereq-card">
        <h4>2. Calculus</h4>
        <ul>
          <li><strong>Derivatives</strong> — how models learn via gradient descent</li>
          <li><strong>Partial Derivatives</strong> — multi-variable loss functions</li>
          <li><strong>Chain Rule</strong> — backpropagation in neural nets</li>
          <li><strong>Maxima/Minima</strong> — finding optimal model parameters</li>
        </ul>
      </div>
      <div class="prereq-card">
        <h4>3. Probability & Statistics</h4>
        <ul>
          <li><strong>Mean/Median/Std Dev</strong> — understand data distributions (M3)</li>
          <li><strong>Normal Distribution</strong> — assumptions in ML models (M3, M4)</li>
          <li><strong>Bayes Theorem</strong> — Naive Bayes, probabilistic models (M4)</li>
          <li><strong>Hypothesis Testing</strong> — model evaluation, A/B testing (M3)</li>
          <li><strong>Correlation & Covariance</strong> — feature selection & EDA (M3)</li>
        </ul>
      </div>
    </div>
    <div class="prereq-resources">
      <h4>📚 Free Math Resources</h4>
      <div class="prereq-link-row">
        <a href="https://www.khanacademy.org/math/linear-algebra" target="_blank" class="prereq-link">🎓 Khan Academy — Linear Algebra</a>
        <a href="https://www.khanacademy.org/math/statistics-probability" target="_blank" class="prereq-link">🎓 Khan Academy — Statistics</a>
        <a href="https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab" target="_blank" class="prereq-link">▶️ 3Blue1Brown — Linear Algebra</a>
        <a href="https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr" target="_blank" class="prereq-link">▶️ 3Blue1Brown — Calculus</a>
        <a href="https://mml-book.github.io/" target="_blank" class="prereq-link">📖 Mathematics for ML (Free PDF)</a>
        <a href="https://www.youtube.com/@statquest" target="_blank" class="prereq-link">▶️ StatQuest — ML & Stats</a>
      </div>
    </div>
  </div>
</div>

<p class="aiml-section-title">📚 Modules</p>
<div class="modules-list">

<!-- M1 -->
<div class="module-card" data-module="m1" data-roles="analyst,scientist,engineer,aigenai" style="--mod-accent: linear-gradient(90deg,#a78bfa,#6366f1);">
  <div class="module-header">
    <div class="module-num-badge">M1</div>
    <div class="module-title-block">
      <h2>Python Programming Fundamentals</h2>
      <div class="module-meta">
        <span class="mod-badge">3 Weeks</span>
        <span class="mod-badge beginner">Beginner</span>
        <span class="mod-badge">All Roles</span>
      </div>
    </div>
    <span class="module-chevron">▼</span>
  </div>
  <div class="module-progress-row">
    <div class="mod-prog-bar-wrap"><div class="mod-prog-bar"></div></div>
    <span class="mod-prog-text">0/3 weeks</span>
    <span class="mod-prog-pct">0%</span>
  </div>
  <div class="module-body">
    <div class="module-section-title">What You'll Learn</div>
    <ul class="learn-list">
      <li>Core syntax: variables, data types, type casting, f-strings</li>
      <li>Data structures: lists, tuples, dictionaries, sets</li>
      <li>Flow control: if/elif/else, for/while loops, break/continue</li>
      <li>Functions: parameters, return values, *args/**kwargs</li>
      <li>File I/O: read/write text & CSV files</li>
      <li>Error handling: try/except/finally blocks</li>
      <li>OOP fundamentals: classes, objects, __init__, methods</li>
    </ul>
    <div class="module-section-title">Weekly Progress</div>
    <ul class="week-list">
      <li class="week-item" data-key="m1-w1"><div class="week-check-box"></div><div><span class="week-badge">W1</span><div class="week-label">Python setup, variables, data types, strings, lists</div><div class="week-tasks">Mini-projects: unit converter, palindrome checker, shopping list app</div></div></li>
      <li class="week-item" data-key="m1-w2"><div class="week-check-box"></div><div><span class="week-badge">W2</span><div class="week-label">Dictionaries, sets, if/elif/else, for/while loops</div><div class="week-tasks">Mini-projects: phone book, number guessing game, grade classifier</div></div></li>
      <li class="week-item" data-key="m1-w3"><div class="week-check-box"></div><div><span class="week-badge">W3</span><div class="week-label">Functions, File I/O, error handling, intro to OOP</div><div class="week-tasks">Mini-projects: student grade calculator (CSV), bank account OOP class</div></div></li>
    </ul>
    <div class="milestone-box">
      <h4>🏆 M1 Milestone — CLI Student Grade Management System</h4>
      <p>Build a command-line app that reads/writes student data from CSV, calculates grades & GPA, filters/sorts by score, handles invalid input gracefully. Beginner · 3–4 days</p>
      <div class="milestone-tags"><span class="milestone-tag">File I/O</span><span class="milestone-tag">Dictionaries</span><span class="milestone-tag">Functions</span><span class="milestone-tag">CSV</span><span class="milestone-tag">OOP</span></div>
    </div>
    <div class="module-section-title">Free Resources</div>
    <div class="resource-grid">
      <a href="https://cs50.harvard.edu/python/2022/" target="_blank" class="resource-link"><span class="resource-icon">🎓</span><span class="resource-info"><span class="resource-name">CS50P — Harvard Python</span><span class="resource-cat">Best free Python course</span></span></a>
      <a href="https://www.youtube.com/watch?v=rfscVS0vtbw" target="_blank" class="resource-link"><span class="resource-icon">▶️</span><span class="resource-info"><span class="resource-name">freeCodeCamp Python (4.5h)</span><span class="resource-cat">YouTube — complete intro</span></span></a>
      <a href="https://www.kaggle.com/learn/python" target="_blank" class="resource-link"><span class="resource-icon">🏅</span><span class="resource-info"><span class="resource-name">Kaggle Python Course</span><span class="resource-cat">Free, interactive exercises</span></span></a>
      <a href="https://automatetheboringstuff.com/" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">Automate the Boring Stuff</span><span class="resource-cat">Free book, project-oriented</span></span></a>
      <a href="https://colab.research.google.com/" target="_blank" class="resource-link"><span class="resource-icon">☁️</span><span class="resource-info"><span class="resource-name">Google Colab</span><span class="resource-cat">Free cloud Jupyter, zero setup</span></span></a>
      <a href="https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU" target="_blank" class="resource-link"><span class="resource-icon">▶️</span><span class="resource-info"><span class="resource-name">Corey Schafer — Python OOP</span><span class="resource-cat">YouTube — OOP deep dive</span></span></a>
    </div>
  </div>
</div>

<!-- M2 -->
<div class="module-card" data-module="m2" data-roles="analyst,scientist,engineer,aigenai" style="--mod-accent: linear-gradient(90deg,#8b5cf6,#a78bfa);">
  <div class="module-header">
    <div class="module-num-badge">M2</div>
    <div class="module-title-block">
      <h2>The Data Handling Toolkit — NumPy & Pandas</h2>
      <div class="module-meta">
        <span class="mod-badge">3 Weeks</span>
        <span class="mod-badge beginner">Beginner–Int.</span>
        <span class="mod-badge">All Roles</span>
      </div>
    </div>
    <span class="module-chevron">▼</span>
  </div>
  <div class="module-progress-row">
    <div class="mod-prog-bar-wrap"><div class="mod-prog-bar"></div></div>
    <span class="mod-prog-text">0/3 weeks</span>
    <span class="mod-prog-pct">0%</span>
  </div>
  <div class="module-body">
    <div class="module-section-title">What You'll Learn</div>
    <ul class="learn-list">
      <li>NumPy: arrays, vectorised ops, broadcasting, slicing, reshaping</li>
      <li>Pandas: Series & DataFrame creation, indexing, loc/iloc</li>
      <li>Data cleaning: handling NaN, duplicates, dtypes, outliers</li>
      <li>GroupBy, aggregation (.agg, .transform), pivot tables</li>
      <li>Merging & joining DataFrames (merge, join, concat)</li>
      <li>String operations: .str.lower, .str.contains, .str.replace</li>
      <li>DateTime handling: pd.to_datetime, .dt.year, .dt.month</li>
    </ul>
    <div class="module-section-title">Weekly Progress</div>
    <ul class="week-list">
      <li class="week-item" data-key="m2-w4"><div class="week-check-box"></div><div><span class="week-badge">W4</span><div class="week-label">NumPy arrays, vectorised operations, broadcasting</div><div class="week-tasks">Exercises: array math, slicing 2D arrays, random number generation</div></div></li>
      <li class="week-item" data-key="m2-w5"><div class="week-check-box"></div><div><span class="week-badge">W5</span><div class="week-label">Pandas Series & DataFrame, indexing, data cleaning</div><div class="week-tasks">Clean Titanic dataset: fix dtypes, handle NaN, remove duplicates</div></div></li>
      <li class="week-item" data-key="m2-w6"><div class="week-check-box"></div><div><span class="week-badge">W6</span><div class="week-label">GroupBy, merge, pivot tables, string ops, datetime</div><div class="week-tasks">Top 5 countries by COVID cases; merge datasets; aggregate by month</div></div></li>
    </ul>
    <div class="milestone-box">
      <h4>🏆 M2 Milestone — COVID-19 Global Data Analysis</h4>
      <p>Load & clean COVID-19 data, compute rolling 7-day averages, find top-10 countries by deaths-per-million, identify surge months with groupby+datetime, export cleaned CSV. Beginner · 4–5 days</p>
      <div class="milestone-tags"><span class="milestone-tag">NumPy</span><span class="milestone-tag">Pandas</span><span class="milestone-tag">GroupBy</span><span class="milestone-tag">DateTime</span><span class="milestone-tag">CSV</span></div>
    </div>
    <div class="module-section-title">Free Resources</div>
    <div class="resource-grid">
      <a href="https://www.kaggle.com/learn/pandas" target="_blank" class="resource-link"><span class="resource-icon">🏅</span><span class="resource-info"><span class="resource-name">Kaggle Pandas Course</span><span class="resource-cat">Best hands-on Pandas</span></span></a>
      <a href="https://www.youtube.com/watch?v=QUT1VHiLmmI" target="_blank" class="resource-link"><span class="resource-icon">▶️</span><span class="resource-info"><span class="resource-name">NumPy for Beginners (fCC)</span><span class="resource-cat">YouTube — complete NumPy</span></span></a>
      <a href="https://pandas.pydata.org/docs/user_guide/" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">Pandas Official User Guide</span><span class="resource-cat">Official reference</span></span></a>
      <a href="https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS" target="_blank" class="resource-link"><span class="resource-icon">▶️</span><span class="resource-info"><span class="resource-name">Corey Schafer — Pandas</span><span class="resource-cat">YouTube deep-dive playlist</span></span></a>
      <a href="https://www.kaggle.com/datasets/imdevskp/corona-virus-report" target="_blank" class="resource-link"><span class="resource-icon">📊</span><span class="resource-info"><span class="resource-name">COVID-19 Dataset (Kaggle)</span><span class="resource-cat">Milestone project dataset</span></span></a>
      <a href="https://www.kaggle.com/c/titanic" target="_blank" class="resource-link"><span class="resource-icon">📊</span><span class="resource-info"><span class="resource-name">Titanic Dataset (Kaggle)</span><span class="resource-cat">Missing values, groupby practice</span></span></a>
    </div>
  </div>
</div>

<!-- M3 -->
<div class="module-card" data-module="m3" data-roles="analyst,scientist,engineer,aigenai" style="--mod-accent: linear-gradient(90deg,#7c3aed,#a78bfa);">
  <div class="module-header">
    <div class="module-num-badge">M3</div>
    <div class="module-title-block">
      <h2>Statistical Thinking, EDA & ML Workflow</h2>
      <div class="module-meta">
        <span class="mod-badge">4 Weeks</span>
        <span class="mod-badge intermediate">Intermediate</span>
        <span class="mod-badge">All Roles</span>
      </div>
    </div>
    <span class="module-chevron">▼</span>
  </div>
  <div class="module-progress-row">
    <div class="mod-prog-bar-wrap"><div class="mod-prog-bar"></div></div>
    <span class="mod-prog-text">0/4 weeks</span>
    <span class="mod-prog-pct">0%</span>
  </div>
  <div class="module-body">
    <div class="module-section-title">What You'll Learn</div>
    <ul class="learn-list">
      <li>Descriptive statistics: mean, median, variance, skewness, kurtosis</li>
      <li>Matplotlib fundamentals: figures, axes, subplots, styling</li>
      <li>Seaborn: histplot, boxplot, violin, pairplot, heatmap, regplot</li>
      <li>Feature engineering: one-hot encoding, label encoding, binning, log transform</li>
      <li>Feature scaling: StandardScaler, MinMaxScaler, RobustScaler</li>
      <li>Handling class imbalance: SMOTE oversampling, undersampling</li>
      <li>ML workflow: train-test split, k-fold cross-validation, sklearn Pipeline</li>
    </ul>
    <div class="module-section-title">Weekly Progress</div>
    <ul class="week-list">
      <li class="week-item" data-key="m3-w7"><div class="week-check-box"></div><div><span class="week-badge">W7</span><div class="week-label">Descriptive stats, correlation matrices, outlier detection, Matplotlib subplots</div><div class="week-tasks">Plot house price distributions, correlation heatmap on Titanic</div></div></li>
      <li class="week-item" data-key="m3-w8"><div class="week-check-box"></div><div><span class="week-badge">W8</span><div class="week-label">Seaborn: boxplot, violin, pairplot, scatter regplot, multi-variate analysis</div><div class="week-tasks">Build full EDA report with 6+ visualisations on any dataset</div></div></li>
      <li class="week-item" data-key="m3-w9"><div class="week-check-box"></div><div><span class="week-badge">W9</span><div class="week-label">Encoding, binning, log transforms, polynomial features, feature selection</div><div class="week-tasks">Transform Titanic dataset — encode categoricals, create FamilySize feature</div></div></li>
      <li class="week-item" data-key="m3-w10"><div class="week-check-box"></div><div><span class="week-badge">W10</span><div class="week-label">Scalers, stratified train-test split, k-fold CV, sklearn Pipeline, data leakage demo</div><div class="week-tasks">Build full preprocessing pipeline; compare CV vs no-CV scores</div></div></li>
    </ul>
    <div class="milestone-box">
      <h4>🏆 M3 Milestone — End-to-End EDA & Feature Engineering Report</h4>
      <p>On a real dataset: statistical summary, 8+ visualisations, outlier treatment, feature engineering (encode + scale + 2 new features), correlation-based feature selection, stratified split, save processed dataset. Intermediate · 5–6 days</p>
      <div class="milestone-tags"><span class="milestone-tag">EDA</span><span class="milestone-tag">Matplotlib</span><span class="milestone-tag">Seaborn</span><span class="milestone-tag">Feature Eng.</span><span class="milestone-tag">sklearn Pipeline</span></div>
    </div>
    <div class="module-section-title">Free Resources</div>
    <div class="resource-grid">
      <a href="https://www.youtube.com/@statquest" target="_blank" class="resource-link"><span class="resource-icon">▶️</span><span class="resource-info"><span class="resource-name">StatQuest — ML Stats</span><span class="resource-cat">Best stats intuition on YouTube</span></span></a>
      <a href="https://www.kaggle.com/learn/data-visualization" target="_blank" class="resource-link"><span class="resource-icon">🏅</span><span class="resource-info"><span class="resource-name">Kaggle Data Visualisation</span><span class="resource-cat">Free interactive course</span></span></a>
      <a href="https://www.kaggle.com/learn/feature-engineering" target="_blank" class="resource-link"><span class="resource-icon">🏅</span><span class="resource-info"><span class="resource-name">Kaggle Feature Engineering</span><span class="resource-cat">Free interactive course</span></span></a>
      <a href="https://scikit-learn.org/stable/modules/preprocessing.html" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">Scikit-learn Preprocessing</span><span class="resource-cat">Scaling & encoding guide</span></span></a>
      <a href="https://www.youtube.com/playlist?list=PLZoTAELRMXVPfBTFOiIXGXGpEPVrKnOlb" target="_blank" class="resource-link"><span class="resource-icon">▶️</span><span class="resource-info"><span class="resource-name">Krish Naik — EDA Playlist</span><span class="resource-cat">YouTube EDA walkthroughs</span></span></a>
      <a href="https://www.kaggle.com/c/house-prices-advanced-regression-techniques" target="_blank" class="resource-link"><span class="resource-icon">📊</span><span class="resource-info"><span class="resource-name">House Prices Dataset</span><span class="resource-cat">EDA + feature engineering</span></span></a>
    </div>
  </div>
</div>

<!-- M4 -->
<div class="module-card" data-module="m4" data-roles="scientist,engineer" style="--mod-accent: linear-gradient(90deg,#ec4899,#a78bfa);">
  <div class="module-header">
    <div class="module-num-badge">M4</div>
    <div class="module-title-block">
      <h2>Core Supervised Learning — Regression & Classification</h2>
      <div class="module-meta">
        <span class="mod-badge">5 Weeks</span>
        <span class="mod-badge intermediate">Intermediate</span>
        <span class="mod-badge">Data Scientist · ML Eng.</span>
      </div>
    </div>
    <span class="module-chevron">▼</span>
  </div>
  <div class="module-progress-row">
    <div class="mod-prog-bar-wrap"><div class="mod-prog-bar"></div></div>
    <span class="mod-prog-text">0/5 weeks</span>
    <span class="mod-prog-pct">0%</span>
  </div>
  <div class="module-body">
    <div class="module-section-title">What You'll Learn</div>
    <ul class="learn-list">
      <li>Regression: Linear, Ridge (L2), Lasso (L1), Polynomial Regression</li>
      <li>Regression metrics: MAE, MSE, RMSE, R² — interpretation & selection</li>
      <li>Classification: Logistic Regression, Decision Trees, KNN, Naive Bayes</li>
      <li>Classification metrics: Accuracy, Precision, Recall, F1, ROC-AUC, Confusion Matrix</li>
      <li>Ensemble methods: Random Forest, Gradient Boosting, XGBoost</li>
      <li>Hyperparameter tuning: GridSearchCV, RandomizedSearchCV</li>
      <li>Model explainability: SHAP values, feature importance plots</li>
    </ul>
    <div class="module-section-title">Weekly Progress</div>
    <ul class="week-list">
      <li class="week-item" data-key="m4-w11"><div class="week-check-box"></div><div><span class="week-badge">W11</span><div class="week-label">Linear Regression, Ridge, Lasso, Polynomial Regression; MAE/RMSE/R²</div><div class="week-tasks">Predict house prices with LinearRegression → Ridge → compare R²</div></div></li>
      <li class="week-item" data-key="m4-w12"><div class="week-check-box"></div><div><span class="week-badge">W12</span><div class="week-label">Logistic Regression, Decision Trees, KNN, Naive Bayes; confusion matrix, ROC-AUC</div><div class="week-tasks">Titanic survival classifier — compare 4 algorithms, plot ROC curves</div></div></li>
      <li class="week-item" data-key="m4-w13"><div class="week-check-box"></div><div><span class="week-badge">W13</span><div class="week-label">Random Forest, Gradient Boosting, XGBoost; feature importance; ensemble intuition</div><div class="week-tasks">XGBoost on house prices vs LinearRegression — benchmark comparison</div></div></li>
      <li class="week-item" data-key="m4-w14"><div class="week-check-box"></div><div><span class="week-badge">W14</span><div class="week-label">GridSearchCV, RandomizedSearchCV, cross-validated tuning, overfitting/underfitting</div><div class="week-tasks">Tune XGBoost hyperparameters on heart disease dataset</div></div></li>
      <li class="week-item" data-key="m4-w15"><div class="week-check-box"></div><div><span class="week-badge">W15</span><div class="week-label">SHAP values, model explainability, Streamlit app deployment basics</div><div class="week-tasks">Add SHAP summary plot to heart disease classifier; publish Streamlit demo</div></div></li>
    </ul>
    <div class="milestone-box">
      <h4>🏆 M4 Milestone A — House Price Predictor (Deployed App)</h4>
      <p>Train, tune, and deploy a regression model predicting house prices. Build a Streamlit web app with form inputs → live prediction. Include model metrics and a SHAP feature importance chart. Intermediate · 5–6 days</p>
      <div class="milestone-tags"><span class="milestone-tag">Ridge/Lasso</span><span class="milestone-tag">XGBoost</span><span class="milestone-tag">GridSearchCV</span><span class="milestone-tag">Streamlit</span></div>
    </div>
    <div class="milestone-box">
      <h4>🏆 M4 Milestone B — Heart Disease Classifier with SHAP</h4>
      <p>Multi-algorithm classification comparison on the UCI Heart Disease dataset. Final model explained with SHAP force plots. Intermediate · 4–5 days</p>
      <div class="milestone-tags"><span class="milestone-tag">Random Forest</span><span class="milestone-tag">XGBoost</span><span class="milestone-tag">SHAP</span><span class="milestone-tag">ROC-AUC</span></div>
    </div>
    <div class="module-section-title">Free Resources</div>
    <div class="resource-grid">
      <a href="https://scikit-learn.org/stable/supervised_learning.html" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">Scikit-learn Supervised Learning</span><span class="resource-cat">Official docs & examples</span></span></a>
      <a href="https://www.kaggle.com/learn/intro-to-machine-learning" target="_blank" class="resource-link"><span class="resource-icon">🏅</span><span class="resource-info"><span class="resource-name">Kaggle — Intro to ML</span><span class="resource-cat">Free interactive course</span></span></a>
      <a href="https://www.kaggle.com/learn/intermediate-machine-learning" target="_blank" class="resource-link"><span class="resource-icon">🏅</span><span class="resource-info"><span class="resource-name">Kaggle — Intermediate ML</span><span class="resource-cat">XGBoost, pipelines, leakage</span></span></a>
      <a href="https://shap.readthedocs.io/" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">SHAP Documentation</span><span class="resource-cat">Model explainability</span></span></a>
      <a href="https://docs.streamlit.io/" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">Streamlit Docs</span><span class="resource-cat">ML web app framework</span></span></a>
      <a href="https://xgboost.readthedocs.io/en/stable/" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">XGBoost Docs</span><span class="resource-cat">Official guide & API ref</span></span></a>
    </div>
  </div>
</div>

<!-- M5 -->
<div class="module-card" data-module="m5" data-roles="scientist,engineer" style="--mod-accent: linear-gradient(90deg,#db2777,#ec4899);">
  <div class="module-header">
    <div class="module-num-badge">M5</div>
    <div class="module-title-block">
      <h2>Advanced ML & Unsupervised Learning</h2>
      <div class="module-meta">
        <span class="mod-badge">4 Weeks</span>
        <span class="mod-badge intermediate">Intermediate</span>
        <span class="mod-badge">Data Scientist · ML Eng.</span>
      </div>
    </div>
    <span class="module-chevron">▼</span>
  </div>
  <div class="module-progress-row">
    <div class="mod-prog-bar-wrap"><div class="mod-prog-bar"></div></div>
    <span class="mod-prog-text">0/4 weeks</span>
    <span class="mod-prog-pct">0%</span>
  </div>
  <div class="module-body">
    <div class="module-section-title">What You'll Learn</div>
    <ul class="learn-list">
      <li>Advanced classification: SVM (linear & kernel), multi-class strategies</li>
      <li>Unsupervised: K-Means clustering, DBSCAN, hierarchical clustering</li>
      <li>Dimensionality reduction: PCA, t-SNE, UMAP</li>
      <li>Anomaly detection: Isolation Forest, Local Outlier Factor</li>
      <li>Time-series forecasting: ARIMA, seasonal decomposition</li>
      <li>Model stacking & blending; Optuna hyperparameter optimisation</li>
      <li>ML Pipelines at scale with joblib, DVC for data versioning</li>
    </ul>
    <div class="module-section-title">Weekly Progress</div>
    <ul class="week-list">
      <li class="week-item" data-key="m5-w16"><div class="week-check-box"></div><div><span class="week-badge">W16</span><div class="week-label">SVM (linear & RBF kernel), multi-class classification, support vector intuition</div><div class="week-tasks">SVM vs XGBoost on the same dataset — when does SVM win?</div></div></li>
      <li class="week-item" data-key="m5-w17"><div class="week-check-box"></div><div><span class="week-badge">W17</span><div class="week-label">K-Means, DBSCAN, hierarchical clustering, elbow method, silhouette score</div><div class="week-tasks">Customer segmentation with K-Means on e-commerce dataset</div></div></li>
      <li class="week-item" data-key="m5-w18"><div class="week-check-box"></div><div><span class="week-badge">W18</span><div class="week-label">PCA, t-SNE, UMAP, anomaly detection (Isolation Forest), time-series basics</div><div class="week-tasks">Reduce MNIST to 2D with PCA vs t-SNE, visualise clusters</div></div></li>
      <li class="week-item" data-key="m5-w19"><div class="week-check-box"></div><div><span class="week-badge">W19</span><div class="week-label">Model stacking, blending, Optuna tuning, DVC for experiment tracking</div><div class="week-tasks">Build a churn prediction ensemble; track experiments with DVC</div></div></li>
    </ul>
    <div class="milestone-box">
      <h4>🏆 M5 Milestone — Customer Segmentation + Churn Prediction</h4>
      <p>Two-part project: (A) Segment customers using K-Means + PCA visualisation; (B) Predict churn with ensemble model (stacked RF + XGBoost). Deploy Streamlit dashboard combining both. Intermediate · 6–7 days</p>
      <div class="milestone-tags"><span class="milestone-tag">K-Means</span><span class="milestone-tag">PCA</span><span class="milestone-tag">Churn</span><span class="milestone-tag">Stacking</span><span class="milestone-tag">Streamlit</span></div>
    </div>
    <div class="module-section-title">Free Resources</div>
    <div class="resource-grid">
      <a href="https://scikit-learn.org/stable/modules/clustering.html" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">Scikit-learn Clustering Guide</span><span class="resource-cat">K-Means, DBSCAN, hierarchical</span></span></a>
      <a href="https://umap-learn.readthedocs.io/en/latest/" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">UMAP Documentation</span><span class="resource-cat">Dimensionality reduction</span></span></a>
      <a href="https://optuna.org/" target="_blank" class="resource-link"><span class="resource-icon">⚙️</span><span class="resource-info"><span class="resource-name">Optuna — Hyperparameter Opt.</span><span class="resource-cat">Automated tuning framework</span></span></a>
      <a href="https://dvc.org/doc" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">DVC Documentation</span><span class="resource-cat">Data versioning & pipelines</span></span></a>
      <a href="https://www.kaggle.com/learn/machine-learning-explainability" target="_blank" class="resource-link"><span class="resource-icon">🏅</span><span class="resource-info"><span class="resource-name">Kaggle ML Explainability</span><span class="resource-cat">SHAP, permutation importance</span></span></a>
    </div>
  </div>
</div>

<!-- M5.5 — Recommended Addition -->
<div class="module-card" data-module="m5-5" data-roles="scientist,engineer,aigenai" style="--mod-accent: linear-gradient(90deg,#f59e0b,#ec4899);">
  <div class="module-header">
    <div class="module-num-badge" style="font-size:0.7rem;">M5.5</div>
    <div class="module-title-block">
      <h2>Neural Networks & Deep Learning Bridge</h2>
      <div class="module-meta">
        <span class="mod-badge">2 Weeks</span>
        <span class="mod-badge intermediate">Intermediate</span>
        <span class="mod-badge added">✨ Recommended Add-on</span>
      </div>
    </div>
    <span class="module-chevron">▼</span>
  </div>
  <div class="module-progress-row">
    <div class="mod-prog-bar-wrap"><div class="mod-prog-bar"></div></div>
    <span class="mod-prog-text">0/2 weeks</span>
    <span class="mod-prog-pct">0%</span>
  </div>
  <div class="module-body">
    <p style="font-size:0.82rem;color:var(--light-text);background:rgba(245,158,11,0.07);border:1px solid rgba(245,158,11,0.25);border-radius:6px;padding:0.6rem 0.8rem;margin:0.75rem 0;">This bridge module fills the gap between classical ML (M5) and GenAI (M6). The doc jumps from XGBoost directly to LLMs — understanding neural networks, CNNs/RNNs, and the Transformer architecture is essential for Module 6.</p>
    <div class="module-section-title">What You'll Learn</div>
    <ul class="learn-list">
      <li>Perceptrons → Multi-layer Perceptrons (MLP): forward pass, weights, biases</li>
      <li>Activation functions: ReLU, Sigmoid, Softmax — intuition & when to use</li>
      <li>Backpropagation & gradient descent: how neural networks learn</li>
      <li>Convolutional Neural Networks (CNNs): filters, pooling, image classification</li>
      <li>Recurrent Neural Networks (RNNs) & LSTMs: sequential data intuition</li>
      <li>The Transformer architecture: attention mechanism, encoder-decoder</li>
      <li>Intro to PyTorch & Keras — define, compile, train a simple model</li>
      <li>Transfer learning with pre-trained models (ResNet, BERT overview)</li>
    </ul>
    <div class="module-section-title">Weekly Progress</div>
    <ul class="week-list">
      <li class="week-item" data-key="m55-w1"><div class="week-check-box"></div><div><span class="week-badge">W1</span><div class="week-label">MLP fundamentals, backpropagation, activation functions; build MLP from scratch with NumPy; then with Keras</div><div class="week-tasks">MNIST digit classifier with a 3-layer MLP; visualise loss curves</div></div></li>
      <li class="week-item" data-key="m55-w2"><div class="week-check-box"></div><div><span class="week-badge">W2</span><div class="week-label">CNNs, RNNs/LSTMs, Transformer attention mechanism; transfer learning overview with PyTorch</div><div class="week-tasks">CIFAR-10 image classifier with a small CNN; sentiment analysis with LSTM</div></div></li>
    </ul>
    <div class="milestone-box">
      <h4>🏆 M5.5 Milestone — MNIST/CIFAR Classifier + Sentiment Analyser</h4>
      <p>Build and compare: (A) MLP on MNIST — 97%+ accuracy; (B) CNN on CIFAR-10; (C) LSTM sentiment analysis on IMDB reviews. Notebook with loss/accuracy curves for each. Intermediate · 3–4 days</p>
      <div class="milestone-tags"><span class="milestone-tag">PyTorch</span><span class="milestone-tag">Keras</span><span class="milestone-tag">CNN</span><span class="milestone-tag">LSTM</span><span class="milestone-tag">Transfer Learning</span></div>
    </div>
    <div class="module-section-title">Free Resources</div>
    <div class="resource-grid">
      <a href="https://course.fast.ai/" target="_blank" class="resource-link"><span class="resource-icon">🎓</span><span class="resource-info"><span class="resource-name">fast.ai — Practical Deep Learning</span><span class="resource-cat">Top-down, free, highly rated</span></span></a>
      <a href="https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi" target="_blank" class="resource-link"><span class="resource-icon">▶️</span><span class="resource-info"><span class="resource-name">3Blue1Brown — Neural Networks</span><span class="resource-cat">Visual intuition series</span></span></a>
      <a href="https://pytorch.org/tutorials/" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">PyTorch Official Tutorials</span><span class="resource-cat">Beginner → advanced</span></span></a>
      <a href="https://keras.io/guides/" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">Keras Developer Guides</span><span class="resource-cat">High-level deep learning API</span></span></a>
      <a href="https://www.youtube.com/watch?v=ySEx_Bqxvvo" target="_blank" class="resource-link"><span class="resource-icon">▶️</span><span class="resource-info"><span class="resource-name">Attention is All You Need (Explained)</span><span class="resource-cat">Transformer architecture deep-dive</span></span></a>
      <a href="https://huggingface.co/learn/nlp-course/" target="_blank" class="resource-link"><span class="resource-icon">🎓</span><span class="resource-info"><span class="resource-name">HuggingFace NLP Course (Free)</span><span class="resource-cat">Transformers & fine-tuning</span></span></a>
    </div>
  </div>
</div>

<!-- M6 -->
<div class="module-card" data-module="m6" data-roles="aigenai" style="--mod-accent: linear-gradient(90deg,#9333ea,#ec4899);">
  <div class="module-header">
    <div class="module-num-badge">M6</div>
    <div class="module-title-block">
      <h2>Generative AI, LLMs, RAG & Agents</h2>
      <div class="module-meta">
        <span class="mod-badge">4 Weeks</span>
        <span class="mod-badge advanced">Advanced</span>
        <span class="mod-badge">AI / GenAI Engineer</span>
      </div>
    </div>
    <span class="module-chevron">▼</span>
  </div>
  <div class="module-progress-row">
    <div class="mod-prog-bar-wrap"><div class="mod-prog-bar"></div></div>
    <span class="mod-prog-text">0/4 weeks</span>
    <span class="mod-prog-pct">0%</span>
  </div>
  <div class="module-body">
    <div class="module-section-title">What You'll Learn</div>
    <ul class="learn-list">
      <li>LLM fundamentals: GPT, BERT, tokenisation, temperature, top-p sampling</li>
      <li>Prompt engineering: zero-shot, few-shot, chain-of-thought prompting</li>
      <li>HuggingFace Transformers: pipeline API, inference, sentiment, summarisation</li>
      <li>OpenAI API / open-source LLMs: Llama, Mistral via Ollama</li>
      <li>LangChain fundamentals: chains, prompts, memory, document loaders</li>
      <li>RAG (Retrieval-Augmented Generation): embeddings, vector stores, FAISS/Chroma</li>
      <li>AI Agents: tool use, ReAct framework, LangGraph basics</li>
      <li>Deploy RAG chatbot to HuggingFace Spaces</li>
    </ul>
    <div class="module-section-title">Weekly Progress</div>
    <ul class="week-list">
      <li class="week-item" data-key="m6-w21"><div class="week-check-box"></div><div><span class="week-badge">W21</span><div class="week-label">LLM fundamentals, tokenisation, prompt engineering (zero-shot, few-shot, CoT), HuggingFace pipeline API</div><div class="week-tasks">Build a prompt-engineering playground with 5 techniques compared</div></div></li>
      <li class="week-item" data-key="m6-w22"><div class="week-check-box"></div><div><span class="week-badge">W22</span><div class="week-label">OpenAI API / Ollama local LLMs, LangChain chains, prompt templates, memory</div><div class="week-tasks">Build a multi-turn chatbot with conversation memory using LangChain</div></div></li>
      <li class="week-item" data-key="m6-w23"><div class="week-check-box"></div><div><span class="week-badge">W23</span><div class="week-label">Embeddings, vector databases (FAISS, ChromaDB), document loaders, RAG pipeline end-to-end</div><div class="week-tasks">RAG system: ingest PDF → chunk → embed → retrieve → answer questions</div></div></li>
      <li class="week-item" data-key="m6-w24"><div class="week-check-box"></div><div><span class="week-badge">W24</span><div class="week-label">AI Agents: ReAct, tool calling, LangGraph, deploy to HuggingFace Spaces</div><div class="week-tasks">Build an agent that has web search, calculator, and Wikipedia tools</div></div></li>
    </ul>
    <div class="milestone-box">
      <h4>🏆 M6 Milestone — RAG Chatbot (Deployed on HuggingFace Spaces)</h4>
      <p>Build a domain-specific RAG chatbot: (1) Ingest your own PDF/text corpus, (2) Chunk & embed with HuggingFace sentence-transformers, (3) Store in ChromaDB, (4) Query with LangChain RAG chain, (5) Streamlit frontend, (6) Deploy to HuggingFace Spaces. Advanced · 5–7 days</p>
      <div class="milestone-tags"><span class="milestone-tag">LangChain</span><span class="milestone-tag">RAG</span><span class="milestone-tag">ChromaDB</span><span class="milestone-tag">HuggingFace</span><span class="milestone-tag">Streamlit</span></div>
    </div>
    <div class="module-section-title">Free Resources</div>
    <div class="resource-grid">
      <a href="https://www.deeplearning.ai/short-courses/" target="_blank" class="resource-link"><span class="resource-icon">🎓</span><span class="resource-info"><span class="resource-name">DeepLearning.AI Short Courses</span><span class="resource-cat">LangChain, RAG, Agents — free</span></span></a>
      <a href="https://huggingface.co/learn/nlp-course/" target="_blank" class="resource-link"><span class="resource-icon">🎓</span><span class="resource-info"><span class="resource-name">HuggingFace NLP Course</span><span class="resource-cat">Transformers & fine-tuning</span></span></a>
      <a href="https://python.langchain.com/docs/tutorials/" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">LangChain Tutorials</span><span class="resource-cat">Official getting-started guide</span></span></a>
      <a href="https://ollama.com/" target="_blank" class="resource-link"><span class="resource-icon">⚙️</span><span class="resource-info"><span class="resource-name">Ollama — Local LLMs</span><span class="resource-cat">Run Llama/Mistral locally, free</span></span></a>
      <a href="https://docs.trychroma.com/" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">ChromaDB Docs</span><span class="resource-cat">Open-source vector database</span></span></a>
      <a href="https://huggingface.co/spaces" target="_blank" class="resource-link"><span class="resource-icon">☁️</span><span class="resource-info"><span class="resource-name">HuggingFace Spaces</span><span class="resource-cat">Free ML app hosting</span></span></a>
    </div>
  </div>
</div>

<!-- M7 -->
<div class="module-card" data-module="m7" data-roles="scientist,engineer,aigenai" style="--mod-accent: linear-gradient(90deg,#a21caf,#ec4899);">
  <div class="module-header">
    <div class="module-num-badge">M7</div>
    <div class="module-title-block">
      <h2>Capstone Project — Full End-to-End AI System</h2>
      <div class="module-meta">
        <span class="mod-badge">2 Weeks</span>
        <span class="mod-badge advanced">Advanced</span>
        <span class="mod-badge">Most Important for Portfolio</span>
      </div>
    </div>
    <span class="module-chevron">▼</span>
  </div>
  <div class="module-progress-row">
    <div class="mod-prog-bar-wrap"><div class="mod-prog-bar"></div></div>
    <span class="mod-prog-text">0/2 weeks</span>
    <span class="mod-prog-pct">0%</span>
  </div>
  <div class="module-body">
    <div class="module-section-title">What You'll Build</div>
    <ul class="learn-list">
      <li>Define a real-world problem statement with business value</li>
      <li>Collect/curate a dataset (web scraping, APIs, or Kaggle)</li>
      <li>Full EDA + feature engineering pipeline</li>
      <li>Model selection and thorough evaluation</li>
      <li>Optional GenAI layer (RAG / agent on top of analytical results)</li>
      <li>Deployed app (Streamlit + FastAPI backend)</li>
      <li>Professional README, GitHub repo, and recorded demo</li>
    </ul>
    <div class="module-section-title">Weekly Progress</div>
    <ul class="week-list">
      <li class="week-item" data-key="m7-w25"><div class="week-check-box"></div><div><span class="week-badge">W25</span><div class="week-label">Problem definition, dataset collection, EDA, feature engineering, modelling — complete analysis notebook</div><div class="week-tasks">Define problem → gather data → EDA → model → evaluate → document findings</div></div></li>
      <li class="week-item" data-key="m7-w26"><div class="week-check-box"></div><div><span class="week-badge">W26</span><div class="week-label">Deploy full-stack app, write professional README, record 2-min demo, publish to GitHub</div><div class="week-tasks">FastAPI backend → Streamlit frontend → Docker → HuggingFace Spaces deploy</div></div></li>
    </ul>
    <div class="milestone-box">
      <h4>🏆 M7 Milestone — Capstone (Your Signature Portfolio Project)</h4>
      <p>This is your most important project. It demonstrates the full AI/ML stack to recruiters: data → model → deployment. Past examples: AI-powered job market analyser, disease risk predictor with RAG explainer, personalised recommendation system. Advanced · 10–14 days</p>
      <div class="milestone-tags"><span class="milestone-tag">Full Stack</span><span class="milestone-tag">FastAPI</span><span class="milestone-tag">Streamlit</span><span class="milestone-tag">GitHub</span><span class="milestone-tag">Portfolio</span></div>
    </div>
    <div class="module-section-title">Capstone Ideas by Role</div>
    <ul class="learn-list">
      <li><strong>Data Analyst:</strong> Interactive dashboard analysing a public dataset (crime, health, finance)</li>
      <li><strong>Data Scientist:</strong> End-to-end prediction system with SHAP explainability</li>
      <li><strong>ML Engineer:</strong> Deployed ML microservice with CI/CD and monitoring</li>
      <li><strong>AI/GenAI Engineer:</strong> Domain-specific RAG assistant with agent capabilities</li>
    </ul>
  </div>
</div>

<!-- M8 -->
<div class="module-card" data-module="m8" data-roles="engineer,aigenai" style="--mod-accent: linear-gradient(90deg,#7c3aed,#db2777);">
  <div class="module-header">
    <div class="module-num-badge">M8</div>
    <div class="module-title-block">
      <h2>MLOps — From Notebook to Production</h2>
      <div class="module-meta">
        <span class="mod-badge">4 Weeks</span>
        <span class="mod-badge advanced">Advanced</span>
        <span class="mod-badge bonus">⭐ Bonus Module</span>
        <span class="mod-badge">ML Eng. · AI Eng.</span>
      </div>
    </div>
    <span class="module-chevron">▼</span>
  </div>
  <div class="module-progress-row">
    <div class="mod-prog-bar-wrap"><div class="mod-prog-bar"></div></div>
    <span class="mod-prog-text">0/4 weeks</span>
    <span class="mod-prog-pct">0%</span>
  </div>
  <div class="module-body">
    <div class="module-section-title">What You'll Learn</div>
    <ul class="learn-list">
      <li>Model serialisation: joblib, pickle, ONNX — save & load models reliably</li>
      <li>FastAPI for ML: REST endpoints, Pydantic validation, async serving</li>
      <li>Streamlit advanced: multi-page apps, authentication, session state</li>
      <li>MLflow: experiment tracking, model registry, run comparison</li>
      <li>Docker: containerise FastAPI + Streamlit with Docker Compose</li>
      <li>CI/CD with GitHub Actions: automated testing, build, deploy on push</li>
      <li>Data drift detection: Evidently AI — monitors prediction distributions</li>
      <li>Cloud ML concepts: AWS SageMaker, GCP Vertex AI overview</li>
    </ul>
    <div class="module-section-title">Weekly Progress</div>
    <ul class="week-list">
      <li class="week-item" data-key="m8-w27"><div class="week-check-box"></div><div><span class="week-badge">W27</span><div class="week-label">FastAPI for ML: endpoints, Pydantic models, async, error handling; model serialisation with joblib</div><div class="week-tasks">Expose your best M4/M5 model as a FastAPI REST service with /predict endpoint</div></div></li>
      <li class="week-item" data-key="m8-w28"><div class="week-check-box"></div><div><span class="week-badge">W28</span><div class="week-label">MLflow tracking, experiment logging, Model Registry, comparing runs in MLflow UI</div><div class="week-tasks">Log all experiments for your M4/M5 project; register best model in MLflow</div></div></li>
      <li class="week-item" data-key="m8-w29"><div class="week-check-box"></div><div><span class="week-badge">W29</span><div class="week-label">Docker fundamentals, write Dockerfile for FastAPI app, Docker Compose for multi-service apps</div><div class="week-tasks">Containerise: FastAPI service + Streamlit frontend with Docker Compose; deploy to Render.com</div></div></li>
      <li class="week-item" data-key="m8-w30"><div class="week-check-box"></div><div><span class="week-badge">W30</span><div class="week-label">GitHub Actions CI/CD, automated model testing with pytest, Evidently AI for data drift detection</div><div class="week-tasks">Write GH Action: tests → build → deploy; generate Evidently drift report on train/test sets</div></div></li>
    </ul>
    <div class="milestone-box">
      <h4>🏆 M8 Milestone — Production-Ready ML Service</h4>
      <p>Productionise your best M4/M5 model: (1) FastAPI with input validation & error handling, (2) Streamlit frontend connected to the API, (3) Docker Compose for both services, (4) MLflow experiment tracking, (5) GitHub Actions CI/CD workflow, (6) Deploy to Render/HuggingFace Spaces, (7) Evidently AI monitoring report. Advanced · 4–5 days</p>
      <div class="milestone-tags"><span class="milestone-tag">FastAPI</span><span class="milestone-tag">Docker</span><span class="milestone-tag">MLflow</span><span class="milestone-tag">GitHub Actions</span><span class="milestone-tag">Evidently AI</span></div>
    </div>
    <div class="module-section-title">Free Resources</div>
    <div class="resource-grid">
      <a href="https://madewithml.com/" target="_blank" class="resource-link"><span class="resource-icon">🎓</span><span class="resource-info"><span class="resource-name">Made With ML — MLOps Course</span><span class="resource-cat">Best free MLOps curriculum</span></span></a>
      <a href="https://www.youtube.com/watch?v=0sOvCWFmrtA" target="_blank" class="resource-link"><span class="resource-icon">▶️</span><span class="resource-info"><span class="resource-name">FastAPI Full Tutorial</span><span class="resource-cat">Sebastián Ramírez — YouTube</span></span></a>
      <a href="https://mlflow.org/docs/latest/index.html" target="_blank" class="resource-link"><span class="resource-icon">📖</span><span class="resource-info"><span class="resource-name">MLflow Documentation</span><span class="resource-cat">Experiment tracking — official</span></span></a>
      <a href="https://www.evidentlyai.com/" target="_blank" class="resource-link"><span class="resource-icon">⚙️</span><span class="resource-info"><span class="resource-name">Evidently AI</span><span class="resource-cat">Open-source model monitoring</span></span></a>
      <a href="https://www.youtube.com/watch?v=i7MI9-6qQcs" target="_blank" class="resource-link"><span class="resource-icon">▶️</span><span class="resource-info"><span class="resource-name">Docker for ML Engineers</span><span class="resource-cat">Abhishek Thakur — YouTube</span></span></a>
      <a href="https://render.com/" target="_blank" class="resource-link"><span class="resource-icon">☁️</span><span class="resource-info"><span class="resource-name">Render.com — Free Hosting</span><span class="resource-cat">Deploy Docker apps free tier</span></span></a>
    </div>
  </div>
</div>

</div><!-- end .modules-list -->

<!-- Timeline Section -->
<p class="aiml-section-title">📅 30-Week Master Timeline</p>
<div class="timeline-section">
  <div class="timeline-table-wrap">
    <table class="timeline-table">
      <thead>
        <tr>
          <th>Weeks</th>
          <th>Module</th>
          <th>Milestone Project</th>
          <th>Career Unlock</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>1–3</td><td><span class="timeline-module-badge">M1: Python Fundamentals</span></td><td>Grade Management CLI</td><td>—</td></tr>
        <tr><td>4–6</td><td><span class="timeline-module-badge">M2: NumPy & Pandas</span></td><td>COVID-19 Analysis</td><td class="timeline-unlock">Data Analyst Intern</td></tr>
        <tr><td>7–10</td><td><span class="timeline-module-badge">M3: Stats, EDA, ML Workflow</span></td><td>EDA Report + Pipeline</td><td class="timeline-unlock">Data Analyst</td></tr>
        <tr><td>11–15</td><td><span class="timeline-module-badge">M4: Supervised Learning</span></td><td>House Price + Heart Disease</td><td class="timeline-unlock">Junior Data Scientist</td></tr>
        <tr><td>16–19</td><td><span class="timeline-module-badge">M5: Advanced ML + Unsupervised</span></td><td>Customer Segmentation + Churn</td><td class="timeline-unlock">Data Scientist / ML Eng.</td></tr>
        <tr><td>20–21</td><td><span class="timeline-module-badge">M5.5: Neural Networks Bridge ✨</span></td><td>MNIST/CIFAR + Sentiment LSTM</td><td class="timeline-unlock">Mid-Level DS/MLE</td></tr>
        <tr><td>21–24</td><td><span class="timeline-module-badge">M6: GenAI, LLMs, RAG, Agents</span></td><td>RAG Chatbot — deployed</td><td class="timeline-unlock">AI / GenAI Engineer</td></tr>
        <tr><td>25–26</td><td><span class="timeline-module-badge">M7: Capstone Project</span></td><td>Full End-to-End AI System</td><td class="timeline-unlock">Mid-Level — All Roles</td></tr>
        <tr><td>27–30</td><td><span class="timeline-module-badge">M8: MLOps (Bonus)</span></td><td>Production ML Service + CI/CD</td><td class="timeline-unlock">ML Eng. / Senior</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Portfolio Checklist -->
<p class="aiml-section-title">🗂️ Portfolio Checklist</p>
<p style="font-size:0.85rem;color:var(--light-text);margin-bottom:1rem;">Check off each project as you build & publish it. Your GitHub profile IS your resume — recruiters look at pinned repos before your CV.</p>
<div class="checklist-grid">
  <label class="check-item" data-key="portfolio-m1"><input type="checkbox"><div class="check-box"></div><div class="check-label-wrap"><span class="check-label">Python CLI Grade Management System</span><span class="check-sub">Module 1 • All roles — shows Python basics</span></div></label>
  <label class="check-item" data-key="portfolio-m2"><input type="checkbox"><div class="check-box"></div><div class="check-label-wrap"><span class="check-label">COVID-19 Pandas Analysis Notebook</span><span class="check-sub">Module 2 • Data Analyst, Data Scientist</span></div></label>
  <label class="check-item" data-key="portfolio-m3"><input type="checkbox"><div class="check-box"></div><div class="check-label-wrap"><span class="check-label">EDA Report with 8+ Visualisations</span><span class="check-sub">Module 3 • Data Analyst, Data Scientist</span></div></label>
  <label class="check-item" data-key="portfolio-m4a"><input type="checkbox"><div class="check-box"></div><div class="check-label-wrap"><span class="check-label">House Price Predictor — Deployed App</span><span class="check-sub">Module 4 • All ML roles</span></div></label>
  <label class="check-item" data-key="portfolio-m4b"><input type="checkbox"><div class="check-box"></div><div class="check-label-wrap"><span class="check-label">Heart Disease Classifier with SHAP</span><span class="check-sub">Module 4 • Data Scientist, ML Engineer</span></div></label>
  <label class="check-item" data-key="portfolio-m5"><input type="checkbox"><div class="check-box"></div><div class="check-label-wrap"><span class="check-label">Customer Segmentation + Churn Prediction</span><span class="check-sub">Module 5 • Data Scientist, ML Engineer</span></div></label>
  <label class="check-item" data-key="portfolio-m55"><input type="checkbox"><div class="check-box"></div><div class="check-label-wrap"><span class="check-label">Neural Net Classifier (MNIST/CIFAR + LSTM)</span><span class="check-sub">Module 5.5 ✨ • Data Scientist, ML Eng., AI Eng.</span></div></label>
  <label class="check-item" data-key="portfolio-m6"><input type="checkbox"><div class="check-box"></div><div class="check-label-wrap"><span class="check-label">RAG Chatbot — Deployed on HuggingFace</span><span class="check-sub">Module 6 • AI / GenAI Engineer</span></div></label>
  <label class="check-item" data-key="portfolio-m7"><input type="checkbox"><div class="check-box"></div><div class="check-label-wrap"><span class="check-label">Capstone Full End-to-End Project</span><span class="check-sub">Module 7 • All roles — most important</span></div></label>
  <label class="check-item" data-key="portfolio-m8"><input type="checkbox"><div class="check-box"></div><div class="check-label-wrap"><span class="check-label">Production ML Service with Docker + CI/CD</span><span class="check-sub">Module 8 • ML Engineer, AI Engineer</span></div></label>
</div>

<!-- Job Readiness -->
<p class="aiml-section-title">✅ Job-Readiness Checklist</p>
<div class="readiness-grid">
  <div class="readiness-card">
    <h4>🐍 Technical Skills</h4>
    <ul>
      <li>Python ✓, Pandas/NumPy ✓, Scikit-learn ✓</li>
      <li>XGBoost ✓, PyTorch/Keras ✓ (for ML Engineer+)</li>
      <li>LangChain ✓, HuggingFace ✓ (for AI/GenAI Eng.)</li>
      <li>FastAPI + Docker (for ML Engineer+)</li>
    </ul>
  </div>
  <div class="readiness-card">
    <h4>📁 GitHub Portfolio</h4>
    <ul>
      <li>5+ public projects with good READMEs</li>
      <li>Deployed links for all major projects</li>
      <li>Profile README with bio + contact + links</li>
      <li>Consistent naming: project-name-ml</li>
    </ul>
  </div>
  <div class="readiness-card">
    <h4>�� Kaggle Profile</h4>
    <ul>
      <li>Contributor status (submit to competitions)</li>
      <li>At least 2 public notebooks published</li>
      <li>Titanic + House Prices entry competitions</li>
      <li>Top 30% in at least one competition</li>
    </ul>
  </div>
  <div class="readiness-card">
    <h4>🌐 Online Presence</h4>
    <ul>
      <li>LinkedIn updated: skills, GitHub link, ML headline</li>
      <li>Resume: 1-page, quantified achievements</li>
      <li>Free certs: Kaggle ML, DeepLearning.AI, Google ML</li>
      <li>Interview prep: 50 Python LeetCode + ML flashcards</li>
    </ul>
  </div>
</div>

<!-- Essential Communities -->
<p class="aiml-section-title">🌍 Essential Platforms & Communities</p>
<div class="resource-grid" style="margin-bottom:3rem;">
  <a href="https://www.kaggle.com/" target="_blank" class="resource-link"><span class="resource-icon">🏅</span><span class="resource-info"><span class="resource-name">Kaggle</span><span class="resource-cat">Datasets, competitions, learning</span></span></a>
  <a href="https://huggingface.co/" target="_blank" class="resource-link"><span class="resource-icon">🤗</span><span class="resource-info"><span class="resource-name">HuggingFace</span><span class="resource-cat">Models, datasets, Spaces</span></span></a>
  <a href="https://colab.research.google.com/" target="_blank" class="resource-link"><span class="resource-icon">☁️</span><span class="resource-info"><span class="resource-name">Google Colab</span><span class="resource-cat">Free GPU Jupyter notebooks</span></span></a>
  <a href="https://www.deeplearning.ai/short-courses/" target="_blank" class="resource-link"><span class="resource-icon">🎓</span><span class="resource-info"><span class="resource-name">DeepLearning.AI Short Courses</span><span class="resource-cat">Free GenAI specialisations</span></span></a>
  <a href="https://developers.google.com/machine-learning/crash-course" target="_blank" class="resource-link"><span class="resource-icon">🎓</span><span class="resource-info"><span class="resource-name">Google ML Crash Course</span><span class="resource-cat">Core ML concepts, free</span></span></a>
  <a href="https://course.fast.ai/" target="_blank" class="resource-link"><span class="resource-icon">🎓</span><span class="resource-info"><span class="resource-name">fast.ai — Practical Deep Learning</span><span class="resource-cat">Top-down deep learning, free</span></span></a>
  <a href="https://paperswithcode.com/" target="_blank" class="resource-link"><span class="resource-icon">📄</span><span class="resource-info"><span class="resource-name">Papers With Code</span><span class="resource-cat">Latest ML research + code</span></span></a>
  <a href="https://towardsdatascience.com/" target="_blank" class="resource-link"><span class="resource-icon">✍️</span><span class="resource-info"><span class="resource-name">Towards Data Science</span><span class="resource-cat">Applied ML articles (Medium)</span></span></a>
</div>

<!-- Footer note -->
<div style="background:linear-gradient(135deg,rgba(167,139,250,0.08),rgba(236,72,153,0.08));border:1px solid rgba(167,139,250,0.25);border-radius:12px;padding:1.5rem;text-align:center;margin-bottom:2rem;">
  <p style="font-size:1rem;font-weight:700;color:var(--text-color);margin:0 0 0.5rem;">�� Consistency beats intensity.</p>
  <p style="font-size:0.88rem;color:var(--light-text);margin:0 0 1rem;">1–2 hours every day beats 10 hours on weekends. Build in public — post your projects and learnings on LinkedIn. <strong>Your first job will come from a project someone saw, not a certificate on your wall.</strong></p>
  <a href="{{ '/roadmap/' | relative_url }}" style="display:inline-block;padding:0.6rem 1.4rem;background:var(--aiml-grad);color:#fff;border-radius:8px;text-decoration:none;font-size:0.9rem;font-weight:700;">← Back to All Roadmaps</a>
</div>
