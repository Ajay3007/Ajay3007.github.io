---
layout: default
title: Practice Problems Hub
permalink: /problems/
---

# 🎯 Practice Problems Hub

Central hub for all coding practice problems organized by topic with solutions and approaches.

---

## 📊 Master Problem List

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 12px; margin-bottom: 3rem; text-align: center; box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);">
  <h2 style="color: white; margin: 0 0 0.5rem 0; font-size: 1.8rem;">🧭 Complete Problem Tracker</h2>
  <!-- <p style="color: rgba(255,255,255,0.95); margin: 0 0 1.5rem 0; font-size: 1.05rem;">Track your progress across all 77 problems from 6 major DSA topics</p> -->
  <a href="{{ '/learning/dsa/master-problem-list/' | relative_url }}" style="display: inline-block; padding: 15px 40px; background: white; color: #667eea; border-radius: 10px; text-decoration: none; font-weight: bold; font-size: 1.2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: all 0.3s;" onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 6px 20px rgba(0,0,0,0.3)';" onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 4px 15px rgba(0,0,0,0.2)';">
    📋 View Master Problem List →
  </a>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 0.75rem; margin-top: 1.5rem; max-width: 600px; margin-left: auto; margin-right: auto;">
    {% assign total = site.data.problems | size %}
    {% assign solved = site.data.problems | where: "solved", true | size %}
    {% assign percent = solved | times: 100.0 | divided_by: total | round %}
    <div style="background: rgba(255,255,255,0.2); padding: 0.75rem; border-radius: 8px; backdrop-filter: blur(10px);">
      <div style="font-size: 2rem; font-weight: bold; color: white;">{{ total }}</div>
      <div style="font-size: 0.85rem; color: rgba(255,255,255,0.9);">Total Problems</div>
    </div>
    <div style="background: rgba(255,255,255,0.2); padding: 0.75rem; border-radius: 8px; backdrop-filter: blur(10px);">
      <div style="font-size: 2rem; font-weight: bold; color: #4ade80;">{{ solved }}</div>
      <div style="font-size: 0.85rem; color: rgba(255,255,255,0.9);">Solved</div>
    </div>
    <div style="background: rgba(255,255,255,0.2); padding: 0.75rem; border-radius: 8px; backdrop-filter: blur(10px);">
      <div style="font-size: 2rem; font-weight: bold; color: white;">{{ percent }}%</div>
      <div style="font-size: 0.85rem; color: rgba(255,255,255,0.9);">Success Rate</div>
    </div>
  </div>
</div>

---

## 📚 Interactive Problem Database

<div class="problems-dashboard" style="margin-top: 2rem;">
  <!-- Filters Bar -->
  <div class="filters-bar" style="display: flex; gap: 1rem; margin-bottom: 2rem; flex-wrap: wrap;">
    <input type="text" id="filter-search" autocomplete="off" placeholder="🔍 Search prob by name/ID..." style="padding: 0.8rem 1rem; flex: 1; min-width: 250px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-color); color: var(--text-color); font-size: 0.95rem; outline: none; transition: box-shadow 0.2s;">
    <select id="filter-difficulty" style="padding: 0.8rem 1rem; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-color); color: var(--text-color); font-size: 0.95rem; cursor: pointer; outline: none;">
      <option value="all">⚡️ All Difficulties</option>
      <option value="easy">🟢 Easy</option>
      <option value="medium">🟡 Medium</option>
      <option value="hard">🔴 Hard</option>
    </select>
    <select id="filter-topic" style="padding: 0.8rem 1rem; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-color); color: var(--text-color); font-size: 0.95rem; cursor: pointer; outline: none;">
      <option value="all">📁 All Topics</option>
      <option value="arrays">Arrays</option>
      <option value="strings">Strings</option>
      <option value="linked-list">Linked List</option>
      <option value="stacks">Stacks</option>
      <option value="tree">Trees</option>
      <option value="searching-sorting">Searching & Sorting</option>
      <option value="sliding-window">Sliding Window</option>
      <option value="two-pointers">Two Pointers</option>
    </select>
    <select id="filter-status" style="padding: 0.8rem 1rem; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-color); color: var(--text-color); font-size: 0.95rem; cursor: pointer; outline: none;">
      <option value="all">🎯 All Status</option>
      <option value="solved">✅ Solved</option>
      <option value="todo">⭕️ Unsolved</option>
    </select>
  </div>

  <!-- Dynamic Data Table -->
  <div class="problem-table-wrapper" style="overflow-x: auto; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); border-radius: 12px; border: 1px solid var(--border-color); background: var(--bg-color);">
    <table id="problems-table" style="width: 100%; border-collapse: collapse; text-align: left; min-width: 800px;">
      <thead style="background: var(--bg-secondary);">
        <tr style="border-bottom: 2px solid var(--border-color);">
          <th style="padding: 1.2rem 1rem; width: 5%; font-weight: 600; color: var(--text-color); text-align: center;">Status</th>
          <th style="padding: 1.2rem 1rem; width: 40%; font-weight: 600; color: var(--text-color);">Problem Title</th>
          <th style="padding: 1.2rem 1rem; width: 10%; font-weight: 600; color: var(--text-color);">Difficulty</th>
          <th style="padding: 1.2rem 1rem; width: 25%; font-weight: 600; color: var(--text-color);">Topics</th>
          <th style="padding: 1.2rem 1rem; width: 20%; font-weight: 600; color: var(--text-color);">Study Material</th>
        </tr>
      </thead>
      <tbody id="problems-tbody">
        <!-- Rows will be injected instantly by problems.js -->
      </tbody>
    </table>
  </div>
</div>

<!-- Serialize the Problem Data Payload for JS -->
<script>
  window.dsaProblems = [
    {% for p in site.data.problems %}
    {
      "id": {{ p.id | jsonify | default: '""' }},
      "title": {{ p.title | jsonify | default: '""' }},
      "platform": {{ p.platform | jsonify | default: '""' }},
      "difficulty": {{ p.difficulty | jsonify | default: '""' }},
      "topics": {{ p.topics | jsonify | default: '[]' }},
      "solved": {{ p.solved | default: false | jsonify }},
      "problem_url": {{ p.problem_url | jsonify | default: '""' }},
      "approach_url": {{ p.approach_url | jsonify | default: '""' }},
      "solution_url": {{ p.solution_url | jsonify | default: '""' }}
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];
</script>
<script src="{{ '/assets/js/problems.js' | relative_url }}"></script>

---

<div style="text-align: center; margin-top: 3rem; padding: 2rem; background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.1)); border-radius: 12px;">
  <p style="color: #64748b; margin-bottom: 1.5rem; font-size: 1.05rem; font-style: italic;">💡 <strong>Pro Tip:</strong> Focus on understanding patterns rather than memorizing solutions. Each problem builds fundamental skills used across multiple scenarios.</p>
  <a href="{{ '/learning/dsa' | relative_url }}" style="display:inline-block;padding:12px 30px;background:#667eea;color:white;border-radius:8px;text-decoration:none;font-weight:600;margin-right:10px;transition: all 0.2s;" onmouseover="this.style.background='#5568d3';" onmouseout="this.style.background='#667eea';">← Back to DSA Hub</a>
  <a href="{{ '/' | relative_url }}" style="display:inline-block;padding:12px 30px;background:#764ba2;color:white;border-radius:8px;text-decoration:none;font-weight:600;transition: all 0.2s;" onmouseover="this.style.background='#63408a';" onmouseout="this.style.background='#764ba2';">🏠 Home</a>
</div>
