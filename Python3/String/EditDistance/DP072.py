class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # initialize dp table
        table = [[-1 for _ in range(n+1)] for _ in range(m+1)] # (m+1) x (n+1) table
        for i in range(m+1):
            table[i][0] = i
        for j in range(n+1):
            table[0][j] = j

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    # if the current chars are the same
                    # just copy the best answer from diagonal
                    table[i+1][j+1] = table[i][j]
                else:
                    # take the minimum number of three and plus one
                    table[i+1][j+1] = min(table[i][j+1], table[i][j], table[i+1][j]) + 1
        
        return table[m][n]
