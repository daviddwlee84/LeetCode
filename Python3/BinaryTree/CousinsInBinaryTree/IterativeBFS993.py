from ..TreeNodeModule import TreeNode
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_parent = None
        x_depth = None
        y_parent = None
        y_depth = None

        # level order traversal
        queue = deque([(root, 0, None)])  # (node, depth, parent)

        while queue:
            curr_node, curr_depth, curr_parent = queue.pop()

            if curr_node.val == x:
                x_depth = curr_depth
                x_parent = curr_parent

            if curr_node.val == y:
                y_depth = curr_depth
                y_parent = curr_parent

            if x_depth and y_depth:
                if x_depth == y_depth and x_parent != y_parent:
                    return True
                else:
                    return False

            if curr_node.left:
                queue.appendleft(
                    (curr_node.left, curr_depth + 1, curr_node.val))
            if curr_node.right:
                queue.appendleft(
                    (curr_node.right, curr_depth + 1, curr_node.val))

# Runtime: 32 ms, faster than 64.35% of Python3 online submissions for Cousins in Binary Tree.
# Memory Usage: 14.1 MB, less than 6.12% of Python3 online submissions for Cousins in Binary Tree.
