from typing import List
from collections import deque, defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        """
        Alex Wice's Solution
        """
        edges = defaultdict(list)
        for pair in adjacentPairs:
            edges[pair[0]].append(pair[1])
            edges[pair[1]].append(pair[0])

        ans = deque(adjacentPairs[0])
        while len(edges[ans[-1]]) == 2:
            for v in edges[ans[-1]]:
                if v != ans[-2]:
                    ans.append(v)
                    break

        while len(edges[ans[0]]) == 2:
            for v in edges[ans[0]]:
                if v != ans[1]:
                    ans.appendleft(v)
                    break

        return list(ans)
