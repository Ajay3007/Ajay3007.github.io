---
layout: default
title: "Ch5 — Trees & Graphs"
permalink: /learning/dsa/tree/ch5-trees-graphs/
custom_css: dsa-chapter
---

<div class="chapter-hero">
  <div class="chapter-hero-inner">
    <div class="ch-hero-breadcrumb">
      <a href="{{ '/roadmap/' | relative_url }}">All Roadmaps</a> ›
      <a href="{{ '/learning/dsa/dsa-roadmap/' | relative_url }}">DSA Mastery</a> ›
      Chapter 5
    </div>
    <div class="chapter-num-badge">Chapter 5 · Intermediate → Advanced · Prereq: Chapter 4</div>
    <h1>Trees & Graphs</h1>
    <p class="chapter-hero-sub">DFS · BFS · Binary Trees · BST Validation · Diameter · LCA · Graph Traversal · Union-Find · Topological Sort — the most structurally rich chapter, unlocking the widest range of interview problems.</p>
    <div class="chapter-meta-row">
      <span class="ch-meta-pill teal">11 Sections</span>
      <span class="ch-meta-pill">16 Practice Problems</span>
      <span class="ch-meta-pill">Intermediate → Advanced</span>
      <a href="{{ '/learning/dsa/dsa-roadmap/#ch5' | relative_url }}" class="ch-nav-btn">← Back to Roadmap</a>
    </div>
  </div>
</div>

<div class="chapter-content">

<!-- ═══════════════════════ Section 1 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 1 — Trees & Graphs: The Big Picture</h2>
<p>Trees and graphs are the most structurally rich data structures in computer science. They model hierarchical and relational data that cannot be represented with arrays or hash maps alone. Mastering DFS and BFS on trees and graphs unlocks a huge range of interview problems.</p>

<h3 class="section-subheading">1.1 — Tree Terminology</h3>
<div class="dsa-pattern-box">
<pre style="font-size:0.82rem;margin:0;color:var(--text-color);">
            1          ← root (depth 0)
          /   \
         2     3       ← internal nodes (depth 1)
        / \     \
       4   5     6     ← leaves (depth 2)
      /
     7                 ← leaf (depth 3)

root:    node with no parent (node 1)
leaf:    node with no children — leaves: 5, 6, 7
height:  longest root-to-leaf path = 3 (1→2→4→7)
depth:   distance from root (root depth = 0)
subtree: node + all descendants (subtree at 2: {2,4,5,7})
</pre>
</div>

<h3 class="section-subheading">1.2 — Graph Terminology</h3>
<div class="insight-box">
  <span class="insight-label">Key Graph Concepts</span>
  <ul>
    <li><strong>Vertices (V):</strong> the nodes; <strong>Edges (E):</strong> the connections.</li>
    <li><strong>Directed (Digraph):</strong> edges have direction (arrows); <strong>Undirected:</strong> edges are bidirectional.</li>
    <li><strong>Cycle:</strong> path that starts and ends at the same vertex.</li>
    <li><strong>DAG:</strong> Directed Acyclic Graph — no cycles; used for dependency ordering (topological sort).</li>
    <li><strong>Connected:</strong> every vertex reachable from every other (undirected graphs).</li>
    <li><strong>Tree vs Graph:</strong> a tree is a connected, acyclic, undirected graph with exactly V–1 edges.</li>
  </ul>
</div>

<h3 class="section-subheading">1.3 — Graph Representations in C++</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// ADJACENCY LIST (preferred for sparse graphs)
// Space: O(V+E) | Add edge: O(1) | Find neighbors: O(degree)
int V = 5;
vector<vector<int>> adj(V);   // adj[u] = list of neighbors
adj[0].push_back(1); adj[1].push_back(0); // undirected: add both
// For weighted graphs:
vector<vector<pair<int,int>>> wadj(V);  // {neighbor, weight}
wadj[0].push_back({1, 5});   // edge 0→1 with weight 5

// ADJACENCY MATRIX (dense graphs or quick edge checks)
// Space: O(V^2) | Check edge (u,v): O(1) | Find neighbors: O(V)
vector<vector<int>> mat(V, vector<int>(V, 0));
mat[0][1] = mat[1][0] = 1;   // undirected edge

// EDGE LIST (Kruskal's MST, sorting edges by weight)
vector<tuple<int,int,int>> edges;  // {weight, u, v}
edges.push_back({5, 0, 1});
{% endhighlight %}
</div>
</div>

<!-- ═══════════════════════ Section 2 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 2 — Tree DFS: Four Traversals</h2>
<p>All four tree traversals are O(n) time and O(h) space (h = tree height = recursion depth). The <em>only</em> difference is <strong>when you process the current node</strong> relative to its children.</p>

<div class="pattern-summary">
  <div class="pattern-card"><h4>Preorder (Root → L → R)</h4><p>Visit root <em>before</em> children. Output: 1,2,4,5,3. Use: copy tree, serialize, expression prefix.</p></div>
  <div class="pattern-card"><h4>Inorder (L → Root → R)</h4><p>Visit root in the <em>middle</em>. Output: 4,2,5,1,3. BST inorder = sorted sequence. Use: validate BST.</p></div>
  <div class="pattern-card"><h4>Postorder (L → R → Root)</h4><p>Visit root <em>after</em> children. Output: 4,5,2,3,1. Use: delete tree, evaluate expression tree, compute height/diameter.</p></div>
  <div class="pattern-card"><h4>Level Order (BFS)</h4><p>Visit level by level (queue). Output: 1,2,3,4,5. Use: shortest path in tree, level processing, zigzag traversal.</p></div>
</div>

<div class="ch-code-wrap">
<span class="ch-code-label">All four traversal templates</span>
{% highlight cpp %}
struct TreeNode { int val; TreeNode *left, *right; };

// Preorder — O(n) time, O(h) space
void preorder(TreeNode* node, vector<int>& res) {
    if (!node) return;
    res.push_back(node->val);     // ROOT first
    preorder(node->left,  res);
    preorder(node->right, res);
}
// Inorder (BST: gives sorted sequence)
void inorder(TreeNode* node, vector<int>& res) {
    if (!node) return;
    inorder(node->left, res);
    res.push_back(node->val);     // ROOT middle
    inorder(node->right, res);
}
// Postorder (compute height, diameter)
void postorder(TreeNode* node, vector<int>& res) {
    if (!node) return;
    postorder(node->left,  res);
    postorder(node->right, res);
    res.push_back(node->val);     // ROOT last
}
// Level Order (BFS)
vector<vector<int>> levelOrder(TreeNode* root) {
    if (!root) return {};
    vector<vector<int>> res;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        int sz = q.size();           // snapshot level size
        vector<int> level;
        while (sz--) {
            TreeNode* n = q.front(); q.pop();
            level.push_back(n->val);
            if (n->left)  q.push(n->left);
            if (n->right) q.push(n->right);
        }
        res.push_back(level);
    }
    return res;
}
{% endhighlight %}
</div>
<div class="ch-cplx-row">
  <span class="ch-cplx"><span>All traversals</span>O(n)</span>
  <span class="ch-cplx"><span>Space (DFS)</span>O(h) call stack</span>
  <span class="ch-cplx"><span>Space (BFS)</span>O(w) — max width</span>
</div>
</div>

<!-- ═══════════════════════ Section 3 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 3 — Tree DFS Patterns</h2>

<h3 class="section-subheading">3.1 — Max Depth (Postorder)</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// Max depth = 1 + max(leftHeight, rightHeight)
int maxDepth(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}
{% endhighlight %}
</div>

<h3 class="section-subheading">3.2 — Diameter (Global Max During Height DFS)</h3>
<div class="insight-box">
  <span class="insight-label">Diameter Insight</span>
  The diameter through any node = leftHeight + rightHeight. Compute this at every node during the height DFS, tracking the global maximum. Return height (for parent's computation) but update diameter as a side effect.
</div>
<div class="ch-code-wrap">
{% highlight cpp %}
int diameter = 0;  // global max — must be initialized to 0, not -1
int height(TreeNode* root) {
    if (!root) return 0;
    int L = height(root->left), R = height(root->right);
    diameter = max(diameter, L + R);  // path through this node
    return 1 + max(L, R);             // height for parent
}
{% endhighlight %}
</div>

<h3 class="section-subheading">3.3 — BST Validation (Pass Min/Max Bounds)</h3>
<div class="insight-box">
  <span class="insight-label">Critical Mistake to Avoid</span>
  Do NOT validate BST by only comparing parent-child pairs. A node must satisfy constraints from ALL ancestors. The value at node 5 must be less than the parent's value AND all the way up to the root's constraint. Always pass (min, max) bounds down.
</div>
<div class="ch-code-wrap">
{% highlight cpp %}
bool isValidBST(TreeNode* root, long lo = LONG_MIN, long hi = LONG_MAX) {
    if (!root) return true;
    if (root->val <= lo || root->val >= hi) return false;
    return isValidBST(root->left,  lo, root->val) &&
           isValidBST(root->right, root->val, hi);
}
{% endhighlight %}
</div>

<h3 class="section-subheading">3.4 — Lowest Common Ancestor</h3>
<div class="ch-code-wrap">
{% highlight cpp %}
// LCA of BST — exploit BST property O(log n) balanced
TreeNode* lcaBST(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (p->val < root->val && q->val < root->val)
        return lcaBST(root->left,  p, q);
    if (p->val > root->val && q->val > root->val)
        return lcaBST(root->right, p, q);
    return root;  // one on each side (or one IS root) → root is LCA
}
// LCA of general binary tree — postorder DFS
TreeNode* lcaGeneral(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root || root == p || root == q) return root;
    TreeNode* left  = lcaGeneral(root->left,  p, q);
    TreeNode* right = lcaGeneral(root->right, p, q);
    if (left && right) return root;  // p and q in different subtrees
    return left ? left : right;
}
{% endhighlight %}
</div>
</div>

<!-- ═══════════════════════ Section 4 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 4 — Graph DFS & BFS</h2>

<div class="insight-box">
  <span class="insight-label">DFS vs BFS — When to Use Each</span>
  <ul>
    <li><strong>DFS:</strong> exploring as far as possible then backtrack. Use for: cycle detection, topological sort, connected components, path existence, tree height/diameter.</li>
    <li><strong>BFS:</strong> level-by-level exploration. Use for: <strong>shortest path in unweighted graph</strong>, level-order traversal, multi-source problems (Rotting Oranges).</li>
    <li><strong>Key BFS rule:</strong> mark nodes visited when <em>enqueued</em>, not when processed. Marking later causes the same node to be enqueued multiple times.</li>
  </ul>
</div>

<div class="ch-code-wrap">
{% highlight cpp %}
// Graph DFS — O(V+E) time, O(V) space
vector<bool> visited(V, false);
void dfs(int node, vector<vector<int>>& adj) {
    visited[node] = true;
    for (int neighbor : adj[node])
        if (!visited[neighbor]) dfs(neighbor, adj);
}

// Graph BFS — O(V+E) time, O(V) space
void bfs(int start, vector<vector<int>>& adj) {
    vector<bool> visited(V, false);
    queue<int> q;
    visited[start] = true;   // mark BEFORE enqueue
    q.push(start);
    while (!q.empty()) {
        int node = q.front(); q.pop();
        for (int neighbor : adj[node])
            if (!visited[neighbor]) {
                visited[neighbor] = true;  // mark BEFORE enqueue
                q.push(neighbor);
            }
    }
}
{% endhighlight %}
</div>
</div>

<!-- ═══════════════════════ Section 5 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 5 — Pattern: Grid DFS (Number of Islands)</h2>
<p>Treat a 2D grid as a graph where each cell is a vertex with up to 4 neighbors (up, down, left, right). DFS from each unvisited land cell, sinking the island as you go.</p>

<div class="dsa-pattern-box">
  <ul>
    <li>Outer loop: iterate all cells (r,c). If cell is '1' → increment islands, start DFS</li>
    <li>DFS: mark cell '0' (sink it) then recurse into 4 neighbors</li>
    <li>Always check bounds AND that cell is '1' before recursing</li>
    <li>Each cell visited at most twice → <strong>O(m×n)</strong> total</li>
  </ul>
</div>

<div class="ch-code-wrap">
{% highlight cpp %}
int numIslands(vector<vector<char>>& grid) {
    int m = grid.size(), n = grid[0].size(), islands = 0;
    // DFS lambda — sinks the island (modifies grid in-place)
    function<void(int,int)> dfs = [&](int r, int c) {
        if (r<0||r>=m||c<0||c>=n||grid[r][c]!='1') return;
        grid[r][c] = '0';  // mark visited by sinking
        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1);
    };
    for (int r = 0; r < m; r++)
        for (int c = 0; c < n; c++)
            if (grid[r][c] == '1') { islands++; dfs(r, c); }
    return islands;
}
// Cannot modify input? Use bool visited[m][n] instead.
{% endhighlight %}
</div>

<div class="ch-cplx-row">
  <span class="ch-cplx"><span>Time</span>O(m×n)</span>
  <span class="ch-cplx"><span>Space</span>O(m×n) DFS stack</span>
</div>
</div>

<!-- ═══════════════════════ Section 6 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 6 — Pattern: Union-Find (Disjoint Set Union)</h2>
<p>Union-Find tracks connected components dynamically. Two optimisations make it nearly O(1) per operation: <strong>path compression</strong> and <strong>union by rank</strong>.</p>

<div class="ch-code-wrap">
{% highlight cpp %}
class UnionFind {
    vector<int> parent, rank;
public:
    UnionFind(int n) : parent(n), rank(n, 0) {
        iota(parent.begin(), parent.end(), 0); // parent[i] = i
    }
    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]); // path compression
        return parent[x];
    }
    bool unite(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;       // already same component
        if (rank[px] < rank[py]) swap(px, py); // union by rank
        parent[py] = px;
        if (rank[px] == rank[py]) rank[px]++;
        return true;
    }
};
// Usage: Redundant Connection — if unite returns false, edge is redundant
{% endhighlight %}
</div>
<div class="ch-cplx-row">
  <span class="ch-cplx"><span>Find / Unite</span>O(α(n)) ≈ O(1)</span>
  <span class="ch-cplx"><span>Space</span>O(V)</span>
</div>
</div>

<!-- ═══════════════════════ Section 7 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 7 — Pattern: Topological Sort (Kahn's Algorithm)</h2>
<p>Topological sort orders vertices of a DAG such that for every directed edge u→v, u comes before v. If a cycle exists, topological sort is impossible.</p>

<div class="ch-code-wrap">
{% highlight cpp %}
// Kahn's Algorithm (BFS-based) — O(V+E) time, O(V) space
vector<int> topoSort(int V, vector<vector<int>>& adj) {
    vector<int> indegree(V, 0);
    for (int u = 0; u < V; u++)
        for (int v : adj[u]) indegree[v]++;
    // Start from all 0-indegree nodes
    queue<int> q;
    for (int i = 0; i < V; i++) if (indegree[i] == 0) q.push(i);
    vector<int> order;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        order.push_back(u);
        for (int v : adj[u])
            if (--indegree[v] == 0) q.push(v); // indegree drops to 0 → ready
    }
    // If order.size() < V, a cycle exists (Course Schedule: return false)
    return order;
}
{% endhighlight %}
</div>
<div class="insight-box">
  <span class="insight-label">Cycle Detection</span>
  If the output order has fewer than V nodes after Kahn's algorithm completes, the graph contains a cycle — topological sort is impossible. LeetCode 207 (Course Schedule) uses this check to return <code>true/false</code>.
</div>
</div>

<!-- ═══════════════════════ Section 8 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 8 — Common Mistakes & Edge Cases</h2>

<div class="pattern-summary">
  <div class="pattern-card"><h4>❌ Null root not handled</h4><p>Always check <code>if (!root) return 0/false/null</code> at the start of every tree function — even before touching <code>root->left</code> or <code>root->right</code>.</p></div>
  <div class="pattern-card"><h4>❌ BST validated by parent-child only</h4><p>A value must satisfy constraints from ALL ancestors, not just its direct parent. Always pass <code>(min, max)</code> bounds down recursively.</p></div>
  <div class="pattern-card"><h4>❌ Height vs Depth confused</h4><p>Height: measured <em>downward</em> to the farthest leaf. Depth: measured <em>upward</em> from root. Max depth = height of tree.</p></div>
  <div class="pattern-card"><h4>❌ BFS: mark when processed not enqueued</h4><p>Mark nodes as visited <em>before</em> pushing to queue. Marking when dequeued causes the same node to be enqueued multiple times → incorrect results or infinite loops.</p></div>
  <div class="pattern-card"><h4>❌ Grid: access before bounds check</h4><p>Always validate <code>r>=0 && r<m && c>=0 && c<n</code> BEFORE accessing <code>grid[r][c]</code>. Out-of-bounds access = undefined behaviour.</p></div>
  <div class="pattern-card"><h4>❌ Union-Find without path compression</h4><p>Without path compression, trees can become deep and <code>find()</code> degrades to O(n). Always use recursive path compression.</p></div>
</div>

<div class="insight-box">
  <span class="insight-label">Edge Cases to Test</span>
  <ul>
    <li>Empty tree (<code>root = null</code>): return 0 depth, empty list for traversal, 0 diameter</li>
    <li>Single node tree: depth = 1, diameter = 0, it is both root and leaf</li>
    <li>Skewed tree (all left children): DFS depth = n — risk of stack overflow for n = 10^5. Use iterative DFS.</li>
    <li>Grid with all water → 0 islands; grid with all land → 1 island</li>
    <li>Disconnected graph: BFS/DFS from one node does NOT reach all nodes. Iterate over ALL unvisited nodes.</li>
  </ul>
</div>
</div>

<!-- ═══════════════════════ Practice Problems ═══════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Practice Problems</h2>

<div class="ch-section-label">Binary Tree Problems</div>
<div class="ch-ed-problems">
<table>
  <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/" target="_blank">104. Maximum Depth of Binary Tree</a></td><td>Postorder DFS</td><td class="diff-easy">Easy</td></tr>
    <tr><td>2</td><td><a href="https://leetcode.com/problems/diameter-of-binary-tree/" target="_blank">543. Diameter of Binary Tree</a></td><td>Global max during height DFS</td><td class="diff-easy">Easy</td></tr>
    <tr><td>3</td><td><a href="https://leetcode.com/problems/balanced-binary-tree/" target="_blank">110. Balanced Binary Tree</a></td><td>Return -1 if unbalanced</td><td class="diff-easy">Easy</td></tr>
    <tr><td>4</td><td><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/" target="_blank">235. LCA of BST</a></td><td>Exploit BST property</td><td class="diff-medium">Medium</td></tr>
    <tr><td>5</td><td><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/" target="_blank">236. LCA of Binary Tree</a></td><td>Postorder DFS — both sides</td><td class="diff-medium">Medium</td></tr>
    <tr><td>6</td><td><a href="https://leetcode.com/problems/binary-tree-level-order-traversal/" target="_blank">102. Binary Tree Level Order Traversal</a></td><td>BFS with level size snapshot</td><td class="diff-medium">Medium</td></tr>
    <tr><td>7</td><td><a href="https://leetcode.com/problems/validate-binary-search-tree/" target="_blank">98. Validate Binary Search Tree</a></td><td>DFS with (min, max) bounds</td><td class="diff-medium">Medium</td></tr>
    <tr><td>8</td><td><a href="https://leetcode.com/problems/kth-smallest-element-in-a-bst/" target="_blank">230. Kth Smallest Element in BST</a></td><td>Inorder traversal, kth element</td><td class="diff-medium">Medium</td></tr>
  </tbody>
</table>
</div>

<div class="ch-section-label" style="margin-top:1.5rem;">Graph Problems</div>
<div class="ch-ed-problems">
<table>
  <thead><tr><th>#</th><th>Problem</th><th>Pattern</th><th>Diff</th></tr></thead>
  <tbody>
    <tr><td>9</td><td><a href="https://leetcode.com/problems/number-of-islands/" target="_blank">200. Number of Islands</a></td><td>Grid DFS — sink land cells</td><td class="diff-medium">Medium</td></tr>
    <tr><td>10</td><td><a href="https://leetcode.com/problems/max-area-of-island/" target="_blank">695. Max Area of Island</a></td><td>DFS returns island size</td><td class="diff-medium">Medium</td></tr>
    <tr><td>11</td><td><a href="https://leetcode.com/problems/clone-graph/" target="_blank">133. Clone Graph</a></td><td>BFS/DFS + hash map for clones</td><td class="diff-medium">Medium</td></tr>
    <tr><td>12</td><td><a href="https://leetcode.com/problems/course-schedule/" target="_blank">207. Course Schedule</a></td><td>Cycle detection — Kahn's</td><td class="diff-medium">Medium</td></tr>
    <tr><td>13</td><td><a href="https://leetcode.com/problems/course-schedule-ii/" target="_blank">210. Course Schedule II</a></td><td>Topological sort order</td><td class="diff-medium">Medium</td></tr>
    <tr><td>14</td><td><a href="https://leetcode.com/problems/pacific-atlantic-water-flow/" target="_blank">417. Pacific Atlantic Water Flow</a></td><td>Reverse BFS from both oceans</td><td class="diff-medium">Medium</td></tr>
    <tr><td>15</td><td><a href="https://leetcode.com/problems/redundant-connection/" target="_blank">684. Redundant Connection</a></td><td>Union-Find cycle detection</td><td class="diff-medium">Medium</td></tr>
    <tr><td>16</td><td><a href="https://leetcode.com/problems/word-ladder/" target="_blank">127. Word Ladder</a></td><td>BFS shortest path — implicit graph</td><td class="diff-hard">Hard</td></tr>
  </tbody>
</table>
</div>
</div>

<!-- ═══════════════════════ Section 9 ═══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 9 — Iterative Traversals &amp; Morris Inorder</h2>
<p>Recursive traversals use O(h) call-stack space. Two alternatives avoid this: <strong>explicit-stack iteration</strong> (still O(h) but heap-allocated) and <strong>Morris Traversal</strong> (O(1) space by temporarily threading the tree).</p>

<h3 class="section-subheading">9.1 — Iterative Preorder (Root → L → R)</h3>
<div class="insight-box">
  <span class="insight-label">Key Idea</span>
  Push root, then repeatedly pop-and-print, pushing <em>right child first</em> so left is processed next (LIFO order gives Root→L→R).
</div>
<div class="ch-code-wrap">
<span class="ch-code-label">Iterative Preorder — O(n) time, O(h) space</span>
{% highlight cpp %}
void preOrder(TreeNode* root) {
    stack<TreeNode*> s;
    TreeNode* cur = root;
    while (cur || !s.empty()) {
        while (cur) {
            cout << cur->val << " ";   // visit ROOT immediately
            s.push(cur);
            cur = cur->left;           // go left
        }
        cur = s.top(); s.pop();
        cur = cur->right;              // backtrack, try right subtree
    }
}
{% endhighlight %}
</div>

<h3 class="section-subheading">9.2 — Iterative Inorder (L → Root → R)</h3>
<div class="insight-box">
  <span class="insight-label">Key Idea</span>
  Same stack pattern as preorder, but <em>print after popping</em> (not while pushing left). This naturally gives left-root-right order, and for a BST produces a <strong>sorted sequence</strong>.
</div>
<div class="ch-code-wrap">
<span class="ch-code-label">Iterative Inorder — O(n) time, O(h) space</span>
{% highlight cpp %}
void inOrder(TreeNode* root) {
    stack<TreeNode*> s;
    TreeNode* cur = root;
    while (cur || !s.empty()) {
        while (cur) {
            s.push(cur);
            cur = cur->left;           // drill left first
        }
        cur = s.top(); s.pop();
        cout << cur->val << " ";       // visit ROOT (left already done)
        cur = cur->right;              // then process right subtree
    }
}
{% endhighlight %}
</div>

<h3 class="section-subheading">9.3 — Morris Inorder Traversal (O(1) Space)</h3>
<div class="insight-box">
  <span class="insight-label">How Morris Traversal Works</span>
  Instead of a stack, Morris threads the <em>inorder predecessor</em>'s right pointer back to the current node — creating a temporary link (thread) to return here after the left subtree finishes. On the second visit the thread is removed and the node is printed. No extra space beyond a few pointers.
</div>
<div class="ch-code-wrap">
<span class="ch-code-label">Morris Inorder — O(n) time, O(1) space</span>
{% highlight cpp %}
void morrisInOrder(TreeNode* root) {
    TreeNode* curr = root;
    while (curr) {
        if (!curr->left) {
            cout << curr->val << " ";  // no left child → print and move right
            curr = curr->right;
        } else {
            // Find inorder predecessor: rightmost node in left subtree
            TreeNode* pred = curr->left;
            while (pred->right && pred->right != curr)
                pred = pred->right;

            if (!pred->right) {        // Thread not created yet
                pred->right = curr;    // create thread back to curr
                curr = curr->left;     // descend left
            } else {                   // Thread already exists → second visit
                pred->right = nullptr; // remove thread (restore tree)
                cout << curr->val << " ";
                curr = curr->right;
            }
        }
    }
}
{% endhighlight %}
</div>
<div class="dsa-pattern-box">
<pre style="font-size:0.82rem;margin:0;color:var(--text-color);">Morris Inorder Traversal walk-through on: [4, 2, 6, 1, 3, 5, 7]

        4
       / \
      2   6
     / \ / \
    1  3 5  7

Step 1: curr=4, pred of 4 is 3 (rightmost of left subtree).
        Thread 3→4. Move curr to 2.
Step 2: curr=2, pred of 2 is 1. Thread 1→2. Move curr to 1.
Step 3: curr=1, no left. Print 1. Move right → follows thread to 2.
Step 4: curr=2, thread found (pred 1→2 exists). Remove thread.
        Print 2. Move right to 3.
Step 5: curr=3, no left. Print 3. Move right → follows thread to 4.
Step 6: curr=4, thread found (pred 3→4). Remove thread.
        Print 4. Move right to 6.
... continues printing 5, 6, 7.

Output: 1 2 3 4 5 6 7  ✓
</pre>
</div>
<div class="ch-cplx-row">
  <span class="ch-cplx"><span>Time</span>O(n)</span>
  <span class="ch-cplx"><span>Space (Morris)</span>O(1) — no stack/recursion</span>
  <span class="ch-cplx"><span>Space (Iterative)</span>O(h) — explicit stack</span>
</div>
</div>

<!-- ═══════════════════════ Section 10 ══════════════════════ -->
<div class="chapter-section">
<h2 class="section-heading">Section 10 — Tree Serialization &amp; Debug Utilities</h2>
<p>These helpers let you build trees from LeetCode-style bracket strings (e.g. <code>"[1,2,3,null,5]"</code>), serialize back to strings, and pretty-print trees visually — invaluable for local testing and debugging.</p>

<h3 class="section-subheading">10.1 — stringToTreeNode (Deserialize)</h3>
<div class="insight-box">
  <span class="insight-label">BFS Construction Algorithm</span>
  Parse the comma-separated input left-to-right. Use a queue of <em>parent nodes waiting for their children</em>. For each parent, consume the next two tokens as left and right child (skip if <code>"null"</code>). This mirrors LeetCode's level-order representation exactly.
</div>
<div class="ch-code-wrap">
<span class="ch-code-label">stringToTreeNode — O(n) time &amp; space</span>
{% highlight cpp %}
void trimLeftTrailingSpaces(string& input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}
void trimRightTrailingSpaces(string& input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}
void trim(string& input) {
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
}

// Parses "[1,2,3,null,5]" → TreeNode*
TreeNode* stringToTreeNode(string input) {
    trim(input);
    input = input.substr(1, input.length() - 2); // strip [ ]
    if (!input.size()) return nullptr;

    stringstream ss; ss.str(input);
    string item;
    getline(ss, item, ',');

    queue<TreeNode*> nodeQ;
    TreeNode* root = new TreeNode(stoi(item));
    nodeQ.push(root);

    while (true) {
        TreeNode* node = nodeQ.front(); nodeQ.pop();

        if (!getline(ss, item, ',')) break;
        trimLeftTrailingSpaces(item);
        if (item != "null") {
            node->left = new TreeNode(stoi(item));
            nodeQ.push(node->left);
        }

        if (!getline(ss, item, ',')) break;
        trimLeftTrailingSpaces(item);
        if (item != "null") {
            node->right = new TreeNode(stoi(item));
            nodeQ.push(node->right);
        }
    }
    return root;
}
{% endhighlight %}
</div>

<h3 class="section-subheading">10.2 — treeNodeToString (Serialize)</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">treeNodeToString — O(n) time &amp; space</span>
{% highlight cpp %}
// Serializes a tree to "[1,2,3,null,5,null,null]" (LeetCode format)
string treeNodeToString(TreeNode* root) {
    if (!root) return "[]";
    string output;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* node = q.front(); q.pop();
        if (!node) { output += "null, "; continue; }
        output += to_string(node->val) + ", ";
        q.push(node->left);
        q.push(node->right);
    }
    return "[" + output.substr(0, output.length() - 2) + "]";
}
{% endhighlight %}
</div>

<h3 class="section-subheading">10.3 — prettyPrintTree (Visual Debugger)</h3>
<div class="insight-box">
  <span class="insight-label">How it Works</span>
  Recursively prints the <em>right</em> subtree first (top of console = rightmost node), then the current node, then the <em>left</em> subtree. Each level is indented with box-drawing characters (<code>└──</code>, <code>┌──</code>, <code>│</code>) to show the tree shape.
</div>
<div class="ch-code-wrap">
<span class="ch-code-label">prettyPrintTree — example output for [4,2,6,1,3,5,7]</span>
{% highlight cpp %}
void prettyPrintTree(TreeNode* node, string prefix = "", bool isLeft = true) {
    if (!node) { cout << "Empty tree"; return; }
    if (node->right)
        prettyPrintTree(node->right, prefix + (isLeft ? "│   " : "    "), false);
    cout << prefix + (isLeft ? "└── " : "┌── ") + to_string(node->val) + "\n";
    if (node->left)
        prettyPrintTree(node->left,  prefix + (isLeft ? "    " : "│   "), true);
}

/*  Output for [4,2,6,1,3,5,7]:
    ┌── 7
│   ┌── 6
│       └── 5
└── 4
    ┌── 3
    └── 2
        └── 1
*/
{% endhighlight %}
</div>

<h3 class="section-subheading">10.4 — Putting It All Together (main driver)</h3>
<div class="ch-code-wrap">
<span class="ch-code-label">Local test driver — reads tree strings from stdin</span>
{% highlight cpp %}
int main() {
    string line;
    while (getline(cin, line)) {
        TreeNode* root = stringToTreeNode(line);
        prettyPrintTree(root);
        cout << "Pre Order:  [ "; preOrder(root);        cout << "]\n";
        cout << "In Order:   [ "; morrisInOrder(root);   cout << "]\n";
        cout << "Post Order: [ "; postOrderTraversal(root); cout << "]\n";
        cout << "Serialized: " << treeNodeToString(root) << "\n\n";
    }
    return 0;
}
// Input example:  [1,2,3,4,5,null,6]
// Pre Order:  [ 1 2 4 5 3 6 ]
// In Order:   [ 4 2 5 1 3 6 ]
// Post Order: [ 4 5 2 6 3 1 ]
{% endhighlight %}
</div>
<div class="ch-cplx-row">
  <span class="ch-cplx"><span>Serialize / Deserialize</span>O(n)</span>
  <span class="ch-cplx"><span>prettyPrintTree</span>O(n)</span>
  <span class="ch-cplx"><span>Space</span>O(n) queue / O(h) recursion</span>
</div>
</div>

</div><!-- end .chapter-content -->

<div class="chapter-nav-footer">
  <a href="{{ '/learning/dsa/stacks/ch4-stacks-queues/' | relative_url }}" class="ch-nav-footer-btn">← Ch4: Stacks & Queues</a>
  <a href="{{ '/learning/dsa/dsa-roadmap/#ch6' | relative_url }}" class="ch-nav-footer-btn primary">Next: Ch6 — Heaps →</a>
</div>
