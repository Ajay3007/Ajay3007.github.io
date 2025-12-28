## 📑 Table of Contents

1. **[📘 DSA: Strings Learning Roadmap (Beginner → Advanced)](#-dsa-strings-learning-roadmap-beginner-advanced)**
  1.1. [1. Basics of Strings (Foundations)](#1-basics-of-strings-foundations)
    1.1.1. [-> [Click here for more details](string-basics.md)](#click-here-for-more-details-string-basics-md)
  1.2. [🔍 2. Two Pointers on Strings](#-2-two-pointers-on-strings)
  1.3. [🪟 3. Sliding Window (Very Important)](#-3-sliding-window-very-important)
    1.3.1. [Understand two types:](#understand-two-types)
      1.3.1.1. [🔸 Fixed Window](#-fixed-window)
      1.3.1.2. [🔸 Variable Window](#-variable-window)
  1.4. [🧮 4. Hashing for Strings](#-4-hashing-for-strings)
    1.4.1. [Character frequency arrays](#character-frequency-arrays)
    1.4.2. [Rolling Hash / Rabin-Karp](#rolling-hash-rabin-karp)
    1.4.3. [Interview problems:](#interview-problems)
  1.5. [🔤 5. Pattern Matching Algorithms](#-5-pattern-matching-algorithms)
    1.5.1. [KMP (Knuth–Morris–Pratt)](#kmp-knuth-morris-pratt)
    1.5.2. [Z-Algorithm](#z-algorithm)
    1.5.3. [Trie (String Tree)](#trie-string-tree)
    1.5.4. [Problems:](#problems)
  1.6. [<img src="{{ '/assets/icons/puzzle.svg' | relative_url }}" class="inline-icon" alt=""> 6. Advanced String Topics](#img-src-assets-icons-puzzle-svg-relativeurl-class-inline-icon-alt-6-advanced-string-topics)
    1.6.1. [Suffix Array](#suffix-array)
    1.6.2. [Suffix Tree / Compressed Trie](#suffix-tree-compressed-trie)
    1.6.3. [Manacher's Algorithm](#manacher-s-algorithm)
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

### -> [Click here for more details](string-basics.md)

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

## <img src="{{ '/assets/icons/puzzle.svg' | relative_url }}" class="inline-icon" alt=""> 6. Advanced String Topics

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

6. [Leetcode 412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/description/){:target="_blank" rel="noopener noreferrer"} - **[Solution](Leetcode-412.cpp)**

7. [Leetcode 14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/){:target="_blank" rel="noopener noreferrer"} - **[Solution](https://leetcode.com/problems/longest-common-prefix/solutions/7391572/horizontal-scanning-approach-on-solution-9y18/){:target="_blank" rel="noopener noreferrer"}**



## 🔹 Level 2 – Medium

1. Longest substring without repeating

2. Longest palindromic substring

3. Group anagrams

4. Valid parentheses

5. Multiply large numbers (string simulation)

6. [Leetcode 271. Encode and Decode Strings{Premium Problem}](https://leetcode.com/problems/encode-and-decode-strings/description/){:target="_blank" rel="noopener noreferrer"} - **[My Leetcode Solution link](https://leetcode.com/problems/encode-and-decode-strings/solutions/7391904/encode-decode-strings-fixed-length-heade-3h9i/){:target="_blank" rel="noopener noreferrer"}**

    - If you can't see the problem, **[Click Here](leetcode-271.md)**

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


