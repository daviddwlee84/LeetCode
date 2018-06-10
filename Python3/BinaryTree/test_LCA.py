from BinaryTree.LowestCommonAncestorofaBinaryTree.Naive236 import Solution as LCA_naive
import BinaryTree.TreeNodeModule as tn

testtree1 = tn.stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]")
p1 = tn.TreeNode(5)
q1 = tn.TreeNode(1)
ans1 = 3

testtree2 = tn.stringToTreeNode("[3,5,1,6,2,0,8,null,null,7,4]")
p2 = tn.TreeNode(5)
q2 = tn.TreeNode(4)
ans2 = 5

def test_LCA_naive():
    assert LCA_naive().lowestCommonAncestor(testtree1, p1, q1).val == ans1
    assert LCA_naive().lowestCommonAncestor(testtree2, p2, q2).val == ans2