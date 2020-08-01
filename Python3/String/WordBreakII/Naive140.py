from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        [Getting rid of TLE - LeetCode Discuss](https://leetcode.com/problems/word-break-ii/discuss/44185/Getting-rid-of-TLE)

        # TLE
        # "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        # ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        """
        if not self.isBreakable(s, wordDict):
            return []

        self.wordStart = defaultdict(list)
        for word in wordDict:
            self.wordStart[word[0]].append(word)

        self.string = s
        self.answer = []
        self.helper(0, '')
        return self.answer

    def helper(self, i: int, curr_word_break: str):
        if i == len(self.string):
            self.answer.append(curr_word_break.strip())
            return
        # elif i > len(self.string):
        #     return

        if self.string[i] in self.wordStart:
            for candidate in self.wordStart[self.string[i]]:
                if candidate == self.string[i:i + len(candidate)]:
                    self.helper(i + len(candidate),
                                curr_word_break + ' ' + candidate)

    def isBreakable(self, s: str, wordDict: List[str]) -> bool:
        """
        Just use the solution of Word Break I

        DP139.py
        """
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

        # """
        # Just use the solution of Word Break I

        # https://leetcode.com/problems/word-break/discuss/43808/Simple-DP-solution-in-Python-with-description
        # """

        # dp = [True] + [False] * len(s)
        # for i in range(1, len(s) + 1):
        #     for word in wordDict:
        #         print(word, s[i - len(word):i])
        #         if word == s[i - len(word):i] and dp[i - len(word)]:
        #             dp[i] == True
        #             break

        # return dp[-1]


# Runtime: 72 ms, faster than 29.42% of Python3 online submissions for Word Break II.
# Memory Usage: 13.8 MB, less than 97.27% of Python3 online submissions for Word Break II.
