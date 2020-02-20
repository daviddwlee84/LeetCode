from interval import Interval
from typing import List


class Solution(object):
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        sortedInterval = sorted(intervals, key=lambda it: (it.start, it.end))
        previuosEnd = 0
        for interval in sortedInterval:
            if previuosEnd > interval.start:
                return False
            previuosEnd = interval.end

        return True
