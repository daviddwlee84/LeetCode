# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        self.traversalList = []
        self.inorderTraversal(root)
        
        for i in range(len(self.traversalList)-1):
            if self.traversalList[i] >= self.traversalList[i+1]:
                return False
        
        return True
        
        
    def inorderTraversal(self, root):
        if root.left:
            self.inorderTraversal(root.left)
        self.traversalList.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
        
        