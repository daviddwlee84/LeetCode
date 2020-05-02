from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        # If the current element is not 0, then we need to
        # append it just in front of last non 0 element we found. 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1
            
        
        # After we have finished processing new elements,
        # all the non-zero elements are already at beginning of array.
        # We just need to fill remaining array with 0's.
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0
