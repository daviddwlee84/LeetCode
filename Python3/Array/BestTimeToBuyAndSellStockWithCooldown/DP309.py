from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75927/Share-my-thinking-process

        buy[i]: The maximum profit can be made if the first i days end with buy or wait.
                E.g "buy, sell, buy" or "buy, cooldown, cooldown"
        sell[i]: The maximum profit can be made if the first i days end with sell or wait.
                E.g "buy, sell, buy, sell" or "buy, sell, cooldown, cooldown"
        price: prices[i - 1], which is the stock price of the i-th day
        """

        if len(prices) < 2:
            return 0

        sell, buy = 0, -prices[0]
        prev_sell, prev_buy = 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)

        return sell

#        buy[i]: means before day i what is the maxProfit for any sequence end with buy.
#        sell[i]: means before day i what is the maxProfit for any sequence end with sell.
#        rest[i]: means before day i what is the maxProfit for any sequence end with rest.
#
#        (rest means no transaction on that day aka. cooldown)
#
#        deduce the transition functions for them
#
#        buy[i]  = max(rest[i-1]-price, buy[i-1])
#        sell[i] = max(buy[i-1]+price, sell[i-1])
#        rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
#
#        to make sure sell before buy => buy[i] <= rest[i] (rest[i] <= sell[i]) => rest[i] = sell[i-1]
#
#        buy[i] = max(sell[i-2]-price, buy[i-1])
#        sell[i] = max(buy[i-1]+price, sell[i-1])
#
#        states of day i relies only on i-1 and i-2 => reduce space to O(1)
