from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        if any(d <= 0 for d in dist):
            return 0

        killed = [False] * len(dist)

        eliminated = 0
        while eliminated < len(dist):

            dist_speed = [(d - s, d - s * 2, d - s * 3, d - s * 4, -s, d, i) for i, (d, s, k)
                          in enumerate(zip(dist, speed, killed)) if not k]

            # Find the next turn closest monster to kill
            i = sorted(dist_speed)[0][-1]
            killed[i] = True
            eliminated += 1

            for i in range(len(dist)):
                if not killed[i]:
                    dist[i] -= speed[i]

                    if dist[i] <= 0:
                        return eliminated

        return eliminated

# WA
# [46,33,44,42,46,36,7,36,31,47,38,42,43,48,48,25,28,44,49,47,29,32,30,6,42,9,39,48,22,26,50,34,40,22,10,45,7,43,24,18,40,44,17,39,36]
# [1,2,1,3,1,1,1,1,1,1,1,1,1,1,7,1,1,3,2,2,2,1,2,1,1,1,1,1,1,1,1,6,1,1,1,8,1,1,1,3,6,1,3,1,1]
# 7 (got 6)
