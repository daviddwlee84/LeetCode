from ..ListNodeModule import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            # []
            return head

        dummy_head = ListNode(None, next=head)
        node = head

        temp_pre = dummy_head
        temp_val = head.val
        count = 1
        # [1, 1]
        while node.next:
            # print(temp_pre.val, temp_val)

            if node.next.val == temp_val:
                # Found duplicate
                count += 1
            else:
                if count > 1:
                    # Remove duplicates
                    count = 1
                    temp_pre.next = node.next
                else:
                    # Simply move to next number
                    temp_pre = node

            node = node.next
            temp_val = node.val

        if count > 1:
            # [1, 1]
            temp_pre.next = node.next

        return dummy_head.next
