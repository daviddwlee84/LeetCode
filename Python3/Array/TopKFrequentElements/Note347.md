# 347. Top K Frequent Elements

## Description

Given a non-empty array of integers, return the **k** most frequent elements.

**Example 1**:

```txt
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2**:

```txt
Input: nums = [1], k = 1
Output: [1]
```

**Note**:

* You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
* Your algorithm's time complexity **must be** better than O(n log n), where n is the array's size.

## Solution

### Hash Table + Heap

1. Use hash table to get the count/frequency of each number
2. Use heap to manage the order of frequency
3. Get/pop the number with the k most frequency

## Others' Solution

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            d[i] += 1

        d = sorted(d, key=d.get, reverse=True)

        for i, key in enumerate(d):
            if i < k:
                output.append(key)
        return output
```

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        priority_queue = []
        for key, value in counter.items():
            if len(priority_queue) == k:
                heapq.heappushpop(priority_queue, (value, key))
            else:
                heapq.heappush(priority_queue, (value, key))
        return [value for key, value in priority_queue]
```
