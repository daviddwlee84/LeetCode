from typing import List
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        """
        My unfinished original solution
        Alex Wice's Solution
        """
        edges = defaultdict(list)
        for pair in adjacentPairs:
            edges[pair[0]].append(pair[1])
            edges[pair[1]].append(pair[0])

        N = len(adjacentPairs) + 1

        for u in edges.keys():
            if len(edges[u]) == 1:
                # find one of the edges
                break

        ans = [u]
        while len(ans) < N:
            for v in edges[ans[-1]]:
                if len(ans) == 1 or v != ans[-2]:
                    ans.append(v)
                    break

        return ans
