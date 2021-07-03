from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                top = self.prefix_sum[i - 1][j] if i > 0 else 0
                left = self.prefix_sum[i][j - 1] if j > 0 else 0
                top_left = self.prefix_sum[i -
                                           1][j - 1] if i > 0 and j > 0 else 0
                # self + top + left - top_left
                self.prefix_sum[i][j] += top + left - top_left

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.prefix_sum[row2][col1 - 1] if col1 > 0 else 0
        left = self.prefix_sum[row1 - 1][col2] if row1 > 0 else 0
        top_left = self.prefix_sum[row1 - 1][col1 -
                                             1] if row1 > 0 and col1 > 0 else 0
        # self - top - left + top_left
        return self.prefix_sum[row2][col2] - top - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Runtime: 616 ms, faster than 32.30% of Python3 online submissions for Range Sum Query 2D - Immutable.
# Memory Usage: 24.1 MB, less than 18.89% of Python3 online submissions for Range Sum Query 2D - Immutable.
