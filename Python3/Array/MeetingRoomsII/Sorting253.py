import heapq
from interval import Interval
from typing import List


class Solution(object):
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        sortedInterval = sorted(intervals, key=lambda it: (it.start, it.end))
        minHeap = []  # to track the minimal end time

        for interval in sortedInterval:
            # the heapq.nsmallest(1, ...) is to simulate heap.peek()
            if len(minHeap) > 0 and heapq.nsmallest(1, minHeap)[0] <= interval.start:
                # if the earlest end time is earlier than current start time,
                # that means they can share the same room (no conflict)
                # thus we can eliminate one number
                heapq.heappop(minHeap)

            heapq.heappush(minHeap, interval.end)

        return len(minHeap)
