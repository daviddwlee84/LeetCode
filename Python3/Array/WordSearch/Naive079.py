from typing import List
from itertools import product

direction = [
    (1, 0),  # down
    (-1, 0),  # up
    (0, 1),  # right
    (0, -1)  # left
]


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m, self.n = len(board), len(board[0])
        self.board = board

        for i, j in product(range(self.m), range(self.n)):
            if board[i][j] == word[0]:
                visited = set([(i, j)])
                if self.search(i, j, word[1:], visited):
                    return True

        return False

    def search(self, i: int, j: int, word: str, visited) -> bool:
        if not word:
            return True

        foundAny = False
        for dir_i, dir_j in direction:
            if 0 <= i + dir_i < self.m and 0 <= j + dir_j < self.n:
                if (i + dir_i, j + dir_j) not in visited:
                    if self.board[i + dir_i][j + dir_j] == word[0]:
                        foundAny |= self.search(i + dir_i, j + dir_j, word[1:],
                                                visited | set([(i + dir_i, j + dir_j)]))

        return foundAny

# TLE
