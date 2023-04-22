from functools import lru_cache


class Solution:
    @lru_cache(None)
    def minInsertions(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return 0

        if s[0] == s[-1]:
            return self.minInsertions(s[1:-1])

        return 1 + min(self.minInsertions(s[:-1]), self.minInsertions(s[1:]))
