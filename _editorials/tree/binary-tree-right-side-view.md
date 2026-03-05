---
permalink: /editorials/binary-tree-right-side-view/
layout: editorial
title: "Binary Tree Right Side View Solution"
problem_id: "199"
date: 2026-03-04T10:24:48.323Z
---

# Right-First BFS Level Order Traversal

**LeetCode #199** | **Difficulty:** Medium  

# Intuition
From the right side of a binary tree, the visible node at each level is the **rightmost node**.

A common approach is to perform a level order traversal (BFS) and pick the **last node of each level**.  
However, another neat trick is to push the **right child before the left child** into the queue.

By doing this, the **first node processed at every level becomes the rightmost node** of that level.  
So we simply record the first node encountered at each level.

# Approach
1. If the root is `NULL`, return an empty result.
2. Use a **queue** to perform **Breadth First Search (level order traversal)**.
3. Push the root node into the queue.
4. For each level:
   - Determine the number of nodes at that level (`sizeQ`).
   - Iterate through all nodes of that level.
   - The **first node processed (`i == 0`)** is the visible node from the right side, so add it to the result.
5. While pushing children into the queue:
   - Push **right child first**
   - Then **left child**
6. Continue until the queue becomes empty.

This ensures that the first node encountered at each level corresponds to the **rightmost node** of that level.

# Complexity
- Time complexity:
  O(n)

  Each node in the tree is visited exactly once.

- Space complexity:
  O(n)

  The queue can contain up to one full level of the tree in the worst case.

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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if(!root) return result;
        queue<TreeNode*> nodeQ;
        nodeQ.push(root);
        while(!nodeQ.empty()) {
            int sizeQ = nodeQ.size();
            for(int i=0; i<sizeQ; i++) {
                TreeNode* node = nodeQ.front();
                nodeQ.pop();
                if(i==0) result.push_back(node->val);
                if(node->right) nodeQ.push(node->right);
                if(node->left) nodeQ.push(node->left);
            }
        }
        return result;
    }
};
```
