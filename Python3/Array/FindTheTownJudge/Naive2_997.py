from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # find a node that in edge is n - 1 and out edge is 0
        in_edges = [0] * n
        out_edges = [0] * n
        for ai, bi in trust:
            in_edges[bi - 1] += 1
            out_edges[ai - 1] += 1

        for i, (in_edge, out_edge) in enumerate(zip(in_edges, out_edges)):
            if in_edge == n - 1 and out_edge == 0:
                return i + 1
        return -1
