from typing import List
from itertools import combinations
from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        edges = defaultdict(set)
        for a, b in roads:
            edges[a].add(b)
            edges[b].add(a)

        answer = 0
        for city_i, city_j in combinations(range(n), 2):
            answer = max(answer, len(
                edges[city_i]) + len(edges[city_j]) - int(city_i in edges[city_j]))

        return answer
