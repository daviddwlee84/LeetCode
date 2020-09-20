# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ..ListNodeModule import ListNode

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        
        # TODO: array[n-1:m-2:-1] => bug
        answer = array[:m-1] + list(reversed(array[m-1:n])) + array[n:]

        dummy_head = ListNode()
        node = dummy_head
        for num in answer:
            node.next = ListNode(num)
            node = node.next
        
        return dummy_head.next

# Runtime: 36 ms, faster than 41.68% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 13.8 MB, less than 89.96% of Python3 online submissions for Reverse Linked List II.
        
