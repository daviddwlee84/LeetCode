from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/island-perimeter/discuss/95007/Short-Python
        Since there are no lakes, every pair of neighbour cells with different values is part of the perimeter (more precisely, the edge between them is).
        So just count the differing pairs, both horizontally and vertically (for the latter I simply transpose the grid).
        """
        return self.horizontal_edges(grid) + self.horizontal_edges(self.transpose(grid))

    def horizontal_edges(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            row = [0] + row + [0]
            for i in range(1, len(row)):
                count += row[i] != row[i - 1]
        return count

    def transpose(self, grid: List[List[int]]) -> List[List[int]]:
        tgrid = [[] for _ in range(len(grid[0]))]
        for row in grid:
            for i, item in enumerate(row):
                tgrid[i].append(item)
        return tgrid

# Runtime: 784 ms, faster than 22.10% of Python3 online submissions for Island Perimeter.
# Memory Usage: 14 MB, less than 74.33% of Python3 online submissions for Island Perimeter.
