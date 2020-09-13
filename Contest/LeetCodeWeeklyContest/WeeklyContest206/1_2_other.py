from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        Alex Wice's Answer

        Row and Column sum
        """

        R, C = len(mat), len(mat[0])
        rowsums = [0] * R
        colsums = [0] * C
        for r in range(R):
            for c in range(C):
                if mat[r][c]:
                    rowsums[r] += 1
                    colsums[c] += 1
        
        ans = 0
        for r in range(R):
            for c in range(C):
                if mat[r][c]:
                    if rowsums[r] == colsums[c] == 1:
                        ans += 1
        
        return ans