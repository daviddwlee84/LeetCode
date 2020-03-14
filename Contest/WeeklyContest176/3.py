from typing import List

import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # sort according to start time
        events = sorted(events)

        # find the maximum end time
        total_days = max(event[1] for event in events)

        # to keep track of the minimal end time (the event ends the earliest)
        min_heap = []

        day = 1  # because the first day is index 1
        cnt = 0  # the answer
        event_id = 0  # to keep track of the event

        while day <= total_days:
            # if no events are available to attend today, let time flies to the next available event
            # (because the earliest start day is not necessary to be day 1)
            if event_id < len(events) and not min_heap:
                day = events[event_id][0]

            # all events starting from today are newly available. add them to the heap
            while event_id < len(events) and events[event_id][0] <= day:
                heapq.heappush(min_heap, events[event_id][1])
                event_id += 1

            # if the event at heap top already ended, then discard it
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # attend the event that will end the earliest
            if min_heap:
                heapq.heappop(min_heap)
                cnt += 1
            elif event_id >= len(events):
                break  # no more events to attend

            day += 1

        return cnt

# Runtime: 920 ms, faster than 62.12% of Python3 online submissions for Maximum Number of Events That Can Be Attended.
# Memory Usage: 50.8 MB, less than 100.00% of Python3 online submissions for Maximum Number of Events That Can Be Attended.
