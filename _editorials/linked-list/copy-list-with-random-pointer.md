---
permalink: /editorials/copy-list-with-random-pointer/
layout: editorial
title: "Copy List with Random Pointer"
problem_id: "138"
date: 2026-02-27T12:23:22.323Z
---

# Two HashMaps (Index Mapping) Approach – O(n) Time | O(n) Space

**LeetCode #138** | **Difficulty:** Medium

## Intuition
Each node has two pointers:
- `next` → normal linked list connection
- `random` → can point to any node in the list (or null)

The main difficulty is correctly assigning the `random` pointers in the new copied list.

To solve this, we need a way to map:
- Original node → Copied node

Instead of directly mapping original node pointer to copied node pointer,
this solution maps nodes using their index positions.

So the idea is:
1. First pass → Create the new list (only next pointers).
2. Store mapping between original nodes and their indices.
3. Store mapping between index and copied nodes.
4. Second pass → Use the stored mappings to correctly assign random pointers.

## Approach

1️⃣ **First Pass – Create the new list (only next pointers)**

- Traverse the original list.
- Create a new node for each original node.
- Maintain two hash maps:
  - `map2`: Original node → index
  - `map1`: index → Copied node
- Link the copied nodes using `next`.

After this pass:
- The structure (next pointers) of the new list is ready.
- Random pointers are still unassigned.

---

2️⃣ **Second Pass – Assign random pointers**

- Traverse both lists simultaneously.
- For each original node:
  - If its random pointer is null → set copied random as null.
  - Otherwise:
    - Get the index of original random node using `map2`.
    - Use that index to get the corresponding copied node from `map1`.
    - Assign copied node’s random pointer.

---

3️⃣ Return the head of the copied list.

This guarantees:
- Deep copy of all nodes
- Correct random pointer mapping
- No modification of original list

## Complexity

- Time complexity:
  O(n)

  First traversal: O(n)  
  Second traversal: O(n)

- Space complexity:
  O(n)

  Two unordered_maps storing n entries each.

## Code
```cpp
/*
 // Definition for a Node.
 class Node {
 public:
     int val;
     Node* next;
     Node* random;
     
     Node(int _val) {
         val = _val;
         next = NULL;
         random = NULL;
     }
 };
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(!head) return nullptr;
        unordered_map<int, Node*> map1;
        unordered_map<Node*, int> map2;
        Node *temp1 = head;
        Node *prev = new Node(temp1->val);
        Node *list2 = prev;
        int index = 0;
        map1[index] = prev;
        map2[temp1] = index;
        while(temp1->next) {
            index++;
            temp1 = temp1->next;
            Node *newNode = new Node(temp1->val);
            prev->next = newNode;
            prev = newNode;
            map1[index] = prev;
            map2[temp1] = index;
        }
        prev->next = nullptr;   // list2 has been created fully but random pointer of each node is still need to be linked
        temp1 = head;   // Pointing list1 head
        prev = list2;   // Pointing list2 head
        while(temp1) {
            prev->random = (temp1->random == nullptr) ? nullptr : map1[map2[temp1->random]];
            temp1 = temp1->next;
            prev = prev->next;
        }
        return list2;
    }
};
```

---

# Optimal Interleaving Technique – O(n) Time | O(1) Extra Space

## Intuition
Instead of using extra space, we can cleverly insert copied nodes
in between original nodes.

Example:

Original:
A → B → C

After inserting copies:
A → A' → B → B' → C → C'

Now:
- Each copied node is right next to its original.
- This helps us assign random pointers without extra space.

## Approach

1️⃣ Insert copied nodes between originals

For each node:
- Create new node.
- Insert it right after the original node.

List becomes:
original → copy → original → copy ...

---

2️⃣ Assign random pointers

If:
original->random = X

Then:
original->next->random = original->random->next

Because:
- original->next is copy node
- original->random->next is copy of random node

---

3️⃣ Separate the two lists

Restore original list and extract copied list.

Traverse:
- Fix original next pointers
- Fix copied next pointers

Return head of copied list.

## Complexity

- Time complexity:
  O(n)

  Three passes over the list.

- Space complexity:
  O(1)

  No extra data structures used.

## Code
```cpp
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;

        // Step 1: Insert copied nodes
        Node* temp = head;
        while (temp) {
            Node* copy = new Node(temp->val);
            copy->next = temp->next;
            temp->next = copy;
            temp = copy->next;
        }

        // Step 2: Assign random pointers
        temp = head;
        while (temp) {
            if (temp->random)
                temp->next->random = temp->random->next;
            temp = temp->next->next;
        }

        // Step 3: Separate lists
        Node* dummy = new Node(0);
        Node* copyTail = dummy;
        temp = head;

        while (temp) {
            Node* copy = temp->next;
            temp->next = copy->next;
            copyTail->next = copy;
            copyTail = copy;
            temp = temp->next;
        }

        return dummy->next;
    }
};
```

---

