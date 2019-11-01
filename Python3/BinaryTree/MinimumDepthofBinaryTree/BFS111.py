# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from BinaryTree.TreeNodeModule import TreeNode
from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.queue = deque([(root, 1)])
        while self.queue:
            node, depth = self.queue.pop()
            if not node.left and not node.right:
                # reach leaf
                return depth
            else:
                if node.left is not None:
                    self.queue.appendleft((node.left, depth+1))
                if node.right is not None:
                    self.queue.appendleft((node.right, depth+1))
