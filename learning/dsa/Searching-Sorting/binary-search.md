---
layout: default
title: Sorting
permalink: /learning/dsa/Searching-Sorting/binary-search/
---


# ✅ Binary Search (Important)

Most used searching technique in interviews.

**Learn:**

- Basic binary search on sorted array

- Lower bound / Upper bound concepts

- Handling integer overflow (mid = low + (high-low)/2)

- Searching ranges

- Binary search on answers (Advanced)

**You must master:**

- Search in rotated sorted array

- First/last occurrence

- Kth element problems

- Peak element

- Binary search on monotonic functions

## 🔥 Binary Search on Answer (Advanced)

**Used when:**

- Search space is monotonic

- You cannot directly see the sorted array, but decisions are monotonic

**Examples:**

- Allocate books

- Aggressive cows

- Minimum days to make bouquets

- Koko eating bananas


# 📝 Must Do Practice Problems

## 🔹 Level 1 – Easy

1. [Leetcode 704. Binary Search](https://leetcode.com/problems/binary-search/description/){:target="_blank" rel="noopener noreferrer"}

**Solution**

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int left = 0, right = n-1;
        int mid;
        while(left <= right) {
            mid = left + (right - left)/2;
            if(nums[mid] > target) right = mid - 1;
            else if(nums[mid] < target) left = mid + 1;
            else return mid;
        }
        return -1;
    }
};
```

2. [Floor/Ceil of an Element in a Sorted Array - Approach](floorAndCeil.pdf)

3. [Leetcode 35. Search Insert Position](https://leetcode.com/problems/search-insert-position/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach](floorAndCeil.pdf)**

4. [Leetcode 744. Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/){:target="_blank" rel="noopener noreferrer"}

    - This is similar to finding Ceil of an element in a Sorted Array.

```cpp
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int n = letters.size();
        int l = 0, r = n-1, mid, ans = 0;
        while(l <= r) {
            mid = l + (r - l)/2;
            if(letters[mid] > target) {
                ans = mid;
                r = mid - 1;
            } else if(letters[mid] <= target) {
                l = mid + 1;
            }
        }
        return letters[ans];
    }
};
```


5. [Leetcode 169. Majority Element](https://leetcode.com/problems/majority-element/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/majority-element/solutions/7418398/majority-element-step-by-step-intuition-woccs/){:target="_blank" rel="noopener noreferrer"}**




## 🔹 Level 2 – Medium

1. [Leetcode 34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/7403935/two-binary-searches-to-locate-target-ran-6k3i/){:target="_blank" rel="noopener noreferrer"}**

2. [Leetcode 540. Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/single-element-in-a-sorted-array/solutions/7404225/single-element-in-a-sorted-array-parity-ktevy/){:target="_blank" rel="noopener noreferrer"}**

3. [Rotation Count in a Rotated Sorted Array](https://www.geeksforgeeks.org/dsa/find-rotation-count-rotated-sorted-array/){:target="_blank" rel="noopener noreferrer"} - **[Click for My Approach](Kth_rotation.pdf)**

    **[Click here for Solution](Kth_rotation.cpp)**

4. [Leetcode 153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/7407426/binary-search-to-locate-rotation-point-o-vh1h/){:target="_blank" rel="noopener noreferrer"}**

    This problem is exactly same as the above problem 3. Rotation Count in a Rotated Sorted Array 

5. [Leetcode 33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/7407549/search-in-rotated-sorted-array-find-rota-q0h3/){:target="_blank" rel="noopener noreferrer"}**

    This problem is also the modified version of the previous problem 4 and hence problem 3.

6. [Find Position of an Element in a Sorted Array of Infinite Numbers](https://www.geeksforgeeks.org/dsa/find-position-element-sorted-array-infinite-numbers/){:target="_blank" rel="noopener noreferrer"} - **[Click here for my Approach](bsOnInfiniteNum.pdf)**

7. [Index of first 1 in an infinite binary sorted array](https://www.geeksforgeeks.org/dsa/find-index-first-1-infinite-sorted-array-0s-1s/){:target="_blank" rel="noopener noreferrer"} - **[Click here for my Approach](firstOneInBinaryInfiniteArray.pdf)**

    Approach for this problem is similar to the previous problem number 6.
    - First find out the Bound where first time 1 can appear (say `[l, r]`).
    - Now find the occurrence of first 1 in `[l, r]`.

8. [Leetcode 162. Find Peak Element](https://leetcode.com/problems/find-peak-element/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/find-peak-element/solutions/7413917/find-peak-element-binary-search-on-slope-sjc3/){:target="_blank" rel="noopener noreferrer"}**

9. [Leetcode 852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/peak-index-in-a-mountain-array/solutions/7413977/binary-search-on-increasingdecreasing-sl-w36n/){:target="_blank" rel="noopener noreferrer"}**

10. [Search in a row wise and column wise sorted matrix](https://www.geeksforgeeks.org/dsa/search-in-row-wise-and-column-wise-sorted-matrix/){:target="_blank" rel="noopener noreferrer"} - **[My Approach and Solution](searchInSortedMatrix.pdf)

11. [Leetcode 74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/search-a-2d-matrix/solutions/7415712/search-a-2d-matrix-double-binary-search-01x4d/){:target="_blank" rel="noopener noreferrer"}**

12. [Allocate Minimum Pages](https://www.geeksforgeeks.org/dsa/allocate-minimum-number-pages/){:target="_blank" rel="noopener noreferrer"} - **[My Approach and Solution](allocateMinimumPages.md)**

    - Binary search on value

13. [Leetcode 875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/koko-eating-bananas/solutions/7429088/binary-search-on-eating-speed-efficient-6ydvw/){:target="_blank" rel="noopener noreferrer"}**

    - **For example visuals [CLICK HERE](koko-banana.pdf)**
    - Binary search on value


14. [Leetcode 981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/time-based-key-value-store/solutions/7429283/time-based-key-value-store-hashmap-order-k75k/){:target="_blank" rel="noopener noreferrer"}**





## 🔹 Level 3 – Hard

1. [Leetcode 1095. Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/find-in-mountain-array/solutions/7414067/binary-search-on-mountain-array-find-pea-s9fz/){:target="_blank" rel="noopener noreferrer"}**

2. [Leetcode 4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/){:target="_blank" rel="noopener noreferrer"} - **[My Approach & Leetcode Solution link](https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/7430537/median-of-two-sorted-arrays-binary-searc-hjg4/){:target="_blank" rel="noopener noreferrer"}**

    - For visual examples **[Click Here](median-sorted-array.pdf)**



