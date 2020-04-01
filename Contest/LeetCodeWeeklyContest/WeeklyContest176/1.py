from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        answer = 0

        for row in grid:
            for item in row:
                if item < 0:
                    answer += 1

        return answer
