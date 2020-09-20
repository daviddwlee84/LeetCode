from itertools import permutations
from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        total_right = len(grid[0]) - 1
        total_down = len(grid) - 1

        total_moves = ['right'] * total_right + ['down'] * total_down

        answer = -1

        MOD = (10**9 + 7)

        for moves in permutations(total_moves):
            i, j = 0, 0
            value = grid[i][j]
            for move in moves:
                if move == 'right':
                    j += 1
                elif move == 'down':
                    i += 1

                value *= grid[i][j]

            if value >= 0:
                answer = max(answer, value) % MOD

        return answer

# TLE
# [[4,-3,0,-4,2,0,4],[3,-3,-4,2,-2,-3,-4],[-4,-4,-1,-2,-1,-2,4],[3,-4,-4,2,-4,-4,-2],[1,0,-3,-2,0,2,-1],[2,-4,0,-1,-2,-2,-3]]
