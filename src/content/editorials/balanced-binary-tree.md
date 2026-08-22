---
title: "Balanced Binary Tree Solution"
description: "Recursive Height Check for Every Node (Top-Down Approach) LeetCode 110 Difficulty: Easy Intuition A binary tree is considered balanced if for every node, the height difference…"
problem_id: "110"
date: 2026-03-04
url: /editorials/balanced-binary-tree/
---

# Recursive Height Check for Every Node (Top-Down Approach)

**LeetCode #110** | **Difficulty:** Easy  

## Intuition
A binary tree is considered balanced if for every node, the height difference
between its left and right subtree is not more than 1.

So the idea is straightforward:
- For each node, compute the height of its left subtree.
- Compute the height of its right subtree.
- If their difference is greater than 1, the tree is not balanced.
- Otherwise, recursively check the same condition for the left and right subtrees.

This naturally suggests a recursive solution where we repeatedly compute
subtree heights and verify the balance condition.

## Approach
1. Define a helper function `height(TreeNode* root)`:
   - If the node is `nullptr`, return height `0`.
   - Otherwise return  
     `1 + max(height(root->left), height(root->right))`.

2. In `isBalanced(root)`:
   - If `root` is `nullptr`, the tree is balanced.
   - Compute:
     - `lh = height(root->left)`
     - `rh = height(root->right)`
   - If `abs(lh - rh) > 1`, return `false`.
   - Otherwise recursively check:
     - `isBalanced(root->left)`
     - `isBalanced(root->right)`

3. If all nodes satisfy the balance condition, return `true`.

This approach checks the balance condition at every node in the tree.

## Complexity
- Time complexity:
  
  O(n²)

  For every node we compute the height of its subtree, which can take O(n) time
  in the worst case. Since this happens for each node, the total complexity
  becomes O(n²).

- Space complexity:
  
  O(h)

  Due to recursion stack where `h` is the height of the tree.
  In the worst case (skewed tree), this can be O(n).

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
    int height(TreeNode* root) {
        if(!root) return 0;
        return 1 + max(height(root->left), height(root->right));
    }
    bool isBalanced(TreeNode* root) {
        if(!root) return true;
        int lh = height(root->left);
        int rh = height(root->right);
        if(abs(lh-rh) > 1) return false;
        return isBalanced(root->left) && isBalanced(root->right);
    }
};
```
