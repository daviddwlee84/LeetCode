import TreeNode
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        outputStack = []
        travelStack = []

        if not root:
            return outputStack
        
        travelStack.append(root)
        while travelStack:
            node = travelStack.pop()
            outputStack.append(node.val)
            if node.right:
                travelStack.append(node.right)
            if node.left:
                travelStack.append(node.left)

        return outputStack