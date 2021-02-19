from typing import List
from itertools import groupby


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """
        sort of math solution
        """
        diff = []
        for i in range(len(A) - 1):
            diff.append(A[i + 1] - A[i])

        ans = 0
        for _, items in groupby(diff):
            items = list(items)

            ans += sum(i + 1 for i in range(len(items) - 1))

        return ans

# Runtime: 36 ms, faster than 77.16% of Python3 online submissions for Arithmetic Slices.
# Memory Usage: 14.6 MB, less than 17.20% of Python3 online submissions for Arithmetic Slices.
