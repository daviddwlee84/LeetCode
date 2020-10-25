from typing import List
from heapq import heappush, heappop


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Alex Wice's Solution

        Dijkstra
        """

        rows = len(heights)
        cols = len(heights[0])

        def neighbors(row: int, col: int):
            for next_row, next_col in ((row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)):
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    yield next_row, next_col

        queue = [(0, 0, 0)]
        dist = {(0, 0): 0}

        while queue:
            effort, row, col = heappop(queue)
            if row == rows - 1 and col == cols - 1:
                return effort

            for neighbor in neighbors(row, col):
                next_row, next_col = neighbor
                next_effort = max(effort, abs(
                    heights[next_row][next_col] - heights[row][col]))
                if next_effort < dist.get(neighbor, float('inf')):
                    dist[neighbor] = next_effort
                    heappush(queue, (next_effort, next_row, next_col))

# Runtime: 892 ms, faster than 100.00% of Python3 online submissions for Path With Minimum Effort.
# Memory Usage: 16 MB, less than 50.00% of Python3 online submissions for Path With Minimum Effort.
