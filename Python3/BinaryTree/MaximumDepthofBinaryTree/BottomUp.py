class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        
        leftdepth = self.maxDepth(root.left)
        rightdepth = self.maxDepth(root.right)
        
        return max(leftdepth, rightdepth) + 1
