from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/island-perimeter/discuss/95007/Short-Python
        Since there are no lakes, every pair of neighbour cells with different values is part of the perimeter (more precisely, the edge between them is).
        So just count the differing pairs, both horizontally and vertically (for the latter I simply transpose the grid).
        """

        # add '0' for edge case
        grid_str = ['0' + ''.join(str(x) for x in row) + '0' for row in grid]
        # as we count it horizontally, we transpose the grid
        grid_trans = list(map(list, zip(*grid)))
        # we can just use same object to count
        grid_str += ['0' + ''.join(str(x)
                                   for x in row) + '0' for row in grid_trans]

        # count every edges
        return sum(row.count('01') + row.count('10') for row in grid_str)

# Runtime: 612 ms, faster than 53.49% of Python3 online submissions for Island Perimeter.
# Memory Usage: 14 MB, less than 68.20% of Python3 online submissions for Island Perimeter.
