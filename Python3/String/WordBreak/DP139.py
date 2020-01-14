from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        # dp[i]
        # i means the length of word break
        # dp[0] is empty string and is base case True
        dp = [True] + [False] * len(s)

        for length in range(1, len(s) + 1):
            for i in range(length):
                if dp[i] is True and s[i:length] in wordSet:
                    # if we found any match case, then this "length" of word break contain valid case
                    dp[length] = True
                    break

        return dp[len(s)]

# Runtime: 32 ms, faster than 87.79% of Python3 online submissions for Word Break.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Word Break.
