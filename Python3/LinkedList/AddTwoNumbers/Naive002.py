from ..ListNodeModule import ListNode, listNodeConverter, printListNode

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode(0)
        l3 = head
        carry = 0
        while(True):
            temp = l1.val + l2.val + carry

            ## other solution:
            # carry = temp/10
            # l3.val = temp%10

            if temp > 9:
                l3.val = temp - 10
                carry = 1
            else:
                l3.val = temp
                carry = 0

            if(carry == 0 and l1.next == None and l2.next == None):
                break
            else:
                l3.next = ListNode(0)
                l3 = l3.next

            if(l1.next == None):
                l1.val = 0
            else:
                l1 = l1.next
            if(l2.next == None):
                l2.val = 0
            else:
                l2 = l2.next

        return head

def main():
    l1 = listNodeConverter([2, 4, 3])
    l2 = listNodeConverter([5, 6, 4])
    printListNode(l1)
    printListNode(l2)
    printListNode(Solution().addTwoNumbers(l1, l2))

    l1 = listNodeConverter([1, 8])
    l2 = listNodeConverter([0])
    printListNode(l1)
    printListNode(l2)
    printListNode(Solution().addTwoNumbers(l1, l2))

if __name__ == "__main__":
    main()