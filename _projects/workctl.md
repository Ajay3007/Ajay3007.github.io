---
layout: project
title: "workctl - AI-Enhanced Workspace Manager"
description: "A Java/JavaFX productivity tool featuring Kanban boards, strict Markdown tracking, and an integrated Claude AI agent. Filesystem as Database."
permalink: /projects/workctl/
tags: [Java, JavaFX, Claude AI, Markdown, CLI]
---

<!-- Hero Section -->
<section class="hero-section" style="background: linear-gradient(135deg, rgba(33, 150, 243, 0.05), rgba(156, 39, 176, 0.05)); border: 1px solid rgba(33, 150, 243, 0.1);">
    <h1 class="hero-title">workctl 🛠️</h1>
    <p class="hero-subtitle">
        A powerful <strong>Project Workspace Manager</strong> engineered with a hybrid CLI/GUI interface, Markdown tracking engine, and built-in Anthropic Claude AI Agent. Zero external DB dependency.
    </p>
    <div class="hero-actions">
        <a href="https://github.com/Ajay3007/workctl/releases/tag/v1.1.0" target="_blank" rel="noopener noreferrer" class="btn-primary" style="background: linear-gradient(135deg, #2196F3, #9C27B0); box-shadow: 0 4px 15px rgba(33, 150, 243, 0.3);">
            ⬇️ Download v1.1.0
        </a>
        <a href="https://github.com/Ajay3007/workctl" target="_blank" rel="noopener noreferrer" class="btn-secondary">
            📦 View on GitHub
        </a>
    </div>
</section>

<!-- Overview / Philosophy -->
<section class="modern-section" style="max-width: 800px; margin: 0 auto 4.5rem auto;">
    <h2 class="section-title">🎯 Design Philosophy</h2>
    <p style="font-size: 1.1rem; color: var(--text-color); line-height: 1.8; margin-bottom: 2rem;">
        <strong>workctl</strong> was built to solve the fragmentation of task tracking across dozens of browser tabs. It operates on a simple principle: <strong>Filesystem as Database</strong>. 
        Your tasks are stored natively as cleanly formatted Markdown files (`tasks.md`). This means your data is perfectly human-readable, highly versionable via Git, and strictly portable. No hidden database migrations, ever.
    </p>
</section>

<!-- Core Features Grid -->
<section class="modern-section">
    <h2 class="section-title">✨ Key Features</h2>
    <div class="nav-grid">
        <div class="nav-card" style="border-left-color: #2196F3;">
            <div class="nav-card-title">📊 Kanban Board Engine</div>
            <div class="nav-card-desc">Interactive JavaFX GUI with drag-and-drop columns (Open, In Progress, Done). Priority-driven automated sorting and live subtask progress tracking.</div>
        </div>
        <div class="nav-card" style="border-left-color: #9C27B0;">
            <div class="nav-card-title">🤖 Claude AI Agent</div>
            <div class="nav-card-desc">Togglable "Write Mode" AI agent. Decompose massive goals into segmented subtasks automatically, or ask the agent to query structural insights via the API loop.</div>
        </div>
        <div class="nav-card" style="border-left-color: #4CAF50;">
            <div class="nav-card-title">📝 Markdown Persistence</div>
            <div class="nav-card-desc">Every element is driven by CommonMark. The GUI features a live Markdown preview pane for parsing task descriptions directly to formatted text.</div>
        </div>
        <div class="nav-card" style="border-left-color: #FF9800;">
            <div class="nav-card-title">⚙️ CLI-First Automation</div>
            <div class="nav-card-desc">Fully functional via terminal using Picocli. Add `workctl` to your PATH to manage workspaces effortlessly without ever leaving your IDE context.</div>
        </div>
    </div>
</section>

<!-- Architecture / Tech Stack Breakdown -->
<section class="modern-section">
    <h2 class="section-title">🏗️ Architecture & Stack</h2>
    <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
        <!-- Architecture List -->
        <div class="featured-project-card" style="flex: 1; min-width: 300px; border-top-color: #2196F3;">
            <div class="featured-project-title">Multi-Module Monorepo</div>
            <ul style="margin: 0; padding-left: 1.2rem; color: var(--text-color); line-height: 1.8;">
                <li><code>core/</code> — Base parsing engine, Subtask models, Logs, and Configs.</li>
                <li><code>cli/</code> — Command-line interface binding to `core`.</li>
                <li><code>gui/</code> — JavaFX visual presentation layer.</li>
                <li><code>agent/</code> — AI API interaction and logical context builder.</li>
            </ul>
        </div>
        
        <!-- Tech Stack Highlight -->
        <div class="featured-project-card" style="flex: 1; min-width: 300px; border-top-color: #9C27B0; background: #f8fafc;">
            <div class="featured-project-title">Primary Tech Stack</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">Language</span><strong style="color: #1a1f36;">Java 17+</strong></div>
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">Build System</span><strong style="color: #1a1f36;">Gradle</strong></div>
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">GUI Framework</span><strong style="color: #1a1f36;">JavaFX 21</strong></div>
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">CLI Framework</span><strong style="color: #1a1f36;">Picocli</strong></div>
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">Parser</span><strong style="color: #1a1f36;">CommonMark</strong></div>
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">LLM Integration</span><strong style="color: #1a1f36;">Claude API</strong></div>
            </div>
        </div>
    </div>
</section>

<!-- Quick Start Section -->
<section class="modern-section">
    <h2 class="section-title">🚀 Quick Start (CLI)</h2>
    <div style="background: linear-gradient(135deg, #1e293b, #0f172a); padding: 2rem; border-radius: 12px; border-left: 4px solid #38bdf8; box-shadow: 0 10px 25px rgba(0,0,0,0.15);">
<pre style="margin: 0; background: transparent; padding: 0; border: none; box-shadow: none;"><code style="color: #e2e8f0; font-family: 'Fira Code', 'Courier New', monospace; font-size: 0.95rem;">> workctl init .
[INFO] Setup complete! Core structures instantiated.

> workctl add-task -t "Prepare System Design Board" -p 1 -c "Open"
[SUCCESS] Added mapping #1: Prepare System Design Board [P1]

> workctl mark #1
[INFO] Validating workflow bounds...
[SUCCESS] Moved task #1 -> Done. Timestamp appended.

> workctl gui
[INFO] Booting visual layout presentation layer...</code></pre>
    </div>
</section>

<div style="text-align: center; margin: 4rem 0 2rem 0; border-top: 1px solid var(--border-color); padding-top: 3rem;">
  <a href="{{ '/projects/' | relative_url }}" class="btn-secondary">
    <span style="margin-right: 0.5rem;">🎒</span> Back to Projects
  </a>
</div>
