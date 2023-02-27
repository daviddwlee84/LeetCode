class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # store operation count for word1[0:i] and word2[0:j]
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # Initial base case of all deletion and all insertion
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
        
        # print(dp)

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    # We can offset the first character
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    # Try insert, delete, or replace
                    dp[i + 1][j + 1] = 1 + \
                        min(dp[i][j + 1], dp[i + 1][j], dp[i][j])

        return dp[len(word1)][len(word2)]
