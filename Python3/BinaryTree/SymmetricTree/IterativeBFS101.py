from typing import Optional
from ..TreeNodeModule import TreeNode
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([(root.left, root.right)])
        while queue:
            left, right = queue.pop()

            if not left and not right:
                continue

            if not left or not right or left.val != right.val:
                return False

            queue.appendleft((left.left, right.right))
            queue.appendleft((left.right, right.left))

        return True
