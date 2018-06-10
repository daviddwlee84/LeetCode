# 236. Lowest Common Ancestor of a Binary Tree

## Description

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”

Given the following binary search tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

```
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
```

**Example 1**:

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
```

**Example 2**:

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
```

**Note**:

* All of the nodes' values will be unique.
* p and q are different and both values will exist in the binary tree.


## Solution

## Naive

The last number of overlapping part of path from root to p and q is LCA

* Time complexity: O(n): find path and compare path

**Get path from root to a given node**:

1. Preorder Traversal aka. Depth-first Search
    * If you implement preorder traversal recursively, then when you reach the desired node, you can unwind your stack (of recursive calls) and construct your path in reverse.
    * If you implement the preorder traversal non-recursively, then you will be building a stack directly, so in this case once you reach your desired node you have your path already.
2. Recursively check if current node is what we want or the descendant has the node. If so, add to the path. (reverse the path or insert node in front of the array)