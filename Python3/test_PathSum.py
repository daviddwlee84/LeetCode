from BinaryTree.PathSum.Naive112 import Solution as PathSum_Naive
import BinaryTree.TreeNodeModule as tn

testcase1 = tn.stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,null,1]")
sum1 = 22
ans1 = True

testcase2 = []
sum2 = 1
ans2 = False

testcase3 = tn.stringToTreeNode("[-2,null,-3]")
sum3 = -5
ans3 = True

def test_PathSumNaive():
    assert PathSum_Naive().hasPathSum(testcase1, sum1) == ans1
    assert PathSum_Naive().hasPathSum(testcase2, sum2) == ans2
    assert PathSum_Naive().hasPathSum(testcase3, sum3) == ans3