from typing import List, Optional
from ..TreeNodeModule import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Use original array index value instead of create new one
        """
        # Get root from postorder
        root_index = len(postorder) - 1

        # Value index map for inorder
        value_index_map = {num: i for i, num in enumerate(inorder)}

        def solve(start: int, end: int) -> Optional[TreeNode]:
            nonlocal root_index
            # optional
            # nonlocal value_index_map

            if start > end:
                return None

            root = TreeNode(postorder[root_index])

            inorder_root_index = value_index_map[root.val]
            root_index -= 1

            # Right should be first
            root.right = solve(inorder_root_index + 1, end)
            root.left = solve(start, inorder_root_index - 1)

            return root

        return solve(0, len(inorder) - 1)
