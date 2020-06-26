from typing import List
from ..TreeNodeModule import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.sum = 0
        self.dfs(root, [root.val])
        return self.sum

    def dfs(self, node: TreeNode, curr_path: List[int]):
        if not node.left and not node.right:
            # leaf
            self.sum += int(''.join(map(str, curr_path)))
            return

        if node.left:
            self.dfs(node.left, curr_path + [node.left.val])
        if node.right:
            self.dfs(node.right, curr_path + [node.right.val])


# Runtime: 56 ms, faster than 5.99 % of Python3 online submissions for Sum Root to Leaf Numbers.
# Memory Usage: 14.2 MB, less than 9.78 % of Python3 online submissions for Sum Root to Leaf Numbers.
