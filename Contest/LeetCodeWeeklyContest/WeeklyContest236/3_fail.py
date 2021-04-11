from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:

        self.side_jumps = float('inf')

        def dfs(pos: int, track: int, jumps: int):
            if pos == len(obstacles):
                self.side_jumps = min(self.side_jumps, jumps)
                return

            if obstacles[pos] == track:
                return

            for next_track in range(1, 4):
                if next_track != obstacles[pos]:
                    dfs(pos + 1, next_track, jumps + (next_track != track))

        dfs(0, 2, 0)
        return self.side_jumps

# TLE
# [0,2,2,1,0,3,0,3,0,1,3,1,1,0,1,3,1,1,1,0,2,0,0,3,3,0,3,2,2,0,0,3,3,3,0,0,2,0,0,3,3,0,3,3,0,0,3,1,0,1,0,2,3,1,1,0,3,3,0,3,1,3,0,2,2,0,1,3,0,1,0,3,0,1,3,1,2,2,0,0,3,0,1,3,2,3,2,1,0,3,2,2,0,3,3,0,3,0,0,1,0]
