from typing import List
from collections import Counter

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        paths = self.getPathsFromRoot(root)
        count = 0

        for path in paths:
            if self.isPseudoPalindromic(path):
                count += 1

        return count

    def getPathsFromRoot(self, root: TreeNode) -> List[int]:
        paths = []

        def dfs(node: TreeNode, curr_path: List[int]):
            if not node.left and not node.right:
                # reach leaf
                paths.append(curr_path + [node.val])
            else:
                if node.left:
                    dfs(node.left, curr_path + [node.val])
                if node.right:
                    dfs(node.right, curr_path + [node.val])

        dfs(root, [])

        return paths

    def isPseudoPalindromic(self, path: List[int]) -> bool:

        odd_count = 0
        even_count = 0

        for _, count in Counter(path).items():
            if count % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        if len(path) % 2 == 0:
            if odd_count != 0:
                return False
            else:
                return True
        else:
            if odd_count != 1:
                return False
            else:
                return True
