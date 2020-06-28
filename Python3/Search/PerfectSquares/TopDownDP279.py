class Solution:
    def numSquares(self, n: int) -> int:
        """
        https://leetcode.com/problems/perfect-squares/discuss/707745/Top-Down-DP-w-code
        """
        dp = [-1] * (n + 1)

        def f(m: int) -> int:
            if dp[m] != -1:
                return dp[m]

            if m == 0:
                return 0

            minimum = float('inf')
            for i in range(1, int(m ** 0.5) + 1):
                curr = f(m - i ** 2) + 1
                minimum = min(minimum, curr)

            dp[m] = minimum
            return dp[m]

        return f(n)

# TLE
# 6603
