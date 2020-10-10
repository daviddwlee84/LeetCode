# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from ..TreeNodeModule import TreeNode


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # 10**4 & 10**5 will have bug (even with + 1)
        # 10**6 will cause MemoryError
        # tree_list = [None] * (10**5)
        tree = {}  # use dict as array to avoid memory problem

        def dfs(node: TreeNode, i: int):
            if not node:
                return

            tree[i] = node.val
            dfs(node.left, 2 * (i + 1) - 1)
            dfs(node.right, 2 * (i + 1))

        dfs(root, 0)

        return str(tree)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        tree = eval(data)

        def build(i: int) -> TreeNode:
            if i not in tree:
                return None

            node = TreeNode(tree[i])
            node.left = build(2 * (i + 1) - 1)
            node.right = build(2 * (i + 1))
            return node

        return build(0)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
