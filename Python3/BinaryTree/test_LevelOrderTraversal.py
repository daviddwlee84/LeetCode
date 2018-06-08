import BinaryTree.TreeNodeModule as tn
from BinaryTree.BinaryTreeLevelOrderTraversal.BFS102 import Solution as levelorder_BFS

testcase = []
'''
    3
   /  \
  9    20
      /  \
     15   7
'''
testcase.append(tn.stringToTreeNode("[3,9,20,null,null,15,7]"))
'''
None
'''
testcase.append(tn.stringToTreeNode("[]"))

levelOrderAns = []
levelOrderAns.append([[3],[9,20],[15,7]])
levelOrderAns.append([])

def test_BFS_LevelOrder():
    for num, case in enumerate(testcase):
        assert levelorder_BFS().levelOrder(case) == levelOrderAns[num]



