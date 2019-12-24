"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import defaultdict, deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        layers = defaultdict(list)
        toVisit = deque([(root, 0)])
        while toVisit:
            node, depth = toVisit.pop()
            layers[depth].append(node)
            if node.left:
                toVisit.appendleft((node.left, depth + 1))
            if node.right:
                toVisit.appendleft((node.right, depth + 1))

        for layer in layers.values():
            for i, node in enumerate(layer):
                if i + 1 == len(layer):
                    node.next = None
                else:
                    node.next = layer[i+1]

        return root

# Runtime: 68 ms, faster than 54.11% of Python3 online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node.
# (I didn't use constant extra space... but still passed)
