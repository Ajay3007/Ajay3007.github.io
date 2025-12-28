---
layout: default
title: Data Plane & Networking
permalink: /blogs/data-plane/
---

# 🌐 Data Plane & Networking <small><a href="{{ '/blogs/' | relative_url }}">All blogs »</a></small>

{% assign posts_in_cat = site.posts | where_exp: "post", "post.categories contains 'data-plane'" | sort: "date" | reverse %}

{% if posts_in_cat.size > 0 %}
{% for post in posts_in_cat %}
- [{{ post.title }}]({{ post.url | relative_url }}) <small>{{ post.date | date: "%B %d, %Y" }}</small>
  {%- if post.excerpt -%}<br><span style="color:#607d8b;font-size:0.9rem;">{{ post.excerpt | strip_html | truncatewords: 20 }}</span>{%- endif -%}
{% endfor %}
{% else %}
> No posts in this category yet.
{% endif %}

<div style="text-align:center;margin-top:2.5rem;">
  <a href="{{ '/blogs/' | relative_url }}" class="btn-crosslink">
    ← Back to Blogs
  </a>
</div>
