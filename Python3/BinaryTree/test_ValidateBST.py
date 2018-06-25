from BinaryTree.ValidateBinarySearchTree.InorderTraversal098 import Solution as inorder
from BinaryTree.ValidateBinarySearchTree.DFS098 import Solution as dfs
import BinaryTree.TreeNodeModule as tn

testBST = []
testBST.append(tn.stringToTreeNode("[2,1,3]"))
testBST.append(tn.stringToTreeNode("[1,1]"))
testBST.append(tn.stringToTreeNode("[5,1,4,null,null,3,6]"))


answer = []
answer.append(True)
answer.append(False)
answer.append(False)

def test_inorderTraversal():
    for i, case in enumerate(testBST):
        assert inorder().isValidBST(case) == answer[i]

def test_dfs():
    for i, case in enumerate(testBST):
        assert dfs().isValidBST(case) == answer[i]
        