# 279. Perfect Squares

Given a positive integer *n*, find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to *n*.

**Example 1**:

```txt
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
```

**Example 2**:

```txt
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

## Solution

### Pure BFS

### BFS with DP

### DP

### Others' Solution

* [Summary of 4 different solutions (BFS, DP, static DP and mathematics) (C++)](https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/discuss/71488/Summary-of-4-different-solutions-(BFS-DP-static-DP-and-mathematics))
* [Short Python solution using BFS](https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/discuss/71475/Short-Python-solution-using-BFS)

```py
## dynamic programming
## Eg: square numbers : 1 4 9 ...
## d[12] = min(d[11]+1, d[8]+1, d[3]+1 )
## d[0] = 0, d[1] = 1
## generalization : d[i] = min{d[i-j^2]+1}, i>=j^2 ( 1<= j <= sqr(i))



class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
```

```py
from collections import deque
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Starting point: Current sum
        # Next layer: The sum that after adding a square
        # Find the shortest path using BFS
        record = []
        for i in range(1, int(n ** 0.5) + 1):
            record.append(i * i)
        # print record
        visited = set()
        q = deque()
        q.append([0, 0])
        while(q):
            m, cnt = q.popleft()
            for num in record:
                s = m + num
                if s == n:
                    return cnt + 1
                if s < n and s not in visited:
                    visited.add(s)
                    q.append([s, cnt + 1])
```
