from BinaryTree.TreeNodeModule import stringToTreeNode
from BinaryTree.MaximumWidthOfBinaryTree.Naive662 import Solution as naive

testcase = [
    (stringToTreeNode("[1,3,2,5,3,null,9]"), 4),
    (stringToTreeNode("[1,1,1,1,null,null,1,1,null,null,1]"), 8),
]


def test_naive():
    for root, ans in testcase:
        assert naive().widthOfBinaryTree(root) == ans
