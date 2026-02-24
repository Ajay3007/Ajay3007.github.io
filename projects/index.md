---
layout: default
title: Projects
---

<!-- Hero Section -->
<section class="hero-section" style="margin-top: 1rem; padding: 3rem 1rem;">
    <h1 class="hero-title" style="font-size: 2.8rem;">Projects & Case Studies 🚀</h1>
    <p class="hero-subtitle" style="margin-bottom: 1rem;">
        A showcase of my applications, architecture designs, and high-performance infrastructure builds.
    </p>
</section>

<!-- Dynamic Project Grid -->
<section class="modern-section" style="margin-bottom: 3rem;">
    <div class="project-grid">
        {% for project in site.projects %}
        <div class="featured-project-card" style="border-top-color: {% cycle '#667eea', '#00d4ff', '#9C27B0', '#4CAF50', '#f59e0b' %};">
            <div class="featured-project-title">
                <a href="{{ project.url | relative_url }}" style="text-decoration: none; color: inherit;">
                    {% if project.title contains "Tax" %}💼{% elsif project.title contains "Dev" %}🛠️{% elsif project.title contains "work" %}🤖{% else %}💻{% endif %} 
                    {{ project.title }}
                </a>
            </div>
            {% if project.description %}
            <div class="featured-project-desc" style="font-size: 1.05rem;">{{ project.description }}</div>
            {% endif %}
            <div style="margin-top: 1rem;">
                <a href="{{ project.url | relative_url }}" class="featured-project-link">Read Case Study →</a>
            </div>
        </div>
        {% endfor %}
    </div>
</section>

<!-- Cross-Linking -->
<div style="text-align: center; margin: 4rem 0 2rem 0; border-top: 1px solid var(--border-color); padding-top: 3rem; display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
  <a href="{{ '/' | relative_url }}" class="btn-secondary">
    <span style="margin-right: 0.5rem;">🏠</span> Back to Home
  </a>
  <a href="{{ '/learning/' | relative_url }}" class="btn-secondary">
    <span style="margin-right: 0.5rem;">📚</span> View Learning Portal
  </a>
</div>
