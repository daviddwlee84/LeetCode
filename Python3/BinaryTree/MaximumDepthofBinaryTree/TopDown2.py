class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.depthAns = 0
        self.maxDepthHelper(root, 1)
        return self.depthAns

    # Depth indicate current depth
    def maxDepthHelper(self, root, depth):
        if not root:
            return
        if not root.left and not root.right: # update the maximum answer when reach the end of leaf
            self.depthAns = max(self.depthAns, depth)

        self.maxDepthHelper(root.left, depth + 1)
        self.maxDepthHelper(root.right, depth + 1)
