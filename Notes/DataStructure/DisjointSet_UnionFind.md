# Disjoint Set (Union-Find)

## Data Structure

* [Disjoint-set data structure - Wikipedia](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)

## Disjoint Set Union (DSU)

* [Basics of Disjoint Data Structures Tutorials & Notes | Data Structures | HackerEarth](https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/tutorial/)
* [Disjoint Set Union (Union Find) | HackerEarth](https://www.hackerearth.com/practice/notes/disjoint-set-union-union-find/)
* [Disjoint Set Union - Competitive Programming Algorithms](https://cp-algorithms.com/data_structures/disjoint_set_union.html)
* [Disjoint Set (Or Union-Find) | Set 1 (Detect Cycle in an Undirected Graph) - GeeksforGeeks](https://www.geeksforgeeks.org/union-find/)
* [Union-Find Algorithm | Set 2 (Union By Rank and Path Compression) - GeeksforGeeks](https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/)

## Template

Fix size

```py
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
```

Dynamic

```py
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
```

## Tutorial

* [花花酱 LeetCode Disjoint set / Union Find Forest SP1 – Huahua's Tech Road](https://zxi.mytechroad.com/blog/data-structure/sp1-union-find-set/)
  * [**花花酱 Disjoint-set/Union-find Forest - 刷题找工作 SP1 - YouTube**](https://www.youtube.com/watch?v=VJnUwsE4fWA)
* [Union-Find算法详解 - labuladong的算法小抄](https://labuladong.gitbook.io/algo/gao-pin-mian-shi-xi-lie/unionfind-suan-fa-xiang-jie)
