from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        min_grid = [[float('inf')] * n for _ in range(m)]

        def dfs(x: int, y: int, m: int, n: int, current_sum: int):
            current_sum += grid[x][y]

            if current_sum > min_grid[x][y]:
                return

            min_grid[x][y] = current_sum

            if x == m - 1 and y == n - 1:
                return

            if x < m - 1 and y < n - 1:
                dfs(x + 1, y, m, n, current_sum)
                dfs(x, y + 1, m, n, current_sum)
            elif x < m - 1 and y == n - 1:
                dfs(x + 1, y, m, n, current_sum)
            else:
                dfs(x, y + 1, m, n, current_sum)

        dfs(0, 0, m, n, 0)

        return min_grid[m - 1][n - 1]
