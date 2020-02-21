from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting by the start time
        sortedIntervals = sorted(intervals, key=lambda interval: interval[0])
        answer = []
        temp_interval = None
        for interval in sortedIntervals:
            if not temp_interval:
                temp_interval = interval.copy()
                continue

            if temp_interval[1] >= interval[0]:
                if interval[1] > temp_interval[1]:
                    temp_interval[1] = interval[1]
            else:
                answer.append(temp_interval)
                temp_interval = interval.copy()

        if temp_interval:
            answer.append(temp_interval)

        return answer

# Runtime: 104 ms, faster than 17.62% of Python3 online submissions for Merge Intervals.
# Memory Usage: 14.7 MB, less than 6.52% of Python3 online submissions for Merge Intervals.
