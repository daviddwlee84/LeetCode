from typing import List
import math


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        """
        https://stackoverflow.com/questions/42258637/how-to-know-the-angle-between-two-points
        """
        max_count = 0
        x, y = location[0], location[1]
        for center_point in points:
            count = 0
            center_degree = math.degrees(math.atan2(
                center_point[1] - y, center_point[0] - x))
            max_degree = center_degree + angle / 2
            min_degree = center_degree - angle / 2

            print(min_degree, center_degree, max_degree)

            for point in points:
                degree = math.degrees(math.atan2(point[1] - y, point[0] - x))

                if point == location:
                    count += 1
                    continue

                print(point, degree, end=' ')
                if max_degree >= degree >= min_degree:
                    print('count!', end='')
                    count += 1
                print()

            max_count = max(max_count, count)

        return max_count

# WA (solved)
#
# [[1,1],[2,2],[3,3],[4,4],[1,2],[2,1]]
# 0
# [1,1]
#
# 4

# WA => shows that we can't use each point as center point
#
# [[0,0],[0,2]]
# 90
# [1,1]
#
# 2
