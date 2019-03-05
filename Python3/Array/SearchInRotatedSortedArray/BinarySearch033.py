from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            middle = (right+left)//2
            print(nums, target, left, middle, right)
            if nums[middle] == target: # found the target
                return middle
            # We only search the sorted side of the array!!
            elif nums[left] < nums[middle]: # left sub-array is sorted
                if nums[left] <= target < nums[middle]: # target is in this sub-array
                    right = middle - 1
                else: # target is not in this sub-array
                    left = middle + 1
            elif nums[right] > nums[middle]: # vise versa for the right sub-array
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            else: # no such 'sub-array': single element left
                break

        # The target might either in left or right, otherwise it don't exist
        if left < len(nums) and nums[left] == target:
            return left
        elif right > -1 and nums[right] == target:
            return right
        else:
            return -1
