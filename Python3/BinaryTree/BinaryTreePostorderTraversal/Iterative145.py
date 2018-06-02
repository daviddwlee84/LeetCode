class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        outputStack = []

        if root == None:
            return outputStack
        
        travelStack = [root]
        while travelStack:
            node = travelStack.pop()
            outputStack.insert(0, node.val)
            if node.left:
                travelStack.append(node.left)
            if node.right:
                travelStack.append(node.right)
        
        return outputStack
        