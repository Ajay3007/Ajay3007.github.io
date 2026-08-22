---
title: "Ch12 Interview Cheat Sheet"
description: "DSA Roadmap › Chapter 12 Interview Cheat Sheet Complete Reference Pattern Selector Complexity Tables C++ STL Top 50 Problems 📚 12 Chapters Covered 🏆 50+ Top Problems 📊 All…"
domain: dsa
track: dsa-mastery
order: 12
url: /learning/dsa/ch12-cheat-sheet/
---

<!-- ========================================== -->
<!-- HERO SECTION                               -->
<!-- ========================================== -->
<div class="chapter-hero" style="--bg-gradient: linear-gradient(135deg, #f0f9ff 0%, #bae6fd 100%); --theme-color: #0284c7;">
  <div class="ch-hero-content">
    <div class="breadcrumb">
      <a href="/learning/dsa/dsa-roadmap/">DSA Roadmap</a> <span class="separator">›</span>
      <span class="current">Chapter 12</span>
    </div>
    <h1>Interview Cheat Sheet</h1>
    <p class="ch-subtitle">Complete Reference | Pattern Selector | Complexity Tables | C++ STL | Top 50 Problems</p>
    <div class="hero-stats">
      <span class="stat-badge"><span class="icon">📚</span> 12 Chapters Covered</span>
      <span class="stat-badge"><span class="icon">🏆</span> 50+ Top Problems</span>
      <span class="stat-badge"><span class="icon">📊</span> All Complexity Tables</span>
      <span class="stat-badge diff-hard">FAANG Target Level</span>
    </div>
  </div>
</div>

<!-- ========================================== -->
<!-- LAYOUT WRAPPER                             -->
<!-- ========================================== -->
<div class="chapter-content">

    <!-- SECTION 1: PATTERN SELECTOR -->
    <section id="pattern-selector" class="chapter-section">
      <h2>🗺 Section 1 — Pattern Selector: Which Algorithm to Use?</h2>
      <p>Read the problem, identify the signals, select the pattern. This table covers the decision process for ~90% of LeetCode-style problems.</p>

      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>If the problem involves…</th>
              <th>Primary Pattern</th>
              <th>Secondary / Fallback</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Sorted array + find/count target</td><td><strong>Binary Search</strong></td><td>Two Pointers</td></tr>
            <tr><td>Optimal contiguous subarray/substring</td><td><strong>Sliding Window</strong></td><td>Two Pointers</td></tr>
            <tr><td>Pairs/triplets summing to target</td><td><strong>Two Pointers</strong> (sorted)</td><td>Hash Map (unsorted)</td></tr>
            <tr><td>Next greater/smaller in array</td><td><strong>Monotonic Stack</strong></td><td>—</td></tr>
            <tr><td>Histogram / rectangle area</td><td><strong>Monotonic Stack</strong></td><td>Divide &amp; Conquer</td></tr>
            <tr><td>Prefix queries / autocomplete</td><td><strong>Trie</strong></td><td>Hash Set</td></tr>
            <tr><td>Dynamic connectivity / cycle detection</td><td><strong>Union-Find</strong></td><td>BFS/DFS</td></tr>
            <tr><td>Shortest path (unweighted)</td><td><strong>BFS</strong></td><td>—</td></tr>
            <tr><td>Shortest path (weighted, non-neg)</td><td><strong>Dijkstra</strong> (BFS + Min-Heap)</td><td>—</td></tr>
            <tr><td>Shortest path (negative edges)</td><td><strong>Bellman-Ford</strong></td><td>—</td></tr>
            <tr><td>Minimum Spanning Tree</td><td><strong>Kruskal (Union-Find) or Prim</strong></td><td>—</td></tr>
            <tr><td>Topological order / dependency</td><td><strong>Kahn's BFS or DFS post-order</strong></td><td>—</td></tr>
            <tr><td>All subsets / combinations / paths</td><td><strong>Backtracking</strong></td><td>—</td></tr>
            <tr><td>Minimum / maximum over sequence</td><td><strong>Dynamic Programming</strong></td><td>Greedy (if exchange arg holds)</td></tr>
            <tr><td>Count ways / number of paths</td><td><strong>DP (counting)</strong></td><td>—</td></tr>
            <tr><td>String alignment / edit operations</td><td><strong>2D DP</strong> (LCS / Edit Distance)</td><td>—</td></tr>
            <tr><td>Pack items into capacity</td><td><strong>0/1 or Unbounded Knapsack DP</strong></td><td>—</td></tr>
            <tr><td>Interval scheduling (max non-overlap)</td><td><strong>Greedy</strong> (earliest finish)</td><td>—</td></tr>
            <tr><td>Merge / insert intervals</td><td><strong>Sort + linear scan</strong></td><td>—</td></tr>
            <tr><td>Kth largest / smallest element</td><td><strong>Min-Heap of size k</strong></td><td>QuickSelect O(n) avg</td></tr>
            <tr><td>Running median</td><td><strong>Two Heaps</strong> (max-heap + min-heap)</td><td>—</td></tr>
            <tr><td>Merge k sorted lists/arrays</td><td><strong>Min-Heap of k heads</strong></td><td>—</td></tr>
            <tr><td>Level-order tree traversal</td><td><strong>BFS</strong></td><td>—</td></tr>
            <tr><td>In/pre/post-order traversal</td><td><strong>DFS</strong> (recursive or iterative)</td><td>—</td></tr>
            <tr><td>LCA in binary tree</td><td><strong>DFS post-order</strong></td><td>Binary lifting for repeated queries</td></tr>
            <tr><td>Detect cycle in graph</td><td><strong>Union-Find or DFS</strong> with colour</td><td>—</td></tr>
            <tr><td>Anagram / frequency matching</td><td><strong>Sliding Window + freq array</strong></td><td>Hash Map</td></tr>
            <tr><td>Palindrome check / construction</td><td><strong>Two Pointers or DP</strong></td><td>—</td></tr>
            <tr><td>Calculator / expression parsing</td><td><strong>Stack</strong></td><td>Recursive descent</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 2: COMPLEXITY REFERENCE -->
    <section id="complexity" class="chapter-section">
      <h2>📊 Section 2 — Master Complexity Reference</h2>

      <h3>2.1 — Data Structures</h3>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr><th>Structure</th><th>Access</th><th>Search</th><th>Insert</th><th>Delete</th><th>Space</th></tr>
          </thead>
          <tbody>
            <tr><td>Array</td><td>O(1)</td><td>O(n)</td><td>O(n)</td><td>O(n)</td><td>O(n)</td></tr>
            <tr><td>Linked List</td><td>O(n)</td><td>O(n)</td><td>O(1) head</td><td>O(1) given ptr</td><td>O(n)</td></tr>
            <tr><td>Stack / Queue</td><td>O(n)</td><td>O(n)</td><td>O(1)</td><td>O(1)</td><td>O(n)</td></tr>
            <tr><td>Hash Map / Set</td><td>O(1) avg</td><td>O(1) avg</td><td>O(1) avg</td><td>O(1) avg</td><td>O(n)</td></tr>
            <tr><td>Binary Search Tree</td><td>O(log n) avg</td><td>O(log n) avg</td><td>O(log n) avg</td><td>O(log n) avg</td><td>O(n)</td></tr>
            <tr><td>AVL / Red-Black Tree</td><td>O(log n)</td><td>O(log n)</td><td>O(log n)</td><td>O(log n)</td><td>O(n)</td></tr>
            <tr><td>Min/Max Heap</td><td>O(1) peek</td><td>O(n)</td><td>O(log n)</td><td>O(log n)</td><td>O(n)</td></tr>
            <tr><td>Trie</td><td>O(L)</td><td>O(L)</td><td>O(L)</td><td>O(L)</td><td>O(n*L*26)</td></tr>
            <tr><td>Union-Find (DSU)</td><td>—</td><td>O(alpha(n))</td><td>O(alpha(n))</td><td>—</td><td>O(n)</td></tr>
          </tbody>
        </table>
      </div>

      <h3>2.2 — Sorting Algorithms</h3>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr><th>Algorithm</th><th>Best</th><th>Average</th><th>Worst</th><th>Space</th><th>Stable?</th></tr>
          </thead>
          <tbody>
            <tr><td>Bubble Sort</td><td>O(n)</td><td>O(n²)</td><td>O(n²)</td><td>O(1)</td><td>✅ Yes</td></tr>
            <tr><td>Insertion Sort</td><td>O(n)</td><td>O(n²)</td><td>O(n²)</td><td>O(1)</td><td>✅ Yes</td></tr>
            <tr><td>Selection Sort</td><td>O(n²)</td><td>O(n²)</td><td>O(n²)</td><td>O(1)</td><td>❌ No</td></tr>
            <tr><td>Merge Sort</td><td>O(n log n)</td><td>O(n log n)</td><td>O(n log n)</td><td>O(n)</td><td>✅ Yes</td></tr>
            <tr><td>Quick Sort</td><td>O(n log n)</td><td>O(n log n)</td><td>O(n²)</td><td>O(log n)</td><td>❌ No</td></tr>
            <tr><td>Heap Sort</td><td>O(n log n)</td><td>O(n log n)</td><td>O(n log n)</td><td>O(1)</td><td>❌ No</td></tr>
            <tr><td>Counting Sort</td><td>O(n+k)</td><td>O(n+k)</td><td>O(n+k)</td><td>O(k)</td><td>✅ Yes</td></tr>
            <tr><td>Radix Sort</td><td>O(d*(n+k))</td><td>O(d*(n+k))</td><td>O(d*(n+k))</td><td>O(n+k)</td><td>✅ Yes</td></tr>
            <tr><td><strong>Tim Sort (std::sort)</strong></td><td>O(n)</td><td>O(n log n)</td><td>O(n log n)</td><td>O(n)</td><td>✅ Yes</td></tr>
          </tbody>
        </table>
      </div>

      <h3>2.3 — Graph Algorithms</h3>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr><th>Algorithm</th><th>Time</th><th>Space</th><th>Use Case</th></tr>
          </thead>
          <tbody>
            <tr><td>BFS</td><td>O(V+E)</td><td>O(V)</td><td>Shortest path (unweighted), level order</td></tr>
            <tr><td>DFS</td><td>O(V+E)</td><td>O(V)</td><td>Cycle detection, topological sort, connected components</td></tr>
            <tr><td>Dijkstra</td><td>O((V+E) log V)</td><td>O(V)</td><td>Shortest path, non-negative weights</td></tr>
            <tr><td>Bellman-Ford</td><td>O(V*E)</td><td>O(V)</td><td>Shortest path, negative weights, detect neg cycles</td></tr>
            <tr><td>Floyd-Warshall</td><td>O(V³)</td><td>O(V²)</td><td>All-pairs shortest path, dense graph</td></tr>
            <tr><td>Kruskal MST</td><td>O(E log E)</td><td>O(V)</td><td>Minimum spanning tree (sparse graph)</td></tr>
            <tr><td>Prim MST</td><td>O((V+E) log V)</td><td>O(V)</td><td>Minimum spanning tree (dense graph)</td></tr>
            <tr><td>Kahn's (Topo Sort)</td><td>O(V+E)</td><td>O(V)</td><td>Topological order, detect cycle in DAG</td></tr>
            <tr><td>Tarjan SCC</td><td>O(V+E)</td><td>O(V)</td><td>Strongly connected components</td></tr>
          </tbody>
        </table>
      </div>

      <h3>2.4 — Key DSA Algorithms</h3>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr><th>Algorithm</th><th>Time</th><th>Space</th><th>Notes</th></tr>
          </thead>
          <tbody>
            <tr><td>Binary Search</td><td>O(log n)</td><td>O(1)</td><td>Requires sorted / monotone input</td></tr>
            <tr><td>Two Pointers</td><td>O(n)</td><td>O(1)</td><td>Requires sorted or monotone property</td></tr>
            <tr><td>Sliding Window</td><td>O(n)</td><td>O(1) or O(k)</td><td>Optimal contiguous window</td></tr>
            <tr><td>Monotonic Stack</td><td>O(n)</td><td>O(n)</td><td>Each element pushed/popped at most once</td></tr>
            <tr><td>Backtracking (subsets)</td><td>O(2ⁿ * n)</td><td>O(n)</td><td>Exponential, pruning helps constant</td></tr>
            <tr><td>Backtracking (permutations)</td><td>O(n! * n)</td><td>O(n)</td><td>—</td></tr>
            <tr><td>Dynamic Programming 1D</td><td>O(n)–O(n²)</td><td>O(n)</td><td>Depends on recurrence</td></tr>
            <tr><td>Dynamic Programming 2D</td><td>O(m*n)</td><td>O(n) opt</td><td>LCS, Edit Distance, Grid paths</td></tr>
            <tr><td>0/1 Knapsack</td><td>O(n*W)</td><td>O(W)</td><td>Reverse capacity iteration</td></tr>
            <tr><td>LIS O(n log n)</td><td>O(n log n)</td><td>O(n)</td><td>Patience sort with binary search</td></tr>
            <tr><td>Heap: Build</td><td>O(n)</td><td>O(1) in-place</td><td>Floyd's build-heap</td></tr>
            <tr><td>Heap: Extract/Insert</td><td>O(log n)</td><td>O(1)</td><td>Sift-down / sift-up</td></tr>
            <tr><td>Union-Find</td><td>O(alpha(n))</td><td>O(n)</td><td>Path compression + union by rank</td></tr>
            <tr><td>Trie: Insert/Search</td><td>O(L)</td><td>O(L)</td><td>L = length of string</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 3: C++ STL -->
    <section id="cpp-stl" class="chapter-section">
      <h2>⚙️ Section 3 — C++ STL Quick Reference</h2>

      <h3>3.1 — Containers</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// ── vector ──────────────────────────────────────────────────
vector<int> v;
v.push_back(x);      // O(1) amortised
v.pop_back();        // O(1)
v[i];                // O(1) random access
v.size(); v.empty(); v.back(); v.front();
sort(v.begin(), v.end());                // O(n log n)
reverse(v.begin(), v.end());             // O(n)
int idx = lower_bound(v.begin(),v.end(),x) - v.begin(); // O(log n)

// ── stack ────────────────────────────────────────────────────
stack<int> stk;
stk.push(x); stk.pop(); stk.top(); stk.empty();  // all O(1)

// ── queue ────────────────────────────────────────────────────
queue<int> q;
q.push(x); q.pop(); q.front(); q.back(); q.empty();  // all O(1)

// ── deque ────────────────────────────────────────────────────
deque<int> dq;
dq.push_back(x); dq.push_front(x);   // O(1)
dq.pop_back();   dq.pop_front();      // O(1)
dq[i];                                // O(1) random access

// ── priority_queue ──────────────────────────────────────────
priority_queue<int> maxH;              // max at top
priority_queue<int,vector<int>,greater<int>> minH;  // min at top
maxH.push(x); maxH.pop(); maxH.top(); // O(log n) except top

// ── set / multiset ────────────────────────────────────────────
set<int> s;                   // sorted, unique
s.insert(x); s.erase(x); s.count(x); s.find(x);  // O(log n)
s.lower_bound(x); s.upper_bound(x);               // O(log n)

// ── map / unordered_map ───────────────────────────────────────
unordered_map<string,int> um; // O(1) avg
map<string,int> m;            // O(log n), sorted by key
um[key] = val;  um.count(key);  um.find(key);
for (auto& [k,v] : um) { }  // structured binding C++17
{% endhighlight %}
</div>

      <h3>3.2 — Useful Algorithms &amp; Functions</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// ── Numeric utilities ────────────────────────────────────────
#include <numeric>
int sum = accumulate(v.begin(), v.end(), 0);
iota(v.begin(), v.end(), 0);          // fill 0,1,2,...,n-1

// ── Min/Max ──────────────────────────────────────────────────
int mx = *max_element(v.begin(), v.end());
int mn = *min_element(v.begin(), v.end());
int res = __gcd(a, b);                // GCD, O(log min(a,b))
int res = __builtin_popcount(x);      // count set bits

// ── String ───────────────────────────────────────────────────
string s = to_string(42);
int n = stoi("42");
s.substr(start, len);                 // O(len)
s.find(sub);                          // O(n*m) naive

// ── Functional / lambda ──────────────────────────────────────
sort(v.begin(), v.end(), [](int a, int b){ return a > b; }); // descending
function<int(int)> dfs = [&](int node) -> int { return 0; }; // recursive lambda

// ── Bit operations ───────────────────────────────────────────
// x & (x-1)       → clear lowest set bit (power of 2: x&(x-1)==0)
// x | (1 << k)    → set bit k
// x & ~(1 << k)   → clear bit k
// (x >> k) & 1    → check bit k
// x ^ x = 0       → XOR self = 0 (find single number)
{% endhighlight %}
</div>

      <h3>3.3 — Graph BFS/DFS Templates</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// ── BFS from source ──────────────────────────────────────────
vector<int> dist(n, INT_MAX);
queue<int> q;
dist[src] = 0; q.push(src);
while (!q.empty()) {
    int u = q.front(); q.pop();
    for (int v : adj[u]) {
        if (dist[v] == INT_MAX) {
            dist[v] = dist[u] + 1;
            q.push(v);
        }
    }
}

// ── DFS iterative ────────────────────────────────────────────
vector<bool> visited(n, false);
stack<int> stk; stk.push(src);
while (!stk.empty()) {
    int u = stk.top(); stk.pop();
    if (visited[u]) continue;
    visited[u] = true;
    for (int v : adj[u]) if (!visited[v]) stk.push(v);
}

// ── Dijkstra ─────────────────────────────────────────────────
vector<long long> dist(n, LLONG_MAX);
priority_queue<pair<long long,int>,
               vector<pair<long long,int>>,
               greater<>> pq;
dist[src] = 0; pq.push({0, src});
while (!pq.empty()) {
    auto [d, u] = pq.top(); pq.pop();
    if (d > dist[u]) continue;  // skip stale entry
    for (auto [v, w] : adj[u]) {
        if (dist[u] + w < dist[v]) {
            dist[v] = dist[u] + w;
            pq.push({dist[v], v});
        }
    }
}
{% endhighlight %}
</div>
    </section>

    <!-- SECTION 4: INTERVIEW FRAMEWORK -->
    <section id="interview-framework" class="chapter-section">
      <h2>🎯 Section 4 — Interview Problem-Solving Framework</h2>

      <div class="insight-box">
        <h4>Step 1 — UNDERSTAND (2–3 min)</h4>
        <ul>
          <li>Restate the problem in your own words. Confirm your understanding with the interviewer.</li>
          <li>Ask about constraints: array size n, value range, negative numbers, duplicates, sorted?</li>
          <li>Ask about edge cases: empty input, single element, all equal, n=1.</li>
          <li>Clarify output format: return value, modify in-place, 1-indexed or 0-indexed?</li>
          <li>Write 1–2 concrete examples including an edge case.</li>
        </ul>
      </div>

      <div class="insight-box">
        <h4>Step 2 — PLAN (3–5 min)</h4>
        <ul>
          <li>State the brute force first. Say: <em>'The naive solution is O(n²) by…'</em></li>
          <li>Identify the bottleneck: inner loop, repeated work, wrong data structure.</li>
          <li>Map to a known pattern using the pattern selector (Section 1).</li>
          <li>State your approach clearly and the expected complexity before writing code.</li>
        </ul>
      </div>

      <div class="insight-box">
        <h4>Step 3 — CODE (10–15 min)</h4>
        <ul>
          <li>Write clean, readable code. Use meaningful variable names (lo/hi over i/j for pointers).</li>
          <li>Code the happy path first. Add edge case handling at the start.</li>
          <li>Think out loud as you code: <em>'Here I'm updating the window by removing the leftmost element…'</em></li>
          <li>Avoid premature optimisation. Get a working solution, then optimise.</li>
        </ul>
      </div>

      <div class="insight-box">
        <h4>Step 4 — TEST (3–5 min)</h4>
        <ul>
          <li>Trace through your example from Step 1 line by line.</li>
          <li>Test with edge cases: empty array, single element, all same, maximum n.</li>
          <li>For graph problems: test disconnected graph, single node, cycle.</li>
          <li>Announce bugs before fixing: <em>'I see that my loop should be &lt;= not &lt;, let me fix that.'</em></li>
        </ul>
      </div>

      <div class="insight-box">
        <h4>Step 5 — OPTIMISE &amp; DISCUSS (2–3 min)</h4>
        <ul>
          <li>State final time and space complexity, explain why.</li>
          <li>Discuss trade-offs: <em>'We could reduce space from O(n) to O(1) by using rolling variables.'</em></li>
          <li>Mention alternative approaches and proactively discuss follow-up variations.</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 5: COMPLEXITY SIGNALS -->
    <section id="complexity-signals" class="chapter-section">
      <h2>⚡ Section 5 — Complexity Signals from Constraints</h2>
      <p>FAANG interviewers set constraints that hint at the expected time complexity. Use these to validate your approach before coding.</p>

      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr><th>Constraint (n)</th><th>Target Complexity</th><th>Algorithms That Fit</th></tr>
          </thead>
          <tbody>
            <tr><td>n ≤ 10</td><td>O(n!) or O(2ⁿ · n)</td><td>Backtracking (all permutations/subsets), brute force</td></tr>
            <tr><td>n ≤ 20</td><td>O(2ⁿ)</td><td>Bitmask DP, backtracking with heavy pruning</td></tr>
            <tr><td>n ≤ 100</td><td>O(n³)</td><td>Floyd-Warshall, interval DP, 3D DP</td></tr>
            <tr><td>n ≤ 1,000</td><td>O(n²)</td><td>2D DP (LCS, Edit Distance), O(n²) DP, naive graph</td></tr>
            <tr><td>n ≤ 10,000</td><td>O(n² tight) or O(n·√n)</td><td>Acceptable O(n²), Sqrt decomposition</td></tr>
            <tr><td>n ≤ 100,000</td><td><strong>O(n log n)</strong></td><td>Sorting, binary search, segment tree, heap, Dijkstra</td></tr>
            <tr><td>n ≤ 1,000,000</td><td><strong>O(n)</strong></td><td>Two pointers, sliding window, monotonic stack, hash map</td></tr>
            <tr><td>n ≤ 10⁹</td><td><strong>O(log n)</strong></td><td>Binary search on answer, math formula</td></tr>
            <tr><td>n ≤ 10¹⁸</td><td>O(log n) or O(√n)</td><td>Binary search, fast exponentiation, prime factorisation</td></tr>
          </tbody>
        </table>
      </div>

      <div class="insight-box">
        <h4>Quick Sanity Check: Will My Solution TLE?</h4>
        <ul>
          <li>Modern CPUs execute <strong>~10⁸ simple operations per second</strong>.</li>
          <li>O(n²) with n=10⁵: 10¹⁰ ops → <span style="color:#dc2626">TLE</span>. Need O(n log n) or better.</li>
          <li>O(n log n) with n=10⁶: ~2·10⁷ ops → <span style="color:#16a34a">Fast ✓</span></li>
          <li>O(2ⁿ) with n=30: 10⁹ ops → borderline TLE. With n=20: 10⁶ ops → OK.</li>
          <li>O(n!) with n=12: 4.8·10⁸ ops → borderline. With n=10: 3.6·10⁶ ops → OK.</li>
          <li><strong>When unsure:</strong> calculate n² or n·log(n) mentally and check against 10⁸.</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 6: TOP 50 PROBLEMS -->
    <section id="top-50" class="chapter-section">
      <h2>🏆 Section 6 — Top 50 Must-Know LeetCode Problems</h2>

      <h3>Arrays &amp; Hashing</h3>
      <div class="table-responsive">
        <table class="insight-table">
          <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Difficulty</th></tr></thead>
          <tbody>
            <tr><td>1</td><td>Two Sum</td><td>Hash Map</td><td class="diff-easy">Easy</td></tr>
            <tr><td>2</td><td>Best Time to Buy &amp; Sell Stock</td><td>Greedy / Kadane variant</td><td class="diff-easy">Easy</td></tr>
            <tr><td>3</td><td>Contains Duplicate</td><td>Hash Set</td><td class="diff-easy">Easy</td></tr>
            <tr><td>4</td><td>Product of Array Except Self</td><td>Prefix Product</td><td class="diff-medium">Medium</td></tr>
            <tr><td>5</td><td>Maximum Subarray (Kadane)</td><td>Greedy / DP</td><td class="diff-medium">Medium</td></tr>
            <tr><td>6</td><td>Maximum Product Subarray</td><td>DP (track min &amp; max)</td><td class="diff-medium">Medium</td></tr>
            <tr><td>7</td><td>Find Minimum in Rotated Array</td><td>Binary Search</td><td class="diff-medium">Medium</td></tr>
            <tr><td>8</td><td>3Sum</td><td>Sort + Two Pointers</td><td class="diff-medium">Medium</td></tr>
            <tr><td>9</td><td>Container With Most Water</td><td>Two Pointers</td><td class="diff-medium">Medium</td></tr>
            <tr><td>10</td><td>Trapping Rain Water</td><td>Monotonic Stack / Two Ptr</td><td class="diff-hard">Hard</td></tr>
          </tbody>
        </table>
      </div>

      <h3>Strings</h3>
      <div class="table-responsive">
        <table class="insight-table">
          <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Difficulty</th></tr></thead>
          <tbody>
            <tr><td>11</td><td>Longest Substring Without Repeating</td><td>Sliding Window</td><td class="diff-medium">Medium</td></tr>
            <tr><td>12</td><td>Minimum Window Substring</td><td>Sliding Window</td><td class="diff-hard">Hard</td></tr>
            <tr><td>13</td><td>Valid Anagram</td><td>Frequency Count</td><td class="diff-easy">Easy</td></tr>
            <tr><td>14</td><td>Group Anagrams</td><td>Sort as Key + Hash Map</td><td class="diff-medium">Medium</td></tr>
            <tr><td>15</td><td>Longest Palindromic Substring</td><td>Expand Around Centre / DP</td><td class="diff-medium">Medium</td></tr>
            <tr><td>16</td><td>Encode and Decode Strings</td><td>Prefix Length Encoding</td><td class="diff-medium">Medium</td></tr>
            <tr><td>17</td><td>Valid Parentheses</td><td>Stack</td><td class="diff-easy">Easy</td></tr>
          </tbody>
        </table>
      </div>

      <h3>Trees &amp; Graphs</h3>
      <div class="table-responsive">
        <table class="insight-table">
          <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Difficulty</th></tr></thead>
          <tbody>
            <tr><td>18</td><td>Invert Binary Tree</td><td>DFS/BFS</td><td class="diff-easy">Easy</td></tr>
            <tr><td>19</td><td>Maximum Depth of Binary Tree</td><td>DFS</td><td class="diff-easy">Easy</td></tr>
            <tr><td>20</td><td>Same Tree</td><td>DFS</td><td class="diff-easy">Easy</td></tr>
            <tr><td>21</td><td>Binary Tree Level Order Traversal</td><td>BFS</td><td class="diff-medium">Medium</td></tr>
            <tr><td>22</td><td>Validate Binary Search Tree</td><td>DFS + bounds</td><td class="diff-medium">Medium</td></tr>
            <tr><td>23</td><td>Lowest Common Ancestor</td><td>DFS post-order</td><td class="diff-medium">Medium</td></tr>
            <tr><td>24</td><td>Binary Tree Right Side View</td><td>BFS (last per level)</td><td class="diff-medium">Medium</td></tr>
            <tr><td>25</td><td>Clone Graph</td><td>DFS + Hash Map</td><td class="diff-medium">Medium</td></tr>
            <tr><td>26</td><td>Course Schedule (Topo Sort)</td><td>Kahn's BFS</td><td class="diff-medium">Medium</td></tr>
            <tr><td>27</td><td>Number of Islands</td><td>BFS/DFS or Union-Find</td><td class="diff-medium">Medium</td></tr>
            <tr><td>28</td><td>Word Ladder</td><td>BFS + Level</td><td class="diff-hard">Hard</td></tr>
            <tr><td>29</td><td>Word Search II</td><td>Trie + DFS Backtrack</td><td class="diff-hard">Hard</td></tr>
          </tbody>
        </table>
      </div>

      <h3>Binary Search &amp; Heaps</h3>
      <div class="table-responsive">
        <table class="insight-table">
          <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Difficulty</th></tr></thead>
          <tbody>
            <tr><td>30</td><td>Binary Search</td><td>Classic Template 1</td><td class="diff-easy">Easy</td></tr>
            <tr><td>31</td><td>Search in Rotated Sorted Array</td><td>Rotated Binary Search</td><td class="diff-medium">Medium</td></tr>
            <tr><td>32</td><td>Find Minimum in Rotated Array</td><td>Compare mid to hi</td><td class="diff-medium">Medium</td></tr>
            <tr><td>33</td><td>Koko Eating Bananas</td><td>Answer Space BS</td><td class="diff-medium">Medium</td></tr>
            <tr><td>34</td><td>Kth Largest Element in Array</td><td>Min-Heap of size k</td><td class="diff-medium">Medium</td></tr>
            <tr><td>35</td><td>Merge K Sorted Lists</td><td>Min-Heap of k heads</td><td class="diff-hard">Hard</td></tr>
            <tr><td>36</td><td>Top K Frequent Elements</td><td>Min-Heap or Bucket Sort</td><td class="diff-medium">Medium</td></tr>
            <tr><td>37</td><td>Find Median from Data Stream</td><td>Two Heaps</td><td class="diff-hard">Hard</td></tr>
          </tbody>
        </table>
      </div>

      <h3>Dynamic Programming</h3>
      <div class="table-responsive">
        <table class="insight-table">
          <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Difficulty</th></tr></thead>
          <tbody>
            <tr><td>38</td><td>Climbing Stairs</td><td>Fibonacci 1D DP</td><td class="diff-easy">Easy</td></tr>
            <tr><td>39</td><td>House Robber</td><td>1D DP rolling</td><td class="diff-medium">Medium</td></tr>
            <tr><td>40</td><td>Coin Change</td><td>Unbounded Knapsack</td><td class="diff-medium">Medium</td></tr>
            <tr><td>41</td><td>Longest Increasing Subsequence</td><td>1D DP or O(n log n)</td><td class="diff-medium">Medium</td></tr>
            <tr><td>42</td><td>Longest Common Subsequence</td><td>2D DP</td><td class="diff-medium">Medium</td></tr>
            <tr><td>43</td><td>Edit Distance</td><td>2D DP 3-way recurrence</td><td class="diff-hard">Hard</td></tr>
            <tr><td>44</td><td>Partition Equal Subset Sum</td><td>0/1 Knapsack</td><td class="diff-medium">Medium</td></tr>
            <tr><td>45</td><td>Unique Paths</td><td>Grid path counting DP</td><td class="diff-medium">Medium</td></tr>
            <tr><td>46</td><td>Word Break</td><td>1D DP + set</td><td class="diff-medium">Medium</td></tr>
            <tr><td>47</td><td>Best Time to Buy Stock w/ Cooldown</td><td>State Machine DP</td><td class="diff-medium">Medium</td></tr>
            <tr><td>48</td><td>Burst Balloons</td><td>Interval DP</td><td class="diff-hard">Hard</td></tr>
          </tbody>
        </table>
      </div>

      <h3>Backtracking &amp; Stack</h3>
      <div class="table-responsive">
        <table class="insight-table">
          <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Difficulty</th></tr></thead>
          <tbody>
            <tr><td>49</td><td>Combination Sum</td><td>Backtracking + pruning</td><td class="diff-medium">Medium</td></tr>
            <tr><td>50</td><td>N-Queens</td><td>Backtracking + O(1) check</td><td class="diff-hard">Hard</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 7: COMMON MISTAKES -->
    <section id="mistakes" class="chapter-section">
      <h2>⚠️ Section 7 — Universal Mistakes &amp; Red Flags</h2>

      <h3>7.1 — Integer Overflow</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// MISTAKE: int overflow in sum/product
int sum = 0;
for (int x : nums) sum += x; // overflows if nums has large values

// FIX: use long long
long long sum = 0;
for (int x : nums) sum += x;

// MISTAKE: mid calculation overflow
int mid = (lo + hi) / 2;   // lo+hi can overflow if both ~2^30

// FIX:
int mid = lo + (hi - lo) / 2;

// MISTAKE: multiplying two ints before assigning to long long
long long area = height * width;   // height*width computed as int first!

// FIX:
long long area = (long long)height * width;
{% endhighlight %}
</div>

      <h3>7.2 — Off-By-One</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// Binary Search variants:
while (lo <= hi)  { hi = mid - 1; lo = mid + 1; }  // exact search
while (lo < hi)   { hi = mid;     lo = mid + 1; }  // lower bound

// Array bounds: always check before accessing
if (i >= 0 && i < n && j >= 0 && j < m) grid[i][j];

// Substring length
s.substr(start, end - start + 1); // inclusive end
s.substr(start, end - start);     // exclusive end
{% endhighlight %}
</div>

      <h3>7.3 — Graph &amp; Tree Pitfalls</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// MISTAKE: Forgetting to check visited before pushing to BFS queue -> infinite loop
// FIX: mark visited WHEN PUSHING, not when popping
if (!visited[v]) { visited[v] = true; q.push(v); }

// Dijkstra: forgetting to skip stale heap entries
auto [d, u] = pq.top(); pq.pop();
if (d > dist[u]) continue; // CRITICAL: skip outdated entries

// Tree: confusing null check
if (!node) return 0;             // null node contributes 0 to depth
if (!node->left && !node->right) // leaf node check
{% endhighlight %}
</div>

      <h3>7.4 — DP Pitfalls</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// Missing base case: dp[0] must be set before the loop
vector<int> dp(amount+1, amount+1);
dp[0] = 0; // CRITICAL base case

// 0/1 Knapsack: iterating capacity forward (allows item reuse)
for (int cap = w[i]; cap <= W; cap++) // WRONG: unbounded knapsack
for (int cap = W; cap >= w[i]; cap--) // CORRECT: 0/1 knapsack

// 2D DP string indexing: text[i-1] not text[i] when using 1-indexed dp
if (s1[i-1] == s2[j-1]) dp[i][j] = dp[i-1][j-1] + 1;
{% endhighlight %}
</div>
    </section>

    <!-- SECTION 8: BIG-O GROWTH -->
    <section id="big-o" class="chapter-section">
      <h2>📈 Section 8 — Big-O Growth Cheat Card</h2>

      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr><th>Notation</th><th>Name</th><th>n=10</th><th>n=100</th><th>n=1,000</th><th>n=10⁶</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>O(1)</strong></td><td>Constant</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>
            <tr><td><strong>O(log n)</strong></td><td>Logarithmic</td><td>3</td><td>7</td><td>10</td><td>20</td></tr>
            <tr><td><strong>O(√n)</strong></td><td>Square Root</td><td>3</td><td>10</td><td>32</td><td>1,000</td></tr>
            <tr><td><strong>O(n)</strong></td><td>Linear</td><td>10</td><td>100</td><td>1,000</td><td>1,000,000</td></tr>
            <tr><td><strong>O(n log n)</strong></td><td>Linearithmic</td><td>33</td><td>664</td><td>10,000</td><td>20,000,000</td></tr>
            <tr><td><strong>O(n²)</strong></td><td>Quadratic</td><td>100</td><td>10,000</td><td>10⁶</td><td style="color:#dc2626">10¹² (TLE)</td></tr>
            <tr><td><strong>O(n³)</strong></td><td>Cubic</td><td>1,000</td><td>10⁶</td><td style="color:#dc2626">10⁹ (TLE)</td><td>—</td></tr>
            <tr><td><strong>O(2ⁿ)</strong></td><td>Exponential</td><td>1,024</td><td style="color:#dc2626">10³⁰ (TLE)</td><td>—</td><td>—</td></tr>
            <tr><td><strong>O(n!)</strong></td><td>Factorial</td><td>3.6M</td><td style="color:#dc2626">10¹⁵⁷ (TLE)</td><td>—</td><td>—</td></tr>
          </tbody>
        </table>
      </div>

      <div class="insight-box">
        <h4>Rules for Simplifying Big-O</h4>
        <ul>
          <li><strong>DROP CONSTANTS:</strong> O(3n) = O(n). O(2n² + 5n) = O(n²).</li>
          <li><strong>DROP LOWER TERMS:</strong> O(n² + n) = O(n²). O(n log n + n) = O(n log n).</li>
          <li><strong>DIFFERENT INPUTS use different variables:</strong> O(a + b) is NOT O(n). Keep separate.</li>
          <li><strong>NESTED LOOPS multiply:</strong> outer O(n) × inner O(n) = O(n²). Unless inner shrinks per outer.</li>
          <li><strong>RECURSION:</strong> T(n) = 2T(n/2) + O(n) ⇒ O(n log n) by Master Theorem (Merge Sort).</li>
          <li><strong>AMORTISED:</strong> dynamic array doubling is O(1) amortised per push_back despite occasional O(n) resize.</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 9: LAST-MINUTE REMINDERS -->
    <section id="reminders" class="chapter-section">
      <h2>🔥 Section 9 — Last-Minute Interview Reminders</h2>

      <div class="insight-box">
        <h4>Before You Code</h4>
        <ul>
          <li>Always ask: what are the constraints? (n, value range, sorted?)</li>
          <li>Always ask: can there be duplicates? negative numbers? empty input?</li>
          <li>State brute force first, then optimise. Never jump straight to the optimal.</li>
          <li>Announce your approach and complexity <strong>BEFORE</strong> writing code.</li>
        </ul>
      </div>

      <div class="insight-box">
        <h4>While Coding</h4>
        <ul>
          <li>Use <code>long long</code> for sums/products that might exceed 2×10⁹.</li>
          <li>Use <code>lo + (hi - lo) / 2</code>, never <code>(lo + hi) / 2</code>.</li>
          <li>Check array bounds before every access: <code>if (i &gt;= 0 &amp;&amp; i &lt; n)</code>.</li>
          <li>In BFS: mark visited when <strong>PUSHING</strong>, not when POPPING.</li>
          <li>In Dijkstra: skip stale heap entries with <code>if (d &gt; dist[u]) continue</code>.</li>
          <li>In 0/1 Knapsack 1D: iterate capacity in <strong>REVERSE</strong>.</li>
          <li>In Backtracking: always undo (<code>pop_back</code> / <code>used[i]=false</code>) after recursion.</li>
        </ul>
      </div>

      <div class="insight-box">
        <h4>Common Gotchas by Topic</h4>
        <ul>
          <li><strong>BINARY SEARCH:</strong> <code>lo &lt;= hi</code> for exact, <code>lo &lt; hi</code> for bound. <code>hi = n</code> (not n-1) for bound.</li>
          <li><strong>TWO POINTERS:</strong> only works on sorted arrays or when property is monotone.</li>
          <li><strong>SLIDING WINDOW:</strong> shrink left <em>WHILE</em> constraint violated (while, not if).</li>
          <li><strong>HEAP:</strong> C++ priority_queue is max-heap by default. For min-heap: <code>greater&lt;int&gt;</code>.</li>
          <li><strong>GRAPH BFS:</strong> use queue, not stack. Visited set prevents revisiting.</li>
          <li><strong>TREE DFS:</strong> handle null node at start: <code>if (!node) return base_val</code>.</li>
          <li><strong>BACKTRACKING:</strong> collect at every node for subsets; only at leaves for permutations.</li>
          <li><strong>DP:</strong> define state precisely BEFORE writing recurrence. Base cases BEFORE loop.</li>
          <li><strong>TRIE:</strong> <code>search()</code> returns false if <code>isEnd=false</code> even if path exists.</li>
          <li><strong>UNION-FIND:</strong> compare <code>find(a)==find(b)</code>, NOT <code>a==b</code>.</li>
        </ul>
      </div>

      <div class="insight-box">
        <h4>Complexity Red Flags</h4>
        <ul>
          <li>O(n²) with n &gt; 10⁴: you probably need sliding window, binary search, or a hash map.</li>
          <li>O(2ⁿ) with n &gt; 25: need DP or bitmask DP instead of backtracking.</li>
          <li>O(n!) with n &gt; 12: almost certainly needs pruning or a completely different approach.</li>
          <li>Calling <code>sort()</code> inside a loop: O(n² log n) — sort once outside.</li>
          <li>Using <code>substr()</code> inside a loop without memoisation: O(n² · L) — cache or use indices.</li>
        </ul>
      </div>

      <div class="insight-box" style="border-left-color: #0284c7; background: linear-gradient(135deg, #f0f9ff, #e0f2fe);">
        <h4>🎓 End of DSA Course — Chapters 0–12 Complete!</h4>
        <p style="margin: 0.5rem 0 0;">Arrays | Linked Lists | Stacks &amp; Queues | Hashing | Trees | Graphs | Heaps | Greedy | Binary Search | Backtracking | Dynamic Programming | Bonus Topics</p>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- CHAPTER NAVIGATION                         -->
    <!-- ========================================== -->
    <div class="chapter-nav-footer">
      <a href="/learning/dsa/intervals/ch11-bonus-topics/" class="ch-nav-footer-btn">← Prev: Ch11 Bonus Topics</a>
      <a href="/learning/dsa/dsa-roadmap/" class="ch-nav-footer-btn">Back to DSA Roadmap 🗺</a>
    </div>

</div>
