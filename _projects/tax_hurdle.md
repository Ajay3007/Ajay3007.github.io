---
layout: project
title: Tax Hurdle - Investment Tax Calculation System
description: "Java-based investment tax calculator for Indian equity traders. Automates STCG calculation with quarter-wise breakdown, Excel integration, and comprehensive logging."
permalink: /projects/tax_hurdle/
---

<!-- Hero Section -->
<section class="hero-section" style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.05), rgba(118, 75, 162, 0.05)); border: 1px solid rgba(102, 126, 234, 0.1);">
    <h1 class="hero-title">Tax Hurdle 💼</h1>
    <p class="hero-subtitle">
        Java-based investment tax calculator automating <strong>Short-Term Capital Gains (STCG)</strong> and quarter-wise breakdowns for equity traders.
    </p>
    <div class="hero-actions">
        <a href="https://github.com/Ajay3007/tax_hurdle" target="_blank" rel="noopener noreferrer" class="btn-primary" style="background: linear-gradient(135deg, #667eea, #764ba2); box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);">
            📦 View on GitHub
        </a>
        <a href="{{ '/learning/finance/' | relative_url }}" class="btn-secondary">
            📚 Full Documentation
        </a>
    </div>
</section>

<!-- The Challenge -->
<section class="modern-section" style="max-width: 800px; margin: 0 auto 4.5rem auto;">
    <h2 class="section-title">🎯 The Challenge</h2>
    <p style="font-size: 1.1rem; color: var(--text-color); line-height: 1.8; margin-bottom: 2rem;">
        Indian equity traders must calculate STCG accurately across thousands of unorganized transactions to file localized ITRs. Manual spreadsheet manipulation leads to calculation drift, missed P&L structures, and hundreds of misspent hours categorizing intraday speculations vs actual holdings. <strong>Tax Hurdle automates the entire analytical workflow.</strong>
    </p>
</section>

<!-- Core Features Grid -->
<section class="modern-section">
    <h2 class="section-title">✨ Key Features</h2>
    <div class="nav-grid">
        <div class="nav-card" style="border-left-color: #f59e0b;">
            <div class="nav-card-title">📊 Quarter STCG Arrays</div>
            <div class="nav-card-desc">Automatically segregates capital gains bounding them by Indian financial quarters (Q1-Q5) seamlessly for advance tax planning.</div>
        </div>
        <div class="nav-card" style="border-left-color: #3b82f6;">
            <div class="nav-card-title">🔄 Trade Classification</div>
            <div class="nav-card-desc">Separates STCG (holdings >24hrs) natively from raw intraday speculation metrics, maintaining accurate tax compartmentalization.</div>
        </div>
        <div class="nav-card" style="border-left-color: #10b981;">
            <div class="nav-card-title">📑 Excel Integration</div>
            <div class="nav-card-desc">Utilizes Apache POI to parse buy/sell pipelines directly from `.xlsx` files without requiring manual data-entry conversions.</div>
        </div>
        <div class="nav-card" style="border-left-color: #9945ff;">
            <div class="nav-card-title">🔒 Thread-Safe Processing</div>
            <div class="nav-card-desc">Incorporates nested `ConcurrentHashMap` arrays for massive-scale parallel thread calculation safety and log auditing stability.</div>
        </div>
    </div>
</section>

<!-- Architecture / Tech Stack Breakdown -->
<section class="modern-section">
    <h2 class="section-title">🏗️ Architecture & Stack</h2>
    <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
        <!-- Architecture List -->
        <div class="featured-project-card" style="flex: 1; min-width: 300px; border-top-color: #667eea;">
            <div class="featured-project-title">Design Patterns</div>
            <ul style="margin: 0; padding-left: 1.2rem; color: var(--text-color); line-height: 1.8;">
                <li><code>Singleton Pattern</code> — Regulating singular application thread states.</li>
                <li><code>Factory Pattern</code> — Offshoring localized security object creation.</li>
                <li><code>Queue Mechanism</code> — Enforcing strict FIFO trade processing.</li>
                <li><code>Strategy Pattern</code> — Injecting dynamic tax calculation math algorithms.</li>
            </ul>
        </div>
        
        <!-- Tech Stack Highlight -->
        <div class="featured-project-card" style="flex: 1; min-width: 300px; border-top-color: #764ba2; background: #f8fafc;">
            <div class="featured-project-title">Primary Backend Stack</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">Core Pipeline</span><strong style="color: #1a1f36;">Java 8+</strong></div>
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">Excel Interface</span><strong style="color: #1a1f36;">Apache POI 4.x</strong></div>
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">Trace Logging</span><strong style="color: #1a1f36;">Apache Log4j2</strong></div>
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">Thread Integrity</span><strong style="color: #1a1f36;">ConcurrentHashMap</strong></div>
            </div>
        </div>
    </div>
</section>

<!-- Documentation Suite -->
<section class="modern-section">
    <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 2rem;">
        <h2 class="section-title" style="margin-bottom: 0;">📚 Documentation Suite</h2>
        <a href="{{ '/learning/finance/' | relative_url }}" class="btn-secondary" style="padding: 0.5rem 1rem; font-size: 0.9rem; margin-bottom: 8px;">Explore Wiki →</a>
    </div>
    <div class="project-grid">
        <div class="featured-project-card" style="border-top-color: #2196F3;">
            <div class="featured-project-title"><a href="{{ '/learning/finance/tax_hurdle/summary/' | relative_url }}" style="text-decoration: none; color: inherit;">📋 Project Summary</a></div>
            <div class="featured-project-desc">Executive overview outlining calculation constraints, system metrics, phase statuses, and software development roadmap.</div>
        </div>

        <div class="featured-project-card" style="border-top-color: #FF9800;">
            <div class="featured-project-title"><a href="{{ '/learning/finance/tax_hurdle/technical-analysis/' | relative_url }}" style="text-decoration: none; color: inherit;">🏗️ Technical Analysis</a></div>
            <div class="featured-project-desc">Hyper-focused deep dive into internal software architecture, logic gates, design patterns, and systemic code quality benchmarks.</div>
        </div>

        <div class="featured-project-card" style="border-top-color: #9C27B0;">
            <div class="featured-project-title"><a href="{{ '/learning/finance/tax_hurdle/refactoring-guide/' | relative_url }}" style="text-decoration: none; color: inherit;">🔧 Refactoring Trajectory</a></div>
            <div class="featured-project-desc">Prioritized optimization roadmap yielding multi-threading improvements alongside heavily abstracted logic simplifications.</div>
        </div>
    </div>
</section>

<!-- Output Snippet -->
<section class="modern-section">
    <h2 class="section-title">🚀 Core Processor Log Example</h2>
    <div style="background: linear-gradient(135deg, #1e293b, #0f172a); padding: 2rem; border-radius: 12px; border-left: 4px solid #667eea; box-shadow: 0 10px 25px rgba(0,0,0,0.15);">
<pre style="margin: 0; background: transparent; padding: 0; border: none; box-shadow: none;"><code style="color: #e2e8f0; font-family: 'Fira Code', 'Courier New', monospace; font-size: 0.95rem;">[INFO] Initialization parameters mapped. Opening [Excel I/O stream].
[WARN] 14 missing STCG markers found. Commencing fallback matching algorithm.
[SUCCESS] Parsed 2401 transactional artifacts.

STCG Summary Data-Stream (FY 2021-22):
├─ Q1 (Apr-Jun):  ₹45,000
├─ Q2 (Jun-Sep):  ₹67,500
├─ Q3 (Sep-Dec):  ₹32,100
├─ Q4 (Dec-Mar):  ₹58,900
└─ Q5 (Mar-end):  ₹12,500

[Finalizer] Total Calculated Term Yield == ₹2,16,000
[Finalizer] Estimated Intra-Day Liquidity == ₹8,50,000</code></pre>
    </div>
</section>

<div style="text-align: center; margin: 4rem 0 2rem 0; border-top: 1px solid var(--border-color); padding-top: 3rem;">
  <a href="{{ '/projects/' | relative_url }}" class="btn-secondary">
    <span style="margin-right: 0.5rem;">🎒</span> Back to Projects
  </a>
</div>
