from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        if rows * cols != r * c:
            # invalid r & c
            return mat

        mat_1d = []
        for i in range(rows):
            for j in range(cols):
                mat_1d.append(mat[i][j])

        new_mat = []
        for i in range(r):
            new_mat.append([])
            for j in range(c):
                new_mat[-1].append(mat_1d[i * c + j])

        return new_mat
