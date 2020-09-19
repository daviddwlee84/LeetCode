class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        > You can always convert a greedy solution to a "DP" solution by keeping a record of the local optima at each timestep.
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
