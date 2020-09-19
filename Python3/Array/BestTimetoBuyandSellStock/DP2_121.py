from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0] means buy; d[i][1] means sell
        """
        dp = [[0, 0] for _ in range(len(prices) + 1)]
        dp[0][0] = float('inf')

        for i in range(1, len(prices) + 1):
            # Update sell (if we can get better profit)
            dp[i][1] = max(dp[i - 1][1], prices[i - 1] - dp[i - 1][0])
            # Update buy (current minimal price)
            dp[i][0] = min(dp[i - 1][0], prices[i - 1])

        return dp[len(prices)][1]
