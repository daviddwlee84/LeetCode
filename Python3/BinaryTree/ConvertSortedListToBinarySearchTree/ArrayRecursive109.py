from typing import Optional, List
from ..TreeNodeModule import TreeNode
from ...LinkedList.ListNodeModule import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return self.sortedArrayToBST(array)

    def sortedArrayToBST(self, array: List[int]) -> Optional[TreeNode]:
        if not array:
            return None
        mid = len(array) // 2
        return TreeNode(array[mid], self.sortedArrayToBST(array[:mid]), self.sortedArrayToBST(array[mid + 1:]))
