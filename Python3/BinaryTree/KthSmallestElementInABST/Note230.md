# 230. Kth Smallest Element in a BST

## Description

Given a binary search tree, write a function `kthSmallest` to find the **k**th smallest element in it.

**Note**:

You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

**Example 1**:

```txt
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```

**Example 2**:

```txt
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```

**Follow up**:

What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

## Note

* [Official Solution](https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/)

Tree Traversal

![traversal](https://leetcode.com/problems/kth-smallest-element-in-a-bst/Figures/230/bfs_dfs.png)

## Solution

## Others' Solution

### Recursive Inorder Traversal

```py
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]
```
