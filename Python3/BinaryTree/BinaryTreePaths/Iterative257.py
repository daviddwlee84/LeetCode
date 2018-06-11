class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        paths = []

        if not root:
            return paths

        preorderStack = [root]
        visited = []

        while preorderStack:
            
            # visit node
            node = preorderStack[-1]
            if node not in visited:
                visited.append(node)
            
            if not node.left and not node.right:
                # when reach leaf, current stack is the path
                paths.append(self.pathStackToString(preorderStack))
                
            if node.left and node.left not in visited:
                # travel left child (if haven't visited)
                preorderStack.append(node.left)
            elif node.right and node.right not in visited:
                # travel right child (if haven't visited)
                preorderStack.append(node.right)
            else:
                # no where to go or all child have visited
                preorderStack.pop()
                
        return paths

    # Transfer stack in to string of path
    def pathStackToString(self, stack):
        string = ""
        for idx in range(len(stack)-1):
            string += str(stack[idx].val)
            string += "->"
        string += str(stack[-1].val)
        return string


