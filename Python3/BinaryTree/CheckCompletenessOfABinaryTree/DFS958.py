from typing import Optional
from ..TreeNodeModule import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """
        Count note id, make sure they are all in order

        https://leetcode.com/problems/check-completeness-of-a-binary-tree/solutions/3298282/image-explanation-dfs-bfs-solution-complete-intuition/
        """
        self.total = self.countTreeNodes(root)
        return self.dfs(root, 1)

    def countTreeNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countTreeNodes(root.left) + self.countTreeNodes(root.right)

    def dfs(self, node: Optional[TreeNode], node_idx: int):
        if not node:
            return True

        if node_idx > self.total:
            return False

        return self.dfs(node.left, 2 * node_idx) and self.dfs(node.right, 2 * node_idx + 1)
