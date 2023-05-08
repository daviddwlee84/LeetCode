from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        indices = set()
        for i in range(n):
            # print(mat[i][i], mat[i][n - i - 1])
            indices.add((i, i))
            indices.add((i, n - i - 1))
        for x, y in indices:
            ans += mat[x][y]
        return ans
