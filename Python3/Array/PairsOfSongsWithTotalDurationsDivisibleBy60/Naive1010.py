from typing import List
from itertools import combinations


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        for time_i, time_j in combinations(time, 2):
            if time_i + time_j % 60 == 0:
                count += 1

        return count
