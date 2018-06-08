class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        if root.left and root.right:
            leftStack = [root.left]
            rightStack = [root.right]
        elif not root.left and not root.right: # The tree only has root
            return True
        else: # Miss either left or right child
            return False

        
        while leftStack and rightStack:

            # Visit and compare
            leftNode = leftStack.pop()
            rightNode = rightStack.pop()
            if leftNode.val != rightNode.val:
                return False
            
            # Check if there is one tree has the child but the other one doesn't have
            if (not leftNode.left and rightNode.right) or (leftNode.left and not rightNode.right):
                return False
            if (not leftNode.right and rightNode.left) or (leftNode.right and not rightNode.left):
                return False
            
            # Left subtree traversal _LR
            if leftNode.right:
                leftStack.append(leftNode.right)
            if leftNode.left:
                leftStack.append(leftNode.left)
                    
            # Right subtree traversal _RL
            if rightNode.left:
                rightStack.append(rightNode.left)
            if rightNode.right:
                rightStack.append(rightNode.right)

        return True