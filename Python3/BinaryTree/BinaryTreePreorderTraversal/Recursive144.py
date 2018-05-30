class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.outputStack = []

        if root == None:
            return []
        self.__preorderTraversalHelper(root)
        return self.outputStack

    def __preorderTraversalHelper(self, root):
        self.outputStack.append(root.val)
        if root.left != None:
            self.__preorderTraversalHelper(root.left)
        if root.right != None:
            self.__preorderTraversalHelper(root.right)