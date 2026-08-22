---
title: "Symmetrical Tree Solution"
description: "Recursive Mirror Comparison of Left and Right Subtrees LeetCode 101 Difficulty: Easy Intuition A binary tree is symmetric if its left and right subtrees are mirror images of…"
problem_id: "101"
date: 2026-03-04
url: /editorials/symmetrical-tree/
---

# Recursive Mirror Comparison of Left and Right Subtrees

**LeetCode #101** | **Difficulty:** Easy

## Intuition
A binary tree is symmetric if its left and right subtrees are mirror images of each other.

For two nodes to be mirrors:
1. Their values must be equal.
2. The left child of one node must match the right child of the other.
3. The right child of one node must match the left child of the other.

This suggests a natural recursive solution where we simultaneously traverse the left subtree and the mirrored side of the right subtree.

## Approach
1. Create a helper function `isMirror(left, right)` that checks whether two subtrees are mirrors.

2. Base cases:
   - If both nodes are `nullptr`, the trees are symmetric → return `true`.
   - If only one is `nullptr`, they are not symmetric → return `false`.

3. Check current nodes:
   - Values must be equal.
   - Recursively verify:
     - `left->left` with `right->right`
     - `left->right` with `right->left`

4. In `isSymmetric()`:
   - If the root is `nullptr`, the tree is symmetric.
   - Otherwise call `isMirror(root->left, root->right)`.

This ensures the tree is checked level-by-level in a mirrored fashion.

## Complexity
- Time complexity:
  $$O(n)$$

  Each node in the tree is visited exactly once.

- Space complexity:
  $$O(h)$$

  Where `h` is the height of the tree due to the recursion stack.
  In the worst case (skewed tree) this becomes `O(n)`.

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
    bool isMirror(TreeNode* left, TreeNode* right) {
        if(!left && !right) return true;
        if(!left || !right) return false;
        return (left->val == right->val) && isMirror(left->left, right->right) &&
                isMirror(left->right, right->left);
    }

    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        return isMirror(root->left, root->right);
    }
};
```

## Visual Intuition

A tree is symmetric if the **left subtree is a mirror reflection of the right subtree**.

<svg width="640" height="340" xmlns="http://www.w3.org/2000/svg">

<!-- Root -->
<circle cx="320" cy="40" r="22" stroke="black" fill="white"/>
<text x="320" y="46" text-anchor="middle" font-size="14">1</text>

<!-- Level 2 -->
<circle cx="200" cy="120" r="22" stroke="black" fill="white"/>
<text x="200" y="126" text-anchor="middle" font-size="14">2</text>

<circle cx="440" cy="120" r="22" stroke="black" fill="white"/>
<text x="440" y="126" text-anchor="middle" font-size="14">2</text>

<!-- Level 3 -->
<circle cx="120" cy="210" r="22" stroke="black" fill="white"/>
<text x="120" y="216" text-anchor="middle" font-size="14">3</text>

<circle cx="280" cy="210" r="22" stroke="black" fill="white"/>
<text x="280" y="216" text-anchor="middle" font-size="14">4</text>

<circle cx="360" cy="210" r="22" stroke="black" fill="white"/>
<text x="360" y="216" text-anchor="middle" font-size="14">4</text>

<circle cx="520" cy="210" r="22" stroke="black" fill="white"/>
<text x="520" y="216" text-anchor="middle" font-size="14">3</text>

<!-- Edges -->
<line x1="320" y1="62" x2="200" y2="98" stroke="black"/>
<line x1="320" y1="62" x2="440" y2="98" stroke="black"/>

<line x1="200" y1="142" x2="120" y2="188" stroke="black"/>
<line x1="200" y1="142" x2="280" y2="188" stroke="black"/>

<line x1="440" y1="142" x2="360" y2="188" stroke="black"/>
<line x1="440" y1="142" x2="520" y2="188" stroke="black"/>

<!-- Mirror axis -->
<line x1="320" y1="10" x2="320" y2="300" stroke="gray" stroke-dasharray="6,6"/>

<!-- Comparison arrows -->
<line x1="120" y1="250" x2="520" y2="250" stroke="red" stroke-width="2"/>
<text x="320" y="245" text-anchor="middle" font-size="13" fill="red">mirror pair</text>

<line x1="280" y1="285" x2="360" y2="285" stroke="red" stroke-width="2"/>
<text x="320" y="280" text-anchor="middle" font-size="13" fill="red">mirror pair</text>

</svg>

### Recursive Mirror Comparison

Your recursion checks nodes in this mirrored order:

```
isMirror(left, right)

1. left.val == right.val
2. isMirror(left->left , right->right)
3. isMirror(left->right, right->left)
```

Mirror pairs checked:

```
(2,2)
(3,3)
(4,4)
```

If all mirrored pairs match, the tree is **symmetric**.


# Iterative BFS Using Queue to Compare Mirror Nodes

## Intuition
A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree.

Instead of recursion, we can simulate the mirror comparison using a **queue**.  
At every step we compare two nodes that should be mirrors of each other.

For two nodes to be mirrors:
1. Their values must be equal.
2. The left child of the first node must match the right child of the second.
3. The right child of the first node must match the left child of the second.

Using BFS, we push node pairs into the queue and verify the mirror property level by level.

## Approach
1. If the root is `nullptr`, the tree is symmetric.

2. Initialize a queue and push:
   ```
   (root->left, root->right)
   ```

3. While the queue is not empty:
   - Pop two nodes `left` and `right`.

   **Case 1:**  
   If both are `nullptr`, continue.

   **Case 2:**  
   If only one is `nullptr`, the tree is not symmetric → return `false`.

   **Case 3:**  
   If their values are different → return `false`.

4. Push their children in mirror order:
   ```
   left->left  with right->right
   left->right with right->left
   ```

5. If the queue finishes without mismatches, the tree is symmetric.

## Complexity

- Time complexity:  
  $$O(n)$$  

  Every node is processed once.

- Space complexity:  
  $$O(n)$$  

  In the worst case the queue may store nodes from an entire level of the tree.

## Code
```cpp
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;

        queue<TreeNode*> q;
        q.push(root->left);
        q.push(root->right);

        while(!q.empty()) {
            TreeNode* left = q.front(); q.pop();
            TreeNode* right = q.front(); q.pop();

            if(!left && !right) continue;
            if(!left || !right) return false;
            if(left->val != right->val) return false;

            q.push(left->left);
            q.push(right->right);

            q.push(left->right);
            q.push(right->left);
        }

        return true;
    }
};
```
