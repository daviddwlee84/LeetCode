from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i: int, j: int):
            if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])):
                return 0, True
            if grid[i][j] == 0:
                return 0, False
            if (i, j) in visited:
                return 0, False

            visited.add((i, j))

            # grid[i][j] == 1
            area_left, reach_boundary_left = dfs(i, j - 1)
            area_right, reach_boundary_right = dfs(i, j + 1)
            area_up, reach_boundary_up = dfs(i + 1, j)
            area_down, reach_boundary_down = dfs(i - 1, j)

            return 1 + area_left + area_right + area_up + area_down, reach_boundary_left or reach_boundary_right or reach_boundary_up or reach_boundary_down

        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area, reach_boundary = dfs(i, j)
                    if not reach_boundary:
                        ans += area

        return ans
