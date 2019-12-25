from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # the answer should be minimum of dp[n], n is the number of rows
        min_val = []
        min_val.append([triangle[0][0]])
        for row in range(1, len(triangle)):
            min_val.append([-1] * len(triangle[row]))
            for col in range(len(triangle[row])):
                if col == 0:
                    min_val[row][col] = min_val[row-1][col] + \
                        triangle[row][col]
                elif col == len(triangle[row]) - 1:
                    min_val[row][col] = min_val[row-1][len(triangle[row-1])-1] + \
                        triangle[row][col]
                else:
                    min_val[row][col] = min(
                        min_val[row - 1][col - 1], min_val[row - 1][col]) + triangle[row][col]

        return min(min_val[-1])


# Runtime: 64 ms, faster than 70.10 % of Python3 online submissions for Triangle.
# Memory Usage: 13.6 MB, less than 46.67 % of Python3 online submissions for Triangle.
