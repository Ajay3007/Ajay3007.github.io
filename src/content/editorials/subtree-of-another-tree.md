---
title: "Subtree of Another Tree Solution"
description: "Recursive Tree Matching: Compare Each Node with Subtree LeetCode 572 Difficulty: Medium Intuition To determine whether subRoot is a subtree of root , we observe that a subtree…"
problem_id: "572"
date: 2026-03-04
url: /editorials/subtree-of-another-tree/
---

# Recursive Tree Matching: Compare Each Node with Subtree

**LeetCode #572** | **Difficulty:** Medium  

# Intuition
To determine whether `subRoot` is a subtree of `root`, we observe that a subtree must match **both structure and node values** exactly.

A simple idea is to check every node of the main tree as a potential starting point of the subtree.  
Whenever we encounter a node whose value matches the root of `subRoot`, we verify whether the entire subtree starting from that node is identical to `subRoot`.

Thus, the problem naturally divides into two tasks:
1. Traverse every node of `root`.
2. For each node, check if the two trees are identical.

# Approach
We use two recursive functions:

### 1. Tree Comparison Function
`isSame(s, t)` checks whether two trees are identical.

Steps:
- If both nodes are `NULL`, the trees match → return `true`.
- If only one node is `NULL`, they differ → return `false`.
- If the values are different → return `false`.
- Recursively check left and right children.

### 2. Subtree Search Function
`isSubtree(root, subRoot)` checks whether `subRoot` exists anywhere inside `root`.

Steps:
1. If `root` is `NULL`, subtree cannot exist → return `false`.
2. Check if the trees starting at this node are identical using `isSame`.
3. If yes, return `true`.
4. Otherwise recursively search in:
   - left subtree
   - right subtree

This effectively tries every node as a possible root of the subtree.

# Complexity

- Time complexity:
  
  O(n * m)

  Where:
  - `n` = number of nodes in `root`
  - `m` = number of nodes in `subRoot`

  For each node in `root`, we may compare up to `m` nodes of `subRoot`.

- Space complexity:
  
  O(h)

  Due to recursion stack where `h` is the height of the tree.  
  Worst case (skewed tree): `O(n)`.

# Code
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
    bool isSame(TreeNode* s, TreeNode* t) {
        if(!s && !t) return true;
        if(!s || !t) return false;
        if(s->val != t->val) return false;
        return isSame(s->left, t->left) && isSame(s->right, t->right);
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(!root) return false;
        if(isSame(root, subRoot)) return true;
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};
```
