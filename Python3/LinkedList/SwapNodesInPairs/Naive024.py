from ..ListNodeModule import ListNode, printListNode, listNodeConverter

# Debug
# import sys, os
# sys.path.append(os.getcwd() + '/Python3/LinkedList')
# from ListNodeModule import ListNode, printListNode, listNodeConverter

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Don't need to swap
        if not head or not head.next:
            return head
    
        ptr = head
        head = self.swapHelper(ptr, ptr.next)
        lastTemp = ptr
        ptr = ptr.next
        
        while ptr and ptr.next:
            lastTemp.next = self.swapHelper(ptr, ptr.next)
            lastTemp = ptr
            ptr = ptr.next

        return head
        
    # Swap two nodes and return its new first node's address
    def swapHelper(self, ori_first, ori_second):
        linkto = ori_second.next
        ori_first.next = linkto
        ori_second.next = ori_first
        return ori_second

def main():
    printListNode(Solution().swapPairs(listNodeConverter([])))
    printListNode(Solution().swapPairs(listNodeConverter([1,2,3,4])))
    printListNode(Solution().swapPairs(listNodeConverter([1,2,3,4,5])))
    printListNode(Solution().swapPairs(listNodeConverter([1,2,3,4,5,6])))

if __name__ == '__main__':
    main()