from typing import List

"""
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

Output:
[
  "cats and dog",
  "cat sand dog"
]
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        answer = []

        def dfs(string: str, curr_words: List[str]):
            if not string:
                answer.append(' '.join(curr_words))
                return

            for word in wordDict:
                # if string[:len(word)] == word:
                if string.startswith(word):
                    dfs(string[len(word):], curr_words + [word])

        dfs(s, [])
        return answer


# TLE
# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
