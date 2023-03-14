from typing import Optional
from ..TreeNodeModule import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        stack = [(root, [str(root.val)])]
        curr_path = []
        total = 0
        while stack:
            node, curr_path = stack.pop()
            
            if not node.left and not node.right:
                # print(''.join(curr_path))
                total += int(''.join(curr_path))
            
            if node.left:
                stack.append((node.left, curr_path + [str(node.left.val)]))
            if node.right:
                stack.append((node.right, curr_path + [str(node.right.val)]))
        
        return total