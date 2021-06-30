from ..TreeNodeModule import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            # if root is p or q, then we don't need to search its children
            return root

        left, right = (self.lowestCommonAncestor(kid, p, q)
                       for kid in (root.left, root.right))
        # since a common ancestor can be in only left or right subtree if it is not current node
        return root if left and right else left or right


# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if not root:
#             return None
#         left_res = self.lowestCommonAncestor(root.left, p, q)
#         right_res = self.lowestCommonAncestor(root.right, p, q)
#
#         if (left_res and right_res) or (root in [p, q]):
#             return root
#         else:
#             return left_res or right_res
