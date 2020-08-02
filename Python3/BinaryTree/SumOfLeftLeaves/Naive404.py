from ..TreeNodeModule import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            # [] case
            return 0

        self.sum = 0
        self.dfs(root, False)
        return self.sum

    def dfs(self, node: TreeNode, isLeft: bool):
        if not node.left and not node.right:
            if isLeft:
                self.sum += node.val
            return

        if node.left:
            self.dfs(node.left, True)

        if node.right:
            self.dfs(node.right, False)

# Runtime: 32 ms, faster than 79.61% of Python3 online submissions for Sum of Left Leaves.
# Memory Usage: 14.4 MB, less than 38.60% of Python3 online submissions for Sum of Left Leaves.
