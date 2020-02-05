from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []  # store index (days haven't found warmer day)
        res = [0] * len(T)  # answer

        for i, t in enumerate(T):

            # If found a higher one then pop
            while stack and T[stack[-1]] < t:
                # t => current highest temperature
                # pop for any temperature is less than t
                res[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)
        return res

# Runtime: 480 ms, faster than 95.43% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 16.6 MB, less than 73.68% of Python3 online submissions for Daily Temperatures.
