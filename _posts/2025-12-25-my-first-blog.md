---
layout: post
title: "Sample Blog"
date: 2025-12-25 00:00:00 +0000
author: Calculusphile
categories: general
permalink: /blogs/my-first-blog.html
---

<div class="project-card">
  <h2 style="margin-bottom:0.25rem;">Sample Blog</h2>
  <p style="margin-top:0; color:var(--light-text);">Designing clean posts with readable sections, code samples and takeaways.</p>
</div>

> Welcome — this is a small demo blog showing a pretty layout using existing site styles.

## Introduction

I like building small, focused write-ups that explain an idea clearly. This sample demonstrates:

- A hero card with brief summary
- Clear headings and readable paragraphs
- Highlighted code blocks and inline code
- A short conclusion with next steps

## Quick Code Example

Here's a small C++ snippet to find the middle of a linked list (fast & slow pointers):

```cpp
ListNode* middleNode(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}
```

## Visual Tip

Use short paragraphs and lists to break information into digestible chunks. Add a screenshot or diagram when the idea is more visual.

## Takeaways

- Keep examples small and focused.
- Use syntax-highlighted code blocks for clarity.
- Link to related projects or posts for deeper reading.

[See linked-list implementation →]({{ '/learning/dsa/LinkedList/leetcode-876.cpp' | relative_url }})

---

*Published with ❤️ by Calculusphile*

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/blogs' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← All Blogs</a>
  <a href="{{ '/' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Home 🏠</a>
</div>
