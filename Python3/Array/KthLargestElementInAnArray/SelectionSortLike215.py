from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for last_range in range(len(nums), len(nums)-k, -1):
            max_idx = 0
            for i in range(last_range):
                if nums[i] > nums[max_idx]:
                    max_idx = i
            nums[max_idx], nums[last_range-1] = nums[last_range-1], nums[max_idx]
        return nums[-k]
                    