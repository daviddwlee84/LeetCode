from typing import List

direction = [
    (1, 0),  # down
    (-1, 0),  # up
    (0, 1),  # right
    (0, -1)  # left
]


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    zero_count = 0
                    for i_dir, j_dir in direction:
                        new_i = i + i_dir
                        new_j = j + j_dir
                        if 0 <= new_i < m and 0 <= new_j < n:
                            if grid[new_i][new_j] == 0:
                                zero_count += 1
                        else:
                            zero_count += 1
                    perimeter += zero_count
        return perimeter

# Runtime: 744 ms, faster than 26.85% of Python3 online submissions for Island Perimeter.
# Memory Usage: 13.8 MB, less than 94.46% of Python3 online submissions for Island Perimeter.
