---
title: "Ch7 — Greedy Algorithms"
description: "All Roadmaps › DSA Mastery › Chapter 7 Chapter 7 · Intermediate · Prereq: Chapter 6 Greedy Algorithms Master the paradigm of short-term optimal decisions."
domain: dsa
track: dsa-mastery
order: 7
url: /learning/dsa/greedy/ch7-greedy/
---

<div class="chapter-hero">
  <div class="chapter-hero-inner">
    <div class="ch-hero-breadcrumb">
      <a href="/roadmap/">All Roadmaps</a> ›
      <a href="/learning/dsa/dsa-roadmap/">DSA Mastery</a> ›
      Chapter 7
    </div>
    <div class="chapter-num-badge">Chapter 7 · Intermediate · Prereq: Chapter 6</div>
    <h1>Greedy Algorithms</h1>
    <p class="chapter-hero-sub">Master the paradigm of short-term optimal decisions. Learn interval scheduling, prove correctness with exchange arguments, and conquer the sweeping line.</p>
    <div class="chapter-meta-row">
      <span class="ch-meta-pill teal">10 Sections</span>
      <span class="ch-meta-pill">8 Practice Problems</span>
      <span class="ch-meta-pill">Intermediate</span>
      <a href="/learning/dsa/dsa-roadmap/#ch7" class="ch-nav-btn">← Back to Roadmap</a>
    </div>
  </div>
</div>

<div class="chapter-content">

<!-- Section 1 -->
<div class="chapter-section">
<h2 class="section-heading">Section 1 — What Is a Greedy Algorithm?</h2>
<p>A greedy algorithm builds a solution by making the locally optimal choice at each step without reconsidering past decisions. It never backtracks. For greedy to yield a globally optimal solution, the problem must satisfy two key properties.</p>

<h3 class="section-subheading">Two Conditions for Greedy Correctness</h3>
<ul>
  <li><strong>1. GREEDY CHOICE PROPERTY:</strong> A globally optimal solution can be constructed by making locally optimal (greedy) choices. The greedy choice at step <code>k</code> is <em>safe</em> — it is part of some optimal solution.</li>
  <li><strong>2. OPTIMAL SUBSTRUCTURE:</strong> An optimal solution to the whole problem contains optimal solutions to its subproblems. After making the greedy choice, the remaining subproblem has the same structure.</li>
  <li>If BOTH conditions hold, greedy is correct. If either fails, greedy gives a wrong answer and you need DP or backtracking.</li>
  <li><strong>Proving greedy correctness:</strong> use the <em>exchange argument</em> — assume an optimal solution makes a different choice; show that swapping to the greedy choice does not worsen the result.</li>
</ul>

<h3 class="section-subheading">1.1 — Greedy vs Dynamic Programming</h3>
<div class="ch-ed-problems">
  <table>
    <thead>
      <tr><th>Dimension</th><th>Greedy</th><th>Dynamic Programming</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Decision style</strong></td><td>Make one irreversible choice per step</td><td>Explore all choices; store best subproblem results</td></tr>
      <tr><td><strong>Subproblem dependency</strong></td><td>Each step independent of future</td><td>Subproblems may overlap; memoisation avoids recompute</td></tr>
      <tr><td><strong>Complexity (typical)</strong></td><td><code>O(n log n)</code> or <code>O(n)</code></td><td><code>O(n^2)</code> or <code>O(n * capacity)</code></td></tr>
      <tr><td><strong>Space (typical)</strong></td><td><code>O(1)</code> or <code>O(n)</code></td><td><code>O(n)</code> to <code>O(n^2)</code></td></tr>
      <tr><td><strong>When correct</strong></td><td>Greedy choice property + optimal substructure</td><td>Optimal substructure alone (no greedy choice needed)</td></tr>
      <tr><td><strong>Classic problems</strong></td><td>Activity selection, Huffman, Dijkstra, Jump Game</td><td>0/1 Knapsack, Coin Change, LCS, Edit Distance</td></tr>
      <tr><td><strong>Key risk</strong></td><td>Easy to construct a wrong greedy — always verify</td><td>Always correct if recurrence is right; harder to optimise</td></tr>
    </tbody>
  </table>
</div>

<div class="insight-box">
  <span class="insight-label">💰 Real-World Analogy: Making Change</span>
  <p><strong>Problem:</strong> make change for 41 cents using fewest coins (denominations: 25, 10, 5, 1).</p>
  <p><strong>Greedy:</strong> always pick the largest coin that does not exceed the remaining amount.</p>
  <ul>
      <li><code>41</code> -> pick 25 (remain 16) -> pick 10 (remain 6) -> pick 5 (remain 1) -> pick 1.</li>
      <li>Result: <strong>4 coins</strong>. This is optimal for standard US coin denominations.</li>
  </ul>
  <p><strong>BUT:</strong> for denominations <code>{1, 3, 4}</code>, greedy fails on amount 6. Greedy picks <code>4+1+1=3</code> coins; optimal is <code>3+3=2</code> coins.</p>
  <p>This illustrates why greedy correctness must always be proven — it is not automatic.</p>
</div>
</div>

<!-- Section 2 -->
<div class="chapter-section">
<h2 class="section-heading">Section 2 — Visual Diagrams: Core Greedy Patterns</h2>

<h3 class="section-subheading">Diagram 1 — Interval Scheduling (Activity Selection)</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">Intervals</span>
<pre><code>Interval Scheduling: Earliest-Finish-Time Greedy
  Problem: select maximum number of non-overlapping intervals.
  Intervals: [1,4], [3,5], [0,6], [5,7], [3,9], [5,10], [6,11], [8,12], [8,11], [2,14]

  Greedy rule: ALWAYS pick the interval with the EARLIEST END TIME
  that does not conflict with the last selected interval.
  Proof: finishing early leaves maximum room for future intervals.

  Sort by end time:
  [1,4] [3,5] [0,6] [5,7] [3,9] [5,10] [6,11] [8,11] [8,12] [2,14]

  Step 1: Pick [1,4].  last_end = 4.
  Step 2: [3,5]  start=3 < last_end=4 -> SKIP
  Step 3: [0,6]  start=0 < 4          -> SKIP
  Step 4: [5,7]  start=5 >= 4         -> PICK.  last_end = 7.
  Step 5: [3,9]  start=3 < 7          -> SKIP
  Step 6: [5,10] start=5 < 7          -> SKIP
  Step 7: [6,11] start=6 < 7          -> SKIP
  Step 8: [8,11] start=8 >= 7         -> PICK.  last_end = 11.
  Step 9: [8,12] start=8 < 11         -> SKIP
  Step 10:[2,14] start=2 < 11         -> SKIP

  Selected: [1,4], [5,7], [8,11]  =  3 intervals.  Optimal!</code></pre>
</div>

<h3 class="section-subheading">Diagram 2 — Jump Game</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">Jump Game trace</span>
<pre><code>Jump Game: maxReach Greedy
  nums = [2, 3, 1, 1, 4]
  nums[i] = max jump length FROM index i.
  Question: can you reach the last index?

  Greedy: track 'maxReach' = farthest index reachable so far.

  i=0: maxReach = max(0, 0+nums[0]) = max(0, 0+2) = 2
  i=1: i=1 <= maxReach=2, ok. maxReach = max(2, 1+3) = 4
  i=2: i=2 <= maxReach=4, ok. maxReach = max(4, 2+1) = 4
  i=3: i=3 <= maxReach=4, ok. maxReach = max(4, 3+1) = 4
  i=4: i=4 <= maxReach=4, ok. maxReach = max(4, 4+4) = 8
  maxReach >= last index (4) -> return true.

  Impossible example: nums = [3, 2, 1, 0, 4]
  i=0: maxReach = 3
  i=1: maxReach = max(3, 1+2) = 3
  i=2: maxReach = max(3, 2+1) = 3
  i=3: maxReach = max(3, 3+0) = 3
  i=4: i=4 > maxReach=3 -> STUCK.  Return false.

  Key insight: if we ever reach a position where i > maxReach,
  we are stuck in a 'zero island' with no way forward.</code></pre>
</div>

<h3 class="section-subheading">Diagram 3 — Kadane's Algorithm (Maximum Subarray)</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">Kadane trace</span>
<pre><code>Kadane's Algorithm: Maximum Subarray Trace
  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

  Greedy insight: extend current subarray if it helps; restart if current sum < 0.
  'currSum' = best sum ending at current index.
  'maxSum'  = best sum seen so far.

  i=0: currSum = max(-2, -2)  = -2.  maxSum = -2
  i=1: currSum = max( 1, -2+1)=  1.  maxSum =  1
  i=2: currSum = max(-3,  1-3)= -2.  maxSum =  1
  i=3: currSum = max( 4, -2+4)=  4.  maxSum =  4
  i=4: currSum = max(-1,  4-1)=  3.  maxSum =  4
  i=5: currSum = max( 2,  3+2)=  5.  maxSum =  5
  i=6: currSum = max( 1,  5+1)=  6.  maxSum =  6   <- peak
  i=7: currSum = max(-5,  6-5)=  1.  maxSum =  6
  i=8: currSum = max( 4,  1+4)=  5.  maxSum =  6

  Answer: maxSum = 6  (subarray [4, -1, 2, 1])

  Greedy rule: if adding current element to currSum makes it negative,
  it is better to start fresh from the current element (restart).</code></pre>
</div>
</div>

<!-- Section 3 -->
<div class="chapter-section">
<h2 class="section-heading">Section 3 — Real-World Use Cases</h2>
<div class="ch-ed-problems">
  <table>
    <thead>
      <tr><th>Problem</th><th>Greedy Strategy</th><th>Real-World System</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Activity / interval selection</strong></td><td>Sort by end time; pick earliest-finishing</td><td>Conference room booking, CPU scheduling</td></tr>
      <tr><td><strong>Minimum spanning tree</strong></td><td>Kruskal: pick cheapest safe edge</td><td>Network layout, road planning</td></tr>
      <tr><td><strong>Shortest path (no neg)</strong></td><td>Dijkstra: expand closest unvisited</td><td>GPS navigation, IP routing</td></tr>
      <tr><td><strong>Huffman encoding</strong></td><td>Merge lowest-freq symbols first</td><td>gzip compression, JPEG encoding</td></tr>
      <tr><td><strong>Fractional knapsack</strong></td><td>Sort by value/weight; take highest ratio</td><td>Portfolio optimisation</td></tr>
      <tr><td><strong>Job scheduling (lateness)</strong></td><td>Sort jobs by deadline ascending</td><td>OS task scheduling</td></tr>
      <tr><td><strong>Gas station circuit</strong></td><td>Track surplus; restart on deficit</td><td>Logistics route planning</td></tr>
    </tbody>
  </table>
</div>
</div>

<!-- Section 4 -->
<div class="chapter-section">
<h2 class="section-heading">Section 4 — Core Concepts & Algorithms</h2>

<h3 class="section-subheading">4.1 — Interval Scheduling & Merging</h3>
<p>Maximum Non-Overlapping Intervals (Activity Selection)</p>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Activity Selection — O(n log n)
// Sort by end time; greedily pick earliest-finishing non-conflicting interval
int maxNonOverlapping(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;
    sort(intervals.begin(), intervals.end(),
         [](auto& a, auto& b){ return a[1] < b[1]; }); // sort by end time
    int count = 1, lastEnd = intervals[0][1];
    for (int i = 1; i < (int)intervals.size(); i++) {
        if (intervals[i][0] >= lastEnd) {
            count++; lastEnd = intervals[i][1];
        }
    }
    return count;
}
{% endhighlight %}
</div>

<p>Merge Overlapping Intervals</p>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Merge Overlapping Intervals — O(n log n)
// Sort by start time; merge when current interval overlaps previous
vector<vector<int>> merge(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end()); // sort by start
    vector<vector<int>> res;
    for (auto& iv : intervals) {
        if (res.empty() || iv[0] > res.back()[1]) res.push_back(iv);
        else res.back()[1] = max(res.back()[1], iv[1]);
    }
    return res;
}
{% endhighlight %}
</div>

<h3 class="section-subheading">4.2 — Jump Game Variants</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// JUMP GAME I (LC 55) — Can you reach the last index?
bool canJump(vector<int>& nums) {
    int maxReach = 0;
    for (int i = 0; i < (int)nums.size(); i++) {
        if (i > maxReach) return false;    // stuck
        maxReach = max(maxReach, i + nums[i]);
    }
    return true;
}

// JUMP GAME II (LC 45) — Minimum jumps to reach end
int jump(vector<int>& nums) {
    int jumps = 0, currEnd = 0, farthest = 0;
    for (int i = 0; i < (int)nums.size()-1; i++) {
        farthest = max(farthest, i + nums[i]);
        if (i == currEnd) {   // reached end of jump range
            jumps++; currEnd = farthest;
        }
    }
    return jumps;
}
{% endhighlight %}
</div>

<h3 class="section-subheading">4.3 — Kadane's Algorithm</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Kadane's Algorithm — O(n) O(1)
// LeetCode 53 — Maximum Subarray
int maxSubArray(vector<int>& nums) {
    int currSum = nums[0], maxSum = nums[0];
    for (int i = 1; i < (int)nums.size(); i++) {
        currSum = max(nums[i], currSum + nums[i]);
        maxSum = max(maxSum, currSum);
    }
    return maxSum;
}
{% endhighlight %}
</div>

<h3 class="section-subheading">4.4 — Gas Station Circuit</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// LeetCode 134 — Gas Station
int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
    int totalSurplus = 0, currSurplus = 0, start = 0;
    for (int i = 0; i < (int)gas.size(); i++) {
        int diff = gas[i] - cost[i];
        totalSurplus += diff; currSurplus += diff;
        if (currSurplus < 0) { // Reset if deficit
            start = i + 1; currSurplus = 0;
        }
    }
    return totalSurplus >= 0 ? start : -1;
}
{% endhighlight %}
</div>

<h3 class="section-subheading">4.5 — Huffman Encoding</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Huffman Encoding — O(n log n)
struct HNode {
    int freq; char ch;
    HNode *left, *right;
    HNode(int f, char c) : freq(f), ch(c), left(nullptr), right(nullptr) {}
};

HNode* buildHuffman(unordered_map<char,int>& freq) {
    auto cmp = [](HNode* a, HNode* b){ return a->freq > b->freq; };
    priority_queue<HNode*, vector<HNode*>, decltype(cmp)> pq(cmp);

    for (auto& [ch, f] : freq) pq.push(new HNode(f, ch));

    while (pq.size() > 1) {
        HNode* l = pq.top(); pq.pop();
        HNode* r = pq.top(); pq.pop();
        HNode* parent = new HNode(l->freq + r->freq, '\0');
        parent->left = l; parent->right = r;
        pq.push(parent);
    }
    return pq.top(); // root
}
{% endhighlight %}
</div>

</div>

<!-- Section 5 -->
<div class="chapter-section">
<h2 class="section-heading">Section 5 — Pattern Recognition Guide</h2>
<div class="ch-ed-problems">
  <table>
    <thead>
      <tr><th>If the problem asks...</th><th>Greedy Strategy</th><th>Sort / Order By</th></tr>
    </thead>
    <tbody>
      <tr><td>Max non-overlapping intervals</td><td>Pick earliest end time first</td><td>End time ascending</td></tr>
      <tr><td>Min intervals to remove</td><td><code>n</code> minus max non-overlapping</td><td>End time ascending</td></tr>
      <tr><td>Min meeting rooms needed</td><td>Sweep events +1/-1</td><td>Event time ascending</td></tr>
      <tr><td>Can reach the last index?</td><td>Track <code>maxReach</code></td><td>No sort — L to R</td></tr>
      <tr><td>Min jumps to last index</td><td>Expand jump window greedily</td><td>No sort — L to R</td></tr>
      <tr><td>Max contiguous subarray sum</td><td>Kadane: restart when sum < 0</td><td>No sort — L to R</td></tr>
      <tr><td>Best time to buy and sell stock</td><td>Track min price; max profit</td><td>No sort — L to R</td></tr>
      <tr><td>Assign cookies to children</td><td>Match smallest sufficient cookie</td><td>Both arrays asc</td></tr>
      <tr><td>Partition labels</td><td>Greedily extend to last occurence</td><td>Last occ map</td></tr>
    </tbody>
  </table>
</div>

<div class="insight-box">
  <span class="insight-label">🔍 How to Recognise a Greedy Problem</span>
  <ul>
    <li><strong>SIGNAL 1:</strong> "Maximum number of..." or "Minimum number of..." with intervals/tasks.</li>
    <li><strong>SIGNAL 2:</strong> Sorting the input by one dimension immediately unlocks a simple scan.</li>
    <li><strong>SIGNAL 3:</strong> At each step there is an obvious "best" local choice.</li>
    <li><strong>VERIFY:</strong> Assume optimal uses a different choice; show swapping to the greedy choice does not worsen the result.</li>
  </ul>
</div>
</div>

<!-- Section 6 -->
<div class="chapter-section">
<h2 class="section-heading">Section 6 — Complete C++ Implementations</h2>

<h3 class="section-subheading">6.1 — Non-overlapping Intervals</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Minimum intervals to remove so remaining are non-overlapping
// Time: O(n log n)  Space: O(1)
int eraseOverlapIntervals(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end(),
         [](auto& a, auto& b){ return a[1] < b[1]; });
    int keep = 1, lastEnd = intervals[0][1];
    for (int i = 1; i < (int)intervals.size(); i++) {
        if (intervals[i][0] >= lastEnd) {
            keep++; lastEnd = intervals[i][1];
        }
    }
    return (int)intervals.size() - keep;
}
{% endhighlight %}
</div>

<h3 class="section-subheading">6.2 — Partition Labels</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Partition Labels — O(n)
// Partition string so each letter appears in at most one part.
vector<int> partitionLabels(string s) {
    int last[26] = {};
    for (int i = 0; i < (int)s.size(); i++) last[s[i]-'a'] = i;

    vector<int> result;
    int start = 0, end = 0;
    for (int i = 0; i < (int)s.size(); i++) {
        end = max(end, last[s[i]-'a']); // extend partition
        if (i == end) {                 // partition boundary found
            result.push_back(end - start + 1);
            start = i + 1;
        }
    }
    return result;
}
{% endhighlight %}
</div>
</div>

<!-- Section 7 -->
<div class="chapter-section">
<h2 class="section-heading">Section 7 — Complexity Reference</h2>
<div class="ch-ed-problems">
  <table>
    <thead>
      <tr><th>Algorithm</th><th>Time</th><th>Space</th></tr>
    </thead>
    <tbody>
      <tr><td>Activity selection (max non-overlap)</td><td><code>O(n log n)</code></td><td><code>O(1)</code></td></tr>
      <tr><td>Merge overlapping intervals</td><td><code>O(n log n)</code></td><td><code>O(n)</code></td></tr>
      <tr><td>Minimum meeting rooms</td><td><code>O(n log n)</code></td><td><code>O(n)</code></td></tr>
      <tr><td>Jump Game I/II</td><td><code>O(n)</code></td><td><code>O(1)</code></td></tr>
      <tr><td>Kadane's (max subarray)</td><td><code>O(n)</code></td><td><code>O(1)</code></td></tr>
      <tr><td>Gas station circuit</td><td><code>O(n)</code></td><td><code>O(1)</code></td></tr>
      <tr><td>Partition labels</td><td><code>O(n)</code></td><td><code>O(1)</code></td></tr>
      <tr><td>Fractional knapsack / Huffman</td><td><code>O(n log n)</code></td><td><code>O(n)</code></td></tr>
    </tbody>
  </table>
</div>
</div>

<!-- Section 8 -->
<div class="chapter-section">
<h2 class="section-heading">Section 8 — Solved Problem 1: Jump Game</h2>

<div class="insight-box">
<span class="insight-label">1. Observations & Core Idea</span>
<p>In DP form, this is reachability. To reach <code>i</code>, we need to reach some <code>j &lt; i</code> where <code>j + nums[j] &gt;= i</code>. The DP takes <code>O(n^2)</code>.</p>
<p><strong>Greedy Insight:</strong> If we can reach any index <code>k</code>, we can naturally reach any index <code>&lt; k</code>. So we just need to track the single "farthest reachable index" (<code>maxReach</code>) scanned from left to right. If at index <code>i</code>, we find <code>i &gt; maxReach</code>, we are stranded!</p>
</div>

<h3 class="section-subheading">2. Approach Comparison</h3>
<div class="ch-ed-problems">
  <table>
    <thead>
      <tr><th>Approach</th><th>Time</th><th>Space</th><th>Method</th></tr>
    </thead>
    <tbody>
      <tr><td>Brute Force DP</td><td>O(n^2)</td><td>O(n)</td><td><code>dp[i] = any(dp[j])</code> for valid jumps</td></tr>
      <tr><td>Optimised Greedy</td><td>O(n)</td><td>O(1)</td><td>Update <code>maxReach = max(maxReach, i+nums[i])</code></td></tr>
    </tbody>
  </table>
</div>

<h3 class="section-subheading">3. Optimized Greedy Approach</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0;
        int n = nums.size();
        
        for (int i = 0; i < n; i++) {
            if (i > maxReach) {
                return false; // stranded at i
            }
            maxReach = max(maxReach, i + nums[i]);
            if (maxReach >= n - 1) {
                return true;  // early exit
            }
        }
        return true;
    }
};
{% endhighlight %}
</div>
</div>

<!-- Section 9 -->
<div class="chapter-section">
<h2 class="section-heading">Section 9 — Solved Problem 2: Merge Intervals</h2>

<div class="insight-box">
<span class="insight-label">1. Observations & Core Idea</span>
<p>Intervals can overlap in arbitrary orders. Standard greedy tells us: sort by START time.</p>
<p>If sorted by start time, overlapping intervals will always be strictly adjacent in the sorted array. If the current interval's start <code>&lt;=</code> the previous interval's end, they overlap. We merge them by making the new end = <code>max(end1, end2)</code>.</p>
</div>

<h3 class="section-subheading">2. Approach Comparison</h3>
<div class="ch-ed-problems">
  <table>
    <thead>
      <tr><th>Approach</th><th>Time</th><th>Space</th><th>Method</th></tr>
    </thead>
    <tbody>
      <tr><td>Graph Connected Components</td><td>O(n^2)</td><td>O(n^2)</td><td>Nodes are intervals; edges if overlap.</td></tr>
      <tr><td>Sort and Scan (Greedy)</td><td>O(n log n)</td><td>O(n)</td><td>Sort by start, merge adjacent continuously.</td></tr>
    </tbody>
  </table>
</div>

<h3 class="section-subheading">3. Optimized Greedy Approach</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        
        // 1. Sort by start coordinate
        sort(intervals.begin(), intervals.end());
        
        vector<vector<int>> merged;
        merged.push_back(intervals[0]);
        
        // 2. Scan and merge
        for (int i = 1; i < intervals.size(); i++) {
            int currentStart = intervals[i][0];
            int currentEnd = intervals[i][1];
            int lastEnd = merged.back()[1];
            
            if (currentStart <= lastEnd) {
                // Overlap: update ending
                merged.back()[1] = max(lastEnd, currentEnd);
            } else {
                // No overlap: strictly later interval
                merged.push_back(intervals[i]);
            }
        }
        
        return merged;
    }
};
{% endhighlight %}
</div>
</div>

<!-- Section 10 -->
<div class="chapter-section">
<h2 class="section-heading">Section 10 — Common Mistakes & Edge Cases</h2>
<ul>
  <li><strong>Assuming Greedy ALWAYS works:</strong> The #1 mistake is using a greedy approach where DP is required (e.g., 0/1 Knapsack where you greedily pick the highest value/weight ratio, but it leaves dead space). Always ask yourself: "Can I create a small test case where this greedy choice blocks the best answer?"</li>
  <li><strong>Sorting by the wrong attribute in intervals:</strong> Non-overlapping/activity selection -> Sort by END time. Merging -> Sort by START time. Meeting rooms -> Split into events and sort by TIME.</li>
  <li><strong>Tie-breaking incorrectly:</strong> E.g., in Meeting Rooms, if a meeting ends at time <code>t</code> and another starts at time <code>t</code>, the end must be processed FIRST (-1 before +1) to avoid allocating a phantom extra room.</li>
</ul>

<div class="insight-box">
<span class="insight-label">Warning</span>
<p><strong>Edge Cases to Consider:</strong></p>
<ul>
    <li>Empty inputs `[]` or single element `[0]`.</li>
    <li>Arrays with all negative numbers (Kadane's should return the max single negative, not `0`).</li>
    <li>Fully enclosed intervals: `[[1, 10], [2, 5]]`. When merging, `lastEnd` must be `max(10, 5)` = 10.</li>
</ul>
</div>
</div>

<!-- Practice Problems -->
<div class="chapter-section">
<h2 class="section-heading">Practice Problems</h2>
<p>Recommended progression for Greedy Algorithms:</p>
<div class="ch-ed-problems">
  <table>
    <thead>
      <tr><th>#</th><th>Problem</th><th>Difficulty</th><th>Key Concept</th></tr>
    </thead>
    <tbody>
      <tr><td>1</td><td><a href="https://leetcode.com/problems/maximum-69-number/">1323. Maximum 69 Number</a></td><td><span class="diff-easy">Easy</span></td><td>Greedy string math</td></tr>
      <tr><td>2</td><td><a href="https://leetcode.com/problems/maximum-units-on-a-truck/">1710. Maximum Units on a Truck</a></td><td><span class="diff-easy">Easy</span></td><td>Fractional knapsack desc</td></tr>
      <tr><td>3</td><td><a href="https://leetcode.com/problems/gas-station/">134. Gas Station</a></td><td><span class="diff-medium">Medium</span></td><td>Cumulative diff tracker</td></tr>
      <tr><td>4</td><td><a href="https://leetcode.com/problems/jump-game/">55. Jump Game</a></td><td><span class="diff-medium">Medium</span></td><td>Track maxReach</td></tr>
      <tr><td>5</td><td><a href="https://leetcode.com/problems/jump-game-ii/">45. Jump Game II</a></td><td><span class="diff-medium">Medium</span></td><td>Expand jump frontier ranges</td></tr>
      <tr><td>6</td><td><a href="https://leetcode.com/problems/non-overlapping-intervals/">435. Non-overlapping Intervals</a></td><td><span class="diff-medium">Medium</span></td><td>Sort by End time</td></tr>
      <tr><td>7</td><td><a href="https://leetcode.com/problems/partition-labels/">763. Partition Labels</a></td><td><span class="diff-medium">Medium</span></td><td>Last occ map bound</td></tr>
      <tr><td>8</td><td><a href="https://leetcode.com/problems/candy/">135. Candy</a></td><td><span class="diff-hard">Hard</span></td><td>Two-pass greedy slopes</td></tr>
    </tbody>
  </table>
</div>
</div>

<div class="ch-nav-footer">
  <a href="/learning/dsa/heaps/ch6-heaps/" class="ch-nav-btn prev">← Prev: Ch6 Heaps</a>
  <a href="/learning/dsa/dsa-roadmap/" class="ch-nav-btn next">Next: Ch8 Binary Search (Locked)<i class="fas fa-lock" style="margin-left: 8px;"></i></a>
</div>

</div>
