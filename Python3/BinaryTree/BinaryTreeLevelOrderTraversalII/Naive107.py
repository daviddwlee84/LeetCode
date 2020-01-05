from ..TreeNodeModule import TreeNode
from typing import List
from collections import deque


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        currDepth = -1
        queue = deque([(root, 0)])
        ans = deque([[root.val]])
        while queue:
            node, depth = queue.pop()
            if depth > currDepth and (node.left or node.right):
                ans.appendleft([])
                currDepth = depth

            if node.left:
                queue.appendleft((node.left, depth + 1))
                ans[0].append(node.left.val)
            if node.right:
                queue.appendleft((node.right, depth + 1))
                ans[0].append(node.right.val)

        return list(ans)

# Runtime: 28 ms, faster than 95.52% of Python3 online submissions for Binary Tree Level Order Traversal II.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal II.
