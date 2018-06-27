# 23. Merge k Sorted Lists

## Description

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

**Example**:

```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

## Solution

* [Official Solution](https://leetcode.com/problems/merge-k-sorted-lists/solution/)
* (N: the total number of nodes; k: the number of linked lists)

* Relative: 021 - Easy - Merge Two Linked List

### Naive - each time merge 2 linked list

(LeetCode: Time Limit Exceeded)

* Time Complexity: O(kN)
    * Almost every selection of node in final linked costs O(k) (k-1 times comparison)
    * There are NN nodes in the final linked list.
* Space Complexity: O(1) - No extra space used (only change the link)

### KMerge - each time merge k linked list

### Divide and Conquer

* Time Complexity: O(Nlogk)
* Space Complexity: O(1)


### Others

#### Heap

```python
import heapq
class Solution:
    # minheap approach. O(XlogX) time, O(X) space
    # where X = K * N. minheap holds elms in every list. 
    # 
    # 1) build minheap with elms from every list 
    # 2) merge lists
    #   A) pop from minheap, grab the min node
    #   B) link previous min to current min
    # 3) return head of merged list
    #
    def mergeKLists(self, lists):
        # iterators through each list
        its = [l for l in lists]
        # sorted by minimum node value. each
        # elm is a tuple (val, list_id)
        min_heap = []
        k = len(lists)
        for list_id in range(k):
            it = lists[list_id]
            while it:
                heapq.heappush(min_heap, (it.val, list_id))
                it = it.next

        sorted_head = None
        sorted_it = sorted_head

        while min_heap:
            # next min elm
            list_id = heapq.heappop(min_heap)[1]
            next_node = its[list_id]
            its[list_id] = its[list_id].next
            # first node in sorted list
            if not sorted_head:
                sorted_head = next_node
            else:
                sorted_it.next = next_node
            sorted_it = next_node
        return sorted_head
```

#### [attrgetter](https://docs.python.org/3/library/operator.html#operator.attrgetter)

```python
class Solution:
    def mergeKLists(self, lists):
        from operator import attrgetter

        sorted_list = []
        for lst in lists:
            while lst is not None:
                sorted_list.append(lst)
                lst = lst.next
        sorted_list = sorted(sorted_list, key = attrgetter('val'))
        dummy  = curr = ListNode(0)
        for node in sorted_list:
            curr.next = curr = node
        return dummy.next
```