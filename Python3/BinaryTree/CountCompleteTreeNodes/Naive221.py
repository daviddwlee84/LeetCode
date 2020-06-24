from ..TreeNodeModule import TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# Runtime: 92 ms, faster than 50.29% of Python3 online submissions for Count Complete Tree Nodes.
# Memory Usage: 21.3 MB, less than 36.36% of Python3 online submissions for Count Complete Tree Nodes.
