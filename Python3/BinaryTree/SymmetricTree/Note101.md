# Symmetric Tree

## Description

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree `[1,2,2,3,4,4,3]` is symmetric:

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

But the following `[1,2,2,null,3,null,3]` is not:

```
    1
   / \
  2   2
   \   \
   3    3
```

**Note**:

Bonus points if you could solve it both recursively and iteratively.

## Solution

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