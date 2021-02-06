from ..TreeNodeModule import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        """
        https://leetcode.com/problems/trim-a-binary-search-tree/discuss/107013/clear-python-solution
        https://leetcode.com/problems/trim-a-binary-search-tree/discuss/158631/Python-DFS-tm
        """
        # Condition for each layer
        # We return "root" that match the condition
        if not root:
            return root
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        elif root.val < low:
            return self.trimBST(root.right, low, high)

        else:
            # If "root" is in normal condition
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root

# Runtime: 52 ms, faster than 75.43% of Python3 online submissions for Trim a Binary Search Tree.
# Memory Usage: 18.3 MB, less than 23.75% of Python3 online submissions for Trim a Binary Search Tree.
