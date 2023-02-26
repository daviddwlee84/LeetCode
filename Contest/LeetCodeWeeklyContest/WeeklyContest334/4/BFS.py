from typing import List
from collections import deque

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        visited = set((0, 0))
        queue = deque([((0, 0), 0)]) # num, time
        m, n = len(grid), len(grid[0])
        while queue:
            (i, j), time = queue.pop()
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                row = i + di
                col = j + dj
                # BUG: We need to wait until we can move forward
                if 0 <= row < m and 0 <= col < n and (row, col) not in visited and time <= grid[row][col]:
                    if (row, col) == (m - 1, n - 1):
                        return time + 1
                    queue.appendleft(((row, col), time + 1))
                    # WA, Deprecated
        
        return -1
