# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ..ListNodeModule import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        odd_head = head
        odd = head
        even_head = head.next
        even = head.next

        while odd is not None and even is not None:
            if odd.next:
                odd.next = odd.next.next
            else:
                break
            if even.next:
                even.next = even.next.next
            else:
                break
            odd = odd.next
            even = even.next

        odd.next = even_head

        return odd_head

# Runtime: 44 ms, faster than 61.48% of Python3 online submissions for Odd Even Linked List.
# Memory Usage: 15.7 MB, less than 8.33% of Python3 online submissions for Odd Even Linked List.

# Official one
#
# public class Solution {
#     public ListNode oddEvenList(ListNode head) {
#         if (head == null) return null;
#         ListNode odd = head, even = head.next, evenHead = even;
#         while (even != null && even.next != null) {
#             odd.next = even.next;
#             odd = odd.next;
#             even.next = odd.next;
#             even = even.next;
#         }
#         odd.next = evenHead;
#         return head;
#     }
# }
#
# Others'
#
# def oddEvenList(self, head):
#     odds = ListNode(0)
#     evens = ListNode(0)
#     oddsHead = odds
#     evensHead = evens
#     isOdd = True
#     while head:
#         if isOdd:
#             odds.next = head
#             odds = odds.next
#         else:
#             evens.next = head
#             evens = evens.next
#         isOdd = not isOdd
#         head = head.next
#     evens.next = None
#     odds.next = evensHead.next
#     return oddsHead.next
