# 21. Merge Two Sorted Lists

## Description

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

**Example**:

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

## Solution

### Better

* Time Complexity: O(n)
* Space Complexity: O(1)

* Key 1: If l1 is empty, then connect the rest of l2 to node. If l2 is empty, vice versa.
* Key 2: Use a temporary node as head. Then return the node.next in the end.

### Naive

* Time Complexity: O(n)
* Space Complexity: O(1)

Compare each node in both l1 and l2. If one of them is empty, keep travel to the end of the non-empty one.