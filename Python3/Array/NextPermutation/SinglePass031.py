from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        # Find the first decreasing from the end
        i = len(nums)-1
        while i > 0:
            if nums[i] > nums[i-1]:
                break
            else:
                i -= 1

        # if i == 0 means it can't find the "first decreasing" item
        # thus it will be the largest permutation
        # so just reverse the entire array
        if i >= 1:
            # Find the number just right larger than nums[i-1]
            # Just search from the end because the tail part
            # MUST be accending order this way
            for j in range(len(nums)-1, i-1, -1):
                if nums[j] > nums[i-1]:
                    break
            nums[i-1], nums[j] = nums[j], nums[i-1]
        
        self.reverseFrom(nums, i)

    def reverseFrom(self, nums: List[int], start: int):
        end = len(nums)-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
