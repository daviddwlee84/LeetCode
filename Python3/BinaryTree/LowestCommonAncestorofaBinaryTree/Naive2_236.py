from typing import List
from ..TreeNodeModule import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Directly search p and q and record its' path.
        Pick the last same node of their path
        """
        p_memory = []
        q_memory = []

        self.dfs(root, [], p, p_memory)
        self.dfs(root, [], q, q_memory)

        if not p_memory[0] or not q_memory[0]:
            return None

        p_memory = set(p_memory[0])

        for node in reversed(q_memory[0]):
            if node in p_memory:
                return node

        return None

    def dfs(self, node: 'TreeNode', path: List['TreeNode'], target: 'TreeNode', memory: List['TreeNode']):
        if node == target:
            memory.append(path + [node])
            return

        if node.left:
            self.dfs(node.left, path + [node], target, memory)
        if node.right:
            self.dfs(node.right, path + [node], target, memory)

# Runtime: 3320 ms, faster than 5.00% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 415.5 MB, less than 5.00% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.

# [3,5,1,6,2,0,8,null,null,7,4]
# 5
# 1
#
# [3,5,1,6,2,0,8,null,null,7,4]
# 5
# 4
