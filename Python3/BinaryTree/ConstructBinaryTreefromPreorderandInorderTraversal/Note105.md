# 105. Construct Binary Tree from Preorder and Inorder Traversal

## Description

Given preorder and inorder traversal of a tree, construct the binary tree.

**Note**:
You may assume that duplicates do not exist in the tree.

For example, given
```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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

Postorder => [ROOT, leftsubtree, rightsubtree]
                  \
                   \
                    \
                     \
                      \
                       \
                        \
Inorder => [LEFTSUBTREE, root, RIGHTSUBTREE]

You can use list.index(root.val) to find the position in Inorder list.
Or you can use an hash table to record each value's position