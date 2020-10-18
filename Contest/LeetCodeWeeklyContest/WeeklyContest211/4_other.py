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
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        """
        Alex Wice's Solution
        Disjoint Set
        """
        dsu = DSU(n + 1)

        # Connect (Union) all the number share the same divisors
        for divisor in range(threshold + 1, n + 1):
            for num in range(2 * divisor, n + 1, divisor):
                dsu.union(divisor, num)

        ans = []
        for qu, qv in queries:
            ans.append(dsu.find(qu) == dsu.find(qv))

        return ans

# Runtime: 1020 ms, faster than 100.00% of Python3 online submissions for Graph Connectivity With Threshold.
# Memory Usage: 49.2 MB, less than 100.00% of Python3 online submissions for Graph Connectivity With Threshold.
