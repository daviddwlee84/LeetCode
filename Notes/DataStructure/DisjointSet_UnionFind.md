# Disjoint Set (Union-Find)

## Data Structure

* [Disjoint-set data structure - Wikipedia](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)

## Disjoint Set Union (DSU)

* [Basics of Disjoint Data Structures Tutorials & Notes | Data Structures | HackerEarth](https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/tutorial/)
* [Disjoint Set Union (Union Find) | HackerEarth](https://www.hackerearth.com/practice/notes/disjoint-set-union-union-find/)
* [Disjoint Set Union - Competitive Programming Algorithms](https://cp-algorithms.com/data_structures/disjoint_set_union.html)
* [Disjoint Set (Or Union-Find) | Set 1 (Detect Cycle in an Undirected Graph) - GeeksforGeeks](https://www.geeksforgeeks.org/union-find/)
* [Union-Find Algorithm | Set 2 (Union By Rank and Path Compression) - GeeksforGeeks](https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/)

### LeetCode explanation

> [Redundant Connection - LeetCode](https://leetcode.com/problems/redundant-connection/solution/)

A DSU (Disjoint Set Union) data structure can be used to maintain knowledge of the connected components of a graph, and query for them quickly. In particular, we would like to support two operations:

* `dsu.find(node x)`, which outputs a unique id so that two nodes have the same id if and only if they are in the same connected component, and:
* `dsu.union(node x, node y)`, which draws an edge `(x, y)` in the graph, connecting the components with id `find(x)` and `find(y)` together.

To achieve this, we keep track of `parent`, which remembers the `id` of a smaller node in the same connected component. If the node is it's own parent, we call this the *leader* of that connected component.

A naive implementation of a DSU structure would look something like this:

```txt
# parent initialized as (x -> x)
function find(x):
    while parent[x] != x: #While x isn't the leader
        x = parent[x]
    return x

function union(x, y):
    parent[find(x)] = find(y)
```

We use two techniques to improve the run-time complexity: *path compression*, and *union-by-rank*.

* Path compression involves changing the `x = parent[x]` in the find function to `parent[x] = find(parent[x])`. Basically, as we compute the correct leader for `x`, we should remember our calculation.
* Union-by-rank involves distributing the workload of find across leaders evenly. Whenever we `dsu.union(x, y)`, we have two leaders `xr`, `yr` and we have to choose whether we want `parent[x] = yr` or `parent[y] = xr`. We choose the leader that has a higher following to pick up a new follower. Specifically, the meaning of `rank` is that there are less than `2 ^ rank[x]` followers of `x`. This strategy can be shown to give us better bounds for how long the recursive loop in `dsu.find` could run for.

```py
class DSU(object):
    def __init__(self):
        self.par = range(1001)
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True
```

Alternate Implementation of DSU without Union-By-Rank

```py
class DSU:
    def __init__(self):
        self.par = range(1001)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)
```

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
