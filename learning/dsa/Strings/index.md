---
layout: default
title: Strings
permalink: /learning/dsa/strings/
---

# ðŸ“˜ DSA: Strings Learning Roadmap (Beginner â†’ Advanced)

## 1. Basics of Strings (Foundations)

These are must-know before solving problems.

- Mutable vs Immutable (C++: std::string is mutable)

- Character arrays vs string class

- Common operations: length, substring, concatenation, comparison

- ASCII & Unicode basics

### -> [Click here for more details](string-basics.md)

## ðŸ” 2. Two Pointers on Strings

Used for many interview problems (palindrome, substring checks).

**Key patterns:**

- Move pointers from left & right

- Shrink/expand window on conditions

## ðŸªŸ 3. Sliding Window (Very Important)

Strings + Sliding Window = 20% of interview questions.

### Understand two types:

#### ðŸ”¸ Fixed Window

E.g., find anagrams of a pattern.

#### ðŸ”¸ Variable Window

E.g., longest substring with K distinct characters.

## ðŸ§® 4. Hashing for Strings

### Character frequency arrays

- For lowercase â†’ size 26

- For ASCII â†’ size 256

- For Unicode â†’ use hash maps

### Rolling Hash / Rabin-Karp

- Efficient substring search

- Used for detecting duplicate substrings, plagiarism, etc.

### Interview problems:

- Rabin-Karp implementation

- Longest duplicate substring (binary search + rolling hash)

## ðŸ”¤ 5. Pattern Matching Algorithms

### KMP (Knuthâ€“Morrisâ€“Pratt)

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

### Manacherâ€™s Algorithm

- O(n) longest palindromic substring


# ðŸ“ Must Do String Problems

## ðŸ”¹ Level 1 â€“ Easy

1. Reverse string

2. Palindrome check

3. Count occurrences of characters

4. Remove duplicates

5. String compression

6. [Leetcode 412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/description/){:target="_blank" rel="noopener noreferrer"} - **[Solution](Leetcode-412.cpp)**

7. [Leetcode 14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/){:target="_blank" rel="noopener noreferrer"} - **[Solution](https://leetcode.com/problems/longest-common-prefix/solutions/7391572/horizontal-scanning-approach-on-solution-9y18/){:target="_blank" rel="noopener noreferrer"}**



## ðŸ”¹ Level 2 â€“ Medium

1. Longest substring without repeating

2. Longest palindromic substring

3. Group anagrams

4. Valid parentheses

5. Multiply large numbers (string simulation)

6. [Leetcode 271. Encode and Decode Strings{Premium Problem}](https://leetcode.com/problems/encode-and-decode-strings/description/){:target="_blank" rel="noopener noreferrer"} - **[My Leetcode Solution link](https://leetcode.com/problems/encode-and-decode-strings/solutions/7391904/encode-decode-strings-fixed-length-heade-3h9i/){:target="_blank" rel="noopener noreferrer"}**

    - If you can't see the problem, **[Click Here](leetcode-271.md)**

7. [Leetcode 647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/description/){:target="_blank" rel="noopener noreferrer"} - **[My Leetcode Solution link](https://leetcode.com/problems/palindromic-substrings/solutions/7395151/expand-around-center-on2-solution-by-aja-6hvd/){:target="_blank" rel="noopener noreferrer"}**

8. [Leetcode 5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/){:target="_blank" rel="noopener noreferrer"} - **[My Leetcode Solution link](https://leetcode.com/problems/longest-palindromic-substring/solutions/7395617/longest-palindromic-substring-expand-aro-ky6o/){:target="_blank" rel="noopener noreferrer"}**


## ðŸ”¹ Level 3 â€“ Hard

1. Minimum window substring

2. Word break (DP + String)

3. Regular expression matching (DP)

4. Wildcard matching

5. KMP + Z-algorithm applications

6. Longest duplicate substring (binary search + hash)

7. [Leetcode 647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/description/){:target="_blank" rel="noopener noreferrer"} - **[My Leetcode Solution link](https://leetcode.com/problems/palindromic-substrings/solutions/7395151/expand-around-center-on2-solution-by-aja-6hvd/){:target="_blank" rel="noopener noreferrer"}**

8. [Leetcode 68. Text Justification](https://leetcode.com/problems/text-justification/description/){:target="_blank" rel="noopener noreferrer"} - **[My Leetcode Solution link](https://leetcode.com/problems/text-justification/solutions/7398638/greedy-line-packing-smart-space-distribu-f3sp/){:target="_blank" rel="noopener noreferrer"}**


