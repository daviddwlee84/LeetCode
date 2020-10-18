from typing import List


class DSU:
    def __init__(self):
        self.mp = {}
        self.par = []
        self.sz = []

    def find(self, x):
        try:
            i = self.mp[x]
        except:
            self.mp[x] = i = len(self.mp)
            self.par.append(i)
            self.sz.append(1)
        return self._find(i)

    def _find(self, x):
        if self.par[x] != x:
            self.par[x] = self._find(self.par[x])
        return self.par[x]

    def union(self, x, y):
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
        dsu = DSU()
        redundants = []
        for edge in edges:
            if dsu.find(edge[0]) == dsu.find(edge[1]):
                redundants.append(edge)
            else:
                dsu.union(edge[0], edge[1])

        return redundants[-1]
