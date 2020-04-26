from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """ sliding window """
        if not matrix:
            return 0

        answer = 0
        for window_size in range(1, min(len(matrix), len(matrix[0])) + 1):
            if self.checkInWindow(window_size, matrix):
                answer = window_size ** 2
                continue

        return answer

    def checkInWindow(self, window_size: int, matrix: List[List[str]]) -> bool:
        for i in range(len(matrix) - window_size + 1):
            for j in range(len(matrix[0]) - window_size + 1):
                if self.checkSingleWindow(i, j, window_size, matrix):
                    return True

        return False

    def checkSingleWindow(self, start_i: int, start_j: int, window_size: int, matrix: List[List[str]]) -> bool:
        """ make sure all element in single square is all 1 """
        for i in range(start_i, start_i + window_size):
            for j in range(start_j, start_j + window_size):
                if matrix[i][j] != '1':
                    return False
        return True

# Runtime: 5368 ms, faster than 5.03% of Python3 online submissions for Maximal Square.
# Memory Usage: 14.5 MB, less than 9.09% of Python3 online submissions for Maximal Square.
