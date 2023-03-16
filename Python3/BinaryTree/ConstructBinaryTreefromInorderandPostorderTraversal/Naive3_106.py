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
        self.index_map = {val: i for i, val in enumerate(inorder)}
        return self.buildHelper(inorder, postorder)

    def buildHelper(self, inorder: List[int], postorder: List[int]):
        if not inorder:
            return None

        node_val = postorder[-1]
        node = TreeNode(node_val)
        idx = self.index_map[node_val]
        node.left = self.buildTree(inorder[:idx], postorder[:idx])
        node.right = self.buildTree(inorder[idx + 1:], postorder[idx:-1])
        return node

# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         postorder_root_index = len(postorder) - 1
#
#         def build_val_index_map(nums):
#             answer = {}
#             for i, num in enumerate(nums):
#                 answer[num] = i
#             return answer
#
#         def solve(start, end):
#             nonlocal postorder_root_index
#             if start > end:
#                 return None
#
#             root_val = postorder[postorder_root_index]
#             root = TreeNode(root_val)
#             inorder_root_index = val_index_map[root_val]
#
#             postorder_root_index -= 1
#
#             root.right = solve(inorder_root_index + 1, end)
#             root.left = solve(start, inorder_root_index - 1)
#
#             return root
#
#         val_index_map = build_val_index_map(inorder)
#         return solve(0, len(inorder) - 1)
