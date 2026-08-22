---
title: "Ch6 — Heaps & Priority Queues"
description: "All Roadmaps › DSA Mastery › Chapter 6 Chapter 6 · Intermediate · Prereq: Chapter 5 Heaps & Priority Queues Master the data structure powered by complete binary trees."
domain: dsa
track: dsa-mastery
order: 6
chrome: bare
ownHeader: true
url: /learning/dsa/heaps/ch6-heaps/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<div class="chapter-hero">
  <div class="chapter-hero-inner">
<div class="ch-hero-breadcrumb">
<a href="/roadmap/">All Roadmaps</a> ›
<a href="/learning/dsa/dsa-roadmap/">DSA Mastery</a> ›
      Chapter 6
</div>
<div class="chapter-num-badge">Chapter 6 · Intermediate · Prereq: Chapter 5</div>
<h1>Heaps & Priority Queues</h1>
<p class="chapter-hero-sub">Master the data structure powered by complete binary trees. Learn to pinpoint Top-K problems, merge K sorted lists, and track rolling medians efficiently.</p>
<div class="chapter-meta-row">
<span class="ch-meta-pill teal">11 Sections</span>
<span class="ch-meta-pill">8 Practice Problems</span>
<span class="ch-meta-pill">Intermediate</span>
<a href="/learning/dsa/dsa-roadmap/#ch6" class="ch-nav-btn">← Back to Roadmap</a>
</div>
  </div>
</div>
<div class="chapter-content">
<!-- Section 1 -->
<div class="chapter-section">
<h2 class="section-heading">Section 1 — What Is a Heap?</h2>
<p>A heap is a <strong>complete binary tree</strong> stored as a flat array satisfying the heap property: every parent is <code>&gt;=</code> its children (max-heap) or <code>&lt;=</code> its children (min-heap). This guarantees <code>O(1)</code> access to the extreme element and <code>O(log n)</code> insert / delete.</p>
<div class="insight-box">
  <span class="insight-label">Real-World Analogy: Hospital ER</span>
  <ul>
<li>Patients arrive with different severity levels — the most critical patient is always treated next (root node).</li>
<li>A new critical patient jumps ahead of less-critical ones already waiting.</li>
<li>Each arrival (push) and each treatment (pop) costs <code>O(log n)</code> to maintain order.</li>
  </ul>
</div>
<h3 class="section-subheading">1.1 — Tree-to-Array Mapping</h3>
<p>Because it's a complete binary tree (nodes filled left-to-right), there are zero wasted slots. No pointers needed.</p>
<div class="ch-code-wrap">
<span class="ch-code-label">Tree vs Array Representation</span>
```text
Max-Heap tree:           Stored as array (0-indexed):

       10                Index: [ 0] [ 1] [ 2] [ 3] [ 4] [ 5] [ 6]
      /  \               Value: [10] [ 9] [ 8] [ 7] [ 6] [ 5] [ 4]
     9    8
    / \  / \
   7   6 5   4

Arithmetic for finding relatives of node `i`:
- Parent:      (i - 1) / 2
- Left child:  2*i + 1
- Right child: 2*i + 2
```
</div>
<h3 class="section-subheading">1.2 — Min-Heap vs Max-Heap</h3>
<div class="ch-ed-problems">
<table>
  <thead>
<tr><th>Property</th><th>Min-Heap</th><th>Max-Heap</th></tr>
  </thead>
  <tbody>
<tr><td><strong>Root</strong></td><td>Minimum value</td><td>Maximum value</td></tr>
<tr><td><strong>Parent Rule</strong></td><td>Parent <code>&lt;=</code> Children</td><td>Parent <code>&gt;=</code> Children</td></tr>
<tr><td><strong><code>peek()</code></strong></td><td>Returns minimum <code>O(1)</code></td><td>Returns maximum <code>O(1)</code></td></tr>
<tr><td><strong>C++ STL</strong></td><td><code>priority_queue&lt;int, vector&lt;int&gt;, greater&lt;int&gt;&gt;</code></td><td><code>priority_queue&lt;int&gt;</code> (default)</td></tr>
<tr><td><strong>Use cases</strong></td><td>Top-K smallest, Dijkstra, K-way merge</td><td>Top-K largest, CPU scheduling</td></tr>
  </tbody>
</table>
</div>
</div>
<!-- Section 2 -->
<div class="chapter-section">
<h2 class="section-heading">Section 2 — Core Operations</h2>
<h3 class="section-subheading">2.1 — Insert (Sift Up) — <code>O(log n)</code></h3>
<p>To insert, append the new element to the end of the array (bottom of the tree). Then, continuously swap it with its parent if it violates the heap property (sifting it "up").</p>
<h3 class="section-subheading">2.2 — Extract Max/Min (Sift Down) — <code>O(log n)</code></h3>
<p>To extract the root, swap it with the very last element in the array. Remove the last element (the answer). Now the root is wrong. Swap the new root with its largest (or smallest) child until the heap property is restored (sifting it "down").</p>
<div class="insight-box">
  <span class="insight-label">The Top-K Paradox</span>
  <p>To find the <strong>top-K LARGEST</strong> elements, use a <strong>MIN-heap</strong> of size K.</p>
  <ul>
<li>The heap strictly holds the "K largest seen so far".</li>
<li>The root is the <em>smallest</em> of that elite group (the "weakest link").</li>
<li>When a new element arrives, if it's strictly greater than the root, it beats the weakest link. Pop the root and push the new element.</li>
  </ul>
</div>
</div>
<!-- Section 3 -->
<div class="chapter-section">
<h2 class="section-heading">Section 3 — C++ Implementation Guide</h2>
<h3 class="section-subheading">3.1 — Priority Queue API</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++ priority_queue</span>
```cpp
#include <queue>

// MAX-HEAP (Default)
priority_queue<int> maxH;       
maxH.push(5);    // O(log n)
maxH.top();      // O(1) - Returns 5
maxH.pop();      // O(log n) - Removes 5. Returns void!

// MIN-HEAP
priority_queue<int, vector<int>, greater<int>> minH;

// PAIR HEAP (e.g. Dijkstra)
// Ordered by first element ascending
using P = pair<int, int>;
priority_queue<P, vector<P>, greater<P>> pq_pairs;

// O(n) HEAPIFY FROM VECTOR
vector<int> v = {3, 1, 4, 1, 5};
priority_queue<int> h(v.begin(), v.end()); // Better than pushing n times!
```
</div>
<h3 class="section-subheading">3.2 — Custom Comparators</h3>
<p>When you need to order objects dynamically (e.g., frequencies), use a lambda comparator.</p>
<div class="ch-code-wrap">
<span class="ch-code-label">Custom Min-Heap</span>
```cpp
auto cmp = [](pair<int,string> a, pair<int,string> b){
    return a.first > b.first; // Note standard reverse operator orientation! MIN-heap on frequency
};
// Use decltype for lambdas
priority_queue<pair<int,string>, vector<pair<int,string>>, decltype(cmp)> customH(cmp);
```
</div>
</div>
<!-- Section 4 -->
<div class="chapter-section">
<h2 class="section-heading">Section 4 — Two-Heap Pattern (Median of Stream)</h2>
<p>A classic architecture pattern is tracking a moving median using two balanced heaps. This guarantees <code>O(log n)</code> inserts and <code>O(1)</code> reads.</p>
<div class="pattern-summary">
  <div class="pattern-card"><h4>Lower Half</h4><p><strong>Max-Heap:</strong> Stores the smaller half of numbers. Root = largest of the smalls.</p></div>
  <div class="pattern-card"><h4>Upper Half</h4><p><strong>Min-Heap:</strong> Stores the larger half of numbers. Root = smallest of the bigs.</p></div>
</div>
<div class="insight-box">
  <span class="insight-label">Two Invariants</span>
  <ol>
<li>Every element in lower half <code>&lt;=</code> every element in upper half (<code>lo.top() &lt;= hi.top()</code>).</li>
<li>Sizes differ by at most 1. Generally, if odd elements, the extra lives in <code>lo</code>.</li>
  </ol>
</div>
<div class="ch-code-wrap">
<span class="ch-code-label">LeetCode 295: Find Median from Data Stream</span>
```cpp
class MedianFinder {
    priority_queue<int> lo;                               // max-heap
    priority_queue<int, vector<int>, greater<int>> hi;    // min-heap
public:
    void addNum(int num) {
        lo.push(num); // 1. Always push lower first
        
        // 2. Fix ordering violation (Invariant 1)
        if (!hi.empty() && lo.top() > hi.top()) {
            hi.push(lo.top()); lo.pop();
        }
        
        // 3. Rebalance (Invariant 2)
        if (lo.size() > hi.size() + 1) {
            hi.push(lo.top()); lo.pop();
        } else if (hi.size() > lo.size()) {
            lo.push(hi.top()); hi.pop();
        }
    }
    
    double findMedian() {
        if (lo.size() > hi.size()) return lo.top();
        return (lo.top() + hi.top()) / 2.0;
    }
};
```
</div>
</div>
<!-- Section 5 -->
<div class="chapter-section">
<h2 class="section-heading">Section 5 — Practice Problems & Patterns</h2>
<div class="ch-ed-problems">
<table>
  <thead>
<tr><th>Pattern Trigger</th><th>Action</th></tr>
  </thead>
  <tbody>
<tr><td><strong>"Kth Largest Element"</strong></td><td>Min-Heap of size K</td></tr>
<tr><td><strong>"Kth Smallest Element"</strong></td><td>Max-Heap of size K</td></tr>
<tr><td><strong>"Top K Frequent"</strong></td><td>Build HashMap counts &rarr; Min-Heap of size K</td></tr>
<tr><td><strong>"Merge K Sorted Lists/Arrays"</strong></td><td>Min-Heap storing heads <code>(value, list_idx)</code></td></tr>
<tr><td><strong>"Shortest Path in Weighted Graph"</strong></td><td>Dijkstra (Min-Heap of <code>(distance, node_id)</code>)</td></tr>
<tr><td><strong>"Data Stream Median"</strong></td><td>Two-Heap (Max lower, Min upper)</td></tr>
  </tbody>
</table>
</div>
<div class="ch-ed-problems" style="margin-top: 2rem;">
  <span class="insight-label">Practice Checklist</span>
  <table>
<thead>
<tr><th>#</th><th>Problem</th><th>Difficulty</th><th>Pattern</th></tr>
</thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/remove-stones-to-minimize-the-total/" target="_blank">1962. Remove Stones</a></td><td>Medium</td><td>Max-Heap</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/minimum-cost-to-connect-sticks/" target="_blank">1167. Connect Sticks</a></td><td>Medium</td><td>Min-Heap</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/kth-largest-element-in-an-array/" target="_blank">215. Kth Largest</a></td><td>Medium</td><td>Top K</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/k-closest-points-to-origin/" target="_blank">973. K Closest Points</a></td><td>Medium</td><td>Top K</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/kth-largest-element-in-a-stream/" target="_blank">703. Kth Largest Stream</a></td><td>Easy</td><td>Top K</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/find-median-from-data-stream/" target="_blank">295. Find Median</a></td><td>Hard</td><td>Two Heaps</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/task-scheduler/" target="_blank">621. Task Scheduler</a></td><td>Medium</td><td>Max-Heap + Queue</td></tr>
<tr><td>8</td><td><a href="https://leetcode.com/problems/merge-k-sorted-lists/" target="_blank">23. Merge K Lists</a></td><td>Hard</td><td>Min-Heap (K-way)</td></tr>
</tbody>
  </table>
</div>
</div>
<div class="chapter-footer-nav">
  <div class="nav-prev">
<a href="/learning/dsa/tree/ch5-trees-graphs/" class="ch-nav-footer-btn">← Ch5 Trees & Graphs</a>
  </div>
  <div class="nav-next">
<a href="/learning/dsa/greedy/ch7-greedy/" class="ch-nav-footer-btn primary">Next: Ch7 — Greedy Algorithms →</a>
  </div>
</div>
</div>
