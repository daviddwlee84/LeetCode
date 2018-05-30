import BinaryTree.TreeNodeModule as tn
from BinaryTree.BinaryTreePreorderTraversal.Recursive144 import Solution as preorder_recursive
from BinaryTree.BinaryTreePreorderTraversal.Iterative144 import Solution as preorder_iterative

testcase = []
testcase.append(tn.stringToTreeNode("[1,null,2,3]"))
testcase.append(tn.stringToTreeNode("[]"))
testcase.append(tn.stringToTreeNode("[2,3,null,1]"))

preorderAns = []
preorderAns.append([1,2,3])
preorderAns.append([])
preorderAns.append([2,3,1])

def test_recursive_preorder():
    for num, case in enumerate(testcase):
        assert preorder_recursive().preorderTraversal(case) == preorderAns[num]
    
def test_iterative_preorder():
    for num, case in enumerate(testcase):
        assert preorder_iterative().preorderTraversal(case) == preorderAns[num]

from BinaryTree.BinaryTreeInorderTraversal.Recursive94 import Solution as inorder_recursive
from BinaryTree.BinaryTreeInorderTraversal.Iterative94 import Solution as inorder_iterative

inorderAns = []
inorderAns.append([1,3,2])
inorderAns.append([])
inorderAns.append([1,3,2])

def test_recursive_inorder():
    for num, case in enumerate(testcase):
        assert inorder_recursive().inorderTraversal(case) == inorderAns[num]
    
def test_iterative_inorder():
    for num, case in enumerate(testcase):
        assert inorder_iterative().inorderTraversal(case) == inorderAns[num]