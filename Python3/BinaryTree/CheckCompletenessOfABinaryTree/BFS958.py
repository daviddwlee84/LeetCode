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
        """
        Check no continuous null

        https://leetcode.com/problems/check-completeness-of-a-binary-tree/solutions/3298591/python-java-c-easy-video-explanation/
        https://leetcode.com/problems/check-completeness-of-a-binary-tree/solutions/3298282/image-explanation-dfs-bfs-solution-complete-intuition/

        https://leetcode.com/problems/check-completeness-of-a-binary-tree/solutions/3298346/clean-codes-full-explanation-b-f-s-c-java-python3/
        """
        queue = deque([root])
        
        seen_null = False

        while queue:
            node = queue.pop()

            if node is None:
                seen_null = True
                continue
            
            if seen_null:
                return False
            
            queue.appendleft(node.left)
            queue.appendleft(node.right)
        
        return True
