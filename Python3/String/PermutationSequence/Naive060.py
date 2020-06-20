from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return ''.join(list(permutations('123456789'[:n]))[k-1])

# Runtime: 2220 ms, faster than 10.20% of Python3 online submissions for Permutation Sequence.
# Memory Usage: 57.4 MB, less than 5.04% of Python3 online submissions for Permutation Sequence.
