from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Basically using the Simpler version of problem 153
        """
        low = 0
        high = len(nums) - 1

        if nums[low] < nums[high]:
            # sorted array case
            return nums[low]

        # The problem's invariant for shifted cases is left element always greater than right
        while high - low > 1:
            mid = (high + low) // 2

            if nums[low] > nums[mid]:
                high = mid
            else:
                low = mid

        return nums[high]
