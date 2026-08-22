---
title: "Ch3 — Linked Lists"
description: "All Roadmaps › DSA Mastery › Chapter 3 Chapter 3 · Intermediate · Prereq: Chapter 2 Linked Lists Singly & Doubly Linked · Fast & Slow Pointers · Reversal · Merge · Cycle…"
domain: dsa
track: dsa-mastery
order: 3
chrome: bare
ownHeader: true
url: /learning/dsa/linked-list/ch3-linked-lists/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<div class="chapter-hero">
  <div class="chapter-hero-inner">
    <div class="ch-hero-breadcrumb">
      <a href="/roadmap/">All Roadmaps</a> ›
      <a href="/learning/dsa/dsa-roadmap/">DSA Mastery</a> ›
      Chapter 3
    </div>
    <div class="chapter-num-badge">Chapter 3 · Intermediate · Prereq: Chapter 2</div>
    <h1>Linked Lists</h1>
    <p class="chapter-hero-sub">Singly & Doubly Linked · Fast & Slow Pointers · Reversal · Merge · Cycle Detection — pointer manipulation patterns that appear in 30% of interview problems.</p>
    <div class="chapter-meta-row">
      <span class="ch-meta-pill teal">11 Sections</span>
      <span class="ch-meta-pill">11 Practice Problems</span>
      <span class="ch-meta-pill">Intermediate</span>
      <a href="/learning/dsa/dsa-roadmap/#ch3" class="ch-nav-btn">← Back to Roadmap</a>
    </div>
  </div>
</div>
<div class="chapter-content">
<div class="chapter-section">
<h2 class="section-heading">Section 1 — What Is a Linked List?</h2>
<p>A linked list is a linear data structure where each element (node) stores a value and a pointer to the next node. Unlike arrays, nodes are <strong>not stored contiguously in memory</strong> — they can be scattered anywhere on the heap, connected only by pointers.</p>
<div class="insight-box">
  <span class="insight-label">Real-World Analogy: A Treasure Hunt</span>
  Each note (node) contains a clue (data) and the location of the next note (pointer). To reach clue #5, you must follow all 4 previous clues — there is no shortcut.
</div>
<h3 class="section-subheading">1.1 — Node Structure</h3>
<div class="ch-code-wrap">
```cpp
// Singly linked list node
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};
// Doubly linked list node (for LRU Cache, deque)
struct DListNode {
    int key, val;
    DListNode* prev;
    DListNode* next;
    DListNode(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
};
```
</div>
<h3 class="section-subheading">1.2 — Complexity vs Arrays</h3>
<div class="insight-box">
  <ul>
    <li><strong>Access by index:</strong> O(n) — must traverse from head. (Arrays: O(1))</li>
    <li><strong>Search:</strong> O(n) — both structures</li>
    <li><strong>Insert/Delete at known position:</strong> O(1) — just rewire pointers. (Arrays: O(n) — must shift)</li>
    <li><strong>Insert/Delete at unknown position:</strong> O(n) — must find position first</li>
    <li><strong>Memory:</strong> Extra pointer per node. No wasted capacity like dynamic arrays.</li>
  </ul>
  <strong>Use Linked List when:</strong> frequent insert/delete at known positions, implementing stacks, queues, or adjacency lists. Not for random access.
</div>
</div>
<div class="chapter-section">
<h2 class="section-heading">Section 2 — Pattern: Fast & Slow Pointers (Floyd's Algorithm)</h2>
<p>Two pointers move through the list at different speeds — fast moves 2 nodes per step, slow moves 1. They meet at meaningful positions.</p>
<div class="pattern-summary">
  <div class="pattern-card"><h4>Find Middle</h4><p>When fast reaches end, slow is at middle. Use for palindrome check, merge sort on linked list.</p></div>
  <div class="pattern-card"><h4>Cycle Detection</h4><p>If fast and slow meet, there's a cycle. If fast hits nullptr, no cycle.</p></div>
  <div class="pattern-card"><h4>Kth from End</h4><p>Advance fast k steps first, then move both. When fast hits null, slow = kth from end.</p></div>
</div>
<div class="ch-code-wrap">
<span class="ch-code-label">Fast/Slow pointer templates</span>
```cpp
// Find middle — slow stops at middle
ListNode *slow = head, *fast = head;
while (fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;
}
// slow = middle (left-middle for even length)

// Cycle detection (Floyd's)
ListNode *slow = head, *fast = head;
while (fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;
    if (slow == fast) return true; // cycle detected
}
return false;

// Kth node from end (two-pointer with gap k)
ListNode *fast = head, *slow = head;
for (int i = 0; i < k; i++) fast = fast->next; // advance fast by k
while (fast) { slow = slow->next; fast = fast->next; }
// slow = kth node from end
```
</div>
<div class="ch-cplx-row">
  <span class="ch-cplx"><span>Time</span>O(n)</span>
  <span class="ch-cplx"><span>Space</span>O(1)</span>
</div>
</div>
<div class="chapter-section">
<h2 class="section-heading">Section 3 — Pattern: Reversal</h2>
<p>Reversing a linked list is O(n) time, O(1) space. Requires tracking three pointers: prev, curr, and next.</p>
<div class="insight-box">
  <span class="insight-label">The 3-Pointer Dance</span>
  Before breaking the link curr→next, save next first. Then redirect curr→prev. Advance: prev=curr, curr=next. Repeat until curr=nullptr. Return prev (new head).
</div>
<div class="ch-code-wrap">
```cpp
// Reverse entire list — iterative (preferred)
ListNode* reverseList(ListNode* head) {
    ListNode *prev = nullptr, *curr = head;
    while (curr) {
        ListNode* nxt = curr->next;   // save next
        curr->next = prev;            // redirect
        prev = curr;                  // advance prev
        curr = nxt;                   // advance curr
    }
    return prev; // new head
}
// Reverse a sublist from position left to right
// (0-indexed) — use dummy node + find boundaries
ListNode dummy(0); dummy.next = head;
ListNode* pre = &dummy;
for (int i = 0; i < left-1; i++) pre = pre->next; // node before sublist
ListNode* curr = pre->next;
for (int i = 0; i < right-left; i++) {
    ListNode* nxt = curr->next;
    curr->next = nxt->next;
    nxt->next = pre->next;
    pre->next = nxt;
}
return dummy.next;
```
</div>
<div class="ch-cplx-row">
  <span class="ch-cplx"><span>Time</span>O(n)</span>
  <span class="ch-cplx"><span>Space</span>O(1)</span>
</div>
</div>
<div class="chapter-section">
<h2 class="section-heading">Section 4 — Pattern: Dummy Node</h2>
<p>Adding a dummy node before the head eliminates edge-case handling for empty lists or removing the head node. Always return dummy.next as the real head.</p>
<div class="insight-box">
  Return <code>dummy.next</code> at the end, not <code>head</code> — the head may have been removed or changed.
</div>
<div class="ch-code-wrap">
```cpp
// Remove nth node from end — dummy + two pointers
ListNode dummy(0); dummy.next = head;
ListNode *fast = &dummy, *slow = &dummy;
for (int i = 0; i <= n; i++) fast = fast->next; // gap of n+1
while (fast) { slow = slow->next; fast = fast->next; }
slow->next = slow->next->next; // remove target
return dummy.next;

// Delete node with specific value — dummy prevents head case
ListNode dummy(0); dummy.next = head;
ListNode* curr = &dummy;
while (curr->next) {
    if (curr->next->val == val) curr->next = curr->next->next;
    else curr = curr->next;
}
return dummy.next;
```
</div>
</div>
<div class="chapter-section">
<h2 class="section-heading">Section 5 — Pattern: Merge Two Sorted Lists</h2>
<p>Compare heads of both lists. Take the smaller one, advance that pointer. Use a dummy node to avoid edge cases.</p>
<div class="ch-code-wrap">
```cpp
// Merge two sorted linked lists — O(m+n) time, O(1) space
ListNode dummy(0); ListNode* tail = &dummy;
while (l1 && l2) {
    if (l1->val <= l2->val) { tail->next = l1; l1 = l1->next; }
    else                    { tail->next = l2; l2 = l2->next; }
    tail = tail->next;
}
tail->next = l1 ? l1 : l2; // attach remaining
return dummy.next;
```
</div>
</div>
<div class="chapter-section">
<h2 class="section-heading">Section 6 — Hard Pattern: Reorder List</h2>
<p>Combines multiple patterns: find middle (fast/slow), reverse second half, then merge two halves. L0→L1→…→Ln becomes L0→Ln→L1→Ln-1→L2→…</p>
<div class="ch-code-wrap">
```cpp
// Reorder List — O(n) time, O(1) space
void reorderList(ListNode* head) {
    // 1. Find middle
    ListNode *slow = head, *fast = head;
    while (fast->next && fast->next->next)
        { slow = slow->next; fast = fast->next->next; }
    // 2. Reverse second half
    ListNode *prev = nullptr, *curr = slow->next;
    slow->next = nullptr; // cut list at middle
    while (curr) { ListNode* nxt = curr->next; curr->next = prev; prev = curr; curr = nxt; }
    // 3. Interleave first half and reversed second half
    ListNode *first = head, *second = prev;
    while (second) {
        ListNode *fn = first->next, *sn = second->next;
        first->next = second; second->next = fn;
        first = fn; second = sn;
    }
}
```
</div>
</div>
<div class="chapter-section">
<h2 class="section-heading">Practice Problems</h2>
<div class="ch-ed-problems">
<table>
  <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><a href="https://leetcode.com/problems/middle-of-the-linked-list/" target="_blank">876. Middle of the Linked List</a></td><td>Fast/Slow</td><td class="diff-easy">Easy</td></tr>
    <tr><td>2</td><td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list/" target="_blank">83. Remove Duplicates from Sorted List</a></td><td>Traversal + pointer redirect</td><td class="diff-easy">Easy</td></tr>
    <tr><td>3</td><td><a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank">206. Reverse Linked List</a></td><td>Reversal (iterative)</td><td class="diff-easy">Easy</td></tr>
    <tr><td>4</td><td><a href="https://leetcode.com/problems/reverse-linked-list-ii/" target="_blank">92. Reverse Linked List II</a></td><td>Reversal (sublist)</td><td class="diff-medium">Medium</td></tr>
    <tr><td>5</td><td><a href="https://leetcode.com/problems/linked-list-cycle/" target="_blank">141. Linked List Cycle</a></td><td>Fast/Slow cycle detection</td><td class="diff-easy">Easy</td></tr>
    <tr><td>6</td><td><a href="https://leetcode.com/problems/merge-two-sorted-lists/" target="_blank">21. Merge Two Sorted Lists</a></td><td>Merge + dummy node</td><td class="diff-easy">Easy</td></tr>
    <tr><td>7</td><td><a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/" target="_blank">19. Remove Nth Node From End of List</a></td><td>Dummy + two-pointer gap</td><td class="diff-medium">Medium</td></tr>
    <tr><td>8</td><td><a href="https://leetcode.com/problems/add-two-numbers/" target="_blank">2. Add Two Numbers</a></td><td>Simultaneous traversal + carry</td><td class="diff-medium">Medium</td></tr>
    <tr><td>9</td><td><a href="https://leetcode.com/problems/reorder-list/" target="_blank">143. Reorder List</a></td><td>Three-part: mid + reverse + merge</td><td class="diff-medium">Medium</td></tr>
    <tr><td>10</td><td><a href="https://leetcode.com/problems/lru-cache/" target="_blank">146. LRU Cache</a></td><td>Doubly linked list + HashMap</td><td class="diff-medium">Medium</td></tr>
    <tr><td>11</td><td><a href="https://leetcode.com/problems/merge-k-sorted-lists/" target="_blank">23. Merge K Sorted Lists</a></td><td>K-way merge (min-heap)</td><td class="diff-hard">Hard</td></tr>
  </tbody>
</table>
</div>
</div>
</div><!-- end .chapter-content -->
<div class="chapter-nav-footer">
  <a href="/learning/dsa/hashing/ch2-hashing/" class="ch-nav-footer-btn">← Ch2: Hashing</a>
  <a href="/learning/dsa/dsa-roadmap/#ch4" class="ch-nav-footer-btn primary">Next: Ch4 — Stacks & Queues →</a>
</div>
