# 1458. Max Dot Product of Two Subsequences

## Description

Given two arrays `nums1` and `nums2`.

Return the maximum dot product between **non-empty** subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, `[2,3,5]` is a subsequence of `[1,2,3,4,5]` while `[1,5,3]` is not).

**Example 1**:

```txt
Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.
```

**Example 2**:

```txt
Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.
```

**Example 3**:

```txt
Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.
```

**Constraints**:

* `1 <= nums1.length, nums2.length <= 500`
* `-1000 <= nums1[i], nums2[i] <= 1000`

> Hint:
>
> Use dynamic programming, define `DP[i][j]` as the maximum dot product of two subsequences starting in the position i of nums1 and position j of nums2.

## Solution

## Others' Solution

* [[C++/Python] Simple DP - LeetCode Discuss](https://leetcode.com/problems/max-dot-product-of-two-subsequences/discuss/648261/C%2B%2BPython-Simple-DP)

Python 3, recursion with memoization

```py
from functools import lru_cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def helper(i, j):
            if i == 0 or j == 0: return -math.inf
            return max(helper(i - 1, j - 1), helper(i, j - 1), helper(i - 1, j),
                       max(helper(i - 1, j - 1), 0) + nums1[i - 1] * nums2[j - 1])
        return helper(len(nums1), len(nums2))
```

Python 3, dp

```py
import math
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [-math.inf] * (m + 1)
        for i in range(1, n + 1):
            dp, old_dp = [-math.inf], dp
            for j in range(1, m + 1):
                dp += max(
                    old_dp[j], # not select i
                    dp[-1], # not select j
                    old_dp[j - 1], # not select either
                    max(old_dp[j - 1], 0) + nums1[i - 1] * nums2[j - 1], # select both
                )
        return dp[-1]
```

* [[Java/C++/Python] the Longest Common Sequence - LeetCode Discuss](https://leetcode.com/problems/max-dot-product-of-two-subsequences/discuss/648420/JavaC%2B%2BPython-the-Longest-Common-Sequence)

```py
    def maxDotProduct(self, A, B):
        n, m = len(A), len(B)
        dp = [[0] * (m) for i in range(n)]
        for i in range(n):
            for j in range(m):
                dp[i][j] = A[i] * B[j]
                if i and j: dp[i][j] += max(dp[i - 1][j - 1], 0)
                if i: dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j: dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[-1][-1]
```
