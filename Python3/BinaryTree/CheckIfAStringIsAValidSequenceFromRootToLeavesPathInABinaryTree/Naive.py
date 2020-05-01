# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from ..TreeNodeModule import TreeNode
from typing import List


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        """
        find all path to leaf and check if it is match arr
        """
        self.arr = arr
        self.found = False

        self.dfs(root, [root.val])

        return self.found

    def dfs(self, root: TreeNode, path: List[int]):
        if self.found:
            return

        if not root.left and not root.right:
            # leaf
            if path == self.arr:
                self.found = True
                return

        if root.left:
            self.dfs(root.left, path + [root.left.val])
        if root.right:
            self.dfs(root.right, path + [root.right.val])
