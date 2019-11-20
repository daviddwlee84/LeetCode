# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

"""
        1
    2       3
  X   4

 2  3  4     5  6
[1, 2, 3, None, 4]
"""
# If parent's index is i then it's left child is i*2 and right child is i*2+1
def listToBinaryTree(lst):
    if len(lst) == 0:
        return None
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


# [Tree Deserializer and Visualizer for Python - LeetCode Discuss](https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python)
def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(0); turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()

if __name__ == '__main__':
    # Draw tree test
    drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
