# LeetCode: Time Limit Exceeded
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Store the calculated result to reduce time complexity
        # Initial with base case of stair 1 and 2
        self.wayToStairs = {1:1, 2:2} 
        self.helper(n)
        return self.wayToStairs[n]
    
    def helper(self, n):
        if not n in self.wayToStairs:
            #                     Climb two more stairs   Climb one more stair
            #                              ^                      ^
            #                              |                      |
            self.wayToStairs[n] =  self.helper(n-2) + self.helper(n-1)
        
        return self.wayToStairs[n]
