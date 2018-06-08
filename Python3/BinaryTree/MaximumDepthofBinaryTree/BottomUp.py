class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        
        leftdepth = 0
        rightdepth = 0
        if root.left:
            leftdepth = self.maxDepth(root.left)
        if root.right:
            rightdepth = self.maxDepth(root.right)
        
        return max(leftdepth, rightdepth) + 1
