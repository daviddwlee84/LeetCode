# 102. Binary Tree Level Order Traversal

## Description

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its level order traversal as:

```
[
  [3],
  [9,20],
  [15,7]
]
```

## Solution

### BFS

* Time Complexity: O(n)

BFS => Queue

1. Put root into queue
2. Do while queue is not empty
    1. Get one number out of queue and add it into current level ans (and current level number - 1)
    2. Put left and right child into queue if there is one (and next level number + 1)
    3. Check if current level node is empty and queue is not empty
        1. go to next level (next level number => current level number, level + 1)