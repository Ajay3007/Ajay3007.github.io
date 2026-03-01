---
layout: default
title: Heaps
permalink: /learning/dsa/heaps/
---

# 🏔️ Heaps (Priority Queues)

Min-heap: parent ≤ children. **O(log n) push/pop. O(1) peek.** C++ `priority_queue` defaults to max-heap — use `greater<int>` for min-heap.

---

## Core Patterns

| Pattern | Approach | Example |
|---------|----------|---------|
| **Top K largest** | Min-heap of size K | Keep K largest, peek = Kth |
| **Top K smallest** | Max-heap of size K | Keep K smallest |
| **K-way merge** | Push (val, list, idx) | Merge K sorted lists |
| **Running median** | Max-heap (lower) + min-heap (upper) | Median of data stream |

## Templates

```cpp
// Min-heap
priority_queue<int, vector<int>, greater<int>> minH;

// Top-K largest elements (min-heap of size K)
priority_queue<int, vector<int>, greater<int>> pq;
for (int x : nums) {
    pq.push(x);
    if ((int)pq.size() > k) pq.pop();
}
// pq.top() = Kth largest

// Custom comparator (min-heap by first element of pair)
auto cmp = [](pair<int,int>& a, pair<int,int>& b){ return a.first > b.first; };
priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(cmp)> pq(cmp);
```

## Complexity

| Operation | Time |
|-----------|------|
| Push / Pop | O(log n) |
| Peek (top) | O(1) |
| Build heap from array | O(n) |

---

<div class="topic-crosslinks">
  <a href="{{ '/learning/dsa/heaps/heaps-problems/' | relative_url }}" class="topic-hub-link topic-hub-link--primary">📋 Practice Problems →</a>
  <a href="{{ '/learning/dsa/' | relative_url }}" class="topic-hub-link">← DSA Hub</a>
  <a href="{{ '/roadmap/#ch6' | relative_url }}" class="topic-hub-link">📍 Roadmap Ch 6</a>
</div>
