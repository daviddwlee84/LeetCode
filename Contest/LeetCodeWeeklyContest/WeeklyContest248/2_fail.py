from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        if any(d <= 0 for d in dist):
            return 0

        killed = [False] * len(dist)

        eliminated = 0
        while eliminated < len(dist):

            dist_speed = [(d, -s, i) for i, (d, s, k)
                          in enumerate(zip(dist, speed, killed)) if not k]

            # Find the closest and fastest monster to kill (wrong)
            _, _, i = sorted(dist_speed)[0]
            killed[i] = True
            eliminated += 1

            for i in range(len(dist)):
                if not killed[i]:
                    dist[i] -= speed[i]

                    if dist[i] <= 0:
                        return eliminated

        return eliminated

# WA
# [4,2]
# [5,1]
# 2 (got 1)
