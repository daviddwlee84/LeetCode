from typing import List
from itertools import product


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_sum = [0] * len(mat)
        for i, row in enumerate(mat):
            row_sum[i] = sum(row)

        trans_mat = [*zip(*mat)]

        col_sum = [0] * len(trans_mat)
        for i, col in enumerate(trans_mat):
            col_sum[i] = sum(col)

        print(trans_mat)
        print(row_sum, col_sum)

        count = 0
        for r, c in product(row_sum, col_sum):
            if r == c == 1:
                count += 1
        return count


if __name__ == "__main__":
    mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
    print(Solution().numSpecial(mat))
