from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        beTrustBy = defaultdict(set)
        trustedOthers = set()
        allPeople = set(range(1, N+1))

        for a, b in trust:
            beTrustBy[b].add(a)
            trustedOthers.add(a)

        if not beTrustBy and len(allPeople) == 1:
            return N

        for people, trustBy in beTrustBy.items():
            if trustBy == allPeople - set([people]) and people not in trustedOthers:
                return people

        return -1

# Runtime: 872 ms, faster than 17.98% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 18.3 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
