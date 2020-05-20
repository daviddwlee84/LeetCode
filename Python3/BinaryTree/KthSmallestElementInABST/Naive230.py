# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from ..TreeNodeModule import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.firstKitem = []
        self.inOrder(root)
        return self.firstKitem[-1]

    def inOrder(self, node: TreeNode):
        """ In order traversal """
        if len(self.firstKitem) >= self.k:
            return

        if node.left:
            self.inOrder(node.left)

        if len(self.firstKitem) < self.k:
            self.firstKitem.append(node.val)

            if node.right:
                self.inOrder(node.right)

# Runtime: 64 ms, faster than 17.89% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 17.8 MB, less than 5.45% of Python3 online submissions for Kth Smallest Element in a BST.
