from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target and (mid + 1 == len(nums) or (mid < len(nums) and nums[mid + 1] > target)):
                if nums[mid] < target:
                    return mid + 1
                else:
                    return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
