# 257. Binary Tree Paths

## Description

Given a binary tree, return all root-to-leaf paths.

**Note**: A leaf is a node with no children.

**Example**:

```
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```

## Solution

### Iterative

Travel binary tree and add current stack into path if reach leaf node.

### Recursive String

* Pass current path as string to next visit.
* Find path for left and right child.
* When reach leaf append path sring to answer.
