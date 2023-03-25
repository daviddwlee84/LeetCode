from typing import List
from collections import Counter


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


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/solutions/3337487/python-java-c-simple-solution-easy-to-understand/
        """
        union_find = UnionFind(n)
        for u, v in edges:
            union_find.union(u, v)

        # (this part is Math)
        group_sizes = list(Counter([union_find.find(i) for i in range(n)]).values())

        # print(group_sizes)

        answer = 0
        first_group_size = group_sizes[0]
        # If not more than 1 group, then answer should be 0
        for group_size in group_sizes[1:]:
            answer += first_group_size * group_size
            first_group_size += group_size
        return answer
