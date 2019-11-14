from typing import List

# Time Limit Exceeded
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        self.table = {}

        for num in nums:
            if num-1 in self.table:
                self.table[num] = self.table[num-1] + 1
            else:
                self.table[num] = 1
            
            self.updateHigherThan(num+1)

        return max(self.table.values())

    def updateHigherThan(self, num: int):
        if num in self.table:
            self.table[num] = self.table[num-1] + 1
            self.updateHigherThan(num+1)
