# 662. Maximum Width of Binary Tree

## Description

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a **full binary tree**, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the `null` nodes between the end-nodes are also counted into the length calculation.

**Example 1**:

```txt
Input:

           1
         /   \
        3     2
       / \     \  
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
```

**Example 2**:

```txt
Input:

          1
         /  
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
```

**Example 3**:

```txt
Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
```

**Example 4**:

```txt
Input:

          1
         / \
        3   2
       /     \  
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
```

**Note**: Answer will in the range of 32-bit signed integer.

## Solution

## Others' Solution

* [Python... - LeetCode Discuss](https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/106650/Python...)
* [Python, Straightforward BFS and DFS solutions - LeetCode Discuss](https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/106707/Python-Straightforward-BFS-and-DFS-solutions)
* [[Java/C++] Very simple dfs solution - LeetCode Discuss](https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/106654/JavaC%2B%2B-Very-simple-dfs-solution)

---

Fail: didn't consider empty middle node

```py
from ..TreeNodeModule import TreeNode
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # count of element
        layers = []

        queue = deque([(root, 0)])
        cur_layer = -1
        while queue:
            node, depth = queue.pop()
            if depth > cur_layer:
                layers.append([])

            cur_layer = depth

            if node:
                # N for number
                layers[depth].append('N')
            else:
                # E for empty
                layers[depth].append('E')
                continue

            queue.appendleft((node.left, depth + 1))
            queue.appendleft((node.right, depth + 1))

        max_width = 0
        for i, layer in enumerate(reversed(layers)):
            if 2 ** (len(layers) - i - 1) < max_width:
                # early stop
                break

            if 'N' in layer:
                first_idx = layer.index('N')
                # https://stackoverflow.com/questions/522372/finding-first-and-last-index-of-some-value-in-a-list-in-python
                last_idx = len(layer) - layer[::-1].index('N') - 1
                max_width = max(max_width, last_idx - first_idx + 1)

        return max_width
```

Fail: wrong width calculation

```py
from ..TreeNodeModule import TreeNode
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # count of element
        layers = []

        queue = deque([(root, 0, 0)])
        cur_layer = -1
        while queue:
            node, depth, shift = queue.pop()
            if depth > cur_layer:
                layers.append({'min': float('inf'), 'max': float('-inf')})

            cur_layer = depth

            layers[depth]['min'] = min(layers[depth]['min'], shift)
            layers[depth]['max'] = max(layers[depth]['max'], shift)

            if node.left:
                queue.appendleft((node.left, depth + 1, shift - 1))
            if node.right:
                queue.appendleft((node.right, depth + 1, shift + 1))

        print(layers)

        max_width = 0
        for i, layer in enumerate(reversed(layers)):
            if 2 ** (len(layers) - i - 1) < max_width:
                # early stop
                break

            max_width = max(max_width, layer['max'] - layer['min'])

        return max_width
```

Fail: just store the temp code

```py
from ..TreeNodeModule import TreeNode
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # count of element
        layers = []

        queue = deque([(root, 0, [])])
        cur_layer = -1
        while queue:
            node, depth, path = queue.pop()
            if depth > cur_layer:
                layers.append({'min': float('inf'), 'max': float('-inf')})

            cur_layer = depth

            layers[depth]['min'] = min(layers[depth]['min'], shift)
            layers[depth]['max'] = max(layers[depth]['max'], shift)

            if node.left:
                queue.appendleft((node.left, depth + 1, shift - 1))
            if node.right:
                queue.appendleft((node.right, depth + 1, shift + 1))

        print(layers)

        max_width = 0
        for i, layer in enumerate(reversed(layers)):
            if 2 ** (len(layers) - i - 1) < max_width:
                # early stop
                break

            max_width = max(max_width, layer['max'] - layer['min'])

        return max_width
```
