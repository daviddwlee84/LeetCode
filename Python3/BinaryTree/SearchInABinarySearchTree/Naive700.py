from ..TreeNodeModule import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        
        return None
    
# Runtime: 80 ms, faster than 59.19% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 15.7 MB, less than 70.02% of Python3 online submissions for Search in a Binary Search Tree.