from typing import List
from itertools import combinations


class Solution:
    def maxArea(self, height: List[int]) -> int:
        height_with_idx = [(i, h) for i, h in enumerate(height)]
        max_area = 0
        for left, right in combinations(height_with_idx, 2):
            max_area = max(max_area,
                           (right[0] - left[0]) * min(left[1], right[1]))

        return max_area

# TLE
