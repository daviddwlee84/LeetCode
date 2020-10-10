from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        number = len(points)
        overlap_end = None
        for point in points:
            if overlap_end and overlap_end >= point[0]:
                number -= 1
                overlap_end = min(overlap_end, point[1])
            else:
                overlap_end = point[1]

        return number

# Runtime: 464 ms, faster than 43.87% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
# Memory Usage: 19.2 MB, less than 97.86% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
