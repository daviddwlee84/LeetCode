# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = deque([(root, 0)])
        curr_level = -1
        level_order = []

        while queue:
            node, depth = queue.pop()
            if depth > curr_level:
                # print(level_order, depth - 1)
                if (depth - 1) % 2 == 0:
                    # even
                    if level_order and level_order[0] % 2 == 0:
                        return False
                    for i in range(1, len(level_order)):
                        if level_order[i - 1] >= level_order[i]:
                            return False
                        if level_order[i] % 2 == 0:
                            return False
                else:
                    # odd
                    if level_order and level_order[0] % 2 != 0:
                        return False
                    for i in range(1, len(level_order)):
                        if level_order[i - 1] <= level_order[i]:
                            return False
                        if level_order[i] % 2 != 0:
                            return False

                curr_level = depth
                level_order = [node.val]

            else:
                level_order.append(node.val)

            if node.left:
                queue.appendleft((node.left, depth + 1))
            if node.right:
                queue.appendleft((node.right, depth + 1))

        # print(level_order, depth)
        if depth % 2 == 0:
            # even
            if level_order and level_order[0] % 2 == 0:
                return False
            for i in range(1, len(level_order)):
                if level_order[i - 1] >= level_order[i]:
                    return False
                if level_order[i] % 2 == 0:
                    return False
        else:
            # odd
            if level_order and level_order[0] % 2 != 0:
                return False
            for i in range(1, len(level_order)):
                if level_order[i - 1] <= level_order[i]:
                    return False
                if level_order[i] % 2 != 0:
                    return False
        return True
