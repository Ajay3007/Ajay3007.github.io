---
layout: learning
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
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1rem; margin-top: 2rem; max-width: 600px; margin-left: auto; margin-right: auto;">
    {% assign total = site.data.problems | size %}
    {% assign solved = site.data.problems | where: "solved", true | size %}
    {% assign percent = solved | times: 100.0 | divided_by: total | round %}
    <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 8px; backdrop-filter: blur(10px);">
      <div style="font-size: 2rem; font-weight: bold; color: white;">{{ total }}</div>
      <div style="font-size: 0.85rem; color: rgba(255,255,255,0.9);">Total Problems</div>
    </div>
    <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 8px; backdrop-filter: blur(10px);">
      <div style="font-size: 2rem; font-weight: bold; color: #4ade80;">{{ solved }}</div>
      <div style="font-size: 0.85rem; color: rgba(255,255,255,0.9);">Solved</div>
    </div>
    <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 8px; backdrop-filter: blur(10px);">
      <div style="font-size: 2rem; font-weight: bold; color: white;">{{ percent }}%</div>
      <div style="font-size: 0.85rem; color: rgba(255,255,255,0.9);">Success Rate</div>
    </div>
  </div>
</div>

---

## 📚 Problems by Topic

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-top: 2rem;">

  <!-- Linked List Problems -->
  <div style="background: white; border-radius: 12px; padding: 1.8rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); border-left: 5px solid #3b82f6; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 8px 25px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 12px rgba(0,0,0,0.08)';">
    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
      <span style="font-size: 2.5rem;">🔗</span>
      <h3 style="margin: 0; color: #2d3748; font-size: 1.3rem;">Linked List</h3>
    </div>
    {% assign ll_total = site.data.problems | where_exp: "p", "p.topics contains 'linked-list'" | size %}
    {% assign ll_solved = site.data.problems | where_exp: "p", "p.topics contains 'linked-list'" | where: "solved", true | size %}
    {% assign ll_percent = ll_solved | times: 100.0 | divided_by: ll_total | round %}
    <p style="color: #64748b; margin: 0 0 1rem 0; line-height: 1.6;">Master pointer manipulation, cycle detection, and reversal techniques with {{ ll_total }} curated problems.</p>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.2rem; padding: 0.75rem; background: #f1f5f9; border-radius: 6px;">
      <span style="font-size: 0.9rem; color: #64748b;">Progress</span>
      <span style="font-weight: bold; color: #3b82f6;">{{ ll_solved }}/{{ ll_total }} solved ({{ ll_percent }}%)</span>
    </div>
    <a href="{{ '/learning/dsa/linked-list/linked-list-problems/' | relative_url }}" style="display: block; text-align: center; padding: 12px 24px; background: linear-gradient(135deg, #3b82f6, #2563eb); color: white; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.2s;" onmouseover="this.style.transform='scale(1.02)';" onmouseout="this.style.transform='scale(1)';">
      View Problems →
    </a>
  </div>

  <!-- Arrays Problems -->
  <div style="background: white; border-radius: 12px; padding: 1.8rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); border-left: 5px solid #10b981; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 8px 25px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 12px rgba(0,0,0,0.08)';">
    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
      <span style="font-size: 2.5rem;">📊</span>
      <h3 style="margin: 0; color: #2d3748; font-size: 1.3rem;">Arrays</h3>
    </div>
    {% assign arr_total = site.data.problems | where_exp: "p", "p.topics contains 'arrays'" | size %}
    {% assign arr_solved = site.data.problems | where_exp: "p", "p.topics contains 'arrays'" | where: "solved", true | size %}
    {% assign arr_percent = arr_solved | times: 100.0 | divided_by: arr_total | round %}
    <p style="color: #64748b; margin: 0 0 1rem 0; line-height: 1.6;">Two pointers, sliding window, and sorting patterns across {{ arr_total }} problems from easy to hard.</p>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.2rem; padding: 0.75rem; background: #f1f5f9; border-radius: 6px;">
      <span style="font-size: 0.9rem; color: #64748b;">Progress</span>
      <span style="font-weight: bold; color: #10b981;">{{ arr_solved }}/{{ arr_total }} solved ({{ arr_percent }}%)</span>
    </div>
    <a href="{{ '/learning/dsa/arrays/arrays-problems/' | relative_url }}" style="display: block; text-align: center; padding: 12px 24px; background: linear-gradient(135deg, #10b981, #059669); color: white; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.2s;" onmouseover="this.style.transform='scale(1.02)';" onmouseout="this.style.transform='scale(1)';">
      View Problems →
    </a>
  </div>

  <!-- Strings Problems -->
  <div style="background: white; border-radius: 12px; padding: 1.8rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); border-left: 5px solid #f59e0b; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 8px 25px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 12px rgba(0,0,0,0.08)';">
    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
      <span style="font-size: 2.5rem;">🔤</span>
      <h3 style="margin: 0; color: #2d3748; font-size: 1.3rem;">Strings</h3>
    </div>
    {% assign str_total = site.data.problems | where_exp: "p", "p.topics contains 'strings'" | size %}
    {% assign str_solved = site.data.problems | where_exp: "p", "p.topics contains 'strings'" | where: "solved", true | size %}
    {% assign str_percent = str_solved | times: 100.0 | divided_by: str_total | round %}
    <p style="color: #64748b; margin: 0 0 1rem 0; line-height: 1.6;">Pattern matching, palindromes, and string manipulation with {{ str_total }} problems.</p>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.2rem; padding: 0.75rem; background: #f1f5f9; border-radius: 6px;">
      <span style="font-size: 0.9rem; color: #64748b;">Progress</span>
      <span style="font-weight: bold; color: #f59e0b;">{{ str_solved }}/{{ str_total }} solved ({{ str_percent }}%)</span>
    </div>
    <a href="{{ '/learning/dsa/strings/strings-problems/' | relative_url }}" style="display: block; text-align: center; padding: 12px 24px; background: linear-gradient(135deg, #f59e0b, #d97706); color: white; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.2s;" onmouseover="this.style.transform='scale(1.02)';" onmouseout="this.style.transform='scale(1)';">
      View Problems →
    </a>
  </div>

  <!-- Stacks Problems -->
  <div style="background: white; border-radius: 12px; padding: 1.8rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); border-left: 5px solid #ef4444; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 8px 25px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 12px rgba(0,0,0,0.08)';">
    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
      <span style="font-size: 2.5rem;">📚</span>
      <h3 style="margin: 0; color: #2d3748; font-size: 1.3rem;">Stacks</h3>
    </div>
    {% assign stk_total = site.data.problems | where_exp: "p", "p.topics contains 'stacks'" | size %}
    {% assign stk_solved = site.data.problems | where_exp: "p", "p.topics contains 'stacks'" | where: "solved", true | size %}
    {% assign stk_percent = stk_solved | times: 100.0 | divided_by: stk_total | round %}
    <p style="color: #64748b; margin: 0 0 1rem 0; line-height: 1.6;">LIFO operations, monotonic stacks, and expression evaluation across {{ stk_total }} problems.</p>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.2rem; padding: 0.75rem; background: #f1f5f9; border-radius: 6px;">
      <span style="font-size: 0.9rem; color: #64748b;">Progress</span>
      <span style="font-weight: bold; color: #ef4444;">{{ stk_solved }}/{{ stk_total }} solved ({{ stk_percent }}%)</span>
    </div>
    <a href="{{ '/learning/dsa/stacks/stacks-problems/' | relative_url }}" style="display: block; text-align: center; padding: 12px 24px; background: linear-gradient(135deg, #ef4444, #dc2626); color: white; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.2s;" onmouseover="this.style.transform='scale(1.02)';" onmouseout="this.style.transform='scale(1)';">
      View Problems →
    </a>
  </div>

  <!-- Searching & Sorting Problems -->
  <div style="background: white; border-radius: 12px; padding: 1.8rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); border-left: 5px solid #8b5cf6; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 8px 25px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 12px rgba(0,0,0,0.08)';">
    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
      <span style="font-size: 2.5rem;">🔍</span>
      <h3 style="margin: 0; color: #2d3748; font-size: 1.3rem;">Searching & Sorting</h3>
    </div>
    {% assign ss_total = site.data.problems | where_exp: "p", "p.topics contains 'searching-sorting'" | size %}
    {% assign ss_solved = site.data.problems | where_exp: "p", "p.topics contains 'searching-sorting'" | where: "solved", true | size %}
    {% assign ss_percent = ss_solved | times: 100.0 | divided_by: ss_total | round %}
    <p style="color: #64748b; margin: 0 0 1rem 0; line-height: 1.6;">Binary search variations and sorting algorithms with {{ ss_total }} comprehensive problems.</p>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.2rem; padding: 0.75rem; background: {% if ss_percent == 100 %}#dcfce7{% else %}#f1f5f9{% endif %}; border-radius: 6px;">
      <span style="font-size: 0.9rem; color: {% if ss_percent == 100 %}#15803d{% else %}#64748b{% endif %};">{% if ss_percent == 100 %}Complete! 🎉{% else %}Progress{% endif %}</span>
      <span style="font-weight: bold; color: {% if ss_percent == 100 %}#15803d{% else %}#8b5cf6{% endif %};">{{ ss_solved }}/{{ ss_total }} solved ({{ ss_percent }}%)</span>
    </div>
    <a href="{{ '/learning/dsa/searching-sorting/searching-sorting-problems/' | relative_url }}" style="display: block; text-align: center; padding: 12px 24px; background: linear-gradient(135deg, #8b5cf6, #7c3aed); color: white; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.2s;" onmouseover="this.style.transform='scale(1.02)';" onmouseout="this.style.transform='scale(1)';">
      View Problems →
    </a>
  </div>

  <!-- Tree Problems (Coming Soon) -->
  <div style="background: white; border-radius: 12px; padding: 1.8rem; box-shadow: 0 2px 12px rgba(0,0,0,0.08); border-left: 5px solid #06b6d4; transition: all 0.3s; opacity: 0.7;">
    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
      <span style="font-size: 2.5rem;">🌳</span>
      <h3 style="margin: 0; color: #2d3748; font-size: 1.3rem;">Tree</h3>
    </div>
    {% assign tree_total = site.data.problems | where_exp: "p", "p.topics contains 'tree'" | size %}
    {% assign tree_solved = site.data.problems | where_exp: "p", "p.topics contains 'tree'" | where: "solved", true | size %}
    {% assign tree_percent = 0 %}
    {% if tree_total > 0 %}{% assign tree_percent = tree_solved | times: 100.0 | divided_by: tree_total | round %}{% endif %}
    <p style="color: #64748b; margin: 0 0 1rem 0; line-height: 1.6;">Binary trees, BST, and traversal patterns with {{ tree_total }} problems to master.</p>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.2rem; padding: 0.75rem; background: #f1f5f9; border-radius: 6px;">
      <span style="font-size: 0.9rem; color: #64748b;">Progress</span>
      <span style="font-weight: bold; color: #06b6d4;">{{ tree_solved }}/{{ tree_total }} solved ({{ tree_percent }}%)</span>
    </div>
    <div style="display: block; text-align: center; padding: 12px 24px; background: #e2e8f0; color: #64748b; border-radius: 8px; font-weight: 600;">
      Coming Soon
    </div>
  </div>

</div>

---

## 💡 How to Use This Hub

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin-top: 2rem; margin-bottom: 3rem;">
  <div style="padding: 1.5rem; background: #f8fafc; border-radius: 10px; border-top: 3px solid #667eea;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">📊</div>
    <h4 style="margin: 0 0 0.5rem 0; color: #2d3748;">Track Progress</h4>
    <p style="margin: 0; color: #64748b; font-size: 0.95rem;">Use the Master Problem List to track your overall progress across all 77 problems.</p>
  </div>
  <div style="padding: 1.5rem; background: #f8fafc; border-radius: 10px; border-top: 3px solid #10b981;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎯</div>
    <h4 style="margin: 0 0 0.5rem 0; color: #2d3748;">Choose Topic</h4>
    <p style="margin: 0; color: #64748b; font-size: 0.95rem;">Select a topic card above to dive into problems organized by difficulty level.</p>
  </div>
  <div style="padding: 1.5rem; background: #f8fafc; border-radius: 10px; border-top: 3px solid #f59e0b;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">💻</div>
    <h4 style="margin: 0 0 0.5rem 0; color: #2d3748;">View Solutions</h4>
    <p style="margin: 0; color: #64748b; font-size: 0.95rem;">Each problem includes links to approaches and working solutions with explanations.</p>
  </div>
  <div style="padding: 1.5rem; background: #f8fafc; border-radius: 10px; border-top: 3px solid #ef4444;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🚀</div>
    <h4 style="margin: 0 0 0.5rem 0; color: #2d3748;">Practice Daily</h4>
    <p style="margin: 0; color: #64748b; font-size: 0.95rem;">Solve problems consistently from Easy → Medium → Hard for best results.</p>
  </div>
</div>

---

<div style="text-align: center; margin-top: 3rem; padding: 2rem; background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.1)); border-radius: 12px;">
  <p style="color: #64748b; margin-bottom: 1.5rem; font-size: 1.05rem; font-style: italic;">💡 <strong>Pro Tip:</strong> Focus on understanding patterns rather than memorizing solutions. Each problem builds fundamental skills used across multiple scenarios.</p>
  <a href="{{ '/learning/dsa' | relative_url }}" style="display:inline-block;padding:12px 30px;background:#667eea;color:white;border-radius:8px;text-decoration:none;font-weight:600;margin-right:10px;transition: all 0.2s;" onmouseover="this.style.background='#5568d3';" onmouseout="this.style.background='#667eea';">← Back to DSA Hub</a>
  <a href="{{ '/' | relative_url }}" style="display:inline-block;padding:12px 30px;background:#764ba2;color:white;border-radius:8px;text-decoration:none;font-weight:600;transition: all 0.2s;" onmouseover="this.style.background='#63408a';" onmouseout="this.style.background='#764ba2';">🏠 Home</a>
</div>
