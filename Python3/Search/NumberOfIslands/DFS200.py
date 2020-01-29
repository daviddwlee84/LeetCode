from typing import List

toSearch = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 0),  # up
]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        count = 0

        self.height = len(grid)
        self.width = len(grid[0])

        self.not_visited = set([(i, j)
                                for i in range(self.height)
                                for j in range(self.width)])

        while self.not_visited:
            y, x = self.not_visited.pop()
            if grid[y][x] == '1':
                self.dfs(x, y, grid)
                count += 1

        return count

    def dfs(self, start_x: int, start_y: int, grid: List[List[str]]):
        """ visit all the point of the island """
        for delta_x, delta_y in toSearch:
            new_x = start_x + delta_x
            new_y = start_y + delta_y
            if 0 <= new_x < self.width and 0 <= new_y < self.height:
                if (new_y, new_x) in self.not_visited:
                    self.not_visited.remove((new_y, new_x))
                    if grid[new_y][new_x] == '1':
                        self.dfs(new_x, new_y, grid)
