from ..TreeNodeModule import TreeNode
from collections import deque


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        if not root.left and not root.right:
            return True

        return self._checkBalanced(root) and self.isBalanced(root.left) and self.isBalanced(root.right)

    def _checkBalanced(self, node: TreeNode) -> bool:
        if not node:
            return True

        ldepth = self._getDepth(node.left)
        rdepth = self._getDepth(node.right)

        if abs(ldepth - rdepth) > 1:
            return False
        else:
            return True

    def _getDepth(self, node: TreeNode) -> int:
        if not node:
            return 0

        return 1 + max(self._getDepth(node.left), self._getDepth(node.right))

# Runtime: 60 ms, faster than 55.93% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for Balanced Binary Tree.
