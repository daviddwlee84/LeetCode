from typing import List
from queue import Queue


toSearch = [
    (0, 1), # right
    (1, 0), # down
    (0, -1), # left
    (-1, 0), # up
]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        self.length = len(grid)
        self.width = len(grid[0])

        self.visited = [[0 for _ in range(self.width)] for _ in range(self.length)]
        numOfIsland = 0

        for i in range(self.length):
            for j in range(self.width):
                if grid[i][j] == '1' and self.visited[i][j] == 0:
                    print("Found an island start with", (i, j))
                    self.markIsland((i, j), grid)
                    numOfIsland += 1

        return numOfIsland


    def markIsland(self, start_position, grid):
        """ use BFS traverse all the lands of an island """
        queue = Queue()
        queue.put(start_position)

        y, x = start_position
        self.visited[y][x] = 1 # visited

        while not queue.empty():
            print(queue.queue)
            # iterate the nodes which are already in the queue
            for _ in range(queue.qsize()):
                y, x = queue.get()
                for x_dir, y_dir in toSearch:
                    new_x = x + x_dir
                    new_y = y + y_dir

                    # make sure the pixel to search is in the range of the grid
                    if 0 <= new_x < self.width and 0 <= new_y < self.length:
                        if self.visited[new_y][new_x] == 0:
                            if grid[new_y][new_x] == '1':
                                queue.put((new_y, new_x))
                            self.visited[new_y][new_x] = 1
