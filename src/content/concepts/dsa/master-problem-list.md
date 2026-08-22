---
title: "Master Problem List"
description: "📋 Master Problem List {{ site.data.problems.problems size }} Total Problems {{ site.data.problems.problems where: \"solved\", true size }} Solved ✓ {{…"
domain: dsa
order: 99
url: /learning/dsa/master-problem-list/
---

# 📋 Master Problem List

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem; text-align: center;">
  <div style="display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap;">
    <div style="color: white;">
      <div style="font-size: 2.5rem; font-weight: 700;">{{ site.data.problems.problems | size }}</div>
      <div style="font-size: 0.9rem; opacity: 0.9;">Total Problems</div>
    </div>
    <div style="color: white;">
      <div style="font-size: 2.5rem; font-weight: 700; color: #a8ffb0;">{{ site.data.problems.problems | where: "solved", true | size }}</div>
      <div style="font-size: 0.9rem; opacity: 0.9;">Solved ✓</div>
    </div>
    <div style="color: white;">
      <div style="font-size: 2.5rem; font-weight: 700; color: #ffd6a5;">{{ site.data.problems.problems | where: "solved", false | size }}</div>
      <div style="font-size: 0.9rem; opacity: 0.9;">In Progress ○</div>
    </div>
  </div>
</div>

---

## Arrays & Sliding Window

<div class="problem-grid">
{% assign sw_problems = site.data.problems.problems | where_exp: "p", "p.topics contains 'sliding-window'" %}
{% for p in sw_problems %}
  {% include problem-card.html problem=p %}
{% endfor %}
</div>

---

## Two Pointers

<div class="problem-grid">
{% assign tp_problems = site.data.problems.problems | where_exp: "p", "p.topics contains 'two-pointers'" | where_exp: "p", "p.topics contains 'arrays'" %}
{% for p in tp_problems %}
  {% include problem-card.html problem=p %}
{% endfor %}
</div>

---

## Strings

<div class="problem-grid">
{% assign str_problems = site.data.problems.problems | where_exp: "p", "p.topics contains 'strings'" | where_exp: "p", "p.topics[0] == 'strings'" %}
{% for p in str_problems %}
  {% include problem-card.html problem=p %}
{% endfor %}
</div>

---

## Linked List

<div class="problem-grid">
{% assign ll_problems = site.data.problems.problems | where_exp: "p", "p.topics contains 'linked-list'" | where_exp: "p", "p.topics[0] == 'linked-list'" %}
{% for p in ll_problems %}
  {% include problem-card.html problem=p %}
{% endfor %}
</div>

---

## Stacks

<div class="problem-grid">
{% assign stk_problems = site.data.problems.problems | where_exp: "p", "p.topics contains 'stacks'" %}
{% for p in stk_problems %}
  {% include problem-card.html problem=p %}
{% endfor %}
</div>

---

## Trees

<div class="problem-grid">
{% assign tree_problems = site.data.problems.problems | where_exp: "p", "p.topics contains 'tree'" %}
{% for p in tree_problems %}
  {% include problem-card.html problem=p %}
{% endfor %}
</div>

---

## Searching & Sorting

<div class="problem-grid">
{% assign ss_problems = site.data.problems.problems | where_exp: "p", "p.topics contains 'searching-sorting'" | where_exp: "p", "p.topics[0] == 'searching-sorting'" %}
{% for p in ss_problems %}
  {% include problem-card.html problem=p %}
{% endfor %}
</div>

---

<div style="text-align:center;margin-top:2.5rem;">
  <a href="/learning/dsa" style="display:inline-block;padding:0.75rem 1.5rem;background:#1976d2;color:white;text-decoration:none;border-radius:8px;font-weight:600;margin-right:1rem;">← Back to DSA Hub</a>
  <a href="/" style="display:inline-block;padding:0.75rem 1.5rem;background:#2d3748;color:white;text-decoration:none;border-radius:8px;font-weight:600;">🏠 Home</a>
</div>
