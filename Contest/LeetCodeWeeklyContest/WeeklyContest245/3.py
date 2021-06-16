from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid_set = []
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                valid_set.append(triplet)

        max_a, max_b, max_c = 0, 0, 0
        for triplet in valid_set:
            max_a = max(max_a, triplet[0])
            max_b = max(max_b, triplet[1])
            max_c = max(max_c, triplet[2])

        return [max_a, max_b, max_c] == target
