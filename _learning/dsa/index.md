---
layout: default
title: Data Structures & Algorithms
permalink: /learning/dsa/
---

# 🧠 Data Structures & Algorithms

{% assign total = site.data.problems.problems | size %}
{% assign solved = site.data.problems.problems | where: "solved", true | size %}

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem; text-align: center;">
  <div style="display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap;">
    <div style="color: white;">
      <div style="font-size: 2.5rem; font-weight: 700;">{{ total }}</div>
      <div style="font-size: 0.9rem; opacity: 0.9;">Problems Curated</div>
    </div>
    <div style="color: white;">
      <div style="font-size: 2.5rem; font-weight: 700; color: #a8ffb0;">{{ solved }}</div>
      <div style="font-size: 0.9rem; opacity: 0.9;">Solved</div>
    </div>
    <div style="color: white;">
      <a href="{{ '/problems/' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:white;color:#667eea;border-radius:8px;text-decoration:none;font-weight:700;margin-top:0.5rem;">
        📋 View All Problems →
      </a>
    </div>
  </div>
</div>

---

## Topics

<div class="projects-list" style="grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; display: grid; margin: 2rem 0;">

  <div class="project-card" style="border-left: 4px solid #3b82f6;">
    <h3><a href="{{ '/learning/dsa/arrays/' | relative_url }}">📐 Arrays</a></h3>
    <p>Sliding window, two pointers, prefix sums, Kadane's. Core pattern mastery.</p>
    {% assign arr_solved = site.data.problems.problems | where_exp: "p", "p.topics contains 'arrays'" | where: "solved", true | size %}
    {% assign arr_total = site.data.problems.problems | where_exp: "p", "p.topics contains 'arrays'" | size %}
    <small style="color:#667eea; font-weight:600;">{{ arr_solved }}/{{ arr_total }} solved</small>
  </div>

  <div class="project-card" style="border-left: 4px solid #8b5cf6;">
    <h3><a href="{{ '/learning/dsa/strings/' | relative_url }}">🔤 Strings</a></h3>
    <p>Pattern matching, hashing, palindromes, anagrams, encoding.</p>
    {% assign str_solved = site.data.problems.problems | where_exp: "p", "p.topics contains 'strings'" | where: "solved", true | size %}
    {% assign str_total = site.data.problems.problems | where_exp: "p", "p.topics contains 'strings'" | size %}
    <small style="color:#667eea; font-weight:600;">{{ str_solved }}/{{ str_total }} solved</small>
  </div>

  <div class="project-card" style="border-left: 4px solid #ec4899;">
    <h3><a href="{{ '/learning/dsa/linked-list/' | relative_url }}">🔗 Linked List</a></h3>
    <p>Singly & doubly lists, cycle detection, reversal, fast/slow pointers.</p>
    {% assign ll_solved = site.data.problems.problems | where_exp: "p", "p.topics contains 'linked-list'" | where: "solved", true | size %}
    {% assign ll_total = site.data.problems.problems | where_exp: "p", "p.topics contains 'linked-list'" | size %}
    <small style="color:#667eea; font-weight:600;">{{ ll_solved }}/{{ ll_total }} solved</small>
  </div>

  <div class="project-card" style="border-left: 4px solid #f59e0b;">
    <h3><a href="{{ '/learning/dsa/stacks/' | relative_url }}">⚡ Stacks</a></h3>
    <p>LIFO structure, monotonic stacks, applications.</p>
    {% assign stk_solved = site.data.problems.problems | where_exp: "p", "p.topics contains 'stacks'" | where: "solved", true | size %}
    {% assign stk_total = site.data.problems.problems | where_exp: "p", "p.topics contains 'stacks'" | size %}
    <small style="color:#667eea; font-weight:600;">{{ stk_solved }}/{{ stk_total }} solved</small>
  </div>

  <div class="project-card" style="border-left: 4px solid #10b981;">
    <h3><a href="{{ '/learning/dsa/queues/' | relative_url }}">🔄 Queues</a></h3>
    <p>FIFO structure, circular & priority queues. 🚧 Content coming.</p>
  </div>

  <div class="project-card" style="border-left: 4px solid #06b6d4;">
    <h3><a href="{{ '/learning/dsa/tree/' | relative_url }}">🌲 Trees</a></h3>
    <p>Traversals, BST, segment trees, tries.</p>
    {% assign tree_solved = site.data.problems.problems | where_exp: "p", "p.topics contains 'tree'" | where: "solved", true | size %}
    {% assign tree_total = site.data.problems.problems | where_exp: "p", "p.topics contains 'tree'" | size %}
    <small style="color:#667eea; font-weight:600;">{{ tree_solved }}/{{ tree_total }} solved</small>
  </div>

  <div class="project-card" style="border-left: 4px solid #6366f1;">
    <h3><a href="{{ '/learning/dsa/searching-sorting/' | relative_url }}">🔍 Searching & Sorting</a></h3>
    <p>Binary search, binary search on answer, all sorting algorithms.</p>
    {% assign ss_solved = site.data.problems.problems | where_exp: "p", "p.topics contains 'searching-sorting'" | where: "solved", true | size %}
    {% assign ss_total = site.data.problems.problems | where_exp: "p", "p.topics contains 'searching-sorting'" | size %}
    <small style="color:#667eea; font-weight:600;">{{ ss_solved }}/{{ ss_total }} solved</small>
  </div>

  <div class="project-card" style="border-left: 4px solid #ef4444;">
    <h3><a href="{{ '/learning/dsa/graphs/' | relative_url }}">🕸️ Graphs</a></h3>
    <p>BFS/DFS, shortest paths, MST, topological sort. 🚧 Content coming.</p>
  </div>

  <div class="project-card" style="border-left: 4px solid #84cc16;">
    <h3><a href="{{ '/learning/dsa/dynamic-programming/' | relative_url }}">💡 Dynamic Programming</a></h3>
    <p>1D/2D DP, Knapsack family, memoization vs tabulation. 🚧 Content coming.</p>
  </div>

  <div class="project-card" style="border-left: 4px solid #a855f7;">
    <h3><a href="{{ '/learning/dsa/recursion/' | relative_url }}">🔁 Recursion</a></h3>
    <p>Base cases, recurrence, stack frames, tail recursion. 🚧 Content coming.</p>
  </div>

  <div class="project-card" style="border-left: 4px solid #f97316;">
    <h3><a href="{{ '/learning/dsa/backtracking/' | relative_url }}">🔙 Backtracking</a></h3>
    <p>Try/choose/backtrack; pruning with constraints. 🚧 Content coming.</p>
  </div>

  <div class="project-card" style="border-left: 4px solid #0ea5e9;">
    <h3><a href="{{ '/learning/dsa/binary-search/' | relative_url }}">📐 Binary Search</a></h3>
    <p>Lower/upper bound, first/last occurrence, rotated arrays. 🚧 Content coming.</p>
  </div>

</div>

---

<div style="text-align:center;margin-top:2rem;">
  <a href="{{ '/learning/' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#1976d2;color:white;text-decoration:none;border-radius:8px;font-weight:600;margin-right:1rem;">← Back to Learning Hub</a>
  <a href="{{ '/' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#2d3748;color:white;text-decoration:none;border-radius:8px;font-weight:600;">🏠 Home</a>
</div>
