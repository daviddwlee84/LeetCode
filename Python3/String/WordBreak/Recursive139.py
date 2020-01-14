from typing import List


def memoize(f):
    """ without this will TLE """
    memo = {}

    def helper(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return helper


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordSet = set(wordDict)
        return self.dfs_helper(s, )

    @memoize
    def dfs_helper(self, s: str) -> bool:
        if not s:
            # empty string is the base case
            return True

        for i in range(1, len(s) + 1):
            if s[:i] in self.wordSet and self.dfs_helper(s[i:]):
                return True

        return False

# Runtime: 40 ms, faster than 48.31% of Python3 online submissions for Word Break.
# Memory Usage: 13.2 MB, less than 58.33% of Python3 online submissions for Word Break.
