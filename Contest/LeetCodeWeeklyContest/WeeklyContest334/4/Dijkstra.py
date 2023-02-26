from typing import List
import heapq


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/solutions/3230787/python-c-clean-dijkstra-s-algorithm-solution-with-explanation/
        """
        m, n = len(grid), len(grid[0])
        # Can't move anywhere
        # [[0,2,4],[3,2,1],[1,0,4]]
        # -1
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        visited = [[False] * n for _ in range(m)]
        heap = [(0, 0, 0)]  # time, row, column

        while heap:
            # Each time we try to visit the minimum time adjacency greedily
            time, row, col = heapq.heappop(heap)

            # Found answer
            if row == m - 1 and col == n - 1:
                return time

            # Skip visited
            if visited[row][col]:
                continue

            # Visit the node
            visited[row][col] = True
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_row = row + di
                new_col = col + dj
                if 0 <= new_row < m and 0 <= new_col < n and not visited[new_row][new_col]:
                    # we may not always be able to move to an adjacent cell immediately.
                    # since we have to move every second
                    # Since it takes an even number of seconds to "stand still" when moving back and forth, we need to wait for an extra second if we want to move after an odd number of seconds
                    wait = (grid[new_row][new_col] - time) % 2 == 0
                    new_time = max(grid[new_row][new_col] + wait, time + 1)
                    heapq.heappush(heap, (new_time, new_row, new_col))

        return -1
