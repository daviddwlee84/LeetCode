from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        double_nums = [num * 2 for num in nums]

        left = len(nums) - 1
        right = len(nums) - 1

        while double_nums[left] > nums[right]:
            left -= 1
        
        right_end = left
        
        temp = 2
        while left >= 0 and right > right_end:
            if double_nums[left] <= nums[right]:
                answer += temp
                temp = 0
            else:
                left -= 1

        # Not finished
