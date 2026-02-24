---
layout: default
title: Home
---

<!-- Hero Section -->
<section class="hero-section">
    <h1 class="hero-title">Hi, I'm Ajay 👋</h1>
    <p class="hero-subtitle">
        Software Engineer with 4+ years building high-performance systems in <strong>networking</strong>, <strong>data plane infrastructure</strong>, and <strong>backend architecture</strong>. Passionate about real-time threat detection and scalable system design.
    </p>
    <div class="hero-actions">
        <a href="{{ '/projects' | relative_url }}" class="btn-primary">View Projects</a>
        <a href="{{ '/about' | relative_url }}" class="btn-secondary">Learn More</a>
    </div>
</section>

<!-- By The Numbers -->
<section class="modern-section">
    <h2 class="section-title">By The Numbers</h2>
    <div class="stats-grid">
        <div class="stat-card" style="border-top-color: var(--secondary-color);">
            <div class="stat-number" style="color: var(--secondary-color);">{{ site.posts | size }}</div>
            <div class="stat-label">Blog Posts</div>
        </div>
        <div class="stat-card" style="border-top-color: var(--accent-color);">
            <div class="stat-number" style="color: var(--accent-color);">{{ site.projects | size }}</div>
            <div class="stat-label">Projects</div>
        </div>
        <div class="stat-card" style="border-top-color: #10b981;">
            <div class="stat-number" style="color: #10b981;">{{ site.data.problems.problems | size | default: '77' }}</div>
            <div class="stat-label">DSA Problems</div>
        </div>
        <div class="stat-card" style="border-top-color: #9945ff;">
            <div class="stat-number" style="color: #9945ff;">10+</div>
            <div class="stat-label">Core Topics</div>
        </div>
    </div>
</section>

<!-- Featured Projects -->
<section class="modern-section">
    <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 2rem;">
        <h2 class="section-title" style="margin-bottom: 0;">Featured Projects</h2>
        <a href="{{ '/projects' | relative_url }}" class="btn-secondary" style="padding: 0.5rem 1rem; font-size: 0.9rem; margin-bottom: 8px;">All Projects →</a>
    </div>
    <div class="project-grid">
        {% for project in site.projects limit: 3 %}
        <div class="featured-project-card" style="border-top-color: {% cycle '#764ba2', '#667eea', '#00d4ff' %};">
            <div class="featured-project-title"><a href="{{ project.url | relative_url }}" style="text-decoration: none; color: inherit;">{{ project.title }}</a></div>
            {% if project.description %}
            <div class="featured-project-desc">{{ project.description }}</div>
            {% endif %}
            <a href="{{ project.url | relative_url }}" class="featured-project-link">Learn more →</a>
        </div>
        {% endfor %}
    </div>
</section>

<!-- DSA Hub Showcase -->
<section class="modern-section">
    <div class="dsa-hub-card">
        <div class="dsa-hub-content">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <span style="font-size: 3rem;">🎯</span>
                <div>
                    <h2 style="margin: 0; color: white; font-size: 2rem;">Practice Problems Hub</h2>
                    <p style="margin: 0.5rem 0 0 0; color: rgba(255,255,255,0.9); font-size: 1.1rem;">Master DSA with curated problems across multiple patterns and structures.</p>
                </div>
            </div>
            <div class="dsa-stats">
                <div class="dsa-stat-box">
                    <div class="val">{{ site.data.problems.problems | size | default: '77' }}</div>
                    <div class="lbl">Total Problems</div>
                </div>
                <!-- Calculate total solved based on the new problems.yml structure if solving property exists, fallback to placeholder -->
                {% assign solved_count = 0 %}
                {% for problem in site.data.problems.problems %}
                    {% if problem.solved == true or problem.solved == "true" or problem.status == "Solved" %}
                        {% assign solved_count = solved_count | plus: 1 %}
                    {% endif %}
                {% endfor %}
                <div class="dsa-stat-box">
                    <div class="val" style="color: #4ade80;">{% if solved_count > 0 %}{{ solved_count }}{% else %}43{% endif %}</div>
                    <div class="lbl">Solved</div>
                </div>
                <div class="dsa-stat-box">
                    <div class="val">6</div>
                    <div class="lbl">Core Topics</div>
                </div>
            </div>
            <a href="{{ '/problems/' | relative_url }}" class="btn-secondary" style="margin-top: 1rem; display: inline-block;">
                🚀 Dive into the Hub
            </a>
        </div>
    </div>
</section>

<!-- Learning Paths -->
<section class="modern-section">
    <h2 class="section-title" style="margin-bottom: 2rem;">Learning Paths</h2>
    <div class="nav-grid">
        <a href="{{ '/learning/dsa/' | relative_url }}" class="nav-card" style="border-left-color: #00d4ff;">
            <div class="nav-card-title">📊 DSA & Algorithms</div>
            <div class="nav-card-desc">Structures, patterns & practical theory solving.</div>
        </a>
        <a href="{{ '/learning/system-design/' | relative_url }}" class="nav-card" style="border-left-color: #ff6b9d;">
            <div class="nav-card-title">🏗️ System Design</div>
            <div class="nav-card-desc">High-level architecture, scalability, & tradeoffs.</div>
        </a>
        <a href="{{ '/learning/networking/' | relative_url }}" class="nav-card" style="border-left-color: #9945ff;">
            <div class="nav-card-title">🌐 Networking</div>
            <div class="nav-card-desc">Protocols, routing, TCP/UDP & practical networks.</div>
        </a>
        <a href="{{ '/learning/oop/' | relative_url }}" class="nav-card" style="border-left-color: #f59e0b;">
            <div class="nav-card-title">🎯 OOP & Patterns</div>
            <div class="nav-card-desc">Core design principles, SOLID, & design patterns.</div>
        </a>
        <a href="{{ '/learning/data-plane/' | relative_url }}" class="nav-card" style="border-left-color: #10b981;">
            <div class="nav-card-title">⚡ Data Plane</div>
            <div class="nav-card-desc">DPDK, VPP, & extreme performance optimization.</div>
        </a>
        <a href="{{ '/learning/programming-language/' | relative_url }}" class="nav-card" style="border-left-color: #3b82f6;">
            <div class="nav-card-title">💻 Languages</div>
            <div class="nav-card-desc">Deep dives into C++, Java, and Python semantics.</div>
        </a>
    </div>
</section>

<!-- Recent Blog Posts -->
<section class="modern-section">
    <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 2rem;">
        <h2 class="section-title" style="margin-bottom: 0;">Recent Thoughts</h2>
        <a href="{{ '/blogs' | relative_url }}" class="btn-secondary" style="padding: 0.5rem 1rem; font-size: 0.9rem; margin-bottom: 8px;">All Posts →</a>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
        {% for post in site.posts limit: 3 %}
        <div class="stat-card" style="text-align: left; padding: 1.8rem; border-left: 4px solid #667eea; border-top: none;">
            <time style="color: #9ca3af; font-size: 0.85rem; display: block; margin-bottom: 0.5rem;">{{ post.date | date: "%B %d, %Y" }}</time>
            <h3 style="margin: 0 0 0.75rem 0; font-size: 1.25rem;"><a href="{{ post.url | relative_url }}" style="text-decoration: none; color: var(--primary-color);">{{ post.title }}</a></h3>
            {% if post.excerpt %}
            <p style="margin: 0; color: var(--light-text); font-size: 0.95rem; line-height: 1.6;">{{ post.excerpt | strip_html | truncatewords: 20 }}</p>
            {% endif %}
        </div>
        {% endfor %}
    </div>
</section>

<!-- About This Site -->
<section class="modern-section" style="text-align: center; max-width: 700px; margin: 5rem auto 3rem auto;">
    <h2 class="section-title">💡 About This Site</h2>
    <p style="font-size: 1.1rem; color: var(--light-text); line-height: 1.8; margin-bottom: 2rem;">
        A comprehensive portfolio and learning hub documenting my <strong>4+ years</strong> in high-performance systems, data plane development, and backend infrastructure. Here you'll find technical deep dives, real-world projects, and actionable learning resources.
    </p>
    <a href="{{ '/about' | relative_url }}" class="btn-primary" style="background: linear-gradient(90deg, #00d4ff, #ff6b9d);">
        <span style="margin-right: 0.5rem;">👤</span> Read the Full Story
    </a>
</section>
