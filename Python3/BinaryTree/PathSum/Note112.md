# 112. Path Sum

## Description

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

**Note**: A leaf is a node with no children.

**Example**:

Given the below binary tree and `sum = 22`,

```txt
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
```

return true, as there exist a root-to-leaf path `5->4->11->2` which sum is 22.

## Solution

### Naive Recursive

1. Pass current sum to the next level
2. When reach a leaf append an answer in list
3. After every traversal check if sum is in the list

Possible improvement:

* Once find an answer then return true and end the search
* When the path sum is larger than expect sum then stop searching that path

### Others' Solution

Instead of sum up the sum, it minus the sum.

```python
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and root.val==sum:
            return True
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
```
