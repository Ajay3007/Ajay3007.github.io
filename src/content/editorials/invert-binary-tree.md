---
title: "Invert Binary Tree Solution"
description: "Recursive DFS: Swap Children at Every Node (Classic Tree Inversion) LeetCode 226 Difficulty: Easy Intuition To invert a binary tree, we simply need to swap the left and right…"
problem_id: "226"
date: 2026-03-04
url: /editorials/invert-binary-tree/
---

# Recursive DFS: Swap Children at Every Node (Classic Tree Inversion)

**LeetCode #226** | **Difficulty:** Easy

## Intuition
To invert a binary tree, we simply need to swap the left and right child of every node in the tree.

Since a binary tree is naturally defined recursively (each node is the root of its own subtree), we can apply the same operation to every node:
- Swap its left and right children
- Recursively invert the left subtree
- Recursively invert the right subtree

By doing this for every node, the entire tree gets inverted.

# Approach
We solve the problem using **Depth-First Search (DFS) recursion**.

1. **Base Case**
   - If the current node is `nullptr`, return `nullptr`.
   - If the node is a leaf (both children are `nullptr`), no work is required.

2. **Swap Children**
   - Swap the `left` and `right` pointers of the current node.

3. **Recursive Calls**
   - Recursively invert the left subtree.
   - Recursively invert the right subtree.

4. **Return Root**
   - Return the root after processing the entire subtree.

Because recursion processes every node exactly once, the whole tree gets inverted efficiently.

# Complexity
- Time complexity:
  
  $$O(n)$$
  
  Every node in the tree is visited exactly once.

- Space complexity:
  
  $$O(h)$$
  
  Where **h** is the height of the tree due to recursion stack.
  
  - Worst case (skewed tree): $$O(n)$$
  - Balanced tree: $$O(\log n)$$

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
    TreeNode* invertTree(TreeNode* root) {
        if(root == nullptr || (!root->left && !root->right)) return root;
        swap(root->left, root->right);
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};
```
