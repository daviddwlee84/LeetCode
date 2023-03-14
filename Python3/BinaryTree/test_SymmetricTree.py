from BinaryTree.SymmetricTree.Recursive101 import Solution as SymTree_recursive
from BinaryTree.SymmetricTree.Iterative101 import Solution as SymTree_iterative
from BinaryTree.SymmetricTree.Preorder101 import Solution as SymTree_preorder
from BinaryTree.SymmetricTree.IterativeBFS101 import Solution as SymTree_iterativeBFS
import BinaryTree.TreeNodeModule as tn


testcase = tn.stringToTreeNode("[1,2,2,3,4,4,3]")
ans = True

testcase2 = tn.stringToTreeNode("[1,2,2,null,3,null,3]")
ans2 = False

testcase3 = tn.stringToTreeNode("[1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]")
ans3 = True

# NOTE: The number of nodes in the tree is in the range [1, 1000].
testcase4 = tn.stringToTreeNode("[]")
ans4 = True

testcase5 = tn.stringToTreeNode("[1]")
ans5 = True

testcase6 = tn.stringToTreeNode("[1,2,2,2,null,2]")
ans6 = False

testcase7 = tn.stringToTreeNode("[1,2,3]")
ans7 = False


def test_SymmetricTreeRecursive():
    assert SymTree_recursive().isSymmetric(testcase) == ans
    assert SymTree_recursive().isSymmetric(testcase2) == ans2
    assert SymTree_recursive().isSymmetric(testcase3) == ans3
    assert SymTree_recursive().isSymmetric(testcase4) == ans4
    assert SymTree_recursive().isSymmetric(testcase5) == ans5
    assert SymTree_recursive().isSymmetric(testcase6) == ans6
    assert SymTree_recursive().isSymmetric(testcase7) == ans7


def test_SymmetricTreeIterative():
    assert SymTree_iterative().isSymmetric(testcase) == ans
    assert SymTree_iterative().isSymmetric(testcase2) == ans2
    assert SymTree_iterative().isSymmetric(testcase3) == ans3
    assert SymTree_iterative().isSymmetric(testcase4) == ans4
    assert SymTree_iterative().isSymmetric(testcase5) == ans5
    assert SymTree_iterative().isSymmetric(testcase6) == ans6
    assert SymTree_iterative().isSymmetric(testcase7) == ans7


def test_SymmetricTreePreorder():
    assert SymTree_preorder().isSymmetric(testcase) == ans
    assert SymTree_preorder().isSymmetric(testcase2) == ans2
    assert SymTree_preorder().isSymmetric(testcase3) == ans3
    assert SymTree_preorder().isSymmetric(testcase4) == ans4
    assert SymTree_preorder().isSymmetric(testcase5) == ans5
    assert SymTree_preorder().isSymmetric(testcase6) == ans6
    assert SymTree_preorder().isSymmetric(testcase7) == ans7


def test_SymmetricTreeIterativeBFS():
    assert SymTree_iterativeBFS().isSymmetric(testcase) == ans
    assert SymTree_iterativeBFS().isSymmetric(testcase2) == ans2
    assert SymTree_iterativeBFS().isSymmetric(testcase3) == ans3
    assert SymTree_iterativeBFS().isSymmetric(testcase4) == ans4
    assert SymTree_iterativeBFS().isSymmetric(testcase5) == ans5
    assert SymTree_iterativeBFS().isSymmetric(testcase6) == ans6
    assert SymTree_iterativeBFS().isSymmetric(testcase7) == ans7
