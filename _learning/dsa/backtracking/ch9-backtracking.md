---
layout: default
title: Ch9 Backtracking
permalink: /learning/dsa/backtracking/ch9-backtracking/
custom_css: dsa-chapter
---

<!-- ========================================== -->
<!-- HERO SECTION                               -->
<!-- ========================================== -->
<div class="chapter-hero" style="--bg-gradient: linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%); --theme-color: #0d9488;">
  <div class="ch-hero-content">
    <div class="breadcrumb">
      <a href="{{ '/learning/dsa/dsa-roadmap/' | relative_url }}">DSA Roadmap</a> <span class="separator">›</span> 
      <span class="current">Chapter 9</span>
    </div>
    <h1>Backtracking</h1>
    <p class="ch-subtitle">Decision Tree | Pruning | Subsets | Permutations | N-Queens</p>
    <div class="hero-stats">
      <span class="stat-badge"><span class="icon">📘</span> 11 Sections</span>
      <span class="stat-badge"><span class="icon">🧩</span> 2 Solved Problems</span>
      <span class="stat-badge diff-advanced">Advanced Difficulty</span>
      <span class="stat-badge prereq">Prerequisite: Ch8</span>
    </div>
  </div>
</div>

<!-- ========================================== -->
<!-- LAYOUT WRAPPER                             -->
<!-- ========================================== -->
<div class="chapter-content">

    <!-- SECTION 1 -->
    <section id="section-1" class="chapter-section">
      <h2> 1 — What Is Backtracking?</h2>
      <p><strong>Backtracking</strong> is a systematic method for exploring all possible solutions to a problem by building candidates incrementally and abandoning (<strong>pruning</strong>) a candidate as soon as it is determined that it cannot lead to a valid solution. It is a refined form of brute-force that avoids redundant exploration.</p>
      
      <div class="insight-box">
        <h4>The Backtracking Template</h4>
        <p>Every backtracking solution follows the same skeleton:</p>
        <ol>
          <li><strong>CHOOSE:</strong> pick a candidate element to add to the current partial solution.</li>
          <li><strong>EXPLORE:</strong> recurse with the candidate added.</li>
          <li><strong>UN-CHOOSE (backtrack):</strong> undo the choice before trying the next candidate.</li>
        </ol>
        <p>The recursion tree is called the <em>'decision tree'</em>. Each node is a partial state; each edge is a choice. Leaves are complete solutions or dead ends. <strong>Pruning</strong> cuts entire subtrees early: if no solution can exist in this subtree (constraint violated), skip it without exploring.</p>
      </div>

<div class="ch-code-wrap">
{% highlight cpp %}
// Universal Backtracking Template
void backtrack(State& state, vector<Result>& results) {
    // Base case: complete solution found
    if (isComplete(state)) {
        results.push_back(buildResult(state));
        return;
    }
    
    // Try every candidate for the next choice
    for (auto& candidate : getCandidates(state)) {
        if (!isValid(state, candidate)) continue; // prune invalid
        
        makeChoice(state, candidate);             // CHOOSE
        backtrack(state, results);                // EXPLORE
        undoChoice(state, candidate);             // UN-CHOOSE
    }
}
{% endhighlight %}
</div>

      <h3>1.1 — Backtracking vs Brute Force vs DP</h3>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>Dimension</th>
              <th>Brute Force</th>
              <th>Backtracking</th>
              <th>Dynamic Programming</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Exploration</strong></td>
              <td>All possible states</td>
              <td>Prune invalid subtrees early</td>
              <td>Reuse stored subproblem results</td>
            </tr>
            <tr>
              <td><strong>When used</strong></td>
              <td>No known structure</td>
              <td>Constraint-based search</td>
              <td>Overlapping subproblems</td>
            </tr>
            <tr>
              <td><strong>Undo step</strong></td>
              <td>Not needed</td>
              <td>Required (un-choose)</td>
              <td>Not needed</td>
            </tr>
            <tr>
              <td><strong>Complexity</strong></td>
              <td>Worst case exponential</td>
              <td>Exponential but pruned</td>
              <td>Polynomial (with memoisation)</td>
            </tr>
            <tr>
              <td><strong>Output type</strong></td>
              <td>One optimal value</td>
              <td>All valid solutions (or one)</td>
              <td>One optimal value</td>
            </tr>
            <tr>
              <td><strong>Space</strong></td>
              <td>O(1) extra</td>
              <td>O(depth) recursion stack</td>
              <td>O(n) to O(n²) table</td>
            </tr>
            <tr>
              <td><strong>Classic problems</strong></td>
              <td>Loop over all subsets</td>
              <td>Subsets, Permutations, N-Queens</td>
              <td>Coin Change, LCS, Knapsack</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="insight-box idea">
        <h4>Real-World Analogy: Solving a Maze</h4>
        <p>You stand at the entrance of a maze and want to find the exit. At each junction, you try one path. If you hit a dead end, you backtrack to the last junction and try a different path. This is exactly backtracking: explore a path fully, and if it fails, undo your steps and try the next option.<br><br><strong>Pruning:</strong> if a corridor is blocked (invalid constraint), skip it immediately without entering.<br><strong>The maze metaphor maps to code:</strong> junction = recursive call, dead end = base case failure, backtrack = undo the last choice.</p>
      </div>
    </section>

    <!-- SECTION 2 -->
    <section id="section-2" class="chapter-section">
      <h2> 2 — Visual Diagrams: Decision Trees</h2>

      <h3>Diagram 1 — Subsets Decision Tree</h3>
      <p><strong>Subsets: Full Decision Tree (n=3)</strong><br><code>nums = [1, 2, 3]</code><br>Generate all subsets (power set). At each level, we decide: include <code>nums[i]</code> or skip it.</p>
<pre class="trace-output">
                  []
               /      \
            [1]         []
           /   \       /  \
        [1,2]  [1]   [2]   []
        /  \   / \   / \   / \
[1,2,3][1,2][1,3][1][2,3][2][3][]
</pre>
      <p>Leaves (all 8 = 2³ subsets): <code>[1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []</code><br>No pruning needed here (all paths are valid). Total nodes in tree = 2^(n+1) - 1 = 15 for n=3.</p>

      <h3>Diagram 2 — Permutations Decision Tree</h3>
      <p><strong>Permutations: Decision Tree (n=3)</strong><br><code>nums = [1, 2, 3]</code><br>Generate all permutations. At each level, pick one unused number. <code>used = {}</code> tracks which numbers are already in the current path.</p>
<pre class="trace-output">
                []
          /      |      \
        [1]     [2]     [3]
       /   \    /  \    /  \
    [1,2][1,3][2,1][2,3][3,1][3,2]
      |     |    |    |    |    |
[1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]
</pre>
      <p>6 leaves = 3! = n! permutations. No pruning (no duplicates in input). Total nodes = 1 + 3 + 6 + 6 = 16 for n=3.<br><em>With duplicates (e.g. [1,1,2]):</em> sort first, then skip if <code>nums[i] == nums[i-1]</code> and <code>nums[i-1]</code> was <strong>NOT</strong> used in this level. This prunes duplicate branches at each depth level.</p>

      <h3>Diagram 3 — N-Queens Pruning</h3>
      <p><strong>N-Queens: Constraint-Based Pruning</strong><br>N=4: place 4 queens on a 4x4 board, no two attacking each other. Place one queen per row. For each row, try all columns.</p>
<pre class="trace-output">
Row 0: try col 0, 1, 2, 3.
Row 0, col 0:
Q . . .

Row 1, try cols:
col 0 (same col, PRUNE), col 1 (diagonal, PRUNE), col 2 (safe), col 3 (diagonal, PRUNE).

Row 1, col 2:
Q . . .
. . Q .

Row 2, try cols:
all attacked by Q at (0,0) or (1,2) -> all PRUNED. Backtrack to row 1.

Try col 3:
Q . . .
. . . Q

Row 2, col 1:
Q . . .
. . . Q
. Q . .

Row 3: cols 0 (col prune), 1 (col prune), 2 (diag prune), 3 (col prune). 
All pruned. Backtrack to row 0, try col 1.  ...
</pre>
      <p><strong>Solutions found: 2 (for N=4).</strong></p>
<pre class="trace-output">
. Q . .      . . Q .
. . . Q      Q . . .
Q . . .      . . . Q
. . Q .      . Q . .
</pre>
      <p><strong>Pruning criteria:</strong> same column, same diagonal (r1-c1 == r2-c2), or same anti-diagonal (r1+c1 == r2+c2).</p>

      <h3>Diagram 4 — Combination Sum</h3>
      <p><strong>Combination Sum: Pruning on Remaining Target</strong><br><code>candidates = [2, 3, 6, 7]</code>, <code>target = 7</code><br>Find all combinations that sum to target (reuse allowed).</p>
<pre class="trace-output">
start=0 (index), path=[], remaining=7
 |
 +-- pick 2, remaining=5
 |     +-- pick 2, remaining=3
 |     |     +-- pick 2, remaining=1
 |     |     |     +-- pick 2, remaining=-1 PRUNE (negative)
 |     |     |     +-- pick 3, remaining=-2 PRUNE
 |     |     +-- pick 3, remaining=0   SOLUTION: [2,2,3]
 |     |     +-- pick 6, remaining=-3 PRUNE
 |     +-- pick 3, remaining=2
 |     |     +-- pick 3, remaining=-1 PRUNE
 |     |     (no more valid picks)
 |     +-- pick 6, remaining=-1 PRUNE
 +-- pick 3, remaining=4
 |     +-- pick 3, remaining=1
 |     |     +-- pick 3, remaining=-2 PRUNE
 |     +-- pick 6, remaining=-2 PRUNE
 +-- pick 6, remaining=1
 |     +-- pick 6, remaining=-5 PRUNE
 +-- pick 7, remaining=0   SOLUTION: [7]
</pre>
      <p>Solutions: <code>[2,2,3]</code> and <code>[7]</code>.</p>
    </section>

    <!-- SECTION 3 -->
    <section id="section-3" class="chapter-section">
      <h2> 3 — Real-World Use Cases</h2>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>Problem</th>
              <th>Backtracking Application</th>
              <th>Industry System</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Puzzle solving</td>
              <td>Sudoku, crosswords, constraint satisfaction</td>
              <td>Game engines, puzzle generators</td>
            </tr>
            <tr>
              <td>Circuit layout</td>
              <td>VLSI routing — place wires avoiding conflicts</td>
              <td>EDA (Electronic Design Automation) tools</td>
            </tr>
            <tr>
              <td>Regex matching</td>
              <td>NFA simulation backtracks on failed matches</td>
              <td>grep, database query engines, parsers</td>
            </tr>
            <tr>
              <td>Natural language parsing</td>
              <td>Earley/CYK parser explores grammar rules</td>
              <td>NLP compilers, syntax highlighters</td>
            </tr>
            <tr>
              <td>Test case generation</td>
              <td>Enumerate all input combinations for coverage</td>
              <td>Automated software testing frameworks</td>
            </tr>
            <tr>
              <td>Scheduling</td>
              <td>Assign tasks to slots satisfying constraints</td>
              <td>University timetabling, exam scheduling</td>
            </tr>
            <tr>
              <td>Cryptography</td>
              <td>Key space enumeration for brute-force attacks</td>
              <td>Security penetration testing tools</td>
            </tr>
            <tr>
              <td>Combinatorial optimisation</td>
              <td>TSP branch-and-bound with backtracking pruning</td>
              <td>Logistics, route planning, supply chain</td>
            </tr>
            <tr>
              <td>AI game playing</td>
              <td>Minimax with alpha-beta pruning</td>
              <td>Chess engines, Go AI (pre-neural era)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 4 -->
    <section id="section-4" class="chapter-section">
      <h2> 4 — Core Concepts & Algorithms</h2>

      <h3>4.1 — Subsets (Power Set)</h3>
      <p>Generate all 2^n subsets of nums. The start index prevents permutations of the same subset.</p>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 78 — Subsets — O(2^n * n) Time, O(n) Space
class Solution {
    void bt(vector<int>& nums, int start, vector<int>& path, vector<vector<int>>& res) {
        res.push_back(path); // every node is a valid subset
        
        for (int i = start; i < (int)nums.size(); i++) {
            path.push_back(nums[i]);       // CHOOSE
            bt(nums, i+1, path, res);      // EXPLORE (i+1: no reuse)
            path.pop_back();               // UN-CHOOSE
        }
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        bt(nums, 0, path, res);
        return res;
    }
};

// Subsets II — with duplicates (LC 90)
// Sort first, then skip nums[i] == nums[i-1] at the same recursion level.
void btII(vector<int>& nums, int start, vector<int>& path, vector<vector<int>>& res) {
    res.push_back(path);
    for (int i = start; i < (int)nums.size(); i++) {
        if (i > start && nums[i] == nums[i-1]) continue; // skip duplicate
        path.push_back(nums[i]);
        btII(nums, i+1, path, res);
        path.pop_back();
    }
}
{% endhighlight %}
</div>

      <h3>4.2 — Permutations</h3>
      <p>Order matters. We use a <code>used[]</code> array to track selections and loop from 0 every time.</p>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 46 — Permutations (no duplicates) — O(n! * n) Time, O(n) Space
class Solution {
    void bt(vector<int>& nums, vector<bool>& used, vector<int>& path, vector<vector<int>>& res) {
        if ((int)path.size() == (int)nums.size()) {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < (int)nums.size(); i++) {
            if (used[i]) continue; // already in path
            used[i] = true;        // CHOOSE
            path.push_back(nums[i]);
            
            bt(nums, used, path, res); // EXPLORE
            
            path.pop_back();       // UN-CHOOSE
            used[i] = false;
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<bool> used(nums.size(), false);
        vector<int> path;
        bt(nums, used, path, res);
        return res;
    }
};

// Permutations II — with duplicates (LC 47)
// Sort first. Skip nums[i]==nums[i-1] when nums[i-1] is NOT used.
// (This means we only take the first copy of a duplicate at each level.)
void btII(vector<int>& nums, vector<bool>& used, vector<int>& path, vector<vector<int>>& res) {
    if ((int)path.size() == (int)nums.size()) { res.push_back(path); return; }
    for (int i = 0; i < (int)nums.size(); i++) {
        if (used[i]) continue;
        if (i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue; // prune dup
        used[i] = true;
        path.push_back(nums[i]);
        btII(nums, used, path, res);
        path.pop_back();
        used[i] = false;
    }
}
{% endhighlight %}
</div>

      <h3>4.3 — Combinations</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 77 — Combinations: choose k numbers from [1..n] — O(C(n,k) * k)
class Solution {
    void bt(int n, int k, int start, vector<int>& path, vector<vector<int>>& res) {
        if ((int)path.size() == k) {
            res.push_back(path);
            return;
        }
        // Pruning: need k-path.size() more elements, at most n-i+1 remain
        for (int i = start; i <= n - (k - (int)path.size()) + 1; i++) {
            path.push_back(i);       // CHOOSE
            bt(n, k, i+1, path, res); // EXPLORE
            path.pop_back();         // UN-CHOOSE
        }
    }
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> path;
        bt(n, k, 1, path, res);
        return res;
    }
};
{% endhighlight %}
</div>

      <h3>4.4 — Combination Sum (Reuse Allowed)</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 39 — Combination Sum — Time: O(N^(T/M)) N=candidates, T=target, M=min
class Solution {
    void bt(vector<int>& cands, int start, int remain, vector<int>& path, vector<vector<int>>& res) {
        if (remain == 0) { res.push_back(path); return; }
        
        for (int i = start; i < (int)cands.size(); i++) {
            if (cands[i] > remain) break; // sorted: all further are larger, PRUNE
            
            path.push_back(cands[i]);
            bt(cands, i, remain - cands[i], path, res); // i (not i+1): reuse ok
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end()); // sort to enable pruning
        vector<vector<int>> res;
        vector<int> path;
        bt(candidates, 0, target, path, res);
        return res;
    }
};
{% endhighlight %}
</div>

      <h3>4.5 — N-Queens</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 51 — N-Queens — O(N!) Time, O(N) Space
// Place N queens on N×N board so none attack each other.
class Solution {
    vector<vector<string>> res;
    vector<bool> col, diag1, diag2; // col, '/' diagonal, '\' diagonal
    
    void bt(int row, int n, vector<string>& board) {
        if (row == n) {
            res.push_back(board);
            return;
        }
        for (int c = 0; c < n; c++) {
            // Prune: column or either diagonal is occupied
            if (col[c] || diag1[row-c+n-1] || diag2[row+c]) continue;
            
            board[row][c] = 'Q';       // CHOOSE
            col[c] = diag1[row-c+n-1] = diag2[row+c] = true;
            
            bt(row+1, n, board);       // EXPLORE
            
            board[row][c] = '.';       // UN-CHOOSE
            col[c] = diag1[row-c+n-1] = diag2[row+c] = false;
        }
    }
public:
    vector<vector<string>> solveNQueens(int n) {
        col.assign(n,false);
        diag1.assign(2*n-1,false); // '/' diagonals: indexed by row-col+n-1
        diag2.assign(2*n-1,false); // '\' diagonals: indexed by row+col
        vector<string> board(n, string(n,'.'));
        bt(0, n, board);
        return res;
    }
};
{% endhighlight %}
</div>

      <h3>4.6 — Word Search on Grid</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 79 — Word Search — O(M*N * 4^L)
class Solution {
    bool bt(vector<vector<char>>& g, string& w, int idx, int r, int c) {
        if (idx == (int)w.size()) return true; // all chars matched
        if (r<0||r>=(int)g.size()||c<0||c>=(int)g[0].size()) return false;
        if (g[r][c] != w[idx]) return false;   // mismatch: prune
        
        char tmp = g[r][c];
        g[r][c] = '#'; // CHOOSE: mark visited
        
        bool found = bt(g,w,idx+1,r+1,c) || bt(g,w,idx+1,r-1,c) || 
                     bt(g,w,idx+1,r,c+1) || bt(g,w,idx+1,r,c-1);
                     
        g[r][c] = tmp; // UN-CHOOSE: restore cell
        return found;
    }
public:
    bool exist(vector<vector<char>>& board, string word) {
        for (int r=0; r<(int)board.size(); r++)
            for (int c=0; c<(int)board[0].size(); c++)
                if (bt(board, word, 0, r, c)) return true;
        return false;
    }
};
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
              <th>Problem Type</th>
              <th>Template Variation</th>
              <th>Key Decisions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Subsets (no duplicates)</td>
              <td>Collect at every node; loop from start</td>
              <td>start index prevents reuse / duplicates</td>
            </tr>
            <tr>
              <td>Subsets (with duplicates)</td>
              <td>Sort + skip nums[i]==nums[i-1] at same level</td>
              <td><code>i > start</code> guards same-level skip</td>
            </tr>
            <tr>
              <td>Permutations (no dupes)</td>
              <td>used[] array; loop from 0 every time</td>
              <td>used[] prevents reusing same element</td>
            </tr>
            <tr>
              <td>Permutations (with dupes)</td>
              <td>Sort + skip when prev duplicate unused</td>
              <td><code>!used[i-1]</code> ensures canonical ordering</td>
            </tr>
            <tr>
              <td>Combinations (k of n)</td>
              <td>Collect when path.size()==k</td>
              <td>Upper bound prune: <code>i <= n-(k-path.size())+1</code></td>
            </tr>
            <tr>
              <td>Combination sum (reuse)</td>
              <td>Pass i (not i+1) to allow reuse</td>
              <td>Sort + break when candidate > remain</td>
            </tr>
            <tr>
              <td>Combination sum II</td>
              <td>Pass i+1; skip duplicates at same level</td>
              <td><code>i > start && nums[i]==nums[i-1]</code></td>
            </tr>
            <tr>
              <td>N-Queens / Sudoku</td>
              <td>Boolean arrays for constraints</td>
              <td>col[], diag1[], diag2[] for O(1) check</td>
            </tr>
            <tr>
              <td>Word search / grid</td>
              <td>Mark cell visited; restore on backtrack</td>
              <td><code>g[r][c]='#'</code> then restore to tmp</td>
            </tr>
            <tr>
              <td>Palindrome partitioning</td>
              <td>Collect when index == s.size()</td>
              <td>isPalindrome check before recursing</td>
            </tr>
            <tr>
              <td>Generate parentheses</td>
              <td>Track open and close counts</td>
              <td>open < n to add <code>'('</code>; close < open to add <code>')'</code></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="insight-box">
        <h4>Backtracking Complexity Formula</h4>
        <ul>
          <li><strong>For subsets:</strong> O(2^n * n) — 2^n subsets, each copied in O(n).</li>
          <li><strong>For permutations:</strong> O(n! * n) — n! permutations, each copied in O(n).</li>
          <li><strong>For combinations C(n,k):</strong> O(C(n,k) * k) — C(n,k) results, each copied in O(k).</li>
          <li><strong>For N-Queens:</strong> O(N!) with pruning significantly reducing the constant factor.</li>
          <li><strong>For word search:</strong> O(M*N * 4^L) — M*N starting points, 4^L paths of length L.</li>
        </ul>
        <p>Backtracking is exponential by nature. Pruning reduces the constant but not the exponent. If a problem has overlapping subproblems AND only needs the count or optimal value (not all solutions), DP is almost always faster.</p>
      </div>

      <div class="insight-box warning">
        <h4>Duplicate Handling Cheat Sheet</h4>
        <ul>
          <li><strong>SUBSETS</strong> with duplicates: sort nums. In the loop, skip if <code>i > start && nums[i] == nums[i-1]</code>.</li>
          <li><strong>PERMUTATIONS</strong> with duplicates: sort nums. Skip if <code>i > 0 && nums[i] == nums[i-1] && !used[i-1]</code>.</li>
        </ul>
        <p><strong>Why different?</strong> <br>
        Subsets: 'start' is the left boundary of the current level. <br>
        Permutations: level always starts at 0, so check <code>!used[i-1]</code> to detect same-level duplicate. <br><br>
        Golden rule: sort the input first, then skip consecutive duplicates AT THE SAME RECURSION LEVEL.</p>
      </div>
    </section>

    <!-- SECTION 6 -->
    <section id="section-6" class="chapter-section">
      <h2> 6 — Complete C++ Implementations</h2>

      <h3>6.1 — Generate Parentheses</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 22 — Generate Parentheses — O(4^n / sqrt(n)) Catalan number
class Solution {
    void bt(int n, int open, int close, string& curr, vector<string>& res) {
        if ((int)curr.size() == 2*n) { res.push_back(curr); return; }
        
        if (open < n) { // can add '('
            curr.push_back('(');
            bt(n, open+1, close, curr, res);
            curr.pop_back();
        }
        if (close < open) { // can add ')' only if open > close
            curr.push_back(')');
            bt(n, open, close+1, curr, res);
            curr.pop_back();
        }
    }
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res; string curr;
        bt(n, 0, 0, curr, res);
        return res;
    }
};
{% endhighlight %}
</div>

      <h3>6.2 — Palindrome Partitioning</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 131 — Palindrome Partitioning — O(2^n * n) Time, O(n) Space
class Solution {
    bool isPalin(string& s, int l, int r) {
        while (l < r) if (s[l++] != s[r--]) return false;
        return true;
    }
    void bt(string& s, int start, vector<string>& path, vector<vector<string>>& res) {
        if (start == (int)s.size()) { res.push_back(path); return; }
        
        for (int end = start; end < (int)s.size(); end++) {
            if (!isPalin(s, start, end)) continue; // prune non-palindromes
            path.push_back(s.substr(start, end-start+1));
            bt(s, end+1, path, res);
            path.pop_back();
        }
    }
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res; vector<string> path;
        bt(s, 0, path, res);
        return res;
    }
};
{% endhighlight %}
</div>

      <h3>6.3 — Sudoku Solver</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 37 — Sudoku Solver — O(9^M) Time M=empty cells, O(M) Space
class Solution {
    bool isValid(vector<vector<char>>& b, int r, int c, char d) {
        for (int i=0;i<9;i++) {
            if (b[r][i]==d || b[i][c]==d) return false;
            if (b[3*(r/3)+i/3][3*(c/3)+i%3]==d) return false;
        }
        return true;
    }
    bool bt(vector<vector<char>>& b) {
        for (int r=0;r<9;r++) {
            for (int c=0;c<9;c++) {
                if (b[r][c] != '.') continue;
                for (char d='1'; d<='9'; d++) {
                    if (!isValid(b,r,c,d)) continue;
                    b[r][c] = d;
                    if (bt(b)) return true;
                    b[r][c] = '.';
                }
                return false; // no digit worked: backtrack
            }
        }
        return true; // all cells filled
    }
public:
    void solveSudoku(vector<vector<char>>& board) {
        bt(board);
    }
};
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
              <th>Time (without pruning)</th>
              <th>Space</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Subsets (no duplicates)</td>
              <td>O(2^n * n)</td>
              <td>O(n)</td>
            </tr>
            <tr>
              <td>Subsets II (duplicates)</td>
              <td>O(2^n * n) pruning reduces const</td>
              <td>O(n)</td>
            </tr>
            <tr>
              <td>Permutations (no duplicates)</td>
              <td>O(n! * n)</td>
              <td>O(n)</td>
            </tr>
            <tr>
              <td>Permutations II (duplicates)</td>
              <td>O(n! * n) pruning reduces const</td>
              <td>O(n)</td>
            </tr>
            <tr>
              <td>Combinations C(n,k)</td>
              <td>O(C(n,k) * k)</td>
              <td>O(k)</td>
            </tr>
            <tr>
              <td>Combination Sum (reuse)</td>
              <td>O(N^(T/M)) T=target, M=min cand</td>
              <td>O(T/M)</td>
            </tr>
            <tr>
              <td>N-Queens</td>
              <td>O(N!) heavily pruned in practice</td>
              <td>O(N)</td>
            </tr>
            <tr>
              <td>Sudoku Solver</td>
              <td>O(9^M) M = empty cells</td>
              <td>O(M)</td>
            </tr>
            <tr>
              <td>Word Search</td>
              <td>O(M*N * 4^L) L = word length</td>
              <td>O(L)</td>
            </tr>
            <tr>
              <td>Generate Parentheses</td>
              <td>O(4^n / sqrt(n)) Catalan number</td>
              <td>O(n)</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p>Backtracking is always exponential in the worst case — this is unavoidable for NP problems. The stated complexity is without pruning. With good pruning, practical performance can be orders of magnitude better. Space is O(depth of recursion tree) = O(n) for most problems — only the current path is stored on the stack.</p>
    </section>

    <!-- SECTION 8 -->
    <section id="section-8" class="chapter-section">
      <h2> 8 — Solved Problem 1</h2>
      <div class="problem-card">
        <div class="problem-header">
          <h3>Combination Sum</h3>
          <span class="diff-medium">Medium</span>
        </div>
        <p>Given an array of distinct integers <code>candidates</code> and a target integer <code>target</code>, return all unique combinations of candidates where the chosen numbers sum to target. The same number may be chosen from candidates an unlimited number of times.</p>
        
        <h4>Observations</h4>
        <p>Since elements can be reused, this is not a standard subset problem. We pass the same index <code>i</code> (not <code>i+1</code>) to allow reuse.</p>
        <ul>
          <li><strong>Key insight 1:</strong> Sort candidates first. If the current candidate exceeds the remaining target, all further candidates (which are larger) also exceed it — break early.</li>
          <li><strong>Key insight 2:</strong> Use a start index to avoid generating duplicates like <code>[2,3]</code> and <code>[3,2]</code>. By only considering candidates at <code>index >= start</code>, we ensure combinations are in non-decreasing order.</li>
        </ul>

        <h4>Complexities</h4>
        <ul>
          <li><strong>Time:</strong> O(N^(T/M)) branching T/M deep where T=target, M=min element.</li>
          <li><strong>Space:</strong> O(T/M) maximum recursion stack depth.</li>
        </ul>

        <h4>Dry Run (candidates = [2,3,6,7], target = 7)</h4>
<pre class="trace-output">
Call       start  remain   path      Action
bt(0,7)    0      7        []        try 2,3,6,7
bt(0,5)    0      5        [2]       try 2,3,6,7
bt(0,3)    0      3        [2,2]     try 2,3,6,7
bt(0,1)    0      1        [2,2,2]   try 2(>1 no), 3(break)
bt(1,1)    1      1        [2,2,3]   3>1, break. backtrack back to [2,2]
           1      3        [2,2]     pick 3: remain=0
remain==0  —      0        [2,2,3]   SOLUTION! add to res
</pre>
        <p>Final result: <code>[[2,2,3], [7]]</code></p>
      </div>
    </section>
    
    <!-- SECTION 9 -->
    <section id="section-9" class="chapter-section">
      <h2> 9 — Solved Problem 2</h2>
      <div class="problem-card">
        <div class="problem-header">
          <h3>N-Queens</h3>
          <span class="diff-hard">Hard</span>
        </div>
        <p>Place n queens on an n x n chessboard so that no two queens attack each other (no shared row, column, or diagonal). Return all distinct solutions as board configurations.</p>
        
        <h4>Observations</h4>
        <ul>
          <li><strong>Key insight 1:</strong> Place exactly one queen per row. This reduces the problem to choosing one column per row.</li>
          <li><strong>Key insight 2:</strong> Three O(1) lookup arrays suffice for constraint checking: <code>col[]</code>, <code>diag1[]</code> (indexed by row-col+n-1 for the '/' diagonal), <code>diag2[]</code> (indexed by row+col for the '\' diagonal).</li>
          <li><strong>Pruning is critical:</strong> Without it, complexity is n^n. With column+diagonal pruning, the search space shrinks to approximtely n!. For n=8: 8^8 = 16M vs 8! = 40K.</li>
        </ul>

        <h4>Complexities</h4>
        <ul>
          <li><strong>Time:</strong> O(N!) — search space pruned heavily.</li>
          <li><strong>Space:</strong> O(n) for the recursion stack and O(1) arrays.</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 10 -->
    <section id="section-10" class="chapter-section">
      <h2> 10 — Common Mistakes & Edge Cases</h2>

      <h3>10.1 — Structural Mistakes</h3>
      <ul>
        <li><strong>Forgetting the un-choose (backtrack) step.</strong> Without undoing the choice, the path accumulates garbage from previous branches.</li>
        <li><strong>Passing <code>path</code> by value instead of by reference.</strong> This copies the path at every node — O(n) per call — making the algorithm significantly slower. Always pass by reference and use <code>push_back</code>/<code>pop_back</code>.</li>
        <li><strong>For subsets, collecting results only at the leaf.</strong> Every node is a valid subset — collect at the beginning of every call.</li>
        <li><strong>For combination sum with reuse, passing i+1 instead of i.</strong> This prevents reusing the same element and misses valid combinations.</li>
      </ul>

      <h3>10.2 — Duplicate Handling Mistakes</h3>
      <ul>
        <li><strong>Subsets/Combo sum:</strong> Skipping duplicates using <code>i > 0</code> instead of <code>i > start</code>. This skips valid paths where a duplicate appears deeper in the tree, not just at the same level.</li>
        <li><strong>Permutations:</strong> Skipping when <code>!used[i-1]</code> without sorting first. The deduplication logic only works if identical elements are adjacent.</li>
        <li><strong>Confusing the skip conditions:</strong> Subsets use <code>i > start</code>. Permutations use <code>i > 0 && nums[i]==nums[i-1] && !used[i-1]</code>.</li>
      </ul>

      <h3>10.3 — Edge Cases</h3>
      <ul>
        <li><strong>Empty input:</strong> subsets of <code>[]</code> = <code>[[]]</code> (one empty subset). Always initialise result with empty and handle gracefully.</li>
        <li><strong>Single element:</strong> subsets of <code>[1]</code> = <code>[[], [1]]</code>. Permutations of <code>[1]</code> = <code>[[1]]</code>.</li>
        <li><strong>Target = 0 for combination sum:</strong> the only solution is <code>[]</code> (empty combination).</li>
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
              <td>Subsets (LC 78)</td>
              <td>Collect at every node, loop from start</td>
            </tr>
            <tr>
              <td>Subsets II (LC 90)</td>
              <td>Sort + skip <code>i > start && nums[i]==nums[i-1]</code></td>
            </tr>
            <tr>
              <td>Permutations (LC 46)</td>
              <td><code>used[]</code> array, loop 0 to N every time</td>
            </tr>
            <tr>
              <td>Permutations II (LC 47)</td>
              <td>Sort + skip when <code>!used[i-1]</code></td>
            </tr>
            <tr>
              <td>Combination Sum (LC 39)</td>
              <td>Reuse allowed, sort + break prune, pass <code>i</code></td>
            </tr>
            <tr>
              <td>Combination Sum II (LC 40)</td>
              <td>No reuse, pass <code>i+1</code>, skip duplicates <code>i > start</code></td>
            </tr>
            <tr>
              <td>N-Queens (LC 51)</td>
              <td><code>col[]</code>, <code>diag1[]</code>, <code>diag2[]</code> O(1) checks</td>
            </tr>
            <tr>
              <td>Word Search (LC 79)</td>
              <td>Mark visited with <code>'#'</code>, restore on backtrack</td>
            </tr>
            <tr>
              <td>Palindrome Partitioning (LC 131)</td>
              <td>Check palindrome before recursing to prune</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="insight-box">
        <h4>Chapter 9 — Key Takeaways</h4>
        <ul>
          <li>Backtracking = <code>choose</code> + <code>explore</code> + <code>un-choose</code>. The un-choose step is non-negotiable.</li>
          <li>Pruning is the difference between TLE and AC. Always prune invalid branches before recursing.</li>
          <li>Subsets: collect at EVERY node. Use start index.</li>
          <li>Permutations: collect at leaves only. Use <code>used[]</code> array. Loop from 0.</li>
          <li>Combination sum with reuse: pass <code>i</code> (not <code>i+1</code>) to allow picking same element again.</li>
          <li>If problem only needs COUNT or OPTIMAL VALUE and subproblems overlap, prefer DP over backtracking.</li>
        </ul>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- CHAPTER NAVIGATION                         -->
    <!-- ========================================== -->
    <div class="chapter-nav-footer">
      <a href="{{ '/learning/dsa/binary-search/ch8-binary-search/' | relative_url }}" class="ch-nav-footer-btn">← Prev: Ch8 Binary Search</a>
      <a href="{{ '/learning/dsa/dsa-roadmap/' | relative_url }}" class="ch-nav-footer-btn">Next: Ch10 DP (Locked)<i class="fas fa-lock" style="margin-left: 8px;"></i></a>
    </div>


</div>
