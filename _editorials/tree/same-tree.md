---
permalink: /editorials/same-tree/
layout: editorial
title: "Same Tree Solution"
problem_id: "100"
date: 2026-03-03T10:24:48.323Z
---

# Approach 1: Simple Recursive DFS Comparison (Clean & Optimal)

**LeetCode #100** | **Difficulty:** Easy

## Intuition
To determine if two binary trees are the same, we must verify:

1. Both trees have identical structure.
2. Corresponding nodes have equal values.

Since a tree is naturally defined recursively (each node has left and right subtrees),
the most intuitive solution is to compare both trees recursively:

- If both nodes are null → they are equal.
- If one is null and the other is not → not equal.
- If values differ → not equal.
- Otherwise → recursively check left and right subtrees.

This directly mirrors the definition of identical trees.

## Approach
We perform a Depth-First Search (DFS) on both trees simultaneously.

For each pair of nodes (p, q):

1. If both are null → return true.
2. If only one is null → return false.
3. If values differ → return false.
4. Recursively check:
   - Left subtree: `isSameTree(p->left, q->left)`
   - Right subtree: `isSameTree(p->right, q->right)`

If both left and right subtree comparisons return true,
the current subtree is identical.

This ensures:
- Structure equality
- Value equality
- Complete traversal of both trees

## Complexity
- Time complexity:
  O(n)

  We visit each node exactly once.
  Here, n is the number of nodes in the trees.

- Space complexity:
  O(h)

  Due to recursion stack.
  In worst case (skewed tree), h = n.
  In balanced tree, h = log(n).

## Code
```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(!p && !q) return true;
        if(!p || !q) return false;
        if(p->val != q->val) return false;
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```


# Approach 2: Iterative BFS Comparison Using Queue (Level-by-Level Check)

## Intuition
Two binary trees are considered the same if:

1. Their structures are identical.
2. Corresponding nodes have equal values.

So instead of comparing the entire trees at once, we can compare them
node by node.

If at any point:
- One node exists and the other does not → trees differ.
- Node values differ → trees differ.

Otherwise, if we traverse both trees simultaneously and never find a mismatch,
the trees are identical.

## Approach
Instead of using recursion, we perform an iterative Breadth-First Search (BFS).

1. Handle base cases:
   - If one root is null and the other is not → return false.
   - If both are null → return true.

2. Use a queue of pairs:
   - Each element stores corresponding nodes from both trees.
   - Push the root pair into the queue.

3. While the queue is not empty:
   - Pop a pair (node1, node2).
   - If values differ → return false.
   - Check left children:
     - If one exists and the other does not → return false.
     - If both exist → push the pair into queue.
   - Check right children similarly.

4. If traversal completes without mismatch → return true.

This ensures both structure and values are verified simultaneously.

## Complexity
- Time complexity:
  O(n)

  Each node is visited exactly once.

- Space complexity:
  O(n)

  In the worst case (complete binary tree),
  the queue may hold up to O(n) nodes.

## Code
```cpp
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if((!p && q) || (p && !q)) return false;
        if(!p && !q) return true;

        queue<pair<TreeNode*, TreeNode*>> nodeQ;
        nodeQ.push({p, q});

        while(!nodeQ.empty()) {
            TreeNode* node1 = nodeQ.front().first;
            TreeNode* node2 = nodeQ.front().second;
            nodeQ.pop();

            if(node1->val != node2->val) return false;

            if((!node1->left && node2->left) || (node1->left && !node2->left))
                return false;
            if(node1->left && node2->left)
                nodeQ.push({node1->left, node2->left});

            if((!node1->right && node2->right) || (node1->right && !node2->right))
                return false;
            if(node1->right && node2->right)
                nodeQ.push({node1->right, node2->right});
        }

        return true;
    }
};
```