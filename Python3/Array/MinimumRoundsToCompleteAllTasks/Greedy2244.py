from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)

        answer = 0
        base_cases = {
            0: 0,
            1: -1,
            2: 1,
            3: 1,
            4: 2,
            5: 2
        }
        for count in counter.values():
            while count not in base_cases:
                count -= 3
                answer += 1

            if base_cases[count] >= 0:
                answer += base_cases[count]
            else:
                return -1

        return answer
