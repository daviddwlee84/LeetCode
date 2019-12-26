from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        temp_pos = {}
        reversed_output = []
        while T:
            lastTemp = T.pop()
            lastPos = len(T)
            nearest = float('inf')
            for value, pos in temp_pos.items():
                if value > lastTemp and pos - lastPos < nearest:
                    nearest = pos - lastPos

            if nearest == float('inf'):
                reversed_output.append(0)
            else:
                reversed_output.append(nearest)

            temp_pos[lastTemp] = lastPos

        return list(reversed(reversed_output))

# Runtime: 968 ms, faster than 10.07% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 16.5 MB, less than 89.47% of Python3 online submissions for Daily Temperatures.
