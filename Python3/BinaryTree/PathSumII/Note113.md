# 113. Path Sum II

## Description

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

**Note**: A leaf is a node with no children.

**Example**:

Given the below binary tree and `sum = 22`,

```txt
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
```

Return:

```txt
[
   [5,4,11,2],
   [5,8,4,5]
]
```

## Solution

### DFS + Backtracking
