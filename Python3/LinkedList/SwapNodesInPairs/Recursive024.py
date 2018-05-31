from ..ListNodeModule import ListNode, printListNode, listNodeConverter

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Don't need to swap
        if not head or not head.next:
            return head
        
        # Old:
        # head -> head.next -> nextPair
        # New:
        # head.next -> head              -> nextPair
        # (newHead)    (head.next.next)     (swapPairs(nextPair))
        nextPair = head.next.next
        newHead = head.next
        head.next.next = head
        head.next = self.swapPairs(nextPair)
        return newHead
