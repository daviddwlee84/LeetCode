from typing import List
from itertools import product


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        https://leetcode.com/problems/word-search/discuss/713113/C%2B%2B-Usiing-dfs-and-recursion-(Perfect-for-beginners)
        https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.

        modify board with # to note that has been visited
        """
        self.m, self.n = len(board), len(board[0])
        for i, j in product(range(self.m), range(self.n)):
            if board[i][j] == word[0]:
                if self.dfs(i, j, 0, board, word):
                    return True
        return False

    def dfs(self, i: int, j: int, count: int, board: List[List[str]], word: str):
        if count == len(word):
            return True

        if i < 0 or i >= self.m or j < 0 or j >= self.n or board[i][j] != word[count]:
            return False

        # '#' is to avoid visit again
        temp_char, board[i][j] = board[i][j], '#'
        # "|" is a binary operator, whereas "or" is a logical operator, which means "or" will stop once True is met, "|" won't.
        found = self.dfs(i - 1, j, count + 1, board, word) or \
            self.dfs(i + 1, j, count + 1, board, word) or \
            self.dfs(i, j - 1, count + 1, board, word) or \
            self.dfs(i, j + 1, count + 1, board, word)
        board[i][j] = temp_char

        return found

# TLE when using "|" while should use "or" in this case

# Runtime: 344 ms, faster than 78.13% of Python3 online submissions for Word Search.
# Memory Usage: 14.8 MB, less than 87.73% of Python3 online submissions for Word Search.
