from typing import List


class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        """
        Returns true iff it connected two previously unconnected components
        """
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False

        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr

        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        self.sz[yr] = self.sz[xr]

        return True

    def size(self, x):
        return self.sz[self.find(x)]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Find the first edge occurring in the graph that is already connected

        Time complexity: about O(N)
        Space complexity: O(N)

        Runtime: 56 ms, faster than 71.41% of Python3 online submissions for Redundant Connection.
        Memory Usage: 15 MB, less than 39.82% of Python3 online submissions for Redundant Connection.

        (use dynamic DSU template)
        Runtime: 60 ms, faster than 48.24% of Python3 online submissions for Redundant Connection.
        Memory Usage: 14.9 MB, less than 66.32% of Python3 online submissions for Redundant Connection.
        """
        dsu = DSU(len(edges) + 1)
        for edge in edges:
            if not dsu.union(*edge):
                return edge


# Other union find solution

"""
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find
        parents, ranks = {}, {}

        def findParent(n, parents):
            while parents[n] != n:
                parents[n] = parents[parents[n]]
                n = parents[n]
            return n

        for edge in edges:
            u = edge[0]
            v = edge[1]

            if u not in parents:
                parents[u] = u
                ranks[u] = 1
            if v not in parents:
                parents[v] = v
                ranks[v] = 1

            pu = findParent(u, parents)
            pv = findParent(v, parents)

            if pu == pv:
                return edge

            if ranks[pu] < ranks[pv]:
                parents[pu] = pv
                ranks[pv] += ranks[pu]
            else:
                parents[pv] = pu
                ranks[pu] += ranks[pv]
"""

"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
"""
