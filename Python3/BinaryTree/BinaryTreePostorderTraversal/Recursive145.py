class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.outputStack = []

        if root == None:
            return []
        self.__postorderTraversalHelper(root)
        return self.outputStack

    def __postorderTraversalHelper(self, root):
        if root.left != None:
            self.__postorderTraversalHelper(root.left)
        if root.right != None:
            self.__postorderTraversalHelper(root.right)
        self.outputStack.append(root.val)