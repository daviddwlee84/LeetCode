from typing import List
from itertools import permutations


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        steps = 'H' * destination[1] + 'V' * destination[0]
        return ''.join(sorted(list(set(permutations(steps))))[k - 1])

# TLE
# [15,15]
# 155117520

# Even use this are still TLE
# https://more-itertools.readthedocs.io/en/stable/_modules/more_itertools/more.html#distinct_permutations

# Related

# https://www.geeksforgeeks.org/lexicographically-n-th-permutation-string/
# https://www.geeksforgeeks.org/find-n-th-lexicographically-permutation-string-set-2/

# https://stackoverflow.com/questions/4223349/python-implementation-for-next-permutation-in-stl
# https://stackoverflow.com/questions/4250125/generate-permutations-of-list-with-repeated-elements
# https://github.com/more-itertools/more-itertools
