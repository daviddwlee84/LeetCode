# 703. Kth Largest Element in a Stream

## Description

Design a class to find the **k**th largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer `k` and an integer array `nums`, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

**Example**:

```txt
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
```

**Note**:

You may assume that `nums`' length ≥ `k-1` and `k` ≥ 1.

## Solution

### Binary Insertion Sort

### Priority Queue

## Fail

This will TLE

```py
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)  # in-place
        self.data = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.data, val)
        return heapq.nlargest(self.k, self.data)[-1]
```
