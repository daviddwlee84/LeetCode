# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from ..TreeNodeModule import TreeNode
from typing import List


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        next_level = [root]
        answer = []
        level = 0

        while next_level:
            # start new level
            next_level_temp = []
            answer.append([])
            # for each node in this level
            for i in range(len(next_level)):
                node = next_level.pop()
                # answer[level].append(node.val)
                answer[-1].append(node.val)

                # push next level node in order, left to right or right to left
                if level % 2 == 0:
                    if node.left:
                        next_level_temp.append(node.left)
                    if node.right:
                        next_level_temp.append(node.right)
                else:
                    if node.right:
                        next_level_temp.append(node.right)
                    if node.left:
                        next_level_temp.append(node.left)

            level += 1
            next_level = next_level_temp

        return answer
