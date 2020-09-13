from typing import List
from collections import defaultdict, deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        rotten_queue = deque()  # (i, j, day)
        fresh_set = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    if grid[i][j] == 1:
                        fresh_set.add((i, j))
                    if grid[i][j] == 2:
                        rotten_queue.appendleft(((i, j), 0))

                    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]):
                            if grid[i + di][j + dj] > 0:
                                adj_list[(i, j)].append((i + di, j + dj))

        day = 0
        while rotten_queue:
            rotten, day = rotten_queue.pop()
            for adj in adj_list[rotten]:
                if adj in fresh_set:
                    fresh_set.remove(adj)
                    rotten_queue.appendleft((adj, day + 1))

        if fresh_set:
            return -1

        return day


# Runtime: 60 ms, faster than 32.73% of Python3 online submissions for Rotting Oranges.
# Memory Usage: 13.9 MB, less than 52.18% of Python3 online submissions for Rotting Oranges.
