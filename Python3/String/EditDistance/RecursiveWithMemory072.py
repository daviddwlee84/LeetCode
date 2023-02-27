from functools import lru_cache


class Solution:
    @lru_cache
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            # We can keep do deletion on long one
            # Or do insertion on short one
            return max(len(word1), len(word2))

        if word1[-1] == word2[-1]:
            # We can offset the last character
            return self.minDistance(word1[:-1], word2[:-1])

        else:
            # Try insert, delete, or replace
            # Insert to word1 is equivalent to delete word2
            return 1 + min(self.minDistance(word1[:-1], word2), self.minDistance(word1, word2[:-1]), self.minDistance(word1[:-1], word2[:-1]))
