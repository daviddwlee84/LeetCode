class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        waysToStair = [1, 2] # Initial value of stair 1 and 2
        for stair in range(2, n): # Calculate stair 3 to n
            waysToStair.append(waysToStair[stair-1] + waysToStair[stair-2])

        return waysToStair[n-1]
        