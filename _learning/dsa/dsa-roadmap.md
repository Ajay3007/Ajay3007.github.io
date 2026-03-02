---
layout: default
title: DSA Mastery Roadmap
permalink: /learning/dsa/dsa-roadmap/
custom_css: dsa-roadmap
---

<div class="roadmap-hero">
  <h1>DSA Mastery Roadmap</h1>
  <p>Data Structures &amp; Algorithms for Coding Interviews — Complete C++ Reference with LeetCode Problems</p>
  <div class="roadmap-stats">
    <div class="roadmap-stat"><div class="roadmap-stat-val">13</div><div class="roadmap-stat-lbl">Chapters</div></div>
    <div class="roadmap-stat"><div class="roadmap-stat-val">100+</div><div class="roadmap-stat-lbl">Problems</div></div>
    <div class="roadmap-stat"><div class="roadmap-stat-val">C++</div><div class="roadmap-stat-lbl">Templates</div></div>
    <div class="roadmap-stat"><div class="roadmap-stat-val">12</div><div class="roadmap-stat-lbl">Patterns</div></div>
  </div>
</div>

<div class="chapter-nav">
  <a href="#ch0">Ch 0 — Big O &amp; Recursion</a>
  <a href="#ch1">Ch 1 — Arrays &amp; Strings</a>
  <a href="#ch2">Ch 2 — Hashing</a>
  <a href="#ch3">Ch 3 — Linked Lists</a>
  <a href="#ch4">Ch 4 — Stacks &amp; Queues</a>
  <a href="#ch5">Ch 5 — Trees &amp; Graphs</a>
  <a href="#ch6">Ch 6 — Heaps</a>
  <a href="#ch7">Ch 7 — Greedy</a>
  <a href="#ch8">Ch 8 — Binary Search</a>
  <a href="#ch9">Ch 9 — Backtracking</a>
  <a href="#ch10">Ch 10 — Dynamic Programming</a>
  <a href="#ch11">Ch 11 — Bonus Topics</a>
  <a href="#ch12">Ch 12 — Study Plan &amp; Cheatsheet</a>
</div>

---

<div class="roadmap-chapter" id="ch0" markdown="1">

## Chapter 0 — Big O &amp; Recursion

### 0.1 Big O Notation

Big O describes computational complexity — how time/space usage scales with input size n. **Always analyse worst-case** unless told otherwise.

<div class="pattern-box">
<ul>
<li>Drop constants: O(5n) = O(n)</li>
<li>Drop lower-order terms: O(n² + n) = O(n²)</li>
<li>Space complexity excludes input; usually excludes output too</li>
</ul>
</div>

**Complexity Hierarchy (fastest → slowest)**

| Complexity | Name | Example |
|---|---|---|
| O(1) | Constant | Array index access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop |
| O(n log n) | Linearithmic | Merge sort, heap sort |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Subsets, backtracking |
| O(n!) | Factorial | All permutations |

### 0.2 Recursion

<div class="pattern-box">
<ul>
<li>Every recursive function needs: <strong>Base case</strong> (stop condition) + <strong>Recursive case</strong></li>
<li>Call stack space = O(depth). Watch for stack overflow on deep recursion</li>
<li>Convert to iteration with an explicit stack when stack depth is a concern</li>
<li>Memoization = cache results to avoid recomputing subproblems</li>
</ul>
</div>

```cpp
// Generic recursion template
ReturnType solve(params, state) {
    // 1. Base case
    if (baseCondition) return baseValue;
    // 2. Recursive case — make smaller subproblem
    return solve(smallerParams, newState);
}
```

#### Practice Problems

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/fibonacci-number/" target="_blank" rel="noopener noreferrer">509. Fibonacci Number</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/climbing-stairs/" target="_blank" rel="noopener noreferrer">70. Climbing Stairs</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/power-of-two/" target="_blank" rel="noopener noreferrer">231. Power of Two</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank" rel="noopener noreferrer">206. Reverse Linked List</a></td><td class="diff-easy">Easy</td></tr>
</tbody>
</table>

</div>

---

<div class="roadmap-chapter" id="ch1" markdown="1">

## Chapter 1 — Arrays &amp; Strings

<a href="{{ '/learning/dsa/arrays/arrays-problems/' | relative_url }}" class="topic-link-badge">📊 Arrays Problems Page →</a>
<a href="{{ '/learning/dsa/strings/strings-problems/' | relative_url }}" class="topic-link-badge">🔤 Strings Problems Page →</a>

### 1.1 Two Pointers

**When to Use:** Sorted arrays, palindrome checks, pair-sum problems, merging sorted arrays. Achieves O(n) instead of O(n²) brute force.

<div class="pattern-box">
<ul>
<li><strong>OPPOSITE ENDS:</strong> left=0, right=n-1, move inward. Use for: palindrome, two-sum on sorted array</li>
<li><strong>SAME DIRECTION:</strong> both start at 0 (fast/slow). Use for: remove duplicates, subsequence check</li>
<li><strong>TWO ARRAYS:</strong> one pointer per array. Use for: merge sorted arrays, compare sequences</li>
</ul>
</div>

<div class="complexity-row">
<span class="complexity-badge"><span class="label">Time</span> O(n)</span>
<span class="complexity-badge"><span class="label">Space</span> O(1)</span>
</div>

```cpp
// Pattern 1: Opposite ends
int left = 0, right = arr.size() - 1;
while (left < right) {
    if (condition) { left++; right--; }
    else if (tooSmall) left++;
    else right--;
}

// Pattern 2: Fast/Slow (same direction)
int slow = 0;
for (int fast = 0; fast < arr.size(); fast++) {
    if (condition(arr[fast])) arr[slow++] = arr[fast];
}

// Pattern 3: Two arrays
int i = 0, j = 0;
while (i < arr1.size() && j < arr2.size()) {
    if (arr1[i] <= arr2[j]) result.push_back(arr1[i++]);
    else result.push_back(arr2[j++]);
}
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/valid-palindrome/" target="_blank" rel="noopener noreferrer">125. Valid Palindrome</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/" target="_blank" rel="noopener noreferrer">167. Two Sum II</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/reverse-string/" target="_blank" rel="noopener noreferrer">344. Reverse String</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/squares-of-a-sorted-array/" target="_blank" rel="noopener noreferrer">977. Squares of a Sorted Array</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/move-zeroes/" target="_blank" rel="noopener noreferrer">283. Move Zeroes</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/" target="_blank" rel="noopener noreferrer">26. Remove Duplicates from Sorted Array</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/is-subsequence/" target="_blank" rel="noopener noreferrer">392. Is Subsequence</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>8</td><td><a href="https://leetcode.com/problems/3sum/" target="_blank" rel="noopener noreferrer">15. 3Sum</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>9</td><td><a href="https://leetcode.com/problems/container-with-most-water/" target="_blank" rel="noopener noreferrer">11. Container With Most Water</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>10</td><td><a href="https://leetcode.com/problems/trapping-rain-water/" target="_blank" rel="noopener noreferrer">42. Trapping Rain Water</a></td><td class="diff-hard">Hard</td></tr>
</tbody>
</table>

### 1.2 Sliding Window

**When to Use:** Contiguous subarray/substring problems with a constraint metric. Trigger words: *subarray/substring with at most / exactly / longest / shortest*.

<div class="pattern-box">
<ul>
<li><strong>DYNAMIC WINDOW:</strong> expand right always, shrink left while constraint violated</li>
<li><strong>FIXED WINDOW (size k):</strong> slide — add arr[right], remove arr[right-k]</li>
<li>COUNT of valid subarrays ending at right = right - left + 1</li>
<li>Constraint metric tracked with a variable (sum, count, hashmap of freq)</li>
</ul>
</div>

<div class="complexity-row">
<span class="complexity-badge"><span class="label">Time</span> O(n) amortized</span>
<span class="complexity-badge"><span class="label">Space</span> O(1) or O(k)</span>
</div>

```cpp
// Dynamic window
int left = 0, curr = 0, ans = 0;
for (int right = 0; right < nums.size(); right++) {
    curr += nums[right];           // expand
    while (curr > k) curr -= nums[left++]; // shrink
    ans = max(ans, right - left + 1);
}

// Fixed window (size k)
int curr = 0;
for (int i = 0; i < k; i++) curr += nums[i];
int ans = curr;
for (int i = k; i < nums.size(); i++) {
    curr += nums[i] - nums[i - k]; // slide
    ans = max(ans, curr);
}
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/maximum-average-subarray-i/" target="_blank" rel="noopener noreferrer">643. Maximum Average Subarray I</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/max-consecutive-ones-iii/" target="_blank" rel="noopener noreferrer">1004. Max Consecutive Ones III</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/" target="_blank" rel="noopener noreferrer">3. Longest Substring Without Repeating Characters</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/subarray-product-less-than-k/" target="_blank" rel="noopener noreferrer">713. Subarray Product Less Than K</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/minimum-size-subarray-sum/" target="_blank" rel="noopener noreferrer">209. Minimum Size Subarray Sum</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/fruit-into-baskets/" target="_blank" rel="noopener noreferrer">904. Fruit Into Baskets</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/sliding-window-maximum/" target="_blank" rel="noopener noreferrer">239. Sliding Window Maximum</a></td><td class="diff-hard">Hard</td></tr>
<tr><td>8</td><td><a href="https://leetcode.com/problems/minimum-window-substring/" target="_blank" rel="noopener noreferrer">76. Minimum Window Substring</a></td><td class="diff-hard">Hard</td></tr>
</tbody>
</table>

### 1.3 Prefix Sum

**When to Use:** Range sum queries in O(1) after O(n) preprocessing. Useful when the same array is queried many times.

<div class="pattern-box">
<ul>
<li>prefix[i] = prefix[i-1] + nums[i-1]. Range sum [l,r] = prefix[r+1] - prefix[l]</li>
<li>2D prefix sums for matrix range queries</li>
<li>Combine with hashmap: store prefix sum frequencies for subarray count problems</li>
</ul>
</div>

<div class="complexity-row">
<span class="complexity-badge"><span class="label">Time</span> O(n) build, O(1) query</span>
<span class="complexity-badge"><span class="label">Space</span> O(n)</span>
</div>

{% raw %}
```cpp
// 1D prefix sum
vector<int> prefix(nums.size() + 1, 0);
for (int i = 0; i < nums.size(); i++)
    prefix[i+1] = prefix[i] + nums[i];
// Sum of nums[l..r] = prefix[r+1] - prefix[l]

// Subarray sum equals k (count) — O(n)
unordered_map<int,int> freq{{0,1}};
int curr = 0, ans = 0;
for (int x : nums) {
    curr += x;
    ans += freq[curr - k];
    freq[curr]++;
}
```
{% endraw %}

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/running-sum-of-1d-array/" target="_blank" rel="noopener noreferrer">1480. Running Sum of 1d Array</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/" target="_blank" rel="noopener noreferrer">1413. Minimum Value to Get Positive Step by Step Sum</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/k-radius-subarray-averages/" target="_blank" rel="noopener noreferrer">2090. K Radius Subarray Averages</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/range-sum-query-immutable/" target="_blank" rel="noopener noreferrer">303. Range Sum Query - Immutable</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/subarray-sum-equals-k/" target="_blank" rel="noopener noreferrer">560. Subarray Sum Equals K</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/contiguous-array/" target="_blank" rel="noopener noreferrer">525. Contiguous Array</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/product-of-array-except-self/" target="_blank" rel="noopener noreferrer">238. Product of Array Except Self</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>8</td><td><a href="https://leetcode.com/problems/find-pivot-index/" target="_blank" rel="noopener noreferrer">724. Find Pivot Index</a></td><td class="diff-easy">Easy</td></tr>
</tbody>
</table>

</div>

---

<div class="roadmap-chapter" id="ch2" markdown="1">

## Chapter 2 — Hashing (Hashmaps &amp; Sets)

Hash maps offer **O(1) average** insert/lookup/delete. Sets track existence. Hashmaps track frequency/mapping.

<div class="pattern-box">
<ul>
<li><strong>EXISTENCE CHECK:</strong> Use unordered_set for O(1) lookup (duplicates, anagram, pangram)</li>
<li><strong>FREQUENCY COUNT:</strong> Use unordered_map&lt;T, int&gt; (count chars, elements, words)</li>
<li><strong>TWO-SUM PATTERN:</strong> Store seen values in map; for each x, check if (target-x) exists</li>
<li><strong>GROUPING:</strong> Map key → list of values (group anagrams by sorted string)</li>
<li><strong>SLIDING WINDOW + HASHMAP:</strong> Track character frequencies in a window</li>
<li><strong>PREFIX SUM + HASHMAP:</strong> Count subarrays with target sum/property</li>
</ul>
</div>

<div class="complexity-row">
<span class="complexity-badge"><span class="label">Time</span> O(n) average</span>
<span class="complexity-badge"><span class="label">Space</span> O(n)</span>
</div>

```cpp
// Frequency count
unordered_map<int, int> freq;
for (int x : arr) freq[x]++;

// Two-sum lookup
unordered_map<int, int> seen;
for (int i = 0; i < nums.size(); i++) {
    if (seen.count(target - nums[i]))
        return {seen[target - nums[i]], i};
    seen[nums[i]] = i;
}

// Group anagrams
unordered_map<string, vector<string>> groups;
for (string& s : strs) {
    string key = s; sort(key.begin(), key.end());
    groups[key].push_back(s);
}
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/check-if-the-sentence-is-pangram/" target="_blank" rel="noopener noreferrer">1832. Check if the Sentence Is Pangram</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/missing-number/" target="_blank" rel="noopener noreferrer">268. Missing Number</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/counting-elements/" target="_blank" rel="noopener noreferrer">1426. Counting Elements</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/two-sum/" target="_blank" rel="noopener noreferrer">1. Two Sum</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/ransom-note/" target="_blank" rel="noopener noreferrer">383. Ransom Note</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/jewels-and-stones/" target="_blank" rel="noopener noreferrer">771. Jewels and Stones</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/find-players-with-zero-or-one-losses/" target="_blank" rel="noopener noreferrer">2225. Find Players With Zero or One Losses</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>8</td><td><a href="https://leetcode.com/problems/largest-unique-number/" target="_blank" rel="noopener noreferrer">1133. Largest Unique Number</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>9</td><td><a href="https://leetcode.com/problems/maximum-number-of-balloons/" target="_blank" rel="noopener noreferrer">1189. Maximum Number of Balloons</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>10</td><td><a href="https://leetcode.com/problems/group-anagrams/" target="_blank" rel="noopener noreferrer">49. Group Anagrams</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>11</td><td><a href="https://leetcode.com/problems/top-k-frequent-elements/" target="_blank" rel="noopener noreferrer">347. Top K Frequent Elements</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>12</td><td><a href="https://leetcode.com/problems/subarray-sum-equals-k/" target="_blank" rel="noopener noreferrer">560. Subarray Sum Equals K</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>13</td><td><a href="https://leetcode.com/problems/lru-cache/" target="_blank" rel="noopener noreferrer">146. LRU Cache</a></td><td class="diff-medium">Medium</td></tr>
</tbody>
</table>

</div>

---

<div class="roadmap-chapter" id="ch3" markdown="1">

## Chapter 3 — Linked Lists

<a href="{{ '/learning/dsa/linked-list/linked-list-problems/' | relative_url }}" class="topic-link-badge">🔗 Linked List Problems Page →</a>

Linked lists excel at **O(1) insert/delete** at known position but O(n) search.

<div class="pattern-box">
<ul>
<li><strong>FAST/SLOW POINTERS (Floyd's):</strong> fast moves 2x, slow moves 1x — middle, cycle detection, kth from end</li>
<li><strong>REVERSAL:</strong> Iterative with prev/curr/next pointers. O(n) time, O(1) space</li>
<li><strong>DUMMY NODE:</strong> Add a dummy head to simplify edge cases (empty list, removing head)</li>
<li><strong>TWO-POINTER MERGE:</strong> Merge two sorted lists by comparing heads</li>
</ul>
</div>

<div class="complexity-row">
<span class="complexity-badge"><span class="label">Time</span> O(n) traversal</span>
<span class="complexity-badge"><span class="label">Space</span> O(1) for most patterns</span>
</div>

```cpp
// Fast/slow — find middle
ListNode *slow = head, *fast = head;
while (fast && fast->next) {
    slow = slow->next; fast = fast->next->next;
}  // slow = middle

// Reverse a linked list
ListNode *prev = nullptr, *curr = head;
while (curr) {
    ListNode* next = curr->next;
    curr->next = prev; prev = curr; curr = next;
}  // prev = new head

// Merge two sorted lists (dummy head)
ListNode dummy(0); ListNode* tail = &dummy;
while (l1 && l2) {
    if (l1->val <= l2->val) { tail->next = l1; l1 = l1->next; }
    else                    { tail->next = l2; l2 = l2->next; }
    tail = tail->next;
}
tail->next = l1 ? l1 : l2;
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/middle-of-the-linked-list/" target="_blank" rel="noopener noreferrer">876. Middle of the Linked List</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list/" target="_blank" rel="noopener noreferrer">83. Remove Duplicates from Sorted List</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank" rel="noopener noreferrer">206. Reverse Linked List</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/reverse-linked-list-ii/" target="_blank" rel="noopener noreferrer">92. Reverse Linked List II</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/linked-list-cycle/" target="_blank" rel="noopener noreferrer">141. Linked List Cycle</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/merge-two-sorted-lists/" target="_blank" rel="noopener noreferrer">21. Merge Two Sorted Lists</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/" target="_blank" rel="noopener noreferrer">19. Remove Nth Node From End of List</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>8</td><td><a href="https://leetcode.com/problems/add-two-numbers/" target="_blank" rel="noopener noreferrer">2. Add Two Numbers</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>9</td><td><a href="https://leetcode.com/problems/reorder-list/" target="_blank" rel="noopener noreferrer">143. Reorder List</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>10</td><td><a href="https://leetcode.com/problems/lru-cache/" target="_blank" rel="noopener noreferrer">146. LRU Cache</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>11</td><td><a href="https://leetcode.com/problems/merge-k-sorted-lists/" target="_blank" rel="noopener noreferrer">23. Merge K Sorted Lists</a></td><td class="diff-hard">Hard</td></tr>
</tbody>
</table>

</div>

---

<div class="roadmap-chapter" id="ch4" markdown="1">

## Chapter 4 — Stacks &amp; Queues

<a href="{{ '/learning/dsa/stacks/stacks-problems/' | relative_url }}" class="topic-link-badge">📚 Stacks Problems Page →</a>

### 4.1 Stacks

**When to Use:** LIFO — matching brackets, undo operations, DFS, expression evaluation, monotonic problems.

<div class="pattern-box">
<ul>
<li><strong>MATCHING/VALIDATION:</strong> Push open brackets, pop on close, check match</li>
<li><strong>MONOTONIC STACK (increasing):</strong> pop smaller than current → next greater element, stock span</li>
<li><strong>MONOTONIC STACK (decreasing):</strong> pop greater than current → next smaller element</li>
<li><strong>STRING SIMULATION:</strong> Build result char-by-char using a stack</li>
</ul>
</div>

<div class="complexity-row">
<span class="complexity-badge"><span class="label">Time</span> O(n)</span>
<span class="complexity-badge"><span class="label">Space</span> O(n)</span>
</div>

```cpp
// Monotonic stack — Next Greater Element
vector<int> ans(nums.size(), -1);
stack<int> stk; // stores indices
for (int i = 0; i < nums.size(); i++) {
    while (!stk.empty() && nums[i] > nums[stk.top()]) {
        ans[stk.top()] = nums[i]; stk.pop();
    }
    stk.push(i);
}

// Bracket matching
stack<char> stk;
for (char c : s) {
    if (c == '(') stk.push(c);
    else if (!stk.empty() && stk.top() == '(') stk.pop();
    else return false;
}
return stk.empty();
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/valid-parentheses/" target="_blank" rel="noopener noreferrer">20. Valid Parentheses</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/simplify-path/" target="_blank" rel="noopener noreferrer">71. Simplify Path</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/make-the-string-great/" target="_blank" rel="noopener noreferrer">1544. Make The String Great</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/next-greater-element-i/" target="_blank" rel="noopener noreferrer">496. Next Greater Element I</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/online-stock-span/" target="_blank" rel="noopener noreferrer">901. Online Stock Span</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/daily-temperatures/" target="_blank" rel="noopener noreferrer">739. Daily Temperatures</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/asteroid-collision/" target="_blank" rel="noopener noreferrer">735. Asteroid Collision</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>8</td><td><a href="https://leetcode.com/problems/largest-rectangle-in-histogram/" target="_blank" rel="noopener noreferrer">84. Largest Rectangle in Histogram</a></td><td class="diff-hard">Hard</td></tr>
</tbody>
</table>

### 4.2 Queues &amp; Deques

<div class="pattern-box">
<ul>
<li><strong>BFS:</strong> uses a queue (FIFO) — process level by level</li>
<li><strong>SLIDING WINDOW MAXIMUM:</strong> Use deque to track max in O(1) per window</li>
<li><strong>MONOTONIC DEQUE:</strong> pop from front (expired) and back (smaller elements)</li>
</ul>
</div>

```cpp
// Sliding window max with deque
deque<int> dq; // stores indices
vector<int> ans;
for (int i = 0; i < nums.size(); i++) {
    while (!dq.empty() && dq.front() < i - k + 1) dq.pop_front(); // expired
    while (!dq.empty() && nums[dq.back()] < nums[i]) dq.pop_back();
    dq.push_back(i);
    if (i >= k - 1) ans.push_back(nums[dq.front()]);
}
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/moving-average-from-data-stream/" target="_blank" rel="noopener noreferrer">346. Moving Average from Data Stream</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/sliding-window-maximum/" target="_blank" rel="noopener noreferrer">239. Sliding Window Maximum</a></td><td class="diff-hard">Hard</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/design-circular-queue/" target="_blank" rel="noopener noreferrer">622. Design Circular Queue</a></td><td class="diff-medium">Medium</td></tr>
</tbody>
</table>

</div>

---

<div class="roadmap-chapter" id="ch5" markdown="1">

## Chapter 5 — Trees &amp; Graphs

<a href="{{ '/learning/dsa/tree/tree-problems/' | relative_url }}" class="topic-link-badge">🌳 Trees Problems Page →</a>
<a href="{{ '/learning/dsa/graphs/graphs-problems/' | relative_url }}" class="topic-link-badge">🕸️ Graphs Problems Page →</a>

### 5.1 Binary Trees — DFS

<div class="pattern-box">
<ul>
<li><strong>PREORDER</strong> (root→left→right): copying, serializing trees</li>
<li><strong>INORDER</strong> (left→root→right): sorted order for BST</li>
<li><strong>POSTORDER</strong> (left→right→root): deletion, computing subtree properties</li>
<li><strong>GLOBAL vs LOCAL:</strong> use a global variable for answers spanning multiple nodes (diameter)</li>
<li><strong>Return value pattern:</strong> return meaningful data upward (height, sum, etc.)</li>
</ul>
</div>

```cpp
// Recursive DFS
int dfs(TreeNode* node) {
    if (!node) return 0;  // base case
    int left  = dfs(node->left);
    int right = dfs(node->right);
    return 1 + max(left, right); // example: height
}

// Iterative DFS (preorder)
stack<TreeNode*> stk; stk.push(root);
while (!stk.empty()) {
    TreeNode* node = stk.top(); stk.pop();
    // process node
    if (node->right) stk.push(node->right);
    if (node->left)  stk.push(node->left);
}
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/minimum-depth-of-binary-tree/" target="_blank" rel="noopener noreferrer">111. Minimum Depth of Binary Tree</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/" target="_blank" rel="noopener noreferrer">104. Maximum Depth of Binary Tree</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/diameter-of-binary-tree/" target="_blank" rel="noopener noreferrer">543. Diameter of Binary Tree</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/" target="_blank" rel="noopener noreferrer">1026. Maximum Difference Between Node and Ancestor</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/path-sum-ii/" target="_blank" rel="noopener noreferrer">113. Path Sum II</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/" target="_blank" rel="noopener noreferrer">236. Lowest Common Ancestor of a Binary Tree</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/binary-tree-maximum-path-sum/" target="_blank" rel="noopener noreferrer">124. Binary Tree Maximum Path Sum</a></td><td class="diff-hard">Hard</td></tr>
</tbody>
</table>

### 5.2 Binary Trees — BFS

```cpp
queue<TreeNode*> q; q.push(root);
while (!q.empty()) {
    int sz = q.size(); // current level size
    for (int i = 0; i < sz; i++) {
        TreeNode* node = q.front(); q.pop();
        // process node
        if (node->left)  q.push(node->left);
        if (node->right) q.push(node->right);
    }
}
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/binary-tree-level-order-traversal/" target="_blank" rel="noopener noreferrer">102. Binary Tree Level Order Traversal</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/deepest-leaves-sum/" target="_blank" rel="noopener noreferrer">1302. Deepest Leaves Sum</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/" target="_blank" rel="noopener noreferrer">103. Binary Tree Zigzag Level Order Traversal</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/average-of-levels-in-binary-tree/" target="_blank" rel="noopener noreferrer">637. Average of Levels in Binary Tree</a></td><td class="diff-easy">Easy</td></tr>
</tbody>
</table>

### 5.3 Binary Search Trees (BST)

<div class="pattern-box">
<ul>
<li>In a valid BST: left subtree values &lt; node &lt; right subtree values</li>
<li>Inorder traversal gives sorted array — useful for validation and kth smallest</li>
<li>BST search is O(h): O(log n) balanced, O(n) skewed</li>
</ul>
</div>

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/insert-into-a-binary-search-tree/" target="_blank" rel="noopener noreferrer">701. Insert into a Binary Search Tree</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/closest-binary-search-tree-value/" target="_blank" rel="noopener noreferrer">270. Closest Binary Search Tree Value</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/validate-binary-search-tree/" target="_blank" rel="noopener noreferrer">98. Validate Binary Search Tree</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/kth-smallest-element-in-a-bst/" target="_blank" rel="noopener noreferrer">230. Kth Smallest Element in a BST</a></td><td class="diff-medium">Medium</td></tr>
</tbody>
</table>

### 5.4 Graphs — DFS &amp; BFS

<div class="pattern-box">
<ul>
<li><strong>ADJACENCY LIST:</strong> vector&lt;vector&lt;int&gt;&gt; adj(n) — most common representation</li>
<li><strong>VISITED SET:</strong> Always track visited to avoid cycles/revisiting</li>
<li><strong>DFS:</strong> Path existence, connected components, topological sort</li>
<li><strong>BFS:</strong> Shortest path (unweighted), level-by-level, nearest cell in grid</li>
<li><strong>UNION-FIND:</strong> Efficient for connected components, cycle detection in undirected graphs</li>
</ul>
</div>

```cpp
// Graph BFS — shortest path (unweighted)
vector<int> dist(n, -1);
queue<int> q;
q.push(start); dist[start] = 0;
while (!q.empty()) {
    int node = q.front(); q.pop();
    for (int nei : adj[node]) {
        if (dist[nei] == -1) { dist[nei] = dist[node]+1; q.push(nei); }
    }
}

// Union-Find (path compression + union by rank)
vector<int> parent(n), rank(n, 0);
iota(parent.begin(), parent.end(), 0);
function<int(int)> find = [&](int x) {
    return parent[x] == x ? x : parent[x] = find(parent[x]);
};
auto unite = [&](int a, int b) {
    a = find(a); b = find(b);
    if (a == b) return;
    if (rank[a] < rank[b]) swap(a, b);
    parent[b] = a;
    if (rank[a] == rank[b]) rank[a]++;
};
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/find-if-path-exists-in-graph/" target="_blank" rel="noopener noreferrer">1971. Find if Path Exists in Graph</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/max-area-of-island/" target="_blank" rel="noopener noreferrer">695. Max Area of Island</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/" target="_blank" rel="noopener noreferrer">1926. Nearest Exit from Entrance in Maze</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/snakes-and-ladders/" target="_blank" rel="noopener noreferrer">909. Snakes and Ladders</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/minimum-genetic-mutation/" target="_blank" rel="noopener noreferrer">433. Minimum Genetic Mutation</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/jump-game-iii/" target="_blank" rel="noopener noreferrer">1306. Jump Game III</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/detonate-the-maximum-bombs/" target="_blank" rel="noopener noreferrer">2101. Detonate the Maximum Bombs</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>8</td><td><a href="https://leetcode.com/problems/word-ladder/" target="_blank" rel="noopener noreferrer">127. Word Ladder</a></td><td class="diff-hard">Hard</td></tr>
<tr><td>9</td><td><a href="https://leetcode.com/problems/number-of-islands/" target="_blank" rel="noopener noreferrer">200. Number of Islands</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>10</td><td><a href="https://leetcode.com/problems/course-schedule/" target="_blank" rel="noopener noreferrer">207. Course Schedule</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>11</td><td><a href="https://leetcode.com/problems/clone-graph/" target="_blank" rel="noopener noreferrer">133. Clone Graph</a></td><td class="diff-medium">Medium</td></tr>
</tbody>
</table>

</div>

---

<div class="roadmap-chapter" id="ch6" markdown="1">

## Chapter 6 — Heaps

Min-heap: parent ≤ children. **O(log n) insert/remove. O(1) peek.** C++ `priority_queue` defaults to max-heap.

<div class="pattern-box">
<ul>
<li><strong>TOP K:</strong> Min-heap of size k — push each element; if size &gt; k, pop. Final heap = top k largest</li>
<li><strong>K-WAY MERGE:</strong> Push (value, listIndex, elemIndex) into heap. Always pop smallest</li>
<li><strong>RUNNING MEDIAN:</strong> Max-heap for lower half + min-heap for upper half</li>
<li>'Smallest/Largest K elements' → heap. 'Kth element' → partial sort or heap</li>
</ul>
</div>

<div class="complexity-row">
<span class="complexity-badge"><span class="label">Time</span> O(log n) push/pop</span>
<span class="complexity-badge"><span class="label">Space</span> O(n)</span>
</div>

```cpp
// Min-heap
priority_queue<int, vector<int>, greater<int>> minHeap;

// Top-K largest elements using min-heap of size K
priority_queue<int, vector<int>, greater<int>> pq;
for (int x : nums) {
    pq.push(x);
    if (pq.size() > k) pq.pop();
}
// pq.top() = kth largest

// Custom comparator (min-heap by first element of pair)
auto cmp = [](pair<int,int>& a, pair<int,int>& b){ return a.first > b.first; };
priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(cmp)> pq(cmp);
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/remove-stones-to-minimize-the-total/" target="_blank" rel="noopener noreferrer">1962. Remove Stones to Minimize the Total</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/minimum-cost-to-connect-sticks/" target="_blank" rel="noopener noreferrer">1167. Minimum Cost to Connect Sticks</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/kth-largest-element-in-an-array/" target="_blank" rel="noopener noreferrer">215. Kth Largest Element in an Array</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/k-closest-points-to-origin/" target="_blank" rel="noopener noreferrer">973. K Closest Points to Origin</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/kth-largest-element-in-a-stream/" target="_blank" rel="noopener noreferrer">703. Kth Largest Element in a Stream</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/find-median-from-data-stream/" target="_blank" rel="noopener noreferrer">295. Find Median from Data Stream</a></td><td class="diff-hard">Hard</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/task-scheduler/" target="_blank" rel="noopener noreferrer">621. Task Scheduler</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>8</td><td><a href="https://leetcode.com/problems/merge-k-sorted-lists/" target="_blank" rel="noopener noreferrer">23. Merge K Sorted Lists</a></td><td class="diff-hard">Hard</td></tr>
</tbody>
</table>

</div>

---

<div class="roadmap-chapter" id="ch7" markdown="1">

## Chapter 7 — Greedy Algorithms

Make the **locally optimal choice** at each step. Greedy works when local optimum leads to global optimum (proven via exchange argument).

<div class="pattern-box">
<ul>
<li><strong>SORT FIRST:</strong> Most greedy problems require sorting by some key (weight, ratio, end time)</li>
<li><strong>INTERVAL SCHEDULING:</strong> Sort by end time. Greedily take non-overlapping intervals</li>
<li><strong>EXCHANGE ARGUMENT:</strong> Prove swapping adjacent elements doesn't improve solution</li>
<li>Ask: 'Does taking the best local choice now ever block a better global solution?' If no → greedy works</li>
</ul>
</div>

<div class="complexity-row">
<span class="complexity-badge"><span class="label">Time</span> O(n log n) with sort</span>
<span class="complexity-badge"><span class="label">Space</span> O(1)</span>
</div>

```cpp
// Interval scheduling — max non-overlapping intervals
sort(intervals.begin(), intervals.end(),
    [](auto& a, auto& b){ return a[1] < b[1]; }); // sort by end
int count = 0, prevEnd = INT_MIN;
for (auto& iv : intervals) {
    if (iv[0] >= prevEnd) { count++; prevEnd = iv[1]; }
}
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/maximum-69-number/" target="_blank" rel="noopener noreferrer">1323. Maximum 69 Number</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/maximum-units-on-a-truck/" target="_blank" rel="noopener noreferrer">1710. Maximum Units on a Truck</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/reduce-array-size-to-the-half/" target="_blank" rel="noopener noreferrer">1338. Reduce Array Size to The Half</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/non-overlapping-intervals/" target="_blank" rel="noopener noreferrer">435. Non-overlapping Intervals</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/jump-game/" target="_blank" rel="noopener noreferrer">55. Jump Game</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/jump-game-ii/" target="_blank" rel="noopener noreferrer">45. Jump Game II</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/gas-station/" target="_blank" rel="noopener noreferrer">134. Gas Station</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>8</td><td><a href="https://leetcode.com/problems/candy/" target="_blank" rel="noopener noreferrer">135. Candy</a></td><td class="diff-hard">Hard</td></tr>
</tbody>
</table>

</div>

---

<div class="roadmap-chapter" id="ch8" markdown="1">

## Chapter 8 — Binary Search

Reduces search space by half each step. **O(log n).** Works on any monotonic function — not just sorted arrays.

<a href="{{ '/learning/dsa/searching-sorting/searching-sorting-problems/' | relative_url }}" class="topic-link-badge">🔍 Searching &amp; Sorting Problems Page →</a>

<div class="pattern-box">
<ul>
<li><strong>ON SORTED ARRAY:</strong> Classic search / find leftmost or rightmost position</li>
<li><strong>ON ANSWER SPACE:</strong> Binary search on the answer when answer has a range and feasibility is monotonic</li>
<li><strong>FIND LEFTMOST:</strong> Use 'left = mid + 1' when condition met to push left boundary right</li>
<li>Trigger phrase: <em>'minimize the maximum'</em> or <em>'maximize the minimum'</em> → binary search on answer</li>
<li>Template: lo=0, hi=n-1. Always move lo or hi strictly — never infinite loop</li>
</ul>
</div>

<div class="complexity-row">
<span class="complexity-badge"><span class="label">Time</span> O(log n)</span>
<span class="complexity-badge"><span class="label">Space</span> O(1)</span>
</div>

```cpp
// Standard binary search
int lo = 0, hi = nums.size() - 1;
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2; // avoid overflow
    if (nums[mid] == target) return mid;
    else if (nums[mid] < target) lo = mid + 1;
    else hi = mid - 1;
}

// Binary search on answer space
int lo = minVal, hi = maxVal, ans = hi;
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;
    if (feasible(mid)) { ans = mid; hi = mid - 1; } // want minimum feasible
    else lo = mid + 1;
}
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/binary-search/" target="_blank" rel="noopener noreferrer">704. Binary Search</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/search-insert-position/" target="_blank" rel="noopener noreferrer">35. Search Insert Position</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/longest-subsequence-with-limited-sum/" target="_blank" rel="noopener noreferrer">2389. Longest Subsequence With Limited Sum</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/" target="_blank" rel="noopener noreferrer">1283. Find the Smallest Divisor Given a Threshold</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/split-array-largest-sum/" target="_blank" rel="noopener noreferrer">410. Split Array Largest Sum</a></td><td class="diff-hard">Hard</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/koko-eating-bananas/" target="_blank" rel="noopener noreferrer">875. Koko Eating Bananas</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/find-peak-element/" target="_blank" rel="noopener noreferrer">162. Find Peak Element</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>8</td><td><a href="https://leetcode.com/problems/search-in-rotated-sorted-array/" target="_blank" rel="noopener noreferrer">33. Search in Rotated Sorted Array</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>9</td><td><a href="https://leetcode.com/problems/median-of-two-sorted-arrays/" target="_blank" rel="noopener noreferrer">4. Median of Two Sorted Arrays</a></td><td class="diff-hard">Hard</td></tr>
</tbody>
</table>

</div>

---

<div class="roadmap-chapter" id="ch9" markdown="1">

## Chapter 9 — Backtracking

Systematically explore all possibilities by building candidates incrementally and **pruning** those that can't lead to a valid solution.

<div class="pattern-box">
<ul>
<li><strong>GENERATION:</strong> Build all permutations/subsets/combinations — just enumerate</li>
<li><strong>CONSTRAINED:</strong> Prune early when constraint violated (e.g. sum exceeds target)</li>
<li>Template: choose → recurse → unchoose (restore state)</li>
<li>Use 'start' index to avoid re-using earlier elements in combination problems</li>
<li>Use 'used[]' boolean array for permutations to avoid duplicate positions</li>
<li>Time: O(n! × n) for permutations, O(2ⁿ × n) for subsets — always exponential</li>
</ul>
</div>

```cpp
// Generic backtracking
vector<vector<int>> result;
vector<int> current;

void backtrack(int start) {
    if (isComplete()) { result.push_back(current); return; }
    for (int i = start; i < candidates.size(); i++) {
        if (shouldPrune(i)) continue;
        current.push_back(candidates[i]);  // choose
        backtrack(i + 1);                  // recurse
        current.pop_back();                // unchoose
    }
}
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/all-paths-from-source-to-target/" target="_blank" rel="noopener noreferrer">797. All Paths From Source to Target</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/" target="_blank" rel="noopener noreferrer">17. Letter Combinations of a Phone Number</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/generate-parentheses/" target="_blank" rel="noopener noreferrer">22. Generate Parentheses</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/numbers-with-same-consecutive-differences/" target="_blank" rel="noopener noreferrer">967. Numbers With Same Consecutive Differences</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/combination-sum-iii/" target="_blank" rel="noopener noreferrer">216. Combination Sum III</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/subsets/" target="_blank" rel="noopener noreferrer">78. Subsets</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/permutations/" target="_blank" rel="noopener noreferrer">46. Permutations</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>8</td><td><a href="https://leetcode.com/problems/combination-sum/" target="_blank" rel="noopener noreferrer">39. Combination Sum</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>9</td><td><a href="https://leetcode.com/problems/word-search/" target="_blank" rel="noopener noreferrer">79. Word Search</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>10</td><td><a href="https://leetcode.com/problems/n-queens/" target="_blank" rel="noopener noreferrer">51. N-Queens</a></td><td class="diff-hard">Hard</td></tr>
<tr><td>11</td><td><a href="https://leetcode.com/problems/sudoku-solver/" target="_blank" rel="noopener noreferrer">37. Sudoku Solver</a></td><td class="diff-hard">Hard</td></tr>
</tbody>
</table>

</div>

---

<div class="roadmap-chapter" id="ch10" markdown="1">

## Chapter 10 — Dynamic Programming

DP solves problems with **overlapping subproblems** and **optimal substructure**. Two approaches: Top-down (memoization) and Bottom-up (tabulation).

<div class="pattern-box">
<ul>
<li><strong>Step 1:</strong> Define what dp[i] (or dp[i][j]) represents</li>
<li><strong>Step 2:</strong> Find the recurrence relation (transition)</li>
<li><strong>Step 3:</strong> Identify base cases</li>
<li><strong>Step 4:</strong> Determine iteration order (ensure subproblems solved before needed)</li>
<li>DP vs Greedy: DP explores all choices; Greedy makes one. Use DP when greedy fails</li>
</ul>
</div>

```cpp
// 1D DP — Climbing Stairs
vector<int> dp(n + 1, 0);
dp[0] = 1; dp[1] = 1;
for (int i = 2; i <= n; i++) dp[i] = dp[i-1] + dp[i-2];

// Coin Change (unbounded knapsack)
vector<int> dp(amount + 1, INT_MAX); dp[0] = 0;
for (int i = 1; i <= amount; i++)
    for (int coin : coins)
        if (coin <= i && dp[i - coin] != INT_MAX)
            dp[i] = min(dp[i], dp[i - coin] + 1);

// State machine DP (Stock with cooldown)
int hold = -prices[0], sold = 0, rest = 0;
for (int i = 1; i < prices.size(); i++) {
    int ph = hold, ps = sold, pr = rest;
    hold = max(ph, pr - prices[i]);
    sold = ph + prices[i];
    rest = max(pr, ps);
}
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/climbing-stairs/" target="_blank" rel="noopener noreferrer">70. Climbing Stairs</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/min-cost-climbing-stairs/" target="_blank" rel="noopener noreferrer">746. Min Cost Climbing Stairs</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/coin-change/" target="_blank" rel="noopener noreferrer">322. Coin Change</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/" target="_blank" rel="noopener noreferrer">714. Best Time to Buy and Sell Stock with Transaction Fee</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/" target="_blank" rel="noopener noreferrer">309. Best Time to Buy and Sell Stock with Cooldown</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/unique-paths-ii/" target="_blank" rel="noopener noreferrer">63. Unique Paths II</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>7</td><td><a href="https://leetcode.com/problems/minimum-falling-path-sum/" target="_blank" rel="noopener noreferrer">931. Minimum Falling Path Sum</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>8</td><td><a href="https://leetcode.com/problems/house-robber/" target="_blank" rel="noopener noreferrer">198. House Robber</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>9</td><td><a href="https://leetcode.com/problems/longest-common-subsequence/" target="_blank" rel="noopener noreferrer">1143. Longest Common Subsequence</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>10</td><td><a href="https://leetcode.com/problems/edit-distance/" target="_blank" rel="noopener noreferrer">72. Edit Distance</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>11</td><td><a href="https://leetcode.com/problems/word-break/" target="_blank" rel="noopener noreferrer">139. Word Break</a></td><td class="diff-medium">Medium</td></tr>
</tbody>
</table>

</div>

---

<div class="roadmap-chapter" id="ch11" markdown="1">

## Chapter 11 — Bonus Topics

### 11.1 Tries (Prefix Trees)

<div class="pattern-box">
<ul>
<li>Store strings character by character. Each node = one character</li>
<li>isEnd flag marks end of a valid word</li>
<li>Use for: autocomplete, spell check, prefix search, word dictionaries</li>
<li>O(m) insert and search where m = string length</li>
</ul>
</div>

```cpp
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEnd = false;
};
struct Trie {
    TrieNode* root = new TrieNode();
    void insert(string s) {
        TrieNode* node = root;
        for (char c : s) {
            if (!node->children.count(c)) node->children[c] = new TrieNode();
            node = node->children[c];
        }
        node->isEnd = true;
    }
    bool search(string s) {
        TrieNode* node = root;
        for (char c : s) {
            if (!node->children.count(c)) return false;
            node = node->children[c];
        }
        return node->isEnd;
    }
};
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/implement-trie-prefix-tree/" target="_blank" rel="noopener noreferrer">208. Implement Trie (Prefix Tree)</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/word-search-ii/" target="_blank" rel="noopener noreferrer">212. Word Search II</a></td><td class="diff-hard">Hard</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/design-add-and-search-words-data-structure/" target="_blank" rel="noopener noreferrer">211. Design Add and Search Words Data Structure</a></td><td class="diff-medium">Medium</td></tr>
</tbody>
</table>

### 11.2 Bit Manipulation

<div class="pattern-box">
<ul>
<li>AND (&amp;): mask bits, check if bit set. n &amp; (n-1) clears lowest set bit</li>
<li>OR (|): set bits. XOR (^): toggle bits, find single element (a^a=0, a^0=a)</li>
<li>Left shift (&lt;&lt;): multiply by 2. Right shift (&gt;&gt;): divide by 2</li>
<li>Check kth bit: (n &gt;&gt; k) &amp; 1. Set: n | (1 &lt;&lt; k). Clear: n &amp; ~(1 &lt;&lt; k)</li>
</ul>
</div>

```cpp
// XOR trick: find single number
int result = 0;
for (int x : nums) result ^= x;

// Clear lowest set bit each iteration
int countBits(int n) {
    int count = 0;
    while (n) { n &= (n-1); count++; }
    return count;
}

bool isPow2(int n) { return n > 0 && (n & (n-1)) == 0; }
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/hamming-distance/" target="_blank" rel="noopener noreferrer">461. Hamming Distance</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/single-number/" target="_blank" rel="noopener noreferrer">136. Single Number</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/number-of-1-bits/" target="_blank" rel="noopener noreferrer">191. Number of 1 Bits</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/counting-bits/" target="_blank" rel="noopener noreferrer">338. Counting Bits</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/reverse-bits/" target="_blank" rel="noopener noreferrer">190. Reverse Bits</a></td><td class="diff-easy">Easy</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/sum-of-two-integers/" target="_blank" rel="noopener noreferrer">371. Sum of Two Integers</a></td><td class="diff-medium">Medium</td></tr>
</tbody>
</table>

### 11.3 Intervals

<div class="pattern-box">
<ul>
<li>SORT by start time. Merge if curr.start ≤ prev.end</li>
<li>MEETING ROOMS: Count overlaps — use event sweep (start +1, end -1)</li>
<li>DIFFERENCE ARRAY: Efficient range update — inc start, dec end+1</li>
</ul>
</div>

```cpp
// Merge intervals
sort(intervals.begin(), intervals.end());
vector<vector<int>> merged;
for (auto& iv : intervals) {
    if (!merged.empty() && iv[0] <= merged.back()[1])
        merged.back()[1] = max(merged.back()[1], iv[1]);
    else merged.push_back(iv);
}

// Difference array: range [l,r] += val
vector<int> diff(n + 1, 0);
diff[l] += val; diff[r+1] -= val;
// Reconstruct: result[i] = result[i-1] + diff[i]
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/insert-interval/" target="_blank" rel="noopener noreferrer">57. Insert Interval</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/merge-intervals/" target="_blank" rel="noopener noreferrer">56. Merge Intervals</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/non-overlapping-intervals/" target="_blank" rel="noopener noreferrer">435. Non-overlapping Intervals</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>4</td><td><a href="https://leetcode.com/problems/meeting-rooms-ii/" target="_blank" rel="noopener noreferrer">253. Meeting Rooms II</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>5</td><td><a href="https://leetcode.com/problems/car-pooling/" target="_blank" rel="noopener noreferrer">1094. Car Pooling</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>6</td><td><a href="https://leetcode.com/problems/corporate-flight-bookings/" target="_blank" rel="noopener noreferrer">1109. Corporate Flight Bookings</a></td><td class="diff-medium">Medium</td></tr>
</tbody>
</table>

### 11.4 Dijkstra's Algorithm

Shortest path in weighted graph with **non-negative weights**. O((V + E) log V) with heap.

```cpp
vector<int> dijkstra(int src, vector<vector<pair<int,int>>>& adj, int n) {
    vector<int> dist(n, INT_MAX);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    dist[src] = 0; pq.push({0, src});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue; // stale entry
        for (auto [w, v] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}
```

<table class="roadmap-table">
<thead><tr><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="https://leetcode.com/problems/cheapest-flights-within-k-stops/" target="_blank" rel="noopener noreferrer">787. Cheapest Flights Within K Stops</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>2</td><td><a href="https://leetcode.com/problems/network-delay-time/" target="_blank" rel="noopener noreferrer">743. Network Delay Time</a></td><td class="diff-medium">Medium</td></tr>
<tr><td>3</td><td><a href="https://leetcode.com/problems/path-with-minimum-effort/" target="_blank" rel="noopener noreferrer">1631. Path with Minimum Effort</a></td><td class="diff-medium">Medium</td></tr>
</tbody>
</table>

</div>

---

<div class="roadmap-chapter" id="ch12" markdown="1">

## Chapter 12 — Study Plan &amp; Interview Cheatsheet

### Recommended Study Order

<ol class="study-order">
<li>Big O + Recursion — non-negotiable foundation</li>
<li>Arrays: Two Pointers → Sliding Window → Prefix Sum</li>
<li>Hashing — amplifies every pattern you've learned</li>
<li>Linked Lists — pointer manipulation</li>
<li>Stacks &amp; Queues — essential for tree/graph traversal</li>
<li>Binary Trees (DFS → BFS) → BST</li>
<li>Graphs (DFS → BFS → Union-Find)</li>
<li>Binary Search</li>
<li>Heaps</li>
<li>Greedy</li>
<li>Backtracking</li>
<li>Dynamic Programming (1D → 2D → State Machine)</li>
<li>Bonus: Tries, Bit Manipulation, Intervals, Dijkstra's</li>
</ol>

### Problem-Type → Pattern Cheatsheet

<div class="cheatsheet-grid">
<div class="cheatsheet-card">
<h4>Pattern Selection</h4>
<table>
<thead><tr><th>Problem Type</th><th>Pattern</th></tr></thead>
<tbody>
<tr><td>Subarray with constraint</td><td>Sliding Window</td></tr>
<tr><td>Pair/triple in sorted array</td><td>Two Pointers</td></tr>
<tr><td>Range sum queries</td><td>Prefix Sum</td></tr>
<tr><td>Frequency / existence</td><td>Hashmap / Set</td></tr>
<tr><td>Shortest path (unweighted)</td><td>BFS</td></tr>
<tr><td>Shortest path (weighted)</td><td>Dijkstra's</td></tr>
<tr><td>All paths / combinations</td><td>Backtracking</td></tr>
<tr><td>Optimal substructure + overlap</td><td>Dynamic Programming</td></tr>
<tr><td>Best local choice works globally</td><td>Greedy</td></tr>
<tr><td>Top K / Kth element</td><td>Heap</td></tr>
<tr><td>Sorted array search</td><td>Binary Search</td></tr>
<tr><td>Minimize max / maximize min</td><td>Binary Search on Answer</td></tr>
<tr><td>Next greater/smaller element</td><td>Monotonic Stack</td></tr>
<tr><td>Prefix search / autocomplete</td><td>Trie</td></tr>
<tr><td>Connected components</td><td>BFS/DFS or Union-Find</td></tr>
<tr><td>Tree path / subtree property</td><td>DFS (recursive)</td></tr>
</tbody>
</table>
</div>
<div class="cheatsheet-card">
<h4>Complexity Quick Reference</h4>
<table>
<thead><tr><th>Algorithm / DS</th><th>Time</th><th>Space</th></tr></thead>
<tbody>
<tr><td>Two Pointers / Sliding Window</td><td>O(n)</td><td>O(1)</td></tr>
<tr><td>Prefix Sum (build)</td><td>O(n)</td><td>O(n)</td></tr>
<tr><td>Hash map ops</td><td>O(1) avg</td><td>O(n)</td></tr>
<tr><td>Binary Search</td><td>O(log n)</td><td>O(1)</td></tr>
<tr><td>Merge Sort / Heap Sort</td><td>O(n log n)</td><td>O(n)</td></tr>
<tr><td>BFS / DFS (graph)</td><td>O(V + E)</td><td>O(V)</td></tr>
<tr><td>Dijkstra's</td><td>O((V+E) log V)</td><td>O(V)</td></tr>
<tr><td>Heap push/pop</td><td>O(log n)</td><td>O(n)</td></tr>
<tr><td>Backtracking (subsets)</td><td>O(2ⁿ × n)</td><td>O(n)</td></tr>
<tr><td>Backtracking (perms)</td><td>O(n!)</td><td>O(n)</td></tr>
<tr><td>Trie insert/search</td><td>O(m)</td><td>O(m×n)</td></tr>
<tr><td>Union-Find</td><td>O(α(n)) ≈ O(1)</td><td>O(n)</td></tr>
</tbody>
</table>
</div>
</div>

### Interview Stage Checklist

**Before Coding** — Clarify constraints, edge cases, expected output. State your approach in plain English. Discuss time/space complexity of your plan.

**While Coding** — Write clean, readable code. Talk through your logic. Handle edge cases (empty input, single element, negatives).

**After Coding** — Trace through your code with the example. State time and space complexity. Suggest optimizations if time permits.

</div>

---

<div style="text-align: center; margin-top: 3rem; padding: 2rem; background: var(--bg-color); border-radius: 12px; border: 1px solid var(--border-color);">
  <p style="font-weight: 700; font-size: 1.1rem; color: var(--post-heading); margin-bottom: 1rem;">Ready to practice?</p>
  <a href="{{ '/problems/' | relative_url }}" style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.75rem 2rem;background:linear-gradient(135deg,#00d4ff,#ff6b9d);color:#1a1f36;border-radius:8px;font-weight:800;text-decoration:none;font-size:1rem;">🎯 Open Problems Hub</a>
</div>
