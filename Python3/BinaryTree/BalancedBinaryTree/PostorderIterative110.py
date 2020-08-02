from ..TreeNodeModule import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        https://leetcode.com/problems/balanced-binary-tree/discuss/35708/VERY-SIMPLE-Python-solutions-(iterative-and-recursive)-both-beat-90
        """
        stack = []
        node = root
        last = None
        depth = {}

        while stack or node:
            if node:
                # Just keep going left while it have reach the end
                stack.append(node)
                node = node.left

            else:
                # Reach the end
                node = stack[-1]
                if not node.right or last == node.right:
                    # We need to backtrack (i.e. pop node from stack)
                    node = stack.pop()
                    left_depth = depth.get(node.left, 0)
                    right_depth = depth.get(node.right, 0)

                    if abs(left_depth - right_depth) > 1:
                        return False

                    depth[node] = 1 + max(left_depth, right_depth)

                    last = node  # make sure we won't go right again
                    node = None  # so we will pop another node
                else:
                    # Usually when we can go right, we will go right first
                    node = node.right

        return True

# Runtime: 48 ms, faster than 90.98% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 14.2 MB, less than 99.63% of Python3 online submissions for Balanced Binary Tree.
