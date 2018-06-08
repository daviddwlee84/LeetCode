class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        else:
            return self.isSymmetricHelper(root.left, root.right)
        
    def isSymmetricHelper(self, leftnode, rightnode):
        if not leftnode and not rightnode: # Both reach leaf
            return True
        elif not leftnode or not rightnode: # Only one reach leaf
            return False
        else:
            '''
                O
               / \
              A   A
             / \ / \
            B  C C  B
            '''
            if leftnode.val != rightnode.val: # Check if values are the same (A)
                return False
            else:
                # Check if left child of left node equal to right child of right node (B)
                # And
                # Check if right child of left node equal to left child of right node (C)
                return self.isSymmetricHelper(leftnode.left, rightnode.right) & self.isSymmetricHelper(leftnode.right, rightnode.left)