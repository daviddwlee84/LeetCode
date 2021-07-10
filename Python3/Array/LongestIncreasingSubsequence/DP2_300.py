from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp[i] means, consider previous i numbers (including the ith number), the length of LIS
        """
        if len(nums) == 0:
            return 0

        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# Runtime: 4432 ms, faster than 12.84% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14.8 MB, less than 17.68% of Python3 online submissions for Longest Increasing Subsequence.
