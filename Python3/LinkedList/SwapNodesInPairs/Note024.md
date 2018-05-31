# 24. Swap Nodes in Pairs

## Description

Given a linked list, swap every two adjacent nodes and return its head.

**Example**:

```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```

**Note**:

* Your algorithm should use only constant extra space.
* You may not modify the values in the list's nodes, only nodes itself may be changed.

## Solution

### Naive

* Time Complexity: O(n)

1. Check if node can swap
2. Swap every two node (use swap helper function)
3. Link the last node to the latest swapped two node

### Recursive

* Time Complexity: O(n)