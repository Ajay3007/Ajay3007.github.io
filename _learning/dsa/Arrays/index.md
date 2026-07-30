---
layout: learning
title: Arrays
permalink: /learning/dsa/arrays/
---

# <img src="{{ '/assets/icons/rocket.svg' | relative_url }}" class="inline-icon" alt=""> Arrays Mastery Guide

Welcome to the complete hub for Array. Here you'll find guides, templates, and curated problems for interviews and mastery.

---

<div style="display:flex;flex-wrap:wrap;gap:2.2rem 2.5rem;justify-content:center;margin-bottom:2.5rem;">
  <!-- Sliding Window Card -->
  <div class="project-card" style="min-width:260px;max-width:340px;background:#f8fafc;border-radius:12px;box-shadow:0 2px 10px #e2e8f0;padding:1.7rem 1.2rem;text-align:center;">
    <span style="font-size:2.2rem;">🧮</span>
    <h3 style="margin:0.7rem 0 0.3rem 0;font-size:1.18rem;font-weight:700;">
      <a href="{{ '/learning/dsa/arrays/sliding-window/' | relative_url }}" style="color:#1976d2;text-decoration:none;">Sliding Window Technique</a>
    </h3>
    <div style="color:#607d8b;font-size:0.98rem;">Sliding Window is a fundamental technique used for solving problems involving contiguous subarrays or substrings.</div>
  </div>
  <!-- Two Pointer Technique -->
  <div class="project-card" style="min-width:260px;max-width:340px;background:#f8fafc;border-radius:12px;box-shadow:0 2px 10px #e2e8f0;padding:1.7rem 1.2rem;text-align:center;">
    <span style="font-size:2.2rem;">🔎</span>
    <h3 style="margin:0.7rem 0 0.3rem 0;font-size:1.18rem;font-weight:700;">
      <a href="{{ '/learning/dsa/arrays/two-pointers/' | relative_url }}" style="color:#1976d2;text-decoration:none;">Two Pointer Technique</a>
    </h3>
    <div style="color:#607d8b;font-size:0.98rem;">Two indices that move independently, reduce time complexity from O(n²) to O(n)</div>
  </div>
</div>

---


<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem; text-align: center;">
  <h2 style="color: white; margin: 0 0 1rem 0;">📋 Practice Problems</h2>
  <a href="{{ '/learning/dsa/arrays/arrays-problems/' | relative_url }}" style="display: inline-block; padding: 12px 30px; background: white; color: #667eea; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 1.1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    ⚡ View All Arrays Problems →
  </a>
  <!-- <p style="color: rgba(255,255,255,0.9); margin: 1rem 0 0 0; font-size: 0.95rem;">22 curated problems with solutions • All Solved! 🎉</p> -->
</div>

---

## ⭐ 1. Array Concepts You Must Master
### 🔹 Basic Operations

- Traversal

- Searching

- Prefix sums

- Suffix sums

- Sorting techniques

- Using hash maps to optimize

### 🔹 Core Patterns

**Arrays revolve around 10 major patterns:**

**1. Sliding Window**

**2. Two Pointers**

**3. Prefix Sum**

**4. Binary Search on Sorted Array**

**5. Binary Search on Answer**

**6. Kadane's Algorithm**

**7. Sorting + Greedy**

**8. Intervals**

**9. Matrix as Array of Arrays**

**10. Hashmap + Array Combo**

We will cover each with template + example.


## ⭐ Pattern → Template → Example

### 🔶 [Pattern 1: Sliding Window](/learning/dsa/arrays/sliding-window)

Sliding Window is used when we deal with **contiguous subarrays or substrings**.

#### 📌 Template (Variable-size window)

```cpp
int left = 0;
for (int right = 0; right < n; right++) {
    // expand window using arr[right]

    while (window_invalid) {
        // shrink window
        left++;
    }

    // track best window
}
```

#### 📘 Example

1. [Longest substring without repeating characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/){:target="_blank" rel="noopener noreferrer"}


### 🔶 [Pattern 2: Two Pointers](/learning/dsa/arrays/two-pointers)

Used when array is sorted, or when you're searching for pairs.

#### 📌 Template

```cpp
int left = 0, right = n - 1;

while (left < right) {
    int sum = arr[left] + arr[right];
    if (sum == target) { ... }
    else if (sum < target) left++;
    else right--;
}
```

#### 📘 Example

Two Sum (sorted)

3-sum

Container With Most Water

### 🔶 Pattern 3: Prefix Sum

Instant sum queries from index `l` to `r`.

#### 📌 Template

```cpp
vector<int> pref(n+1, 0);
for (int i = 0; i < n; i++) pref[i+1] = pref[i] + arr[i];

// sum of l..r
int sum = pref[r+1] - pref[l];
```

#### 📘 Example

Subarray sum equals K

Range sum queries

### 🔶 Pattern 4: Kadane's Algorithm

Max subarray sum in O(n).

#### 📌 Template

```cpp
int max_ending_here = 0, best = INT_MIN;

for (int x : arr) {
    max_ending_here = max(x, max_ending_here + x);
    best = max(best, max_ending_here);
}
```

### 🔶 Pattern 5: Sorting + Greedy

Used in:

Meeting rooms

Task scheduling

Minimum arrows to burst balloons

### 🔶 Pattern 6: Binary Search

Used on sorted arrays.

#### 📌 Standard Template

```cpp
int l = 0, r = n - 1;
while (l <= r) {
    int mid = l + (r - l) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) l = mid + 1;
    else r = mid - 1;
}
```

### 🔶 Pattern 7: Binary Search on Answer

Used when the array is not sorted but the answer lies in a monotonic search space.
#### Examples:

Koko eating bananas

Minimum pages allocation

Aggressive cows

### 🔶 Pattern 8: Intervals (Important!)

Many array problems are actually interval problems.

#### Steps:

1. Sort by start

2. Merge or process based on end

### 🔶 Pattern 9: Matrix as Array of Arrays

2D array concepts:

- Row-wise traversal

- Column-wise traversal

- Diagonal traversal

- Simulation problems

### 🔶 Pattern 10: Hashmap + Array Combo

Most-used pattern in arrays.

#### Examples:

- Two sum

- Group anagrams

- Top K frequent

- Subarray sum K

---

<div style="text-align:center;margin-top:2.5rem;">
  <a href="{{ '/learning/dsa' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#1976d2;color:white;text-decoration:none;border-radius:8px;font-weight:600;margin-right:1rem;">← Back to DSA</a>

  <a href="{{ '/' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#2d3748;color:white;text-decoration:none;border-radius:8px;font-weight:600;">🏠 Home</a>
</div>



