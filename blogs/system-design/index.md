---
layout: default
title: System Design
permalink: /blogs/system-design/
---

# System Design <small><a href="{{ '/blogs/' | relative_url }}">All blogs »</a></small>

{% assign posts_in_cat = site.posts | where_exp: "post", "post.categories contains 'system-design'" | sort: "date" | reverse %}

{% if posts_in_cat.size > 0 %}
{% for post in posts_in_cat %}
- [{{ post.title }}]({{ post.url | relative_url }}) <small>{{ post.date | date: "%B %d, %Y" }}</small>
{% endfor %}
{% else %}
> No posts in this category yet.
{% endif %}

<div style="text-align:center;margin-top:2.5rem;">
  <a href="{{ '/blogs/' | relative_url }}" class="btn-crosslink">
    ← Back to Blogs
  </a>
</div>
