# Remove Nth Node From End of List

## Description

Given a linked list, remove the *n*-th node from the end of list and return its head.

**Example**:

```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```

**Note**:

Given n will always be valid.

**Follow up**:

Could you do this in one pass?

## Solution

### Hash Table

Use hash table to store the index for each node. Then we can easily access and delete the node we want.

* Time Complexity: O(n)
* Space Complexity: O(n)
