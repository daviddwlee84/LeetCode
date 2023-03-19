from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        positions = {}
        for i, row in enumerate(grid):
            for j, order in enumerate(row):
                positions[order] = (i, j)

        if positions[0] != (0, 0):
            return False

        prev_i, prev_j = positions[0]
        step = 1
        while step < len(grid) * len(grid[0]):
            i, j = positions[step]
            valid = False
            for diff_i, diff_j in [(2, 1), (1, 2), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
                if i + diff_i == prev_i and j + diff_j == prev_j:
                    valid = True
            if not valid:
                return False
            
            prev_i, prev_j = i, j
            step += 1

        return True

# WA (position 0 not at top-left)
# [[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]]
