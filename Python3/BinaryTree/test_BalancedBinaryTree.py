from BinaryTree.TreeNodeModule import stringToTreeNode
from BinaryTree.BalancedBinaryTree.Naive110 import Solution as naive
from BinaryTree.BalancedBinaryTree.Recursive110 import Solution as recursive
from BinaryTree.BalancedBinaryTree.PostorderIterative110 import Solution as postorder

testcase = [
    (stringToTreeNode("[3,9,20,null,null,15,7]"), True),
    (stringToTreeNode("[1,2,2,3,3,null,null,4,4]"), False),
    (stringToTreeNode("[1,null,2,null,3]"), False),
    (stringToTreeNode("[1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5]"), True),
    (stringToTreeNode("[]"), True)
]


def test_naive():
    for root, ans in testcase:
        assert naive().isBalanced(root) == ans


def test_recursive():
    for root, ans in testcase:
        assert recursive().isBalanced(root) == ans


def test_postorder():
    for root, ans in testcase:
        assert postorder().isBalanced(root) == ans
