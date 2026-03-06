---
layout: default
title: Ch10 Dynamic Programming
permalink: /learning/dsa/dynamic-programming/ch10-dynamic-programming/
custom_css: dsa-chapter
---

<!-- ========================================== -->
<!-- HERO SECTION                               -->
<!-- ========================================== -->
<div class="chapter-hero" style="--bg-gradient: linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%); --theme-color: #0d9488;">
  <div class="ch-hero-content">
    <div class="breadcrumb">
      <a href="{{ '/learning/dsa/dsa-roadmap/' | relative_url }}">DSA Roadmap</a> <span class="separator">›</span> 
      <span class="current">Chapter 10</span>
    </div>
    <h1>Dynamic Programming</h1>
    <p class="ch-subtitle">1D DP | 2D DP | Knapsack | LCS | Intervals | State Machines</p>
    <div class="hero-stats">
      <span class="stat-badge"><span class="icon">📘</span> 12 Sections</span>
      <span class="stat-badge"><span class="icon">🧩</span> 2 Solved Problems</span>
      <span class="stat-badge diff-advanced">Advanced Difficulty</span>
      <span class="stat-badge prereq">Prerequisite: Ch9</span>
    </div>
  </div>
</div>

<!-- ========================================== -->
<!-- LAYOUT WRAPPER                             -->
<!-- ========================================== -->
<div class="chapter-content">

    <!-- SECTION 1 -->
    <section id="section-1" class="chapter-section">
      <h2> 1 — What Is Dynamic Programming?</h2>
      <p><strong>Dynamic Programming (DP)</strong> solves problems by breaking them into overlapping subproblems and storing the results of each subproblem to avoid redundant computation. It is applicable when a problem has <strong>optimal substructure</strong> (an optimal solution is built from optimal sub-solutions) and <strong>overlapping subproblems</strong> (the same subproblem is solved multiple times in naive recursion).</p>
      
      <div class="insight-box">
        <h4>Two Implementation Styles</h4>
        <ul>
          <li><strong>TOP-DOWN (Memoisation):</strong> Write a recursive solution, add a memo table to cache results. Natural translation from the recurrence relation. Call the function with the original problem size.</li>
          <li><strong>BOTTOM-UP (Tabulation):</strong> Fill a DP table iteratively, starting from the smallest subproblems. Usually more space-efficient and avoids recursion stack overhead. Preferred in production code.</li>
          <li>Both styles have the same asymptotic complexity. Top-down is often easier to derive; bottom-up is often easier to space-optimise.</li>
          <li><strong>Space optimisation:</strong> many DP problems only need the previous row/value, allowing O(n²) space to reduce to O(n) or O(1).</li>
        </ul>
      </div>

      <h3>1.1 — The Four-Step DP Framework</h3>
      <ol>
        <li><strong>STEP 1 — DEFINE THE STATE:</strong> What does <code>dp[i]</code> (or <code>dp[i][j]</code>) represent? Be precise. Write it in plain English first.</li>
        <li><strong>STEP 2 — WRITE THE RECURRENCE:</strong> How does <code>dp[i]</code> relate to smaller subproblems <code>dp[i-1], dp[i-2], ...</code>? This is the heart of the solution.</li>
        <li><strong>STEP 3 — IDENTIFY BASE CASES:</strong> What are the smallest subproblems with known answers? Fill these first to avoid out-of-bounds access.</li>
        <li><strong>STEP 4 — DETERMINE FILL ORDER:</strong> Which order guarantees that when computing <code>dp[i]</code>, all required <code>dp[j &lt; i]</code> are already filled? (Usually left-to-right for 1D, top-left to bottom-right for 2D.)</li>
      </ol>

      <h3>1.2 — DP vs Greedy vs Backtracking</h3>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>Dimension</th>
              <th>Backtracking</th>
              <th>Greedy</th>
              <th>Dynamic Programming</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Core idea</strong></td>
              <td>Explore all paths, prune invalid</td>
              <td>One locally optimal choice per step</td>
              <td>Store & reuse overlapping subproblem results</td>
            </tr>
            <tr>
              <td><strong>Correctness requirement</strong></td>
              <td>No requirement — explores all</td>
              <td>Greedy choice property + optimal substructure</td>
              <td>Optimal substructure alone</td>
            </tr>
            <tr>
              <td><strong>Output</strong></td>
              <td>All solutions (or one)</td>
              <td>One optimal value</td>
              <td>One optimal value (or count)</td>
            </tr>
            <tr>
              <td><strong>Complexity</strong></td>
              <td>Exponential (pruned)</td>
              <td>O(n) or O(n log n)</td>
              <td>Polynomial: O(n²), O(n*W), etc.</td>
            </tr>
            <tr>
              <td><strong>When to use</strong></td>
              <td>Constraint satisfaction, enumeration</td>
              <td>Interval scheduling, greedy exchange</td>
              <td>Sequence, knapsack, string, path problems</td>
            </tr>
            <tr>
              <td><strong>Space</strong></td>
              <td>O(depth)</td>
              <td>O(1) or O(n)</td>
              <td>O(n) to O(n²)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 2 -->
    <section id="section-2" class="chapter-section">
      <h2> 2 — Visual Diagrams: DP in Action</h2>

      <h3>Diagram 1 — Fibonacci: Naive vs Memoised</h3>
      <div class="ch-code-wrap">
<pre><code>Fibonacci: Why Memoisation Eliminates Redundancy
  fib(5) — NAIVE RECURSION (no memoisation):
                    fib(5)
                  /       \
              fib(4)       fib(3)
             /     \       /    \
          fib(3) fib(2) fib(2) fib(1)
          /   \
       fib(2) fib(1)

  fib(2) computed 3 times, fib(3) computed 2 times -> exponential O(2^n).

  fib(5) — WITH MEMOISATION:
  memo = {}
  fib(5) -> fib(4) -> fib(3) -> fib(2) -> fib(1) = 1, fib(0) = 0
  fib(2) = 1 -> stored in memo[2]
  fib(3) = fib(2)+fib(1) = 2 -> stored in memo[3]
  fib(4) = fib(3)+fib(2) = 3 -> stored in memo[4]  <- fib(2) read from memo
  fib(3) already in memo -> return memo[3] = 2
  fib(5) = fib(4)+fib(3) = 5

  Each subproblem solved ONCE. Total: O(n) time, O(n) space.</code></pre>
      </div>

      <h3>Diagram 2 — Coin Change DP Table</h3>
      <div class="ch-code-wrap">
<pre><code>Coin Change: Full DP Table Trace
  coins = [1, 5, 6, 9]   amount = 11
  dp[i] = minimum coins to make amount i.  dp[0] = 0, rest = INF initially.

  i=0:  dp[0] = 0
  i=1:  try coin 1: dp[1-1]+1 = dp[0]+1 = 1.  dp[1] = 1
  i=2:  try coin 1: dp[1]+1 = 2.  dp[2] = 2
  i=3:  try coin 1: dp[2]+1 = 3.  dp[3] = 3
  i=4:  try coin 1: dp[3]+1 = 4.  dp[4] = 4
  i=5:  try coin 1: dp[4]+1 = 5.
        try coin 5: dp[0]+1 = 1.  dp[5] = 1   <- coin 5 wins
  i=6:  try coin 1: dp[5]+1 = 2.
        try coin 5: dp[1]+1 = 2.
        try coin 6: dp[0]+1 = 1.  dp[6] = 1   <- coin 6 wins
  i=7:  try coin 1: dp[6]+1 = 2.
        try coin 5: dp[2]+1 = 3.
        try coin 6: dp[1]+1 = 2.  dp[7] = 2
  i=8:  coin 1: dp[7]+1=3. coin 5: dp[3]+1=4. coin 6: dp[2]+1=3. dp[8]=3
  i=9:  coin 1: dp[8]+1=4. coin 5: dp[4]+1=5. coin 6: dp[3]+1=4.
        coin 9: dp[0]+1=1.  dp[9] = 1   <- coin 9 wins
  i=10: coin 1: dp[9]+1=2. coin 5: dp[5]+1=2. coin 6: dp[4]+1=5.
        coin 9: dp[1]+1=2.  dp[10] = 2
  i=11: coin 1: dp[10]+1=3. coin 5: dp[6]+1=2. coin 6: dp[5]+1=2.
        coin 9: dp[2]+1=3.  dp[11] = 2

  Answer: dp[11] = 2  (coins 5+6 or coins 2+9).  Correct!</code></pre>
      </div>

      <h3>Diagram 3 — LCS DP Table</h3>
      <div class="ch-code-wrap">
<pre><code>LCS: DP Table Fill and Traceback
  s1 = 'ABCDE'   s2 = 'ACE'
  dp[i][j] = LCS length of s1[0..i-1] and s2[0..j-1]

       ''  A  C  E
    ''  0  0  0  0
    A   0  1  1  1
    B   0  1  1  1
    C   0  1  2  2
    D   0  1  2  2
    E   0  1  2  3   <- answer: dp[5][3] = 3

  Recurrence:
  if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1] + 1  (extend LCS)
  else:                  dp[i][j] = max(dp[i-1][j], dp[i][j-1])

  Trace the LCS: start at dp[5][3]=3.
  E==E (match): go diagonal to dp[4][2]=2. Track 'E'.
  D!=C:  max(dp[3][2], dp[4][1]) = max(2,1) -> came from dp[3][2].
  C==C (match): go diagonal to dp[2][1]=1. Track 'C'.
  B!=A:  max(dp[1][1], dp[2][0]) = max(1,0) -> came from dp[1][1].
  A==A (match): go diagonal to dp[0][0]=0. Track 'A'.
  LCS = 'ACE' (reversed tracking).  Length 3.  Correct!</code></pre>
      </div>

      <h3>Diagram 4 — 0/1 Knapsack DP Table</h3>
      <div class="ch-code-wrap">
<pre><code>0/1 Knapsack: DP Table Fill
  items = [(w=2,v=6), (w=3,v=10), (w=4,v=12)]   capacity W = 5
  dp[i][w] = max value using first i items with capacity w.

        w: 0   1   2   3   4   5
  i=0    : 0   0   0   0   0   0
  i=1(2,6) : 0   0   6   6   6   6
  i=2(3,10): 0   0   6  10  10  16  <- 16 = v1+v2 = 6+10
  i=3(4,12): 0   0   6  10  12  16

  Answer: dp[3][5] = 16.  Items selected: (w=2,v=6) + (w=3,v=10).

  Recurrence:
  if items[i-1].w > w: dp[i][w] = dp[i-1][w]                      // can't include
  else: dp[i][w] = max(dp[i-1][w],                                // exclude
                       dp[i-1][w - items[i-1].w] + items[i-1].v)  // include</code></pre>
      </div>
    </section>

    <!-- SECTION 3 -->
    <section id="section-3" class="chapter-section">
      <h2> 3 — Real-World Use Cases</h2>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>DP Problem Pattern</th>
              <th>Real-World Application</th>
              <th>System</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Shortest / Longest Path</td>
              <td>Route optimisation, cheapest flight</td>
              <td>Google Maps, airline booking systems</td>
            </tr>
            <tr>
              <td>Edit Distance (LCS/LIS)</td>
              <td>Diff algorithms, DNA alignment</td>
              <td>git diff, bioinformatics BLAST</td>
            </tr>
            <tr>
              <td>Knapsack / Packing</td>
              <td>Budget allocation, resource scheduling</td>
              <td>Cloud cost optimisation, ad budget planning</td>
            </tr>
            <tr>
              <td>Sequence alignment</td>
              <td>Spell correction, plagiarism detection</td>
              <td>Autocorrect, Turnitin, Grammarly</td>
            </tr>
            <tr>
              <td>Interval DP</td>
              <td>Matrix chain multiplication, expression parsing</td>
              <td>Compilers, query optimisers</td>
            </tr>
            <tr>
              <td>Bitmask DP</td>
              <td>Travelling Salesman, assignment problems</td>
              <td>Logistics routing, hardware scheduling</td>
            </tr>
            <tr>
              <td>Stock trading DP</td>
              <td>Portfolio rebalancing with constraints</td>
              <td>Algorithmic trading systems</td>
            </tr>
            <tr>
              <td>Text segmentation</td>
              <td>Word wrap, code formatter line breaking</td>
              <td>LaTeX typesetting, VS Code formatter</td>
            </tr>
            <tr>
              <td>Probability DP</td>
              <td>Dice game probabilities, HMM decoding</td>
              <td>Speech recognition, Monte Carlo pricing</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 4 -->
    <section id="section-4" class="chapter-section">
      <h2> 4 — Core Concepts: DP Patterns</h2>

      <h3>4.1 — 1D DP: Climbing Stairs / Fibonacci</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// Climbing Stairs (LC 70) — number of ways to reach step n
// dp[i] = ways to reach step i = dp[i-1] + dp[i-2]
// Time: O(n)  Space: O(1) after optimisation
int climbStairs(int n) {
    if (n <= 2) return n;
    int prev2 = 1, prev1 = 2;
    for (int i = 3; i <= n; i++) {
        int curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}
// Space optimised: only keep the last two values (rolling variables).
// General pattern: whenever dp[i] depends only on dp[i-1] and dp[i-2],
// you can reduce O(n) space to O(1).
{% endhighlight %}
</div>

      <h3>4.2 — 1D DP: Coin Change</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 322 — Coin Change
// Minimum number of coins to make amount. Unlimited supply per denomination.
// Time: O(amount * n)  Space: O(amount)
int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount+1, amount+1); // INF = amount+1 (impossible sentinel)
    dp[0] = 0;                          // base case: 0 coins for amount 0
    for (int i = 1; i <= amount; i++) {
        for (int c : coins) {
            if (c <= i)
                dp[i] = min(dp[i], dp[i-c] + 1);
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}
// Why amount+1 as INF? Any valid answer is <= amount (using all 1-coins).
// If dp[amount] > amount after filling, no solution exists.
{% endhighlight %}
</div>

      <h3>4.3 — 1D DP: Longest Increasing Subsequence (LIS)</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 300 — Longest Increasing Subsequence
// Time: O(n^2)  Space: O(n)   [O(n log n) with patience sorting]
int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n, 1);  // dp[i] = LIS ending at index i
    int best = 1;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i])           // nums[i] extends LIS at j
                dp[i] = max(dp[i], dp[j]+1);
        }
        best = max(best, dp[i]);
    }
    return best;
}

// O(n log n) version using binary search + patience sorting
int lengthOfLIS_nlogn(vector<int>& nums) {
    vector<int> tails; // tails[i] = smallest tail of all IS of length i+1
    for (int x : nums) {
        auto it = lower_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) tails.push_back(x);  // extend
        else                  *it = x;              // replace
    }
    return (int)tails.size();
}
{% endhighlight %}
</div>

      <h3>4.4 — 2D DP: Longest Common Subsequence</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 1143 — Longest Common Subsequence
// Time: O(m*n)  Space: O(m*n) -> O(n) with rolling array
int longestCommonSubsequence(string s1, string s2) {
    int m = s1.size(), n = s2.size();
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i-1] == s2[j-1])
                dp[i][j] = dp[i-1][j-1] + 1;      // chars match: extend
            else
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]); // skip one char
        }
    }
    return dp[m][n];
}

// Space-optimised: O(n) using two rolling rows
int lcs_space(string s1, string s2) {
    int m = s1.size(), n = s2.size();
    vector<int> prev(n+1,0), curr(n+1,0);
    for (int i=1;i<=m;i++) {
        for (int j=1;j<=n;j++)
            curr[j] = s1[i-1]==s2[j-1] ? prev[j-1]+1 : max(prev[j],curr[j-1]);
        swap(prev, curr);
        fill(curr.begin(), curr.end(), 0);
    }
    return prev[n];
}
{% endhighlight %}
</div>

      <h3>4.5 — 0/1 Knapsack</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// 0/1 Knapsack: each item used at most once
// Time: O(n*W)  Space: O(W) with 1D optimisation
int knapsack(vector<int>& w, vector<int>& v, int W) {
    int n = w.size();
    vector<int> dp(W+1, 0);
    for (int i = 0; i < n; i++) {
        // CRITICAL: iterate W down to w[i] to prevent using item i twice
        for (int cap = W; cap >= w[i]; cap--) {
            dp[cap] = max(dp[cap], dp[cap - w[i]] + v[i]);
        }
    }
    return dp[W];
}
// Why iterate capacity in REVERSE for 0/1 knapsack?
// When filling dp[cap], we need dp[cap-w[i]] from the PREVIOUS item iteration.
// Iterating forward would update dp[cap-w[i]] first, allowing item i to be
// used multiple times. Reverse iteration preserves the 'at most once' constraint.

// Unbounded Knapsack (items reusable): iterate capacity FORWARD
int unboundedKnapsack(vector<int>& w, vector<int>& v, int W) {
    vector<int> dp(W+1, 0);
    for (int cap = 1; cap <= W; cap++)
        for (int i = 0; i < (int)w.size(); i++)
            if (w[i] <= cap)
                dp[cap] = max(dp[cap], dp[cap - w[i]] + v[i]);
    return dp[W];
}
{% endhighlight %}
</div>

      <h3>4.6 — State Machine DP: Stock Problems</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// Best Time to Buy and Sell Stock with Cooldown (LC 309)
// States: held (holding stock), sold (just sold), rest (cooldown done)
// Time: O(n)  Space: O(1)
int maxProfit(vector<int>& prices) {
    int held = INT_MIN, sold = 0, rest = 0;
    for (int p : prices) {
        int prevHeld = held, prevSold = sold, prevRest = rest;
        held = max(prevHeld, prevRest - p);  // hold: keep or buy from rest
        sold = prevHeld + p;                  // sell: was holding, now sell
        rest = max(prevRest, prevSold);       // rest: keep resting or cooldown
    }
    return max(sold, rest); // can't end holding stock
}
// State transition diagram:
// rest -> held (buy)    held -> sold (sell)    sold -> rest (cooldown)
// rest -> rest (wait)   held -> held (hold)
{% endhighlight %}
</div>

      <h3>4.7 — Interval DP: Burst Balloons</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 312 — Burst Balloons
// dp[l][r] = max coins from bursting all balloons between l and r (exclusive)
// Key: think of k as the LAST balloon to burst in [l,r], not the first.
// Time: O(n^3)  Space: O(n^2)
int maxCoins(vector<int>& nums) {
    int n = nums.size();
    // Pad with sentinel 1s at both ends
    vector<int> a(n+2);
    a[0] = a[n+1] = 1;
    for (int i=0;i<n;i++) a[i+1] = nums[i];
    n += 2;
    vector<vector<int>> dp(n, vector<int>(n, 0));
    // len = length of open interval (l,r)
    for (int len = 2; len < n; len++) {
        for (int l = 0; l < n-len; l++) {
            int r = l + len;
            for (int k = l+1; k < r; k++) { // k is last burst in (l,r)
                dp[l][r] = max(dp[l][r],
                    dp[l][k] + a[l]*a[k]*a[r] + dp[k][r]);
            }
        }
    }
    return dp[0][n-1];
}
{% endhighlight %}
</div>
    </section>

    <!-- SECTION 5 -->
    <section id="section-5" class="chapter-section">
      <h2> 5 — Pattern Recognition Guide</h2>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>DP Pattern</th>
              <th>Problem Signals</th>
              <th>State Definition</th>
              <th>Recurrence Shape</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Linear 1D</strong></td>
              <td>Single sequence, previous results matter</td>
              <td><code>dp[i]</code> = answer for prefix i</td>
              <td><code>dp[i] = f(dp[i-1], dp[i-2], ...)</code></td>
            </tr>
            <tr>
              <td><strong>Two-sequence 2D</strong></td>
              <td>Two strings/arrays, alignment/matching</td>
              <td><code>dp[i][j]</code> = answer for s1[0..i], s2[0..j]</td>
              <td><code>dp[i][j] = f(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])</code></td>
            </tr>
            <tr>
              <td><strong>Knapsack</strong></td>
              <td>Items with weight+value, capacity constraint</td>
              <td><code>dp[i][w]</code> = max value with i items, cap w</td>
              <td>include/exclude item i</td>
            </tr>
            <tr>
              <td><strong>Interval</strong></td>
              <td>Optimal over all sub-intervals [i,j]</td>
              <td><code>dp[i][j]</code> = answer for subarray [i,j]</td>
              <td>min/max over all splits k</td>
            </tr>
            <tr>
              <td><strong>State machine</strong></td>
              <td>Finite states with transitions (stocks)</td>
              <td><code>dp[state]</code> = best value in this state</td>
              <td>transitions between states per element</td>
            </tr>
            <tr>
              <td><strong>Counting paths</strong></td>
              <td>Count ways (not optimise)</td>
              <td><code>dp[i]</code> = number of ways to reach i</td>
              <td>sum of <code>dp[j]</code> for valid j</td>
            </tr>
            <tr>
              <td><strong>Digit DP</strong></td>
              <td>Count numbers in range with digit constraints</td>
              <td><code>dp[pos][tight][...]</code> = count</td>
              <td>try each digit, maintain tight constraint</td>
            </tr>
            <tr>
              <td><strong>Bitmask DP</strong></td>
              <td>Small n (~20), subsets of items</td>
              <td><code>dp[mask]</code> = answer for subset mask</td>
              <td><code>dp[mask | (1&lt;&lt;i)] = f(dp[mask])</code></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="insight-box">
        <h4>How to Identify a DP Problem</h4>
        <ul>
          <li><strong>SIGNAL 1:</strong> 'Count the number of ways' or 'Find the minimum/maximum'. These are classic DP outputs.</li>
          <li><strong>SIGNAL 2:</strong> 'Optimal decisions over a sequence' — each decision affects future options.</li>
          <li><strong>SIGNAL 3:</strong> Future choices depend on past choices (state carries forward).</li>
          <li><strong>SIGNAL 4:</strong> Greedy gives wrong answer (try a small counter-example). Backtracking TLEs. DP is the middle ground.</li>
          <li><strong>SIGNAL 5:</strong> The problem has well-defined subproblems that can be expressed as 'solve for i' or 'solve for (i,j)'.</li>
          <li><strong>NOT DP:</strong> problems with no ordering, problems that require enumerating all solutions, or problems solvable in O(n) with greedy.</li>
        </ul>
      </div>

      <div class="insight-box">
        <h4>Space Optimisation Decision Table</h4>
        <ul>
          <li><code>dp[i]</code> depends on <code>dp[i-1]</code> only &#8594; use two variables (O(n) &#8594; O(1)).</li>
          <li><code>dp[i]</code> depends on <code>dp[i-1]</code> and <code>dp[i-2]</code> &#8594; use three rolling variables (O(n) &#8594; O(1)).</li>
          <li><code>dp[i][j]</code> depends on <code>dp[i-1][...]</code> only &#8594; use two 1D arrays (O(n²) &#8594; O(n)).</li>
          <li><code>dp[i][j]</code> depends on <code>dp[i-1][j-1]</code> &#8594; use one 1D array with careful update order.</li>
          <li><strong>0/1 knapsack 2D &#8594; 1D</strong> by iterating capacity in REVERSE (prevents item reuse).</li>
          <li><strong>Unbounded knapsack 2D &#8594; 1D</strong> by iterating capacity FORWARD (allows item reuse).</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 6 -->
    <section id="section-6" class="chapter-section">
      <h2> 6 — Complete C++ Implementations</h2>

      <h3>6.1 — Edit Distance (Levenshtein)</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 72 — Edit Distance
// Min operations (insert, delete, replace) to convert word1 to word2.
// Time: O(m*n)  Space: O(n) rolling array
int minDistance(string s, string t) {
    int m = s.size(), n = t.size();
    vector<int> dp(n+1);
    iota(dp.begin(), dp.end(), 0); // dp[j] = j (delete j chars from t)
    for (int i = 1; i <= m; i++) {
        int prev = dp[0]; // dp[i-1][j-1] before overwrite
        dp[0] = i;        // dp[i][0] = i (delete i chars from s)
        for (int j = 1; j <= n; j++) {
            int temp = dp[j];
            if (s[i-1] == t[j-1])
                dp[j] = prev;           // chars match: no operation
            else
                dp[j] = 1 + min({prev,  // replace
                                 dp[j],  // delete from s
                                 dp[j-1]}); // insert into s
            prev = temp;
        }
    }
    return dp[n];
}
{% endhighlight %}
</div>

      <h3>6.2 — Unique Paths on Grid</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 62 — Unique Paths
// Count paths from top-left to bottom-right moving only right or down.
// Time: O(m*n)  Space: O(n)
int uniquePaths(int m, int n) {
    vector<int> dp(n, 1); // first row: all 1s (only rightward path)
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[j] += dp[j-1]; // paths from top + paths from left
    return dp[n-1];
}
// Mathematical answer: C(m+n-2, m-1) — choose m-1 down moves from m+n-2 total.

// LC 63 — Unique Paths II (with obstacles)
int uniquePathsWithObstacles(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    vector<long long> dp(n, 0);
    dp[0] = grid[0][0] == 0 ? 1 : 0;
    for (int i = 0; i < m; i++) {
        if (grid[i][0] == 1) dp[0] = 0; // obstacle blocks leftmost column
        for (int j = 1; j < n; j++)
            dp[j] = grid[i][j] == 1 ? 0 : dp[j] + dp[j-1];
    }
    return (int)dp[n-1];
}
{% endhighlight %}
</div>

      <h3>6.3 — Word Break</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 139 — Word Break
// Can string s be segmented into words from wordDict?
// Time: O(n^2 * L)  L=avg word length  Space: O(n)
bool wordBreak(string s, vector<string>& wordDict) {
    unordered_set<string> ws(wordDict.begin(), wordDict.end());
    int n = s.size();
    vector<bool> dp(n+1, false);
    dp[0] = true; // empty string always segmentable
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            // If prefix s[0..j-1] is breakable AND s[j..i-1] is a word
            if (dp[j] && ws.count(s.substr(j, i-j))) {
                dp[i] = true;
                break; // found one valid split, no need to check more
            }
        }
    }
    return dp[n];
}
{% endhighlight %}
</div>
    </section>

    <!-- SECTION 7 -->
    <section id="section-7" class="chapter-section">
      <h2> 7 — Complexity Reference</h2>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>Algorithm</th>
              <th>Time</th>
              <th>Space</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Fibonacci / Climbing Stairs</td>
              <td>O(n)</td>
              <td>O(1) rolling</td>
            </tr>
            <tr>
              <td>Coin Change (min coins)</td>
              <td>O(amount * n)</td>
              <td>O(amount)</td>
            </tr>
            <tr>
              <td>Coin Change II (count ways)</td>
              <td>O(amount * n)</td>
              <td>O(amount)</td>
            </tr>
            <tr>
              <td>Longest Increasing Subsequence (O(n²))</td>
              <td>O(n²)</td>
              <td>O(n)</td>
            </tr>
            <tr>
              <td>LIS O(n log n) with patience sort</td>
              <td>O(n log n)</td>
              <td>O(n)</td>
            </tr>
            <tr>
              <td>Longest Common Subsequence</td>
              <td>O(m*n)</td>
              <td>O(n) rolling</td>
            </tr>
            <tr>
              <td>Edit Distance</td>
              <td>O(m*n)</td>
              <td>O(n) rolling</td>
            </tr>
            <tr>
              <td>0/1 Knapsack</td>
              <td>O(n*W)</td>
              <td>O(W) 1D</td>
            </tr>
            <tr>
              <td>Unbounded Knapsack / Coin Change</td>
              <td>O(amount*n)</td>
              <td>O(amount)</td>
            </tr>
            <tr>
              <td>Unique Paths on Grid</td>
              <td>O(m*n)</td>
              <td>O(n)</td>
            </tr>
            <tr>
              <td>Word Break</td>
              <td>O(n² * L)</td>
              <td>O(n)</td>
            </tr>
            <tr>
              <td>Stock with Cooldown / k transactions</td>
              <td>O(n * k)</td>
              <td>O(k)</td>
            </tr>
            <tr>
              <td>Burst Balloons / Interval DP</td>
              <td>O(n³)</td>
              <td>O(n²)</td>
            </tr>
            <tr>
              <td>Bitmask DP (TSP-style)</td>
              <td>O(2^n * n²)</td>
              <td>O(2^n * n)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="insight-box">
        <h4>Pseudo-polynomial vs Polynomial</h4>
        <ul>
          <li>Coin Change and Knapsack run in O(amount * n) or O(n * W). This looks polynomial but is actually pseudo-polynomial.</li>
          <li>Reason: the input size is O(log amount) bits, not O(amount). A truly polynomial algorithm would be O(n * log(amount)).</li>
          <li>In practice: if amount &lt;= 10⁴ or W &lt;= 10⁴, DP is fast enough. If amount ~ 10⁹, DP is infeasible.</li>
          <li>Truly polynomial DP: LCS, LIS, Edit Distance are polynomial in input size n (length of the strings/arrays).</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 8 -->
    <section id="section-8" class="chapter-section">
      <h2> 8 — Solved Problem 1: Coin Change</h2>
      <p>Given an integer array <code>coins</code> and an integer <code>amount</code>, return the fewest number of coins needed to make up <code>amount</code>. If it is impossible, return <code>-1</code>. You may use each coin denomination an unlimited number of times.</p>
      
      <div class="insight-box">
        <h4>OBSERVATIONS</h4>
        <ul>
          <li>Greedy fails here. Example: coins=[1,5,6,9], amount=11. Greedy picks 9+1+1=3 coins. Optimal is 5+6=2 coins.</li>
          <li>Optimal substructure: <code>dp[i] = min coins for amount i = 1 + min(dp[i-c])</code> for each coin c where c &lt;= i.</li>
          <li>Overlapping subproblems: <code>dp[6]</code> is needed when computing <code>dp[7]</code>, <code>dp[8]</code>, <code>dp[9]</code>, <code>dp[11]</code>, ... Memoising <code>dp[6]</code> avoids recomputing it.</li>
          <li>Unlimited coin use = unbounded knapsack variant. Iterate amounts from 1 to target, try each coin.</li>
          <li>Initialise <code>dp[0]=0</code> (base case: 0 coins for amount 0). <code>dp[i] = amount+1</code> as sentinel for 'unreachable'.</li>
        </ul>
      </div>

<div class="ch-code-wrap">
{% highlight cpp %}
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // dp[i] = minimum coins needed to make amount i
        vector<int> dp(amount+1, amount+1); // sentinel: larger than any valid answer
        dp[0] = 0;  // base case

        for (int i = 1; i <= amount; i++) {
            for (int c : coins) {
                if (c <= i)  // coin c can contribute to amount i
                    dp[i] = min(dp[i], dp[i-c] + 1);
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
};
{% endhighlight %}
</div>
      <p><strong>Complexity:</strong> Time O(amount * n), Space O(amount)</p>
    </section>


    <!-- SECTION 9 -->
    <section id="section-9" class="chapter-section">
      <h2> 9 — Solved Problem 2: Longest Common Subsequence</h2>
      <p>Given two strings <code>text1</code> and <code>text2</code>, return the length of their longest common subsequence (LCS). A subsequence is a sequence derived by deleting some characters without changing the relative order of the remaining characters.</p>
      
      <div class="insight-box">
        <h4>OBSERVATIONS</h4>
        <ul>
          <li>A subsequence is NOT a substring — characters don't need to be contiguous.</li>
          <li>State definition: <code>dp[i][j]</code> = length of LCS of <code>text1[0..i-1]</code> and <code>text2[0..j-1]</code>. 1-indexed to simplify base cases.</li>
          <li>Recurrence: If <code>text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1</code> (extend LCS by matching char). Else: <code>dp[i][j] = max(dp[i-1][j], dp[i][j-1])</code> (skip one char from either string).</li>
          <li>Base cases: <code>dp[0][j] = 0</code> (empty text1) and <code>dp[i][0] = 0</code> (empty text2). Automatically initialised by vector constructor.</li>
          <li>Fill order: row by row, left to right. <code>dp[i][j]</code> only depends on <code>dp[i-1][j-1]</code>, <code>dp[i-1][j]</code>, <code>dp[i][j-1]</code> — all already computed.</li>
        </ul>
      </div>

<div class="ch-code-wrap">
{% highlight cpp %}
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.size(), n = text2.size();
        // Space-optimised: use two rows only
        vector<int> prev(n+1, 0), curr(n+1, 0);

        for (int i = 1; i <= m; i++) {
            fill(curr.begin(), curr.end(), 0);
            for (int j = 1; j <= n; j++) {
                if (text1[i-1] == text2[j-1])
                    curr[j] = prev[j-1] + 1;         // chars match
                else
                    curr[j] = max(prev[j], curr[j-1]); // skip one
            }
            swap(prev, curr);
        }
        return prev[n];
    }
};
{% endhighlight %}
</div>
      <p><strong>Complexity:</strong> Time O(m*n), Space O(n)</p>
    </section>

    <!-- SECTION 10 -->
    <section id="section-10" class="chapter-section">
      <h2> 10 — Common Mistakes & Edge Cases</h2>
      
      <h3>10.1 — State Definition Mistakes</h3>
      <ul>
        <li><strong>Imprecise state definition.</strong> <code>dp[i]</code> must have an exact meaning. 'dp[i] = something about index i' is not enough — write 'dp[i] = minimum cost to reach index i from index 0 using exactly i steps'.</li>
        <li><strong>Off-by-one in string/array DP.</strong> When using 1-indexed dp (dp[1..n] for string of length n), always access text[i-1] for the i-th character. Mixing 0-indexed and 1-indexed causes subtle bugs.</li>
        <li><strong>Wrong base case.</strong> For coin change, initialising <code>dp[0] = 0</code> is critical. For LCS, the entire <code>dp[0][j]</code> and <code>dp[i][0]</code> row/column must be 0. For path counting, <code>dp[0][0] = 1</code>.</li>
        <li><strong>Missing the 'impossible' sentinel.</strong> For coin change, initialise to amount+1 (not INT_MAX — adding 1 to INT_MAX overflows). For paths, -1 or 0 are natural sentinels.</li>
      </ul>

      <h3>10.2 — Knapsack Direction Mistakes</h3>
      <ul>
        <li><strong>0/1 knapsack — iterating capacity forward in the 1D optimisation.</strong> This allows the same item to be used multiple times (becomes unbounded knapsack). Always iterate capacity in REVERSE for 0/1 knapsack.</li>
        <li><strong>Coin Change II (combinations) — iterating loops in wrong order.</strong> Iterating coins in inner loop and amounts in outer counts permutations (e.g. [1,2] and [2,1] counted separately). Swap the loops: outer = coins, inner = amounts.</li>
        <li><strong>Confusing 'at most W' capacity with 'exactly W'.</strong> For knapsack, <code>dp[W]</code> gives the answer for capacity AT MOST W. For 'exactly W' problems, initialise with -infinity except <code>dp[0]=0</code>.</li>
      </ul>

      <h3>10.3 — Edge Cases</h3>
      <ul>
        <li><strong>Empty string LCS:</strong> if either string is empty, LCS = 0. Base cases <code>dp[0][j]=dp[i][0]=0</code> handle this.</li>
        <li><strong>No valid coin combination:</strong> return -1, not 0. Check if <code>dp[amount] &gt; amount</code> after filling.</li>
        <li><strong><code>amount = 0</code> for coin change:</strong> always return 0 (zero coins needed). <code>dp[0] = 0</code> handles this.</li>
        <li><strong>Identical strings for LCS:</strong> LCS = the string itself. <code>dp[n][n] = n</code>.</li>
        <li><strong>All-negative array for max subarray:</strong> Kadane returns the single maximum element (not 0). Initialise both currSum and maxSum to nums[0].</li>
      </ul>
    </section>

    <!-- SECTION 11 -->
    <section id="section-11" class="chapter-section">
      <h2> 11 — Common Interview Questions</h2>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>Problem</th>
              <th>Key Implementation Detail</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Climbing Stairs (LC 70)</td>
              <td>Fibonacci pattern, O(1) space</td>
            </tr>
            <tr>
              <td>House Robber (LC 198)</td>
              <td><code>dp[i] = max(dp[i-1], dp[i-2]+nums[i])</code></td>
            </tr>
            <tr>
              <td>Coin Change (LC 322)</td>
              <td>Unbounded knapsack, <code>dp[i] = min(dp[i-c]+1)</code></td>
            </tr>
            <tr>
              <td>Coin Change II (LC 518)</td>
              <td>count combinations, outer=coins inner=amounts</td>
            </tr>
            <tr>
              <td>Longest Increasing Subsequence (LC 300)</td>
              <td>O(n²) DP or O(n log n) patience sort</td>
            </tr>
            <tr>
              <td>Word Break (LC 139)</td>
              <td><code>dp[i]</code> = any <code>dp[j] &amp;&amp; s[j..i] in dict</code></td>
            </tr>
            <tr>
              <td>Longest Common Subsequence (LC 1143)</td>
              <td>Classic 2D DP, O(n) space opt</td>
            </tr>
            <tr>
              <td>Edit Distance (LC 72)</td>
              <td>3-way recurrence: insert/delete/replace</td>
            </tr>
            <tr>
              <td>Unique Paths (LC 62)</td>
              <td>Grid path counting, O(n) space</td>
            </tr>
            <tr>
              <td>Partition Equal Subset Sum (LC 416)</td>
              <td>0/1 knapsack with target = sum/2</td>
            </tr>
            <tr>
              <td>Best Time to Buy Stock with Cooldown (LC 309)</td>
              <td>State machine DP</td>
            </tr>
            <tr>
              <td>Burst Balloons (LC 312)</td>
              <td>Interval DP, think last burst not first</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="insight-box">
        <h4>Chapter 10 — Key Takeaways</h4>
        <ul>
          <li><strong>DP requires BOTH</strong> optimal substructure (optimal solution built from optimal sub-solutions) AND overlapping subproblems.</li>
          <li><strong>Four steps:</strong> define state precisely, write recurrence, identify base cases, determine fill order.</li>
          <li><strong>Top-down vs Bottom-up:</strong> Top-down = recursion + memo cache. Bottom-up = iterative table. Same complexity; bottom-up avoids stack overhead.</li>
          <li><strong>1D DP space opt:</strong> rolling variables when <code>dp[i]</code> depends on <code>dp[i-1]</code> and <code>dp[i-2]</code> only.</li>
          <li><strong>2D DP space opt:</strong> two 1D arrays (prev/curr) when <code>dp[i][j]</code> depends only on row i-1.</li>
          <li><strong>0/1 knapsack 1D:</strong> iterate capacity in <strong>REVERSE</strong> to prevent item reuse.</li>
          <li><strong>Unbounded knapsack / Coin Change:</strong> iterate capacity <strong>FORWARD</strong> to allow item reuse.</li>
          <li><strong>Coin Change:</strong> outer=amounts, inner=coins. <strong>Coin Change II:</strong> outer=coins, inner=amounts.</li>
          <li><strong>LCS recurrence:</strong> match &#8594; diagonal+1. Mismatch &#8594; max(up, left).</li>
        </ul>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- CHAPTER NAVIGATION                         -->
    <!-- ========================================== -->
    <div class="chapter-nav-footer">
      <a href="{{ '/learning/dsa/backtracking/ch9-backtracking/' | relative_url }}" class="ch-nav-footer-btn">← Prev: Ch9 Backtracking</a>
      <a href="{{ '/learning/dsa/intervals/ch11-bonus-topics/' | relative_url }}" class="ch-nav-footer-btn">Next: Ch11 Bonus Topics →</a>
    </div>

</div>
