from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        This is a DP solution

        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)

        * 0: state_rest (can buy)
            * Rest: stay
            * Buy: go to state_holding
        * 1: state_hold (can sell)
            * Rest: stay
            * Sell: go to selling
        * 2: state_sold (take a rest)
            * Rest: go to state_empty

        because the state transitions only involve limited states and steps => we can use O(1) space

        https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75942/4-line-Python-solution-52-ms
        """

        sold = 0  # at the start, you don't have any stock if you just rest
        hold = float('-inf')
        rest = 0

        for i in range(len(prices)):

            # stay at state_hold or buy from state_rest
            # can buy, i.e. we have no sock now,
            # and the max profit should be "last no stock profit" or "last rest profit"
            hold = max(hold, rest - prices[i])
            # stay at state_rest or rest from state_sold
            # can sell, i.e. we now have stock,
            # and the profit should be "last stock profit" or "last no stock but buy this time"
            rest = max(rest, sold)
            # only one way from state_hold
            # we should sell then take a rest
            sold = hold + prices[i]

        return max(sold, rest)
