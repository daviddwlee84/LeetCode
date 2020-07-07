from typing import List
from collections import defaultdict

direction = [
    (1, 0),  # down
    (-1, 0),  # up
    (0, 1),  # right
    (0, -1)  # left
]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        backtracking and early stop with tire
        """

        self.tire = defaultdict(list)
        self.board = board
        self.words = set(words)
        self.m, self.n = len(board), len(board[0])

        for word in words:
            self.addWord(word)

        # might have some duplicate words
        self.answer = set()

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in self.tire:
                    visited = set([(i, j)])
                    self.dfsOnTire(
                        self.tire[board[i][j]], board[i][j], i, j, visited)

        return list(self.answer)

    def addWord(self, word: str) -> None:
        node = self.tire
        for char in word:
            node = node.setdefault(char, {})
        node['$'] = True

    def dfsOnTire(self, node: dict, word: str, i: int, j: int, visited: set):
        if '$' in node:
            self.answer.add(word)
            # don't return here
            # we can avoid the following case that never reach aaab
            # aaa, aaab

        for i_dir, j_dir in direction:
            next_i, next_j = i + i_dir, j + j_dir
            if 0 <= next_i < self.m and 0 <= next_j < self.n and (next_i, next_j) not in visited:
                next_char = self.board[next_i][next_j]
                if next_char in node:
                    self.dfsOnTire(node[next_char], word +
                                   next_char, next_i, next_j, visited | set([(next_i, next_j)]))


# Runtime: 512 ms, faster than 29.99% of Python3 online submissions for Word Search II.
# Memory Usage: 30.6 MB, less than 54.77% of Python3 online submissions for Word Search II.
