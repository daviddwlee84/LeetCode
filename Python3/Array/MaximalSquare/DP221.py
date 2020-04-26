from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Time Complexity: O(mn)
        Space Complexity: O(mn)
        """
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        maxsqlen = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1]
                                   [j], dp[i - 1][j - 1]) + 1
                    maxsqlen = max(maxsqlen, dp[i][j])

        return maxsqlen ** 2

# Runtime: 200 ms, faster than 76.69% of Python3 online submissions for Maximal Square.
# Memory Usage: 14.5 MB, less than 9.09% of Python3 online submissions for Maximal Square.
