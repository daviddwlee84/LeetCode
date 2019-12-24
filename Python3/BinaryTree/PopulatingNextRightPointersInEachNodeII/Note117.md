# 117. Populating Next Right Pointers in Each Node II

## Description

Given a binary tree

```txt
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

**Follow up**:

* You may only use constant extra space.
* Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

**Example 1**:

```txt
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

**Constraints**:

* The number of nodes in the given tree is less than `6000`.
* `-100 <= node.val <= 100`

## Solution

### DFS

* Maintain three pointer
  * parent: iterate through horizontally, find next parents' child to connect
  * childHead: replace current parent when reach next level
  * child: iterate through horizontally, connect next possible child

## Others' Solution

### Queue

```py
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = [root]
        while queue:
            length = len(queue)
            for i in range(length):
                cur_node = queue.pop(0)
                if i == length - 1:
                    cur_node.next = None
                else:
                    cur_node.next = queue[0]
                if cur_node.left: queue.append(cur_node.left)
                if cur_node.right: queue.append(cur_node.right)
        return root
```
