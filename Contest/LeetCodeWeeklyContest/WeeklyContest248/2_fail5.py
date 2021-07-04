from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        if any(d <= 0 for d in dist):
            return 0

        dist_speed = sorted([((d / s), i)
                             for i, (d, s) in enumerate(zip(dist, speed))])

        eliminated = 0
        while eliminated < len(dist):

            eliminated += 1

            for i in range(eliminated, len(dist)):
                j = dist_speed[i][-1]
                if dist[j] - speed[j] * eliminated <= 0:
                    return eliminated

        return eliminated

# TLE
# Hidden for this testcase during contest.
