from collections import Counter
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        answer = ''
        heap = []
        for char, freq in Counter(s).items():
            # max heap
            heapq.heappush(heap, (-freq, char))

        while heap:
            freq, char = heapq.heappop(heap)
            answer += -freq * char

        return answer

# Runtime: 40 ms, faster than 75.30% of Python3 online submissions for Sort Characters By Frequency.
# Memory Usage: 15 MB, less than 7.14% of Python3 online submissions for Sort Characters By Frequency.
