from typing import List
import numpy as np


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        matrix = np.array(matrix)
        min_row = set(matrix.min(axis=1))
        max_column = set(matrix.max(axis=0))
        return list(min_row & max_column)


if __name__ == "__main__":

    matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    print(Solution().luckyNumbers(matrix))
