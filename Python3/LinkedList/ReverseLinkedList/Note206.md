# 206. Reverse Linked List

## Description

Reverse a singly linked list.

**Example**:

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

**Follow up**:

A linked list can be reversed either iteratively or recursively. Could you implement both?

## Solution

### Iterative

* Time Complexity: O(n) - Travel all the node in linked list
* Space Complexity: O(1) - Two variabel to keep last and next node

### Recursive

* Time Complexity: O(n) - Travel all the node in linked list
* Space Complexity: O(n) - Call back stack

1. Use a helper function to connect last node with current, and recursively call for the next one
2. When reach the end, update the head node with the last node

### Brute Force

* Travel each node in sequence and store it in an array.
* Construct another linked list with the reverse of the array.