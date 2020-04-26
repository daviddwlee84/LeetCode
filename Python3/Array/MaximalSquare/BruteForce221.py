from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Move diagonally (expand the square and check)
        """
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        maxsqlen = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    sqlen = 1
                    flag = True

                    while sqlen + i < rows and sqlen + j < cols and flag:
                        for k in range(j, sqlen + j + 1):
                            if matrix[i + sqlen][k] == '0':
                                flag = False
                                break

                        for k in range(i, sqlen + i + 1):
                            if matrix[k][j + sqlen] == '0':
                                flag = False
                                break

                        if flag:
                            sqlen += 1

                    if maxsqlen < sqlen:
                        maxsqlen = sqlen

        return maxsqlen ** 2

# Runtime: 352 ms, faster than 16.79% of Python3 online submissions for Maximal Square.
# Memory Usage: 14.3 MB, less than 9.09% of Python3 online submissions for Maximal Square.
