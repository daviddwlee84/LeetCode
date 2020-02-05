from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        output = []
        for i in range(len(T)):
            next_day = 0
            j = i

            while j < len(T):
                # Attempt to find the closest warmer day
                j += 1
                next_day += 1

                if j == len(T):
                    # If reach the end then must be not found
                    next_day = 0
                    break

                if T[i] < T[j]:
                    # If found any
                    break

            output.append(next_day)

        return output

# Time Limit Exceeded
