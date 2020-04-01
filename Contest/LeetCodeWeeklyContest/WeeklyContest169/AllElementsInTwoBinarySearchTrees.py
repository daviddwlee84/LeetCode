# Definition for a binary tree node.
from typing import List

# [Python Program for Merge Sort - GeeksforGeeks](https://www.geeksforgeeks.org/python-program-for-merge-sort/)


class TreeNode:
    """ Definition for a binary tree node """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = []
        self.inorderTraversal(root1, list1)
        list2 = []
        self.inorderTraversal(root2, list2)

        return self.mergeSort(list1, list2)

    def inorderTraversal(self, root: TreeNode, nums: List[int]):
        if not root:
            return
        self.inorderTraversal(root.left, nums)
        nums.append(root.val)
        self.inorderTraversal(root.right, nums)

    def mergeSort(self, list1: List[int], list2: List[int]) -> List[int]:
        i, j = 0, 0
        ans = []
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                ans.append(list1[i])
                i += 1
            else:
                ans.append(list2[j])
                j += 1

        while i < len(list1):
            ans.append(list1[i])
            i += 1

        while j < len(list2):
            ans.append(list2[j])
            j += 1

        return ans
