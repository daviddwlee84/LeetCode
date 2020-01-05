# 114. Flatten Binary Tree to Linked List

## Description

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

```txt
    1
   / \
  2   5
 / \   \
3   4   6
```

The flattened tree should look like:

```txt
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

## Solution

### Naive

1. Pre-order traverse the entire tree, store in a list
2. Reconstruct the tree using this list...

## Others' Solution

[Recursive Python beats 98% - LeetCode Discuss](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/465146/Recursive-Python-beats-98)

```py
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        #flattens subtree and returns bottom node
        def helper(node):
            left_bot = node
            right = node.right
            if node.left:
                left_bot = helper(node.left)
                node.right = node.left
                left_bot.right = right
                node.left = None
            if right:
                right_bot = helper(right)
                return right_bot
            else:
                return left_bot

        if not root:
            return root

        helper(root)
```
