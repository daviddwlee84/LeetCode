from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        https://leetcode.com/problems/surrounded-regions/discuss/691589/Detailed-Steps-or-Pictorial-Flow-or-DFS-on-the-Boarders-or-Easy-to-understand
        """
        self.board = board
        self.rows = len(board)
        if self.rows == 0:
            return
        self.cols = len(board[0])

        # 1. Replace any boarder O with P

        for i in range(self.rows):
            if self.board[i][0] == 'O':
                self.dfs(i, 0)
            if self.board[i][-1] == 'O':
                self.dfs(i, self.cols - 1)

        for j in range(self.cols):
            if self.board[0][j] == 'O':
                self.dfs(0, j)
            if self.board[-1][j] == 'O':
                self.dfs(self.rows - 1, j)

        for i in range(self.rows):
            for j in range(self.cols):
                # 2. Replace all left O with X
                if self.board[i][j] == 'O':
                    self.board[i][j] = 'X'
                # 3. Replace all P back to O
                if self.board[i][j] == 'P':
                    self.board[i][j] = 'O'

    def dfs(self, i: int, j: int):
        """
        DFS to replace any boarder O with P
        """
        if 0 <= i < self.rows and 0 <= j < self.cols:
            if self.board[i][j] == 'O':
                self.board[i][j] = 'P'
                self.dfs(i + 1, j)
                self.dfs(i - 1, j)
                self.dfs(i, j + 1)
                self.dfs(i, j - 1)

# Runtime: 144 ms, faster than 78.53% of Python3 online submissions for Surrounded Regions.
# Memory Usage: 15 MB, less than 71.56% of Python3 online submissions for Surrounded Regions.
