# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Input: [1,null,2,3]
   1
    \
     2
    /
   3
'''
# def listToBinaryTree(lst):
#     for i in lst:

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