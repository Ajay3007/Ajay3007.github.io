---
title: "Strings"
description: "📋 Practice Problems ⚡ View All Strings Problems → 9 curated problems with solutions • Easy to Hard difficulty 📑 Table of Contents 1."
domain: dsa
order: 0
url: /learning/dsa/strings/
---

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem; text-align: center;">
  <h2 style="color: white; margin: 0 0 1rem 0;">📋 Practice Problems</h2>
  <a href="/learning/dsa/strings/strings-problems/" style="display: inline-block; padding: 12px 30px; background: white; color: #667eea; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 1.1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    ⚡ View All Strings Problems →
  </a>
  <p style="color: rgba(255,255,255,0.9); margin: 1rem 0 0 0; font-size: 0.95rem;">9 curated problems with solutions • Easy to Hard difficulty</p>
</div>

## 📑 Table of Contents

1. **[📘 DSA: Strings Learning Roadmap (Beginner → Advanced)](#-dsa-strings-learning-roadmap-beginner-advanced)**
    1.1. [1. Basics of Strings (Foundations)](#1-basics-of-strings-foundations)
    1.2. [🔍 2. Two Pointers on Strings](#-2-two-pointers-on-strings)
    1.3. [🪟 3. Sliding Window (Very Important)](#-3-sliding-window-very-important)
    1.4. [🧮 4. Hashing for Strings](#-4-hashing-for-strings)
    1.5. [🔤 5. Pattern Matching Algorithms](#-5-pattern-matching-algorithms)
    1.6. [<img src="/assets/icons/puzzle.svg" class="inline-icon" alt=""> 6. Advanced String Topics](#img-src-assets-icons-puzzle-svg-relativeurl-class-inline-icon-alt-6-advanced-string-topics)
2. **[📝 Must Do String Problems](#-must-do-string-problems)**
    2.1. [🔹 Level 1 – Easy](#-level-1-easy)
    2.2. [🔹 Level 2 – Medium](#-level-2-medium)
    2.3. [🔹 Level 3 – Hard](#-level-3-hard)

---

### 🎯 Main Topics Covered

1. **1 Basics of Strings Foundations**
2. **2 Two Pointers on Strings**
3. **3 Sliding Window Very Important**
4. **4 Hashing for Strings**
5. **5 Pattern Matching Algorithms**
6. **img src assetsiconspuzzlesvg  relative_url  classinline-icon alt 6 Advanced String Topics**
7. **Level 1  Easy**
8. **Level 2  Medium**
... and 1 more

---

# 📘 DSA: Strings Learning Roadmap (Beginner → Advanced)

## 1. Basics of Strings (Foundations)

These are must-know before solving problems.

- Mutable vs Immutable (C++: std::string is mutable)

- Character arrays vs string class

- Common operations: length, substring, concatenation, comparison

- ASCII & Unicode basics

### -> [Click here for more details](/learning/dsa/strings/string-basics)

## 🔍 2. Two Pointers on Strings

Used for many interview problems (palindrome, substring checks).

**Key patterns:**

- Move pointers from left & right

- Shrink/expand window on conditions

## 🪟 3. Sliding Window (Very Important)

Strings + Sliding Window = 20% of interview questions.

### Understand two types:

#### 🔸 Fixed Window

E.g., find anagrams of a pattern.

#### 🔸 Variable Window

E.g., longest substring with K distinct characters.

## 🧮 4. Hashing for Strings

### Character frequency arrays

- For lowercase → size 26

- For ASCII → size 256

- For Unicode → use hash maps

### Rolling Hash / Rabin-Karp

- Efficient substring search

- Used for detecting duplicate substrings, plagiarism, etc.

### Interview problems:

- Rabin-Karp implementation

- Longest duplicate substring (binary search + rolling hash)

## 🔤 5. Pattern Matching Algorithms

### KMP (Knuth–Morris–Pratt)

Why important?

- Used for substring search in O(n + m)

- LPS array is commonly asked in interviews.

### Z-Algorithm

- Alternate fast pattern matching

- Helps in string prefix-based problems

### Trie (String Tree)

- Useful for autocomplete, prefix search, dictionary problems

### Problems:

- Word search

- Longest common prefix

- Implement Trie

## <img src="/assets/icons/puzzle.svg" class="inline-icon" alt=""> 6. Advanced String Topics

These help in elite interviews.

### Suffix Array

- Used for lexicographical ordering of suffixes

- **Applications:** substring search, LCP computation

### Suffix Tree / Compressed Trie

- Extremely fast substring search

- Rare but high-reward for deep interviews

### Manacher's Algorithm

- O(n) longest palindromic substring


# 📝 Must Do String Problems

## 🔹 Level 1 – Easy

1. Reverse string

2. Palindrome check

3. Count occurrences of characters

4. Remove duplicates

5. String compression

6. [Leetcode 412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/description/){:target="_blank" rel="noopener noreferrer"} - **[Solution](/learning/dsa/strings/Leetcode-412.cpp)**

7. [Leetcode 14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/){:target="_blank" rel="noopener noreferrer"} - **[Solution](https://leetcode.com/problems/longest-common-prefix/solutions/7391572/horizontal-scanning-approach-on-solution-9y18/){:target="_blank" rel="noopener noreferrer"}**



## 🔹 Level 2 – Medium

1. Longest substring without repeating

2. Longest palindromic substring

3. Group anagrams

4. Valid parentheses

5. Multiply large numbers (string simulation)

6. [Leetcode 271. Encode and Decode Strings{Premium Problem}](https://leetcode.com/problems/encode-and-decode-strings/description/){:target="_blank" rel="noopener noreferrer"} - **[My Leetcode Solution link](https://leetcode.com/problems/encode-and-decode-strings/solutions/7391904/encode-decode-strings-fixed-length-heade-3h9i/){:target="_blank" rel="noopener noreferrer"}**

    - If you can't see the problem, **[Click Here](/learning/dsa/strings/leetcode-271)**

7. [Leetcode 647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/description/){:target="_blank" rel="noopener noreferrer"} - **[My Leetcode Solution link](https://leetcode.com/problems/palindromic-substrings/solutions/7395151/expand-around-center-on2-solution-by-aja-6hvd/){:target="_blank" rel="noopener noreferrer"}**

8. [Leetcode 5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/){:target="_blank" rel="noopener noreferrer"} - **[My Leetcode Solution link](https://leetcode.com/problems/longest-palindromic-substring/solutions/7395617/longest-palindromic-substring-expand-aro-ky6o/){:target="_blank" rel="noopener noreferrer"}**


## 🔹 Level 3 – Hard

1. Minimum window substring

2. Word break (DP + String)

3. Regular expression matching (DP)

4. Wildcard matching

5. KMP + Z-algorithm applications

6. Longest duplicate substring (binary search + hash)

7. [Leetcode 647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/description/){:target="_blank" rel="noopener noreferrer"} - **[My Leetcode Solution link](https://leetcode.com/problems/palindromic-substrings/solutions/7395151/expand-around-center-on2-solution-by-aja-6hvd/){:target="_blank" rel="noopener noreferrer"}**

8. [Leetcode 68. Text Justification](https://leetcode.com/problems/text-justification/description/){:target="_blank" rel="noopener noreferrer"} - **[My Leetcode Solution link](https://leetcode.com/problems/text-justification/solutions/7398638/greedy-line-packing-smart-space-distribu-f3sp/){:target="_blank" rel="noopener noreferrer"}**


