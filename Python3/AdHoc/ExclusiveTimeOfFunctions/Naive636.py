from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        Stack

        https://leetcode.com/problems/exclusive-time-of-functions/solution/
        https://leetcode.com/problems/exclusive-time-of-functions/discuss/105100/Python-Straightforward-with-Explanation
        """
        exclusive_times = [0] * n

        stack = []  # keep track of the "current function"
        prev_t = 0

        for log in logs:
            index, op, t = log.split(':')
            index = int(index)
            t = int(t)

            # Don't have to do like this
            # We don't care if the index of function is equal to current one
            # We just settle the time
            # if stack and stack[-1][0] == index:
            #     exclusive_times

            if op == 'start':
                if stack:
                    exclusive_times[stack[-1]] += t - prev_t
                stack.append(index)
                prev_t = t
            else:
                exclusive_times[stack.pop()] += t - prev_t + 1
                prev_t = t + 1

        return exclusive_times

# Runtime: 80 ms, faster than 30.60% of Python3 online submissions for Exclusive Time of Functions.
# Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Exclusive Time of Functions.
