from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/720265/Java-Detailed-Explanation-From-O(MNM)-to-O(MN)-by-using-Stack
        https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/720114/python-o(mn)-solution-w-a-stack
        """
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] and i - 1 >= 0:
                    mat[i][j] += mat[i-1][j]

        # storing how many 1s above
        # print(mat)

        # count submatrices with all 1s with bottom left corner at (i, j)
        answer = 0
        for i in range(m):
            row = mat[i]
            stack = []
            total = 0
            for j in range(n):
                count = 1
                while stack and stack[-1][0] >= row[j]:
                    pre_height, pre_count = stack.pop()
                    # undo previous count
                    total -= pre_height * pre_count
                    count += pre_count

                stack.append((row[j], count))
                total += row[j] * count
                answer += total
        return answer

# Runtime: 268 ms, faster than 100.00% of Python3 online submissions for Count Submatrices With All Ones.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Count Submatrices With All Ones.
