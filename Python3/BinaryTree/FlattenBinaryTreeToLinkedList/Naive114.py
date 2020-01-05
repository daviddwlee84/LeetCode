from ..TreeNodeModule import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.treeNodeList = []
        self.preorderTraversal(root)
        for i in range(len(self.treeNodeList)-1):
            node = self.treeNodeList[i]
            node.left = None
            node.right = self.treeNodeList[i+1]

    def preorderTraversal(self, root: TreeNode) -> None:
        if not root:
            return

        self.treeNodeList.append(root)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

# Runtime: 36 ms, faster than 75.74% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Flatten Binary Tree to Linked List.
