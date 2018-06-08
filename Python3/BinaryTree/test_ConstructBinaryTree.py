from BinaryTree.ConstructBinaryTreefromInorderandPostorderTraversal.DivideAndConquer import Solution as InPostOrder_DC
import BinaryTree.TreeNodeModule as tn

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
treeAns = tn.stringToTreeNode("[3,9,20,null,null,15,7]")

inorder2 = []
postorder2 = []
treeAns2 = tn.stringToTreeNode("[]") 

def test_InorderAndPostorderDivideAndConquer():
    assert tn.treeNodeToList(InPostOrder_DC().buildTree(inorder, postorder)) == tn.treeNodeToList(treeAns)
    assert tn.treeNodeToList(InPostOrder_DC().buildTree(inorder2, postorder2)) == tn.treeNodeToList(treeAns2) 