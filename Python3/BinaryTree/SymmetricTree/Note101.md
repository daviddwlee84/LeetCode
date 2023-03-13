# Symmetric Tree

## Description

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree `[1,2,2,3,4,4,3]` is symmetric:

```txt
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

But the following `[1,2,2,null,3,null,3]` is not:

```txt
    1
   / \
  2   2
   \   \
   3    3
```

**Note**:

Bonus points if you could solve it both recursively and iteratively.

## Solution

> Basically traverse the left and right sub-tree at the same time

### Recursive

1. Return True if it's empty
2. Check if leftnode value is equal to rightnode value
3. If both leftnode child and rightnode child are empty return True
4. If only one child is empty return False
5. Compare leftnode's left child with rightnode's right child AND leftnode's right child with rightnode's leftchild

### Iterative

Both do preorder traversal, but in different way
Left subtree visit left child first, and right subtree visit right child first
Compare the value of leftNode and rightNode each time

## Wrong Answer

Can't capture structure difference (e.g. `[1,2,2,2,null,2]`)

> 195 / 199 testcases passed

```txt
    1
   / \
  2   2
 /   /
2   2
```

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.left_inorder = []
        self.right_inorder = []
        
        def inorder(node: Optional[TreeNode], left_first: bool):
            if not node:
                return
            
            if left_first:
                inorder(node.left, left_first)
                self.left_inorder.append(node.val)
                inorder(node.right, left_first)
            else:
                inorder(node.right, left_first)
                self.right_inorder.append(node.val)
                inorder(node.left, left_first)
        
        inorder(root.left, True)
        inorder(root.right, False)
        
        return self.left_inorder == self.right_inorder
```
