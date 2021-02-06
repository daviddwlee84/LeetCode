from ..TreeNodeModule import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        sorted_array = []

        def inorder_to_sorted_array(node: TreeNode):
            nonlocal sorted_array
            if not node:
                return
            if node.left:
                inorder_to_sorted_array(node.left)
            sorted_array.append(node)
            if node.right:
                inorder_to_sorted_array(node.right)

        inorder_to_sorted_array(root)

        cumulated = 0
        for node in reversed(sorted_array):
            val = node.val
            node.val += cumulated
            cumulated += val

        return root
