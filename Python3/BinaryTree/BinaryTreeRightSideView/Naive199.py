from typing import List
from ..TreeNodeModule import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        Do level order traversal and return the last elements
        """
        if not root:
            return []

        # In python version 3.7: Dictionary order is guaranteed to be insertion order.
        # https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/
        levelorder = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.pop()
            levelorder[depth].append(node.val)
            if node.left:
                queue.appendleft((node.left, depth + 1))
            if node.right:
                queue.appendleft((node.right, depth + 1))

        return [level[-1] for level in levelorder.values()]
