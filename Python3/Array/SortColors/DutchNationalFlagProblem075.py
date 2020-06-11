from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        https://leetcode.com/problems/sort-colors/discuss/681591/Algorithm-Explained-or-Single-pass-or-O(n)
        https://en.wikipedia.org/wiki/Dutch_national_flag_problem
        [0] 0, 0, 0 [low] 1, 1, 1 [mid] unknown [high] 2, 2, 2 [n-1] 
        """
        low, mid, high = 0, 0, len(nums) - 1

        # the unknown/unsorted number are lied between mid and high
        while mid <= high:
            if nums[mid] == 0:
                # swap number with low
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # expand the boundary
                mid += 1
            elif nums[mid] == 2:
                # swap number with high
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

# Runtime: 36 ms, faster than 41.78% of Python3 online submissions for Sort Colors.
# Memory Usage: 13.8 MB, less than 49.55% of Python3 online submissions for Sort Colors.
