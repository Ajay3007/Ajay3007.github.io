---
layout: default
title: Archive
permalink: /blogs/
---

<section class="c-section" style="margin-top: 0; padding-top: 56px;">
  <div class="c-section-head">
    <div>
      <div class="c-kicker">// JOURNAL</div>
      <h1 class="c-section-title">Archive.</h1>
    </div>
  </div>

  {% assign categories = "dsa|algorithms|competitive-programming|system-design|data-plane|general|finance" | split: "|" %}
  {% assign labels = "DSA & Algorithms|Algorithms|Competitive Programming|System Design|Data Plane & Networking|General|Finance & Economics" | split: "|" %}

  {% for cat in categories %}
  {% assign posts_in_cat = site.posts | where_exp: "post", "post.categories contains cat" | sort: "date" | reverse %}
  {% if posts_in_cat.size > 0 %}
  <div style="margin-bottom: 40px;">
    <div class="c-kicker" style="margin-bottom: 12px;">// {{ labels[forloop.index0] | upcase }}</div>
    <div class="c-post-list">
      {% for post in posts_in_cat %}
      <a href="{{ post.url | relative_url }}" class="c-post-row">
        <span class="c-post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
        <span class="c-post-title">{{ post.title }}</span>
        <span class="c-post-cat">{{ post.categories | first | default: "general" }}</span>
        <span class="c-post-arrow">→</span>
      </a>
      {% endfor %}
    </div>
  </div>
  {% endif %}
  {% endfor %}

</section>
