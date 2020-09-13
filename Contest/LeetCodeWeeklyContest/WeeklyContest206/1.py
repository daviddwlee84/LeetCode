from typing import List
from itertools import product


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        Brute Force
        """

        def test_ij(i: int, j: int):
            for ii in range(len(mat)):
                if mat[ii][j] == 1 and ii != i:
                    return False

            for jj in range(len(mat[0])):
                if mat[i][jj] == 1 and jj != j:
                    return False

            return True

        count = 0
        for i, j in product(range(len(mat)), range(len(mat[0]))):
            if mat[i][j] == 1:
                count += test_ij(i, j)
        return count


if __name__ == "__main__":
    mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
    print(Solution().numSpecial(mat))
