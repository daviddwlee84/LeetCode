from typing import List
from itertools import permutations


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        def flatten(t):
            """
            https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
            """
            return [item for sublist in t for item in sublist]

        for perm_pieces in permutations(pieces):
            if arr == flatten(perm_pieces):
                return True

        return False

# TLE
# [75,1,60,91,84,55,5,39,19,52,38,66,14,17,49]
# [[60],[52,38],[66],[39],[19],[1],[84,55],[17],[14],[49],[91],[5],[75]]
