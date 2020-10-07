from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        answer = []
        for s, e in intervals:
            if answer:
                if answer[-1][1] >= e:
                    continue

                if answer[-1][1] >= s:
                    answer[-1][1] = e
                    continue

            answer.append([s, e])

        return answer

# Runtime: 80 ms, faster than 96.24% of Python3 online submissions for Merge Intervals.
# Memory Usage: 15.8 MB, less than 10.11% of Python3 online submissions for Merge Intervals.
