from ..ListNodeModule import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        fakeRoot = ListNode(-1)
        current = fakeRoot.next = head

        while current and current.next:
            if current.val <= current.next.val:
                # already sorted
                current = current.next
            else:
                # delete current.next and save as temp
                temp = current.next
                current.next = current.next.next

                # iterate from the start to find the position to insert
                previous = fakeRoot
                while previous.next.val <= temp.val:
                    previous = previous.next

                # insert after previous node
                temp.next = previous.next
                previous.next = temp

        return fakeRoot.next

# Runtime: 200 ms, faster than 67.41% of Python3 online submissions for Insertion Sort List.
# Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for Insertion Sort List.
