# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ..ListNodeModule import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        index = 0
        index2node = {}
        node = head
        while node != None:
            index2node[index] = node
            index += 1
            node = node.next
        
        # index here will be the length of linked list
        
        if index-n-1 >= 0 and index-n+1 < index: # normal case
            index2node[index-n-1].next = index2node[index-n+1]
        elif index-n-1 >= 0 and index-n+1 >= index: # delete tail one
            index2node[index-n-1].next = None
        elif index-n-1 < 0: # delete head
            if index-n+1 < index: # still have something left
                head = head.next
            else:
                head = None

        return head