# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        total = 0
        while head is not None:
            total *= 2
            total += head.val
            head = head.next

        return total
