import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        # 57, 2 => 56.99999999999999
        return round(math.factorial(m + n) / math.factorial(n) / math.factorial(m))

# Runtime: 32 ms, faster than 57.17% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.7 MB, less than 85.45% of Python3 online submissions for Unique Paths.
