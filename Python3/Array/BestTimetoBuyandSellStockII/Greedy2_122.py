from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices:
        #     return 0

        max_profit = 0
        previous = prices[0]
        for price in prices:
            if price - previous > 0:
                max_profit += price - previous
            previous = price

        return max_profit
