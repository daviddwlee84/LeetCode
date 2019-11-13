# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
from ..TreeNodeModule import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        mid_idx = len(nums)//2
        
        node = TreeNode(nums[mid_idx])

        if len(nums) == 1:
            # only one element in the nums
            return node
        
        node.left = self.sortedArrayToBST(nums[:mid_idx])
        node.right = self.sortedArrayToBST(nums[mid_idx+1:])

        return node
