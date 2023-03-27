from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp_min_grid = [[float('inf')] * n for _ in range(m)]

        cumulative = 0
        for i in range(m):
            dp_min_grid[i][0] = grid[i][0] + cumulative
            cumulative += grid[i][0]

        cumulative = 0
        for i in range(n):
            dp_min_grid[0][i] = grid[0][i] + cumulative
            cumulative += grid[0][i]

        # print(dp_min_grid)

        for i in range(1, m):
            for j in range(1, n):
                dp_min_grid[i][j] = min(
                    dp_min_grid[i - 1][j], dp_min_grid[i][j - 1]) + grid[i][j]

        return dp_min_grid[m - 1][n - 1]
