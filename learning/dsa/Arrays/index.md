---
layout: default
title: Arrays
permalink: /learning/dsa/arrays/
---

---

## 📋 Executive Summary

**Document:** Arrays Mastery Guide  
**Type:** Technical Documentation  
**Reading Time:** ~12 min  
**Last Updated:** December 2025  

### 📊 Quick Stats

| Metric | Value |
|--------|-------|
| **Core Patterns** | 10 essential techniques |
| **Code Examples** | 25+ implementations |
| **Practice Problems** | 30+ curated questions |
| **Difficulty Range** | Easy to Hard |
| **Languages** | C++, Python, Java examples |

### 🎯 Main Topics Covered

1. **Array Fundamentals** — Traversal, searching, basic operations
2. **Sliding Window** — Fixed/variable size window problems
3. **Two Pointers** — Opposite/same direction techniques
4. **Prefix & Suffix Sums** — Cumulative computation tricks
5. **Binary Search** — On sorted arrays & answer space
6. **Kadane's Algorithm** — Maximum subarray problems
7. **Sorting + Greedy** — Combined pattern strategies
8. **Intervals** — Merge, insert, overlap problems
9. **Matrix Operations** — 2D array manipulations
10. **HashMap + Array** — Frequency counting optimizations

### 💡 What You'll Learn

- Master 10 core array patterns used in 90% of interview questions
- Recognize when to apply sliding window vs two pointers
- Implement binary search on answer space for optimization problems
- Use prefix sums to achieve O(1) range queries
- Apply Kadane's algorithm and its variations
- Solve interval problems with sorting-based approaches
- Optimize brute force solutions using hashmap techniques
- Handle edge cases and boundary conditions confidently

### 📚 Prerequisites

- Basic programming knowledge (loops, conditionals, functions)
- Understanding of Big-O notation and time complexity
- Familiarity with arrays/lists in your chosen language
- Basic knowledge of sorting algorithms

### 👥 Target Audience

✅ **Interview Candidates** — Preparing for FAANG/tech company interviews  
✅ **CS Students** — Learning data structures and algorithms  
✅ **Competitive Programmers** — Building pattern recognition skills  
✅ **Self-Learners** — Strengthening algorithmic problem-solving  

### 🎓 Learning Path

**Beginner** → Start with patterns 1-4 (Sliding Window, Two Pointers, Prefix Sum)  
**Intermediate** → Add patterns 5-7 (Binary Search, Kadane's, Sorting+Greedy)  
**Advanced** → Master patterns 8-10 (Intervals, Matrix, HashMap combinations)  

---

# <img src="{{ '/assets/icons/rocket.svg' | relative_url }}" class="inline-icon" alt=""> Arrays Mastery Guide

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

## ⭐ Must-Do Array Problems - Practice

#### 1. [Leetcode 1. Two Sum](https://leetcode.com/problems/two-sum/description/){:target="_blank" rel="noopener noreferrer"}

#### 2. [Leetcode 217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/){:target="_blank" rel="noopener noreferrer"}

#### 3. [Leetcode 219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/description/){:target="_blank" rel="noopener noreferrer"}

#### 4. [Leetcode 242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/){:target="_blank" rel="noopener noreferrer"}

#### 5. [Leetcode 49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/){:target="_blank" rel="noopener noreferrer"}

#### 6. [Leetcode 238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/){:target="_blank" rel="noopener noreferrer"}

#### 7. [Leetcode 347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/){:target="_blank" rel="noopener noreferrer"}

#### 8. [Leetcode 13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/description/){:target="_blank" rel="noopener noreferrer"}

#### 9. [Leetcode 953. Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/description/){:target="_blank" rel="noopener noreferrer"}

#### 10. [Leetcode 128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/){:target="_blank" rel="noopener noreferrer"}

#### 11. [Leetcode 41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/description/){:target="_blank" rel="noopener noreferrer"}


## ⭐ Pattern → Template → Example

### 🔶 [Pattern 1: Sliding Window](sliding-window/index.md)

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


### 🔶 [Pattern 2: Two Pointers](two-pointers/index.md)

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
