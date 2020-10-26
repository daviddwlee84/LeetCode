from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/merge-intervals/solution/
        """

        intervals.sort()

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

# Runtime: 120 ms, faster than 19.59% of Python3 online submissions for Merge Intervals.
# Memory Usage: 15.9 MB, less than 92.25% of Python3 online submissions for Merge Intervals.