from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []  # store index
        res = [0] * len(T)  # answer

        for i, t in enumerate(T):

            # if found a higher one then pop
            while stack and T[stack[-1]] < t:
                res[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)
        return res

# Runtime: 480 ms, faster than 95.43% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 16.6 MB, less than 73.68% of Python3 online submissions for Daily Temperatures.
