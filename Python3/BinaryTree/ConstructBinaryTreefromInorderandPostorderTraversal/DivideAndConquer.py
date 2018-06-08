from ..TreeNodeModule import TreeNode

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # No tree to build
        if not inorder or not postorder:
            return None
        
        # The last node of postorder is root
        rootval = postorder.pop()
        root = TreeNode(rootval)
        
        # Find the position of root in inorder (it seperate left and right subtree)
        rootIdx = inorder.index(rootval)

        # Build left subtree
        leftInorder = inorder[:rootIdx]
        leftPostorder = postorder[:len(leftInorder)]
        root.left = self.buildTree(leftInorder, leftPostorder)

        # Build right subtree
        rightInorder = inorder[rootIdx+1:]
        rightPostorder = postorder[-len(rightInorder):]
        root.right = self.buildTree(rightInorder, rightPostorder)

        return root