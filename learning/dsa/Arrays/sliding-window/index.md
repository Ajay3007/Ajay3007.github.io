---
layout: default
title: Sliding Window
permalink: /learning/dsa/arrays/sliding-window/
---

## 📑 Table of Contents

1. **[<img src="{{ '/assets/icons/rocket.svg' | relative_url }}" class="inline-icon" alt=""> Sliding Window](#img-src-assets-icons-rocket-svg-relativeurl-class-inline-icon-alt-sliding-window)**
    1.1. [⭐ 2. Types of Sliding Window](#-2-types-of-sliding-window)
    1.2. [⭐ Templates (MOST IMPORTANT PART)](#-templates-most-important-part)
    1.3. [⭐ Top 5 Sliding Window Patterns](#-top-5-sliding-window-patterns)
    1.4. [⭐ Must-Do Sliding Window Problems](#-must-do-sliding-window-problems)

---

### 🎯 Main Topics Covered

1. **2 Types of Sliding Window**
2. **Templates MOST IMPORTANT PART**
3. **Top 5 Sliding Window Patterns**
4. **Must-Do Sliding Window Problems**

---

# <img src="{{ '/assets/icons/rocket.svg' | relative_url }}" class="inline-icon" alt=""> Sliding Window

Sliding Window is used when we deal with **contiguous subarrays or substrings**.

**Common keywords:**

- longest
- smallest
- maximum
- minimum
- subarray/substring
- at most / at least K distinct
- average of size K

## ⭐ 2. Types of Sliding Window

You must know BOTH:

### 1️⃣ Fixed-Size Window (size = K)

Useful when **K is fixed.**

#### 📌 Examples

Max sum of subarray size K

First negative number in window size K

#### 2️⃣ Variable-Size Window (stretch/shrink)

Used when the **window grows** until a **condition** becomes **invalid**, then we **shrink**.

#### 📌 Examples

Longest substring without repeating characters

Longest subarray with sum ≤ K

Minimum window substring

Fruits into baskets (max subarray with at most 2 distinct fruits)

## ⭐ Templates (MOST IMPORTANT PART)
### 🔶 Template 1 — Fixed Size Window (size = K)

```cpp
int left = 0;
long long sum = 0, best = 0;

for (int right = 0; right < n; right++) {
    sum += arr[right]; // expand window

    if (right - left + 1 == K) {
        best = max(best, sum);
        sum -= arr[left]; // shrink
        left++;
    }
}
```

### 🔶 Template 2 — Variable Window (Most Important)

```cpp
int left = 0;
for (int right = 0; right < n; right++) {
    // Add arr[right] and make window bigger

    while (window_invalid_condition) {
        // Shrink window
        left++;
    }

    // track best window
}
```

Use when:
👉 window size is always exactly K

### 🔶 Template 2 — Variable Window (Most Important)

```cpp
int left = 0;
for (int right = 0; right < n; right++) {
    // Add arr[right] and make window bigger

    while (window_invalid_condition) {
        // Shrink window
        left++;
    }

    // track best window
}
```

### 🔶 Template 3 — Window with Frequency Map

Used for substring problems.

unordered_map<char,int> freq;
int left = 0;

```cpp
for (int right = 0; right < s.size(); right++) {
    freq[s[right]]++;

    while (condition_invalid) {
        freq[s[left]]--;
        left++;
    }

    ans = max(ans, right - left + 1);
}
```

## ⭐ Top 5 Sliding Window Patterns

#### 🔸 Pattern 1: Longest substring without repeating characters

Condition: window is invalid when any character count > 1

👉 shrink until all chars have freq 1

#### 🔸 Pattern 2: At most K distinct characters

Condition: invalid when freq_map.size() > K

#### 🔸 Pattern 3: Sum ≤ K

When sum exceeds K → shrink window

#### 🔸 Pattern 4: Minimum window substring

A classic variable window with two hash maps:

- need

- have

Shrink window only when it satisfies the target.

#### 🔸 Pattern 5: Fixed Size

Very direct.

## ⭐ Must-Do Sliding Window Problems
### Level 1 — Basics

#### 1. [Leetcode 121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/){:target="_blank" rel="noopener noreferrer"}

**- Brute Force Approach:**
For every prices[i], check profit for every prices[j]; where, j>i
take maximum of all profits.
In formal, find max(prices[j]−prices[i]), for every i and j such that j>i.

Time Complexity - O(n^2)

**- Optimal Solution**
We can maintain two variables - minprice(buy) and maxprofit corresponding to the smallest buy and maximum profit (maximum difference between selling price and minprice(buy)) obtained so far respectively.

Time Complexity : O(n)

**[Solution Leetcode 121](Leetcode-121.cpp)**

#### 2. [Leetcode 567. Permutation in String](https://leetcode.com/problems/permutation-in-string/description/){:target="_blank" rel="noopener noreferrer"}

**- Brute Force Approach:**

```cpp
s1 = "abc"; 
s2 = "badcbalm";
```

Check for each permutation of s1 whether it is present in s2 or not!

**- Optimal Solution**

1. Use hashmap or array(size - 26) to store frequency of each character of s1.
2. Decide a window size(size = s1, say k
) in s2.
3. For each possible window size check the same frequency matches with the original frequency of s1.

**[Solution Leetcode 567](Leetcode-567.cpp)**

#### 3. [Leetcode 424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/){:target="_blank" rel="noopener noreferrer"}

**- Brute Force Approach:**

```cpp 
s = "PXQXYXB";
k = 2
```
What will be a valid substring? Because we are allowed only k operations to do so, we would want to minimize the number of operations.

Lets a substring with length `len`. It is valid if following condition satisfies:

`(len - [most occuring char freq]) <= k`

Generate all substring and check for a valid substring as defined above.

**- Optimal Solution**

**[Refer this pdf image for Explaination](leetcode424.pdf)**

**[Solution Leetcode 424](Leetcode-424.cpp)**

#### 4. [Leetcode 3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/){:target="_blank" rel="noopener noreferrer"}

**- Brute Force Approach:**

```cpp
s = "abatman"
ans = 4
```

Generate all substring and check for the longest substring without repeating character

**- Optimal Solution**

**[Refer this pdf image for Explaination](leetcode-3.pdf)**

**[Solution Leetcode 3](Leetcode-3.cpp)**

#### 5. [Leetcode 239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/){:target="_blank" rel="noopener noreferrer"}

**- Brute Force Approach:**

```cpp
nums = [1,3,-1,-3,5,3,6,7]
k = 3
```

Iterate for each window and find maximum of each window 

Time Complexity : O(n*k)

**- Better Approach**

**[For my Leetcode Solution link click here](https://leetcode.com/problems/sliding-window-maximum/solutions/7381366/sliding-window-maximum-using-multiset-cl-pres/){:target="_blank" rel="noopener noreferrer"}**

**- Optimal Solution**

We may observe that in a window, the elements that come before the largest element will never be selected as the largest element of any future windows.

In general, whenever we encounter a new element x, we want to discard all elements that are less than x before adding x. Let's say we currently have [63, 15, 8, 3] and we encounter 12. Any future window with 8 or 3 will also contain 12, so we can discard them. After discarding them and adding 12, we have [63, 15, 12]. As you can see, we keep elements in descending order.

**[Solution Leetcode 239](Leetcode-239.cpp)**


#### 6. [Leetcode 76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/){:target="_blank" rel="noopener noreferrer"}

```cpp
s = "ADOBECODEBANC"
T = "ABC"
```

**[For my Leetcode Solution link click here](https://leetcode.com/problems/minimum-window-substring/solutions/7384109/leetcode-76-minimum-window-substring-two-jqes/){:target="_blank" rel="noopener noreferrer"}**

All solution and approaches are discussed in above link.



Max sum subarray of size K

First negative number in window size K

Count occurrences of anagrams

### Level 2 — Medium

Longest substring without repeating

Longest repeating character replacement

Fruits into baskets

Minimum window substring

Subarray sum equals K (prefix + sliding combination)

Binary subarray with sum

### Level 3 — Hard

Subarrays with K different integers

Minimum size subarray sum

Longest substring with at most K distinct characters

Count substring with exactly K distinct

Max consecutive ones III

Number of nice subarrays

Longest subarray with sum ≤ K

Sliding window maximum (Deque, bonus)


