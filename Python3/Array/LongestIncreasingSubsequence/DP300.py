from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        dp = [None] * len(nums)
        dp[0] = 1 # initial value for the first element only

        for end in range(1, len(nums)):
            max_val = 0
            for j in range(end):
                if nums[end] > nums[j]:
                    # if the nums[end] can be followed by nums[j]
                    # update the maximum possible pre-LIS value
                    max_val = max(max_val, dp[j])
            
            dp[end] = max_val + 1 # plus itself

        return max(dp)
