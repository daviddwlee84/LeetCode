from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        as we are using only the previous elements, therefore we just need 1D dp array
        """
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        # store the last row
        dp = [0] * (cols + 1)
        prev = 0
        maxsqlen = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]

                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                    maxsqlen = max(maxsqlen, dp[j])

                else:
                    dp[j] = 0

                prev = temp

        return maxsqlen ** 2

# Runtime: 200 ms, faster than 76.69% of Python3 online submissions for Maximal Square.
# Memory Usage: 14.4 MB, less than 9.09% of Python3 online submissions for Maximal Square.
