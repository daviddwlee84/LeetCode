# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from ..TreeNodeModule import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """ Iterative inorder traversal with early stop """

        stack = []

        while True:
            while root:
                # keep track of current node and go to the leftmost/smallest node
                stack.append(root)
                root = root.left

            # reach the smallest node and pop it out
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val

            # go to the right subtree
            root = root.right

# Runtime: 64 ms, faster than 17.89% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 17.8 MB, less than 5.45% of Python3 online submissions for Kth Smallest Element in a BST.
