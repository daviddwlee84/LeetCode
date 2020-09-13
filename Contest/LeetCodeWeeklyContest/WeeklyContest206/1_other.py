from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        Alex Wice's Answer
        """

        ans = 0
        for r, row in enumerate(mat):
            if sum(row) == 1:
                c = row.index(1)
                if sum(mat[r0][c] for r0 in range(len(mat))) == 1:
                    ans += 1
        
        return ans