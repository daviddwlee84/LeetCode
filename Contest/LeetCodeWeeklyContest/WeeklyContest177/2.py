from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = [None] * n
        for i in range(n):
            if leftChild[i] != -1:
                if parents[leftChild[i]] is None:
                    parents[leftChild[i]] = i
                else:
                    # If one node has two parent, then it can't be tree
                    return False

            if rightChild[i] != -1:
                if parents[rightChild[i]] is None:
                    parents[rightChild[i]] = i
                else:
                    # If one node has two parent, then it can't be tree
                    return False

        # Check if only single root
        cntNone = 0
        for parent in parents:
            if parent is None:
                cntNone += 1

        if cntNone != 1:
            return False
        return True
