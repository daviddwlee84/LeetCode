# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from ..TreeNodeModule import TreeNode


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        https://leetcode.com/problems/insert-into-a-binary-search-tree/discuss/180244/Python-4-line-clean-recursive-solution
        """
        if not root:
            return TreeNode(val=val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root

# Runtime: 120 ms, faster than 99.88% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 16.8 MB, less than 5.01% of Python3 online submissions for Insert into a Binary Search Tree.
