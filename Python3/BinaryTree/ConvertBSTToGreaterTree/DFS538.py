from ..TreeNodeModule import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/discuss/286725/JavaC%2B%2BPython-Revered-Inorder-Traversal
        """
        if not root:
            return root

        pre = 0

        def dfs(node: TreeNode):
            nonlocal pre
            if node.right:
                dfs(node.right)
            node.val = pre = pre + node.val
            if node.left:
                dfs(node.left)
            return node

        return dfs(root)
