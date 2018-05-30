class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        outputStack = []
        travelStack = []

        if not root:
            return outputStack
        
        node = root
        while travelStack or node: # if stack is not empty or node is not None
            if node: # travel all left subtree and push into stack
                travelStack.append(node)
                node = node.left
            else: # the end of left subtree
                # pop and visit
                node = travelStack.pop()
                outputStack.append(node.val)

                node = node.right # go to right subtree

        return outputStack