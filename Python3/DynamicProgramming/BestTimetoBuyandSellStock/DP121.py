class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0

        if len(prices) <= 1:
            return profit

        minimum = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif (prices[i] - minimum) > profit:
                profit = prices[i] - minimum

        return profit
