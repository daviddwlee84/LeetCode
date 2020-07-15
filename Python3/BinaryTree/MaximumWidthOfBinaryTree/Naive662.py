# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from ..TreeNodeModule import TreeNode
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # count of element
        layers = []

        queue = deque([(root, 0, 0)])
        cur_layer = -1
        while queue:
            node, depth, position = queue.pop()
            if depth > cur_layer:
                layers.append({'min': float('inf'), 'max': float('-inf')})

            cur_layer = depth

            layers[depth]['min'] = min(layers[depth]['min'], position)
            layers[depth]['max'] = max(layers[depth]['max'], position)

            if node.left:
                queue.appendleft((node.left, depth + 1, position * 2))
            if node.right:
                queue.appendleft((node.right, depth + 1, position * 2 + 1))
        
        max_width = 0
        for i, layer in enumerate(reversed(layers)):
            if 2 ** (len(layers) - i - 1) < max_width:
                # early stop
                break

            max_width = max(max_width, layer['max'] - layer['min'] + 1)

        return max_width

# Runtime: 48 ms, faster than 56.89% of Python3 online submissions for Maximum Width of Binary Tree.
# Memory Usage: 14.5 MB, less than 41.51% of Python3 online submissions for Maximum Width of Binary Tree.
