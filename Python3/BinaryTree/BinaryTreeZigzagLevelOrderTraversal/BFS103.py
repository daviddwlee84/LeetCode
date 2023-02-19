from typing import Optional, List
from collections import deque
from BinaryTree.TreeNodeModule import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # node and depth
        queue = deque([(root, 1)])
        answer = []
        while queue:
            node, depth = queue.pop()
            if node.left:
                queue.appendleft((node.left, depth + 1))
            if node.right:
                queue.appendleft((node.right, depth + 1))
            
            if depth > len(answer):
                answer.append([])
            answer[-1].append(node.val)
        
        return [level if depth % 2 == 0 else list(reversed(level)) for depth, level in enumerate(answer)]
