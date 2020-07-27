from BinaryTree.ConstructBinaryTreefromPreorderandInorderTraversal.DivideAndConquer105 import Solution as PreInOrder_DC
from BinaryTree.ConstructBinaryTreefromInorderandPostorderTraversal.DivideAndConquer106 import Solution as InPostOrder_DC
import BinaryTree.TreeNodeModule as tn

inorder = [9, 3, 15, 20, 7]
preorder = [3, 9, 20, 15, 7]
postorder = [9, 15, 7, 20, 3]
treeAns = tn.stringToTreeNode("[3,9,20,null,null,15,7]")

inorder2 = []
preorder2 = []
postorder2 = []
treeAns2 = tn.stringToTreeNode("[]")

#   1
#        4
#     2
#       3

inorder3 = [1, 2, 3, 4]
preorder3 = [1, 4, 2, 3]
postorder3 = [3, 2, 4, 1]
treeAns3 = tn.stringToTreeNode("[1,null,4,2,null,null,3]")


def test_PreorderAndInorderDivideAndConquer():
    assert tn.treeNodeToList(PreInOrder_DC().buildTree(
        preorder, inorder)) == tn.treeNodeToList(treeAns)
    assert tn.treeNodeToList(PreInOrder_DC().buildTree(
        preorder2, inorder2)) == tn.treeNodeToList(treeAns2)
    assert tn.treeNodeToList(PreInOrder_DC().buildTree(
        preorder3, inorder3)) == tn.treeNodeToList(treeAns3)


def test_InorderAndPostorderDivideAndConquer():
    assert tn.treeNodeToList(InPostOrder_DC().buildTree(
        inorder, postorder)) == tn.treeNodeToList(treeAns)
    assert tn.treeNodeToList(InPostOrder_DC().buildTree(
        inorder2, postorder2)) == tn.treeNodeToList(treeAns2)
    assert tn.treeNodeToList(InPostOrder_DC().buildTree(
        inorder3, postorder3)) == tn.treeNodeToList(treeAns3)
