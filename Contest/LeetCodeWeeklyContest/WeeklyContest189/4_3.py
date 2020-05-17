from typing import List
from itertools import combinations
import math


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        self.points = points
        self.r_square = r ** 2

        # get all candidate centroid (center of circle)
        any_two_points = combinations(self.points, 2)
        centroid_to_test = []
        for two_point in any_two_points:
            centroid_to_test.extend(
                self.getIntersectCentroidOfTwoPoint(*two_point, r))

        # find the max point it can include
        max_points = 1
        for centroid in centroid_to_test:
            num_in_circle = self.numInCircle(centroid)
            if num_in_circle > max_points:
                max_points = num_in_circle

        return max_points

    def getIntersectCentroidOfTwoPoint(self, pointA: List[int], pointB: List[int], r: int) -> List[int]:
        (x1, y1), (x2, y2) = pointA, pointB

        # delta x, delta y between points
        dx, dy = x2 - x1, y2 - y1

        # dist between points
        q = math.sqrt(dx**2 + dy**2)

        # if two points are too far away, there is no such circle
        if q > 2.0 * r:
            return []

        # find the halfway point
        x3, y3 = (x1 + x2) / 2, (y1 + y2) / 2

        # distance along the mirror line
        d = math.sqrt(r**2 - (q / 2)**2)

        # One circle
        c1 = [x3 - d * dy / q, y3 + d * dx / q]

        # The other circle
        c2 = [x3 + d * dy / q, y3 - d * dx / q]
        if c1 == c2:
            return [c1]
        return [c1, c2]

    def numInCircle(self, centroid: List[int]) -> int:
        count = 0
        for point in self.points:
            if self.isIncircle(point, centroid):
                count += 1

        return count

    def isIncircle(self, point: List[int], centroid: List[int]) -> bool:
        # + 10**-6 is very important
        # or case like
        # [[4,5],[-4,1],[-3,2],[-4,0],[0,2]]
        # 5
        # will count one less due to the little error
        return (point[0] - centroid[0])**2 + (point[1] - centroid[1])**2 <= self.r_square + 10**-6

# Runtime: 1408 ms, faster than 41.18% of Python3 online submissions for Maximum Number of Darts Inside of a Circular Dartboard.
# Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Maximum Number of Darts Inside of a Circular Dartboard.
