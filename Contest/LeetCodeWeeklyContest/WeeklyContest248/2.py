from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        if any(d <= 0 for d in dist):
            return 0

        dist_speed = sorted([((d / s), i)
                             for i, (d, s) in enumerate(zip(dist, speed))])

        for j, (_, i) in enumerate(dist_speed):

            if dist[i] - speed[i] * j <= 0:
                return j

        return len(dist)
