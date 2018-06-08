from BinaryTree.MaximumDepthofBinaryTree.TopDown import Solution as TopDown
import BinaryTree.TreeNodeModule as tn

'''
    3
   / \
  9  20
    /  \
   15   7
'''
testTree = tn.stringToTreeNode("[3,9,20,null,null,15,7]")
depthAns = 3
testTree2 = tn.stringToTreeNode("[]")
depthAns2 = 0
testTree3 = tn.stringToTreeNode("[1]")
depthAns3 = 1

def test_TopDown():
    assert TopDown().maxDepth(testTree) == depthAns
    assert TopDown().maxDepth(testTree2) == depthAns2
    assert TopDown().maxDepth(testTree3) == depthAns3


from BinaryTree.MaximumDepthofBinaryTree.BottomUp import Solution as BottomUp

def test_BottomUp():
    assert BottomUp().maxDepth(testTree) == depthAns
    assert BottomUp().maxDepth(testTree2) == depthAns2
    assert BottomUp().maxDepth(testTree3) == depthAns3