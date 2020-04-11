# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from ..TreeNodeModule import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        # counting the "node" we passed through
        self.answer = 1
        # (if counting the "edge" we passed through, we can initial this to 0,
        # and use self.answer = max(self.answer, L + R) later
        # finally return self.answer itself

        def depth(node: TreeNode):
            if not node:
                return 0

            L = depth(node.left)
            R = depth(node.right)

            # update the longest path (if any)
            self.answer = max(self.answer, L + R + 1)

            # from one node to calculate the maximum left or right decessor leaf
            return max(L, R) + 1

        depth(root)

        return self.answer - 1

# Runtime: 40 ms, faster than 86.70% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 16 MB, less than 37.93% of Python3 online submissions for Diameter of Binary Tree.
