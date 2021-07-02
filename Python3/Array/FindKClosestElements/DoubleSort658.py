from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sort using custom comparator
        sorted_arr = sorted(arr, key=lambda num: abs(x - num))

        # Only take k elements
        # Sort again to have output in ascending order
        return sorted(sorted_arr[:k])

# Runtime: 308 ms, faster than 52.20% of Python3 online submissions for Find K Closest Elements.
# Memory Usage: 15.6 MB, less than 69.77% of Python3 online submissions for Find K Closest Elements.
