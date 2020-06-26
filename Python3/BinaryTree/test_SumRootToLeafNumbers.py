from BinaryTree.SumRootToLeafNumbers.Naive129 import Solution as naive
from BinaryTree.SumRootToLeafNumbers.DFS129 import Solution as dfs
import BinaryTree.TreeNodeModule as tn


testcase = [
    (tn.listToBinaryTree([1, 2, 3]), 25),
    (tn.listToBinaryTree([4, 9, 0, 5, 1]), 1026)
]


def test_naive():
    for root, ans in testcase:
        assert naive().sumNumbers(root) == ans


def test_dfs():
    for root, ans in testcase:
        assert dfs().sumNumbers(root) == ans
