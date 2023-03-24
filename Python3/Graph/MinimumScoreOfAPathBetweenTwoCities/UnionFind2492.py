from typing import List


class Solution:

    def __init__(self) -> None:
        # For Union Find
        self.root = []
        # Same rank item will be in the same group
        self.rank = []

    def find_root(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find_root(self.root[x])
        return self.root[x]

    def create_union(self, x: int, y: int) -> bool:
        root_x = self.find_root(x)
        root_y = self.find_root(y)

        if root_x == root_y:
            # already exist
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_y] = root_x
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

        return True

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/solutions/3326975/day-81-union-find-easiest-beginner-friendly-sol/
        """
        # Initialize
        self.root = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

        # Create the Disjoint Set
        for u, v, _ in roads:
            self.create_union(u, v)

        # Find answer
        min_score = float('inf')
        root1 = self.find_root(1)
        for u, v, dis in roads:
            root_u = self.find_root(u)
            root_v = self.find_root(v)
            if root1 == root_u == root_v:
                min_score = min(min_score, dis)

        return min_score
