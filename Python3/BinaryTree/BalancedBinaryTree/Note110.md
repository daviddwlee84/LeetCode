# 110. Balanced Binary Tree

## Description

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

> a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

**Example 1**:

Given the following tree `[3,9,20,null,null,15,7]`:

```txt
    3
   / \
  9  20
    /  \
   15   7
```

Return true.

**Example 2**:

Given the following tree `[1,2,2,3,3,null,null,4,4]`:

```txt
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
```

Return false.

## Solution

### DFS

* check if current tree is balanced
* check its left and right subtree is balanced
* get depth recursively

## Others' Solution

```py
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        val = self.checkHeight(root)
        return val != -1

    def checkHeight(self, root):
        if not root:
            return 0

        leftHeight, rightHeight = self.checkHeight(root.left), self.checkHeight(root.right)
        if leftHeight == -1 or rightHeight == -1:
            return -1
        elif abs(leftHeight - rightHeight) > 1:
            return -1
        else:
            return 1 + max(leftHeight, rightHeight)
```
