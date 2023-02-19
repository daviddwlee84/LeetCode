# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from ..TreeNodeModule import TreeNode
from typing import List
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Just level order + reverse
        """
        if not root:
            return []

        queue = deque([(root, 0)])
        level_order_traversal = []

        while queue:
            node, depth = queue.pop()
            if len(level_order_traversal) < depth + 1:
                level_order_traversal.append([])

            level_order_traversal[depth].append(node.val)

            if node.left:
                queue.appendleft((node.left, depth + 1))
            if node.right:
                queue.appendleft((node.right, depth + 1))

        return [level if depth % 2 == 0 else list(reversed(level)) for depth, level in enumerate(level_order_traversal)]

# Runtime: 28 ms, faster than 92.24% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 14 MB, less than 50.38% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
