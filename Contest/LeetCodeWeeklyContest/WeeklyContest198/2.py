from typing import List
from collections import defaultdict
from functools import lru_cache

# TODO: try iterative stack DFS


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.edge_dict = {0: []}
        # the root of the tree is the node 0

        # build tree because edges is not always start -> end
        # e.g.
        # 4
        # [[0, 2], [0, 3], [1, 2]]
        # "aeed"
        # [1,1,2,1]
        edge_left = edges
        while edge_left:
            edge_left = []
            for a, b, in edges:
                if a in self.edge_dict and b not in self.edge_dict:
                    self.edge_dict[a].append(b)
                    self.edge_dict[b] = []
                elif b in self.edge_dict and a not in self.edge_dict:
                    self.edge_dict[b].append(a)
                    self.edge_dict[a] = []
                else:
                    edge_left.append([a, b])

        self.labels = labels

        self.ans = [0] * n
        for i in range(n):
            self.countSubTree(i, i)

        return self.ans

    def countSubTree(self, node, i) -> int:
        if self.labels[node] == self.labels[i]:
            self.ans[i] += 1

        if node not in self.edge_dict:
            return

        for next_node in self.edge_dict[node]:
            self.countSubTree(next_node, i)


# TLE
