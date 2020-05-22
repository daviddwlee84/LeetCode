from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """ https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space)
        This use the same matrix to store the DP result
        """

        if matrix is None or len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        result = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:  # Cases with first row or first col
                        result += 1       # The 1 cells are square on its own
                    else:                 # Other cells
                        cell_val = min(
                            matrix[r-1][c-1], matrix[r][c-1], matrix[r-1][c]) + matrix[r][c]
                        result += cell_val
                        # **memoize the updated result**
                        matrix[r][c] = cell_val
        return result
