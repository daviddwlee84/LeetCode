from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return -1

# Runtime: 244 ms, faster than 97.92% of Python3 online submissions for Binary Search.
# Memory Usage: 15 MB, less than 6.45% of Python3 online submissions for Binary Search.
