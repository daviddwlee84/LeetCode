from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        Brute Force with 2D sliding window
        """
        m, n = len(matrix), len(matrix[0])
        count = 0
        for side in range(1, min(m, n) + 1):
            for i in range(m - side + 1):
                for j in range(n - side + 1):
                    if self.checkAllOnes(matrix, i, j, side):
                        count += 1
        return count

    def checkAllOnes(self, matrix: List[List[int]], topleft_i: int, topleft_j: int, side: int) -> bool:
        for i in range(topleft_i, topleft_i + side):
            for j in range(topleft_j, topleft_j + side):
                if matrix[i][j] != 1:
                    return False
        return True

# TLE
