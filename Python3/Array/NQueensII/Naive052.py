class Solution:
    def totalNQueens(self, n: int) -> int:
        self.position = set()  # (i, j)
        self.answer = 0
        self.helper(0, n)
        return self.answer

    def helper(self, row, n):
        if row == n:
            self.answer += 1
            return

        for col in range(n):
            if self.isValid(row, col, n):
                self.position.add((row, col))
                self.helper(row + 1, n)
                self.position.remove((row, col))

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

# Runtime: 144 ms, faster than 22.18% of Python3 online submissions for N-Queens II.
# Memory Usage: 13.9 MB, less than 40.00% of Python3 online submissions for N-Queens II.
