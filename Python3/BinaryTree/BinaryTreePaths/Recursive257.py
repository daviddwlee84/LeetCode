class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        self.paths = []
        
        if root:
            self.findPaths(root, str(root.val) + "")
        
        return self.paths

        
    def findPaths(self, node, pathString):
        if not node.left and not node.right:
            # when reach leaf, append current path string
            self.paths.append(pathString)
        if node.left:
            self.findPaths(node.left, pathString + "->" + str(node.left.val))
        if node.right:
            self.findPaths(node.right, pathString + "->" + str(node.right.val))
