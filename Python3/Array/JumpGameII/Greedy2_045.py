from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # Update each nums to be the index it can reach
        for i, num in enumerate(nums):
            nums[i] = num + i

        prev = 0
        curr = 0
        times = 0
        while curr < len(nums) - 1:
            # Try to jump to the maximum index
            curr, prev = max(nums[prev:curr + 1]), curr
            times += 1
        return times
