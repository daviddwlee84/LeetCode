from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/discuss/720200/Clean-Python-3-O(N)
        """
        min_val = min(arr)
        gap = (max(arr) - min_val) / (len(arr) - 1)

        if gap == 0:
            return True

        num_diffs = set(num - min_val for num in arr)
        return len(num_diffs) == len(arr) and all(diff % gap == 0 for diff in num_diffs)
