from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
        Alex Wice's Solution

        1. prefix sum for each column

        0 0 1     0 0 1
        1 1 1  => 1 1 2
        0 1 1     0 2 3

        2. sort the matrix
        """

        rows, cols = len(matrix), len(matrix[0])

        for col in range(cols):
            s = 0
            for row in range(rows):
                s = 0 if matrix[row][col] == 0 else s + 1
                matrix[row][col] = s

        ans = 0
        for srow in map(sorted, matrix):
            for col in range(cols - 1, -1, -1):
                cand = (cols - col) * srow[col]
                ans = max(ans, cand)

        return ans
