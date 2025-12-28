---
layout: default
title: Blogs
permalink: /blogs/
---


# Blogs


Welcome to the blogs index. Explore posts by category:

<div class="section-divider"></div>

<div class="category-list" style="display:flex;flex-wrap:wrap;gap:2.5rem 2.5rem;justify-content:center;margin:2.5rem 0 2.5rem 0;">
  <a href="{{ '/blogs/dsa/' | relative_url }}" class="category-card" style="display:flex;flex-direction:column;align-items:center;justify-content:center;min-width:220px;max-width:260px;padding:2.2rem 1.2rem;background:rgba(255,255,255,0.88);border-radius:16px;box-shadow:0 2px 12px #e2e8f0;transition:transform 0.15s,box-shadow 0.15s;text-decoration:none;color:#222;position:relative;overflow:hidden;">
    <span style="font-size:2.2rem;">🔎</span>
    <span style="font-size:1.13rem;font-weight:700;margin:1.1rem 0 0.2rem 0;">Data Structures & Algorithms</span>
    <span style="color:#607d8b;font-size:0.98rem;">All DSA & Algorithm posts</span>
  </a>
  <a href="{{ '/blogs/algorithms/' | relative_url }}" class="category-card" style="display:flex;flex-direction:column;align-items:center;justify-content:center;min-width:220px;max-width:260px;padding:2.2rem 1.2rem;background:rgba(255,255,255,0.88);border-radius:16px;box-shadow:0 2px 12px #e2e8f0;transition:transform 0.15s,box-shadow 0.15s;text-decoration:none;color:#222;position:relative;overflow:hidden;">
    <span style="font-size:2.2rem;">🧩</span>
    <span style="font-size:1.13rem;font-weight:700;margin:1.1rem 0 0.2rem 0;">Algorithms</span>
    <span style="color:#607d8b;font-size:0.98rem;">Algorithm posts</span>
  </a>
  <a href="{{ '/blogs/competitive-programming/' | relative_url }}" class="category-card" style="display:flex;flex-direction:column;align-items:center;justify-content:center;min-width:220px;max-width:260px;padding:2.2rem 1.2rem;background:rgba(255,255,255,0.88);border-radius:16px;box-shadow:0 2px 12px #e2e8f0;transition:transform 0.15s,box-shadow 0.15s;text-decoration:none;color:#222;position:relative;overflow:hidden;">
    <span style="font-size:2.2rem;">🏆</span>
    <span style="font-size:1.13rem;font-weight:700;margin:1.1rem 0 0.2rem 0;">Competitive Programming</span>
    <span style="color:#607d8b;font-size:0.98rem;">CP & Problem Solving posts</span>
  </a>
  <a href="{{ '/blogs/system-design/' | relative_url }}" class="category-card" style="display:flex;flex-direction:column;align-items:center;justify-content:center;min-width:220px;max-width:260px;padding:2.2rem 1.2rem;background:rgba(255,255,255,0.88);border-radius:16px;box-shadow:0 2px 12px #e2e8f0;transition:transform 0.15s,box-shadow 0.15s;text-decoration:none;color:#222;position:relative;overflow:hidden;">
    <span style="font-size:2.2rem;">🧠</span>
    <span style="font-size:1.13rem;font-weight:700;margin:1.1rem 0 0.2rem 0;">System Design</span>
    <span style="color:#607d8b;font-size:0.98rem;">System Design posts</span>
  </a>
  <a href="{{ '/blogs/data-plane/' | relative_url }}" class="category-card" style="display:flex;flex-direction:column;align-items:center;justify-content:center;min-width:220px;max-width:260px;padding:2.2rem 1.2rem;background:rgba(255,255,255,0.88);border-radius:16px;box-shadow:0 2px 12px #e2e8f0;transition:transform 0.15s,box-shadow 0.15s;text-decoration:none;color:#222;position:relative;overflow:hidden;">
    <span style="font-size:2.2rem;">🌐</span>
    <span style="font-size:1.13rem;font-weight:700;margin:1.1rem 0 0.2rem 0;">Data Plane & Networking</span>
    <span style="color:#607d8b;font-size:0.98rem;">VPP, DPDK, Networking posts</span>
  </a>
  <a href="{{ '/blogs/general/' | relative_url }}" class="category-card" style="display:flex;flex-direction:column;align-items:center;justify-content:center;min-width:220px;max-width:260px;padding:2.2rem 1.2rem;background:rgba(255,255,255,0.88);border-radius:16px;box-shadow:0 2px 12px #e2e8f0;transition:transform 0.15s,box-shadow 0.15s;text-decoration:none;color:#222;position:relative;overflow:hidden;">
    <span style="font-size:2.2rem;">📝</span>
    <span style="font-size:1.13rem;font-weight:700;margin:1.1rem 0 0.2rem 0;">General & Learning</span>
    <span style="color:#607d8b;font-size:0.98rem;">General & Learning posts</span>
  </a>
</div>



## All Blog Posts by Category

{% assign categories = "dsa|algorithms|competitive-programming|system-design|data-plane|general" | split: "|" %}

{% for cat in categories %}
{% case cat %}
  {% when 'dsa' %}{% assign label = "Data Structures & Algorithms" %}{% assign emoji = "🔎" %}
  {% when 'algorithms' %}{% assign label = "Algorithms" %}{% assign emoji = "🧩" %}
  {% when 'competitive-programming' %}{% assign label = "Competitive Programming" %}{% assign emoji = "🏆" %}
  {% when 'system-design' %}{% assign label = "System Design" %}{% assign emoji = "🧠" %}
  {% when 'data-plane' %}{% assign label = "Data Plane & Networking" %}{% assign emoji = "🌐" %}
  {% when 'general' %}{% assign label = "General & Learning" %}{% assign emoji = "📝" %}
{% endcase %}

{% assign cat_url = '/blogs/' | append: cat | append: '/' %}

{%- assign posts_in_cat = site.posts | where_exp: "post", "post.categories contains cat" | sort: "date" | reverse -%}

### {{ emoji }} {{ label }} <span style="background:#e2e8f0;border-radius:12px;padding:0.1rem 0.45rem;font-size:0.85rem;color:#34495e;margin-left:0.35rem;">{{ posts_in_cat.size }}</span> <small><a href="{{ cat_url | relative_url }}">View all »</a></small>
{%- if posts_in_cat.size > 0 -%}
{%- for post in posts_in_cat -%}
- [{{ post.title }}]({{ post.url | relative_url }}) <small>{{ post.date | date: "%B %d, %Y" }}</small>
  {%- if post.excerpt -%}<br><span style="color:#607d8b;font-size:0.9rem;">{{ post.excerpt | strip_html | truncatewords: 20 }}</span>{%- endif -%}
{%- endfor -%}
{%- else -%}
> No posts in this category yet.
{%- endif -%}

<div style="border-top:1px solid #e2e8f0;margin:1.5rem 0;"></div>

{%- endfor -%}

<div style="text-align:center;margin-top:2.5rem;">
  <a href="{{ '/' | relative_url }}" class="btn-crosslink">
    <span style="font-size:1.3rem;">🏠</span> Back to Home
  </a>
</div>
