from typing import List, Optional, Callable
from ..ListNodeModule import ListNode
import heapq


class HeapWrapper(object):
    def __init__(self, initial: List[Optional[ListNode]] = [], key: Callable[[Optional[ListNode]], int] = lambda x: x.val) -> None:
        self.key = key
        self._data = [(self.key(item), i, item)
                      for i, item in enumerate(initial) if item]
        # The index is use to make each tuple unique, so heapq won't have to compare the "ListNode"
        # TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
        self._index = len(self._data)
        heapq.heapify(self._data)

    def __len__(self):
        return len(self._data)

    def push(self, item: ListNode):
        self._index += 1 # Make sure the index is unique
        heapq.heappush(self._data, (self.key(item), self._index, item))

    def pop(self):
        return heapq.heappop(self._data)[2]


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate
        https://leetcode.com/problems/merge-k-sorted-lists/solutions/3287717/merge-k-sorted-linked-lists-in-o-n-log-k-time-with-priority-queue-full-explanation/
        """

        heap = HeapWrapper(lists)
        node = dummy_head = ListNode(None)
        while heap:
            node.next = heap.pop()
            node = node.next

            if node.next:
                heap.push(node.next)

        return dummy_head.next


if __name__ == '__main__':
    heap = HeapWrapper([ListNode(num) for num in (1, 2, 3, 4, 5, 6)])
    heap.push(ListNode(7))
    print(len(heap))
    print(heap.pop().val)
    print(bool(heap))
    print(bool(HeapWrapper()))  # Empty is false
