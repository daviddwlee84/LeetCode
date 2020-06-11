from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_count = [0, 0, 0]  # red, white, blue
        for num in nums:
            color_count[num] += 1

        i, color = 0, 0
        while i < len(nums):
            if color_count[color] <= 0:
                # go to next color
                color += 1
                continue

            color_count[color] -= 1
            nums[i] = color
            i += 1

# Runtime: 60 ms, faster than 6.70% of Python3 online submissions for Sort Colors.
# Memory Usage: 13.9 MB, less than 27.71% of Python3 online submissions for Sort Colors.
