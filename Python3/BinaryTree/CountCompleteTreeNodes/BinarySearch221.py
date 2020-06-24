from ..TreeNodeModule import TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/count-complete-tree-nodes/discuss/701392/Two-Solution-or-Simple-0(logn-*-logn)-and-1-liner-recursive-O(n)
        """

        # count total level
        left_level = 0
        node = root
        while node:
            left_level += 1
            node = node.left

        right_level = 0
        node = root
        while node:
            right_level += 1
            node = node.right

        if left_level == right_level:
            # found a full binary tree
            return 2 ** left_level - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# Runtime: 72 ms, faster than 96.02% of Python3 online submissions for Count Complete Tree Nodes.
# Memory Usage: 21.3 MB, less than 27.46% of Python3 online submissions for Count Complete Tree Nodes.
