---
layout: default
title: "Ch4 — Stacks & Queues"
permalink: /learning/dsa/stacks/ch4-stacks-queues/
custom_css: dsa-chapter
---

<div class="chapter-hero">
  <div class="chapter-hero-inner">
    <div class="ch-hero-breadcrumb">
      <a href="{{ '/roadmap/' | relative_url }}">All Roadmaps</a> ›
      <a href="{{ '/learning/dsa/dsa-roadmap/' | relative_url }}">DSA Mastery</a> ›
      Chapter 4
    </div>
    <div class="chapter-num-badge">Chapter 4 · Intermediate · Prereq: Chapter 3</div>
    <h1>Stacks & Queues</h1>
    <p class="chapter-hero-sub">LIFO vs FIFO · Bracket Matching · Monotonic Stacks · Deque Sliding Window — the patterns that eliminate O(n²) loops with elegant O(n) stack-based sweeps.</p>
    <div class="chapter-meta-row">
      <span class="ch-meta-pill teal">11 Sections</span>
      <span class="ch-meta-pill">13 Practice Problems</span>
      <span class="ch-meta-pill">Intermediate</span>
      <a href="{{ '/learning/dsa/dsa-roadmap/#ch4' | relative_url }}" class="ch-nav-btn">← Back to Roadmap</a>
    </div>
  </div>
</div>

<div class="chapter-content">

<!-- ═══════════════════════ Section 1 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 1 — Stacks: LIFO Data Structure</h2>
<p>A <strong>stack</strong> is a linear data structure following <strong>Last In, First Out (LIFO)</strong>: the last element pushed is the first one popped. Think of a pile of dinner plates — you always add and remove from the top.</p>

<div class="insight-box">
  <span class="insight-label">Real-World Stack Analogies</span>
  <ul>
    <li><strong>Function call stack:</strong> OS pushes a stack frame on each function call, pops on return. Stack overflow = too deep recursion.</li>
    <li><strong>Browser history:</strong> Back button pops the last visited URL. Forward button uses a second stack.</li>
    <li><strong>Undo/Redo:</strong> Text editors push changes; undo pops the last change.</li>
    <li><strong>Expression evaluator:</strong> Compilers evaluate infix/postfix math using stacks.</li>
  </ul>
</div>

<h3 class="section-subheading">1.1 — Stack Operations in C++</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
#include <stack>
stack<int> st;

st.push(10);       // push — O(1)
st.push(20);
st.push(30);
st.top();          // peek top = 30 — O(1), does NOT remove
st.pop();          // remove top = 30 — O(1), returns void
st.empty();        // true if empty — O(1)
st.size();         // number of elements — O(1)

// CRITICAL: ALWAYS check empty() before top() or pop()
if (!st.empty()) { int val = st.top(); st.pop(); }
{% endhighlight %}
</div>

<div class="ch-cplx-row">
  <span class="ch-cplx"><span>Push / Pop / Top</span>O(1)</span>
  <span class="ch-cplx"><span>Space</span>O(n)</span>
</div>
</div>

<!-- ═══════════════════════ Section 2 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 2 — Queues: FIFO Data Structure</h2>
<p>A <strong>queue</strong> is a linear data structure following <strong>First In, First Out (FIFO)</strong>: the first element enqueued is the first dequeued. Think of a supermarket checkout line — customers are served in arrival order.</p>

<div class="insight-box">
  <span class="insight-label">Stack vs Queue in One Sentence</span>
  Stack: last in, first out (DFS). Queue: first in, first out (BFS). Mixing them is the #1 source of wrong answers on BFS/DFS problems.
</div>

<div class="ch-code-wrap">
{% highlight cpp %}
#include <queue>
queue<int> q;

q.push(1);         // enqueue rear — O(1)
q.push(2);
q.push(3);
q.front();         // peek front = 1 — O(1), does NOT remove
q.back();          // peek rear = 3 — O(1)
q.pop();           // dequeue front = 1 — O(1), returns void
q.empty();         // true if empty — O(1)
q.size();          // number of elements — O(1)

// Deque (double-ended queue) — push/pop from BOTH ends O(1)
#include <deque>
deque<int> dq;
dq.push_back(1);   dq.push_front(0);
dq.pop_back();     dq.pop_front();
dq.front();        dq.back();
{% endhighlight %}
</div>

<div class="ch-cplx-row">
  <span class="ch-cplx"><span>Push / Pop / Front / Back</span>O(1)</span>
  <span class="ch-cplx"><span>Space</span>O(n)</span>
</div>
</div>

<!-- ═══════════════════════ Section 3 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 3 — Pattern: Bracket Matching</h2>
<p>The classic stack application: use a stack to ensure every opening bracket has a matching closing bracket in the correct order.</p>

<div class="insight-box">
  <span class="insight-label">Algorithm — Valid Parentheses</span>
  <ul>
    <li>Opening bracket <code>( [ {</code> → <strong>push</strong> onto stack</li>
    <li>Closing bracket <code>) ] }</code> → check if stack top is the matching opener; if yes <strong>pop</strong>, if no → <strong>invalid</strong></li>
    <li>At the end: stack must be <strong>empty</strong> (all openers matched)</li>
  </ul>
  Common mistake: returning <code>true</code> at end without checking <code>st.empty()</code>. Input <code>((( </code> is invalid but stack is non-empty!
</div>

<div class="ch-code-wrap">
{% highlight cpp %}
bool isValid(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else {
            if (st.empty()) return false;  // no matching opener
            char top = st.top(); st.pop();
            if ((c==')' && top!='(') ||
                (c==']' && top!='[') ||
                (c=='}' && top!='{')) return false;
        }
    }
    return st.empty();  // all openers must be matched
}
{% endhighlight %}
</div>
<div class="ch-cplx-row">
  <span class="ch-cplx"><span>Time</span>O(n)</span>
  <span class="ch-cplx"><span>Space</span>O(n)</span>
</div>
</div>

<!-- ═══════════════════════ Section 4 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 4 — Pattern: Min Stack (O(1) getMin)</h2>
<p>Design a stack that supports push, pop, top, and <strong>getMin() in O(1)</strong>. The trick: maintain an auxiliary <em>min-tracking stack</em> that stores the current minimum at each depth.</p>

<div class="insight-box">
  <span class="insight-label">Key Insight</span>
  When you push a value, also push the minimum of (that value, current minStack top) onto the auxiliary stack. When you pop the main stack, pop the auxiliary stack too. The auxiliary stack top always holds the global minimum for the current state.
</div>

<div class="ch-code-wrap">
{% highlight cpp %}
class MinStack {
    stack<int> st, minSt;
public:
    void push(int val) {
        st.push(val);
        int curMin = minSt.empty() ? val : min(val, minSt.top());
        minSt.push(curMin);
    }
    void pop() { st.pop(); minSt.pop(); }   // always pop both
    int top() { return st.top(); }
    int getMin() { return minSt.top(); }    // O(1)
};
{% endhighlight %}
</div>
<div class="ch-cplx-row">
  <span class="ch-cplx"><span>All ops</span>O(1)</span>
  <span class="ch-cplx"><span>Space</span>O(n) — two stacks</span>
</div>
</div>

<!-- ═══════════════════════ Section 5 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 5 — Pattern: Queue Using Two Stacks</h2>
<p>Simulate FIFO queue behaviour using two LIFO stacks. Key: <strong>lazy transfer</strong> — only move elements from inbox to outbox when outbox is empty.</p>

<div class="insight-box">
  <span class="insight-label">Two-Stack Queue — Amortised O(1)</span>
  <ul>
    <li><strong>inbox</strong> stack: receives all push() calls — O(1)</li>
    <li><strong>outbox</strong> stack: serves all pop()/peek() calls</li>
    <li>When outbox is empty, transfer ALL elements from inbox to outbox (single reversal gives FIFO order)</li>
    <li>Each element moves at most once: inbox→outbox. Total work across n operations = O(n) → <strong>amortised O(1) per operation</strong></li>
  </ul>
</div>

<div class="ch-code-wrap">
{% highlight cpp %}
class MyQueue {
    stack<int> inbox, outbox;
    void transfer() {
        if (outbox.empty())
            while (!inbox.empty()) { outbox.push(inbox.top()); inbox.pop(); }
    }
public:
    void push(int x) { inbox.push(x); }  // O(1)
    int pop()  { transfer(); int v=outbox.top(); outbox.pop(); return v; }
    int peek() { transfer(); return outbox.top(); }
    bool empty() { return inbox.empty() && outbox.empty(); }
};
{% endhighlight %}
</div>
</div>

<!-- ═══════════════════════ Section 6 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 6 — Pattern: Monotonic Stack</h2>
<p>A <strong>monotonic stack</strong> maintains elements in strictly increasing or decreasing order. When a new element violates the order, we pop until order is restored. This solves Next Greater Element and similar problems in <strong>O(n)</strong>.</p>

<div class="insight-box">
  <span class="insight-label">Two Monotonic Stack Variants</span>
  <ul>
    <li><strong>Decreasing stack</strong> (top is smallest): pop when new element is <em>greater</em>. Answers: Next Greater Element, Daily Temperatures.</li>
    <li><strong>Increasing stack</strong> (top is largest): pop when new element is <em>smaller</em>. Answers: Next Smaller Element, Histogram.</li>
    <li><strong>Always store INDICES, not values</strong> — you need indices to compute distances and record answers at the right position.</li>
    <li>Each element is pushed once and popped at most once → <strong>O(n) amortised total</strong>.</li>
  </ul>
</div>

<h3 class="section-subheading">6.1 — Next Greater Element</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// Next Greater Element — O(n) time, O(n) space
vector<int> nextGreater(vector<int>& arr) {
    int n = arr.size();
    vector<int> ans(n, -1);  // default: no greater element
    stack<int> st;            // stores INDICES, decreasing stack
    for (int i = 0; i < n; i++) {
        while (!st.empty() && arr[i] > arr[st.top()]) {
            ans[st.top()] = arr[i];  // arr[i] is the next greater
            st.pop();
        }
        st.push(i);
    }
    return ans;
    // Remaining elements in stack have no next greater (ans=-1 by default)
}

// Circular array (scan 2n indices, use i%n)
for (int i = 0; i < 2*n; i++) {
    while (!st.empty() && arr[i%n] > arr[st.top()])
        { ans[st.top()] = arr[i%n]; st.pop(); }
    if (i < n) st.push(i);
}
{% endhighlight %}
</div>

<h3 class="section-subheading">6.2 — Daily Temperatures Trace (arr = [73,74,75,71,69,72,76,73])</h3>
<div class="dsa-pattern-box">
  <ul>
    <li><strong>i=0, temp=73:</strong> stack empty → push 0. Stack:[0]</li>
    <li><strong>i=1, temp=74:</strong> 74 > 73 → pop 0, ans[0]=1–0=1; push 1. Stack:[1]</li>
    <li><strong>i=2, temp=75:</strong> 75 > 74 → pop 1, ans[1]=2–1=1; push 2. Stack:[2]</li>
    <li><strong>i=3, temp=71:</strong> 71 < 75 → push 3. Stack:[2,3]</li>
    <li><strong>i=4, temp=69:</strong> 69 < 71 → push 4. Stack:[2,3,4]</li>
    <li><strong>i=5, temp=72:</strong> 72>69 pop 4 ans[4]=1; 72>71 pop 3 ans[3]=2; push 5. Stack:[2,5]</li>
    <li><strong>i=6, temp=76:</strong> 76>72 pop 5 ans[5]=1; 76>75 pop 2 ans[2]=4; push 6. Stack:[6]</li>
    <li><strong>i=7, temp=73:</strong> 73 < 76 → push 7. Stack:[6,7]</li>
    <li><strong>END:</strong> idx 6,7 remain → no warmer day → ans[6]=0, ans[7]=0</li>
    <li><strong>Final: ans = [1, 1, 4, 2, 1, 1, 0, 0]</strong> ✓</li>
  </ul>
</div>

<h3 class="section-subheading">6.3 — Largest Rectangle in Histogram</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// Largest Rectangle in Histogram — O(n) with sentinel
int largestRectangleArea(vector<int>& heights) {
    heights.push_back(0);  // sentinel: forces all bars to be popped
    stack<int> st;
    int maxArea = 0;
    for (int i = 0; i < heights.size(); i++) {
        while (!st.empty() && heights[i] < heights[st.top()]) {
            int h = heights[st.top()]; st.pop();
            int w = st.empty() ? i : i - st.top() - 1;
            maxArea = max(maxArea, h * w);
        }
        st.push(i);
    }
    return maxArea;
}
{% endhighlight %}
</div>
</div>

<!-- ═══════════════════════ Section 7 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 7 — Pattern: Monotonic Deque (Sliding Window Maximum)</h2>
<p>For a fixed-size sliding window of size k, maintain a <strong>monotonic decreasing deque of indices</strong>. The front always holds the index of the maximum element in the current window.</p>

<div class="dsa-pattern-box">
  <ul>
    <li>Remove from front if the front index is out of the current window (index &lt; i–k+1)</li>
    <li>Remove from back while the back element is ≤ new element (smaller elements can never be the window max)</li>
    <li>Push new index to back; front of deque = index of the window maximum</li>
  </ul>
</div>

<div class="ch-code-wrap">
{% highlight cpp %}
// Sliding Window Maximum — O(n) time, O(k) space
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> dq;   // indices, front = index of max in window
    vector<int> ans;
    for (int i = 0; i < nums.size(); i++) {
        // Remove indices outside window
        while (!dq.empty() && dq.front() < i-k+1) dq.pop_front();
        // Remove smaller elements from back (they can never be max)
        while (!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();
        dq.push_back(i);
        if (i >= k-1) ans.push_back(nums[dq.front()]); // window full
    }
    return ans;
}
{% endhighlight %}
</div>
<div class="ch-cplx-row">
  <span class="ch-cplx"><span>Time</span>O(n)</span>
  <span class="ch-cplx"><span>Space</span>O(k)</span>
</div>
</div>

<!-- ═══════════════════════ Section 8 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 8 — Common Mistakes & Edge Cases</h2>

<div class="pattern-summary">
  <div class="pattern-card"><h4>❌ top() on empty stack</h4><p>Always check <code>st.empty()</code> before <code>st.top()</code> or <code>st.pop()</code>. Empty access = undefined behaviour / runtime crash.</p></div>
  <div class="pattern-card"><h4>❌ pop() returns void</h4><p>C++ STL <code>stack::pop()</code> does NOT return the value. Use <code>st.top()</code> to read, then <code>st.pop()</code> to remove.</p></div>
  <div class="pattern-card"><h4>❌ Stack for BFS</h4><p>Stack gives DFS. BFS requires a queue (FIFO). Mixing them gives wrong shortest-path results.</p></div>
  <div class="pattern-card"><h4>❌ Not checking empty at end</h4><p>Valid Parentheses: return <code>st.empty()</code>, not <code>true</code>. Input "(((" leaves stack non-empty → invalid.</p></div>
  <div class="pattern-card"><h4>❌ Values not indices in mono-stack</h4><p>Monotonic stack must store <strong>indices</strong> to compute distances and record answers at the right array position.</p></div>
  <div class="pattern-card"><h4>❌ Wrong monotonicity direction</h4><p>Next Greater → decreasing stack (pop when arr[i] > arr[top]). Next Smaller → increasing stack. Swapping gives wrong answers.</p></div>
</div>

<div class="insight-box">
  <span class="insight-label">Edge Cases to Test</span>
  <ul>
    <li>Empty string for bracket matching → return <code>true</code></li>
    <li>Single bracket <code>'('</code> → invalid</li>
    <li>Temperatures all equal [5,5,5,5] → strictly greater condition never fires → all answers = 0</li>
    <li>k=1 for sliding window → each element is its own window max</li>
    <li>k=n for sliding window → single result = global maximum</li>
  </ul>
</div>
</div>

<!-- ═══════════════════════ Section 9 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Practice Problems</h2>

<div class="ch-section-label">Stack Problems</div>
<div class="ch-ed-problems">
<table>
  <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><a href="https://leetcode.com/problems/valid-parentheses/" target="_blank">20. Valid Parentheses</a></td><td>Bracket matching</td><td class="diff-easy">Easy</td></tr>
    <tr><td>2</td><td><a href="https://leetcode.com/problems/min-stack/" target="_blank">155. Min Stack</a></td><td>Auxiliary min-tracking stack</td><td class="diff-medium">Medium</td></tr>
    <tr><td>3</td><td><a href="https://leetcode.com/problems/evaluate-reverse-polish-notation/" target="_blank">150. Evaluate Reverse Polish Notation</a></td><td>Postfix expression evaluation</td><td class="diff-medium">Medium</td></tr>
    <tr><td>4</td><td><a href="https://leetcode.com/problems/decode-string/" target="_blank">394. Decode String</a></td><td>Nested encoding — two stacks</td><td class="diff-medium">Medium</td></tr>
    <tr><td>5</td><td><a href="https://leetcode.com/problems/implement-queue-using-stacks/" target="_blank">232. Implement Queue using Stacks</a></td><td>Two stacks + lazy transfer</td><td class="diff-easy">Easy</td></tr>
  </tbody>
</table>
</div>

<div class="ch-section-label" style="margin-top:1.5rem;">Monotonic Stack Problems</div>
<div class="ch-ed-problems">
<table>
  <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr></thead>
  <tbody>
    <tr><td>6</td><td><a href="https://leetcode.com/problems/daily-temperatures/" target="_blank">739. Daily Temperatures</a></td><td>Decreasing stack (days to wait)</td><td class="diff-medium">Medium</td></tr>
    <tr><td>7</td><td><a href="https://leetcode.com/problems/next-greater-element-i/" target="_blank">496. Next Greater Element I</a></td><td>Monotonic stack + hash map</td><td class="diff-easy">Easy</td></tr>
    <tr><td>8</td><td><a href="https://leetcode.com/problems/next-greater-element-ii/" target="_blank">503. Next Greater Element II</a></td><td>Circular array — scan 2n</td><td class="diff-medium">Medium</td></tr>
    <tr><td>9</td><td><a href="https://leetcode.com/problems/largest-rectangle-in-histogram/" target="_blank">84. Largest Rectangle in Histogram</a></td><td>Increasing stack + sentinel</td><td class="diff-hard">Hard</td></tr>
    <tr><td>10</td><td><a href="https://leetcode.com/problems/trapping-rain-water/" target="_blank">42. Trapping Rain Water</a></td><td>Monotonic stack or two-pointer</td><td class="diff-hard">Hard</td></tr>
  </tbody>
</table>
</div>

<div class="ch-section-label" style="margin-top:1.5rem;">Queue & Deque Problems</div>
<div class="ch-ed-problems">
<table>
  <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr></thead>
  <tbody>
    <tr><td>11</td><td><a href="https://leetcode.com/problems/sliding-window-maximum/" target="_blank">239. Sliding Window Maximum</a></td><td>Monotonic deque — O(n)</td><td class="diff-hard">Hard</td></tr>
    <tr><td>12</td><td><a href="https://leetcode.com/problems/binary-tree-level-order-traversal/" target="_blank">102. Binary Tree Level Order Traversal</a></td><td>BFS with queue</td><td class="diff-medium">Medium</td></tr>
    <tr><td>13</td><td><a href="https://leetcode.com/problems/rotting-oranges/" target="_blank">994. Rotting Oranges</a></td><td>Multi-source BFS with queue</td><td class="diff-medium">Medium</td></tr>
  </tbody>
</table>
</div>
</div>

</div><!-- end .chapter-content -->

<div class="chapter-nav-footer">
  <a href="{{ '/learning/dsa/linked-list/ch3-linked-lists/' | relative_url }}" class="ch-nav-footer-btn">← Ch3: Linked Lists</a>
  <a href="{{ '/learning/dsa/tree/ch5-trees-graphs/' | relative_url }}" class="ch-nav-footer-btn primary">Next: Ch5 — Trees & Graphs →</a>
</div>
