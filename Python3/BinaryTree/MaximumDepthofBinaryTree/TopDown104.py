class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        else:
            return self.maxDepthHelper(root, 1)

    # Depth indicate current depth
    def maxDepthHelper(self, root, depth):
        leftdepth = depth
        rightdepth = depth
        if root.left:
            leftdepth = self.maxDepthHelper(root.left, depth + 1)
        if root.right:
            rightdepth = self.maxDepthHelper(root.right, depth + 1)
        return max(leftdepth, rightdepth)
