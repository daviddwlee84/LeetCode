from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 2:
            return False
        elif len(coordinates) == 2:
            return True

        if coordinates[1][0] - coordinates[0][0] == 0:
            vertical = True
        else:
            vertical = False
            slope = (coordinates[1][1] - coordinates[0][1]) / \
                (coordinates[1][0] - coordinates[0][0])

        for x, y in coordinates[2:]:
            if vertical and x != coordinates[0][0]:
                return False
            elif not vertical and (x == coordinates[0][0] or (y - coordinates[0][1]) / (x - coordinates[0][0]) != slope):
                return False

        return True

# Runtime: 68 ms, faster than 20.60% of Python3 online submissions for Check If It Is a Straight Line.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Check If It Is a Straight Line.

# Other styles
#
# class Solution:
#     def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
#         try:  # general case
#             return len(set([(coordinates[i+1][1] - coordinates[i][1]) / (coordinates[i+1][0] - coordinates[i][0]) for i in range(len(coordinates) - 1)])) == 1
#         except: # check vertical line
#             return len(set([(coordinates[i+1][0] - coordinates[i][0]) for i in range(len(coordinates) - 1)])) == 1
#
#
# class Solution:
#     def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
#         n = len(coordinates)
#         if n < 2:
#             return False
#         if n == 2:
#             return True
#         xs = [coordinates[i][0] for i in range(n)]
#
#         if max(xs) == min(xs):
#             return True
#
#         i = 1
#         while coordinates[i][0] == coordinates[1][0]:
#             i += 1
#
#         k = (coordinates[i][1]-coordinates[0][1]) /(coordinates[i][0]-coordinates[0][0])
#         b = coordinates[0][1] - k * coordinates[0][0]
#
#         for i in range(2,n):
#             if abs(coordinates[i][1] - k * coordinates[i][0] - b) > 0.0001:
#                 return False
#
#         return True
