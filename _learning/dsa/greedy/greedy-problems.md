---
layout: learning
title: Greedy - Practice Problems
permalink: /learning/dsa/greedy/greedy-problems/
---

{% assign topic_slug = "greedy" %}
{% assign topic_name = "Greedy" %}
{% assign topic_back_url = "/learning/dsa/greedy/" %}

{% assign topic_all    = site.data.problems.problems | where_exp: "p", "p.topics contains topic_slug" %}
{% assign topic_solved = topic_all | where: "solved", true %}
{% assign topic_easy   = topic_all | where: "difficulty", "easy" %}
{% assign topic_medium = topic_all | where: "difficulty", "medium" %}
{% assign topic_hard   = topic_all | where: "difficulty", "hard" %}

# 🌿 {{ topic_name }} — Practice Problems

<div class="topic-crosslinks">
  <a href="{{ '/problems/' | relative_url }}" class="topic-hub-link topic-hub-link--primary">🎯 All Problems Hub</a>
  <a href="{{ topic_back_url | relative_url }}" class="topic-hub-link">← Back to Greedy</a>
  <a href="{{ '/learning/dsa' | relative_url }}" class="topic-hub-link">📊 DSA Hub</a>
</div>

<div class="topic-stats-bar">
  <div class="topic-stat">
    <div class="topic-stat-val">{{ topic_all | size }}</div>
    <div class="topic-stat-lbl">Total</div>
  </div>
  <div class="topic-stat">
    <div class="topic-stat-val" style="color:#10b981;">{{ topic_solved | size }}</div>
    <div class="topic-stat-lbl">Solved</div>
  </div>
  <div class="topic-stat">
    <div class="topic-stat-val" style="color:#10b981;">{{ topic_easy | size }}</div>
    <div class="topic-stat-lbl">Easy</div>
  </div>
  <div class="topic-stat">
    <div class="topic-stat-val" style="color:#f59e0b;">{{ topic_medium | size }}</div>
    <div class="topic-stat-lbl">Medium</div>
  </div>
  <div class="topic-stat">
    <div class="topic-stat-val" style="color:#ef4444;">{{ topic_hard | size }}</div>
    <div class="topic-stat-lbl">Hard</div>
  </div>
</div>

{% assign easy_count = topic_easy | size %}
{% if easy_count > 0 %}
## 🟢 Easy

<div class="pc-grid">
{% for p in topic_easy %}{% include problem-card.html problem=p %}
{% endfor %}</div>
{% endif %}

{% assign medium_count = topic_medium | size %}
{% if medium_count > 0 %}
## 🟡 Medium

<div class="pc-grid">
{% for p in topic_medium %}{% include problem-card.html problem=p %}
{% endfor %}</div>
{% endif %}

{% assign hard_count = topic_hard | size %}
{% if hard_count > 0 %}
## 🔴 Hard

<div class="pc-grid">
{% for p in topic_hard %}{% include problem-card.html problem=p %}
{% endfor %}</div>
{% endif %}

---

<div class="topic-crosslinks" style="justify-content:center; margin-top:2rem;">
  <a href="{{ '/problems/' | relative_url }}" class="topic-hub-link topic-hub-link--primary">🎯 View All Problems in Hub</a>
  <a href="{{ topic_back_url | relative_url }}" class="topic-hub-link">← Back to Greedy</a>
</div>
