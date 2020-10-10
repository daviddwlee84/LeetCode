# 297. Serialize and Deserialize Binary Tree

## Description

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Example**:

```txt
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
```

**Clarification**: The above format is the same as [how LeetCode serializes a binary tree](https://leetcode.com/faq/#binary-tree). You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

> * [What does [1,null,2,3] mean in binary tree representation? – Help Center](https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation-)
> * [Tree Deserializer and Visualizer for Python - LeetCode Discuss](https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python)

**Note**: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

## Solution

## Others' Solution

* [Recursive preorder, Python and C++, O(n) - LeetCode Discuss](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74259/Recursive-preorder-Python-and-C%2B%2B-O%28n%29)

### Pre-order

```py
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def preorder(root):
            if not root:
                return None
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ' '.join(map(str, res))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        inputs = data.split()
        inputs = list(map(int, inputs))
        def build(minv, maxv):
            if inputs and minv < inputs[0] < maxv:
                v = inputs.pop(0)
                root = TreeNode(v)
                root.left = build(minv, v)
                root.right = build(v, maxv)
                return root

        node = build(float('-inf'), float('inf'))
        return node
```

```py
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)
        return ' '.join(map(str, vals))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = deque(int(val) for val in data.split())
        def build(min_val, max_val):
            if vals and min_val < vals[0] < max_val:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(min_val, val)
                node.right = build(val, max_val)
                return node

        return build(float('-inf'), float('inf'))
```

```py
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # pre-order traverse
        if root == None:
            return ""
        return "->".join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        s = collections.deque(data.split("->"))

        def helper(datalist: collections.deque()) -> TreeNode:
            val = datalist.popleft()
            if val == "":
                return None
            root = TreeNode(int(val), None, None)
            root.left = helper(datalist)
            root.right = helper(datalist)
            return root

        return helper(s)
```
