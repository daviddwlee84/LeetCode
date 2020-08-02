from ..TreeNodeModule import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        https://leetcode.com/problems/balanced-binary-tree/discuss/35708/VERY-SIMPLE-Python-solutions-(iterative-and-recursive)-both-beat-90
        """
        return self.check(root) != -1

    def check(self, node: TreeNode) -> int:
        """
        Return the depth if the tree is valid
        Otherwise return -1
        """
        if node is None:
            return 0

        left = self.check(node.left)
        if left == -1:
            # we do it here that we could save a lot of time if the tree is heavily skewed right
            return -1

        right = self.check(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

# Runtime: 44 ms, faster than 97.07% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 17.2 MB, less than 97.77% of Python3 online submissions for Balanced Binary Tree.
