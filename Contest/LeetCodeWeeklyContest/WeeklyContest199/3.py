from itertools import combinations

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.leaves = []

        self.dfs(root, [], 0)

        count = 0

        for (leaf_a, leaf_a_parents, leaf_a_depth), (leaf_b, leaf_b_parents, leaf_b_depth) in combinations(self.leaves, 2):
            i = 0
            j = 0
            a_len = len(leaf_a_parents)
            b_len = len(leaf_b_parents)
            while i < a_len and j < b_len:
                if leaf_a_depth - leaf_a_parents[a_len - i - 1][1] + leaf_b_depth - leaf_b_parents[b_len - j - 1][1] > distance:
                    # early stop
                    break

                if leaf_a_parents[a_len - i - 1][1] == leaf_b_parents[b_len - j - 1][1]:
                    # same depth
                    if leaf_a_parents[a_len - i - 1][0] == leaf_b_parents[b_len - j - 1][0]:
                        # same node
                        # print(leaf_a_depth, leaf_b_depth,
                        #       leaf_a_parents[a_len - i - 1][1])
                        # print(leaf_a_depth - leaf_a_parents[a_len - i - 1]
                        #       [1] + leaf_b_depth - leaf_a_parents[a_len - i - 1][1])
                        if leaf_a_depth - leaf_a_parents[a_len - i - 1][1] + leaf_b_depth - leaf_a_parents[a_len - i - 1][1] <= distance:
                            count += 1
                        break
                    i += 1
                    j += 1
                elif leaf_a_parents[a_len - i - 1][1] < leaf_b_parents[b_len - j - 1][1]:
                    j += 1
                else:
                    i += 1

        return count

    def dfs(self, node: TreeNode, parents: list, depth: int):
        if not node.left and not node.right:
            self.leaves.append([node, parents, depth])
            return

        if node.left:
            self.dfs(node.left, parents + [[node, depth]], depth + 1)
        if node.right:
            self.dfs(node.right, parents + [[node, depth]], depth + 1)

# TLE (when without early stop)
# [70,76,43,24,1,7,85,null,33,14,10,38,33,23,41,96,27,49,16,50,99,null,74,41,41,18,79,9,11,null,null,74,22,null,null,89,71,96,71,34,49,null,19,null,53,95,18,null,2,43,72,53,20,75,13,null,null,45,17,null,null,null,92,null,null,6,67,null,8,94,19,97,18,null,84,null,90,62,69,80,42,null,61,52,11,null,98,88,3,71,85,75,15,null,null,null,45,42,33,null,null,null,42,null,7,25,97,22,15,null,null,null,82,null,7,null,31,null,81,null,88,null,83,null,54,null,83,94,4,90,84,null,36,null,93,24,57,4,67,96,43,83,49,83,6,null,null,null,null,null,null,null,33,null,81,null,3,null,32,97,4,40,53,30,null,11,78,null,78,null,30,8,76,null,75,null,82,71,66,null,null,null,58,null,29,44,68,null,38,7,71,62,56,35,93,null,null,null,55,null,97,29,100,null,68,13,93,11,30,100,28,80,30,null,null,null,null,null,65,null,null,23,9,75,9,87,43,null,null,null,null,23,33,null,15,null,68,null,23,12,67,null,null,97,20,null,null,null,98,null,1,null,null,null,66,5,2,null,14,null,null,40,92,null,null,null,80,null,53,65,88,null,81,null,null,92,60,3,49,92,20,null,10,63,75,null,85,14,83,8,82,52,34,null,null,null,32,38,null,null,null,null,92,null,null,null,82,null,null,31,57,null,null,null,null,null,41,null,null,25,25,null,54,43,11,null,null,null,39,null,28,null,72,null,47,null,30,52,27,null,47,null,null,null,11,null,76,null,90,null,70,null,73,null,null,null,null,null,60,null,23,36,78,null,23,null,85,75,92,null,41,75,94,null,47,50,95,53,68,null,22,76,38,56,71,45,49,null,70,null,null,null,null,null,62,null,2,9,40,null,null,null,null,null,null,null,85,null,21,90,71,null,null,null,null,null,null,null,49,null,90,null,67,58,93,null,null,null,32,null,31,null,7,null,null,27,5,null,51,89,42,39,44,60,63,null,null,null,null,null,null,null,null,null,46,23,13,71,88,null,36,null,null,null,20,null,80,2,79,null,38,null,78,66,34,null,null,69,76,59,60,33,52,null,null,null,null,null,4,null,40,83,12,null,null,null,34,null,84,3,48,null,null,null,null,null,null,null,98,33,5,null,16,null,null,null,null,null,27,20,3,null,77,null,null,null,null,null,null,null,45,null,24,88,77,22,null,null,null,null,2,94,81,1,23,null,null,null,98,null,null,null,null,null,23,null,61,33,9,91,41,7,1,85,75,null,16,null,57,11,44,65,4,71,95,null,74,null,84,null,null,99,25,34,null,null,null,null,null,54,42,null,34,null,null,null,18,null,null,null,17,null,null,20,75,null,null,null,null,null,19,null,64,77,47,null,null,null,17,null,null,null,27,null,75,81,2,null,79,16,97,null,1,null,null,null,null,null,null,null,null,20,43,null,59,null,null,null,73,98,47,null,null,null,null,56,72,null,47,65,19,98,76,64,60,null,null,null,null,null,null,29,56,null,null,null,44,null,45,44,13,2,99,null,48,null,80,32,54,null,null,null,35,null,2,10,83,null,null,null,null,null,null,null,10,62,92,null,null,99,43,66,100,null,null,null,null,null,21,null,29,null,null,28,76,36,6,null,49,86,68,null,35,null,88,75,60,72,52,62,75,9,96,76,64,null,null,null,77,null,null,46,57,null,null,null,null,null,null,30,46,null,80,null,null,null,34,46,68,null,null,null,null,null,24,50,58,null,null,null,29,22,6,30,null,null,null,71,51,26,47,null,null,50,30,null,null,null,16,null,null,78,32,null,null,null,null,71,66,null,57,null,null,null,null,82,69,null,null,null,61,70,40,56,14,null,80,33,78,80,50,86,100,null,27,null,null,null,23,null,null,74,77,null,null,null,11,null,null,null,31,null,null,null,61,16,81,null,81,null,46,22,75,null,null,null,null,null,null,null,null,7,48,null,null,null,34,null,9,null,20,null,8,null,96,23,87,null,8,null,44,27,49,null,null,null,null,null,null,null,37,36,47,null,null,null,null,44,70,null,null,63,85,81,49,57,66,null,74,21,12,null,null,92,42,null,null,null,3,null,null,null,null,null,98,null,null,null,null,null,null,40,49,null,null,53,31,null,49,null,null,null,null,48,19,null,95,null,null,null,4,null,null,null,null,null,36,30,63,null,null,null,21,7,19,null,null,40,35,21,58,7,6,null,null,53,90,51,49,78,10,88,9,null,50,null,58,null,null,null,68,27,70,98,86,null,79,null,50,null,null,93,70,33,38,null,null,null,99,null,50,34,24,null,null,null,50,94,56,77,34,null,null,60,66,76,7,72,85,null,null,null,77,null,70,null,21,null,10,22,45,null,94,85,66,null,56,23,15,null,null,null,null,null,null,null,42,null,67,null,98,47,64,null,35,null,92,null,56,null,44,null,null,null,35,null,31,null,66,54,13,null,null,null,47,null,62,null,17,null,null,null,34,null,null,null,null,42,null,null,46,null,null,null,null,13,null,98,89,null,null,null,null,56,37,null,null,null,18,43,68,null,null,null,null,5,53,41,96,97,14,65,5,null,98,null,26,null,null,null,null,29,62,null,null,46,28,null,null,null,48,null,66,null,null,1,60,null,null,5,51,null,null,null,null,24,null,41,13,null,null,null,28,null,null,null,null,null,90,null,null,null,22,null,null,49,null,19,63,null,94,81,90,null,33,78,48,null,49,null,70,66,95,48,78,null,69,null,85,null,null,9,83,null,null,null,55,94,28,null,64,null,79,null,12,null,null,null,77,null,null,null,null,null,null,87,64,61,29,null,19,null,null,null,23,null,56,null,null,null,null,null,53,null,null,null,null,null,50,null,null,98,70,null,66,2,81,75,43,43,48,null,null,null,68,null,null,null,62,27,28,null,98,52,71,null,23,null,null,8,92,null,69,null,null,null,89,null,10,87,86,null,88,null,null,null,91,19,99,22,36,null,null,null,99,null,null,null,null,null,49,null,null,null,97,null,9,90,95,100,3,null,33,null,null,null,null,null,null,null,null,null,34,null,31,null,null,null,45,null,49,79,10,null,4,null,91,73,79,null,22,null,87,null,null,null,80,null,null,37,40,21,59,null,32,null,59,null,98,18,54,25,58,null,null,null,null,17,54,null,null,null,19,null,64,null,null,null,null,null,5,null,null,null,null,null,null,null,76,null,19,null,51,5,76,null,null,23,98,null,null,null,45,null,34,65,null,null,null,null,null,null,75,62,7,50,19,null,null,null,null,null,null,null,null,null,68,null,8,null,50,null,77,null,44,96,79,null,null,null,null,null,63,43,37,null,null,null,4,87,null,null,79,null,57,29,31,53,64,null,90,null,60,null,99,null,null,91,null,null,34,null,1,null,null,null,6,null,21,null,null,null,14,null,null,null,6,39,59,null,null,null,null,69,68,null,88,null,60,null,null,null,46,null,null,null,81,null,9,null,69,92,83,null,51,22,44,null,null,null,null,null,19,null,null,92,72,null,16,null,29,null,null,null,null,null,35,14,84,null,75,100,45,null,null,null,null,null,24,null,null,null,57,null,null,null,null,null,68,null,71,83,56,2,13,null,null,null,16,null,18,null,null,null,22,null,4,44,7,24,39,null,null,23,53,null,null,null,74,null,null,57,55,87,45,9,24,null,null,null,null,null,47,null,null,null,80,null,null,null,null,null,59,45,82,null,null,null,null,null,null,89,49,95,18,null,null,null,37,4,null,89,39,null,82,null,null,null,null,44,61,null,null,null,57,29,64,null,null,null,null,10,52,null,null,2,45,null,75,null,44,null,12,null,55]
# 2
