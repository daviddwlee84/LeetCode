from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.recursive(nums, target, 0, len(nums) - 1)

    def recursive(self, nums: List[int], target: int, left: int, right: int) -> int:
        mid = (left + right) // 2
        if left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.recursive(nums, target, mid + 1, right)
            else:
                return self.recursive(nums, target, left, mid - 1)
        else:
            return -1

# Runtime: 264 ms, faster than 40.81% of Python3 online submissions for Binary Search.
# Memory Usage: 15 MB, less than 6.45% of Python3 online submissions for Binary Search.
