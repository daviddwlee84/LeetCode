from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.ans = 0
        self.S = S
        self.helper(nums, currentSum = 0)
        return self.ans
    
    def helper(self, nums: List[int], currentSum):
        if len(nums) == 0 and currentSum == self.S:
            self.ans += 1
        elif len(nums) > 0:
            last_num = nums.pop()
            self.helper(nums.copy(), currentSum - last_num)
            self.helper(nums.copy(), currentSum + last_num)

# Time Limit Exceeded
