# Brute force
# LeetCode: Time Limit Exceeded
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        MAX = min(nums)
        for i in range(1, len(nums)+1): # i: compare length
            for j in range(len(nums)-i+1): # j: start position
                sumTemp = sum(nums[j:j+i+1]) # j to j+i+1
                if MAX < sumTemp:
                    MAX = sumTemp

        return MAX