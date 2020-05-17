from typing import List
from itertools import combinations


# https://benalexkeen.com/k-means-clustering-in-python/
# https://www.geeksforgeeks.org/permutation-and-combination-in-python/


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        self.points = points
        self.r_square = r ** 2
        num_point = len(points)
        max_points = 1
        for points_to_cal in range(num_point, 1, -1):
            subsets = combinations(self.points, points_to_cal)
            for subset in subsets:
                centroid = self.getMeanCentroid(subset, points_to_cal)
                num_in_circle = self.numInCircle(centroid)
                if num_in_circle > max_points:
                    max_points = num_in_circle
                if max_points >= points_to_cal:
                    break

            if max_points >= points_to_cal:
                break

        return max_points

    def getMeanCentroid(self, subset: List[List[int]], n: int) -> List[int]:
        x_sum = 0
        y_sum = 0
        for point in subset:
            x_sum += point[0]
            y_sum += point[1]

        return [x_sum / n, y_sum / n]

    def numInCircle(self, centroid: List[int]) -> int:
        count = 0
        for point in self.points:
            if self.isIncircle(point, centroid):
                count += 1

        return count

    def isIncircle(self, point: List[int], centroid: List[int]) -> bool:
        return (point[0] - centroid[0])**2 + (point[1] - centroid[1])**2 <= self.r_square

# WA (can't pass second case)
# Input: points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
# Output: 5
# Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all points except the point (7,8).
