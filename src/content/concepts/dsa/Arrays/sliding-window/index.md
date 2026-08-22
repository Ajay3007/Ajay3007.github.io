---
title: "Sliding Window Technique"
description: "🪟 Sliding Window Technique Sliding Window is a fundamental technique used for solving problems involving contiguous subarrays or substrings ."
domain: dsa
order: 0
ownHeader: true
url: /learning/dsa/arrays/sliding-window/
---

# 🪟 Sliding Window Technique

Sliding Window is a fundamental technique used for solving problems involving **contiguous subarrays or substrings**. It optimizes problems that would otherwise require nested loops by maintaining a dynamic window that expands and contracts based on a condition.

## 📑 Table of Contents

1. [Overview & Keywords](#overview--keywords)
2. [Types of Sliding Window](#types-of-sliding-window)
3. [Core Templates](#core-templates)
4. [Key Patterns](#key-patterns)
5. [Practice Problems](#practice-problems)

---

## Overview & Keywords

**Common problem indicators:**
- longest / smallest
- maximum / minimum
- subarray / substring
- at most / at least K distinct
- average of size K
- contiguous elements

---

## Types of Sliding Window

### 1️⃣ Fixed-Size Window (size = K)

Use when **window size is constant**.

**Common Use Cases:**
- Max sum of subarray of size K
- First negative number in every window of size K
- Average of every subarray of size K

### 2️⃣ Variable-Size Window (Stretch/Shrink)

Use when **window grows and shrinks dynamically** based on a condition.

**Common Use Cases:**
- Longest substring without repeating characters
- Longest subarray with sum ≤ K
- Minimum window substring
- Fruits into baskets (at most K distinct elements)

---

## Core Templates

### 🔶 Template 1: Fixed Size Window

```cpp
int left = 0;
long long sum = 0, best = 0;

for (int right = 0; right < n; right++) {
    sum += arr[right]; // expand window

    if (right - left + 1 == K) {
        best = max(best, sum); // process window
        sum -= arr[left]; // shrink
        left++;
    }
}
```

### 🔶 Template 2: Variable Window (Universal)

```cpp
int left = 0;
for (int right = 0; right < n; right++) {
    // Add arr[right] to window

    while (window_condition_invalid) {
        // Shrink window from left
        left++;
    }

    // Update answer with current window [left, right]
}
```

### 🔶 Template 3: Frequency Map (Substring Problems)

```cpp
unordered_map<char, int> freq;
int left = 0;

for (int right = 0; right < s.size(); right++) {
    freq[s[right]]++;

    while (condition_invalid) {
        freq[s[left]]--;
        if (freq[s[left]] == 0) freq.erase(s[left]);
        left++;
    }

    ans = max(ans, right - left + 1);
}
```

---

## Key Patterns

| Pattern | Condition | Trigger | Use When |
|---------|-----------|---------|----------|
| **No Repeating** | Any char count > 1 | Shrink until all freq = 1 | Longest substring without repeating chars |
| **At Most K Distinct** | freq_map.size() > K | Shrink until size ≤ K | Max subarray with ≤ K distinct elements |
| **Sum ≤ Target** | sum > target | Shrink until sum ≤ target | Min subarray, max subarray with constraint |
| **Two Hash Maps** | Elements not in target | Shrink while valid | Minimum window substring |
| **Fixed Size** | window size = K | Always process at size K | Fixed window problems |

---

## Practice Problems

### 📋 Level 1 — Fundamentals

<div class="problem-grid">
  <div class="problem-card">
    <span class="problem-number">121</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/" target="_blank" rel="noopener noreferrer" class="problem-title">Best Time to Buy and Sell Stock</a>
      <a href="/learning/dsa/arrays/arrays-problems/#best-time-to-buy-and-sell-stock" class="problem-btn">📋 View Solution</a>
    </div>
  </div>

  <div class="problem-card">
    <span class="problem-number">567</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/permutation-in-string/" target="_blank" rel="noopener noreferrer" class="problem-title">Permutation in String</a>
      <a href="/learning/dsa/arrays/arrays-problems/#permutation-in-string" class="problem-btn">📋 View Solution</a>
    </div>
  </div>

  <div class="problem-card">
    <span class="problem-number">3</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/" target="_blank" rel="noopener noreferrer" class="problem-title">Longest Substring Without Repeating</a>
      <a href="/learning/dsa/arrays/arrays-problems/#longest-substring-without-repeating-characters" class="problem-btn">📋 View Solution</a>
    </div>
  </div>

  <div class="problem-card">
    <span class="problem-number">424</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/longest-repeating-character-replacement/" target="_blank" rel="noopener noreferrer" class="problem-title">Longest Repeating Character Replacement</a>
      <a href="/learning/dsa/arrays/arrays-problems/#longest-repeating-character-replacement" class="problem-btn">📋 View Solution</a>
    </div>
  </div>

  <div class="problem-card">
    <span class="problem-number">239</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/sliding-window-maximum/" target="_blank" rel="noopener noreferrer" class="problem-title">Sliding Window Maximum</a>
      <a href="/learning/dsa/arrays/arrays-problems/#sliding-window-maximum" class="problem-btn">📋 View Solution</a>
    </div>
  </div>

  <div class="problem-card">
    <span class="problem-number">76</span>
    <span class="problem-status solved">✓ Solved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/minimum-window-substring/" target="_blank" rel="noopener noreferrer" class="problem-title">Minimum Window Substring</a>
      <a href="/learning/dsa/arrays/arrays-problems/#minimum-window-substring" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
</div>

### 📋 Level 2 — Medium

<div class="problem-grid">
  <div class="problem-card">
    <span class="problem-number">904</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/fruit-into-baskets/" target="_blank" rel="noopener noreferrer" class="problem-title">Fruits Into Baskets</a>
      <a href="/learning/dsa/arrays/arrays-problems/#fruits-into-baskets" class="problem-btn">📋 View Solution</a>
    </div>
  </div>

  <div class="problem-card">
    <span class="problem-number">560</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/subarray-sum-equals-k/" target="_blank" rel="noopener noreferrer" class="problem-title">Subarray Sum Equals K</a>
      <a href="/learning/dsa/arrays/arrays-problems/#subarray-sum-equals-k" class="problem-btn">📋 View Solution</a>
    </div>
  </div>

  <div class="problem-card">
    <span class="problem-number">930</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/binary-subarrays-with-sum/" target="_blank" rel="noopener noreferrer" class="problem-title">Binary Subarrays With Sum</a>
      <a href="/learning/dsa/arrays/arrays-problems/#binary-subarrays-with-sum" class="problem-btn">📋 View Solution</a>
    </div>
  </div>

  <div class="problem-card">
    <span class="problem-number">209</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/minimum-size-subarray-sum/" target="_blank" rel="noopener noreferrer" class="problem-title">Minimum Size Subarray Sum</a>
      <a href="/learning/dsa/arrays/arrays-problems/#minimum-size-subarray-sum" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
</div>

### 📋 Level 3 — Advanced

<div class="problem-grid">
  <div class="problem-card">
    <span class="problem-number">992</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/subarrays-with-k-different-integers/" target="_blank" rel="noopener noreferrer" class="problem-title">Subarrays with K Different Integers</a>
      <a href="/learning/dsa/arrays/arrays-problems/#subarrays-with-k-different-integers" class="problem-btn">📋 View Solution</a>
    </div>
  </div>

  <div class="problem-card">
    <span class="problem-number">340</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/" target="_blank" rel="noopener noreferrer" class="problem-title">Longest Substring with At Most K Distinct</a>
      <a href="/learning/dsa/arrays/arrays-problems/#longest-substring-with-at-most-k-distinct-characters" class="problem-btn">📋 View Solution</a>
    </div>
  </div>

  <div class="problem-card">
    <span class="problem-number">1004</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/max-consecutive-ones-iii/" target="_blank" rel="noopener noreferrer" class="problem-title">Max Consecutive Ones III</a>
      <a href="/learning/dsa/arrays/arrays-problems/#max-consecutive-ones-iii" class="problem-btn">📋 View Solution</a>
    </div>
  </div>

  <div class="problem-card">
    <span class="problem-number">1248</span>
    <span class="problem-status unsolved">○ Unsolved</span>
    <div class="problem-card-inner">
      <a href="https://leetcode.com/problems/count-number-of-nice-subarrays/" target="_blank" rel="noopener noreferrer" class="problem-title">Count Number of Nice Subarrays</a>
      <a href="/learning/dsa/arrays/arrays-problems/#count-number-of-nice-subarrays" class="problem-btn">📋 View Solution</a>
    </div>
  </div>
</div>

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="/learning/dsa/arrays" style="display: inline-block; padding: 12px 28px; background: #667eea; color: white; border-radius: 8px; text-decoration: none; font-weight: 600; margin-right: 1rem;">← Back to Arrays</a>
  <a href="/learning/dsa" style="display: inline-block; padding: 12px 28px; background: #764ba2; color: white; border-radius: 8px; text-decoration: none; font-weight: 600;">DSA Hub 🏠</a>
</div>


