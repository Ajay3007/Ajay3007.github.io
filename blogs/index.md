---
layout: default
title: Blogs
permalink: /blogs/
---

<!-- Hero Section -->
<section class="hero-section" style="margin-top: 1rem; padding: 3rem 1rem;">
    <h1 class="hero-title" style="font-size: 2.8rem;">Engineering Library 📝</h1>
    <p class="hero-subtitle" style="margin-bottom: 1rem;">
        Insights, tutorials, and deep dives into Data Structures, System Design, and Backend Infrastructure.
    </p>
</section>

<!-- Category Navigation Grid -->
<section class="modern-section" style="margin-bottom: 4rem;">
    <h2 class="section-title">Explore by Logic Area</h2>
    <div class="nav-grid">
        <a href="{{ '/blogs/dsa/' | relative_url }}" class="nav-card" style="text-decoration: none; color: inherit; border-left-color: #fca5a5; display: block;">
            <div class="nav-card-title">🔎 Data Structures & Algorithms</div>
            <div class="nav-card-desc">Arrays, Trees, Graphs, and foundational logic.</div>
        </a>
        <a href="{{ '/blogs/algorithms/' | relative_url }}" class="nav-card" style="text-decoration: none; color: inherit; border-left-color: #fcd34d; display: block;">
            <div class="nav-card-title">🧩 Advanced Algorithms</div>
            <div class="nav-card-desc">Dynamic Programming, Greedy, and complex math.</div>
        </a>
        <a href="{{ '/blogs/competitive-programming/' | relative_url }}" class="nav-card" style="text-decoration: none; color: inherit; border-left-color: #6ee7b7; display: block;">
            <div class="nav-card-title">🏆 Competitive Programming</div>
            <div class="nav-card-desc">Fast-execution contest solutions and strategies.</div>
        </a>
        <a href="{{ '/blogs/system-design/' | relative_url }}" class="nav-card" style="text-decoration: none; color: inherit; border-left-color: #93c5fd; display: block;">
            <div class="nav-card-title">🧠 System Architecture</div>
            <div class="nav-card-desc">Scalability, HLD/LLD patterns, and distributed systems.</div>
        </a>
        <a href="{{ '/blogs/data-plane/' | relative_url }}" class="nav-card" style="text-decoration: none; color: inherit; border-left-color: #c4b5fd; display: block;">
            <div class="nav-card-title">🌐 Data Plane & Net</div>
            <div class="nav-card-desc">VPP, DPDK, and low-level packet switching networks.</div>
        </a>
        <a href="{{ '/blogs/finance/' | relative_url }}" class="nav-card" style="text-decoration: none; color: inherit; border-left-color: #a7f3d0; display: block;">
            <div class="nav-card-title">💰 Financial Engineering</div>
            <div class="nav-card-desc">Market topologies, Economics, and HFT.</div>
        </a>
    </div>
</section>

<!-- Recent Posts Loop Overhaul -->
<section class="modern-section">
    <h2 class="section-title">Recent Literature</h2>
    
    {% assign categories = "dsa|algorithms|competitive-programming|system-design|data-plane|general|finance" | split: "|" %}
    
    <div style="max-width: 1000px; margin: 0 auto;">
    {% for cat in categories %}
    {% case cat %}
      {% when 'dsa' %}{% assign label = "Data Structures & Algorithms" %}{% assign line_color = "#fca5a5" %}
      {% when 'algorithms' %}{% assign label = "Algorithms" %}{% assign line_color = "#fcd34d" %}
      {% when 'competitive-programming' %}{% assign label = "Competitive Programming" %}{% assign line_color = "#6ee7b7" %}
      {% when 'system-design' %}{% assign label = "System Design" %}{% assign line_color = "#93c5fd" %}
      {% when 'data-plane' %}{% assign label = "Data Plane & Networking" %}{% assign line_color = "#c4b5fd" %}
      {% when 'general' %}{% assign label = "General & Learning" %}{% assign line_color = "#9ca3af" %}
      {% when 'finance' %}{% assign label = "Finance & Economics" %}{% assign line_color = "#a7f3d0" %}
    {% endcase %}
    
    {% assign cat_url = '/blogs/' | append: cat | append: '/' %}
    {% assign posts_in_cat = site.posts | where_exp: "post", "post.categories contains cat" | sort: "date" | reverse %}
    
    <div style="margin-bottom: 4rem;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.5rem; padding-bottom: 0.5rem; border-bottom: 2px solid var(--border-color);">
            <h3 style="margin: 0; font-size: 1.5rem; font-weight: 700; color: var(--text-color); display: flex; align-items: center; gap: 0.8rem;">
                {{ label }}
                <span style="background: var(--bg-secondary); border-radius: 12px; padding: 0.1rem 0.6rem; font-size: 0.85rem; color: var(--light-text);">{{ posts_in_cat.size }}</span>
            </h3>
            <a href="{{ cat_url | relative_url }}" style="color: #3b82f6; text-decoration: none; font-weight: 600; transition: color 0.2s;">View Archive →</a>
        </div>

        {% if posts_in_cat.size > 0 %}
            <div class="project-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));">
            {% for post in posts_in_cat limit:3 %}
                <div class="featured-project-card" style="border-top-color: {{ line_color }};">
                    <div style="color: var(--light-text); font-size: 0.85rem; margin-bottom: 0.5rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">
                        {{ post.date | date: "%b %d, %Y" }}
                    </div>
                    <div class="featured-project-title">
                        <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: inherit;">{{ post.title }}</a>
                    </div>
                    {% if post.excerpt %}
                    <div class="featured-project-desc" style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 1rem;">
                        {{ post.excerpt | strip_html | truncatewords: 18 }}
                    </div>
                    {% endif %}
                    <a href="{{ post.url | relative_url }}" class="featured-project-link" style="color: {{ line_color | replace: '50', '600' | replace: '100', '600' | replace: 'a5', '600' | replace: 'b7', '600' | replace: 'fd', '600' }}; font-weight: 600;">Read Post →</a>
                </div>
            {% endfor %}
            </div>
        {% else %}
            <div style="background: var(--bg-secondary); border: 1px dashed var(--border-color); border-radius: 12px; padding: 2rem; text-align: center; color: var(--light-text); font-style: italic;">
                Publication stream initializing.
            </div>
        {% endif %}
    </div>
    {% endfor %}
    </div>
</section>

<!-- Foot Navigation -->
<div style="text-align: center; margin: 4rem 0 2rem 0; border-top: 1px solid var(--border-color); padding-top: 3rem;">
  <a href="{{ '/' | relative_url }}" class="btn-secondary">
    <span style="margin-right: 0.5rem;">🏠</span> Return to Root
  </a>
</div>
