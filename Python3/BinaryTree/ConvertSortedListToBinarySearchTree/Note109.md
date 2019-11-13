# 109. Convert Sorted List to Binary Search Tree

## Description

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

**Example**:

```txt
Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
```

## Note

### Binary Search Tree

For a given node of the binary search tree, it's value must be $\geq$ the value of all the nodes in the left subtree and $\leq$ the value of all the nodes in the right subtree

### Hight Balanced Binary Search Tree

The middle element of the given list would form the root of the binary search tree. All the elements to the left of the middle element would form the left subtree recursively. Similarly, all the elements to the right of the middle element will form the right subtree of the binary search tree. This would ensure the height balance required in the resulting binary search tree.

## Solution

### Recursion with Two Pointer

1. Find the middle element with two pointer ($O(N/2)$)
2. Split the list into two linked list
3. Create a tree node with middle element
   1. Build left sub-tree
   2. Build right sub-tree

* Time Complexity: $O(N\log N)$
* Space Complexity: $O(\log N)$

### Recursion with Conversion to Array

To improve the time complexity of finding the middle element.

1. Converse linked list to array (so the access time to the middle element will be $O(1)$)
2. Do the same thing as previous did

* Time Complexity: $O(N)$ - convert the linked list to an array
* Space Complexity: $O(N)$ - the array we construct
