from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.m, self.n = len(image), len(image[0])
        self.newColor = newColor
        self.centerColor = image[sr][sc]
        self.visited = set()  # actually we don't need this, because we will change its color after visit it
        self.paintSurrounding(sr, sc)
        return self.image

    def paintSurrounding(self, row: int, col: int):
        self.visited.add((row, col))
        if 0 <= row < self.m and 0 <= col < self.n:
            if self.image[row][col] == self.centerColor:
                self.image[row][col] = self.newColor

                if (row + 1, col) not in self.visited:
                    self.paintSurrounding(row + 1, col)
                if (row - 1, col) not in self.visited:
                    self.paintSurrounding(row - 1, col)
                if (row, col + 1) not in self.visited:
                    self.paintSurrounding(row, col + 1)
                if (row, col - 1) not in self.visited:
                    self.paintSurrounding(row, col - 1)

# Runtime: 80 ms, faster than 54.79% of Python3 online submissions for Flood Fill.
# Memory Usage: 14 MB, less than 5.56% of Python3 online submissions for Flood Fill.
