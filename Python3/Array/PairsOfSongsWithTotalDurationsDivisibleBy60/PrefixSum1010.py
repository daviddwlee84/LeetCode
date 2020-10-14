from collections import Counter
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = Counter()
        answer = 0
        for i in range(len(time)):
            time[i] %= 60

            if 60 - time[i] in counter:
                answer += counter[60 - time[i]]

            counter[time[i]] += 1

        return answer

# Runtime: 252 ms, faster than 37.99% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
# Memory Usage: 17.4 MB, less than 39.64% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
