from typing import List
import numpy as np


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/interval-list-intersections/solution/
        https://leetcode.com/problems/interval-list-intersections/discuss/647482/Python-Two-Pointer-Approach-%2B-Thinking-Process-Diagrams
        """
        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # low - the startpoint of the intersection
            # high - the endpoint of the intersection
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])

            if low <= high:
                result.append([low, high])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return result

# Runtime: 212 ms, faster than 17.66% of Python3 online submissions for Interval List Intersections.
# Memory Usage: 14.6 MB, less than 6.06% of Python3 online submissions for Interval List Intersections.
