# 98. Validate Binary Search Tree

## Description

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

* The left subtree of a node contains only nodes with keys less than the node's key.
* The right subtree of a node contains only nodes with keys greater than the node's key.
* Both the left and right subtrees must also be binary search trees.

**Example 1**:

```
Input:
    2
   / \
  1   3
Output: true
```

**Example 2**:

```
    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
```

## Solution

### Inorder Traversal

* Time Complexity: O(n) - traversal
* Space Complexity: O(n) - an array to store the traversal result and call back stack

Use inorder traversal (i.e. DFS) to travel all the node in order. And then check if it's acending.

### DFS

* Time Complexity: O(n) - visit every node
* Space Complexity: O(n) - call back stack

Use a helper function with two extra input for minimum and maximum. Check if current node is in the range. Then search if the left subtree is in minimum~node.val and right subtree is in node.val~maximum.