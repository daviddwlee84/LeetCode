class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                       for kid in (root.left, root.right))
        return root if left and right else left or right


# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if not root:
#             return None
#         left_res = self.lowestCommonAncestor(root.left,p,q)
#         right_res = self.lowestCommonAncestor(root.right,p,q)
#
#         if (left_res and right_res) or (root in [p,q]):
#             return root
#         else:
#             return left_res or right_res
