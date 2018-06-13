class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        
        maxSum = curSum = nums[0] # Initialize

        for i in range(1, len(nums)): # Go through every elements
            curSum = nums[i]+curSum if curSum > 0 else nums[i]
            maxSum = max(maxSum, curSum)
        
        return maxSum