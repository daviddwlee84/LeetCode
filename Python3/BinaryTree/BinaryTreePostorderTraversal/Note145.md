# 145. Binary Tree Postorder Traversal

## Description

Given a binary tree, return the postorder traversal of its nodes' values.

**Example**:

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
```

**Follow up**: Recursive solution is trivial, could you do it iteratively?

## Solution

### Recursive


### Iterative

1. push root into stack
2. while stack isn't empty
    1. pop node and insert into front of answer stack
    2. push left child and right child into stack
