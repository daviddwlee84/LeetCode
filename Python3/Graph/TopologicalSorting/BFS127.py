from typing import List
from collections import defaultdict, deque


class DirectedGraphNode:
    def __init__(self, x: int):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph: List[DirectedGraphNode]) -> List[DirectedGraphNode]:
        # Get in-degree to find starting node
        node_indegree = defaultdict(int)
        for node in graph:
            # initial to 0
            node_indegree[node]
            for neighbor in node.neighbors:
                node_indegree[neighbor] += 1

        possible = []
        queue = deque(
            [node for node, indegree in node_indegree.items() if indegree == 0])
        while queue:
            node = queue.popleft()
            possible.append(node)
            for neighbor in node.neighbors:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return possible

# Wrong Answer
# class Solution:
#     """
#     @param graph: A list of Directed graph node
#     @return: Any topological order for the given graph.
#     """
#
#     def topSort(self, graph: List[DirectedGraphNode]) -> List[DirectedGraphNode]:
#         possible = []
#
#         to_this = set()
#         for node in graph:
#             for neighbor in node.neighbors:
#                 to_this.add(neighbor)
#         first_nodes = set(graph) - to_this
#
#         node = first_nodes.pop()
#         possible = [node]
#         while len(possible) < len(graph):
#             if not node.neighbors:
#                 for another_node in graph:
#                     if another_node not in possible:
#                         node = another_node
#                         break
#             else:
#                 node = node.neighbors[0]
#             possible.append(node)
#
#         return possible

# Wrong Answer
# class Solution:
#     """
#     @param graph: A list of Directed graph node
#     @return: Any topological order for the given graph.
#     """
#
#     def topSort(self, graph: List[DirectedGraphNode]) -> List[DirectedGraphNode]:
#         # Your code cost too much memory than we expected. Check your space complexity.
#         # Memory limit exceeded usually caused by you create a 2D-array which is unnecessary.
#         # self.graph = graph
#         # self.possibles = []
#         self.possible = None
#
#         def dfs(node: DirectedGraphNode, curr_order: List[DirectedGraphNode]):
#             # https://stackoverflow.com/questions/5218895/python-nested-functions-variable-scoping
#             nonlocal graph
#             # if self.possibles:
#             #     # Early stop
#             #     return
#             if self.possible:
#                 # Early stop
#                 return
#
#             if not node.neighbors:
#                 # if len(curr_order) == len(self.graph):
#                 if len(curr_order) == len(graph):
#                     # self.possibles.append(curr_order + [node])
#                     self.possible = curr_order + [node]
#                     return
#
#                 # for another_node in self.graph:
#                 for another_node in graph:
#                     if another_node not in curr_order:
#                         dfs(another_node, curr_order)
#
#             for neighbor in node.neighbors:
#                 dfs(neighbor, curr_order + [node])
#
#         # The first node in the order can be any node in the graph with no nodes direct to it.
#         to_this = set()
#         for node in graph:
#             for neighbor in node.neighbors:
#                 to_this.add(neighbor)
#         first_nodes = set(graph) - to_this
#
#         for first_node in first_nodes:
#             dfs(first_node, [])
#
#         # return self.possibles[0]
#         return self.possible
