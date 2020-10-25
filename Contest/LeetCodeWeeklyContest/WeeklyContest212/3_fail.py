from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.answer = float('inf')
        rows = len(heights)
        cols = len(heights[0])

        def dfs(row: int, col: int, path_height: List[int]):
            if row == rows - 1 and col == cols - 1:
                return

            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= row + i < rows and 0 <= col + j < cols:
                    curr_effort = abs(
                        heights[row + i][col + j] - heights[row][col])
                    if curr_effort > self.answer:
                        continue

                    self.answer = curr_effort
                    dfs(row + i, col + j, path_height +
                        [heights[row + i][col + j]])

        dfs(0, 0, [heights[0][0]])
        return self.answer

# MLE
# this shouldn't work
# but with "visited", its hard to maintain the minimal effort
