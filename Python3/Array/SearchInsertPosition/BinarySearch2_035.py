from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (right - left) // 2 + left
        
            # print(mid, nums[mid])

            if nums[mid] == target:
                break
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
            
        # actually, left is mid + 1
        return mid if nums[mid] >= target else mid + 1
