from collections import defaultdict
from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/merge-intervals/solution/
        """
        graph = self.build_graph(intervals)
        nodes_in_comp, number_of_comps = self.get_components(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.merge_nodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]

    def overlap(self, a: List[int], b: List[int]):
        return a[0] <= b[1] and b[0] <= a[1]

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def build_graph(self, intervals: List[List[int]]):
        graph = defaultdict(list)

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if self.overlap(intervals[i], intervals[j]):
                    graph[tuple(intervals[i])].append(intervals[j])
                    graph[tuple(intervals[j])].append(intervals[i])

        return graph

    # merges all of the nodes in this connected component into one interval.
    def merge_nodes(self, nodes: List[List[int]]):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]

    # gets the connected components of the interval overlap graph.
    def get_components(self, graph: defaultdict, intervals: List[List[int]]):
        visited = set()
        comp_number = 0
        nodes_in_comp = defaultdict(list)

        def mark_component_dfs(start: List[int]):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if tuple(interval) not in visited:
                mark_component_dfs(interval)
                comp_number += 1

        return nodes_in_comp, comp_number
