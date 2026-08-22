---
title: "Two Pointers"
description: "Two Pointers Technique Summary: The two pointers technique is a powerful pattern for solving array and string problems efficiently."
domain: dsa
order: 0
ownHeader: true
url: /learning/dsa/arrays/two-pointers/
---

# <img src="/assets/icons/rocket.svg" class="inline-icon" alt=""> Two Pointers Technique

<div style="background:#f8fafc;border-radius:8px;padding:1.2em 1.5em 1.2em 1.5em;margin-bottom:1.5em;box-shadow:0 2px 8px #e2e8f0;">
<strong>Summary:</strong> The <b>two pointers</b> technique is a powerful pattern for solving array and string problems efficiently. By using two indices that move independently, you can often reduce time complexity from <b>O(n²)</b> to <b>O(n)</b>.
</div>

## What is the Two Pointers Technique?

Two pointers is a general approach where you use two indices (or iterators) to traverse a data structure, usually an array or string. The pointers can move in the same or opposite directions, or even on different arrays.

<div style="margin-bottom:1em;"><b>When to use:</b> When you need to search for pairs, subarrays, substrings, or perform in-place modifications efficiently.</div>

---

## 🧩 Common Two Pointers Patterns

1. <b>Opposite Direction Pointers (Left + Right)</b>
   - <i>When:</i> Array/string is sorted, looking for a pair that satisfies a condition.
   - <i>Example:</i> Two Sum in Sorted Array, Container With Most Water, Valid Palindrome, Reverse a string/linked list.
   - <b>Template:</b>
     ```cpp
     int l = 0, r = n - 1;
     while (l < r) {
         // Check condition
         if (arr[l] + arr[r] == target) return true;
         if (arr[l] + arr[r] < target) l++;
         else r--;
     }
     ```

2. <b>Sliding Window (Two Pointers in Same Direction)</b>
   - <i>When:</i> You need a window that grows/shrinks (e.g., substring/subarray problems).
   - <i>Example:</i> Largest substring without repeating characters, Minimum window substring, Subarray sum constraints.
   - <b>Template:</b>
     ```cpp
     int l = 0;
     for (int r = 0; r < n; r++) {
         // expand window by including arr[r]
         while (window violates condition) {
             // shrink from left
             l++;
         }
         // update answer
     }
     ```
   - <a href="/learning/dsa/arrays/sliding-window/">More on Sliding Window &rarr;</a>

3. <b>Fast & Slow Pointers (Tortoise & Hare)</b>
   - <i>When:</i> Detecting cycles, finding the middle, removing Nth node from end, etc.
   - <b>Template:</b>
     ```cpp
     ListNode* slow = head;
     ListNode* fast = head;
     while (fast && fast->next) {
         slow = slow->next;
         fast = fast->next->next;
     }
     ```

4. <b>Same Direction but With Gap / K-distance Pointers</b>
   - <i>When:</i> Removing duplicates, merging sorted arrays, comparing substrings, k-distance apart comparisons.
   - <b>Template:</b>
     ```cpp
     int i = 0;
     for (int j = 0; j < n; j++) {
         if (arr[j] != arr[i]) {
             i++;
             arr[i] = arr[j];
         }
     }
     ```

5. <b>Two Pointers on Two Arrays</b>
   - <i>When:</i> Merging sorted arrays, intersection, comparing two sequences.
   - <b>Template:</b>
     ```cpp
     int i = 0, j = 0;
     while (i < n && j < m) {
         if (a[i] == b[j]) { ... i++; j++; }
         else if (a[i] < b[j]) i++;
         else j++;
     }
     ```

---

## 🚩 Key Takeaways

- Two pointers is a versatile pattern for many array and string problems.
- It helps reduce time and space complexity.
- Patterns include opposite direction, sliding window, fast/slow, k-gap, and two arrays.
- Mastering these unlocks efficient solutions to many classic problems.

---


---

## ⭐ Must Do Problems

### Level 1 — Basics

<div class="problems-grid">
<!-- Valid Palindrome -->
<div class="problem-card-easy">
    <span class="problem-number">125</span>
    <span class="problem-status solved">✓ Solved</span>
    <h3>Valid Palindrome</h3>
    <div class="problem-buttons">
        <a href="https://leetcode.com/problems/valid-palindrome/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-problem">🔗 Problem</a>
        <a href="https://leetcode.com/problems/valid-palindrome/solutions/7386854/efficient-on-palindrome-check-using-two-yt59z/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-solution">💻 Solution</a>
    </div>
</div>
<!-- Remove Duplicates from Sorted Array -->
<div class="problem-card-easy">
    <span class="problem-number">26</span>
    <span class="problem-status solved">✓ Solved</span>
    <h3>Remove Duplicates from Sorted Array</h3>
    <div class="problem-buttons">
        <a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-problem">🔗 Problem</a>
        <a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/7389802/remove-duplicates-from-sorted-array-in-p-jar9/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-solution">💻 Solution</a>
    </div>
</div>
</div>

### Level 2 — Medium

<div class="problems-grid">
<!-- Two Sum II - Input Array Is Sorted -->
<div class="problem-card-medium">
    <span class="problem-number">167</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <h3>Two Sum II - Input Array Is Sorted</h3>
    <div class="problem-buttons">
        <a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-problem">🔗 Problem</a>
        <a href="/learning/dsa/arrays/two-pointers/leetcode-167.pdf" class="problem-btn-link btn-solution">💻 PDF Solution</a>
    </div>
</div>
<!-- 3Sum -->
<div class="problem-card-medium">
    <span class="problem-number">15</span>
    <span class="problem-status solved">✓ Solved</span>
    <h3>3Sum</h3>
    <div class="problem-buttons">
        <a href="https://leetcode.com/problems/3sum/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-problem">🔗 Problem</a>
        <a href="https://leetcode.com/problems/3sum/solutions/7388635/three-sum-using-sorting-two-pointers-c-o-r6ta/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-solution">💻 Solution</a>
    </div>
</div>
<!-- Container With Most Water -->
<div class="problem-card-medium">
    <span class="problem-number">11</span>
    <span class="problem-status solved">✓ Solved</span>
    <h3>Container With Most Water</h3>
    <div class="problem-buttons">
        <a href="https://leetcode.com/problems/container-with-most-water/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-problem">🔗 Problem</a>
        <a href="https://leetcode.com/problems/container-with-most-water/solutions/7388718/container-with-most-water-two-pointer-op-k9im/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-solution">💻 Solution</a>
    </div>
</div>
<!-- Next Permutation -->
<div class="problem-card-medium">
    <span class="problem-number">31</span>
    <span class="problem-status solved">✓ Solved</span>
    <h3>Next Permutation</h3>
    <div class="problem-buttons">
        <a href="https://leetcode.com/problems/next-permutation/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-problem">🔗 Problem</a>
        <a href="https://leetcode.com/problems/next-permutation/solutions/7389967/next-permutation-pivot-swap-reverse-on-o-ggbj/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-solution">💻 Solution</a>
    </div>
</div>
</div>

### Level 3 — Hard

<div class="problems-grid">
<!-- Trapping Rain Water -->
<div class="problem-card-hard">
    <span class="problem-number">42</span>
    <span class="problem-status solved">✓ Solved</span>
    <h3>Trapping Rain Water</h3>
    <div class="problem-buttons">
        <a href="https://leetcode.com/problems/trapping-rain-water/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-problem">🔗 Problem</a>
        <a href="https://leetcode.com/problems/trapping-rain-water/solutions/7388828/trapping-rain-water-prefixsuffix-max-app-zatc/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-solution">💻 Prefix/Suffix Max Solution</a>
        <a href="https://leetcode.com/problems/trapping-rain-water/solutions/7389700/trapping-rain-water-optimal-o1-space-two-snbg/" target="_blank" rel="noopener noreferrer" class="problem-btn-link btn-solution">💻 O(1) Space Two-Pointer</a>
    </div>
</div>
</div>


---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="/learning/dsa/arrays" style="display: inline-block; padding: 12px 28px; background: #667eea; color: white; border-radius: 8px; text-decoration: none; font-weight: 600; margin-right: 1rem;">← Back to Arrays</a>
  <a href="/learning/dsa" style="display: inline-block; padding: 12px 28px; background: #764ba2; color: white; border-radius: 8px; text-decoration: none; font-weight: 600;">DSA Hub 🏠</a>
</div>

