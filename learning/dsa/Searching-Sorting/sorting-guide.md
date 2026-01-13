---
layout: default
title: Sorting Algorithms Master Guide
permalink: /learning/dsa/Searching-Sorting/sorting-guide/
---

# 🧮 Sorting Algorithms Master Guide

Sorting is a foundational topic in computer science and interviews. Mastering sorting means understanding the intuition, implementation, and use-cases for each algorithm.

## 📑 Table of Contents
1. [Overview & Keywords](#overview--keywords)
2. [Must-Know Sorting Algorithms](#must-know-sorting-algorithms)
3. [Templates](#templates)
4. [Key Patterns](#key-patterns)
5. [Practice Problems](#practice-problems)

---

## Overview & Keywords

Sorting is the process of arranging data in a particular order (ascending/descending). Common interview keywords:
- stable
- adaptive
- in-place
- time/space complexity
- custom comparator
- hybrid sort

---

## Must-Know Sorting Algorithms

### 🔶 Selection Sort
- Simple, conceptual warmup
- Time: O(N²), Space: O(1)
- Not stable, not adaptive
- Rarely used except for teaching

### 🔶 Bubble Sort
- Swap adjacent elements until sorted
- Time: O(N²), Space: O(1)
- Stable, adaptive (with optimization)
- Rarely used in practice

### 🔶 Insertion Sort
- Insert each element into its correct position
- Time: O(N²), Space: O(1), Best: O(N) for nearly sorted
- Stable, adaptive
- Used in TimSort, C++ STL hybrid sorts

### 🔶 Merge Sort
- Divide & conquer, merge sorted halves
- Time: O(N log N), Space: O(N)
- Stable, not in-place
- Used in stable_sort(), linked lists

### 🔶 Quick Sort
- Partition, recursively sort
- Time: Avg O(N log N), Worst O(N²)
- In-place, not stable
- Used in C++ STL sort() (as part of Introsort)

### 🔶 Heap Sort
- Build heap, extract max/min
- Time: O(N log N), Space: O(1)
- Not stable
- Used in priority queue, top-K problems

### 🔶 Counting Sort
- For small, bounded integer ranges
- Time: O(N + K), Space: O(K)
- Not comparison-based

### 🔶 Bucket Sort
- For uniformly distributed input
- Used in max gap, sorting floats

### 🔶 Radix Sort
- For integers/strings
- Time: O(d * (N + K))
- Used in phone number sorting, large datasets

---

## Templates

### Selection Sort
```cpp
void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) minIndex = j;
        }
        swap(arr[i], arr[minIndex]);
    }
}
```

### Merge Sort
```cpp
void mergeSort(vector<int>& arr, int l, int r) {
    if (l >= r) return;
    int mid = l + (r - l) / 2;
    mergeSort(arr, l, mid);
    mergeSort(arr, mid+1, r);
    merge(arr, l, mid, r);
}
```

### Quick Sort (Lomuto)
```cpp
int partition(vector<int>& a, int l, int r) {
    int pivot = a[r];
    int i = l;
    for (int j = l; j < r; j++) {
        if (a[j] < pivot) {
            swap(a[i], a[j]);
            i++;
        }
    }
    swap(a[i], a[r]);
    return i;
}
```

---

## Key Patterns

| Pattern         | Stable | Adaptive | In-place | Used In                |
|----------------|--------|----------|----------|------------------------|
| Selection Sort | ❌     | ❌       | ✅       | Teaching               |
| Bubble Sort    | ✅     | ✅       | ✅       | Teaching               |
| Insertion Sort | ✅     | ✅       | ✅       | TimSort, STL           |
| Merge Sort     | ✅     | ❌       | ❌       | stable_sort(), Linked  |
| Quick Sort     | ❌     | ❌       | ✅       | STL sort(), Introsort  |
| Heap Sort      | ❌     | ❌       | ✅       | Priority Queue         |
| Counting Sort  | ✅     | ❌       | ✅       | Bucket/Dutch Flag      |
| Bucket Sort    | ✅     | ❌       | ✅       | Max Gap, Floats        |
| Radix Sort     | ✅     | ❌       | ✅       | Phone Numbers, Strings |

---

## Practice Problems

### Level 1 — Basics
<div class="problem-grid">
  <div class="problem-card">
    <span class="problem-number">88</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/merge-sorted-array/" target="_blank" rel="noopener noreferrer" class="problem-title">Merge Sorted Array</a>
      <a href="https://leetcode.com/problems/merge-sorted-array/solutions/7417731/merge-sorted-array-in-place-backward-two-j35p/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
</div>

### Level 2 — Medium
<div class="problem-grid">
  <div class="problem-card">
    <span class="problem-number">148</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/sort-list/" target="_blank" rel="noopener noreferrer" class="problem-title">Sort List</a>
      <a href="https://leetcode.com/problems/sort-list/solutions/7428100/merge-sort-on-linked-list-on-log-n-time-v8lx2/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">179</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/largest-number/" target="_blank" rel="noopener noreferrer" class="problem-title">Largest Number</a>
      <a href="https://leetcode.com/problems/largest-number/solutions/7429080/largest-number-custom-sorting-by-concate-z4et/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">75</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/sort-colors/" target="_blank" rel="noopener noreferrer" class="problem-title">Sort Colors</a>
      <a href="https://leetcode.com/problems/sort-colors/solutions/7418299/sort-colors-dutch-national-flag-algorith-e7eo/" target="_blank" rel="noopener noreferrer" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
</div>

### Level 3 — Hard
<div class="problem-grid">
  <div class="problem-card">
    <span class="problem-number">23</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/merge-k-sorted-lists/" target="_blank" rel="noopener noreferrer" class="problem-title">Merge k Sorted Lists</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">315</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/count-of-smaller-numbers-after-self/" target="_blank" rel="noopener noreferrer" class="problem-title">Count of Smaller Numbers After Self</a>
    </div>
  </div>
  <div class="problem-card">
    <span class="problem-number">164</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/maximum-gap/" target="_blank" rel="noopener noreferrer" class="problem-title">Maximum Gap</a>
    </div>
  </div>
</div>

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/learning/dsa/Searching-Sorting/' | relative_url }}" style="display: inline-block; padding: 12px 28px; background: #667eea; color: white; border-radius: 8px; text-decoration: none; font-weight: 600; margin-right: 1rem;">← Back to Searching & Sorting</a>
  <a href="{{ '/learning/dsa' | relative_url }}" style="display: inline-block; padding: 12px 28px; background: #764ba2; color: white; border-radius: 8px; text-decoration: none; font-weight: 600;">DSA Hub 🏠</a>
</div>
