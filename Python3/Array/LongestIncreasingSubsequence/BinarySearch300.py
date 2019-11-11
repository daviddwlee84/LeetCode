from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        array = []
        for num in nums:
            i = self._binarySearch(array, num)
            if i < 0: # not found num in array
                # i is the (-(insertion point) - 1)
                i = -(i + 1) # get insertion point
            
            if i < len(array):
                array[i] = num
            else:
                array.append(num)

        # although the array itself is not the LIS
        # but the length match
        return len(array)
            
    def _binarySearch(self, array, x):
        # iterative version of binary search
        left = 0
        right = len(array)

        while left < right:
            mid = (left + right)//2
            if array[mid] == x:
                return mid
            elif x > array[mid]:
                left = mid + 1
            else:
                right = mid

        # element not found
        # returns -(insertion point) - 1
        return -(left + 1)
