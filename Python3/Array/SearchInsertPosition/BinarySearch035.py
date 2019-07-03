from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)  # exclude
        # end = len(nums) - 1 # include
        while start < end:  # exclude
        # while start <= end:  # include
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle  # exclude
                # end = middle - 1  # include
            else:
                start = middle + 1
        return start
