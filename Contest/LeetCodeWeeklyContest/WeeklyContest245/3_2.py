from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_a, found_b, found_c = False, False, False
        for triplet in triplets:
            if not found_a and triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                found_a = True
            if not found_b and triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
                found_b = True
            if not found_c and triplet[2] == target[2] and triplet[1] <= target[1] and triplet[0] <= target[0]:
                found_c = True

        return found_a and found_b and found_c
