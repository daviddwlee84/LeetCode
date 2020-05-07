from ..TreeNodeModule import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        def depth(root, x, parent, level):
            """ find the node and return its level and parent """
            if not root:
                return

            if root.val == x:
                return [level, parent]

            # find the node either in the left or the right subtree
            return depth(root.left, x, root, level + 1) or depth(root.right, x, root, level + 1)

        x_depth, x_parent = depth(root, x, None, 1)
        y_depth, y_parent = depth(root, y, None, 1)
        if x_depth == y_depth and x_parent != y_parent:
            return True
        return False

# Runtime: 28 ms, faster than 88.05% of Python3 online submissions for Cousins in Binary Tree.
# Memory Usage: 13.9 MB, less than 6.12% of Python3 online submissions for Cousins in Binary Tree.
