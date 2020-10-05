from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_distance = 0
        cur_min = float('inf')
        cur_max = -float('inf')

        for arr in arrays:
            max_distance = max(arr[-1] - cur_min,
                               cur_max - arr[0], max_distance)
            cur_min = min(arr[0], cur_min)
            cur_max = max(arr[-1], cur_max)

        return max_distance
