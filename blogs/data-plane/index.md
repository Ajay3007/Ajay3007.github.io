---
layout: default
title: Data Plane & Networking
permalink: /blogs/data-plane/
---

<div style="max-width:900px;margin:0 auto;padding:2rem 1rem;">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:2.5rem;flex-wrap:wrap;gap:1rem;">
    <h1 style="display:flex;align-items:center;gap:0.75rem;margin:0;">
      <span style="font-size:2.5rem;">🌐</span>
      <span>Data Plane & Networking</span>
    </h1>
    <a href="{{ '/blogs/' | relative_url }}" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.75rem 1.5rem;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;text-decoration:none;border-radius:8px;font-weight:600;font-size:0.95rem;box-shadow:0 4px 6px rgba(102,126,234,0.3);transition:all 0.3s;">
      ← All Blogs
    </a>
  </div>

  {% assign posts_in_cat = site.posts | where_exp: "post", "post.categories contains 'data-plane'" | sort: "date" | reverse %}

  {% if posts_in_cat.size > 0 %}
  <div style="display:grid;gap:1.5rem;">
    {% for post in posts_in_cat %}
    <article style="padding:1.75rem;background:white;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.08);border-left:4px solid #667eea;transition:all 0.3s;">
      <a href="{{ post.url | relative_url }}" style="text-decoration:none;color:inherit;">
        <h3 style="margin:0 0 0.75rem 0;color:#1e293b;font-size:1.35rem;font-weight:700;line-height:1.4;">{{ post.title }}</h3>
        <div style="color:#64748b;font-size:0.9rem;margin-bottom:1rem;display:flex;align-items:center;gap:0.5rem;">
          <span>📅</span>
          <span>{{ post.date | date: "%B %d, %Y" }}</span>
        </div>
        {% if post.excerpt %}
        <p style="color:#475569;font-size:1rem;line-height:1.7;margin:0;">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
        {% endif %}
      </a>
    </article>
    {% endfor %}
  </div>
  {% else %}
  <div style="text-align:center;padding:3rem 2rem;background:#f8fafc;border-radius:12px;border:2px dashed #cbd5e1;">
    <p style="color:#64748b;font-size:1.1rem;margin:0;">📭 No posts in this category yet.</p>
  </div>
  {% endif %}
</div>
