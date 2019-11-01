from BinaryTree.MinimumDepthofBinaryTree.BFS111 import Solution as BFS
import BinaryTree.TreeNodeModule as tn

raw_testcase = [
    ("[]", 0),
    ("[1]", 1),
    ("[3,9,20,null,null,15,7]", 2)
]
testcase = [(tn.stringToTreeNode(treeStr), ans) for treeStr, ans in raw_testcase]

def test_BFS():
    for root, ans in testcase:
        assert BFS().minDepth(root) == ans
