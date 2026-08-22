---
title: "Ch0 — Big O Notation & Recursion"
description: "All Roadmaps › DSA Mastery › Chapter 0 Chapter 0 · Beginner · No Prerequisite Big O Notation & Recursion The foundation every DSA topic builds upon — learn to analyse algorithm…"
domain: dsa
track: dsa-mastery
order: 0
chrome: bare
ownHeader: true
url: /learning/dsa/recursion/ch0-bigo-recursion/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<div class="chapter-hero">
  <div class="chapter-hero-inner">
    <div class="ch-hero-breadcrumb">
      <a href="/roadmap/">All Roadmaps</a> ›
      <a href="/learning/dsa/dsa-roadmap/">DSA Mastery</a> ›
      Chapter 0
    </div>
    <div class="chapter-num-badge">Chapter 0 · Beginner · No Prerequisite</div>
    <h1>Big O Notation & Recursion</h1>
    <p class="chapter-hero-sub">The foundation every DSA topic builds upon — learn to analyse algorithm complexity and think recursively before writing a single line of interview code.</p>
    <div class="chapter-meta-row">
      <span class="ch-meta-pill teal">11 Sections</span>
      <span class="ch-meta-pill">4 Practice Problems</span>
      <span class="ch-meta-pill">Beginner</span>
      <a href="/learning/dsa/dsa-roadmap/#ch0" class="ch-nav-btn">← Back to Roadmap</a>
    </div>
  </div>
</div>
<div class="chapter-content">
<div class="chapter-section">
<h2 class="section-heading">Section 1 — What Is Big O Notation?</h2>
<p>Before you write a single line of code in an interview, your interviewer wants to know one thing: <strong>will your solution scale?</strong> Big O notation is the language we use to answer that question.</p>
<p>Big O describes how an algorithm's resource usage grows relative to its input size. It gives a worst-case upper bound on two dimensions:</p>
<div class="insight-box">
  <span class="insight-label">Two Dimensions of Complexity</span>
  <ul>
    <li><strong>Time complexity</strong> — how many operations does the algorithm perform as input grows?</li>
    <li><strong>Space complexity</strong> — how much extra memory does it use? (Input itself is usually excluded)</li>
  </ul>
</div>
<h3 class="section-subheading">1.1 — The Complexity Hierarchy</h3>
<p>Memorise this table. Every time you write code, you should be able to identify which class it falls into:</p>
<div class="ch-ed-problems">
<table>
  <thead>
    <tr><th>Complexity</th><th>Name</th><th>Example</th><th>Acceptable for n=</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>O(1)</strong></td><td>Constant</td><td>Array index access</td><td>Any</td></tr>
    <tr><td><strong>O(log n)</strong></td><td>Logarithmic</td><td>Binary search</td><td>10⁹</td></tr>
    <tr><td><strong>O(n)</strong></td><td>Linear</td><td>Single for-loop</td><td>10⁸</td></tr>
    <tr><td><strong>O(n log n)</strong></td><td>Linearithmic</td><td>Merge sort, heap sort</td><td>10⁷</td></tr>
    <tr><td><strong>O(n²)</strong></td><td>Quadratic</td><td>Nested loops</td><td>5000</td></tr>
    <tr><td><strong>O(2ⁿ)</strong></td><td>Exponential</td><td>Subsets, backtracking</td><td>~25</td></tr>
    <tr><td><strong>O(n!)</strong></td><td>Factorial</td><td>All permutations</td><td>~12</td></tr>
  </tbody>
</table>
</div>
<h3 class="section-subheading">1.2 — Big O Rules</h3>
<div class="insight-box">
  <span class="insight-label">Drop & Simplify Rules</span>
  <ul>
    <li><strong>Drop constants:</strong> O(5n) = O(n). We care about growth rate, not the multiplier.</li>
    <li><strong>Drop lower-order terms:</strong> O(n² + n) = O(n²). The dominant term wins.</li>
    <li><strong>Different inputs = different variables:</strong> Two loops over different arrays is O(a + b), not O(n).</li>
    <li><strong>Nested loops multiply:</strong> An O(n) loop inside an O(m) loop = O(n × m).</li>
    <li><strong>Always analyse worst case</strong> unless told otherwise.</li>
  </ul>
</div>
</div>
<div class="chapter-section">
<h2 class="section-heading">Section 2 — Analysing Common Patterns</h2>
<h3 class="section-subheading">2.1 — Loop-Based Complexity</h3>
<div class="pattern-summary">
  <div class="pattern-card"><h4>Single Loop</h4><p>O(n) — each element visited once. Default assumption for array scan.</p></div>
  <div class="pattern-card"><h4>Nested Loops</h4><p>O(n²) — inner loop runs n times for each outer iteration. Two-pointer avoids this.</p></div>
  <div class="pattern-card"><h4>Half-and-Half</h4><p>O(log n) — problem halved each step. Binary search, balanced BST.</p></div>
  <div class="pattern-card"><h4>Two-Phase</h4><p>O(n + m) — e.g., BFS scan + preprocessing. Add, don't multiply when sequential.</p></div>
</div>
<h3 class="section-subheading">2.2 — Space Complexity</h3>
<div class="insight-box">
  <ul>
    <li>Space complexity counts <em>extra</em> memory your algorithm allocates — not the input.</li>
    <li>Recursive call stack counts as space: a function that recurses n times deep = O(n) space.</li>
    <li>A HashMap storing n entries = O(n) space.</li>
    <li>In-place operations (two-pointer reversal, bubble sort) = O(1) space.</li>
  </ul>
</div>
<div class="ch-code-wrap">
<span class="ch-code-label">Space complexity examples</span>
```cpp
// O(n) space — new vector of size n
vector<int> doubled(n);
for (int i = 0; i < n; i++) doubled[i] = 2 * nums[i];

// O(1) space — in-place swap
int left = 0, right = n-1;
while (left < right) swap(nums[left++], nums[right--]);

// O(n) space (call stack) — recursion depth is n
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n-1);  // n stack frames
}
```
</div>
</div>
<div class="chapter-section">
<h2 class="section-heading">Section 3 — Recursion Fundamentals</h2>
<p>Recursion is a function calling itself with a smaller, simpler version of the same problem. Every recursive function must have exactly two parts:</p>
<div class="insight-box">
  <span class="insight-label">Two Required Components</span>
  <ul>
    <li><strong>Base case:</strong> The condition under which the function stops calling itself and returns a direct answer.</li>
    <li><strong>Recursive case:</strong> Reduce the problem to a smaller subproblem and call yourself again.</li>
  </ul>
  Without a base case → infinite recursion → stack overflow. Without a recursive case → no recursion.
</div>
<h3 class="section-subheading">3.1 — The Call Stack</h3>
<p>Every function call occupies a frame on the call stack. Recursive calls stack up sequentially, then unwind once the base case is hit:</p>
<div class="ch-code-wrap">
<span class="ch-code-label">Fibonacci — trace the call stack</span>
```cpp
int fib(int n) {
    if (n <= 1) return n;          // base case
    return fib(n-1) + fib(n-2);   // recursive case
}
// fib(4):
//   fib(3) → fib(2) → fib(1) → 1
//                    → fib(0) → 0
//          → fib(2) → fib(1) → 1
//                    → fib(0) → 0
//   fib(2) → fib(1) → 1
//           → fib(0) → 0
// Call tree is O(2ⁿ) without memoization!
```
</div>
<h3 class="section-subheading">3.2 — Memoization (Top-Down DP)</h3>
<p>Memoization eliminates repeated subproblem computation by caching results. Transforms Fibonacci from O(2ⁿ) to O(n):</p>
<div class="ch-code-wrap">
```cpp
unordered_map<int,int> memo;
int fib(int n) {
    if (n <= 1) return n;
    if (memo.count(n)) return memo[n];   // cache hit
    return memo[n] = fib(n-1) + fib(n-2); // cache result
}
// Time: O(n) — each state computed once
// Space: O(n) — memo table + call stack
```
</div>
</div>
<div class="chapter-section">
<h2 class="section-heading">Section 4 — Recursive Patterns</h2>
<div class="pattern-summary">
  <div class="pattern-card"><h4>Linear Recursion</h4><p>One recursive call per invocation. O(n) time, O(n) space (stack). Example: factorial, array sum.</p></div>
  <div class="pattern-card"><h4>Binary Recursion</h4><p>Two recursive calls. O(2ⁿ) without memo. O(n) with memoization. Example: Fibonacci, merge sort.</p></div>
  <div class="pattern-card"><h4>Tree/DFS Recursion</h4><p>Recurse on left and right children. O(n) for balanced tree, O(n) stack space.</p></div>
  <div class="pattern-card"><h4>Backtracking</h4><p>Choose → Recurse → Unchoose. Explores O(n!) or O(2ⁿ) paths but prunes early.</p></div>
</div>
<div class="ch-code-wrap">
<span class="ch-code-label">Universal recursion template</span>
```cpp
ReturnType solve(params, state) {
    // 1. Base case
    if (baseCondition) return baseValue;
    // 2. Reduce problem
    subResult = solve(smallerParams, updatedState);
    // 3. Combine and return
    return combine(subResult, currentElement);
}
```
</div>
</div>
<div class="chapter-section">
<h2 class="section-heading">Practice Problems</h2>
<div class="ch-ed-problems">
<table>
  <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Difficulty</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><a href="https://leetcode.com/problems/fibonacci-number/" target="_blank">509. Fibonacci Number</a></td><td>Basic Recursion / Memo</td><td class="diff-easy">Easy</td></tr>
    <tr><td>2</td><td><a href="https://leetcode.com/problems/climbing-stairs/" target="_blank">70. Climbing Stairs</a></td><td>1D Memoized DP</td><td class="diff-easy">Easy</td></tr>
    <tr><td>3</td><td><a href="https://leetcode.com/problems/power-of-two/" target="_blank">231. Power of Two</a></td><td>Bit manipulation + recursion</td><td class="diff-easy">Easy</td></tr>
    <tr><td>4</td><td><a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank">206. Reverse Linked List</a></td><td>Linear Recursion</td><td class="diff-easy">Easy</td></tr>
  </tbody>
</table>
</div>
</div>
</div><!-- end .chapter-content -->
<div class="chapter-nav-footer">
  <a href="/learning/dsa/dsa-roadmap/" class="ch-nav-footer-btn">← DSA Roadmap</a>
  <a href="/learning/dsa/arrays/ch1-arrays-strings/" class="ch-nav-footer-btn primary">Next: Ch1 — Arrays & Strings →</a>
</div>
