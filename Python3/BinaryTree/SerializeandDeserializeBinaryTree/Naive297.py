# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# i.e. The stringToTreeNode, treeNodeToList function in my TreeNodeModule.py
# follow the LeetCode convention

import sys
sys.path.append('..')
from collections import deque
from BinaryTree.TreeNodeModule import TreeNode, stringToTreeNode, treeNodeToList

class Codec:

    # i.e. Level-order traversal
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        visitQueue = deque([root])
        serializedString = '['

        while visitQueue:
            node = visitQueue.pop()
            if node is not None:
                serializedString += str(node.val) + ','
                visitQueue.appendleft(node.left)
                visitQueue.appendleft(node.right)
            else:
                serializedString += 'null,'

            if all(n is None for n in visitQueue):
                break # skip when all the element in queue is None
            
        serializedString = serializedString[:-1] + ']'
        if serializedString == '[null]':
            return '[]'
        return serializedString
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        items = data[1:-1].split(',')
        if items == ['']:
            return None

        nodes = []
        front = 0 # indicate the parent node
        for i, item in enumerate(items):
            if item == 'null':
                val = None
            else:
                val = int(item)

            if val is not None:
                node = TreeNode(val)
            else:
                node = None

            if i > 0:
                parent_node = nodes[front]
                if i % 2 != 0: # odd
                    parent_node.left = node
                else: # even
                    parent_node.right = node
                    front += 1 # move to next parent node

            if node is not None:
                nodes.append(node)
        
        return nodes[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == "__main__":
    # cd ..; python3 SerializeandDeserializeBinaryTree/Naive297.py
    test = Codec()
    print(test.serialize(stringToTreeNode("[]")))
    print(treeNodeToList(test.deserialize("[]")))
    print(test.serialize(stringToTreeNode("[1,2,3,null,null,4,5]")))
    print(treeNodeToList(test.deserialize("[1,2,3,null,null,4,5]")))
    print(test.serialize(stringToTreeNode("[-1,0,1]")))
    print(treeNodeToList(test.deserialize("[-1,0,1]")))
    # from BinaryTree.TreeNodeModule import drawtree
    # drawtree(stringToTreeNode("[5,2,3,null,null,2,4,3,1]"))
    # drawtree(test.deserialize("[5,2,3,null,null,2,4,3,1]"))
    print(test.serialize(stringToTreeNode("[5,2,3,null,null,2,4,3,1]")))
    print(treeNodeToList(test.deserialize("[5,2,3,null,null,2,4,3,1]")))
