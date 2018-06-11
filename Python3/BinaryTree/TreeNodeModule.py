# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
        1
    2       3
  X   4

 2  3  4     5  6
[1, 2, 3, None, 4]
"""
# If parent's index is i then it's left child is i*2 and right child is i*2+1
def listToBinaryTree(lst):
    root = TreeNode(lst[0])
    nodeList = [root]
    for i in range(2, len(lst)+1):
        new_node = TreeNode(lst[i-1])
        nodeList.append(new_node)
        if nodeList[i//2]:
            if i % 2:
                nodeList[i//2-1].right = new_node
            else:
                nodeList[i//2-1].left = new_node
        else:
            print('Input Error: Not a tree list')
    return root


### Below follow LeetCode's format (i.e. Level-order)

# Deserialize
def stringToTreeNode(input_string):
    input_string = input_string.strip()
    input_string = input_string[1:-1]
    if not input_string:
        return None

    input_stringValues = [s.strip() for s in input_string.split(',')]
    root = TreeNode(int(input_stringValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(input_stringValues):
        node = nodeQueue[front]
        front = front + 1

        item = input_stringValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(input_stringValues):
            break

        item = input_stringValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

# Serialize
from queue import Queue
# i.e. Level-order Traversal
def treeNodeToList(root):
    outputList = []
    visitQueue = Queue()
    visitQueue.put(root)
    while 1:
        if visitQueue.empty():
            break
        else:
            node = visitQueue.get()
        if node:
            outputList.append(node.val)
            if node.left:
                visitQueue.put(node.left)
            else:
                visitQueue.put(None)
            if node.right:
                visitQueue.put(node.right)
            else:
                visitQueue.put(None)
        else:
            outputList.append(None)
    
    for i in range(len(outputList)-1, -1, -1):
        if outputList[i]:
            break
        else:
            outputList.pop()

    return outputList