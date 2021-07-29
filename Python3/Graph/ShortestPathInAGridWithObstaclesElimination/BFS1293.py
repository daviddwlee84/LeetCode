from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        BFS on (x,y,r) x,y is coordinate, r is remain number of obstacles you can remove.

        https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/451787/Python-O(m*n*k)-BFS-Solution-with-Explanation
        """
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        queue = deque([(0, 0, k, 0)])
        # The k here is the key, that we should try all the possible elimination
        visited = set((0, 0, k))
        while queue:
            x, y, r, step = queue.pop()

            # The end condition shouldn't be here, or it will TLE
            # if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
            #     return step

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newx, newy = x + dx, y + dy

                # This is wrong
                # if (newx, newy) in visited:
                #     continue

                if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]):
                    if r <= 0:
                        if grid[newx][newy] == 0:
                            if (newx, newy, r) not in visited:
                                queue.appendleft((newx, newy, r, step + 1))
                                visited.add((newx, newy, r))
                                if (newx, newy) == (len(grid) - 1, len(grid[0]) - 1):
                                    return step + 1
                    else:
                        if (newx, newy, r - int(grid[newx][newy])) not in visited:
                            queue.appendleft(
                                (newx, newy, r - int(grid[newx][newy] == 1), step + 1))
                            visited.add(
                                (newx, newy, r - int(grid[newx][newy] == 1)))
                            if (newx, newy) == (len(grid) - 1, len(grid[0]) - 1):
                                return step + 1

        return -1

# Runtime: 1020 ms, faster than 13.75% of Python3 online submissions for Shortest Path in a Grid with Obstacles Elimination.
# Memory Usage: 22.8 MB, less than 10.02% of Python3 online submissions for Shortest Path in a Grid with Obstacles Elimination.
