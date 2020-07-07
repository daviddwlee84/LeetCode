from typing import List
from itertools import product


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        https://leetcode.com/problems/word-search/discuss/27820/Python-DFS-solution
        https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.

        use visited set
        """
        visited = set()

        self.m, self.n = len(board), len(board[0])
        self.board = board
        self.word = word
        for i, j in product(range(self.m), range(self.n)):
            if self.dfs(i, j, visited):
                return True

        return False

    def dfs(self, i, j, visited, pos=0):
        if pos == len(self.word):
            return True

        if i < 0 or i >= self.m or j < 0 or j >= self.n or (i, j) in visited or self.word[pos] != self.board[i][j]:
            return False

        visited.add((i, j))
        found = self.dfs(i, j + 1, visited, pos + 1) \
            or self.dfs(i, j - 1, visited, pos + 1) \
            or self.dfs(i + 1, j, visited, pos + 1) \
            or self.dfs(i - 1, j, visited, pos + 1)
        visited.remove((i, j))

        return found
