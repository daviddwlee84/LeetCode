from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k

        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]

# Runtime: 292 ms, faster than 71.95% of Python3 online submissions for Find K Closest Elements.
# Memory Usage: 15.6 MB, less than 69.77% of Python3 online submissions for Find K Closest Elements.