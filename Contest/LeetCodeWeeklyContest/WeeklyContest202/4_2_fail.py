class Solution:
    def minDays(self, n: int) -> int:
        # dp = [0] * (2*10 ^ 9 + 1)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i % 6 == 0:
                # print(i - 1, i - 2 * (i // 3), i - i // 2)
                dp[i] = min(dp[i - 1], dp[i - 2 * (i // 3)],
                            dp[i - i // 2]) + 1
            elif i % 3 == 0:
                # print(i - 1, i - 2 * (i // 3))
                dp[i] = min(dp[i - 1], dp[i - 2 * (i // 3)]) + 1
            elif i % 2 == 0:
                # print(i - 1, i - i // 2)
                dp[i] = min(dp[i - 1], dp[i - i // 2]) + 1
            else:
                # print(i - 1, i - i // 2)
                dp[i] = dp[i - 1] + 1

        return dp[n]

# TLE
# 3681069
