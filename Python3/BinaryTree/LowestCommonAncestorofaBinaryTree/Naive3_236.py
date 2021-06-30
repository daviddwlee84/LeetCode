from ..TreeNodeModule import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        To see if a node has p and q as their descendant. Find the deepest one.
        (This will have lots of redundant search)
        """
        self.answer = None
        self.answer_depth = -1

        def is_descendant(node: 'TreeNode', target: 'TreeNode', depth: int):
            if not node:
                return False, None

            if node == target:
                return True, 'self'
            is_left, _ = is_descendant(node.left, target, depth + 1)
            if is_left:
                return True, 'left'
            is_right, _ = is_descendant(node.right, target, depth + 1)
            if is_right:
                return True, 'right'

            return False, None

        def dfs(node: 'TreeNode', depth: int):
            is_p, direct_p = is_descendant(node, p, depth)
            is_q, direct_q = is_descendant(node, q, depth)

            # print(node.val, (is_p, direct_p), (is_q, direct_q))

            if is_p and is_q:
                if depth > self.answer_depth:
                    self.answer = node
                    self.answer_depth = depth

                if direct_p == direct_q:
                    if direct_p == 'left':
                        dfs(node.left, depth + 1)
                    elif direct_p == 'right':
                        dfs(node.right, depth + 1)

        dfs(root, 0)

        return self.answer

# TLE
# [-1,0,null,1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9,null,10,null,11,null,12,null,13,null,14,null,15,null,16,null,17,null,18,null,19,null,20,null,21,null,22,null,23,null,24,null,25,null,26,null,27,null,28,null,29,null,30,null,31,null,32,null,33,null,34,null,35,null,36,null,37,null,38,null,39,null,40,null,41,null,42,null,43,null,44,null,45,null,46,null,47,null,48,null,49,null,50,null,51,null,52,null,53,null,54,null,55,null,56,null,57,null,58,null,59,null,60,null,61,null,62,null,63,null,64,null,65,null,66,null,67,null,68,null,69,null,70,null,71,null,72,null,73,null,74,null,75,null,76,null,77,null,78,null,79,null,80,null,81,null,82,null,83,null,84,null,85,null,86,null,87,null,88,null,89,null,90,null,91,null,92,null,93,null,94,null,95,null,96,null,97,null,98,null,99,null,100,null,101,null,102,null,103,null,104,null,105,null,106,null,107,null,108,null,109,null,110,null,111,null,112,null,113,null,114,null,115,null,116,null,117,null,118,null,119,null,120,null,121,null,122,null
# 9998
