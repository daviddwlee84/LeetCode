# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from ..TreeNodeModule import TreeNode
from typing import List
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/33825/c%2B%2B-5ms-version%3A-one-queue-and-without-reverse-operation-by-using-size-of-each-level
        """
        if not root:
            return []

        queue = deque([root])
        result = []
        left_to_right = True

        while queue:
            size = len(queue)
            row = [0] * size
            for i in range(size):
                node = queue.pop()

                # find position to fill node's value
                index = i if left_to_right else (size - 1 - i)
                row[index] = node.val

                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
            # after this level
            left_to_right = not left_to_right
            result.append(row)

        return result

# Runtime: 72 ms, faster than 5.54% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 14.2 MB, less than 15.24% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
