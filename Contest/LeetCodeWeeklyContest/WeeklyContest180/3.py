# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sortedList = self.traverseTree(root)
        return self.buildBalanceBST(sortedList, 0, len(sortedList)-1)

    def traverseTree(self, node: TreeNode) -> List[int]:
        """ iterative inorder traversal """
        stack = []
        result = []

        while True:
            if node is not None:
                stack.append(node)
                node = node.left

            elif stack:
                node = stack.pop()
                result.append(node.val)
                node = node.right
            else:
                break

        return result

    def buildBalanceBST(self, sortedList: List[int], start: int, end: int) -> TreeNode:
        """ recursively doing binary search search like seperation """

        if start > end:
            return None

        mid = (start + end) // 2
        root = TreeNode(sortedList[mid])

        root.left = self.buildBalanceBST(sortedList, start, mid-1)
        root.right = self.buildBalanceBST(sortedList, mid+1, end)

        return root
