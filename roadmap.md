---
layout: default
title: Learning Roadmaps
permalink: /roadmap/
custom_css: roadmap-hub
---

<!-- Hero -->
<div class="hub-hero">
  <h1>🗺️ Learning Roadmaps</h1>
  <p>Structured, chapter-by-chapter mastery paths across core engineering domains — from interview prep to systems-level design.</p>
  <div class="hub-hero-meta">
    <div class="hub-meta-item">
      <span class="hub-meta-val">{{ site.data.roadmaps.list | where: "status", "live" | size }}</span>
      <span class="hub-meta-lbl">Live Roadmaps</span>
    </div>
    <div class="hub-meta-item">
      <span class="hub-meta-val">{{ site.data.roadmaps.list | where: "status", "soon" | size }}</span>
      <span class="hub-meta-lbl">In Progress</span>
    </div>
    <div class="hub-meta-item">
      <span class="hub-meta-val">{{ site.data.roadmaps.curated_problems }}</span>
      <span class="hub-meta-lbl">Curated Problems</span>
    </div>
    <div class="hub-meta-item">
      <span class="hub-meta-val">{{ site.data.roadmaps.primary_language }}</span>
      <span class="hub-meta-lbl">Primary Language</span>
    </div>
  </div>
</div>

<!-- How It Works -->
<div class="how-strip">
  <div class="how-item">
    <div class="how-num">1</div>
    <div class="how-text">
      <strong>Pick a domain</strong>
      <span>Choose the roadmap that matches your current goal.</span>
    </div>
  </div>
  <div class="how-item">
    <div class="how-num">2</div>
    <div class="how-text">
      <strong>Follow chapters</strong>
      <span>Each chapter builds on the last — theory + patterns + problems.</span>
    </div>
  </div>
  <div class="how-item">
    <div class="how-num">3</div>
    <div class="how-text">
      <strong>Track your progress</strong>
      <span>Mark problems solved in the Problems Hub — progress saves in your browser.</span>
    </div>
  </div>
</div>

<!-- Domain Grid (data-driven from _data/roadmaps.yml) -->
<h2 class="section-title">Choose Your Domain</h2>
<div class="domain-grid">
  {% for rm in site.data.roadmaps.list %}
  <div class="domain-card{% if rm.status == 'soon' %} coming-soon{% endif %}" style="--card-accent: {{ rm.accent }};">
    <div class="dc-icon">{{ rm.icon }}</div>
    <div class="dc-header">
      <div class="dc-title">{{ rm.title }}</div>
      {% if rm.status == 'live' %}<span class="dc-badge live">✅ Live</span>{% else %}<span class="dc-badge soon">🔜 Soon</span>{% endif %}
    </div>
    <div class="dc-desc">{{ rm.desc }}</div>
    <div class="dc-tags">
      {% for tag in rm.tags %}<span class="dc-tag">{{ tag }}</span>{% endfor %}
    </div>
    <div class="dc-progress">
      {% assign filled = 0 %}{% if rm.status == 'live' %}{% assign filled = 5 %}{% endif %}
      {% for i in (1..5) %}<span class="dc-dot{% if forloop.index <= filled %} filled{% endif %}"></span>{% endfor %}
      <span style="margin-left:0.25rem;">{{ rm.meta }}</span>
    </div>
    <div class="dc-cta"{% if rm.ctas.size > 1 %} style="display:flex;flex-wrap:wrap;gap:.6rem;"{% endif %}>
      {% if rm.ctas.size > 0 %}{% for cta in rm.ctas %}<a href="{{ cta.url | relative_url }}" class="dc-btn"{% if cta.style %} style="{{ cta.style }}"{% endif %}>{{ cta.label }}</a>{% endfor %}{% else %}<span class="dc-btn-soon">🔒 Coming Soon</span>{% endif %}
    </div>
  </div>
  {% endfor %}
</div>

<!-- Foot nav -->
<div style="display:flex;gap:1rem;justify-content:center;margin:3rem 0 1rem 0;flex-wrap:wrap;">
  <a href="{{ '/problems/' | relative_url }}" class="btn-primary" style="background:linear-gradient(135deg,#00d4ff,#3b82f6);">🎯 Practice Problems Hub</a>
  <a href="{{ '/learning/dsa/dsa-roadmap/' | relative_url }}" class="btn-secondary">📖 Jump to DSA Roadmap →</a>
</div>
