from ..GraphNodeModule import Node
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        root = Node(node.val)
        val_node_map = {node.val: root}

        visited = set([node])
        queue = deque([node])
        while queue:
            temp = queue.pop()
            for neigh in temp.neighbors:
                if neigh.val not in val_node_map:
                    val_node_map[neigh.val] = Node(neigh.val)
                val_node_map[temp.val].neighbors.append(
                    val_node_map[neigh.val])
                if neigh not in visited:
                    visited.add(neigh)
                    queue.appendleft(neigh)

        return root
