# 120. Triangle

## Description

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

```txt
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is `11` (i.e., **2** + **3** + **5** + **1** = 11).

**Note**:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

## Solution

### Naive

Build another triangle and store the mininum path sum currently. In the end, return the minimum of the last row.

### Dynamic Programming

## Others' Solution

### Use less than O(n) space

```py
def minimumTotal(self, triangle: List[List[int]]) -> int:
    l = len(triangle)-1
    for i in range(l-1,-1,-1):
        for j in range(len(triangle[i])):
            triangle[-1][j] = min(triangle[-1][j], triangle[-1][j+1]) + triangle[i][j]
    return triangle[l][0]
```

```py
class Solution:
    def minimumTotal(self, T: List[List[int]]) -> int:

        for i in range(len(T)):
            T[i] = [float('inf')] + T[i] + [float('inf')]
        m = len(T)
        for i in range(1,m):
            n = len(T[i])
            for j in range(1,n-1):
                T[i][j] += min(T[i-1][j-1], T[i-1][j])
        return min(T[-1])
```

> Bottom Up

```py
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        m = len(triangle)
        dp = triangle[m - 1][:]
        for i in range(m - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]
```

> Bottom Up 2

```py
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                dp[i] = row[i] + min(dp[i], dp[i + 1])
        return dp[0]
```

### Use more than O(n) space

> [Python solution, Clean code - LeetCode Discuss](https://leetcode.com/problems/triangle/discuss/444712/Python-solution-Clean-code)

```py
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float('inf')]*(i+1) for i in range(len(triangle))]
        dp[0] = triangle[0]

        for j in range(1, len(dp)):
            for i in range(len(dp[j])):
                left = dp[j-1][max(0,i-1)]
                right = dp[j-1][min(i,len(dp[j-1])-1)]

                dp[j][i] = min(dp[j][i], triangle[j][i] + min(left,right))
        return min(dp[-1])
```
