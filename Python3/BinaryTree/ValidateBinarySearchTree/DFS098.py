# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Solution:
    def isValidBST(self, root):
        return self.isBSTUtil(root, -sys.maxsize, sys.maxsize) # (+-9223372036854775807 or +-21474836480)

    def isBSTUtil(self, root, minimum, maximum):
        if root == None:
            return True
        
        if root.val <= minimum or root.val >= maximum:
            return False
        
        return self.isBSTUtil(root.left, minimum, root.val) and self.isBSTUtil(root.right, root.val, maximum)
