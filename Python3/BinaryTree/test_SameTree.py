from BinaryTree.TreeNodeModule import listToBinaryTree
from BinaryTree.SameTree.Recursive100 import Solution as recursive
from BinaryTree.SameTree.Naive100 import Solution as naive


testcase = [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, None, 2], False),
    ([1, 2, 3], [1, 1, 2], False),
    ([], [], True)
]


def test_recursive():
    for p_list, q_list, isSame in testcase:
        p = listToBinaryTree(p_list)
        q = listToBinaryTree(q_list)
        assert recursive().isSameTree(p, q) == isSame


def test_naive():
    for p_list, q_list, isSame in testcase:
        p = listToBinaryTree(p_list)
        q = listToBinaryTree(q_list)
        assert naive().isSameTree(p, q) == isSame
