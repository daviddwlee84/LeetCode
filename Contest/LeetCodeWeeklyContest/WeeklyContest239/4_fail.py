from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        answer = []
        for query in queries:
            min_length = float('inf')
            for start, end in intervals:
                if start <= query <= end:
                    min_length = min(end - start + 1, min_length)
            answer.append(min_length if min_length != float('inf') else -1)

        return answer

# TLE