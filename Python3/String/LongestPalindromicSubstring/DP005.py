class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""

        longest = ""

        # Initial DP table
        dp = [[False for _ in range(len(s))] for _ in range(len(s))] # an n*n table initialized with False

        for end in range(len(s)):
            for start in range(end+1):
                # surounding char are the same && char group inside is palindromic
                dp[start][end] = (s[start] == s[end]) and ((end - start <= 2) or dp[start+1][end-1])
                # end - start = 0: single character
                # end - start = 1: pair characters
                # end - start = 2: three characters (means the SINGLE MIDDLE char will definitely be palindromic)

                if dp[start][end] and end-start+1 > len(longest):
                    longest = s[start:end+1]

        return longest
