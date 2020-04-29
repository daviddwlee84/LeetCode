from ..TreeNodeModule import TreeNode


class Solution:
    """ https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/602827/Python-recursive-clean-beat-99 """

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path_sum = float('-inf')

        def get_sum(root: TreeNode) -> int:
            if root is None:
                return 0

            left_sum = max(get_sum(root.left), 0)
            right_sum = max(get_sum(root.right), 0)
            self.max_path_sum = max(
                self.max_path_sum, left_sum + right_sum + root.val)

            # because it is path, so you can only choose either way (left or right sum) with itself
            return max(left_sum, right_sum, 0) + root.val

        get_sum(root)
        return self.max_path_sum
