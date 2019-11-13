# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from ..TreeNodeModule import TreeNode
from ...LinkedList.ListNodeModule import ListNode

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        mid = self.findMiddle(head)
        
        # Create a tree node with the middle node
        node = TreeNode(mid.val)
        
        if head == mid:
            # Base case when there is just one element in linked list!
            return node
        
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        
        return node


    def findMiddle(self, head: ListNode) -> ListNode:
        """ two pointer one's speed is another's twice """
        
        # Initial
        prevPtr = None # the pointer used to disconnect the left half from the mid node
        slowPtr = head
        fastPtr = head
        
        # Loop until fastPtr reach the end
        # and the slowPtr will be the middle node
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        
        if prevPtr:
            # break the connection of the left half and the right half linked list
            prevPtr.next = None
        # if slowPtr == head, then prevPtr will be None
        # thus we should avoid it
        
        return slowPtr # the middle node
