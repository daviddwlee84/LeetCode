from typing import List, Tuple
from HeapSort391 import Solution as HeapSort


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


testcases = [
    ([(1, 10), (2, 3), (5, 8), (4, 7)], 3),
    ([(1, 2), (2, 3), (3, 4)], 1),
    ([(1, 4), (1, 4), (1, 4)], 3),
    ([(1, 10), (10, 20), (20, 30), (30, 40)], 1),
    ([(10, 14), (10, 15), (10, 16), (1, 10), (2, 10), (3, 10), (4, 10)], 4),
    ([(52, 61), (54, 59), (34, 35), (28, 37), (94, 97), (96, 100), (76, 85), (77, 87), (77, 87), (21, 24), (9, 15), (45, 55), (99, 103), (58, 66), (35, 43), (23, 27), (40, 49), (45, 49), (13, 19), (37, 42), (31, 32), (5, 11), (83, 89), (90, 97), (36, 41), (90, 97), (91, 98), (98, 101), (93, 102), (80, 85),
     (60, 62), (72, 79), (85, 87), (77, 86), (93, 103), (64, 74), (62, 69), (77, 78), (71, 74), (47, 53), (21, 29), (43, 50), (30, 34), (68, 75), (53, 61), (3, 10), (8, 9), (14, 21), (32, 40), (10, 15), (91, 96), (6, 11), (16, 23), (27, 31), (51, 58), (73, 74), (98, 106), (51, 58), (10, 17), (24, 34)], 7)
]


def _convert_intervals(list_intervals: List[Tuple[int, int]]):
    result = []
    for start, end in list_intervals:
        result.append(Interval(start, end))
    return result


def test_HeapSort():
    for airplanes, ans in testcases:
        assert HeapSort().count_of_airplanes(
            _convert_intervals(airplanes)) == ans


# Wrong Answer

# class Solution:
#     """
#     @param airplanes: An interval array
#     @return: Count of airplanes are in the sky.
#     """
#     def count_of_airplanes(self, airplanes: List[Interval]) -> int:
#         if len(airplanes) < 2:
#             return len(airplanes)
#         airplanes = sorted(airplanes, key=lambda x: (x.end, x.start))
#
#         ans = 0
#         temp = 0
#         for i in range(len(airplanes) - 1):
#             if airplanes[i].end > airplanes[i + 1].start:
#                 temp += 1
#             else:
#                 ans = max(ans, temp)
#                 temp  = 0
#             print(temp)
#
#         ans = max(ans, temp)
#
#         return ans + 1

# class Solution:
#     """
#     @param airplanes: An interval array
#     @return: Count of airplanes are in the sky.
#     """
#     def count_of_airplanes(self, airplanes: List[Interval]) -> int:
#         if len(airplanes) < 2:
#             return len(airplanes)
#         airplanes = sorted(airplanes, key=lambda x: (x.end, x.start))
#
#         i = 0
#         ans = 0
#         while i < len(airplanes) - 1:
#             curr = airplanes[i]
#             temp = 1
#             i += 1
#             while i < len(airplanes) and curr.end > airplanes[i].start:
#                 i += 1
#                 temp += 1
#
#             ans = max(ans, temp)
#
#         return ans

# class Solution:
#     """
#     @param airplanes: An interval array
#     @return: Count of airplanes are in the sky.
#     """
#     def count_of_airplanes(self, airplanes: List[Interval]) -> int:
#         if len(airplanes) < 2:
#             return len(airplanes)
#         airplanes = sorted(airplanes, key=lambda x: (x.end, x.start))
#
#         ans = 0
#         for i in range(len(airplanes) - 1):
#             temp = 1
#             for j in range(i + 1, len(airplanes)):
#                 if airplanes[i].end > airplanes[j].start:
#                     temp += 1
#                 else:
#                     break
#             print((airplanes[i].start, airplanes[i].end), ans, temp)
#             ans = max(ans, temp)
#
#         return ans
