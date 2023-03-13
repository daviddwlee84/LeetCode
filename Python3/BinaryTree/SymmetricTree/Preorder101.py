from typing import Optional
from ..TreeNodeModule import TreeNode

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

        def dfs_left_and_right(left_node: Optional[TreeNode], right_node: Optional[TreeNode]):
            if (left_node is None) ^ (right_node is None):
                return False
            elif not left_node and not right_node:
                return True

            if left_node.val != right_node.val:
                return False

            result = True
            result &= dfs_left_and_right(left_node.left, right_node.right)
            result &= dfs_left_and_right(left_node.right, right_node.left)

            return result

        return dfs_left_and_right(root.left, root.right)
