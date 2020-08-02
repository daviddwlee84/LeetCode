from typing import List
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        self.edges = defaultdict(list)
        for f, t, p in flights:
            self.edges[f].append((t, p))

        self.cost = float('inf')

        def dfs(cur_station, stop_left, curr_cost):
            if cur_station == dst and stop_left >= -1:
                self.cost = min(self.cost, curr_cost)
                return
            if stop_left <= -1:
                return
            for n, p in self.edges[cur_station]:
                if curr_cost + p > self.cost:
                    continue
                dfs(n, stop_left - 1, curr_cost + p)

        dfs(src, K, 0)
        if self.cost == float('inf'):
            return -1
        else:
            return self.cost
