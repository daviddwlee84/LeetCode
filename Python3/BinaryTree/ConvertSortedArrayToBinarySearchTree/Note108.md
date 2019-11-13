# 108. Convert Sorted Array to Binary Search Tree

## Description

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

**Example**:

```txt
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
```

## Note

[Shared contents link](../ConvertSortedListToBinarySearchTree/Note109.md#Note)

## Solution

### Recursive

1. Find middle element
2. Build the tree of left half array and right half
