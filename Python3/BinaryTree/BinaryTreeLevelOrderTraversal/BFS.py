class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        outputStack = []

        if not root:
            return outputStack
        
        outputStack.append([])
        visitQueue = [root]
        thislevelnum = 1
        nextlevelnum = 0
        level = 0
        while visitQueue:
            node = visitQueue.pop()
            outputStack[level].append(node.val)
            thislevelnum -= 1 # Because get one number from queue

            if node.left: # Add left subnode
                visitQueue.insert(0, node.left) # Put left node
                nextlevelnum += 1

            if node.right: # Add right subnode
                visitQueue.insert(0, node.right) # Put right node
                nextlevelnum += 1

            if thislevelnum == 0: # This level is end, go to next level
                if visitQueue: # If there is node hasn't visited
                    outputStack.append([])
                thislevelnum = nextlevelnum
                nextlevelnum = 0
                level += 1
            
        return outputStack
