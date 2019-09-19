# 215. Kth Largest Element in an Array

## Description

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

**Example 1**:

```txt
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```

**Example 2**:

```txt
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```

**Note**:

You may assume k is always valid, 1 ≤ k ≤ array's length.

## Solution

### Sort entire array

> Time Limit Exceeded => because of the worst case => can be solved by using different pivot selection method

### Selection Sort Like Approach

* Each time find the largest number and insert to the k-1 position

### Maintain a top K list

### Min-heap

* maintain a min-heap with k element

### Others

* [Python different solutions with comments (bubble sort, selection sort, heap sort and quick sort)](https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-(bubble-sort-selection-sort-heap-sort-and-quick-sort).)
* [Solution explained](https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60294/Solution-explained)

```py
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Initialize the pq with first k elements
        pq=[]
        for i in range(k):
            heapq.heappush(pq, nums[i])

        # Iterate rest of the elements
        for num in nums[k:]:
            if num > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, num)

        return pq[0]
```
