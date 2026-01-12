---
layout: default
title: Finance & Economics
permalink: /blogs/finance/
---

# 💰 Finance & Economics

All posts related to finance, economics, treasury bonds, forex reserves, and financial analysis.

---

## All Finance Posts

<div style="display:grid;gap:1.5rem;margin:2rem 0;">
{% assign finance_posts = site.posts | where_exp: "post", "post.categories contains 'finance'" | sort: "date" | reverse %}

{% if finance_posts.size > 0 %}
  {% for post in finance_posts %}
  <div style="padding:1.5rem;background:linear-gradient(135deg,#f8fafc 0%,#e0f7ff 100%);border-radius:10px;border-left:4px solid #667eea;box-shadow:0 2px 8px rgba(102,126,234,0.1);">
    <a href="{{ post.url | relative_url }}" style="text-decoration:none;color:#1e293b;display:block;">
      <h3 style="margin:0 0 0.5rem 0;">{{ post.title }}</h3>
      <div style="color:#64748b;font-size:0.9rem;margin-bottom:0.75rem;">
        📅 {{ post.date | date: "%B %d, %Y" }}
      </div>
      {% if post.excerpt %}
      <p style="color:#475569;margin:0;line-height:1.6;">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
      {% endif %}
    </a>
  </div>
  {% endfor %}
{% else %}
  <p style="color:#64748b;font-style:italic;padding:2rem;text-align:center;background:#f8fafc;border-radius:8px;">No finance posts yet. Check back soon!</p>
{% endif %}
</div>

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/blogs' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← All Blogs</a>
  <a href="{{ '/' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Home 🏠</a>
</div>
