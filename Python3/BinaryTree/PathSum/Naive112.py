class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        self.sum = sum
        self.pathSum = [] # Store all path sum
        self.hasPathSumHelper(root, 0)
        if sum in self.pathSum:
            return True
        else:
            return False

    def hasPathSumHelper(self, root, lastSum):
        currentSum = lastSum + root.val
        if not root.left and not root.right: # Save path sum when reach leaf
            self.pathSum.append(currentSum)
        if root.left:
            self.hasPathSumHelper(root.left, currentSum)
        if root.right:
            self.hasPathSumHelper(root.right, currentSum)
            
