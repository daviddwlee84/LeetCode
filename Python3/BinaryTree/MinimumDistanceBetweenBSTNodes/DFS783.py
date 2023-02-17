from typing import Optional
from BinaryTree.TreeNodeModule import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        sorted_array = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            sorted_array.append(node.val)
            dfs(node.right)
        dfs(root)
        min_diff = float('inf')
        for i in range(len(sorted_array) - 1):
            min_diff = min(min_diff, sorted_array[i + 1] - sorted_array[i])
        return min_diff
