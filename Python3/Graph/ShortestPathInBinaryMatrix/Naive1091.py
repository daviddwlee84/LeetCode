from typing import List
from collections import deque
from itertools import product


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1

        rows = len(grid)
        cols = len(grid[0])

        visited = {(0, 0)}
        queue = deque([((0, 0), 1)])
        # min_step = float('inf')  # this is not necessary, because it is BFS
        while queue:
            curr, step = queue.pop()
            if curr == (rows-1, cols-1):
                # min_step = min(step, min_step)
                return step

            # https://stackoverflow.com/questions/29001085/python-combination-with-replacement
            for di, dj in product([0, 1, -1], repeat=2):
                i, j = curr[0] + di, curr[1] + dj
                if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 0 and (i, j) not in visited:
                    queue.appendleft(((i, j), step + 1))
                    visited.add((i, j))

        # return min_step if min_step != float('inf') else -1
        return -1
