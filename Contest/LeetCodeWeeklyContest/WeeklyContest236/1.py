from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:

        def signFunc(x: int):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0

        neg_one_count = 0
        for num in nums:
            res = signFunc(num)
            if res == 0:
                return 0

            if res == -1:
                neg_one_count += 1

        return 1 if neg_one_count % 2 == 0 else -1
