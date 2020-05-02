from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. All elements before the slow pointer (lastNonZeroFoundAt) are non-zeroes.
        # 2. All elements between the current and slow pointer are zeroes.

        lastNonZeroFoundAt = 0 # slow pointer
        
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[lastNonZeroFoundAt], nums[curr] = nums[curr], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1

# Runtime: 52 ms, faster than 53.98% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.2 MB, less than 5.97% of Python3 online submissions for Move Zeroes.
