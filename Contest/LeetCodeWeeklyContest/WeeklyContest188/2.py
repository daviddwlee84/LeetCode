from typing import List
from functools import reduce


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    a = reduce(lambda x, y: x ^ y, arr[i:j])
                    b = reduce(lambda x, y: x ^ y, arr[j:k+1])

                    # print(a, b, (i, j, k))

                    if a == b:
                        count += 1

        return count

# TLE
