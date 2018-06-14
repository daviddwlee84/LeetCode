class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        valley = peak = 0
        profit = 0
        i = 0

        while i < len(prices)-1:
            while i < len(prices)-1 and not prices[i] < prices[i+1]:
                # Keep finding the turning up point
                i += 1
            # Update valley
            valley = prices[i]
            while i < len(prices)-1 and not prices[i] > prices[i+1]:
                # Keep finding the turning down point
                i += 1
            # Update peak
            peak = prices[i]
            # When find a valley and corresponding peak, calculate the profit
            profit += peak - valley

        return profit
