from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        pointer = 0
        i = 1
        last_miss = 0
        while k and pointer < len(arr):
            while i < arr[pointer] and k:
                # print(i, arr[pointer])
                last_miss = i
                i += 1
                k -= 1
            i += 1
            pointer += 1
        
        if k == 0:
            return last_miss + k
        return arr[-1] + k
