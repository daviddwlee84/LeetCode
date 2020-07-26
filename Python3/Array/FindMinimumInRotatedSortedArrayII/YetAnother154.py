from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/48808/My-pretty-simple-code-to-solve-it
        """

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[high]:
                low = mid + 1

            elif nums[mid] < nums[high]:
                high = mid

            else:  # when nums[mid] and nums[high] are same
                high -= 1

        # already include the case of already sorted and single one element
        return nums[low]
