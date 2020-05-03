from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longest = 0
        for i in range(len(nums)):
            temp_min = nums[i]
            temp_max = nums[i]
            for j in range(i + 1, len(nums)):
                temp_max = max(temp_max, nums[j])
                temp_min = min(temp_min, nums[j])
                if temp_max - temp_min <= limit:
                    longest = max(longest, j - i)

        return longest + 1

# TLE
