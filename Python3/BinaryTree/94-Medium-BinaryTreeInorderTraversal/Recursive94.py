class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.outputStack = []

        if root == None:
            return []
        self.__inorderTraversalHelper(root)
        return self.outputStack

    def __inorderTraversalHelper(self, root):
        if root.left != None:
            self.__inorderTraversalHelper(root.left)
        self.outputStack.append(root.val)
        if root.right != None:
            self.__inorderTraversalHelper(root.right)