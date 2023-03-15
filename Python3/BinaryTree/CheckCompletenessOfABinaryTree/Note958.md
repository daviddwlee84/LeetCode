# 958. Check Completeness of a Binary Tree

## Description

## Fail

> `[1,2,3,5,null,7,8] False`

```py
from typing import Optional
from ..TreeNodeModule import TreeNode
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, 0)])
        
        while queue:
            node, depth = queue.pop()
            if node.right and not node.left:
                return False
            
            if node.left:
                queue.appendleft((node.left, depth + 1))
            if node.right:
                queue.appendleft((node.right, depth + 1))
        
        return True

# [1,2,3,5,null,7,8] False
```
