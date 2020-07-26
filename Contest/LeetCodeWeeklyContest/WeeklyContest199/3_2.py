# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        Alex Wice's Solution
        """

        self.ans = 0

        def dfs(node: TreeNode, depth: int = 0):
            # Return a list of depths of all leaves in this subtree
            # Also count all paths with LCA == `node`
            # (LCA stands for lowest common ancestor)
            if not node:
                return []

            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

            for depth_left in left:
                for depth_right in right:
                    cand = depth_left - depth + depth_right - depth
                    if cand <= distance:
                        self.ans += 1

            return left + right + ([depth] if node.left is node.right else [])

        dfs(root)
        return self.ans
