from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/island-perimeter/discuss/95001/clear-and-easy-java-solution

        the description of this problem implies there may be an "pattern" in calculating the perimeter of the islands.
        and the pattern is islands * 4 - neighbours * 2, since every adjacent islands made two sides disappeared(as picture below).

        +--+     +--+                   +--+--+
        |  |  +  |  |          ->       |     |
        +--+     +--+                   +--+--+

        4 + 4 - ? = 6  -> ? = 2

        Only check right and down, because left and up will get checked by a previous element.
        A neighbor subtracts a side from the perimeter. But since only count right and down, we have to double count. thus -2*neighbors.
        """
        m, n = len(grid), len(grid[0])
        islands, neighbours = 0, 0
        # alternative
        # count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    islands += 1  # count islands
                    # count += 4
                    if i < m - 1 and grid[i + 1][j] == 1:
                        # count down neighbours
                        neighbours += 1
                        # count -= 2
                    if j < n - 1 and grid[i][j + 1] == 1:
                        # count right neighbours
                        neighbours += 1
                        # count -= 2

        return islands * 4 - neighbours * 2
        # return count

# Runtime: 644 ms, faster than 46.37% of Python3 online submissions for Island Perimeter.
# Memory Usage: 14.2 MB, less than 22.03% of Python3 online submissions for Island Perimeter.
