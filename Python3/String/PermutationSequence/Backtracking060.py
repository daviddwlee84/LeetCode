from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.all_permutation = []
        self.getAllPermutation([], [str(i) for i in range(1, n+1)])
        return ''.join(self.all_permutation[k - 1])

    def getAllPermutation(self, curr_array: List[str], candidate: List[str]):
        if len(candidate) == 0:
            self.all_permutation.append(curr_array)
            return

        for i in range(len(candidate)):
            self.getAllPermutation(
                curr_array + [candidate[i]], candidate[:i] + candidate[i+1:])

# TLE
