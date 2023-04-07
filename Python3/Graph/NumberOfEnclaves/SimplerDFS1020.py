from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/number-of-enclaves/solutions/3388131/python-java-c-simple-solution-easy-to-understand/
        https://leetcode.com/problems/number-of-enclaves/solutions/3388645/python3-c-java-easy-and-understand-dfs-beats-97-85/
        """
        def dfs_clear(i: int, j: int) -> None:
            # This is also worked as "visited"
            grid[i][j] = 0
            for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
                if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and grid[i + di][j + dj]:
                    dfs_clear(i + di, j + dj)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1):
                    # Clear all cells that connect to edge
                    dfs_clear(i, j)

        # Collecting the remains 1
        return sum(sum(row) for row in grid)
