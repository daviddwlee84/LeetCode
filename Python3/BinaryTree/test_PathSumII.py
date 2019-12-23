from BinaryTree.TreeNodeModule import stringToTreeNode
from BinaryTree.PathSumII.Naive113 import Solution as DFS

testcase = [
    (stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,5,1]"), 22, [
        [5, 4, 11, 2],
        [5, 8, 4, 5]
    ]),
    (stringToTreeNode("[5]"), 5, [
        [5]
    ]),
    (stringToTreeNode("[6]"), 5, []),
    (stringToTreeNode("[]"), 1, []),
    (stringToTreeNode("[-2,null,-3]"), -5, [
        [[-2, -3]]
    ])
]


def test_dfs():
    for root, s, ans in testcase:
        assert DFS().pathSum(root, s).sort() == ans.sort()
