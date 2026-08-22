---
title: "Searching Algorithms Master Guide"
description: "🔎 Searching Algorithms Master Guide Searching is a core topic in computer science and interviews."
domain: dsa
order: 99
url: /learning/dsa/searching-sorting/searching-guide/
---

# 🔎 Searching Algorithms Master Guide

Searching is a core topic in computer science and interviews. This guide covers all major searching techniques, templates, and must-do problems.

## 📑 Table of Contents
1. [Overview & Keywords](#overview--keywords)
2. [Must-Know Searching Algorithms](#must-know-searching-algorithms)
3. [Templates](#templates)
4. [Key Patterns](#key-patterns)
5. [Practice Problems](#practice-problems)

---

## Overview & Keywords

Searching is the process of finding an element or condition in a data structure. Common interview keywords:
- linear search
- binary search
- lower/upper bound
- search space
- monotonic function
- binary search on answer

---

## Must-Know Searching Algorithms

### ✅ Linear Search
- Scan each element until found
- Time: O(N)
- Works on unsorted data
- Simple, but rarely used in interviews

### ✅ Binary Search
- Search sorted array by halving search space
- Time: O(log N)
- Used for lower/upper bound, first/last occurrence, peak element, rotated array
- Binary search on answer: search space is monotonic, not always a direct array

### ✅ Advanced Binary Search
- Binary search on monotonic functions
- Used in allocation, scheduling, optimization problems

---

## Templates

### Linear Search
```cpp
int linearSearch(vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
```

### Binary Search (Basic)
```cpp
int binarySearch(vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
```

### Binary Search on Answer
```cpp
int solve(vector<int>& arr) {
    int left = min_possible, right = max_possible, answer = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (isValid(mid)) {
            answer = mid;
            right = mid - 1; // or left = mid + 1 for max
        } else {
            left = mid + 1;
        }
    }
    return answer;
}
```

---

## Key Patterns

| Pattern                | Use When                        | Example Problems                |
|-----------------------|----------------------------------|---------------------------------|
| Linear Search         | Unsorted, small data             | Find element in array           |
| Binary Search         | Sorted, monotonic, ranges        | First/last occurrence, peak     |
| Binary Search on Answer| Search space is monotonic        | Allocate books, Koko bananas    |

---

## Practice Problems

### Level 1 — Easy
<div class="problem-grid">
  <div class="problem-card">
    <span class="problem-number">704</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/binary-search/" target="_blank" rel="noopener noreferrer" class="problem-title">Binary Search</a>
      <a href="https://leetcode.com/problems/binary-search/solutions/7417731/binary-search-iterative-recursive/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">35</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/search-insert-position/" target="_blank" rel="noopener noreferrer" class="problem-title">Search Insert Position</a>
      <a href="/learning/dsa/searching-sorting/floorAndCeil.pdf" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 My Approach (PDF)</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">744</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/find-smallest-letter-greater-than-target/" target="_blank" rel="noopener noreferrer" class="problem-title">Find Smallest Letter Greater Than Target</a>
      <a href="/learning/dsa/searching-sorting/floorAndCeil.pdf" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 Ceil Approach (PDF)</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">169</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/majority-element/" target="_blank" rel="noopener noreferrer" class="problem-title">Majority Element</a>
      <a href="https://leetcode.com/problems/majority-element/solutions/7418398/majority-element-step-by-step-intuition-woccs/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
</div>

### Level 2 — Medium
<div class="problem-grid">
  <div class="problem-card">
    <span class="problem-number">34</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/" target="_blank" rel="noopener noreferrer" class="problem-title">Find First and Last Position</a>
      <a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/7403935/two-binary-searches-to-locate-target-ran-6k3i/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">540</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/single-element-in-a-sorted-array/" target="_blank" rel="noopener noreferrer" class="problem-title">Single Element in a Sorted Array</a>
      <a href="https://leetcode.com/problems/single-element-in-a-sorted-array/solutions/7404225/single-element-in-a-sorted-array-parity-ktevy/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">gfg</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://www.geeksforgeeks.org/dsa/find-rotation-count-rotated-sorted-array/" target="_blank" rel="noopener noreferrer" class="problem-title">Rotation Count in Rotated Sorted Array</a>
      <a href="/learning/dsa/searching-sorting/Kth_rotation.pdf" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 My Approach (PDF)</a>
      <a href="/learning/dsa/searching-sorting/Kth_rotation.cpp" target="_blank" rel="noopener noreferrer" class="problem-btn">💻 Solution (Code)</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">153</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/" target="_blank" rel="noopener noreferrer" class="problem-title">Find Minimum in Rotated Sorted Array</a>
      <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/7407426/binary-search-to-locate-rotation-point-o-vh1h/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">33</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/" target="_blank" rel="noopener noreferrer" class="problem-title">Search in Rotated Sorted Array</a>
      <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/7407549/search-in-rotated-sorted-array-find-rota-q0h3/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">gfg</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://www.geeksforgeeks.org/dsa/find-position-element-sorted-array-infinite-numbers/" target="_blank" rel="noopener noreferrer" class="problem-title">Find Position in Infinite Sorted Array</a>
      <a href="/learning/dsa/searching-sorting/bsOnInfiniteNum.pdf" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 My Approach (PDF)</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">gfg</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://www.geeksforgeeks.org/dsa/find-index-first-1-infinite-sorted-array-0s-1s/" target="_blank" rel="noopener noreferrer" class="problem-title">Index of First 1 in Infinite Binary Array</a>
      <a href="/learning/dsa/searching-sorting/firstOneInBinaryInfiniteArray.pdf" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 My Approach (PDF)</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">162</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/find-peak-element/" target="_blank" rel="noopener noreferrer" class="problem-title">Find Peak Element</a>
      <a href="https://leetcode.com/problems/find-peak-element/solutions/7413917/find-peak-element-binary-search-on-slope-sjc3/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">852</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/peak-index-in-a-mountain-array/" target="_blank" rel="noopener noreferrer" class="problem-title">Peak Index in Mountain Array</a>
      <a href="https://leetcode.com/problems/peak-index-in-a-mountain-array/solutions/7413977/binary-search-on-increasingdecreasing-sl-w36n/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">gfg</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://www.geeksforgeeks.org/dsa/search-in-row-wise-and-column-wise-sorted-matrix/" target="_blank" rel="noopener noreferrer" class="problem-title">Search in Row & Column Wise Sorted Matrix</a>
      <a href="/learning/dsa/searching-sorting/searchInSortedMatrix.pdf" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 Approach (PDF)</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">74</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/search-a-2d-matrix/" target="_blank" rel="noopener noreferrer" class="problem-title">Search a 2D Matrix</a>
      <a href="https://leetcode.com/problems/search-a-2d-matrix/solutions/7415712/search-a-2d-matrix-double-binary-search-01x4d/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">gfg</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://www.geeksforgeeks.org/dsa/allocate-minimum-number-pages/" target="_blank" rel="noopener noreferrer" class="problem-title">Allocate Minimum Pages</a>
      <a href="/learning/dsa/searching-sorting/allocateMinimumPages/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 My Approach (MD)</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">875</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/koko-eating-bananas/" target="_blank" rel="noopener noreferrer" class="problem-title">Koko Eating Bananas</a>
      <a href="https://leetcode.com/problems/koko-eating-bananas/solutions/7429088/binary-search-on-eating-speed-efficient-6ydvw/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
      <a href="/learning/dsa/searching-sorting/koko-banana.pdf" target="_blank" rel="noopener noreferrer" class="problem-btn">📊 Example Visuals (PDF)</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">981</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/time-based-key-value-store/" target="_blank" rel="noopener noreferrer" class="problem-title">Time Based Key-Value Store</a>
      <a href="https://leetcode.com/problems/time-based-key-value-store/solutions/7429283/time-based-key-value-store-hashmap-order-k75k/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
</div>

### Level 3 — Hard
<div class="problem-grid">
  <div class="problem-card">
    <span class="problem-number">1095</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/find-in-mountain-array/" target="_blank" rel="noopener noreferrer" class="problem-title">Find in Mountain Array</a>
      <a href="https://leetcode.com/problems/find-in-mountain-array/solutions/7414067/binary-search-on-mountain-array-find-pea-s9fz/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">4</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/median-of-two-sorted-arrays/" target="_blank" rel="noopener noreferrer" class="problem-title">Median of Two Sorted Arrays</a>
      <a href="https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/7430537/median-of-two-sorted-arrays-binary-searc-hjg4/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
      <a href="/learning/dsa/searching-sorting/median-sorted-array.pdf" target="_blank" rel="noopener noreferrer" class="problem-btn">📊 Example Visuals (PDF)</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">410</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/split-array-largest-sum/" target="_blank" rel="noopener noreferrer" class="problem-title">Split Array Largest Sum</a>
    </div>
  </div>
</div>

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="/learning/dsa/searching-sorting" style="display: inline-block; padding: 12px 28px; background: #667eea; color: white; border-radius: 8px; text-decoration: none; font-weight: 600; margin-right: 1rem;">← Back to Searching & Sorting</a>
  <a href="/learning/dsa" style="display: inline-block; padding: 12px 28px; background: #764ba2; color: white; border-radius: 8px; text-decoration: none; font-weight: 600;">DSA Hub 🏠</a>
</div>
