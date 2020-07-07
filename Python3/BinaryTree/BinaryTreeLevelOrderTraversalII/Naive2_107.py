# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from ..TreeNodeModule import TreeNode
from typing import List
from collections import deque, defaultdict


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        answer = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.pop()
            answer[depth].append(node.val)
            if node.left:
                queue.appendleft((node.left, depth + 1))
            if node.right:
                queue.appendleft((node.right, depth + 1))

        return [num for _, num in sorted(answer.items(), reverse=True)]

# Runtime: 36 ms, faster than 60.68% of Python3 online submissions for Binary Tree Level Order Traversal II.
# Memory Usage: 13.9 MB, less than 94.79% of Python3 online submissions for Binary Tree Level Order Traversal II.
