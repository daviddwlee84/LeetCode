from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        j = 0
        for i in range(1, arr[-1] + k + 1):
            if j < len(arr) and i == arr[j]:
                # print('match', i, k)
                j += 1
            else:
                # print('missing', i, k)
                k -= 1
            if k == 0:
                return i
