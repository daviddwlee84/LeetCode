from ..TreeNodeModule import TreeNode
from typing import List


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(postorder[-1])
        inorder_root_idx = inorder.index(root.val)
        left_inorder = inorder[:inorder_root_idx]
        right_inorder = inorder[inorder_root_idx+1:]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[-len(right_inorder)-1:-1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root
