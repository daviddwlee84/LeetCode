from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        society_level = [0] * N
        suspicion_level = [0] * N

        for a, b in trust:
            # - 1 because trust index from 1
            society_level[b - 1] += 1
            suspicion_level[a - 1] += 1

        for i in range(N):
            if society_level[i] == N - 1 and suspicion_level[i] == 0:
                return i + 1

        return -1

# Runtime: 792 ms, faster than 63.51% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 18.2 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
