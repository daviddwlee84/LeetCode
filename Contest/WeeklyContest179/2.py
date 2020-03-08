from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        answer = 0
        max_open = -1
        moments = [[False for _ in range(len(light))]
                   for _ in range(len(light))]
        for i, curr_open in enumerate(light):
            # curr_open - 1 because index range from 1 ~ n
            if curr_open > max_open:
                max_open = curr_open
            for j in range(i, len(light)):
                moments[j][curr_open-1] = True

            if all(moments[i][:max_open-1]):
                answer += 1

        return answer

# TLE
