from typing import List
from collections import defaultdict, deque


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        edge_dict = defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            edge_dict[a].append((b, prob))
            edge_dict[b].append((a, prob))

        visited = set([start])
        queue = deque([(start, 1, visited)])
        total_prob = 0
        while queue:
            node, cur_prob, visited = queue.pop()
            if node == end:
                total_prob = max(total_prob, cur_prob)
                continue

            for next_node, next_prob in edge_dict[node]:
                if next_node not in visited:
                    if cur_prob * next_prob < total_prob:
                        # early stop
                        continue
                    queue.appendleft(
                        (next_node, cur_prob * next_prob, visited | set([next_node])))

        return total_prob
