from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.position = []  # (i, j)
        self.answer = []
        self.helper(0, n)
        return self.answer

    def helper(self, row, n):
        if row == n:
            self.answer.append(self.constructBoard(n))
            return

        for col in range(n):
            if self.isValid(row, col, n):
                self.position.append((row, col))
                self.helper(row + 1, n)
                self.position.pop()

    def isValid(self, row, col, n):
        for i, j in self.position:
            if col == j:
                return False

            # TODO: more brute force way to check the slash

            # (1, 2) <= 2 - 1 = 1
            # (3, 4) <= 4 - 3 = 1
            # (5, 6) <= 6 - 5 = 1
            if row - col == i - j:
                return False

            # (2, 5) <= 2 + 5 = 7
            # (3, 4) <= 3 + 4 = 7
            # (4, 3) <= 4 + 3 = 7
            if row + col == i + j:
                return False

        return True

    def constructBoard(self, n) -> List[str]:
        result = []
        for _, col in self.position:
            result.append('.' * col + 'Q' + '.' * (n - col - 1))
        return result


# Runtime: 152 ms, faster than 26.63% of Python3 online submissions for N-Queens.
# Memory Usage: 14.2 MB, less than 43.60% of Python3 online submissions for N-Queens.
