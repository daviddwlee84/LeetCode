from typing import List
from functools import lru_cache

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        """ longest common subsequence recursion with memorization """

        @lru_cache(None)
        def helper(i: int, j: int):
            if i <= -1 or j <= -1:
                return 0

            if A[i] == B[j]:
                # draw connecting line
                return helper(i - 1, j - 1) + 1
            else:
                return max(helper(i - 1, j), helper(i, j - 1))

        return helper(len(A) - 1, len(B) - 1)
