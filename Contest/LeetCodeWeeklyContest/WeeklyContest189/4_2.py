from typing import List
from collections import defaultdict
from itertools import combinations


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        diameter_square = (2 * r) ** 2
        all_points_tuple_set = set([tuple(point) for point in points])

        disance_in_range = []
        max_count = 1
        for point_A in points:
            distance_in_As_range = []
            for point_B in points:
                if (point_A[0] - point_B[0]) ** 2 + (point_A[1] - point_B[1]) ** 2 <= diameter_square:
                    distance_in_As_range.append(tuple(point_B))

            disance_in_range.append(set(distance_in_As_range))

        for points_to_cal in range(len(points), 1, -1):
            subsets = combinations(disance_in_range, points_to_cal)
            in_range_intersection = all_points_tuple_set.copy()

            for subset in subsets:
                for point_subset in subset:
                    in_range_intersection &= point_subset
                    if len(in_range_intersection) > max_count:
                        max_count = len(in_range_intersection)

                    if max_count >= points_to_cal:
                        return max_count

        return max_count

# WA (can't pass fourth case)
# Input: points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
# Output: 4
