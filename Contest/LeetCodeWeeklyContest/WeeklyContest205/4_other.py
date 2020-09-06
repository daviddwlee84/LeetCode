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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=e6SR2_CSQwU

        Greedy with DSU

        Usually the MST algorithm need DSU


        A edges, B edges, AB edges

        => if we want to get the max edges to remove, we should maximum keep the AB edges
        """

        dsuA = DSU(n + 1)  # Alice
        dsuB = DSU(n + 1)  # Bob

        ans = 0

        # First remove the AB edges that are completely useless
        for t, u, v in edges:
            if t == 3:
                if not dsuA.union(u, v):
                    ans += 1
                dsuB.union(u, v)

        # Try to remove the A or B edges that are redundant
        for t, u, v in edges:
            if t == 1:
                if not dsuA.union(u, v):
                    ans += 1
            elif t == 2:
                if not dsuB.union(u, v):
                    ans += 1

        return ans if dsuA.size(1) == dsuB.size(1) == n else -1
