# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        head = self.merge2List(lists[0], lists[1])
        
        for ll in lists[2:]:
            head = self.merge2List(head, ll)
        
        return head
    
    # Merge two linked list and return head of them
    # PS. The merge2List can be simplified, since the linked lists are sorted.
    #     So if one linked list reach the end, you can simply connect the rest of the other linked list
    #     by redirect the pointer to the head of the rest linked list. 
    def merge2List(self, ll1, ll2):
        if ll1 and not ll2:
            head = ll1
            ll1 = ll1.next
        elif not ll1 and ll2:
            head = ll2
            ll2 = ll2.next
        elif ll1 and ll2:
            if ll1.val < ll2.val:
                head = ll1
                ll1 = ll1.next
            else:
                head = ll2
                ll2 = ll2.next
        else:
            return None

        current = head

        while ll1 or ll2:
            if ll1 and not ll2:
                current.next = ll1
                ll1 = ll1.next
            elif not ll1 and ll2:
                current.next = ll2
                ll2 = ll2.next
            else:
                if ll1.val < ll2.val:
                    current.next = ll1
                    ll1 = ll1.next
                else:
                    current.next = ll2
                    ll2 = ll2.next
            current = current.next
        return head
