from BinaryTree.SymmetricTree.Recursive import Solution as SymTree_recursive
import BinaryTree.TreeNodeModule as tn


testcase = tn.stringToTreeNode("[1,2,2,3,4,4,3]")
ans = True

testcase2 = tn.stringToTreeNode("[1,2,2,null,3,null,3]")
ans2 = False

testcase3 = tn.stringToTreeNode("[1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]")
ans3 = True

testcase4 = tn.stringToTreeNode("[]")
ans4 = True

def test_SymmetricTreeRecursive():
    assert SymTree_recursive().isSymmetric(testcase) == ans
    assert SymTree_recursive().isSymmetric(testcase2) == ans2
    assert SymTree_recursive().isSymmetric(testcase3) == ans3
    assert SymTree_recursive().isSymmetric(testcase4) == ans4
