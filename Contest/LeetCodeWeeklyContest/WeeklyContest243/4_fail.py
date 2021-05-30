from typing import List
import math
from itertools import combinations


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:

        def total_time(skips: List[int]) -> int:
            time = 0
            temp = 0
            for i, d in enumerate(dist):
                if i in skips:
                    temp += d
                else:
                    if i == len(dist) - 1:
                        time += (d + temp) / speed
                    else:
                        time += math.ceil((d + temp) / speed)
                    temp = 0

            if temp:
                # skip on the last one
                time += temp / speed

            return time

        candidates = [i for i in range(len(dist))]
        for skip_num in range(len(dist)):
            if skip_num == 0:
                time = total_time([])
                if time <= hoursBefore:
                    return skip_num
            else:
                for skips in combinations(candidates, skip_num):
                    time = total_time(skips)
                    if time <= hoursBefore:
                        return skip_num
        return -1

# TLE
# [18,66,64,12,97,7,15,20,81,21,88,55,77,9,50,49,77,60,68,33,71,2,88,93,15,88,69,97,35,99,83,44,15,38,56,21,59,1,93,93,34,65,98,23,65,14,81,39,82,65,78,26,20,48,98,21,70,100,68,1,77,42,63,3]
# 17
# 160
