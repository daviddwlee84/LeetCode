import BinaryTree.TreeNodeModule as tn
from BinaryTree.BinaryTreePreorderTraversal.Recursive144 import Solution as preorder_recursive
from BinaryTree.BinaryTreePreorderTraversal.Iterative144 import Solution as preorder_iterative

testcase = []
'''
  1
   \
    2
   /
  3
'''
testcase.append(tn.stringToTreeNode("[1,null,2,3]"))
'''
None
'''
testcase.append(tn.stringToTreeNode("[]"))
'''
    2
   /
  3
 /
1
'''
testcase.append(tn.stringToTreeNode("[2,3,null,1]"))
'''
  3
 / \
1   2
'''
testcase.append(tn.stringToTreeNode("[3,1,2]"))

preorderAns = []
preorderAns.append([1,2,3])
preorderAns.append([])
preorderAns.append([2,3,1])
preorderAns.append([3,1,2])


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
inorderAns.append([1,3,2])

def test_recursive_inorder():
    for num, case in enumerate(testcase):
        assert inorder_recursive().inorderTraversal(case) == inorderAns[num]
    
def test_iterative_inorder():
    for num, case in enumerate(testcase):
        assert inorder_iterative().inorderTraversal(case) == inorderAns[num]

from BinaryTree.BinaryTreePostorderTraversal.Recursive145 import Solution as postorder_recursive
from BinaryTree.BinaryTreePostorderTraversal.Iterative145 import Solution as postorder_iterative

postorderAns = []
postorderAns.append([3,2,1])
postorderAns.append([])
postorderAns.append([1,3,2])
postorderAns.append([1,2,3])

def test_recursive_postorder():
    for num, case in enumerate(testcase):
        assert postorder_recursive().postorderTraversal(case) == postorderAns[num]
    
def test_iterative_postorder():
    for num, case in enumerate(testcase):
        assert postorder_iterative().postorderTraversal(case) == postorderAns[num]