---
layout: default
title: DSA Mastery Roadmap
permalink: /learning/dsa/dsa-roadmap/
custom_css: dsa-roadmap
custom_js: dsa-roadmap
---

<div class="dsa-breadcrumb">
  <a href="{{ '/roadmap/' | relative_url }}">🗺️ All Roadmaps</a>
  <span>›</span>
  <span>DSA Mastery</span>
</div>

<div class="dsa-hero">
  <h1>🧠 DSA Mastery Roadmap</h1>
  <p>Data Structures & Algorithms for Coding Interviews — Complete C++ Reference with LeetCode Problems & Chapter Deep-Dives</p>
  <div class="dsa-hero-stats">
    <div><span class="dsa-stat-val">13</span><span class="dsa-stat-lbl">Chapters</span></div>
    <div><span class="dsa-stat-val">150+</span><span class="dsa-stat-lbl">Problems</span></div>
    <div><span class="dsa-stat-val">C++</span><span class="dsa-stat-lbl">Templates</span></div>
    <div><span class="dsa-stat-val">13</span><span class="dsa-stat-lbl">Patterns</span></div>
  </div>
</div>

<div class="dsa-overall-progress">
  <span class="dsa-op-label">📊 Your Progress</span>
  <div class="dsa-op-bar-wrap"><div class="dsa-op-bar"></div></div>
  <span class="dsa-op-pct">0%</span>
  <span class="dsa-op-count">Loading…</span>
</div>

<div class="dsa-filter-bar">
  <label>Filter:</label>
  <button class="diff-btn active" data-diff="all">All</button>
  <button class="diff-btn" data-diff="easy">Easy</button>
  <button class="diff-btn" data-diff="medium">Medium</button>
  <button class="diff-btn" data-diff="hard">Hard</button>
</div>

<nav class="dsa-chapter-nav" aria-label="Chapter navigation">
  <div class="dsa-chapter-pills">
    <a href="#ch0" class="ch-pill">Ch0 — Big O & Recursion<span class="pill-count">0/4</span></a>
    <a href="#ch1" class="ch-pill">Ch1 — Arrays & Strings<span class="pill-count">0/26</span></a>
    <a href="#ch2" class="ch-pill">Ch2 — Hashing<span class="pill-count">0/13</span></a>
    <a href="#ch3" class="ch-pill">Ch3 — Linked Lists<span class="pill-count">0/11</span></a>
    <a href="#ch4" class="ch-pill">Ch4 — Stacks & Queues<span class="pill-count">0/11</span></a>
    <a href="#ch5" class="ch-pill">Ch5 — Trees & Graphs<span class="pill-count">0/22</span></a>
    <a href="#ch6" class="ch-pill">Ch6 — Heaps<span class="pill-count">0/8</span></a>
    <a href="#ch7" class="ch-pill">Ch7 — Greedy<span class="pill-count">0/8</span></a>
    <a href="#ch8" class="ch-pill">Ch8 — Binary Search<span class="pill-count">0/9</span></a>
    <a href="#ch9" class="ch-pill">Ch9 — Backtracking<span class="pill-count">0/11</span></a>
    <a href="#ch10" class="ch-pill">Ch10 — Dynamic Programming<span class="pill-count">0/11</span></a>
    <a href="#ch11" class="ch-pill">Ch11 — Bonus Topics<span class="pill-count">0/6</span></a>
    <a href="#ch12" class="ch-pill">Ch12 — Study Plan<span class="pill-count"></span></a>
  </div>
</nav>

<div class="dsa-chapters">

<!-- ═══════════════════════════════════════════════
     Ch 0 — Big O & Recursion
═══════════════════════════════════════════════ -->
<div class="ch-card" id="ch0" data-ch="ch0" style="--ch-accent: linear-gradient(90deg,#00c9a7,#00b4d8);">
  <div class="ch-header">
    <div class="ch-num">Ch0</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Big O Notation & Recursion</div>
      <div class="ch-meta">
        <span class="ch-badge">Beginner</span>
        <span class="ch-badge">No Prerequisites</span>
        <a href="{{ '/learning/dsa/recursion/ch0-bigo-recursion/' | relative_url }}" class="ch-badge notes-live">📄 Chapter Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/4 solved</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Concepts</div>
    <div class="dsa-pattern-box">
      <ul>
        <li>Big O: drop constants (O(5n)=O(n)), drop lower-order terms (O(n²+n)=O(n²))</li>
        <li>Complexity Hierarchy: O(1) → O(log n) → O(n) → O(n log n) → O(n²) → O(2ⁿ) → O(n!)</li>
        <li>Recursion: every recursive function needs a <strong>base case</strong> + <strong>recursive case</strong></li>
        <li>Call stack space = O(depth) — watch for stack overflow on deep recursion</li>
        <li>Memoization = cache results to avoid recomputing subproblems</li>
      </ul>
    </div>
    <div class="ch-complexity">
      <span class="cplx-badge"><span class="cplx-label">Recursion space</span>O(depth)</span>
      <span class="cplx-badge"><span class="cplx-label">Memoized</span>O(n) states</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C++ Template</button>
    <div class="code-block-wrap">
{% highlight cpp %}
// Generic recursion template
ReturnType solve(params, state) {
    if (baseCondition) return baseValue;   // 1. Base case
    return solve(smallerParams, newState); // 2. Recursive case
}
// Top-down memoization
unordered_map<int, int> memo;
int dp(int n) {
    if (n <= 1) return n;
    if (memo.count(n)) return memo[n];
    return memo[n] = dp(n-1) + dp(n-2);
}
{% endhighlight %}
    </div>
    <div class="ch-section-label">Practice Problems</div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch0-p1" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td><a href="https://leetcode.com/problems/fibonacci-number/" target="_blank" class="problem-link">509. Fibonacci Number</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch0-p2" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td><a href="https://leetcode.com/problems/climbing-stairs/" target="_blank" class="problem-link">70. Climbing Stairs</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch0-p3" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td><a href="https://leetcode.com/problems/power-of-two/" target="_blank" class="problem-link">231. Power of Two</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch0-p4" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td><a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank" class="problem-link">206. Reverse Linked List</a></td><td class="diff-easy">Easy</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     Ch 1 — Arrays & Strings
═══════════════════════════════════════════════ -->
<div class="ch-card" id="ch1" data-ch="ch1" style="--ch-accent: linear-gradient(90deg,#06b6d4,#00c9a7);">
  <div class="ch-header">
    <div class="ch-num">Ch1</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Arrays & Strings</div>
      <div class="ch-meta">
        <span class="ch-badge">Intermediate</span>
        <span class="ch-badge">Prereq: Ch0</span>
        <a href="{{ '/learning/dsa/arrays/ch1-arrays-strings/' | relative_url }}" class="ch-badge notes-live">📄 Chapter Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/26 solved</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">1.1 Two Pointers</div>
    <div class="dsa-pattern-box">
      <ul>
        <li><strong>OPPOSITE ENDS:</strong> left=0, right=n-1, move inward — palindrome, two-sum on sorted</li>
        <li><strong>SAME DIRECTION:</strong> fast/slow pointers — remove duplicates, subsequence check</li>
        <li><strong>TWO ARRAYS:</strong> one pointer per array — merge sorted arrays, compare sequences</li>
      </ul>
    </div>
    <div class="ch-complexity">
      <span class="cplx-badge"><span class="cplx-label">Time</span>O(n)</span>
      <span class="cplx-badge"><span class="cplx-label">Space</span>O(1)</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C++ Templates</button>
    <div class="code-block-wrap">
{% highlight cpp %}
// Opposite ends
int left = 0, right = arr.size() - 1;
while (left < right) {
    if (condition) { left++; right--; }
    else if (tooSmall) left++;
    else right--;
}
// Fast/Slow (same direction)
int slow = 0;
for (int fast = 0; fast < arr.size(); fast++)
    if (condition(arr[fast])) arr[slow++] = arr[fast];
{% endhighlight %}
    </div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch1-p1" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td><a href="https://leetcode.com/problems/valid-palindrome/" target="_blank" class="problem-link">125. Valid Palindrome</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch1-p2" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td><a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/" target="_blank" class="problem-link">167. Two Sum II</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch1-p3" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td><a href="https://leetcode.com/problems/reverse-string/" target="_blank" class="problem-link">344. Reverse String</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch1-p4" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td><a href="https://leetcode.com/problems/squares-of-a-sorted-array/" target="_blank" class="problem-link">977. Squares of a Sorted Array</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch1-p5" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td><a href="https://leetcode.com/problems/move-zeroes/" target="_blank" class="problem-link">283. Move Zeroes</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch1-p6" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/" target="_blank" class="problem-link">26. Remove Duplicates from Sorted Array</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch1-p7" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td><a href="https://leetcode.com/problems/is-subsequence/" target="_blank" class="problem-link">392. Is Subsequence</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch1-p8" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td><a href="https://leetcode.com/problems/3sum/" target="_blank" class="problem-link">15. 3Sum</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch1-p9" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td><a href="https://leetcode.com/problems/container-with-most-water/" target="_blank" class="problem-link">11. Container With Most Water</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch1-p10" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>10</td><td><a href="https://leetcode.com/problems/trapping-rain-water/" target="_blank" class="problem-link">42. Trapping Rain Water</a></td><td class="diff-hard">Hard</td></tr>
      </tbody>
    </table>
    <div class="ch-section-label">1.2 Sliding Window</div>
    <div class="dsa-pattern-box">
      <ul>
        <li><strong>DYNAMIC WINDOW:</strong> expand right always, shrink left while constraint violated</li>
        <li><strong>FIXED WINDOW (size k):</strong> slide — add arr[right], remove arr[right-k]</li>
        <li>Count of valid subarrays ending at right = right - left + 1</li>
      </ul>
    </div>
    <div class="ch-complexity">
      <span class="cplx-badge"><span class="cplx-label">Time</span>O(n) amortized</span>
      <span class="cplx-badge"><span class="cplx-label">Space</span>O(1) or O(k)</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C++ Templates</button>
    <div class="code-block-wrap">
{% highlight cpp %}
// Dynamic window
int left = 0, curr = 0, ans = 0;
for (int right = 0; right < nums.size(); right++) {
    curr += nums[right];
    while (curr > k) curr -= nums[left++];
    ans = max(ans, right - left + 1);
}
// Fixed window (size k)
int curr = 0;
for (int i = 0; i < k; i++) curr += nums[i];
int ans = curr;
for (int i = k; i < nums.size(); i++) {
    curr += nums[i] - nums[i-k];
    ans = max(ans, curr);
}
{% endhighlight %}
    </div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch1-p11" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>11</td><td><a href="https://leetcode.com/problems/maximum-average-subarray-i/" target="_blank" class="problem-link">643. Maximum Average Subarray I</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch1-p12" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>12</td><td><a href="https://leetcode.com/problems/max-consecutive-ones-iii/" target="_blank" class="problem-link">1004. Max Consecutive Ones III</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch1-p13" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>13</td><td><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/" target="_blank" class="problem-link">3. Longest Substring Without Repeating Characters</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch1-p14" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>14</td><td><a href="https://leetcode.com/problems/subarray-product-less-than-k/" target="_blank" class="problem-link">713. Subarray Product Less Than K</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch1-p15" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>15</td><td><a href="https://leetcode.com/problems/minimum-size-subarray-sum/" target="_blank" class="problem-link">209. Minimum Size Subarray Sum</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch1-p16" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>16</td><td><a href="https://leetcode.com/problems/fruit-into-baskets/" target="_blank" class="problem-link">904. Fruit Into Baskets</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch1-p17" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>17</td><td><a href="https://leetcode.com/problems/sliding-window-maximum/" target="_blank" class="problem-link">239. Sliding Window Maximum</a></td><td class="diff-hard">Hard</td></tr>
        <tr data-key="ch1-p18" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>18</td><td><a href="https://leetcode.com/problems/minimum-window-substring/" target="_blank" class="problem-link">76. Minimum Window Substring</a></td><td class="diff-hard">Hard</td></tr>
      </tbody>
    </table>
    <div class="ch-section-label">1.3 Prefix Sum</div>
    <div class="dsa-pattern-box">
      <ul>
        <li>prefix[i] = prefix[i-1] + nums[i-1]. Range sum [l,r] = prefix[r+1] - prefix[l]</li>
        <li>Combine with hashmap: store prefix sum frequencies for subarray count problems</li>
        <li>2D prefix sums for matrix range queries</li>
      </ul>
    </div>
    <div class="ch-complexity">
      <span class="cplx-badge"><span class="cplx-label">Time</span>O(n) build, O(1) query</span>
      <span class="cplx-badge"><span class="cplx-label">Space</span>O(n)</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C++ Template</button>
    <div class="code-block-wrap">
{% highlight cpp %}
vector<int> prefix(nums.size() + 1, 0);
for (int i = 0; i < nums.size(); i++) prefix[i+1] = prefix[i] + nums[i];
// Sum nums[l..r] = prefix[r+1] - prefix[l]

// Subarray sum equals k — O(n)
unordered_map<int,int> freq; freq[0] = 1; // init: prefix sum 0 seen once
int curr = 0, ans = 0;
for (int x : nums) { curr += x; ans += freq[curr - k]; freq[curr]++; }
{% endhighlight %}
    </div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch1-p19" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>19</td><td><a href="https://leetcode.com/problems/running-sum-of-1d-array/" target="_blank" class="problem-link">1480. Running Sum of 1d Array</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch1-p20" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>20</td><td><a href="https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/" target="_blank" class="problem-link">1413. Minimum Value to Get Positive Step by Step Sum</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch1-p21" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>21</td><td><a href="https://leetcode.com/problems/k-radius-subarray-averages/" target="_blank" class="problem-link">2090. K Radius Subarray Averages</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch1-p22" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>22</td><td><a href="https://leetcode.com/problems/range-sum-query-immutable/" target="_blank" class="problem-link">303. Range Sum Query - Immutable</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch1-p23" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>23</td><td><a href="https://leetcode.com/problems/subarray-sum-equals-k/" target="_blank" class="problem-link">560. Subarray Sum Equals K</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch1-p24" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>24</td><td><a href="https://leetcode.com/problems/contiguous-array/" target="_blank" class="problem-link">525. Contiguous Array</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch1-p25" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>25</td><td><a href="https://leetcode.com/problems/product-of-array-except-self/" target="_blank" class="problem-link">238. Product of Array Except Self</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch1-p26" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>26</td><td><a href="https://leetcode.com/problems/find-pivot-index/" target="_blank" class="problem-link">724. Find Pivot Index</a></td><td class="diff-easy">Easy</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     Ch 2 — Hashing
═══════════════════════════════════════════════ -->
<div class="ch-card" id="ch2" data-ch="ch2" style="--ch-accent: linear-gradient(90deg,#00b4d8,#0077b6);">
  <div class="ch-header">
    <div class="ch-num">Ch2</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Hashing — HashMaps & Sets</div>
      <div class="ch-meta">
        <span class="ch-badge">Intermediate</span>
        <span class="ch-badge">Prereq: Ch1</span>
        <a href="{{ '/learning/dsa/hashing/ch2-hashing/' | relative_url }}" class="ch-badge notes-live">📄 Chapter Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/13 solved</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Patterns</div>
    <div class="dsa-pattern-box">
      <ul>
        <li><strong>EXISTENCE CHECK:</strong> Use unordered_set for O(1) lookup (duplicates, anagram, pangram)</li>
        <li><strong>FREQUENCY COUNT:</strong> Use unordered_map&lt;T,int&gt; (count chars, elements, words)</li>
        <li><strong>TWO-SUM PATTERN:</strong> Store seen values; for each x, check if (target-x) exists</li>
        <li><strong>GROUPING:</strong> Map key → list of values (group anagrams by sorted string)</li>
        <li><strong>SLIDING WINDOW + HASHMAP:</strong> Track character frequencies in a window</li>
        <li><strong>PREFIX SUM + HASHMAP:</strong> Count subarrays with target sum/property</li>
      </ul>
    </div>
    <div class="ch-complexity">
      <span class="cplx-badge"><span class="cplx-label">Time</span>O(n) average</span>
      <span class="cplx-badge"><span class="cplx-label">Space</span>O(n)</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C++ Templates</button>
    <div class="code-block-wrap">
{% highlight cpp %}
// Frequency count
unordered_map<int,int> freq;
for (int x : arr) freq[x]++;
// Two-sum lookup
unordered_map<int,int> seen;
for (int i = 0; i < nums.size(); i++) {
    if (seen.count(target - nums[i])) return {seen[target-nums[i]], i};
    seen[nums[i]] = i;
}
// Group anagrams
unordered_map<string, vector<string>> groups;
for (string& s : strs) {
    string key = s; sort(key.begin(), key.end());
    groups[key].push_back(s);
}
{% endhighlight %}
    </div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch2-p1" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td><a href="https://leetcode.com/problems/check-if-the-sentence-is-pangram/" target="_blank" class="problem-link">1832. Check if the Sentence Is Pangram</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch2-p2" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td><a href="https://leetcode.com/problems/missing-number/" target="_blank" class="problem-link">268. Missing Number</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch2-p3" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td><a href="https://leetcode.com/problems/counting-elements/" target="_blank" class="problem-link">1426. Counting Elements</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch2-p4" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td><a href="https://leetcode.com/problems/two-sum/" target="_blank" class="problem-link">1. Two Sum</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch2-p5" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td><a href="https://leetcode.com/problems/ransom-note/" target="_blank" class="problem-link">383. Ransom Note</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch2-p6" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td><a href="https://leetcode.com/problems/jewels-and-stones/" target="_blank" class="problem-link">771. Jewels and Stones</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch2-p7" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td><a href="https://leetcode.com/problems/find-players-with-zero-or-one-losses/" target="_blank" class="problem-link">2225. Find Players With Zero or One Losses</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch2-p8" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td><a href="https://leetcode.com/problems/largest-unique-number/" target="_blank" class="problem-link">1133. Largest Unique Number</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch2-p9" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td><a href="https://leetcode.com/problems/maximum-number-of-balloons/" target="_blank" class="problem-link">1189. Maximum Number of Balloons</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch2-p10" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>10</td><td><a href="https://leetcode.com/problems/group-anagrams/" target="_blank" class="problem-link">49. Group Anagrams</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch2-p11" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>11</td><td><a href="https://leetcode.com/problems/top-k-frequent-elements/" target="_blank" class="problem-link">347. Top K Frequent Elements</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch2-p12" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>12</td><td><a href="https://leetcode.com/problems/subarray-sum-equals-k/" target="_blank" class="problem-link">560. Subarray Sum Equals K</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch2-p13" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>13</td><td><a href="https://leetcode.com/problems/lru-cache/" target="_blank" class="problem-link">146. LRU Cache</a></td><td class="diff-medium">Medium</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     Ch 3 — Linked Lists
═══════════════════════════════════════════════ -->
<div class="ch-card" id="ch3" data-ch="ch3" style="--ch-accent: linear-gradient(90deg,#0077b6,#023e8a);">
  <div class="ch-header">
    <div class="ch-num">Ch3</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Linked Lists</div>
      <div class="ch-meta">
        <span class="ch-badge">Intermediate</span>
        <span class="ch-badge">Prereq: Ch2</span>
        <a href="{{ '/learning/dsa/linked-list/ch3-linked-lists/' | relative_url }}" class="ch-badge notes-live">📄 Chapter Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/11 solved</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Patterns</div>
    <div class="dsa-pattern-box">
      <ul>
        <li><strong>FAST/SLOW POINTERS (Floyd's):</strong> fast moves 2x, slow 1x — middle, cycle, kth from end</li>
        <li><strong>REVERSAL:</strong> Iterative with prev/curr/next. O(n) time, O(1) space</li>
        <li><strong>DUMMY NODE:</strong> Add dummy head to simplify edge cases (empty list, removing head)</li>
        <li><strong>TWO-POINTER MERGE:</strong> Merge two sorted lists by comparing heads</li>
      </ul>
    </div>
    <div class="ch-complexity">
      <span class="cplx-badge"><span class="cplx-label">Time</span>O(n) traversal</span>
      <span class="cplx-badge"><span class="cplx-label">Space</span>O(1) most patterns</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C++ Templates</button>
    <div class="code-block-wrap">
{% highlight cpp %}
// Fast/slow — find middle
ListNode *slow = head, *fast = head;
while (fast && fast->next) { slow = slow->next; fast = fast->next->next; }
// slow = middle

// Reverse iteratively
ListNode *prev = nullptr, *curr = head;
while (curr) { ListNode* nxt = curr->next; curr->next = prev; prev = curr; curr = nxt; }
// prev = new head

// Merge sorted (dummy head)
ListNode dummy(0); ListNode* tail = &dummy;
while (l1 && l2) {
    if (l1->val <= l2->val) { tail->next = l1; l1 = l1->next; }
    else { tail->next = l2; l2 = l2->next; }
    tail = tail->next;
}
tail->next = l1 ? l1 : l2;
{% endhighlight %}
    </div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch3-p1" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td><a href="https://leetcode.com/problems/middle-of-the-linked-list/" target="_blank" class="problem-link">876. Middle of the Linked List</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch3-p2" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-list/" target="_blank" class="problem-link">83. Remove Duplicates from Sorted List</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch3-p3" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td><a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank" class="problem-link">206. Reverse Linked List</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch3-p4" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td><a href="https://leetcode.com/problems/reverse-linked-list-ii/" target="_blank" class="problem-link">92. Reverse Linked List II</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch3-p5" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td><a href="https://leetcode.com/problems/linked-list-cycle/" target="_blank" class="problem-link">141. Linked List Cycle</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch3-p6" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td><a href="https://leetcode.com/problems/merge-two-sorted-lists/" target="_blank" class="problem-link">21. Merge Two Sorted Lists</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch3-p7" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td><a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/" target="_blank" class="problem-link">19. Remove Nth Node From End of List</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch3-p8" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td><a href="https://leetcode.com/problems/add-two-numbers/" target="_blank" class="problem-link">2. Add Two Numbers</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch3-p9" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td><a href="https://leetcode.com/problems/reorder-list/" target="_blank" class="problem-link">143. Reorder List</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch3-p10" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>10</td><td><a href="https://leetcode.com/problems/lru-cache/" target="_blank" class="problem-link">146. LRU Cache</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch3-p11" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>11</td><td><a href="https://leetcode.com/problems/merge-k-sorted-lists/" target="_blank" class="problem-link">23. Merge K Sorted Lists</a></td><td class="diff-hard">Hard</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     Ch 4 — Stacks & Queues
═══════════════════════════════════════════════ -->
<div class="ch-card" id="ch4" data-ch="ch4" style="--ch-accent: linear-gradient(90deg,#06d6a0,#1b9aaa);">
  <div class="ch-header">
    <div class="ch-num">Ch4</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Stacks & Queues</div>
      <div class="ch-meta">
        <span class="ch-badge">Intermediate</span>
        <span class="ch-badge">Prereq: Ch3</span>
        <a href="{{ '/learning/dsa/stacks/ch4-stacks-queues/' | relative_url }}" class="ch-badge notes-live">📄 Chapter Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/11 solved</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">4.1 Stacks — Key Patterns</div>
    <div class="dsa-pattern-box">
      <ul>
        <li><strong>MATCHING/VALIDATION:</strong> Push open brackets, pop on close, check match</li>
        <li><strong>MONOTONIC STACK (increasing):</strong> pop smaller than current → next greater element</li>
        <li><strong>MONOTONIC STACK (decreasing):</strong> pop greater than current → next smaller element</li>
        <li><strong>STRING SIMULATION:</strong> Build result char-by-char on a stack</li>
      </ul>
    </div>
    <div class="ch-complexity">
      <span class="cplx-badge"><span class="cplx-label">Time</span>O(n)</span>
      <span class="cplx-badge"><span class="cplx-label">Space</span>O(n)</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C++ Templates</button>
    <div class="code-block-wrap">
{% highlight cpp %}
// Monotonic stack — Next Greater Element
vector<int> ans(nums.size(), -1);
stack<int> stk;
for (int i = 0; i < nums.size(); i++) {
    while (!stk.empty() && nums[i] > nums[stk.top()])
        { ans[stk.top()] = nums[i]; stk.pop(); }
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
// Deque — sliding window max
deque<int> dq;
for (int i = 0; i < nums.size(); i++) {
    while (!dq.empty() && dq.front() < i-k+1) dq.pop_front();
    while (!dq.empty() && nums[dq.back()] < nums[i]) dq.pop_back();
    dq.push_back(i);
    if (i >= k-1) ans.push_back(nums[dq.front()]);
}
{% endhighlight %}
    </div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch4-p1" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td><a href="https://leetcode.com/problems/valid-parentheses/" target="_blank" class="problem-link">20. Valid Parentheses</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch4-p2" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td><a href="https://leetcode.com/problems/simplify-path/" target="_blank" class="problem-link">71. Simplify Path</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch4-p3" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td><a href="https://leetcode.com/problems/make-the-string-great/" target="_blank" class="problem-link">1544. Make The String Great</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch4-p4" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td><a href="https://leetcode.com/problems/next-greater-element-i/" target="_blank" class="problem-link">496. Next Greater Element I</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch4-p5" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td><a href="https://leetcode.com/problems/online-stock-span/" target="_blank" class="problem-link">901. Online Stock Span</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch4-p6" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td><a href="https://leetcode.com/problems/daily-temperatures/" target="_blank" class="problem-link">739. Daily Temperatures</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch4-p7" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td><a href="https://leetcode.com/problems/asteroid-collision/" target="_blank" class="problem-link">735. Asteroid Collision</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch4-p8" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td><a href="https://leetcode.com/problems/largest-rectangle-in-histogram/" target="_blank" class="problem-link">84. Largest Rectangle in Histogram</a></td><td class="diff-hard">Hard</td></tr>
        <tr data-key="ch4-p9" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td><a href="https://leetcode.com/problems/moving-average-from-data-stream/" target="_blank" class="problem-link">346. Moving Average from Data Stream</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch4-p10" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>10</td><td><a href="https://leetcode.com/problems/sliding-window-maximum/" target="_blank" class="problem-link">239. Sliding Window Maximum</a></td><td class="diff-hard">Hard</td></tr>
        <tr data-key="ch4-p11" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>11</td><td><a href="https://leetcode.com/problems/design-circular-queue/" target="_blank" class="problem-link">622. Design Circular Queue</a></td><td class="diff-medium">Medium</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     Ch 5 — Trees & Graphs
═══════════════════════════════════════════════ -->
<div class="ch-card" id="ch5" data-ch="ch5" style="--ch-accent: linear-gradient(90deg,#2dc653,#00b4d8);">
  <div class="ch-header">
    <div class="ch-num">Ch5</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Trees & Graphs</div>
      <div class="ch-meta">
        <span class="ch-badge">Advanced</span>
        <span class="ch-badge">Prereq: Ch4</span>
        <a href="{{ '/learning/dsa/tree/ch5-trees-graphs/' | relative_url }}" class="ch-badge notes-live">📄 Chapter Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/22 solved</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">5.1 Binary Tree — DFS</div>
    <div class="dsa-pattern-box">
      <ul>
        <li><strong>PREORDER</strong> (root→left→right): copying, serializing trees</li>
        <li><strong>INORDER</strong> (left→root→right): sorted order for BST</li>
        <li><strong>POSTORDER</strong> (left→right→root): deletion, computing subtree properties</li>
        <li><strong>GLOBAL vs LOCAL:</strong> use a global variable for answers spanning multiple nodes</li>
      </ul>
    </div>
    <div class="ch-complexity">
      <span class="cplx-badge"><span class="cplx-label">Time</span>O(n)</span>
      <span class="cplx-badge"><span class="cplx-label">Space</span>O(h) stack</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C++ Templates</button>
    <div class="code-block-wrap">
{% highlight cpp %}
// Recursive DFS
int dfs(TreeNode* node) {
    if (!node) return 0;
    int left = dfs(node->left), right = dfs(node->right);
    return 1 + max(left, right); // example: height
}
// BFS level-order
queue<TreeNode*> q; q.push(root);
while (!q.empty()) {
    int sz = q.size();
    for (int i = 0; i < sz; i++) {
        TreeNode* node = q.front(); q.pop();
        if (node->left)  q.push(node->left);
        if (node->right) q.push(node->right);
    }
}
// Graph BFS — shortest path
vector<int> dist(n, -1);
queue<int> q; q.push(start); dist[start] = 0;
while (!q.empty()) {
    int node = q.front(); q.pop();
    for (int nei : adj[node])
        if (dist[nei]==-1) { dist[nei]=dist[node]+1; q.push(nei); }
}
{% endhighlight %}
    </div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch5-p1" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td><a href="https://leetcode.com/problems/minimum-depth-of-binary-tree/" target="_blank" class="problem-link">111. Minimum Depth of Binary Tree</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch5-p2" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td><a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/" target="_blank" class="problem-link">104. Maximum Depth of Binary Tree</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch5-p3" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td><a href="https://leetcode.com/problems/diameter-of-binary-tree/" target="_blank" class="problem-link">543. Diameter of Binary Tree</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch5-p4" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td><a href="https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/" target="_blank" class="problem-link">1026. Maximum Difference Between Node and Ancestor</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p5" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td><a href="https://leetcode.com/problems/path-sum-ii/" target="_blank" class="problem-link">113. Path Sum II</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p6" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/" target="_blank" class="problem-link">236. Lowest Common Ancestor of a Binary Tree</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p7" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td><a href="https://leetcode.com/problems/binary-tree-maximum-path-sum/" target="_blank" class="problem-link">124. Binary Tree Maximum Path Sum</a></td><td class="diff-hard">Hard</td></tr>
        <tr data-key="ch5-p8" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td><a href="https://leetcode.com/problems/binary-tree-level-order-traversal/" target="_blank" class="problem-link">102. Binary Tree Level Order Traversal</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p9" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td><a href="https://leetcode.com/problems/deepest-leaves-sum/" target="_blank" class="problem-link">1302. Deepest Leaves Sum</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p10" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>10</td><td><a href="https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/" target="_blank" class="problem-link">103. Binary Tree Zigzag Level Order Traversal</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p11" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>11</td><td><a href="https://leetcode.com/problems/average-of-levels-in-binary-tree/" target="_blank" class="problem-link">637. Average of Levels in Binary Tree</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch5-p12" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>12</td><td><a href="https://leetcode.com/problems/insert-into-a-binary-search-tree/" target="_blank" class="problem-link">701. Insert into a Binary Search Tree</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p13" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>13</td><td><a href="https://leetcode.com/problems/closest-binary-search-tree-value/" target="_blank" class="problem-link">270. Closest Binary Search Tree Value</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch5-p14" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>14</td><td><a href="https://leetcode.com/problems/validate-binary-search-tree/" target="_blank" class="problem-link">98. Validate Binary Search Tree</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p15" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>15</td><td><a href="https://leetcode.com/problems/kth-smallest-element-in-a-bst/" target="_blank" class="problem-link">230. Kth Smallest Element in a BST</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p16" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>16</td><td><a href="https://leetcode.com/problems/find-if-path-exists-in-graph/" target="_blank" class="problem-link">1971. Find if Path Exists in Graph</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch5-p17" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>17</td><td><a href="https://leetcode.com/problems/max-area-of-island/" target="_blank" class="problem-link">695. Max Area of Island</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p18" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>18</td><td><a href="https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/" target="_blank" class="problem-link">1926. Nearest Exit from Entrance in Maze</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p19" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>19</td><td><a href="https://leetcode.com/problems/number-of-islands/" target="_blank" class="problem-link">200. Number of Islands</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p20" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>20</td><td><a href="https://leetcode.com/problems/course-schedule/" target="_blank" class="problem-link">207. Course Schedule</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p21" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>21</td><td><a href="https://leetcode.com/problems/clone-graph/" target="_blank" class="problem-link">133. Clone Graph</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch5-p22" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>22</td><td><a href="https://leetcode.com/problems/word-ladder/" target="_blank" class="problem-link">127. Word Ladder</a></td><td class="diff-hard">Hard</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     Ch 6 — Heaps
═══════════════════════════════════════════════ -->
<div class="ch-card" id="ch6" data-ch="ch6" style="--ch-accent: linear-gradient(90deg,#f77f00,#d62828);">
  <div class="ch-header">
    <div class="ch-num">Ch6</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Heaps & Priority Queues</div>
      <div class="ch-meta">
        <span class="ch-badge">Intermediate</span>
        <span class="ch-badge">Prereq: Ch5</span>
        <a href="{{ '/learning/dsa/heaps/ch6-heaps/' | relative_url }}" class="ch-badge notes-live">📄 Chapter Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/8 solved</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Patterns</div>
    <div class="dsa-pattern-box">
      <ul>
        <li><strong>TOP K:</strong> Min-heap of size k — push each element; if size > k, pop. Heap = top k largest</li>
        <li><strong>K-WAY MERGE:</strong> Push (value, listIndex, elemIndex) into heap; always pop smallest</li>
        <li><strong>RUNNING MEDIAN:</strong> Max-heap for lower half + min-heap for upper half</li>
        <li>Trigger: 'Smallest/Largest K elements' → heap. C++ default is max-heap; use greater&lt;int&gt; for min</li>
      </ul>
    </div>
    <div class="ch-complexity">
      <span class="cplx-badge"><span class="cplx-label">Push/Pop</span>O(log n)</span>
      <span class="cplx-badge"><span class="cplx-label">Peek</span>O(1)</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C++ Template</button>
    <div class="code-block-wrap">
{% highlight cpp %}
// Min-heap
priority_queue<int, vector<int>, greater<int>> minH;
// Top-K largest using min-heap of size K
priority_queue<int, vector<int>, greater<int>> pq;
for (int x : nums) { pq.push(x); if (pq.size() > k) pq.pop(); }
// pq.top() = kth largest
// Custom comparator
auto cmp = [](pair<int,int>& a, pair<int,int>& b){ return a.first > b.first; };
priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(cmp)> pq(cmp);
{% endhighlight %}
    </div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch6-p1" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td><a href="https://leetcode.com/problems/remove-stones-to-minimize-the-total/" target="_blank" class="problem-link">1962. Remove Stones to Minimize the Total</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch6-p2" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td><a href="https://leetcode.com/problems/minimum-cost-to-connect-sticks/" target="_blank" class="problem-link">1167. Minimum Cost to Connect Sticks</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch6-p3" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td><a href="https://leetcode.com/problems/kth-largest-element-in-an-array/" target="_blank" class="problem-link">215. Kth Largest Element in an Array</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch6-p4" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td><a href="https://leetcode.com/problems/k-closest-points-to-origin/" target="_blank" class="problem-link">973. K Closest Points to Origin</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch6-p5" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td><a href="https://leetcode.com/problems/kth-largest-element-in-a-stream/" target="_blank" class="problem-link">703. Kth Largest Element in a Stream</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch6-p6" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td><a href="https://leetcode.com/problems/find-median-from-data-stream/" target="_blank" class="problem-link">295. Find Median from Data Stream</a></td><td class="diff-hard">Hard</td></tr>
        <tr data-key="ch6-p7" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td><a href="https://leetcode.com/problems/task-scheduler/" target="_blank" class="problem-link">621. Task Scheduler</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch6-p8" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td><a href="https://leetcode.com/problems/merge-k-sorted-lists/" target="_blank" class="problem-link">23. Merge K Sorted Lists</a></td><td class="diff-hard">Hard</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     Ch 7 — Greedy
═══════════════════════════════════════════════ -->
<div class="ch-card" id="ch7" data-ch="ch7" style="--ch-accent: linear-gradient(90deg,#e63946,#f77f00);">
  <div class="ch-header">
    <div class="ch-num">Ch7</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Greedy Algorithms</div>
      <div class="ch-meta">
        <span class="ch-badge">Intermediate</span>
        <span class="ch-badge">Prereq: Ch3</span>
        <a href="{{ '/learning/dsa/greedy/ch7-greedy/' | relative_url }}" class="ch-badge notes-live">📄 Chapter Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/8 solved</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Patterns</div>
    <div class="dsa-pattern-box">
      <ul>
        <li><strong>SORT FIRST:</strong> Most greedy problems require sorting by some key (weight, ratio, end time)</li>
        <li><strong>INTERVAL SCHEDULING:</strong> Sort by end time — greedily take non-overlapping intervals</li>
        <li><strong>EXCHANGE ARGUMENT:</strong> Prove swapping adjacent elements doesn't improve solution</li>
        <li>Ask: 'Does taking the best local choice block a better global solution?' If no → greedy works</li>
      </ul>
    </div>
    <div class="ch-complexity">
      <span class="cplx-badge"><span class="cplx-label">Time</span>O(n log n) with sort</span>
      <span class="cplx-badge"><span class="cplx-label">Space</span>O(1)</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C++ Template</button>
    <div class="code-block-wrap">
{% highlight cpp %}
// Interval scheduling — max non-overlapping intervals
sort(intervals.begin(), intervals.end(),
    [](auto& a, auto& b){ return a[1] < b[1]; }); // sort by end
int count = 0, prevEnd = INT_MIN;
for (auto& iv : intervals)
    if (iv[0] >= prevEnd) { count++; prevEnd = iv[1]; }
{% endhighlight %}
    </div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch7-p1" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td><a href="https://leetcode.com/problems/maximum-69-number/" target="_blank" class="problem-link">1323. Maximum 69 Number</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch7-p2" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td><a href="https://leetcode.com/problems/maximum-units-on-a-truck/" target="_blank" class="problem-link">1710. Maximum Units on a Truck</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch7-p3" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td><a href="https://leetcode.com/problems/reduce-array-size-to-the-half/" target="_blank" class="problem-link">1338. Reduce Array Size to The Half</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch7-p4" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td><a href="https://leetcode.com/problems/non-overlapping-intervals/" target="_blank" class="problem-link">435. Non-overlapping Intervals</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch7-p5" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td><a href="https://leetcode.com/problems/jump-game/" target="_blank" class="problem-link">55. Jump Game</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch7-p6" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td><a href="https://leetcode.com/problems/jump-game-ii/" target="_blank" class="problem-link">45. Jump Game II</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch7-p7" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td><a href="https://leetcode.com/problems/gas-station/" target="_blank" class="problem-link">134. Gas Station</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch7-p8" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td><a href="https://leetcode.com/problems/candy/" target="_blank" class="problem-link">135. Candy</a></td><td class="diff-hard">Hard</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     Ch 8 — Binary Search
═══════════════════════════════════════════════ -->
<div class="ch-card" id="ch8" data-ch="ch8" style="--ch-accent: linear-gradient(90deg,#7209b7,#560bad);">
  <div class="ch-header">
    <div class="ch-num">Ch8</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Binary Search</div>
      <div class="ch-meta">
        <span class="ch-badge">Intermediate</span>
        <span class="ch-badge">Prereq: Ch1</span>
        <a href="{{ '/learning/dsa/binary-search/ch8-binary-search/' | relative_url }}" class="ch-badge notes-live">📄 Chapter Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/9 solved</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Patterns</div>
    <div class="dsa-pattern-box">
      <ul>
        <li><strong>ON SORTED ARRAY:</strong> Classic search / find leftmost or rightmost position</li>
        <li><strong>ON ANSWER SPACE:</strong> Binary search on the answer when feasibility is monotonic</li>
        <li><strong>FIND LEFTMOST:</strong> Use 'left = mid + 1' when condition met — pushes left boundary right</li>
        <li>Trigger: <em>'minimize the maximum'</em> or <em>'maximize the minimum'</em> → binary search on answer</li>
      </ul>
    </div>
    <div class="ch-complexity">
      <span class="cplx-badge"><span class="cplx-label">Time</span>O(log n)</span>
      <span class="cplx-badge"><span class="cplx-label">Space</span>O(1)</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C++ Templates</button>
    <div class="code-block-wrap">
{% highlight cpp %}
// Standard binary search
int lo = 0, hi = nums.size()-1;
while (lo <= hi) {
    int mid = lo + (hi-lo)/2;  // avoid overflow
    if (nums[mid] == target) return mid;
    else if (nums[mid] < target) lo = mid+1;
    else hi = mid-1;
}
// Binary search on answer (minimise)
int lo = minVal, hi = maxVal, ans = hi;
while (lo <= hi) {
    int mid = lo + (hi-lo)/2;
    if (feasible(mid)) { ans = mid; hi = mid-1; }
    else lo = mid+1;
}
{% endhighlight %}
    </div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch8-p1" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td><a href="https://leetcode.com/problems/binary-search/" target="_blank" class="problem-link">704. Binary Search</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch8-p2" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td><a href="https://leetcode.com/problems/search-insert-position/" target="_blank" class="problem-link">35. Search Insert Position</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch8-p3" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td><a href="https://leetcode.com/problems/longest-subsequence-with-limited-sum/" target="_blank" class="problem-link">2389. Longest Subsequence With Limited Sum</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch8-p4" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td><a href="https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/" target="_blank" class="problem-link">1283. Find the Smallest Divisor Given a Threshold</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch8-p5" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td><a href="https://leetcode.com/problems/split-array-largest-sum/" target="_blank" class="problem-link">410. Split Array Largest Sum</a></td><td class="diff-hard">Hard</td></tr>
        <tr data-key="ch8-p6" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td><a href="https://leetcode.com/problems/koko-eating-bananas/" target="_blank" class="problem-link">875. Koko Eating Bananas</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch8-p7" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td><a href="https://leetcode.com/problems/find-peak-element/" target="_blank" class="problem-link">162. Find Peak Element</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch8-p8" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td><a href="https://leetcode.com/problems/search-in-rotated-sorted-array/" target="_blank" class="problem-link">33. Search in Rotated Sorted Array</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch8-p9" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td><a href="https://leetcode.com/problems/median-of-two-sorted-arrays/" target="_blank" class="problem-link">4. Median of Two Sorted Arrays</a></td><td class="diff-hard">Hard</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     Ch 9 — Backtracking
═══════════════════════════════════════════════ -->
<div class="ch-card" id="ch9" data-ch="ch9" style="--ch-accent: linear-gradient(90deg,#f72585,#7209b7);">
  <div class="ch-header">
    <div class="ch-num">Ch9</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Backtracking</div>
      <div class="ch-meta">
        <span class="ch-badge">Advanced</span>
        <span class="ch-badge">Prereq: Ch0 Recursion</span>
        <a href="{{ '/learning/dsa/backtracking/ch9-backtracking/' | relative_url }}" class="ch-badge notes-live">📄 Chapter Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/11 solved</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Patterns</div>
    <div class="dsa-pattern-box">
      <ul>
        <li><strong>GENERATION:</strong> Build all permutations/subsets/combinations — just enumerate</li>
        <li><strong>CONSTRAINED:</strong> Prune early when constraint violated (sum exceeds target)</li>
        <li>Template: <strong>choose → recurse → unchoose</strong> (restore state)</li>
        <li>Use 'start' index to avoid re-using earlier elements in combination problems</li>
        <li>Use 'used[]' boolean array for permutations to avoid duplicate positions</li>
        <li>Time: O(n! × n) permutations, O(2ⁿ × n) subsets — always exponential</li>
      </ul>
    </div>
    <div class="ch-complexity">
      <span class="cplx-badge"><span class="cplx-label">Subsets</span>O(2ⁿ × n)</span>
      <span class="cplx-badge"><span class="cplx-label">Perms</span>O(n! × n)</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C++ Template</button>
    <div class="code-block-wrap">
{% highlight cpp %}
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
{% endhighlight %}
    </div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch9-p1" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td><a href="https://leetcode.com/problems/all-paths-from-source-to-target/" target="_blank" class="problem-link">797. All Paths From Source to Target</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch9-p2" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td><a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/" target="_blank" class="problem-link">17. Letter Combinations of a Phone Number</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch9-p3" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td><a href="https://leetcode.com/problems/generate-parentheses/" target="_blank" class="problem-link">22. Generate Parentheses</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch9-p4" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td><a href="https://leetcode.com/problems/numbers-with-same-consecutive-differences/" target="_blank" class="problem-link">967. Numbers With Same Consecutive Differences</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch9-p5" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td><a href="https://leetcode.com/problems/combination-sum-iii/" target="_blank" class="problem-link">216. Combination Sum III</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch9-p6" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td><a href="https://leetcode.com/problems/subsets/" target="_blank" class="problem-link">78. Subsets</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch9-p7" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td><a href="https://leetcode.com/problems/permutations/" target="_blank" class="problem-link">46. Permutations</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch9-p8" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td><a href="https://leetcode.com/problems/combination-sum/" target="_blank" class="problem-link">39. Combination Sum</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch9-p9" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td><a href="https://leetcode.com/problems/word-search/" target="_blank" class="problem-link">79. Word Search</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch9-p10" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>10</td><td><a href="https://leetcode.com/problems/n-queens/" target="_blank" class="problem-link">51. N-Queens</a></td><td class="diff-hard">Hard</td></tr>
        <tr data-key="ch9-p11" data-diff="hard"><td class="solved-cell"><div class="solved-check"></div></td><td>11</td><td><a href="https://leetcode.com/problems/sudoku-solver/" target="_blank" class="problem-link">37. Sudoku Solver</a></td><td class="diff-hard">Hard</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     Ch 10 — Dynamic Programming
═══════════════════════════════════════════════ -->
<div class="ch-card" id="ch10" data-ch="ch10" style="--ch-accent: linear-gradient(90deg,#4361ee,#7209b7);">
  <div class="ch-header">
    <div class="ch-num">Ch10</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Dynamic Programming</div>
      <div class="ch-meta">
        <span class="ch-badge">Advanced</span>
        <span class="ch-badge">Prereq: Ch0, Ch9</span>
        <a href="{{ '/learning/dsa/dynamic-programming/ch10-dynamic-programming/' | relative_url }}" class="ch-badge notes-live">📄 Chapter Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/11 solved</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Patterns</div>
    <div class="dsa-pattern-box">
      <ul>
        <li><strong>Step 1:</strong> Define what dp[i] (or dp[i][j]) represents</li>
        <li><strong>Step 2:</strong> Find the recurrence relation (transition)</li>
        <li><strong>Step 3:</strong> Identify base cases</li>
        <li><strong>Step 4:</strong> Determine iteration order (ensure subproblems solved before needed)</li>
        <li>DP vs Greedy: DP explores all choices; Greedy makes one. Use DP when Greedy fails</li>
      </ul>
    </div>
    <div class="ch-complexity">
      <span class="cplx-badge"><span class="cplx-label">1D DP</span>O(n)</span>
      <span class="cplx-badge"><span class="cplx-label">2D DP</span>O(m×n)</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C++ Templates</button>
    <div class="code-block-wrap">
{% highlight cpp %}
// 1D DP — Climbing Stairs
vector<int> dp(n+1, 0); dp[0]=1; dp[1]=1;
for (int i = 2; i <= n; i++) dp[i] = dp[i-1] + dp[i-2];
// Coin Change (unbounded knapsack)
vector<int> dp(amount+1, INT_MAX); dp[0]=0;
for (int i = 1; i <= amount; i++)
    for (int coin : coins)
        if (coin<=i && dp[i-coin]!=INT_MAX) dp[i]=min(dp[i],dp[i-coin]+1);
// State machine DP (Stock with cooldown)
int hold = -prices[0], sold = 0, rest = 0;
for (int i = 1; i < prices.size(); i++) {
    int ph=hold,ps=sold,pr=rest;
    hold=max(ph,pr-prices[i]); sold=ph+prices[i]; rest=max(pr,ps);
}
{% endhighlight %}
    </div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch10-p1" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td><a href="https://leetcode.com/problems/climbing-stairs/" target="_blank" class="problem-link">70. Climbing Stairs</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch10-p2" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td><a href="https://leetcode.com/problems/min-cost-climbing-stairs/" target="_blank" class="problem-link">746. Min Cost Climbing Stairs</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch10-p3" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td><a href="https://leetcode.com/problems/coin-change/" target="_blank" class="problem-link">322. Coin Change</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch10-p4" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/" target="_blank" class="problem-link">714. Best Time to Buy and Sell Stock with Transaction Fee</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch10-p5" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/" target="_blank" class="problem-link">309. Best Time to Buy and Sell Stock with Cooldown</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch10-p6" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td><a href="https://leetcode.com/problems/unique-paths-ii/" target="_blank" class="problem-link">63. Unique Paths II</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch10-p7" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td><a href="https://leetcode.com/problems/minimum-falling-path-sum/" target="_blank" class="problem-link">931. Minimum Falling Path Sum</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch10-p8" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td><a href="https://leetcode.com/problems/house-robber/" target="_blank" class="problem-link">198. House Robber</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch10-p9" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td><a href="https://leetcode.com/problems/longest-common-subsequence/" target="_blank" class="problem-link">1143. Longest Common Subsequence</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch10-p10" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>10</td><td><a href="https://leetcode.com/problems/edit-distance/" target="_blank" class="problem-link">72. Edit Distance</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch10-p11" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>11</td><td><a href="https://leetcode.com/problems/word-break/" target="_blank" class="problem-link">139. Word Break</a></td><td class="diff-medium">Medium</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     Ch 11 — Bonus Topics
═══════════════════════════════════════════════ -->
<div class="ch-card" id="ch11" data-ch="ch11" style="--ch-accent: linear-gradient(90deg,#00c9a7,#4361ee);">
  <div class="ch-header">
    <div class="ch-num">Ch11</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Bonus Topics — Tries, Bit Manipulation, Intervals</div>
      <div class="ch-meta">
        <span class="ch-badge">Advanced</span>
        <a href="{{ '/learning/dsa/intervals/ch11-bonus-topics/' | relative_url }}" class="ch-badge notes-live">📄 Chapter Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/6 solved</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">11.1 Tries (Prefix Trees)</div>
    <div class="dsa-pattern-box">
      <ul>
        <li>Store strings character by character. Each node = one character; isEnd flag marks valid word</li>
        <li>O(m) insert and search where m = string length. Use for: autocomplete, prefix search</li>
      </ul>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show Trie C++ Template</button>
    <div class="code-block-wrap">
{% highlight cpp %}
struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool isEnd = false;
};
class Trie {
    TrieNode* root = new TrieNode();
public:
    void insert(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (!curr->children.count(c)) curr->children[c] = new TrieNode();
            curr = curr->children[c];
        }
        curr->isEnd = true;
    }
    bool search(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (!curr->children.count(c)) return false;
            curr = curr->children[c];
        }
        return curr->isEnd;
    }
};
{% endhighlight %}
    </div>
    <div class="ch-section-label">11.2 Bit Manipulation</div>
    <div class="dsa-pattern-box">
      <ul>
        <li>n & (n-1): removes lowest set bit (check power of 2: n&(n-1)==0)</li>
        <li>n & (-n): isolates lowest set bit</li>
        <li>XOR: a^a=0, a^0=a — find single non-duplicate element</li>
      </ul>
    </div>
    <div class="ch-section-label">Practice Problems</div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Problem</th><th>Difficulty</th></tr></thead>
      <tbody>
        <tr data-key="ch11-p1" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td><a href="https://leetcode.com/problems/implement-trie-prefix-tree/" target="_blank" class="problem-link">208. Implement Trie (Prefix Tree)</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch11-p2" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td><a href="https://leetcode.com/problems/search-suggestions-system/" target="_blank" class="problem-link">1268. Search Suggestions System</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch11-p3" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td><a href="https://leetcode.com/problems/single-number/" target="_blank" class="problem-link">136. Single Number (XOR)</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch11-p4" data-diff="easy"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td><a href="https://leetcode.com/problems/number-of-1-bits/" target="_blank" class="problem-link">191. Number of 1 Bits</a></td><td class="diff-easy">Easy</td></tr>
        <tr data-key="ch11-p5" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td><a href="https://leetcode.com/problems/insert-interval/" target="_blank" class="problem-link">57. Insert Interval</a></td><td class="diff-medium">Medium</td></tr>
        <tr data-key="ch11-p6" data-diff="medium"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td><a href="https://leetcode.com/problems/merge-intervals/" target="_blank" class="problem-link">56. Merge Intervals</a></td><td class="diff-medium">Medium</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ═══════════════════════════════════════════════
     Ch 12 — Study Plan & Cheatsheet
═══════════════════════════════════════════════ -->
<div class="ch-card" id="ch12" data-ch="ch12" style="--ch-accent: linear-gradient(90deg,#00c9a7,#00b4d8);">
  <div class="ch-header">
    <div class="ch-num">Ch12</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Study Plan & Complexity Cheatsheet</div>
      <div class="ch-meta">
        <span class="ch-badge">Reference</span>
        <a href="{{ '/learning/dsa/ch12-cheat-sheet/' | relative_url }}" class="ch-badge notes-live">📄 Chapter Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row" style="display:none;"></div>
  <div class="ch-body">
    <div class="ch-section-label">Phase 1 — Foundations (Weeks 1–4)</div>
    <div class="dsa-pattern-box">
      <ul>
        <li>Week 1: Ch0 Big O + Ch1 Two Pointers. Solve all Easy problems.</li>
        <li>Week 2: Ch1 Sliding Window + Prefix Sum. Solve all Easy + 2 Medium.</li>
        <li>Week 3: Ch2 Hashing. Core patterns — Two Sum, freq count, grouping.</li>
        <li>Week 4: Ch3 Linked Lists. All patterns — fast/slow, reversal, merge.</li>
      </ul>
    </div>
    <div class="ch-section-label">Phase 2 — Core (Weeks 5–9)</div>
    <div class="dsa-pattern-box">
      <ul>
        <li>Week 5: Ch4 Stacks (monotonic, bracket matching).</li>
        <li>Week 6–7: Ch5 Trees — DFS first (preorder, postorder, LCA), then BFS + BST.</li>
        <li>Week 8: Ch5 Graphs — DFS + BFS + Union-Find.</li>
        <li>Week 9: Ch6 Heaps + Ch7 Greedy.</li>
      </ul>
    </div>
    <div class="ch-section-label">Phase 3 — Advanced (Weeks 10–13)</div>
    <div class="dsa-pattern-box">
      <ul>
        <li>Week 10: Ch8 Binary Search — standard + answer space search.</li>
        <li>Week 11: Ch9 Backtracking — all generation/constrained problems.</li>
        <li>Week 12–13: Ch10 DP — 1D, 2D, state machine, knapsack.</li>
      </ul>
    </div>
    <div class="ch-section-label">Complexity Cheatsheet</div>
    <div class="cheatsheet-grid">
      <div class="cheatsheet-card">
        <h4>Array / String</h4>
        <table><tr><td>Access</td><td>O(1)</td></tr><tr><td>Search</td><td>O(n)</td></tr><tr><td>Insert/Delete</td><td>O(n)</td></tr><tr><td>Append</td><td>O(1) amort.</td></tr></table>
      </div>
      <div class="cheatsheet-card">
        <h4>HashMap / HashSet</h4>
        <table><tr><td>Insert</td><td>O(1) avg</td></tr><tr><td>Lookup</td><td>O(1) avg</td></tr><tr><td>Delete</td><td>O(1) avg</td></tr><tr><td>Worst case</td><td>O(n)</td></tr></table>
      </div>
      <div class="cheatsheet-card">
        <h4>Binary Tree</h4>
        <table><tr><td>DFS / BFS</td><td>O(n)</td></tr><tr><td>BST search</td><td>O(h)</td></tr><tr><td>BST balanced</td><td>O(log n)</td></tr><tr><td>Space</td><td>O(h) stack</td></tr></table>
      </div>
      <div class="cheatsheet-card">
        <h4>Heap</h4>
        <table><tr><td>Push</td><td>O(log n)</td></tr><tr><td>Pop</td><td>O(log n)</td></tr><tr><td>Peek</td><td>O(1)</td></tr><tr><td>Build</td><td>O(n)</td></tr></table>
      </div>
      <div class="cheatsheet-card">
        <h4>Sorting</h4>
        <table><tr><td>std::sort</td><td>O(n log n)</td></tr><tr><td>Counting sort</td><td>O(n+k)</td></tr><tr><td>Radix sort</td><td>O(nk)</td></tr><tr><td>Merge sort</td><td>O(n log n)</td></tr></table>
      </div>
      <div class="cheatsheet-card">
        <h4>Graph</h4>
        <table><tr><td>BFS / DFS</td><td>O(V+E)</td></tr><tr><td>Dijkstra</td><td>O((V+E)log V)</td></tr><tr><td>Union-Find</td><td>O(α(n))≈O(1)</td></tr><tr><td>Topo sort</td><td>O(V+E)</td></tr></table>
      </div>
    </div>
  </div>
</div>

</div><!-- end .dsa-chapters -->

<div style="text-align:center;padding:2rem 0 1rem;">
  <a href="{{ '/roadmap/' | relative_url }}" style="display:inline-block;padding:0.6rem 1.4rem;background:linear-gradient(135deg,#00c9a7,#00b4d8);color:#fff;border-radius:8px;text-decoration:none;font-size:0.9rem;font-weight:700;">← Back to All Roadmaps</a>
</div>
