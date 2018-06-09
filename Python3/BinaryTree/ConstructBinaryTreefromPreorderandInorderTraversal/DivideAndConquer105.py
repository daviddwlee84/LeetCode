from ..TreeNodeModule import TreeNode
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        inorderIdx = inorder.index(root.val)
        leftInorder = inorder[:inorderIdx]
        rightInorder = inorder[inorderIdx+1:]
        root.left = self.buildTree(preorder[1:len(leftInorder)+1], leftInorder)
        root.right = self.buildTree(preorder[-len(rightInorder):], rightInorder)

        return root