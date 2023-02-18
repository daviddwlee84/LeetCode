from typing import Optional
from BinaryTree.TreeNodeModule import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    previous_val = float('-inf')
    result = float('inf')

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        
        self.result = min(self.result, root.val - self.previous_val)
        self.previous_val = root.val

        if root.right:
            self.minDiffInBST(root.right)
        
        return self.result
