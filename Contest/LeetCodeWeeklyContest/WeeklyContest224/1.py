from typing import List
from collections import Counter


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        min_edge_count = Counter([min(rect_edge) for rect_edge in rectangles])
        max_key = max(min_edge_count)
        return min_edge_count[max_key]
