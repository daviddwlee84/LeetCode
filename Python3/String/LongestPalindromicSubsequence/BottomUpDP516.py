class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        https://leetcode.com/problems/longest-palindromic-subsequence/solutions/3415577/image-explanation-best-on-internet-recursion-top-down-bottom-up-bottom-up-o-n/
        """
        # define dp[i][j] as length of the longest palindromic subsequence
        # in the substring s[i:j+1]
        # final answer is dp[0][n-1]
        dp = [[0] * len(s) for _ in range(len(s))]

        for length in range(1, len(s) + 1):
            for start in range(len(s) - length + 1):
                end = start + length - 1

                if length == 1:
                    dp[start][end] = 1
                    continue

                if s[start] == s[end]:
                    dp[start][end] = 2 + dp[start + 1][end - 1]
                else:
                    dp[start][end] = max(
                        dp[start + 1][end], dp[start][end - 1])

        return dp[0][len(s) - 1]
