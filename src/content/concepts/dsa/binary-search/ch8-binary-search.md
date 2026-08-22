---
title: "Binary Search - DSA Mastery"
description: "← Back to Roadmap Ch8 Intermediate Binary Search Classic Search • Rotated Array • Answer Space • Lower/Upper Bound 11 Sections 2 Solved Problems Section 1 — What Is Binary Search?"
domain: dsa
track: dsa-mastery
order: 8
chrome: bare
ownHeader: true
url: /learning/dsa/binary-search/ch8-binary-search/
---

<link rel="stylesheet" href="/assets/css/dsa-chapter.css">

<!-- ==============================================
     HERO SECTION
=============================================== -->
<div class="chapter-hero">
  <div class="ch-hero-content">
    <div class="back-link">
      <a href="/learning/dsa/dsa-roadmap/">← Back to Roadmap</a>
    </div>
    <div class="ch-badge-row">
      <span class="ch-badge-item">Ch8</span>
      <span class="ch-badge-item">Intermediate</span>
    </div>
    <h1 class="ch-title">Binary Search</h1>
    <p class="ch-subtitle">Classic Search • Rotated Array • Answer Space • Lower/Upper Bound</p>
    
    <div class="ch-hero-stats">
      <div class="stat-box">
        <span class="stat-val">11</span>
        <span class="stat-label">Sections</span>
      </div>
      <div class="stat-box">
        <span class="stat-val">2</span>
        <span class="stat-label">Solved Problems</span>
      </div>
    </div>
  </div>
</div>

<!-- ==============================================
     MAIN CONTENT
=============================================== -->
<div class="chapter-content">

<!-- Section 1 -->
<div class="chapter-section">
<h2 class="section-heading">Section 1 — What Is Binary Search?</h2>
<p>Binary search finds a target in a sorted (or monotone) space by repeatedly halving the search interval. Each comparison eliminates half the remaining candidates, giving <code>O(log n)</code> time — far superior to <code>O(n)</code> linear search for large inputs.</p>

<div class="insight-box">
  <span class="insight-label">The Core Invariant</span>
  <ul>
    <li>At every step, the answer (if it exists) lies within <code>[lo, hi]</code>.</li>
    <li>We compute <code>mid = lo + (hi - lo) / 2</code> (avoids integer overflow vs <code>(lo+hi)/2</code>).</li>
    <li>We then shrink the window: move <code>lo</code> up or <code>hi</code> down based on the comparison at <code>mid</code>.</li>
    <li>The loop terminates when <code>lo &gt; hi</code> (classic) or <code>lo == hi</code> (boundary search).</li>
    <li><strong>Critical:</strong> every iteration MUST reduce the window size. If <code>lo</code> or <code>hi</code> never moves, the loop runs forever.</li>
  </ul>
</div>

<h3 class="section-subheading">1.1 — The Three Binary Search Templates</h3>
<p>Most binary search bugs come from wrong loop condition or wrong boundary update. The following three templates cover 99% of interview problems.</p>

<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// ── TEMPLATE 1: Classic exact search ────────────────────────
// Use when: searching for an exact value in a sorted array.
// Loop exits when lo > hi (element not found).
int bsClassic(vector<int>& a, int target) {
    int lo = 0, hi = (int)a.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if      (a[mid] == target) return mid;   // found
        else if (a[mid] <  target) lo = mid + 1; // target in right half
        else                       hi = mid - 1; // target in left half
    }
    return -1; // not found
}

// ── TEMPLATE 2: Lower bound ──────────────────────────────────
// Use when: find first index where a[i] >= target.
// Loop exits when lo == hi == insertion point.
int lowerBound(vector<int>& a, int target) {
    int lo = 0, hi = (int)a.size(); // hi = n (one past end) is valid
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] < target) lo = mid + 1; // mid is too small, exclude it
        else                 hi = mid;      // mid could be the answer, keep it
    }
    return lo; // first index with a[lo] >= target
}

// ── TEMPLATE 3: Upper bound ──────────────────────────────────
// Use when: find first index where a[i] > target.
int upperBound(vector<int>& a, int target) {
    int lo = 0, hi = (int)a.size();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] <= target) lo = mid + 1; // mid is not strictly greater
        else                  hi = mid;
    }
    return lo; // first index with a[lo] > target
}
// C++ equivalents: lower_bound(a.begin(),a.end(),t) and upper_bound(...)
{% endhighlight %}
</div>

<h3 class="section-subheading">1.2 — Template Comparison</h3>
<div class="ch-ed-problems">
  <table>
    <thead>
      <tr><th>Template</th><th>Loop Condition</th><th><code>hi</code> initialised to</th><th><code>lo/hi</code> Update</th><th>Returns</th></tr>
    </thead>
    <tbody>
      <tr><td>Classic exact</td><td><code>lo &lt;= hi</code></td><td><code>n - 1</code></td><td><code>lo=mid+1</code> or <code>hi=mid-1</code></td><td>Index or <code>-1</code></td></tr>
      <tr><td>Lower bound</td><td><code>lo &lt; hi</code></td><td><code>n</code></td><td><code>lo=mid+1</code> or <code>hi=mid</code></td><td>First idx &gt;= target</td></tr>
      <tr><td>Upper bound</td><td><code>lo &lt; hi</code></td><td><code>n</code></td><td><code>lo=mid+1</code> or <code>hi=mid</code></td><td>First idx &gt; target</td></tr>
      <tr><td>Answer space</td><td><code>lo &lt; hi</code> or <code>&lt;=</code></td><td>problem max</td><td>depends on feasibility</td><td>Optimal value</td></tr>
    </tbody>
  </table>
</div>
</div>

<!-- Section 2 -->
<div class="chapter-section">
<h2 class="section-heading">Section 2 — Visual Diagrams: Binary Search in Action</h2>

<h3 class="section-subheading">Diagram 1 — Classic Binary Search</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">Trace</span>
{% highlight text %}
Classic Binary Search: Target = 7
  Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]   target = 7
  Index:  0  1  2  3  4   5   6   7   8   9

  Iteration 1: lo=0, hi=9, mid=4, a[mid]=9
    9 > 7  =>  search left half.  hi = mid-1 = 3.
  [1, 3, 5, 7] [9, 11, 13, 15, 17, 19]
   lo=0      hi=3

  Iteration 2: lo=0, hi=3, mid=1, a[mid]=3
    3 < 7  =>  search right half.  lo = mid+1 = 2.
  [1, 3] [5, 7]
          lo=2 hi=3

  Iteration 3: lo=2, hi=3, mid=2, a[mid]=5
    5 < 7  =>  lo = mid+1 = 3.
         [7]
          lo=3=hi=3

  Iteration 4: lo=3, hi=3, mid=3, a[mid]=7
    7 == 7  =>  FOUND at index 3.

  Total comparisons: 4 = ceil(log2(10)).  Without binary search: up to 10.
{% endhighlight %}
</div>

<h3 class="section-subheading">Diagram 2 — Lower Bound (First Occurrence)</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">Trace</span>
{% highlight text %}
Lower Bound and Upper Bound Trace
  Array: [1, 3, 3, 3, 5, 7, 9]   target = 3
  Index:  0  1  2  3  4  5  6
  Goal: find FIRST index where a[i] >= 3  (first occurrence of 3)

  lo=0, hi=7 (n=7, one past end)

  Iteration 1: mid=3, a[3]=3
    3 >= target=3  =>  hi = mid = 3.  (keep mid as candidate)
  lo=0, hi=3

  Iteration 2: mid=1, a[1]=3
    3 >= 3  =>  hi = 1.
  lo=0, hi=1

  Iteration 3: mid=0, a[0]=1
    1 < 3  =>  lo = mid+1 = 1.
  lo=1, hi=1  =>  loop exits (lo == hi).

  Return lo = 1.  a[1] = 3 = first occurrence.  Correct!

  Upper bound (first index > 3): returns 4.
  So all occurrences of 3 are in indices [1, 4) = {1, 2, 3}.
  Count of 3s = upperBound - lowerBound = 4 - 1 = 3.  Correct!
{% endhighlight %}
</div>

<h3 class="section-subheading">Diagram 3 — Binary Search on Answer Space</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">Trace</span>
{% highlight text %}
Binary Search on Answer Space: Koko Bananas
  Problem: Koko eats bananas. Piles = [3, 6, 7, 11]. H = 8 hours.
  Find minimum eating speed k such that Koko finishes all piles in H hours.

  Key insight: 'Can Koko finish at speed k?' is monotone.
  If YES at speed k, then YES at speed k+1, k+2, ... (faster is always feasible).
  If NO  at speed k, then NO  at speed k-1, k-2, ... (slower is never feasible).
  => Binary search on k!

  Search space: lo=1 (min possible speed), hi=11 (max pile = always works).

  mid=6: hours = ceil(3/6)+ceil(6/6)+ceil(7/6)+ceil(11/6) = 1+1+2+2 = 6 <= 8. YES
  hi = 6.

  mid=3: hours = ceil(3/3)+ceil(6/3)+ceil(7/3)+ceil(11/3) = 1+2+3+4 = 10 > 8. NO
  lo = 4.

  mid=5: hours = ceil(3/5)+ceil(6/5)+ceil(7/5)+ceil(11/5) = 1+2+2+3 = 8 <= 8. YES
  hi = 5.

  mid=4: hours = ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) = 1+2+2+3 = 8 <= 8. YES
  hi = 4.

  lo=4 == hi=4  =>  return 4.
  Answer: minimum speed = 4.  Correct!
{% endhighlight %}
</div>

<h3 class="section-subheading">Diagram 4 — Rotated Sorted Array</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">Trace</span>
{% highlight text %}
Rotated Array: Which Half Is Sorted?
  Original sorted: [1, 2, 3, 4, 5, 6, 7]
  Rotated at index 3: [4, 5, 6, 7, 1, 2, 3]
  Index:               0  1  2  3  4  5  6

  Key property: at least ONE half is always normally sorted.
  Check: if a[lo] <= a[mid]  =>  left half [lo..mid] is sorted.
         else                =>  right half [mid..hi] is sorted.

  Search for target = 1:
  lo=0, hi=6, mid=3, a[mid]=7.
    a[lo]=4 <= a[mid]=7  =>  LEFT half [0..3] = [4,5,6,7] is sorted.
    Is target 1 in [4, 7]?  1 < 4  =>  NO.  Search right: lo = 4.

  lo=4, hi=6, mid=5, a[mid]=2.
    a[lo]=1 <= a[mid]=2  =>  LEFT half [4..5] = [1,2] is sorted.
    Is target 1 in [1, 2]?  1 >= 1 and 1 <= 2  =>  YES.  Search left: hi = 5.

  lo=4, hi=5, mid=4, a[mid]=1.
    a[mid] == target  =>  FOUND at index 4.
{% endhighlight %}
</div>
</div>

<!-- Section 3 -->
<div class="chapter-section">
<h2 class="section-heading">Section 3 — Real-World Use Cases</h2>
<div class="ch-ed-problems">
  <table>
    <thead>
      <tr><th>Application</th><th>System</th><th>How Binary Search Is Used</th></tr>
    </thead>
    <tbody>
      <tr><td>Dictionary / index lookup</td><td>Database B-Tree index</td><td>Search sorted key space in O(log n) I/O pages</td></tr>
      <tr><td>Version control bisect</td><td><code>git bisect</code></td><td>Binary search through commit history to find first bad commit</td></tr>
      <tr><td>IP routing</td><td>Network router lookup</td><td>Longest prefix match via binary search on sorted prefix table</td></tr>
      <tr><td>Load balancing</td><td>Consistent hashing ring</td><td>Binary search for the next server on the sorted hash ring</td></tr>
      <tr><td>Media streaming</td><td>Video player seek</td><td>Binary search on sorted timestamp index for O(log n) seek</td></tr>
      <tr><td>Spell checker</td><td>Sorted dictionary file</td><td>Binary search for word existence / nearest match</td></tr>
      <tr><td>Compression</td><td>Arithmetic / range coding</td><td>Binary search on cumulative frequency table</td></tr>
      <tr><td>Scheduling</td><td>Rate limiter / throttle</td><td>Binary search on sorted event timestamps for window queries</td></tr>
      <tr><td>Machine learning</td><td>Hyperparameter tuning</td><td>Binary / ternary search on unimodal loss curve</td></tr>
      <tr><td>Scientific computing</td><td>Root finding</td><td>Bisection method: binary search for f(x)=0 in continuous domain</td></tr>
    </tbody>
  </table>
</div>
</div>

<!-- Section 4 -->
<div class="chapter-section">
<h2 class="section-heading">Section 4 — Core Concepts & Algorithms</h2>

<h3 class="section-subheading">4.1 — Search in Rotated Sorted Array</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Rotated Sorted Array Search — O(log n)
// LeetCode 33 — Search in Rotated Sorted Array
// Time: O(log n)  Space: O(1)
// Key: at mid, exactly one half is normally sorted. Use that to guide search.
int search(vector<int>& a, int target) {
    int lo = 0, hi = (int)a.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] == target) return mid;

        // Determine which half is sorted
        if (a[lo] <= a[mid]) {           // left half [lo..mid] is sorted
            if (a[lo] <= target && target < a[mid])
                hi = mid - 1;            // target is in sorted left half
            else
                lo = mid + 1;            // target must be in right half
        } else {                         // right half [mid..hi] is sorted
            if (a[mid] < target && target <= a[hi])
                lo = mid + 1;            // target is in sorted right half
            else
                hi = mid - 1;            // target must be in left half
        }
    }
    return -1;
}
{% endhighlight %}
</div>

<h3 class="section-subheading">4.2 — Find Minimum in Rotated Sorted Array</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Find Minimum in Rotated Array — O(log n)
// LeetCode 153 — Find Minimum in Rotated Sorted Array
// Time: O(log n)  Space: O(1)
// The minimum is always in the UNSORTED (rotated) half.
int findMin(vector<int>& a) {
    int lo = 0, hi = (int)a.size() - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] > a[hi])
            lo = mid + 1;  // min is in right half (right is unsorted)
        else
            hi = mid;      // min is in left half or at mid
    }
    return a[lo]; // lo == hi == index of minimum
}
// Why compare with a[hi] not a[lo]?
// Comparing mid to hi tells us if the right side is 'out of order' (rotated).
// If a[mid] > a[hi]: right half wraps around, minimum is in [mid+1, hi].
// If a[mid] <= a[hi]: right half is sorted normally, minimum is in [lo, mid].
{% endhighlight %}
</div>

<h3 class="section-subheading">4.3 — Binary Search on Answer Space</h3>
<p>Many optimisation problems can be solved by binary searching on the answer value directly. The key insight: define a feasibility function <code>f(x)</code> that returns true/false. If <code>f</code> is monotone (all true for x &gt;= answer, all false below), binary search finds the boundary.</p>

<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Binary Search on Answer Space — O(n log(max_val))
// Generic answer-space binary search template
// Find minimum x such that feasible(x) is true.
int answerSpaceBS(int lo, int hi) {
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (feasible(mid))
            hi = mid;      // mid works, try smaller
        else
            lo = mid + 1;  // mid does not work, must go larger
    }
    return lo; // minimum feasible value
}

// Koko Eating Bananas (LC 875)
// feasible(k): can Koko eat all piles at speed k in H hours?
bool feasible(vector<int>& piles, int k, int H) {
    long long hours = 0;
    for (int p : piles) hours += (p + k - 1) / k; // ceil(p/k)
    return hours <= H;
}
int minEatingSpeed(vector<int>& piles, int h) {
    int lo = 1, hi = *max_element(piles.begin(), piles.end());
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (feasible(piles, mid, h)) hi = mid;
        else                         lo = mid + 1;
    }
    return lo;
}
{% endhighlight %}
</div>

<h3 class="section-subheading">4.4 — Counting Occurrences with Lower/Upper Bound</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Lower/Upper Bound Applications
// Count occurrences of target in sorted array
// Time: O(log n)  Space: O(1)
int countOccurrences(vector<int>& a, int target) {
    // lower_bound: first index with a[i] >= target
    int lo = (int)(lower_bound(a.begin(), a.end(), target) - a.begin());
    // upper_bound: first index with a[i] > target
    int hi = (int)(upper_bound(a.begin(), a.end(), target) - a.begin());
    return hi - lo; // number of elements equal to target
}

// First and last position of target (LC 34)
vector<int> searchRange(vector<int>& a, int target) {
    int first = (int)(lower_bound(a.begin(),a.end(),target) - a.begin());
    if (first == (int)a.size() || a[first] != target) return {-1,-1};
    int last  = (int)(upper_bound(a.begin(),a.end(),target) - a.begin()) - 1;
    return {first, last};
}
{% endhighlight %}
</div>

<h3 class="section-subheading">4.5 — Binary Search on 2D Matrix</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Binary Search on 2D Matrix — O(log(mn)) and O(m+n)
// LeetCode 74 — Search a 2D Matrix
// Matrix: rows sorted, last element of row < first element of next row.
// => Treat as a flattened 1D sorted array of m*n elements.
// Time: O(log(m*n))  Space: O(1)
bool searchMatrix(vector<vector<int>>& mat, int target) {
    int m = mat.size(), n = mat[0].size();
    int lo = 0, hi = m * n - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int val = mat[mid / n][mid % n];  // convert 1D index to 2D
        if      (val == target) return true;
        else if (val <  target) lo = mid + 1;
        else                   hi = mid - 1;
    }
    return false;
}

// LeetCode 240 — Search a 2D Matrix II
// Each row sorted, each column sorted (but rows don't connect).
// Use staircase search from top-right corner: O(m+n)
bool searchMatrixII(vector<vector<int>>& mat, int target) {
    int r = 0, c = (int)mat[0].size() - 1;  // start top-right
    while (r < (int)mat.size() && c >= 0) {
        if      (mat[r][c] == target) return true;
        else if (mat[r][c] >  target) c--;  // too big: move left
        else                          r++;  // too small: move down
    }
    return false;
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
      <tr><th>If the problem asks...</th><th>Binary Search Variant</th><th>Key Setup</th></tr>
    </thead>
    <tbody>
      <tr><td>Find exact value in sorted array</td><td>Classic (Template 1)</td><td><code>lo=0, hi=n-1, lo&lt;=hi</code></td></tr>
      <tr><td>First position of target (or &gt;= target)</td><td>Lower bound (Template 2)</td><td><code>lo=0, hi=n, lo&lt;hi</code></td></tr>
      <tr><td>Last position of target</td><td>Upper bound - 1</td><td><code>upperBound(target) - 1</code></td></tr>
      <tr><td>Count occurrences of target</td><td><code>upperBound - lowerBound</code></td><td>Both in <code>O(log n)</code></td></tr>
      <tr><td>Search in rotated sorted array</td><td>Rotated BS</td><td>Identify sorted half at each step</td></tr>
      <tr><td>Find minimum in rotated array</td><td>Compare <code>mid</code> to <code>hi</code></td><td>Minimum is in unsorted half</td></tr>
      <tr><td>Minimum feasible value (Koko, capacity)</td><td>Answer space BS</td><td>Binary search on answer, check feasibility</td></tr>
      <tr><td>Maximum feasible value</td><td>Answer space BS (reversed)</td><td>Flip condition: search for last true</td></tr>
      <tr><td>Peak element in array</td><td>Binary search on slope</td><td>Move toward the higher neighbour</td></tr>
      <tr><td>Square root / power search</td><td>Answer space BS</td><td><code>lo=1, hi=target, check mid*mid</code></td></tr>
      <tr><td>Search in 2D matrix (rows+cols connected)</td><td>Flatten to 1D</td><td><code>index (r,c) = (mid/n, mid%n)</code></td></tr>
      <tr><td>Search in 2D matrix (rows+cols sorted)</td><td>Staircase from top-right</td><td><code>O(m+n)</code>, not binary search</td></tr>
    </tbody>
  </table>
</div>

<div class="insight-box">
  <span class="insight-label">🔍 How to Identify an Answer-Space Binary Search Problem</span>
  <ul>
    <li><strong>SIGNAL 1:</strong> The problem asks for a minimum or maximum VALUE satisfying some condition.</li>
    <li><strong>SIGNAL 2:</strong> You can define a yes/no feasibility function <code>f(x)</code> that is monotone (all NO below threshold, all YES above).</li>
    <li><strong>SIGNAL 3:</strong> Keywords: 'minimise the maximum', 'maximum minimum', 'smallest k such that', 'allocate optimally'.</li>
    <li><strong>SETUP:</strong> <code>lo</code> = smallest possible answer, <code>hi</code> = largest possible answer (often max element or sum).</li>
    <li><strong>DIRECTION:</strong> minimise answer -&gt; on feasible, go left (<code>hi=mid</code>). Maximise answer -&gt; on feasible, go right (<code>lo=mid</code>).</li>
    <li><strong>EXAMPLES:</strong> Koko Bananas, Capacity to Ship Packages, Split Array Largest Sum, Magnetic Force Between Balls.</li>
  </ul>
</div>

<div class="insight-box">
  <span class="insight-label">🛡️ The Off-By-One Survival Guide</span>
  <ul>
    <li>Use <code>lo + (hi - lo) / 2</code> always — never <code>(lo + hi) / 2</code>. Avoids integer overflow.</li>
    <li>Classic search (exact): <code>lo &lt;= hi</code>, update <code>lo=mid+1</code> or <code>hi=mid-1</code>.</li>
    <li>Boundary search (lower/upper bound): <code>lo &lt; hi</code>, update <code>lo=mid+1</code> or <code>hi=mid</code> (NOT <code>mid-1</code>!).</li>
    <li><code>hi = n</code> (not <code>n-1</code>) for lower/upper bound — allows returning <code>n</code> (insert at end).</li>
    <li>Never set <code>hi = mid - 1</code> in a lower-bound template — you will skip the answer.</li>
    <li>After the loop: <code>lo == hi</code> == the answer index. No need to check both.</li>
  </ul>
</div>
</div>

<!-- Section 6 -->
<div class="chapter-section">
<h2 class="section-heading">Section 6 — Complete C++ Implementations</h2>

<h3 class="section-subheading">6.1 — Capacity to Ship Packages (Answer Space BS)</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Capacity to Ship — O(n log sum)
// LeetCode 1011 — Capacity to Ship Packages Within D Days
// Find minimum ship capacity to deliver all packages within D days.
// Time: O(n log(sum))  Space: O(1)
class Solution {
    bool canShip(vector<int>& weights, int cap, int days) {
        int d = 1, load = 0;
        for (int w : weights) {
            if (load + w > cap) { d++; load = 0; } // start new day
            load += w;
        }
        return d <= days;
    }
public:
    int shipWithinDays(vector<int>& weights, int days) {
        // lo: must hold heaviest package; hi: ship all at once
        int lo = *max_element(weights.begin(), weights.end());
        int hi = accumulate(weights.begin(), weights.end(), 0);
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (canShip(weights, mid, days)) hi = mid;
            else                             lo = mid + 1;
        }
        return lo;
    }
};
{% endhighlight %}
</div>

<h3 class="section-subheading">6.2 — Find Peak Element</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Find Peak Element — O(log n)
// LeetCode 162 — Find Peak Element
// A peak is an element strictly greater than its neighbours.
// Time: O(log n)  Space: O(1)
// Key insight: always move toward the higher neighbour.
// A peak must exist in that direction (by the rising slope argument).
int findPeakElement(vector<int>& a) {
    int lo = 0, hi = (int)a.size() - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] < a[mid+1])
            lo = mid + 1;  // slope going up: peak is to the right
        else
            hi = mid;      // slope going down: peak is at mid or left
    }
    return lo; // lo == hi == index of a peak
}
{% endhighlight %}
</div>

<h3 class="section-subheading">6.3 — Split Array Largest Sum</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
// Split Array Largest Sum — O(n log sum)
// LeetCode 410 — Split Array Largest Sum
// Split nums into k non-empty subarrays to minimise the largest subarray sum.
// Time: O(n log(sum))  Space: O(1)
class Solution {
    bool canSplit(vector<int>& nums, int k, int limit) {
        int parts = 1, curr = 0;
        for (int x : nums) {
            if (curr + x > limit) { parts++; curr = 0; }
            curr += x;
        }
        return parts <= k;
    }
public:
    int splitArray(vector<int>& nums, int k) {
        int lo = *max_element(nums.begin(), nums.end());
        int hi = accumulate(nums.begin(), nums.end(), 0);
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (canSplit(nums, k, mid)) hi = mid;
            else                        lo = mid + 1;
        }
        return lo;
    }
};
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
      <tr><td>Classic binary search (exact)</td><td><code>O(log n)</code></td><td><code>O(1)</code></td></tr>
      <tr><td>Lower bound / upper bound</td><td><code>O(log n)</code></td><td><code>O(1)</code></td></tr>
      <tr><td>First and last position of target</td><td><code>O(log n)</code></td><td><code>O(1)</code></td></tr>
      <tr><td>Search in rotated sorted array</td><td><code>O(log n)</code></td><td><code>O(1)</code></td></tr>
      <tr><td>Find minimum in rotated array</td><td><code>O(log n)</code></td><td><code>O(1)</code></td></tr>
      <tr><td>Find peak element</td><td><code>O(log n)</code></td><td><code>O(1)</code></td></tr>
      <tr><td>Koko bananas / eating speed</td><td><code>O(n log M)</code>  M = max pile</td><td><code>O(1)</code></td></tr>
      <tr><td>Capacity to ship (D days)</td><td><code>O(n log S)</code>  S = sum</td><td><code>O(1)</code></td></tr>
      <tr><td>Split array largest sum</td><td><code>O(n log S)</code>  S = sum</td><td><code>O(1)</code></td></tr>
      <tr><td>Search in 2D matrix (LC 74)</td><td><code>O(log(m*n))</code></td><td><code>O(1)</code></td></tr>
      <tr><td>Search in 2D matrix II (LC 240)</td><td><code>O(m + n)</code></td><td><code>O(1)</code></td></tr>
      <tr><td>Count occurrences (lower+upper)</td><td><code>O(log n)</code></td><td><code>O(1)</code></td></tr>
      <tr><td>Square root integer</td><td><code>O(log n)</code></td><td><code>O(1)</code></td></tr>
    </tbody>
  </table>
</div>

<div class="insight-box">
  <span class="insight-label">Why is Binary Search O(log n)?</span>
  <ul>
    <li>Each iteration halves the search window: <code>n -&gt; n/2 -&gt; n/4 -&gt; ... -&gt; 1</code>.</li>
    <li>After <code>k</code> iterations, window size = <code>n / 2^k</code>. Loop ends when <code>n / 2^k = 1</code>, so <code>k = log2(n)</code>.</li>
    <li>For <code>n = 10^9</code>: <code>log2(10^9) ~ 30</code> iterations. Linear search would need up to <code>10^9</code>.</li>
    <li>Answer-space binary search: <code>O(log(hi-lo))</code> iterations * <code>O(feasibility check)</code> per iteration.</li>
    <li>If feasibility check is <code>O(n)</code>, total is <code>O(n log(hi-lo))</code>. For Koko: <code>O(n log(max_pile))</code>.</li>
  </ul>
</div>
</div>

<!-- Section 8 -->
<div class="chapter-section">
<h2 class="section-heading">Section 8 — Solved Problem 1: Search in Rotated Sorted Array</h2>

<div class="insight-box">
<span class="insight-label">1. Observations & Core Idea</span>
<p>Given an integer array nums sorted in ascending order that has been rotated at an unknown pivot, and a target value, return the index of target or -1 if not present. Must run in O(log n).</p>
<ul>
    <li>A rotated sorted array like <code>[4,5,6,7,0,1,2]</code> is NOT globally sorted, so naive binary search fails.</li>
    <li><strong>Key insight:</strong> Even after rotation, at least one of the two halves <code>[lo..mid]</code> or <code>[mid..hi]</code> is ALWAYS sorted normally. We can determine which by comparing <code>a[lo]</code> with <code>a[mid]</code>.</li>
    <li>If <code>a[lo] &lt;= a[mid]</code>: the left half <code>[lo..mid]</code> is sorted. Check if target falls within <code>[a[lo], a[mid])</code>. If yes, search left; otherwise search right.</li>
    <li>If <code>a[lo] &gt; a[mid]</code>: the right half <code>[mid..hi]</code> is sorted. Check if target falls within <code>(a[mid], a[hi]]</code>. If yes, search right; otherwise search left.</li>
</ul>
</div>

<h3 class="section-subheading">2. Approach Comparison</h3>
<div class="ch-ed-problems">
  <table>
    <thead>
      <tr><th>Approach</th><th>Time</th><th>Space</th><th>Method</th></tr>
    </thead>
    <tbody>
      <tr><td>Linear Scan</td><td>O(n)</td><td>O(1)</td><td>Check every element until found.</td></tr>
      <tr><td>Rotated Binary Search</td><td>O(log n)</td><td>O(1)</td><td>Identify sorted half, eliminate half array per step.</td></tr>
    </tbody>
  </table>
</div>

<h3 class="section-subheading">3. Optimised Solution</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int lo = 0, hi = (int)nums.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;

            if (nums[lo] <= nums[mid]) {
                // Left half [lo..mid] is sorted
                if (nums[lo] <= target && target < nums[mid])
                    hi = mid - 1;   // target in sorted left half
                else
                    lo = mid + 1;   // target in right half
            } else {
                // Right half [mid..hi] is sorted
                if (nums[mid] < target && target <= nums[hi])
                    lo = mid + 1;   // target in sorted right half
                else
                    hi = mid - 1;   // target in left half
            }
        }
        return -1;
    }
};
{% endhighlight %}
</div>

<h3 class="section-subheading">4. Follow-Up Questions</h3>
<ul>
  <li><strong>Q: What if the array has duplicates (LC 81)?</strong> When <code>a[lo] == a[mid]</code>, we cannot determine which half is sorted. Increment <code>lo</code> (<code>lo++</code>) to skip the duplicate and continue. Worst case degrades to O(n).</li>
  <li><strong>Q: Find the pivot index?</strong> Binary search for the minimum element (LC 153). The pivot is the index of the minimum.</li>
  <li><strong>Q: Why use <code>a[lo] &lt;= a[mid]</code> instead of <code>&lt;</code>?</strong> When <code>lo == mid</code> (two-element window), <code>a[lo] == a[mid]</code> and the left half of size 1 is trivially sorted. The <code>&lt;=</code> safely handles this.</li>
</ul>
</div>

<!-- Section 9 -->
<div class="chapter-section">
<h2 class="section-heading">Section 9 — Solved Problem 2: Koko Eating Bananas</h2>

<div class="insight-box">
<span class="insight-label">1. Observations & Core Idea</span>
<p>Koko has piles of bananas. She eats at speed k (k bananas per hour). Each hour she picks one pile and eats min(pile, k) bananas. Find the minimum k so she can eat all bananas in at most h hours.</p>
<ul>
    <li>For a given speed <code>k</code>, hours needed = sum of <code>ceil(pile[i] / k)</code> over all piles.</li>
    <li><strong>Monotone property:</strong> If speed <code>k</code> is feasible, then any speed <code>k' &gt; k</code> is also feasible. This enables binary search on <code>k</code>.</li>
    <li>Search space: <code>lo = 1</code>, <code>hi = max(piles)</code>.</li>
    <li>Binary search finds the minimum <code>k</code> where <code>feasible(k)</code> is true. This is the lower-bound template on the answer space.</li>
</ul>
</div>

<h3 class="section-subheading">2. Approach Comparison</h3>
<div class="ch-ed-problems">
  <table>
    <thead>
      <tr><th>Approach</th><th>Time</th><th>Space</th><th>Method</th></tr>
    </thead>
    <tbody>
      <tr><td>Brute Force (Linear Scan)</td><td>O(n * M)</td><td>O(1)</td><td>Try every speed from 1 to M (max pile).</td></tr>
      <tr><td>Binary Search on Answer</td><td>O(n log M)</td><td>O(1)</td><td>Binary search <code>lo</code> to <code>hi</code> boundary.</td></tr>
    </tbody>
  </table>
</div>

<h3 class="section-subheading">3. Optimised Solution</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">C++</span>
{% highlight cpp %}
class Solution {
    // Can Koko finish all piles at speed k within h hours?
    bool feasible(vector<int>& piles, long long k, int h) {
        long long hours = 0;
        for (int p : piles)
            hours += (p + k - 1) / k; // ceil(p / k)
        return hours <= h;
    }
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int lo = 1;
        int hi = *max_element(piles.begin(), piles.end());
        // Binary search: find minimum k where feasible(k) is true
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (feasible(piles, mid, h))
                hi = mid;      // mid works, try smaller
            else
                lo = mid + 1;  // mid too slow, need faster
        }
        return lo; // lo == hi == minimum feasible speed
    }
};
{% endhighlight %}
</div>

<h3 class="section-subheading">4. Follow-Up Questions</h3>
<ul>
  <li><strong>Q: Capacity to Ship Packages (LC 1011)?</strong> Identical structure. <code>feasible(cap)</code>: simulate loading, increment day. <code>lo = max weight</code>, <code>hi = sum of weights</code>.</li>
  <li><strong>Q: Split Array Largest Sum (LC 410)?</strong> Same template. <code>lo = max element</code>, <code>hi = total sum</code>.</li>
  <li><strong>Q: Why <code>ceil(p/k) = (p + k - 1) / k</code>?</strong> In integer math for positive integers <code>a</code> and <code>b</code>, <code>ceil(a/b) = (a + b - 1) / b</code>. Verify: <code>ceil(7/3) = (7+2)/3 = 9/3 = 3</code>.</li>
</ul>
</div>

<!-- Section 10 -->
<div class="chapter-section">
<h2 class="section-heading">Section 10 — Common Mistakes & Edge Cases</h2>

<h3 class="section-subheading">10.1 — Classic Off-By-One Errors</h3>
<ul>
  <li><strong>MISTAKE: Using (lo + hi) / 2</strong>. When lo and hi are both large, lo + hi overflows a 32-bit integer. Always use <code>lo + (hi - lo) / 2</code>.</li>
  <li><strong>MISTAKE: Using hi = mid - 1 in a lower-bound template</strong>. If mid is the answer, this skips it. Lower-bound must use <code>hi = mid</code>.</li>
  <li><strong>MISTAKE: Using lo &lt;= hi in a lower-bound search</strong>. This can loop forever when lo == hi. Lower-bound uses <code>lo &lt; hi</code>.</li>
  <li><strong>MISTAKE: Initialising hi = n - 1 for lower/upper bound</strong>. The answer can be n (insert at end). Always initialise <code>hi = n</code>.</li>
</ul>

<h3 class="section-subheading">10.2 — Rotated Array & Answer Space Mistakes</h3>
<ul>
  <li><strong>MISTAKE: strict less in rotated array search</strong>: using <code>a[lo] &lt; a[mid]</code> instead of <code>&lt;=</code>. Fails on a two-element window.</li>
  <li><strong>MISTAKE: integer overflow in feasibility check</strong>. Use <code>long long</code> for accumulated sums or counts (like hours needed for Koko).</li>
  <li><strong>MISTAKE: confusing minimise vs maximise answer space</strong>. Draw the YES/NO monotone map. If you want the first YES (minimise), use <code>hi = mid</code> on YES. If you want the last YES (maximise), use <code>lo = mid</code> on YES.</li>
</ul>

<div class="insight-box">
<span class="insight-label">Warning</span>
<p><strong>Edge Cases to Consider:</strong></p>
<ul>
    <li>Single-element array: <code>lo==hi==mid</code>. Classic search works.</li>
    <li>All elements equal (e.g. <code>[3,3,3]</code>): <code>lower_bound</code> returns 0, <code>upper_bound</code> returns n.</li>
    <li>Target larger than all elements: <code>lower_bound</code> and <code>upper_bound</code> both return n.</li>
</ul>
</div>
</div>

<!-- Section 11 -->
<div class="chapter-section">
<h2 class="section-heading">Section 11 — Common Interview Questions</h2>
<p>Recommended progression for Binary Search:</p>
<div class="ch-ed-problems">
  <table>
    <thead>
      <tr><th>#</th><th>Problem</th><th>Difficulty</th><th>Key Concept</th></tr>
    </thead>
    <tbody>
      <tr><td>1</td><td><a href="https://leetcode.com/problems/binary-search/">704. Binary Search</a></td><td><span class="diff-easy">Easy</span></td><td>Template 1, exact search</td></tr>
      <tr><td>2</td><td><a href="https://leetcode.com/problems/search-insert-position/">35. Search Insert Position</a></td><td><span class="diff-easy">Easy</span></td><td>Lower bound, return lo</td></tr>
      <tr><td>3</td><td><a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/">34. Find First and Last Position</a></td><td><span class="diff-medium">Medium</span></td><td>Lower + upper bound</td></tr>
      <tr><td>4</td><td><a href="https://leetcode.com/problems/search-in-rotated-sorted-array/">33. Search in Rotated Sorted Array</a></td><td><span class="diff-medium">Medium</span></td><td>Identify sorted half</td></tr>
      <tr><td>5</td><td><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/">153. Find Minimum in Rotated Sorted Array</a></td><td><span class="diff-medium">Medium</span></td><td>Compare mid to hi</td></tr>
      <tr><td>6</td><td><a href="https://leetcode.com/problems/search-a-2d-matrix/">74. Search a 2D Matrix</a></td><td><span class="diff-medium">Medium</span></td><td>Flatten to 1D binary search</td></tr>
      <tr><td>7</td><td><a href="https://leetcode.com/problems/koko-eating-bananas/">875. Koko Eating Bananas</a></td><td><span class="diff-medium">Medium</span></td><td>Answer space: minimise</td></tr>
      <tr><td>8</td><td><a href="https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/">1011. Capacity to Ship Packages</a></td><td><span class="diff-medium">Medium</span></td><td>Answer space: min capacity</td></tr>
    </tbody>
  </table>
</div>
</div>

<div class="chapter-nav-footer">
  <a href="/learning/dsa/greedy/ch7-greedy/" class="ch-nav-footer-btn">← Prev: Ch7 Greedy</a>
  <a href="/learning/dsa/backtracking/ch9-backtracking/" class="ch-nav-footer-btn primary">Next: Ch9 Backtracking →</a>
</div>

</div>
