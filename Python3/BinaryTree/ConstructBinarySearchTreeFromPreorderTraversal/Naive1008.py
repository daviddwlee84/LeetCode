from typing import List
from ..TreeNodeModule import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # same as build tree from inorder + preorder
        # the inorder is just the sorted preorder, since the values of preorder are distinct
        inorder = sorted(preorder)
        return self.buildTree(preorder, inorder)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """ build tree recursively """
        if not preorder or not inorder:
            return None

        # first node of preorder must be the root
        root = TreeNode(preorder[0])
        # nodes seperated by the root node in inorder are just left and right sub-tree
        inorderIdx = inorder.index(root.val)
        leftInorder = inorder[:inorderIdx]
        rightInorder = inorder[inorderIdx+1:]

        # construct tree
        root.left = self.buildTree(preorder[1:len(leftInorder)+1], leftInorder)
        root.right = self.buildTree(
            preorder[-len(rightInorder):], rightInorder)

        return root
