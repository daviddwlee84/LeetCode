from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        answer = 0

        for i in range(len(light)):
            sorted_bulb = sorted(light[:i+1])
            if sorted_bulb[0] == 1 and sorted_bulb[-1] == i + 1:
                answer += 1

        return answer

# didn't test
