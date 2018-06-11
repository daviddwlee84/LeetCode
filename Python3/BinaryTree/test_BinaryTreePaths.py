from BinaryTree.BinaryTreePaths.Iterative257 import Solution as iterative
from BinaryTree.BinaryTreePaths.Recursive257 import Solution as recursive
import BinaryTree.TreeNodeModule as tn

testtree = tn.stringToTreeNode("[1,2,3,null,5]")
ans = ["1->2->5","1->3"]

def test_iterative():
    assert iterative().binaryTreePaths(testtree) == ans

def test_recursive():
    assert recursive().binaryTreePaths(testtree) == ans
