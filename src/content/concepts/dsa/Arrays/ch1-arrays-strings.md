---
title: "Ch1 — Arrays & Strings"
description: "All Roadmaps › DSA Mastery › Chapter 1 Chapter 1 · Intermediate · Prereq: Chapter 0 Arrays & Strings Two Pointers · Sliding Window · Prefix Sum — three universal patterns that…"
domain: dsa
track: dsa-mastery
order: 1
chrome: bare
ownHeader: true
url: /learning/dsa/arrays/ch1-arrays-strings/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<div class="chapter-hero">
  <div class="chapter-hero-inner">
    <div class="ch-hero-breadcrumb">
      <a href="/roadmap/">All Roadmaps</a> ›
      <a href="/learning/dsa/dsa-roadmap/">DSA Mastery</a> ›
      Chapter 1
    </div>
    <div class="chapter-num-badge">Chapter 1 · Intermediate · Prereq: Chapter 0</div>
    <h1>Arrays & Strings</h1>
    <p class="chapter-hero-sub">Two Pointers · Sliding Window · Prefix Sum — three universal patterns that reduce O(n²) brute-force solutions to O(n). Mastering this chapter unlocks solutions to hundreds of problems.</p>
    <div class="chapter-meta-row">
      <span class="ch-meta-pill teal">11 Sections</span>
      <span class="ch-meta-pill">26 Practice Problems</span>
      <span class="ch-meta-pill">Intermediate</span>
      <a href="/learning/dsa/dsa-roadmap/#ch1" class="ch-nav-btn">← Back to Roadmap</a>
    </div>
  </div>
</div>
<div class="chapter-content">
<div class="chapter-section">
<h2 class="section-heading">Section 1 — What Are Arrays & Strings?</h2>
<p>Arrays and strings are the most common data structures in coding interviews. Nearly every problem — regardless of topic — involves manipulating sequences of elements.</p>
<h3 class="section-subheading">1.1 — Arrays</h3>
<p>An array is a contiguous block of memory storing elements of the same type. The key property is <strong>O(1) random access</strong> — given an index, computing the memory address is a single arithmetic operation.</p>
<div class="insight-box">
  <span class="insight-label">Array Complexity Summary</span>
  <ul>
    <li><strong>Access by index:</strong> O(1)</li>
    <li><strong>Search (unsorted):</strong> O(n)</li>
    <li><strong>Search (sorted + binary search):</strong> O(log n)</li>
    <li><strong>Insert/Delete at end:</strong> O(1) amortized</li>
    <li><strong>Insert/Delete at middle:</strong> O(n) — elements must shift</li>
  </ul>
</div>
<h3 class="section-subheading">1.2 — Strings in C++</h3>
<p>C++ strings are mutable arrays of characters with O(1) random access. Key operations to know:</p>
<div class="ch-code-wrap">
```cpp
string s = "hello world";
s.length();         // O(1) — size cached
s.substr(2, 4);     // O(k) — creates new string of length k
s[i];               // O(1) — direct access
s += "!";           // O(n) amortized — appending
sort(s.begin(), s.end()); // O(n log n)
// Reverse a string in-place O(n)
reverse(s.begin(), s.end());
// Convert int ↔ string
int n = stoi("42");   // string to int
string t = to_string(99); // int to string
```
</div>
</div>
<div class="chapter-section">
<h2 class="section-heading">Section 2 — Pattern: Two Pointers</h2>
<p>Two Pointers eliminates an inner loop by maintaining two indices that together cover the search space. Result: O(n²) → O(n).</p>
<h3 class="section-subheading">2.1 — Opposite-End Pointers</h3>
<p>Start with left=0 and right=n-1. Move inward based on a condition. Converge in O(n).</p>
<div class="insight-box">
  <span class="insight-label">When to Use Opposite-End</span>
  <ul>
    <li>Array is <strong>sorted</strong> (or can be sorted without losing information)</li>
    <li>Looking for a <strong>pair</strong> (two-sum, palindrome check, container with most water)</li>
    <li>Need to <strong>squeeze from both ends</strong> (trapping rain water)</li>
  </ul>
</div>
<div class="ch-code-wrap">
```cpp
// Palindrome check — O(n) time, O(1) space
int left = 0, right = s.size()-1;
while (left < right) {
    if (s[left] != s[right]) return false;
    left++; right--;
}
return true;
// Two-sum on sorted array — O(n) time, O(1) space
while (left < right) {
    int sum = nums[left] + nums[right];
    if (sum == target) return {left, right};
    else if (sum < target) left++;
    else right--;
}
```
</div>
<h3 class="section-subheading">2.2 — Fast/Slow Pointers (Same Direction)</h3>
<p>Both pointers move right, but at different speeds or with different conditions. Used to filter or compact arrays in-place.</p>
<div class="ch-code-wrap">
```cpp
// Remove duplicates from sorted array — slow tracks write head
int slow = 0;
for (int fast = 1; fast < nums.size(); fast++) {
    if (nums[fast] != nums[slow]) nums[++slow] = nums[fast];
}
return slow + 1; // new length

// Move zeroes to end — preserve relative order
int slow = 0;
for (int fast = 0; fast < nums.size(); fast++)
    if (nums[fast]) nums[slow++] = nums[fast];
while (slow < nums.size()) nums[slow++] = 0;

// Is Subsequence — two pointers on two arrays
int i = 0, j = 0;
while (i < s.size() && j < t.size())
    if (s[i] == t[j++]) i++;
return i == s.size();
```
</div>
<div class="ch-cplx-row">
  <span class="ch-cplx"><span>Time</span>O(n)</span>
  <span class="ch-cplx"><span>Space</span>O(1)</span>
</div>
<div class="ch-ed-problems">
<table>
  <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><a href="https://leetcode.com/problems/valid-palindrome/" target="_blank">125. Valid Palindrome</a></td><td>Opposite-end</td><td class="diff-easy">Easy</td></tr>
    <tr><td>2</td><td><a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/" target="_blank">167. Two Sum II</a></td><td>Opposite-end (sorted)</td><td class="diff-medium">Medium</td></tr>
    <tr><td>3</td><td><a href="https://leetcode.com/problems/reverse-string/" target="_blank">344. Reverse String</a></td><td>Opposite-end swap</td><td class="diff-easy">Easy</td></tr>
    <tr><td>4</td><td><a href="https://leetcode.com/problems/squares-of-a-sorted-array/" target="_blank">977. Squares of a Sorted Array</a></td><td>Opposite-end merge</td><td class="diff-easy">Easy</td></tr>
    <tr><td>5</td><td><a href="https://leetcode.com/problems/move-zeroes/" target="_blank">283. Move Zeroes</a></td><td>Fast/Slow (same dir)</td><td class="diff-easy">Easy</td></tr>
    <tr><td>6</td><td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/" target="_blank">26. Remove Duplicates from Sorted Array</a></td><td>Fast/Slow (write head)</td><td class="diff-easy">Easy</td></tr>
    <tr><td>7</td><td><a href="https://leetcode.com/problems/is-subsequence/" target="_blank">392. Is Subsequence</a></td><td>Two-array pointers</td><td class="diff-easy">Easy</td></tr>
    <tr><td>8</td><td><a href="https://leetcode.com/problems/3sum/" target="_blank">15. 3Sum</a></td><td>Sort + opposite-end</td><td class="diff-medium">Medium</td></tr>
    <tr><td>9</td><td><a href="https://leetcode.com/problems/container-with-most-water/" target="_blank">11. Container With Most Water</a></td><td>Opposite-end (greedy)</td><td class="diff-medium">Medium</td></tr>
    <tr><td>10</td><td><a href="https://leetcode.com/problems/trapping-rain-water/" target="_blank">42. Trapping Rain Water</a></td><td>Two-pointer + max tracking</td><td class="diff-hard">Hard</td></tr>
  </tbody>
</table>
</div>
</div>
<div class="chapter-section">
<h2 class="section-heading">Section 3 — Pattern: Sliding Window</h2>
<p>A window is a contiguous subarray [left, right]. Sliding Window maintains and updates a window as right expands — avoiding recompution by only adding/removing boundary elements.</p>
<div class="insight-box">
  <span class="insight-label">Two Sliding Window Variants</span>
  <ul>
    <li><strong>Variable size window:</strong> expand right always, shrink left while a constraint is violated. Used for 'longest subarray satisfying condition'.</li>
    <li><strong>Fixed size window (size k):</strong> slide — add nums[right], subtract nums[right-k] each step. Used for 'average/max/sum over every window of size k'.</li>
  </ul>
</div>
<h3 class="section-subheading">3.1 — Variable-Size Window</h3>
<div class="ch-code-wrap">
```cpp
// Longest subarray with sum ≤ k
int left = 0, curr = 0, ans = 0;
for (int right = 0; right < nums.size(); right++) {
    curr += nums[right];                 // expand
    while (curr > k) curr -= nums[left++]; // shrink
    ans = max(ans, right - left + 1);
}
// Longest substring with at most k distinct chars
unordered_map<char,int> freq;
int left = 0, ans = 0;
for (int right = 0; right < s.size(); right++) {
    freq[s[right]]++;
    while (freq.size() > k) {
        if (--freq[s[left]] == 0) freq.erase(s[left]);
        left++;
    }
    ans = max(ans, right - left + 1);
}
```
</div>
<h3 class="section-subheading">3.2 — Fixed-Size Window</h3>
<div class="ch-code-wrap">
```cpp
// Max sum subarray of size k — O(n)
int curr = 0;
for (int i = 0; i < k; i++) curr += nums[i]; // init window
int ans = curr;
for (int i = k; i < nums.size(); i++) {
    curr += nums[i] - nums[i-k];             // slide
    ans = max(ans, curr);
}
```
</div>
<div class="ch-cplx-row">
  <span class="ch-cplx"><span>Time</span>O(n) amortized</span>
  <span class="ch-cplx"><span>Space</span>O(1) or O(k)</span>
</div>
<div class="ch-ed-problems">
<table>
  <thead><tr><th>#</th><th>Problem</th><th>Type</th><th>Diff</th></tr></thead>
  <tbody>
    <tr><td>11</td><td><a href="https://leetcode.com/problems/maximum-average-subarray-i/" target="_blank">643. Maximum Average Subarray I</a></td><td>Fixed window</td><td class="diff-easy">Easy</td></tr>
    <tr><td>12</td><td><a href="https://leetcode.com/problems/max-consecutive-ones-iii/" target="_blank">1004. Max Consecutive Ones III</a></td><td>Variable window</td><td class="diff-medium">Medium</td></tr>
    <tr><td>13</td><td><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/" target="_blank">3. Longest Substring Without Repeating Characters</a></td><td>Variable + set</td><td class="diff-medium">Medium</td></tr>
    <tr><td>14</td><td><a href="https://leetcode.com/problems/subarray-product-less-than-k/" target="_blank">713. Subarray Product Less Than K</a></td><td>Variable (count valid)</td><td class="diff-medium">Medium</td></tr>
    <tr><td>15</td><td><a href="https://leetcode.com/problems/minimum-size-subarray-sum/" target="_blank">209. Minimum Size Subarray Sum</a></td><td>Variable (min length)</td><td class="diff-medium">Medium</td></tr>
    <tr><td>16</td><td><a href="https://leetcode.com/problems/fruit-into-baskets/" target="_blank">904. Fruit Into Baskets</a></td><td>Variable (≤2 distinct)</td><td class="diff-medium">Medium</td></tr>
    <tr><td>17</td><td><a href="https://leetcode.com/problems/sliding-window-maximum/" target="_blank">239. Sliding Window Maximum</a></td><td>Fixed + deque</td><td class="diff-hard">Hard</td></tr>
    <tr><td>18</td><td><a href="https://leetcode.com/problems/minimum-window-substring/" target="_blank">76. Minimum Window Substring</a></td><td>Variable + freq map</td><td class="diff-hard">Hard</td></tr>
  </tbody>
</table>
</div>
</div>
<div class="chapter-section">
<h2 class="section-heading">Section 4 — Pattern: Prefix Sum</h2>
<p>Prefix Sum pre-computes cumulative sums so that any range sum query [l,r] takes O(1) instead of O(n).</p>
<div class="insight-box">
  <span class="insight-label">Key Formula</span>
  <strong>prefix[i] = prefix[i-1] + nums[i-1]</strong><br>
  Range sum nums[l..r] = <strong>prefix[r+1] - prefix[l]</strong><br><br>
  <strong>Prefix + HashMap trick:</strong> Store how many times each prefix sum has appeared.
  For every curr, ans += freq[curr - target]. This counts subarrays summing to target in O(n).
</div>
<div class="ch-code-wrap">
```cpp
// Build 1D prefix sum — O(n)
vector<int> prefix(nums.size()+1, 0);
for (int i = 0; i < nums.size(); i++) prefix[i+1] = prefix[i] + nums[i];
// Query range sum [l,r] — O(1)
int rangeSum = prefix[r+1] - prefix[l];

// Count subarrays summing to k — O(n), O(n) space
unordered_map<int,int> freq; freq[0] = 1;
int curr = 0, ans = 0;
for (int x : nums) {
    curr += x;
    ans += freq[curr - k];
    freq[curr]++;
}
```
</div>
<div class="ch-cplx-row">
  <span class="ch-cplx"><span>Build</span>O(n)</span>
  <span class="ch-cplx"><span>Query</span>O(1)</span>
  <span class="ch-cplx"><span>Space</span>O(n)</span>
</div>
<div class="ch-ed-problems">
<table>
  <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr></thead>
  <tbody>
    <tr><td>19</td><td><a href="https://leetcode.com/problems/running-sum-of-1d-array/" target="_blank">1480. Running Sum of 1d Array</a></td><td>Build prefix sum</td><td class="diff-easy">Easy</td></tr>
    <tr><td>20</td><td><a href="https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/" target="_blank">1413. Minimum Value to Get Positive Step by Step Sum</a></td><td>Prefix + min</td><td class="diff-easy">Easy</td></tr>
    <tr><td>21</td><td><a href="https://leetcode.com/problems/k-radius-subarray-averages/" target="_blank">2090. K Radius Subarray Averages</a></td><td>Prefix + range query</td><td class="diff-medium">Medium</td></tr>
    <tr><td>22</td><td><a href="https://leetcode.com/problems/range-sum-query-immutable/" target="_blank">303. Range Sum Query - Immutable</a></td><td>Classic prefix query</td><td class="diff-easy">Easy</td></tr>
    <tr><td>23</td><td><a href="https://leetcode.com/problems/subarray-sum-equals-k/" target="_blank">560. Subarray Sum Equals K</a></td><td>Prefix + HashMap</td><td class="diff-medium">Medium</td></tr>
    <tr><td>24</td><td><a href="https://leetcode.com/problems/contiguous-array/" target="_blank">525. Contiguous Array</a></td><td>Transformed prefix + HashMap</td><td class="diff-medium">Medium</td></tr>
    <tr><td>25</td><td><a href="https://leetcode.com/problems/product-of-array-except-self/" target="_blank">238. Product of Array Except Self</a></td><td>Prefix/suffix product</td><td class="diff-medium">Medium</td></tr>
    <tr><td>26</td><td><a href="https://leetcode.com/problems/find-pivot-index/" target="_blank">724. Find Pivot Index</a></td><td>Prefix = suffix check</td><td class="diff-easy">Easy</td></tr>
  </tbody>
</table>
</div>
</div>
</div><!-- end .chapter-content -->
<div class="chapter-nav-footer">
  <a href="/learning/dsa/recursion/ch0-bigo-recursion/" class="ch-nav-footer-btn">← Ch0: Big O & Recursion</a>
  <a href="/learning/dsa/hashing/ch2-hashing/" class="ch-nav-footer-btn primary">Next: Ch2 — Hashing →</a>
</div>
