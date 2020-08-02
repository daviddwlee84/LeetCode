from BinaryTree.TreeNodeModule import stringToTreeNode
from BinaryTree.BinaryTreeTilt.Naive559 import Solution as naive

testcase = [
    ("[1,2,3]", 1),
    ("[1,2,3,2]", 3),
    ("[1,2,3,4,null,5]", 11),
]


def test_naive():
    for root_str, ans in testcase:
        assert naive().findTilt(stringToTreeNode(root_str)) == ans
