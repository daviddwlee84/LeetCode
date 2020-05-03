from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist = -1
        for num in nums:
            if num == 1:
                if dist >= 0:
                    if dist < k:
                        return False
                dist = 0
            elif num == 0 and dist >= 0:
                dist += 1

        return True
