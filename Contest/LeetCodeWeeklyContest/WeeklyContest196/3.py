from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/720227/Pre-computation-VIDEO-solution-O(m*n*n)
        https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/720265/Java-Detailed-Explanation-From-O(MNM)-to-O(MN)-by-using-Stack
        """
        m, n = len(mat), len(mat[0])
        arr = [[0] * n for _ in range(m)]

        # pre computation
        # "compress" the 2D array to the 1D array
        for i in range(m):
            count = 0
            for j in reversed(range(n)):
                if mat[i][j] == 1:
                    count += 1
                else:
                    count = 0
                arr[i][j] = count

        # storing the 1s of the right (from left to right)
        # print(arr)

        answer = 0
        for i in range(m):
            for j in range(n):
                # i, j is the top most left point of the rectangle
                count = float('inf')
                for k in range(i, n):
                    count = min(count, arr[k][j])
                    answer += count

        return answer
