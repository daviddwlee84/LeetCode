from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = set()
        for num in nums:
            if num in temp:
                temp.remove(num)
            else:
                temp.add(num)

        return temp.pop()  # will left only one item
