from BinaryTree.TreeNodeModule import stringToTreeNode
from BinaryTree.BinaryTreeLevelOrderTraversalII.Naive107 import Solution as naive
from BinaryTree.BinaryTreeLevelOrderTraversalII.Naive2_107 import Solution as naive2


testcase = [
    (stringToTreeNode("[3,9,20,null,null,15,7]"), [
        [15, 7],
        [9, 20],
        [3]
    ]),
    (stringToTreeNode("[]"), [])
]


def test_naive():
    for root, ans in testcase:
        assert naive().levelOrderBottom(root) == ans


def test_naive2():
    for root, ans in testcase:
        assert naive2().levelOrderBottom(root) == ans
