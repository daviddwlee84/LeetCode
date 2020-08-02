from ..TreeNodeModule import TreeNode


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.tilt_sum = 0
        self.dfs(root)
        return self.tilt_sum

    def dfs(self, node: TreeNode) -> int:
        """
        Return the sum of the child nodes' value while updating the global tilt sum at the same time
        """
        if not node:
            return 0

        if not node.left and not node.right:
            return node.val

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.tilt_sum += abs(left - right)

        return left + right + node.val

# Runtime: 56 ms, faster than 90.13% of Python3 online submissions for Binary Tree Tilt.
# Memory Usage: 15.5 MB, less than 85.71% of Python3 online submissions for Binary Tree Tilt.
