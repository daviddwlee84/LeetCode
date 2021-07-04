from typing import List
import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/445540/Python-bisect-solution-(960ms-beat-71.25)
        """
        def maxSumSubarray(arr: List[int]):
            sub_s_max = float('-inf')
            s_curr = 0  # current sum
            prefix_sums = [float('inf')]
            for x in arr:
                bisect.insort(prefix_sums, s_curr)
                s_curr += x
                i = bisect.bisect_left(prefix_sums, s_curr - k)
                sub_s_max = max(sub_s_max, s_curr - prefix_sums[i])
            return sub_s_max

        m, n = len(matrix), len(matrix[0])
        # For each row, calculate the prefix sum.
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y + 1] += matrix[x][y]

        res = float('-inf')
        # For each pair of columns, calculate the sum of rows.
        for y1 in range(n):
            for y2 in range(y1, n):
                arr = [matrix[x][y2] -
                       (matrix[x][y1 - 1] if y1 > 0 else 0) for x in range(m)]
                res = max(res, maxSumSubarray(arr))
        return res
