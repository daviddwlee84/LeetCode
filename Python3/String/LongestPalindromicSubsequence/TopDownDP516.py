from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        https://leetcode.com/problems/longest-palindromic-subsequence/solutions/3415577/image-explanation-best-on-internet-recursion-top-down-bottom-up-bottom-up-o-n/
        """

        @lru_cache(None)
        def palindrome_length(start: int, end: int) -> int:
            nonlocal s

            if start == end:
                return 1

            if start > end:
                return 0

            if s[start] == s[end]:
                return 2 + palindrome_length(start + 1, end - 1)

            return max(palindrome_length(start + 1, end), palindrome_length(start, end - 1))

        return palindrome_length(0, len(s) - 1)
