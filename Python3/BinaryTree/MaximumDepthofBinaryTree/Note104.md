# 104. Maximum Depth of Binary Tree

## Description

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Note**: A leaf is a node with no children.

**Example**:

Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its depth = 3.

## Solution

### Top-down Solution

Method 1

1. Pass current depth + 1 to left and right subtree
2. return the maximum of left and right subtree

Method 2

1. Pass current depth + 1 to left and right subtree
2. when reach the end of leaf update the maximum of depth

### Bottom-up Solution

1. Return 0 when reach the end (node is None)
2. Return 1 + maximum depth of left and right child