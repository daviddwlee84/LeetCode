import BinaryTree.TreeNodeModule as tn
# from BinaryTree.MinimumDepthOfBinaryTree.DFS111 import Solution as DFS
# from BinaryTree.MinimumDepthOfBinaryTree.DFSImprove111 import Solution as DFSImprove

testcases = [
    ('[4,2,6,1,3]', 1),
    ('[1,0,48,null,null,12,49]', 1),
    ('[90,69,null,49,89,null,52]', 1),
]

# TODO: the tree is not constructed to be the binary search tree
# testcases = [(tn.stringToTreeNode(tree_str), ans) for tree_str, ans in testcases]


# def test_DFS():
#     for root, ans in testcases:
#         assert DFS().minDepth(root) == ans

# def test_DFSImprove():
#     for root, ans in testcases:
#         assert DFSImprove().minDepth(root) == ans


# Wrong answer
# class Solution:
#     def minDiffInBST(self, root: Optional[TreeNode]) -> int:
#         self.min_diff = float('inf')
#
#         def dfs(node, last_num: int):
#             if not node:
#                 return
#             dfs(node.left, node.val)
#             if last_num:
#                 self.min_diff = min(self.min_diff, abs(last_num - node.val))
#             dfs(node.right, node.val)
#
#         dfs(root, None)
#         return self.min_diff
