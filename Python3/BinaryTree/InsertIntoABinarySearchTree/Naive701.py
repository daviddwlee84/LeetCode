# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from ..TreeNodeModule import TreeNode


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root

        if not root:
            # insert into an empty BST
            return TreeNode(val=val)

        while node:
            if node.val > val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val=val)
                    break
            else:  # node.val < val
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val=val)
                    break

        return root

# Runtime: 140 ms, faster than 75.09% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 16.6 MB, less than 5.01% of Python3 online submissions for Insert into a Binary Search Tree.
