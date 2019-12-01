from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        if rows == 0 and cols == 0:
            return 0
        
        grid1d = [item for items in grid for item in items]
        
        k %= rows * cols 
        
        new_grid1d = grid1d[-k:] + grid1d[:-k]
        
        new_grid2d = [[new_grid1d[i*cols + j] for j in range(cols)] for i in range(rows)]
        
        return new_grid2d

if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    # [[9,1,2],[3,4,5],[6,7,8]]
    print(Solution().shiftGrid(grid, k))

    grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
    k = 4
    # [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
    print(Solution().shiftGrid(grid, k))

    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 9
    # [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().shiftGrid(grid, k))
