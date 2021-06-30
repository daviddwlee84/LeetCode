class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        Directly search p and q and record its' path.
        Pick the last same node of their path

        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        pathP = self.PathToNode(root, p.val)
        pathQ = self.PathToNode(root, q.val)

        sameStack = []

        # Compare the path and return the last same node
        for i in range(min(len(pathP), len(pathQ))):
            if pathP[i].val == pathQ[i].val:
                sameStack.append(pathP[i])
            else:
                break

        return sameStack[-1]
        
    # Return path value as list
    def PathToNode(self, root, nodeVal):
        
        path = []

        def visit(root, nodeVal):
            if not root:
                return False
            # if find the node or it's descendant has the node return true
            if root.val == nodeVal or visit(root.left, nodeVal) or visit(root.right, nodeVal):
                path.insert(0, root)
                return True
            return False

        visit(root, nodeVal)
        return path

            