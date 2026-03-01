---
layout: default
title: Bit Manipulation
permalink: /learning/dsa/bit-manipulation/
---

# ⚙️ Bit Manipulation

Bit operations work directly on binary representations. **O(1) per operation.** Essential for competitive programming and low-level optimizations.

---

## Core Operations

| Operation | Syntax | Use Case |
|-----------|--------|----------|
| **AND** | `a & b` | Mask bits, check if even (`n & 1 == 0`) |
| **OR** | `a \| b` | Set bits |
| **XOR** | `a ^ b` | Toggle bits, find unique element |
| **NOT** | `~a` | Flip all bits |
| **Left shift** | `a << k` | Multiply by 2^k |
| **Right shift** | `a >> k` | Divide by 2^k |

## Key Tricks

| Trick | Expression | Notes |
|-------|------------|-------|
| Check bit i | `(n >> i) & 1` | Returns 0 or 1 |
| Set bit i | `n \| (1 << i)` | |
| Clear bit i | `n & ~(1 << i)` | |
| Count set bits | `__builtin_popcount(n)` | Or Brian Kernighan: `n &= n-1` |
| Is power of 2 | `n > 0 && (n & (n-1)) == 0` | |
| XOR cancels duplicates | `a ^ a == 0`, `a ^ 0 == a` | Find single number |

## Templates

```cpp
// Count set bits (Brian Kernighan)
int countBits(int n) {
    int count = 0;
    while (n) { n &= n - 1; count++; }
    return count;
}

// Single Number — XOR all elements
int singleNumber(vector<int>& nums) {
    int res = 0;
    for (int x : nums) res ^= x;
    return res;
}

// Check power of two
bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}
```

## Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Any bit op | O(1) | O(1) |
| Count bits (Kernighan) | O(k) — k = set bits | O(1) |
| DP count bits (0..n) | O(n) | O(n) |

---

<div class="topic-crosslinks">
  <a href="{{ '/learning/dsa/bit-manipulation/bit-manipulation-problems/' | relative_url }}" class="topic-hub-link topic-hub-link--primary">📋 Practice Problems →</a>
  <a href="{{ '/learning/dsa/' | relative_url }}" class="topic-hub-link">← DSA Hub</a>
  <a href="{{ '/roadmap/#ch11' | relative_url }}" class="topic-hub-link">📍 Roadmap Ch 11</a>
</div>
