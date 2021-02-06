from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Directly sort the nums and swap them

        https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof
        https://leetcode.com/problems/wiggle-sort-ii/discuss/155764/Python-3-lines-simplest-solution-for-everyone-to-understand
        """
        nums.sort()
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]

        # tmp = sorted(nums)
        # nums[0::2] = tmp[:(len(tmp)+1)//2][::-1]
        # nums[1::2] = tmp[(len(tmp)+1)//2:][::-1]

        # arr = sorted(nums)
        # for i in range(1, len(nums), 2):
        #     nums[i] = arr.pop()
        # for i in range(0, len(nums), 2):
        #     nums[i] = arr.pop()

# Runtime: 164 ms, faster than 78.30% of Python3 online submissions for Wiggle Sort II.
# Memory Usage: 17.2 MB, less than 47.34% of Python3 online submissions for Wiggle Sort II.
