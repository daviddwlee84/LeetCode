from typing import List
import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def count_of_airplanes(self, airplanes: List[Interval]) -> int:
        sweep_line = []
        for airplane in airplanes:
            # end set to 0 to make sure it will be operate before take off 1
            sweep_line.append((airplane.start, 1))
            sweep_line.append((airplane.end, 0))
        
        sweep_line.sort()

        ans = 0
        temp = 0
        for _, is_start in sweep_line:
            if is_start:
                # start a plane
                temp += 1
            else:
                # land a plane
                temp -= 1

            ans = max(ans, temp)
        return ans
