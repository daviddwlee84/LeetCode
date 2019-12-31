from BinaryTree.TreeNodeModule import stringToTreeNode, treeNodeToList
from BinaryTree.FlattenBinaryTreeToLinkedList.Naive114 import Solution as naive

testcase = [
    (stringToTreeNode("[1,2,5,3,4,null,6]"), stringToTreeNode(
        "[1,null,2,null,3,null,4,null,5,null,6]")),
    (stringToTreeNode("[]"), stringToTreeNode("[]")),
    (stringToTreeNode("[1]"), stringToTreeNode("[1]"))
]


def test_naive():
    for root, ans in testcase:
        naive().flatten(root)
        assert treeNodeToList(root) == treeNodeToList(ans)
