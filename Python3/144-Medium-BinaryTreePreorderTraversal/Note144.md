# 144. Binary Tree Preorder Traversal

## Descripton

Given a binary tree, return the *preorder* traversal of its nodes' values.

**Example**:

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
```

**Follow up**: Recursive solution is trivial, could you do it iteratively?


## Solution

### Recursive


### Iterative

* Stack

1. Push root into stack
2. do while stack is not empty
3. Pop the stack and add to result
4. Push right node into stack if there is one (Because stack is LIFO)
5. Push left node into stack if there is one
6. repeat 2-5