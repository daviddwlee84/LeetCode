class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
        # the 0 column, row are used for initial value
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[len(text1)][len(text2)]
