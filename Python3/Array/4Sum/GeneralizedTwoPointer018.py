from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.answer = []
        self.findNSum(nums, target, 4, [])
        return self.answer

    def findNSum(self, nums: List[int], target: int, N: int, result: List[int]):
        if len(nums) < N or N < 2:
            return # invalid case (early termination)

        if N == 2: # 2Sum
            left, right = 0, len(nums)-1 # initialize the pointer
            while left < right:
                if nums[left] + nums[right] == target: # found the answer
                    self.answer.append(result + [nums[left], nums[right]])
                    left += 1; right -= 1 # at least move to next one (for different combination)
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1 # if left one is still the same, keep moving
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1 # if right one is still the same, keep moving
                elif nums[left] + nums[right] < target: # current sum too small
                    left += 1
                else: # current sum too big
                    right -= 1
        else: # More than 2Sum
            for i in range(len(nums)-N+1):
                if target < nums[i]*N or target > nums[-1]*N: # the case that can never fulfill
                    break # early termination (take advantages of sorted list)
                
                if i == 0 or i > 0 and nums[i-1] != nums[i]: # recursively reduce N
                    # put nums[i] into candidate list and try
                    self.findNSum(nums[i+1:], target-nums[i], N-1, result+[nums[i]])
