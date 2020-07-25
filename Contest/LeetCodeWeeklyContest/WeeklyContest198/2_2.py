from typing import List
from collections import defaultdict


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        """
        William's solution

        treat this tree as a undiredted graph
        """
        edge_dict = defaultdict(list)
        for a, b in edges:
            edge_dict[a].append(b)
            edge_dict[b].append(a)

        ans = [0] * n

        count = [0] * 26

        def dfs(node: int = 0, previous_node: int = -1):
            # level_count is the key
            level_count = count[ord(labels[node]) - ord('a')]
            count[ord(labels[node]) - ord('a')] += 1

            # visiting all the neighbours except the previous node
            for next_node in edge_dict[node]:
                if next_node ^ previous_node:
                    dfs(next_node, node)

            ans[node] = count[ord(labels[node]) - ord('a')] - level_count

        dfs()

        return ans
