from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        self.answer = float('inf')

        def dfs(x: int, y: int, m: int, n: int, current_sum: int):
            current_sum += grid[x][y]

            if x == m - 1 and y == n - 1:
                self.answer = min(self.answer, current_sum)
                return

            if x < m - 1 and y < n - 1:
                dfs(x + 1, y, m, n, current_sum)
                dfs(x, y + 1, m, n, current_sum)
            elif x < m - 1 and y == n - 1:
                dfs(x + 1, y, m, n, current_sum)
            else:
                dfs(x, y + 1, m, n, current_sum)

        dfs(0, 0, m, n, 0)

        return self.answer
