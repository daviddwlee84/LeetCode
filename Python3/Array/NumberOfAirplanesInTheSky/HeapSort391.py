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
        # sorting flights by start time in ascending order
        airplanes.sort(key=lambda x: x.start)

        ans = 0

        # heap: keep track of end time; the size of heap is the number of flight in the air
        in_the_air = []

        for plane in airplanes:

            # if start time is greater or equal than the min end time
            while in_the_air and plane.start >= in_the_air[0]:
                # pop all the planes need to be landing first
                heapq.heappop(in_the_air)

            # push the current end time into heap
            heapq.heappush(in_the_air, plane.end)

            # update the answer
            ans = max(ans, len(in_the_air))

        return ans
