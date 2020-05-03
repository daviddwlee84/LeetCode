from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        for window_size in range(len(nums), 0, -1):
            for start in range(len(nums) - window_size + 1):
                temp = nums[start:start + window_size]
                if max(temp) - min(temp) <= limit:
                    return window_size

        return 0

# TLE
