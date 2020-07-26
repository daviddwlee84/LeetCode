from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        Alex Wice's Solution
        """

        INF = int(1e9)
        N = len(s)

        def rle(x):
            # the length of a RLE-version of a character repeated x times
            # 1 <= s.length <= 100
            # 0 <= k <= s.length
            if x <= 1:
                return 1
            elif x <= 9:
                return 2
            elif x <= 99:
                return 3
            else:
                return 4

        @lru_cache(None)
        def dp(i, last_char, cur_length, eaten):
            # The minimum length of a RLE version of s[i:], where:
            # * The last character written was `last_char`
            # * The length of the suffix group of last_char is `cur_length`
            # * The number of characters removed currently is `eaten`
            if eaten > k:
                return INF
            if i == N:
                return 0

            ans = dp(i + 1, last_char, cur_length, eaten + 1)
            if s[i] == last_char:
                delta = rle(cur_length + 1) - rle(cur_length)
                cand = dp(i + 1, s[i], cur_length + 1, eaten) + delta
                ans = min(ans, cand)
            else:
                delta = 1
                cand = dp(i + 1, s[i], 1, eaten) + delta
                ans = min(ans, cand)

            return ans

        return dp(0, '', 0, 0)
