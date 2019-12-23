# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
from BinaryTree.TreeNodeModule import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        self.ans = []
        if root:
            self.dfs(root, s, [])
        return self.ans

    def dfs(self, node: TreeNode, sum_left: int, currentPath: List[int]):
        if not node.left and not node.right:
            # leaf
            if sum_left == node.val:
                self.ans.append(currentPath + [node.val])
            return
        else:
            if node.left:
                self.dfs(node.left, sum_left - node.val,
                         currentPath + [node.val])
            if node.right:
                self.dfs(node.right, sum_left - node.val,
                         currentPath + [node.val])

# Runtime: 44 ms, faster than 85.78% of Python3 online submissions for Path Sum II.
# Memory Usage: 17.5 MB, less than 37.93% of Python3 online submissions for Path Sum II.
