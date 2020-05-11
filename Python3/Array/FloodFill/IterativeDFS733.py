from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        X, Y = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        
        frontier_stack = [(sr, sc)]
        while len(frontier_stack) > 0:
            point = frontier_stack.pop()
            x, y = point[0], point[1]
            image[x][y] = newColor
            
            candidates = ((x + 1, y),
                          (x - 1, y),
                          (x, y + 1),
                          (x, y - 1),)

            for cand in candidates:
                x, y = cand[0], cand[1]
                if x >= X or x < 0 or y >= Y or y < 0:
                    continue
                if image[x][y] == color:
                    frontier_stack.append(cand)
        
        return image