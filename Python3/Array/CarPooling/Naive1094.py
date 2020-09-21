import numpy as np


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Actually this is kind of a "bucket sort"
        """
        max_passenger = np.zeros((1000, ))
        for n, s, e in trips:
            max_passenger[s:e] += n
        return max(max_passenger) <= capacity
