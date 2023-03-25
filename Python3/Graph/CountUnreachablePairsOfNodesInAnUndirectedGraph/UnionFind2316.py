from typing import List
from itertools import combinations


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x

        return self.find(self.parent[x])

    def union(self, x: int, y: int) -> bool:

        root_x = self.find(x)
        root_y = self.find(y)

        # Already union
        if root_x == root_y:
            return False

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] = 1

        return True

    def is_in_same_group(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        return root_x == root_y


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)

        for u, v in edges:
            union_find.union(u, v)

        edge_set = set(tuple(edge) for edge in edges)

        answer = 0
        for u, v in combinations(range(n), 2):

            if (u, v) in edge_set or (v, u) in edge_set:
                continue

            if not union_find.is_in_same_group(u, v):
                answer += 1

        return answer


# TLE
# 51 / 66 testcases passed
# n =
# 9628
# edges =
# []
