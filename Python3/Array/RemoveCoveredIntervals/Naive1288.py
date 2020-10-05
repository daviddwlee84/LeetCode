from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        Kind of greedy
        """
        # sorted by accending end time and decending start time
        intervals.sort(key=lambda x: (x[1], -x[0]))

        def coveredBy(small_interval: List[int], large_interval: List[int]) -> bool:
            return large_interval[1] >= small_interval[1] and large_interval[0] <= small_interval[0]

        # print(intervals)
        to_remove = 0
        # TODO: this part should have some ways to improve
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if coveredBy(intervals[i], intervals[j]):
                    # remove i because of j cover it
                    # print(intervals[i], intervals[j])
                    to_remove += 1
                    break

        return len(intervals) - to_remove

# Runtime: 108 ms, faster than 41.65% of Python3 online submissions for Remove Covered Intervals.
# Memory Usage: 14.7 MB, less than 5.08% of Python3 online submissions for Remove Covered Intervals.
