from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i, num in enumerate(nums):
            if i > max_index:
                break
            max_index = max(max_index, i + num)

        return max_index >= len(nums) - 1

# Runtime: 88 ms, faster than 75.27% of Python3 online submissions for Jump Game.
# Memory Usage: 15.9 MB, less than 99.99% of Python3 online submissions for Jump Game.
