from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        left = []
        for c, r in zip(capacity, rocks):
            left.append(c - r)

        full_bags = 0

        left.sort()
        for l in left:
            if l == 0:
                full_bags += 1
                continue

            additionalRocks -= l
            if additionalRocks >= 0:
                full_bags += 1
            else:
                break

        return full_bags
