from ..TreeNodeModule import TreeNode


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(o_node: TreeNode, c_node: TreeNode) -> TreeNode:
            if o_node == target:
                return c_node

            if o_node.left:
                obj = dfs(o_node.left, c_node.left)
                if obj is not None:
                    return obj

            if o_node.right:
                obj = dfs(o_node.right, c_node.right)
                if obj is not None:
                    return obj

        return dfs(original, cloned)
