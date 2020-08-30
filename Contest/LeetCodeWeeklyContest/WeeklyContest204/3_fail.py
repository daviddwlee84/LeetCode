from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def get_surround_zeros(i, j) -> int:
            count = 0
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]):
                    if grid[i + di][j + dj] == 0:
                        count += 1
                else:
                    count += 1
            return count

        max_zero = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num = get_surround_zeros(i, j)
                    if num == 4:
                        return 0
                    max_zero = max(max_zero, num)

        if max_zero == 3:
            return 1

        return 2
