from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashTable = {}

        for num in nums:
            if num in hashTable:
                # all the twice element will be pop
                hashTable.pop(num)
            else:
                # the first time
                hashTable[num] = 1

        return hashTable.popitem()[0]  # should have only one element left
