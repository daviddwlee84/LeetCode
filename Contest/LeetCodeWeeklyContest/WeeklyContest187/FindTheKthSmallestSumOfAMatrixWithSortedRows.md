# 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows

## Description

You are given an `m * n` matrix, `mat`, and an integer `k`, which has its rows sorted in non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. Return the Kth **smallest** array sum among all possible arrays.

**Example 1**:

```txt
Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.  
```

**Example 2**:

```txt
Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17
```

**Example 3**:

```txt
Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  
```

**Example 4**:

```txt
Input: mat = [[1,1,10],[2,2,9]], k = 7
Output: 12
```

**Constraints**:

* `m == mat.length`
* `n == mat.length[i]`
* `1 <= m, n <= 40`
* `1 <= k <= min(200, n ^ m)`
* `1 <= mat[i][j] <= 5000`
* `mat[i]` is a non decreasing array.

> Hint
>
> Save all visited sums and corresponding indexes in a priority queue. Then, once you pop the smallest sum so far, you can quickly identify the next m candidates for smallest sum by incrementing each row index by 1.

## Solution

## Others' Solution

* [[Python] O(k * logk * len(mat)) with detailed explanations + [4 lines python]. - LeetCode Discuss](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/discuss/609678/Python-O%28k-*-logk-*-len%28mat%29%29-with-detailed-explanations-%2B-4-lines-python.)

A pythonic one

```py
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        h = mat[0][:]
        for row in mat[1:]:
            h = sorted([i+j for i in row for j in h])[:k]
        return h[k-1]
```

A super fast one with heap

```py
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0])
        '''
        # brute force
        ans = []
        def search(row, acc=0):
            if row<m-1:
                for i in mat[row]:
                    search(row+1, acc+i)
            else:
                for i in mat[row]:
                    ans.append(acc+i)
        search(0)
        ans.sort()
        return ans[k-1]
        '''

        # better solution
        tmp = 0
        for i in range(m):
            tmp += mat[i][0]
        if k == 1:
            return tmp
        candidate = [(tmp, (0,)*m)]
        visited = set()
        while(k>1):
            k-=1
            ans, indexs = heapq.heappop(candidate)
            indexs = list(indexs)
            for i in range(m):
                if indexs[i]>=n-1:
                    continue
                indexs[i]+=1
                key = tuple(indexs)
                if key in visited:
                    indexs[i]-=1
                    continue
                visited.add(key)
                tmp = ans + mat[i][indexs[i]]-mat[i][indexs[i]-1]
                indexs[i]-=1
                heapq.heappush(candidate, (tmp, key))
        return candidate[0][0]
```
