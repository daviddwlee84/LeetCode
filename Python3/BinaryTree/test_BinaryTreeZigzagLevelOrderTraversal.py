from BinaryTree.BinaryTreeZigzagLevelOrderTraversal.Naive102 import Solution as naive
from BinaryTree.BinaryTreeZigzagLevelOrderTraversal.WithoutReverse102 import Solution as without_recursion
from BinaryTree.TreeNodeModule import stringToTreeNode

testcase = [
    ("[3,9,20,null,null,15,7]", [
        [3],
        [20, 9],
        [15, 7]
    ]),
    ("[]", []),
    ("[1,2,3,4,null,null,5]", [[1], [3, 2], [4, 5]])
]


def test_naive():
    for tree_str, ans in testcase:
        assert naive().zigzagLevelOrder(stringToTreeNode(tree_str)) == ans


def test_without_recursion():
    for tree_str, ans in testcase:
        assert without_recursion().zigzagLevelOrder(stringToTreeNode(tree_str)) == ans
