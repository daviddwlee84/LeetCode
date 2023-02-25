from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        This will TLE
        """
        max_profit = 0
        for i, buy in enumerate(prices):
            for sell in prices[i + 1:]:
                max_profit = max(max_profit, sell - buy)
                
        return max_profit
