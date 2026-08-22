---
title: "Ch2 — Hashing"
description: "All Roadmaps › DSA Mastery › Chapter 2 Chapter 2 · Intermediate · Prereq: Chapter 1 Hashing — Hash Maps & Hash Sets Hash Maps & Hash Sets · Collision Handling · Frequency…"
domain: dsa
track: dsa-mastery
order: 2
url: /learning/dsa/hashing/ch2-hashing/
---

<div class="chapter-hero">
  <div class="chapter-hero-inner">
    <div class="ch-hero-breadcrumb">
      <a href="/roadmap/">All Roadmaps</a> ›
      <a href="/learning/dsa/dsa-roadmap/">DSA Mastery</a> ›
      Chapter 2
    </div>
    <div class="chapter-num-badge">Chapter 2 · Intermediate · Prereq: Chapter 1</div>
    <h1>Hashing — Hash Maps & Hash Sets</h1>
    <p class="chapter-hero-sub">Hash Maps & Hash Sets · Collision Handling · Frequency Counting · Grouping — the single most powerful technique for reducing O(n²) solutions to O(n).</p>
    <div class="chapter-meta-row">
      <span class="ch-meta-pill teal">11 Sections</span>
      <span class="ch-meta-pill">13 Practice Problems</span>
      <span class="ch-meta-pill">Intermediate</span>
      <a href="/learning/dsa/dsa-roadmap/#ch2" class="ch-nav-btn">← Back to Roadmap</a>
    </div>
  </div>
</div>

<div class="chapter-content">

<div class="chapter-section">
<h2 class="section-heading">Section 1 — What Is Hashing?</h2>
<p>Hashing is the process of converting a key of any type into a fixed-size integer (the <strong>hash code</strong>) and using that integer as an index into an array (the <strong>hash table</strong>). This gives us <strong>O(1) average-case</strong> insertion, deletion, and lookup — regardless of how many elements are stored.</p>
<div class="insight-box">
  <span class="insight-label">Why Hashing Matters</span>
  This is the <strong>single most powerful technique</strong> for reducing O(n) or O(n²) solutions to O(n). Almost every medium-hard problem that does not involve ordering or hierarchy has a hash-based optimal solution.
</div>

<h3 class="section-subheading">1.1 — Hash Function & Collision Handling</h3>
<p>A hash function maps keys to indices. Two keys can hash to the same index — a <strong>collision</strong>. C++ resolves collisions via <strong>chaining</strong> (linked list at each index) in <code>unordered_map</code>.</p>
<div class="insight-box">
  <ul>
    <li><strong>Chaining:</strong> Each bucket holds a linked list. Average O(1); worst case O(n) if all keys collide.</li>
    <li><strong>Load factor:</strong> When table is ≥ 75% full, it rehashes to a larger table. O(n) but amortized O(1).</li>
    <li><strong>In C++:</strong> <code>unordered_map</code> uses open addressing with <code>std::hash</code> internally.</li>
  </ul>
</div>

<h3 class="section-subheading">1.2 — C++ API</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// unordered_map — key-value store
unordered_map<string, int> freq;
freq["hello"]++;                   // insert or increment
freq.count("world");               // 0 or 1 — check existence
freq.find("hello");                // returns iterator
freq.erase("hello");               // remove key

// unordered_set — existence only
unordered_set<int> seen;
seen.insert(42);
seen.count(42);  // 1 if exists, 0 if not

// Default int value in map is 0
unordered_map<int,int> cnt;
cnt[key]++;  // OK — default-initialises to 0 then increments
{% endhighlight %}
</div>
<div class="ch-cplx-row">
  <span class="ch-cplx"><span>All ops average</span>O(1)</span>
  <span class="ch-cplx"><span>Space</span>O(n)</span>
  <span class="ch-cplx"><span>Worst case</span>O(n)</span>
</div>
</div>

<div class="chapter-section">
<h2 class="section-heading">Section 2 — Pattern: Existence Check</h2>
<p>Use <code>unordered_set</code> when you just want to know if a value has been seen. O(1) average per lookup.</p>
<div class="ch-code-wrap">
{% highlight cpp %}
// Pangram check — has the sentence all 26 letters?
unordered_set<char> letters(sentence.begin(), sentence.end());
return letters.size() == 26;

// Has any duplicate?
unordered_set<int> seen;
for (int x : nums) {
    if (seen.count(x)) return true; // duplicate found
    seen.insert(x);
}
return false;
{% endhighlight %}
</div>
</div>

<div class="chapter-section">
<h2 class="section-heading">Section 3 — Pattern: Frequency Count</h2>
<p>Use <code>unordered_map&lt;T, int&gt;</code> to count how many times each element appears. Foundation for anagram, top-K, most-frequent problems.</p>
<div class="ch-code-wrap">
{% highlight cpp %}
// Frequency count for any iterable
unordered_map<int,int> freq;
for (int x : arr) freq[x]++;

// Is Anagram — same char frequencies?
unordered_map<char,int> cnt;
for (char c : s) cnt[c]++;
for (char c : t) {
    if (--cnt[c] < 0) return false;
}
return true;

// Top K frequent elements — combine freq map + heap
unordered_map<int,int> freq;
for (int x : nums) freq[x]++;
priority_queue<pair<int,int>, vector<pair<int,int>>,
    // min-heap by frequency
    greater<pair<int,int>>> pq;
for (auto& [val, cnt] : freq) {
    pq.push({cnt, val});
    if (pq.size() > k) pq.pop();
}
{% endhighlight %}
</div>
</div>

<div class="chapter-section">
<h2 class="section-heading">Section 4 — Pattern: Two-Sum Lookup</h2>
<p>For each element x, check if its complement (target - x) exists in the hash map. One-pass O(n).</p>
<div class="insight-box">
  <span class="insight-label">General Two-Sum Pattern</span>
  Store what you have seen so far. For each new element, ask: "Is its complement already here?" This converts O(n²) nested search into O(n) with one hash table lookup.
</div>
<div class="ch-code-wrap">
{% highlight cpp %}
// Classical two-sum — return indices
unordered_map<int,int> seen; // val → index
for (int i = 0; i < nums.size(); i++) {
    if (seen.count(target - nums[i]))
        return {seen[target-nums[i]], i};
    seen[nums[i]] = i;
}
// Counting elements (x+1 exists for all x in set)
unordered_set<int> s(arr.begin(), arr.end());
int count = 0;
for (int x : arr) if (s.count(x+1)) count++;
return count;
{% endhighlight %}
</div>
</div>

<div class="chapter-section">
<h2 class="section-heading">Section 5 — Pattern: Grouping</h2>
<p>Map a grouping key to a list of all elements sharing that key. Classic example: group anagrams by their sorted form.</p>
<div class="ch-code-wrap">
{% highlight cpp %}
// Group Anagrams — map sorted key → strings
unordered_map<string, vector<string>> groups;
for (string& s : strs) {
    string key = s;
    sort(key.begin(), key.end());
    groups[key].push_back(s);
}
vector<vector<string>> result;
for (auto& [key, group] : groups) result.push_back(group);
return result;
{% endhighlight %}
</div>
</div>

<div class="chapter-section">
<h2 class="section-heading">Section 6 — Pattern: Sliding Window + HashMap</h2>
<p>Maintain a frequency map of elements in the current window. Expand right, shrink left when constraint violated.</p>
<div class="ch-code-wrap">
{% highlight cpp %}
// Longest substring with at most k distinct characters
unordered_map<char,int> freq;
int left = 0, ans = 0;
for (int right = 0; right < s.size(); right++) {
    freq[s[right]]++;
    while (freq.size() > k) {               // shrink
        if (--freq[s[left]] == 0) freq.erase(s[left]);
        left++;
    }
    ans = max(ans, right - left + 1);
}
{% endhighlight %}
</div>
</div>

<div class="chapter-section">
<h2 class="section-heading">Section 7 — Pattern: Prefix Sum + HashMap</h2>
<p>Store cumulative prefix sums and their frequencies. For each prefix sum curr, the count of subarrays summing to target ending at this index = freq[curr - target].</p>
<div class="ch-code-wrap">
{% highlight cpp %}
// Count subarrays with sum == k
unordered_map<int,int> freq; freq[0] = 1;
int curr = 0, ans = 0;
for (int x : nums) {
    curr += x;
    ans += freq[curr - k];  // subarrays ending here summing to k
    freq[curr]++;
}
// Count subarrays with equal number of 0s and 1s
// Transform: 0 → -1. Then counts subarrays summing to 0.
unordered_map<int,int> freq; freq[0] = 1;
int curr = 0, ans = 0;
for (int x : nums) {
    curr += (x == 1 ? 1 : -1);
    ans += freq[curr];
    freq[curr]++;
}
{% endhighlight %}
</div>
</div>

<div class="chapter-section">
<h2 class="section-heading">Practice Problems</h2>
<div class="ch-ed-problems">
<table>
  <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><a href="https://leetcode.com/problems/check-if-the-sentence-is-pangram/" target="_blank">1832. Check if the Sentence Is Pangram</a></td><td>Existence check (set)</td><td class="diff-easy">Easy</td></tr>
    <tr><td>2</td><td><a href="https://leetcode.com/problems/missing-number/" target="_blank">268. Missing Number</a></td><td>Existence check (set)</td><td class="diff-easy">Easy</td></tr>
    <tr><td>3</td><td><a href="https://leetcode.com/problems/counting-elements/" target="_blank">1426. Counting Elements</a></td><td>Two-sum lookup (x+1)</td><td class="diff-easy">Easy</td></tr>
    <tr><td>4</td><td><a href="https://leetcode.com/problems/two-sum/" target="_blank">1. Two Sum</a></td><td>Two-sum lookup</td><td class="diff-easy">Easy</td></tr>
    <tr><td>5</td><td><a href="https://leetcode.com/problems/ransom-note/" target="_blank">383. Ransom Note</a></td><td>Frequency count</td><td class="diff-easy">Easy</td></tr>
    <tr><td>6</td><td><a href="https://leetcode.com/problems/jewels-and-stones/" target="_blank">771. Jewels and Stones</a></td><td>Existence check (set)</td><td class="diff-easy">Easy</td></tr>
    <tr><td>7</td><td><a href="https://leetcode.com/problems/find-players-with-zero-or-one-losses/" target="_blank">2225. Find Players With Zero or One Losses</a></td><td>Frequency count (map)</td><td class="diff-medium">Medium</td></tr>
    <tr><td>8</td><td><a href="https://leetcode.com/problems/largest-unique-number/" target="_blank">1133. Largest Unique Number</a></td><td>Frequency count (unique = 1)</td><td class="diff-easy">Easy</td></tr>
    <tr><td>9</td><td><a href="https://leetcode.com/problems/maximum-number-of-balloons/" target="_blank">1189. Maximum Number of Balloons</a></td><td>Frequency ratio</td><td class="diff-easy">Easy</td></tr>
    <tr><td>10</td><td><a href="https://leetcode.com/problems/group-anagrams/" target="_blank">49. Group Anagrams</a></td><td>Grouping (sorted key)</td><td class="diff-medium">Medium</td></tr>
    <tr><td>11</td><td><a href="https://leetcode.com/problems/top-k-frequent-elements/" target="_blank">347. Top K Frequent Elements</a></td><td>Frequency count + heap</td><td class="diff-medium">Medium</td></tr>
    <tr><td>12</td><td><a href="https://leetcode.com/problems/subarray-sum-equals-k/" target="_blank">560. Subarray Sum Equals K</a></td><td>Prefix sum + HashMap</td><td class="diff-medium">Medium</td></tr>
    <tr><td>13</td><td><a href="https://leetcode.com/problems/lru-cache/" target="_blank">146. LRU Cache</a></td><td>HashMap + Doubly Linked List</td><td class="diff-medium">Medium</td></tr>
  </tbody>
</table>
</div>
</div>

</div><!-- end .chapter-content -->

<div class="chapter-nav-footer">
  <a href="/learning/dsa/arrays/ch1-arrays-strings/" class="ch-nav-footer-btn">← Ch1: Arrays & Strings</a>
  <a href="/learning/dsa/linked-list/ch3-linked-lists/" class="ch-nav-footer-btn primary">Next: Ch3 — Linked Lists →</a>
</div>
