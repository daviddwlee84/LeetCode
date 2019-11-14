"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

from collections import deque

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        self.max_depth = 0
        self._helper(root, 1)

        return self.max_depth
    
    def _helper(self, node, depth: int):
        self.max_depth = max(depth, self.max_depth)
        for child in node.children:
            if child is not None:
                self._helper(child, depth+1)
