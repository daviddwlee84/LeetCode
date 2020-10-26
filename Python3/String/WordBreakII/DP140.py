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


from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution

        This is basically the same as the DFS but this return answer rather than append to a global answer

        # dp[s]: vector of string (forget about this....)
        """

        @lru_cache(None)
        def helper(string: str) -> List[str]:
            if not string:
                return []

            result = []
            for word in wordDict:
                if not string.startswith(word):
                    continue

                if len(word) == len(string):
                    result.append(word)
                else:
                    result_of_the_rest = helper(string[len(word):])
                    for item in result_of_the_rest:
                        item = word + ' ' + item
                        result.append(item)

            return result

        return helper(s)

# Runtime: 60 ms, faster than 24.80% of Python3 online submissions for Word Break II.
# Memory Usage: 14.4 MB, less than 12.83% of Python3 online submissions for Word Break II.
