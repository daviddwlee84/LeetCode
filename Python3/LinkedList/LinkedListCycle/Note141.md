# 141. Linked List Cycle

## Description

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (0-indexed) in the linked list where tail connects to. If `pos` is -1, then there is no cycle in the linked list.

**Example 1**:

```txt
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

![ex1](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**Example 2**:

```txt
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

![ex2](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Example 3**:

```txt
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

![ex3](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

**Follow up**:

Can you solve it using O(1) (i.e. constant) memory?

## Solution

### Naive - Hash Table

* store all visited node
* if revisit => cycle exist

### Improved (use O(1) memory) - Two Pointers

* Use a "slow" and a "fast" pointer
* If the fast reach the end => no cycle
* If they bump into each other => there is cycle
  * Consider, will they always bump into each other?
