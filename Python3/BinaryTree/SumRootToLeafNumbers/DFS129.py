from ..TreeNodeModule import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.sum = 0

    def sumNumbers(self, root: TreeNode) -> int:
        """
        https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/705994/Python-dfs-O(n)-with-explanations
        https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/705970/Recursive-Preorder-Traversal-or-Easy-to-Understand
        """
        if not root:
            return 0

        if not root.left and not root.right:
            self.sum += root.val

        else:
            if root.left:
                root.left.val = 10 * root.val + root.left.val
                self.sumNumbers(root.left)
            if root.right:
                root.right.val = 10 * root.val + root.right.val
                self.sumNumbers(root.right)

        return self.sum


# Runtime: 52 ms, faster than 9.07 % of Python3 online submissions for Sum Root to Leaf Numbers.
# Memory Usage: 13.9 MB, less than 77.12 % of Python3 online submissions for Sum Root to Leaf Numbers.

# class Solution:
#     def sumNumbers(self, root: TreeNode) -> int:
#         def helper(root: TreeNode, n: int) -> int:
#             if not root:
#                 return 0
#         
#             if not root.left and not root.right:
#                 return n * 10 + root.val
#             
#             return helper(root.left, n * 10 + root.val) + helper(root.right, n * 10 + root.val)
#       
#         return helper(root, 0)