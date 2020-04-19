from typing import List


class Solution:
    """ https://leetcode.com/problems/minimum-path-sum/discuss/584967/Python-Grid-reduction-(Sounds-fancy-but-a-simple-method)-no-additional-space """

    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) <= 0 or grid is None:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:  # We just want to skip the top-left corner of the grid
                    continue
                if r-1 < 0:  # Cases for elements in top row
                    grid[r][c] = grid[r][c] + grid[r][c-1]
                elif c-1 < 0:  # Cases for elements in leftmost column
                    grid[r][c] = grid[r][c] + grid[r-1][c]
                else:  # Normal cell
                    grid[r][c] = grid[r][c] + min(grid[r-1][c], grid[r][c-1])

        # We have got the minimum path accumaled at the bottom-right corner, just return this
        return grid[rows-1][cols-1]
