class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

# Runtime: 28 ms, faster than 80.72% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.9 MB, less than 28.53% of Python3 online submissions for Climbing Stairs.
