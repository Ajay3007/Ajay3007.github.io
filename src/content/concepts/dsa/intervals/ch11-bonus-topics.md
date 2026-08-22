---
title: "Ch11 Bonus Topics"
description: "DSA Roadmap › Chapter 11 Bonus Topics Trie Union-Find (DSU) Monotonic Stack Sliding Window Two Pointers 📘 5 Topics 🧩 3 Solved Problems Intermediate Difficulty Prerequisite:…"
domain: dsa
track: dsa-mastery
order: 11
url: /learning/dsa/intervals/ch11-bonus-topics/
---

<!-- ========================================== -->
<!-- HERO SECTION                               -->
<!-- ========================================== -->
<div class="chapter-hero" style="--bg-gradient: linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%); --theme-color: #0d9488;">
  <div class="ch-hero-content">
    <div class="breadcrumb">
      <a href="/learning/dsa/dsa-roadmap/">DSA Roadmap</a> <span class="separator">›</span> 
      <span class="current">Chapter 11</span>
    </div>
    <h1>Bonus Topics</h1>
    <p class="ch-subtitle">Trie | Union-Find (DSU) | Monotonic Stack | Sliding Window | Two Pointers</p>
    <div class="hero-stats">
      <span class="stat-badge"><span class="icon">📘</span> 5 Topics</span>
      <span class="stat-badge"><span class="icon">🧩</span> 3 Solved Problems</span>
      <span class="stat-badge diff-intermediate">Intermediate Difficulty</span>
      <span class="stat-badge prereq">Prerequisite: Ch10</span>
    </div>
  </div>
</div>

<!-- ========================================== -->
<!-- LAYOUT WRAPPER                             -->
<!-- ========================================== -->
<div class="chapter-content">

    <!-- TOPIC A: TRIE -->
    <section id="topic-a" class="chapter-section">
      <h2> Topic A — Trie (Prefix Tree)</h2>
      
      <h3>A.1 — What Is a Trie?</h3>
      <p>A <strong>Trie</strong> (pronounced 'try', from retrieval) is a tree-shaped data structure for storing strings where each node represents a single character. Strings that share a common prefix share the same path from the root. This gives <strong>O(L) insert, search, and prefix-search</strong> operations where L is the string length — independent of the number of stored strings.</p>

      <div class="ch-code-wrap">
<pre><code>Trie Structure: Character-by-Character Branching
  Insert: ['apple', 'app', 'apt', 'bat', 'bad']

              root
             /    \
            a      b
            |      |
            p      a
           / \    / \
          p   t  t   d
          |   |  *   *     (* = isEnd marker)
          l   *
          |
          e
          |
          *

  'app'  -> root->a->p->p*       (isEnd=true at second p)
  'apple' -> root->a->p->p->l->e* (extends 'app' branch)
  'apt'  -> root->a->p->t*       (shares 'ap' with above)

  Search 'app': traverse a->p->p, check isEnd -> true.
  StartsWith 'ap': traverse a->p, node exists -> true.
  Search 'ap': traverse a->p, isEnd=false -> false.</code></pre>
      </div>

      <h3>A.2 — Trie Implementation</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// Trie — O(L) per operation
// Insert/Search/StartsWith: O(L) time, O(L) space per word
struct TrieNode {
    TrieNode* children[26] = {};  // null = child doesn't exist
    bool isEnd = false;
};

class Trie {
    TrieNode* root;
public:
    Trie() { root = new TrieNode(); }

    void insert(const string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!cur->children[idx])
                cur->children[idx] = new TrieNode();
            cur = cur->children[idx];
        }
        cur->isEnd = true;
    }

    bool search(const string& word) {
        TrieNode* cur = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!cur->children[idx]) return false;
            cur = cur->children[idx];
        }
        return cur->isEnd;   // must be a complete word
    }

    bool startsWith(const string& prefix) {
        TrieNode* cur = root;
        for (char c : prefix) {
            int idx = c - 'a';
            if (!cur->children[idx]) return false;
            cur = cur->children[idx];
        }
        return true;  // prefix exists, word completeness irrelevant
    }
};
{% endhighlight %}
</div>

      <h3>A.3 — Word Search II (Trie + Backtracking)</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 212 — Word Search II
// Find all words from a dictionary that exist in a 2D grid.
// Time: O(M*N * 4^L)  L=longest word  Space: O(total chars in dict)
struct TrieNode {
    TrieNode* ch[26] = {};
    string word;  // non-empty = this node is end of a word
};

class Solution {
    void dfs(vector<vector<char>>& g, TrieNode* node,
             int r, int c, vector<string>& res) {
        if (r<0||r>=(int)g.size()||c<0||c>=(int)g[0].size()) return;
        char ch = g[r][c];
        if (ch=='#' || !node->ch[ch-'a']) return; // visited or no prefix
        node = node->ch[ch-'a'];
        if (!node->word.empty()) {                // found a complete word
            res.push_back(node->word);
            node->word = "";  // de-duplicate
        }
        g[r][c] = '#';  // mark visited
        dfs(g,node,r+1,c,res); dfs(g,node,r-1,c,res);
        dfs(g,node,r,c+1,res); dfs(g,node,r,c-1,res);
        g[r][c] = ch;   // restore
    }
public:
    vector<string> findWords(vector<vector<char>>& board,
                             vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (auto& w : words) {            // build trie
            TrieNode* cur = root;
            for (char c : w) {
                if (!cur->ch[c-'a']) cur->ch[c-'a'] = new TrieNode();
                cur = cur->ch[c-'a'];
            }
            cur->word = w;
        }
        vector<string> res;
        for (int r=0;r<(int)board.size();r++)
            for (int c=0;c<(int)board[0].size();c++)
                dfs(board, root, r, c, res);
        return res;
    }
};
{% endhighlight %}
</div>

      <h3>A.4 — When to Use a Trie</h3>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>Operation</th>
              <th>Trie</th>
              <th>Hash Set</th>
              <th>Sorted Array (binary search)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Insert word</td>
              <td>O(L)</td>
              <td>O(L)</td>
              <td>O(L + log n)</td>
            </tr>
            <tr>
              <td>Exact search</td>
              <td>O(L)</td>
              <td>O(L)</td>
              <td>O(L log n)</td>
            </tr>
            <tr>
              <td>Prefix search</td>
              <td><strong>O(L)</strong></td>
              <td>O(n*L) scan</td>
              <td>O(L log n)</td>
            </tr>
            <tr>
              <td>All words with prefix</td>
              <td><strong>O(L + output)</strong></td>
              <td>O(n*L) scan</td>
              <td>O(L log n + output)</td>
            </tr>
            <tr>
              <td>Space</td>
              <td>O(total chars * 26)</td>
              <td>O(total chars)</td>
              <td>O(total chars)</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="insight-box">
        <h4>Trie Complexity</h4>
        <ul>
          <li><strong>Insert / Search / StartsWith (length L):</strong> O(L) time</li>
          <li><strong>Build Trie from n words avg length L:</strong> O(n*L) time, O(n*L*26) space worst case</li>
          <li><strong>Autocomplete (all words with prefix p):</strong> O(|p| + k) time where k = output size</li>
          <li><strong>Trie vs Hash Set:</strong> Hash set gives O(L) exact lookup. Trie gives O(L) exact lookup PLUS O(L) prefix queries. Use Trie when prefix operations are needed.</li>
        </ul>
      </div>
    </section>

    <!-- TOPIC B: UNION-FIND -->
    <section id="topic-b" class="chapter-section">
      <h2> Topic B — Union-Find (Disjoint Set Union)</h2>

      <h3>B.1 — What Is Union-Find?</h3>
      <p><strong>Union-Find</strong> (also called Disjoint Set Union, DSU) is a data structure that tracks a partition of elements into disjoint sets. It supports two operations in near-constant amortised time: <code>union(a, b)</code> — merge the sets containing a and b — and <code>find(a)</code> — identify which set a belongs to (by its representative).</p>

      <div class="ch-code-wrap">
<pre><code>Union-Find: Union by Rank + Path Compression
  Elements: {0, 1, 2, 3, 4, 5}  Initially each element is its own set.
  parent = [0, 1, 2, 3, 4, 5]   rank = [0, 0, 0, 0, 0, 0]

  union(0, 1):  find(0)=0, find(1)=1. rank equal -> parent[1]=0, rank[0]++.
  union(2, 3):  find(2)=2, find(3)=3. parent[3]=2, rank[2]++.
  union(0, 2):  find(0)=0, find(2)=2. parent[2]=0, rank[0]++.
  parent = [0, 0, 0, 2, 4, 5]

  find(3) with PATH COMPRESSION:
    find(3) -> parent[3]=2 -> parent[2]=0 -> root=0.
    Compress: parent[3] = 0, parent[2] = 0.
    parent = [0, 0, 0, 0, 4, 5]   (3 now directly points to root 0)

  Sets: Set A: {0, 1, 2, 3}   Set B: {4}   Set C: {5}</code></pre>
      </div>

      <h3>B.2 — Union-Find Implementation</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// Union-Find with Union by Rank + Path Compression
// find: amortised O(alpha(n)) ~ O(1)   unite: amortised O(alpha(n))
class UnionFind {
    vector<int> parent, rank_;
    int components;
public:
    UnionFind(int n) : parent(n), rank_(n,0), components(n) {
        iota(parent.begin(), parent.end(), 0); // parent[i] = i
    }

    // Path compression: make every node on the find-path point to root
    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]); // recursive compression
        return parent[x];
    }

    // Union by rank: attach smaller tree under larger tree
    bool unite(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false; // already in same set
        if (rank_[ra] < rank_[rb]) swap(ra, rb);
        parent[rb] = ra;             // attach rb under ra
        if (rank_[ra] == rank_[rb]) rank_[ra]++;
        components--;
        return true;
    }

    bool connected(int a, int b) { return find(a) == find(b); }
    int  count()                 { return components; }
};
{% endhighlight %}
</div>

      <h3>B.3 — Number of Islands Using Union-Find</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 200 — Number of Islands (Union-Find approach)
// Time: O(M*N * alpha(M*N))  Space: O(M*N)
int numIslands(vector<vector<char>>& grid) {
    int m = grid.size(), n = grid[0].size();
    UnionFind uf(m * n);
    int water = 0;
    int dr[] = {0, 1, 0, -1};
    int dc[] = {1, 0, -1, 0};
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (grid[r][c] == '0') { water++; continue; }
            for (int d = 0; d < 4; d++) {
                int nr = r+dr[d], nc = c+dc[d];
                if (nr>=0&&nr<m&&nc>=0&&nc<n&&grid[nr][nc]=='1')
                    uf.unite(r*n+c, nr*n+nc); // merge adjacent land
            }
        }
    }
    return uf.count() - water; // subtract water cells
}
{% endhighlight %}
</div>

      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>Operation</th>
              <th>Time</th>
              <th>Notes</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>find(x) — no optimisation</td>
              <td>O(n) worst</td>
              <td>Linear chain without path compression</td>
            </tr>
            <tr>
              <td>find(x) — path compression only</td>
              <td>O(log n) amortised</td>
              <td>Better but not optimal</td>
            </tr>
            <tr>
              <td>find(x) — union by rank only</td>
              <td>O(log n) worst</td>
              <td>Tree height bounded by log n</td>
            </tr>
            <tr>
              <td>find(x) — <strong>both optimisations</strong></td>
              <td><strong>O(alpha(n)) amortised</strong></td>
              <td>Alpha = inverse Ackermann, &lt; 5 for all practical n</td>
            </tr>
            <tr>
              <td>n operations total</td>
              <td>O(n * alpha(n)) ~ O(n)</td>
              <td>Entire DSU effectively linear</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- TOPIC C: MONOTONIC STACK -->
    <section id="topic-c" class="chapter-section">
      <h2> Topic C — Monotonic Stack</h2>

      <h3>C.1 — What Is a Monotonic Stack?</h3>
      <p>A <strong>monotonic stack</strong> is a stack that maintains its elements in either strictly increasing or strictly decreasing order from bottom to top. When a new element is pushed, elements that violate the monotone property are popped first. This gives <strong>O(n) solutions</strong> to problems that naively require O(n²) nested loops.</p>

      <div class="ch-code-wrap">
<pre><code>Monotonic Stack: Next Greater Element Trace
  Array: [2, 1, 5, 6, 2, 3]
  Goal: find Next Greater Element (NGE) for each index.

  Use a DECREASING monotonic stack. Stack stores INDICES.
  When we pop index j because nums[i] > nums[j], nums[i] is the NGE for j.

  i=0: nums[0]=2. Stack empty. Push 0.        stack=[0]    (values: [2])
  i=1: nums[1]=1. 1 < nums[top]=2 -> push 1.  stack=[0,1]  (values: [2,1])
  i=2: nums[2]=5. 5 > nums[1]=1 -> pop 1, NGE[1]=5.
                   5 > nums[0]=2 -> pop 0, NGE[0]=5.
                   Stack empty. Push 2.        stack=[2]    (values: [5])
  i=3: nums[3]=6. 6 > nums[2]=5 -> pop 2, NGE[2]=6. Push 3.
  i=4: nums[4]=2. 2 < nums[3]=6 -> push 4.    stack=[3,4]
  i=5: nums[5]=3. 3 > nums[4]=2 -> pop 4, NGE[4]=3. Push 5.
  End: remaining {3,5} have no NGE -> NGE[3]=NGE[5]=-1.

  Result: NGE = [5, 5, 6, -1, 3, -1]
  Each element pushed and popped at most once -> O(n) total.</code></pre>
      </div>

      <h3>C.2 — Next Greater Element</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// Next Greater Element I (LC 496) — O(n)
vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int,int> nge; // nge[val] = next greater element value
    stack<int> stk;             // decreasing monotonic stack of VALUES
    for (int x : nums2) {
        while (!stk.empty() && stk.top() < x) {
            nge[stk.top()] = x; // x is NGE for stk.top()
            stk.pop();
        }
        stk.push(x);
    }
    vector<int> res;
    for (int x : nums1) res.push_back(nge.count(x) ? nge[x] : -1);
    return res;
}
{% endhighlight %}
</div>

      <h3>C.3 — Daily Temperatures</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LeetCode 739 — Daily Temperatures
// For each day, how many days until a warmer temperature?
// Time: O(n)  Space: O(n)
vector<int> dailyTemperatures(vector<int>& temps) {
    int n = temps.size();
    vector<int> res(n, 0);
    stack<int> stk; // decreasing monotonic stack of indices
    for (int i = 0; i < n; i++) {
        while (!stk.empty() && temps[i] > temps[stk.top()]) {
            int j = stk.top(); stk.pop();
            res[j] = i - j; // days to wait = i - j
        }
        stk.push(i);
    }
    return res; // indices still in stack: res[j]=0 (never warmer)
}
{% endhighlight %}
</div>

      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>Problem</th>
              <th>Stack Type</th>
              <th>Pop trigger</th>
              <th>Answer at pop time</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Next Greater Element</td>
              <td>Decreasing</td>
              <td><code>new &gt; top</code></td>
              <td>NGE = current element</td>
            </tr>
            <tr>
              <td>Next Smaller Element</td>
              <td>Increasing</td>
              <td><code>new &lt; top</code></td>
              <td>NSE = current element</td>
            </tr>
            <tr>
              <td>Daily Temperatures</td>
              <td>Decreasing</td>
              <td><code>new &gt; top</code></td>
              <td>wait = current_idx - popped_idx</td>
            </tr>
            <tr>
              <td>Largest Rectangle</td>
              <td>Increasing</td>
              <td><code>new &lt; top</code></td>
              <td>area = h * calculated_width</td>
            </tr>
            <tr>
              <td>Trapping Rain Water</td>
              <td>Decreasing</td>
              <td><code>new &gt;= top</code></td>
              <td>trapped = (min(L,R)-h)*width</td>
            </tr>
            <tr>
              <td>Remove K Digits</td>
              <td>Increasing</td>
              <td><code>new &lt; top AND k &gt; 0</code></td>
              <td>remove top</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="insight-box">
        <h4>Key Insight</h4>
        <ul>
          <li><strong>DECREASING stack (top is smallest):</strong> use to find NEXT GREATER ELEMENT. Pop when new element &gt; top.</li>
          <li><strong>INCREASING stack (top is largest):</strong> use to find NEXT SMALLER ELEMENT. Pop when new element &lt; top.</li>
          <li><strong>Store INDICES not values</strong> when you need width/distance calculations (Histogram, Trapping Rain Water).</li>
          <li>Each element is pushed once and popped at most once &#8594; O(n) total operations.</li>
        </ul>
      </div>
    </section>

    <!-- TOPIC D: SLIDING WINDOW -->
    <section id="topic-d" class="chapter-section">
      <h2> Topic D — Sliding Window</h2>

      <h3>D.1 — Fixed vs Variable Window</h3>
      <p>The <strong>sliding window</strong> technique maintains a contiguous subarray or substring by moving two pointers. It reduces O(n²) brute-force to O(n) by avoiding recomputation — instead of restarting from scratch, we slide forward: add the new element on the right, remove the old element on the left.</p>

      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>Type</th>
              <th>When to use</th>
              <th>Template shape</th>
              <th>Classic problems</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Fixed window (size k)</strong></td>
              <td>Window size is given</td>
              <td>Advance both ends together</td>
              <td>Max sum subarray of size k, sliding window max</td>
            </tr>
            <tr>
              <td><strong>Variable window (shrink)</strong></td>
              <td>Optimise window size under constraint</td>
              <td>Expand right, shrink left when violated</td>
              <td>Longest substring without repeat, min window substring</td>
            </tr>
          </tbody>
        </table>
      </div>

<div class="ch-code-wrap">
{% highlight cpp %}
// ── FIXED WINDOW: Maximum sum subarray of size k ────────────
// Time: O(n)  Space: O(1)
int maxSumFixed(vector<int>& nums, int k) {
    int sum = 0;
    for (int i = 0; i < k; i++) sum += nums[i];  // initial window
    int best = sum;
    for (int i = k; i < (int)nums.size(); i++) {
        sum += nums[i] - nums[i-k];  // slide: add right, remove left
        best = max(best, sum);
    }
    return best;
}

// ── VARIABLE WINDOW: Longest substring without repeating chars ─
// Time: O(n)  Space: O(min(n, charset))
int lengthOfLongestSubstring(string s) {
    unordered_map<char,int> freq;
    int lo = 0, best = 0;
    for (int hi = 0; hi < (int)s.size(); hi++) {
        freq[s[hi]]++;
        while (freq[s[hi]] > 1) {  // constraint violated: shrink left
            freq[s[lo]]--;
            lo++;
        }
        best = max(best, hi - lo + 1);
    }
    return best;
}

// ── VARIABLE WINDOW: Minimum Window Substring (LC 76) ────────
// Time: O(n)  Space: O(charset)
string minWindow(string s, string t) {
    unordered_map<char,int> need, have;
    for (char c : t) need[c]++;
    int formed = 0, required = need.size();
    int lo = 0, minLen = INT_MAX, start = 0;
    for (int hi = 0; hi < (int)s.size(); hi++) {
        char c = s[hi];
        have[c]++;
        if (need.count(c) && have[c] == need[c]) formed++;
        while (formed == required) {  // valid window: try to shrink
            if (hi - lo + 1 < minLen) { minLen = hi-lo+1; start = lo; }
            have[s[lo]]--;
            if (need.count(s[lo]) && have[s[lo]] < need[s[lo]]) formed--;
            lo++;
        }
    }
    return minLen == INT_MAX ? "" : s.substr(start, minLen);
}
{% endhighlight %}
</div>
    </section>

    <!-- TOPIC E: TWO POINTERS -->
    <section id="topic-e" class="chapter-section">
      <h2> Topic E — Two Pointers</h2>

      <h3>E.1 — Two Pointer Patterns</h3>
      <p><strong>Two pointers</strong> uses two indices that move through a data structure, typically towards each other or in the same direction. This eliminates the inner loop of an O(n²) solution when the data has monotone properties (sorted array, or a constraint that improves/worsens as pointers move).</p>

      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>Pattern</th>
              <th>Pointer motion</th>
              <th>Classic problems</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Opposite ends (converge)</strong></td>
              <td>lo starts left, hi starts right; move toward each other</td>
              <td>Two Sum (sorted), Container With Most Water, 3Sum</td>
            </tr>
            <tr>
              <td><strong>Same direction (fast/slow)</strong></td>
              <td>Both move left-to-right at different speeds</td>
              <td>Remove duplicates, find middle of linked list, cycle detection</td>
            </tr>
            <tr>
              <td><strong>Partition</strong></td>
              <td>lo tracks write position, hi reads</td>
              <td>Dutch National Flag, partition for QuickSort</td>
            </tr>
          </tbody>
        </table>
      </div>

<div class="ch-code-wrap">
{% highlight cpp %}
// ── OPPOSITE ENDS: Two Sum on sorted array ──────────────────
// Time: O(n)  Space: O(1)
vector<int> twoSumSorted(vector<int>& nums, int target) {
    int lo = 0, hi = (int)nums.size()-1;
    while (lo < hi) {
        int sum = nums[lo] + nums[hi];
        if      (sum == target) return {lo+1, hi+1}; // 1-indexed
        else if (sum <  target) lo++;  // need larger sum
        else                   hi--;  // need smaller sum
    }
    return {};
}

// ── SAME DIRECTION: Remove duplicates from sorted array ──────
// Time: O(n)  Space: O(1)
int removeDuplicates(vector<int>& nums) {
    int lo = 0;  // write pointer
    for (int hi = 1; hi < (int)nums.size(); hi++) {
        if (nums[hi] != nums[lo]) {  // new unique element
            lo++;
            nums[lo] = nums[hi];
        }
    }
    return lo + 1; // new length
}

// ── FAST/SLOW: Floyd's cycle detection ───────────────────────
// Time: O(n)  Space: O(1)
bool hasCycle(ListNode* head) {
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;  // cycle detected
    }
    return false;
}
{% endhighlight %}
</div>
    </section>

    <!-- SOLVED PROBLEM 1 -->
    <section id="solved-1" class="chapter-section">
      <h2> Solved Problem 1: Implement Trie (Prefix Tree)</h2>
      <p>Implement a Trie supporting <code>insert(word)</code>, <code>search(word)</code>, and <code>startsWith(prefix)</code>. (LeetCode 208 — Medium)</p>

      <div class="insight-box">
        <h4>OBSERVATIONS</h4>
        <ul>
          <li>Each node has 26 children (one per lowercase letter) and a boolean <code>isEnd</code> flag. Traversal always takes O(L) steps.</li>
          <li><code>search()</code> requires <code>isEnd=true</code> at the final node. <code>startsWith()</code> only requires the path to exist.</li>
          <li><strong>Common mistake:</strong> returning true in <code>search()</code> as soon as the path exists without checking <code>isEnd</code>. 'app' exists as a path even if only 'apple' was inserted.</li>
        </ul>
      </div>

<div class="ch-code-wrap">
{% highlight cpp %}
class Trie {
    struct Node {
        Node* ch[26] = {};
        bool isEnd = false;
    };
    Node* root = new Node();

    Node* traverse(const string& s) {  // returns node after last char or null
        Node* cur = root;
        for (char c : s) {
            if (!cur->ch[c-'a']) return nullptr;
            cur = cur->ch[c-'a'];
        }
        return cur;
    }
public:
    void insert(string word) {
        Node* cur = root;
        for (char c : word) {
            if (!cur->ch[c-'a']) cur->ch[c-'a'] = new Node();
            cur = cur->ch[c-'a'];
        }
        cur->isEnd = true;
    }
    bool search(string word) {
        Node* end = traverse(word);
        return end && end->isEnd;   // path exist AND complete word
    }
    bool startsWith(string prefix) {
        return traverse(prefix) != nullptr; // path existence is sufficient
    }
};
{% endhighlight %}
</div>
      <p><strong>Complexity:</strong> Time O(L) per operation, Space O(total_chars * 26)</p>
    </section>

    <!-- SOLVED PROBLEM 2 -->
    <section id="solved-2" class="chapter-section">
      <h2> Solved Problem 2: Number of Connected Components</h2>
      <p>Given n nodes (0 to n-1) and a list of undirected edges, return the number of connected components. (LeetCode 323 — Medium)</p>

      <div class="insight-box">
        <h4>OBSERVATIONS</h4>
        <ul>
          <li>Classic Union-Find application: initialise n components (each node is its own set), then for each edge union the two endpoints. Final component count = answer.</li>
          <li>Alternative: BFS/DFS counting visited components. Both O(V+E). Union-Find is cleaner for dynamic edge-addition scenarios.</li>
          <li>Every time <code>unite(a,b)</code> successfully merges two different sets, the component count decreases by 1. Start from n, apply all edges.</li>
        </ul>
      </div>

<div class="ch-code-wrap">
{% highlight cpp %}
class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<int> parent(n), rank_(n, 0);
        iota(parent.begin(), parent.end(), 0);

        function<int(int)> find = [&](int x) -> int {
            if (parent[x] != x) parent[x] = find(parent[x]); // path compress
            return parent[x];
        };

        int components = n;
        for (auto& e : edges) {
            int ra = find(e[0]), rb = find(e[1]);
            if (ra == rb) continue; // already connected: skip
            if (rank_[ra] < rank_[rb]) swap(ra, rb);
            parent[rb] = ra;
            if (rank_[ra] == rank_[rb]) rank_[ra]++;
            components--;
        }
        return components;
    }
};
{% endhighlight %}
</div>
      <p><strong>Complexity:</strong> Time O((V+E) * alpha(V)), Space O(V)</p>
    </section>

    <!-- SOLVED PROBLEM 3 -->
    <section id="solved-3" class="chapter-section">
      <h2> Solved Problem 3: Largest Rectangle in Histogram</h2>
      <p>Given an array of bar heights representing a histogram, return the area of the largest rectangle. (LeetCode 84 — Hard)</p>

      <div class="insight-box">
        <h4>OBSERVATIONS</h4>
        <ul>
          <li>For each bar, the largest rectangle using that bar as the shortest has height = heights[i] and extends left and right as far as all bars are &gt;= heights[i].</li>
          <li><strong>Brute force:</strong> For each pair (i,j), compute min height × width. O(n²). TLE for large n.</li>
          <li><strong>Monotonic stack insight:</strong> Maintain an increasing stack of indices. When we encounter a bar shorter than the stack top, the top bar is the shortest in its maximal range — compute its area immediately.</li>
          <li><strong>Width calculation:</strong> when popping index j at trigger i, width = i - stack.top() - 1 (or just i if stack is empty).</li>
          <li><strong>Sentinel:</strong> append 0 to heights to force all bars to pop at the end.</li>
        </ul>
      </div>

<div class="ch-code-wrap">
{% highlight cpp %}
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(0);  // sentinel forces complete flush
        stack<int> stk;        // increasing monotonic stack of indices
        int maxArea = 0;
        for (int i = 0; i < (int)heights.size(); i++) {
            while (!stk.empty() && heights[i] < heights[stk.top()]) {
                int h = heights[stk.top()]; stk.pop();
                // Width: from after current stack top to just before i
                int w = stk.empty() ? i : i - stk.top() - 1;
                maxArea = max(maxArea, h * w);
            }
            stk.push(i);
        }
        return maxArea;
    }
};
{% endhighlight %}
</div>
      <p><strong>Complexity:</strong> Time O(n), Space O(n)</p>
    </section>

    <!-- SECTION: COMPLEXITY REFERENCE -->
    <section id="complexity" class="chapter-section">
      <h2> Complexity Reference — All Bonus Topics</h2>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>Data Structure / Algorithm</th>
              <th>Operation</th>
              <th>Time</th>
              <th>Space</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Trie</td>
              <td>Insert / Search / StartsWith</td>
              <td>O(L)</td>
              <td>O(n*L*26)</td>
            </tr>
            <tr>
              <td>Trie</td>
              <td>Build from n words</td>
              <td>O(n*L)</td>
              <td>O(n*L*26)</td>
            </tr>
            <tr>
              <td>Union-Find (both optimisations)</td>
              <td>find / unite</td>
              <td>O(alpha(n)) ~ O(1)</td>
              <td>O(n)</td>
            </tr>
            <tr>
              <td>Monotonic Stack</td>
              <td>Next Greater/Smaller Element</td>
              <td>O(n)</td>
              <td>O(n)</td>
            </tr>
            <tr>
              <td>Monotonic Stack</td>
              <td>Largest Rectangle in Histogram</td>
              <td>O(n)</td>
              <td>O(n)</td>
            </tr>
            <tr>
              <td>Sliding Window (fixed)</td>
              <td>Max/min over window of size k</td>
              <td>O(n)</td>
              <td>O(1)</td>
            </tr>
            <tr>
              <td>Sliding Window (variable)</td>
              <td>Longest/shortest window under constraint</td>
              <td>O(n)</td>
              <td>O(charset)</td>
            </tr>
            <tr>
              <td>Two Pointers (converge)</td>
              <td>Two Sum on sorted array</td>
              <td>O(n)</td>
              <td>O(1)</td>
            </tr>
            <tr>
              <td>Two Pointers (fast/slow)</td>
              <td>Cycle detection, find middle</td>
              <td>O(n)</td>
              <td>O(1)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION: INTERVIEW QUESTIONS -->
    <section id="interview" class="chapter-section">
      <h2> Common Interview Questions</h2>
      <div class="table-responsive">
        <table class="insight-table">
          <thead>
            <tr>
              <th>Topic</th>
              <th>Problem</th>
              <th>Key Detail</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td rowspan="5"><strong>Trie</strong></td>
              <td>Implement Trie (LC 208)</td>
              <td>insert, search, startsWith</td>
            </tr>
            <tr>
              <td>Design Add and Search Words (LC 211)</td>
              <td>Trie with wildcard '.' DFS</td>
            </tr>
            <tr>
              <td>Word Search II (LC 212)</td>
              <td>Trie + DFS backtracking on grid</td>
            </tr>
            <tr>
              <td>Replace Words (LC 648)</td>
              <td>Trie prefix replacement in sentence</td>
            </tr>
            <tr>
              <td>Maximum XOR of Two Numbers (LC 421)</td>
              <td>Binary Trie (30 levels)</td>
            </tr>
            <tr>
              <td rowspan="5"><strong>Union-Find</strong></td>
              <td>Number of Connected Components (LC 323)</td>
              <td>Classic DSU application</td>
            </tr>
            <tr>
              <td>Redundant Connection (LC 684)</td>
              <td>First edge creating a cycle</td>
            </tr>
            <tr>
              <td>Graph Valid Tree (LC 261)</td>
              <td>n-1 edges + 1 component</td>
            </tr>
            <tr>
              <td>Accounts Merge (LC 721)</td>
              <td>Union on shared emails</td>
            </tr>
            <tr>
              <td>Number of Islands (LC 200)</td>
              <td>BFS or Union-Find on grid</td>
            </tr>
            <tr>
              <td rowspan="5"><strong>Monotonic Stack</strong></td>
              <td>Daily Temperatures (LC 739)</td>
              <td>Days until warmer, decreasing stack</td>
            </tr>
            <tr>
              <td>Next Greater Element I (LC 496)</td>
              <td>NGE with hash map + stack</td>
            </tr>
            <tr>
              <td>Largest Rectangle in Histogram (LC 84)</td>
              <td>Increasing stack, O(n)</td>
            </tr>
            <tr>
              <td>Maximal Rectangle (LC 85)</td>
              <td>Histogram per row + LC 84</td>
            </tr>
            <tr>
              <td>Trapping Rain Water (LC 42)</td>
              <td>Monotonic stack or two pointers</td>
            </tr>
            <tr>
              <td rowspan="5"><strong>Sliding Window</strong></td>
              <td>Maximum Average Subarray (LC 643)</td>
              <td>Fixed window of size k</td>
            </tr>
            <tr>
              <td>Longest Substring Without Repeating (LC 3)</td>
              <td>Variable window, freq map</td>
            </tr>
            <tr>
              <td>Minimum Window Substring (LC 76)</td>
              <td>Variable window, formed count</td>
            </tr>
            <tr>
              <td>Permutation in String (LC 567)</td>
              <td>Fixed window, freq comparison</td>
            </tr>
            <tr>
              <td>Sliding Window Maximum (LC 239)</td>
              <td>Fixed window, monotonic deque</td>
            </tr>
            <tr>
              <td rowspan="5"><strong>Two Pointers</strong></td>
              <td>Two Sum II — sorted array (LC 167)</td>
              <td>Converging pointers</td>
            </tr>
            <tr>
              <td>3Sum (LC 15)</td>
              <td>Sort + two pointers for each fixed element</td>
            </tr>
            <tr>
              <td>Container With Most Water (LC 11)</td>
              <td>Always move the shorter pointer</td>
            </tr>
            <tr>
              <td>Linked List Cycle II (LC 142)</td>
              <td>Floyd's algorithm, find cycle entry</td>
            </tr>
            <tr>
              <td>Sort Colors / Dutch Flag (LC 75)</td>
              <td>3-way partition, lo/mid/hi pointers</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="insight-box">
        <h4>Chapter 11 — Key Takeaways</h4>
        <ul>
          <li><strong>TRIE:</strong> O(L) insert/search/prefix-check regardless of dictionary size. Children array [26] + isEnd flag. Use when prefix queries are needed.</li>
          <li><strong>UNION-FIND:</strong> near-O(1) amortised connectivity queries. Path compression + union by rank together give O(alpha(n)). Use for dynamic connectivity, cycle detection, and component counting.</li>
          <li><strong>MONOTONIC STACK:</strong> O(n) Next Greater/Smaller Element and histogram problems. Store indices (not values) when width/distance is needed.</li>
          <li><strong>SLIDING WINDOW:</strong> O(n) for subarray/substring optimisation. Fixed window: slide both ends. Variable window: expand right, shrink left when constraint violated.</li>
          <li><strong>TWO POINTERS:</strong> O(n) on sorted arrays or linked lists. Converging pointers for sum problems; fast/slow for cycle detection; partition for in-place array reorganisation.</li>
          <li><strong>Pattern selection:</strong> prefix queries &#8594; Trie. Dynamic connectivity &#8594; Union-Find. Next greater in O(n) &#8594; Monotonic Stack. Optimal contiguous window &#8594; Sliding Window. O(n) on sorted structure &#8594; Two Pointers.</li>
        </ul>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- CHAPTER NAVIGATION                         -->
    <!-- ========================================== -->
    <div class="chapter-nav-footer">
      <a href="/learning/dsa/dynamic-programming/ch10-dynamic-programming/" class="ch-nav-footer-btn">← Prev: Ch10 Dynamic Programming</a>
      <a href="/learning/dsa/ch12-cheat-sheet/" class="ch-nav-footer-btn">Next: Ch12 Interview Cheat Sheet →</a>
    </div>

</div>
