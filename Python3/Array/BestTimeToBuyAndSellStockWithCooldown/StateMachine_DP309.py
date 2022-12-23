from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solutions/75927/Share-my-thinking-process/
        """

        buy = [float('-inf')] * (len(prices) + 1)
        sell = [0] * (len(prices) + 1)
        rest = [0] * (len(prices) + 1)
        for i, price in enumerate(prices):
            # Buy at this time or not
            buy[i + 1] = max(rest[i] - price, buy[i])
            # Sell at this time or not
            sell[i + 1] = max(buy[i] + price, sell[i])
            # Rest
            rest[i + 1] = max(buy[i], sell[i], rest[i])

        # print(buy)
        # print(sell)
        # print(rest)

        return max(sell[i + 1], rest[i + 1])
