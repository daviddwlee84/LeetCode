# 106. Construct Binary Tree from Inorder and Postorder Traversal

## Description

Given inorder and postorder traversal of a tree, construct the binary tree.

**Note**:
You may assume that duplicates do not exist in the tree.

For example, given

```
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```

Return the following binary tree:

```
    3
   / \
  9  20
    /  \
   15   7
```

## Solution

### Divide and Conquer

Key point

* The last node of postorder is root
* Parent node in inorder seperate left and right subtree

1. pop the last node of postorder as root (Construct a TreeNode)
2. seperate left and right subtree in inorder list
3. recursively build left and right subtree