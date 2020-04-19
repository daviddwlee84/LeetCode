from typing import List


class Solution:
    """ https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/587024/C%2B%2B-Detailed-and-Easy-to-Understand-Solution-Explanation """

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            midElement = nums[mid]
            curLeft = nums[left]
            curRight = nums[right]

            # If target found, return the index
            if midElement == target:
                return mid

            # If middle element is less thant the current left (mid element is in the right section of the rotation)
            if midElement < curLeft:
                if midElement < target <= curRight:
                    # target is in the right of midElement
                    left = mid + 1
                else:
                    right = mid - 1

            # If middle is greater than the current right (mid element is in the left section of the rotation)
            elif midElement > curRight:
                if curLeft <= target < midElement:
                    right = mid - 1
                else:
                    left = mid + 1

            # No rotation
            else:
                if target > midElement:
                    left = mid + 1
                else:
                    right = mid - 1

        # value does not exist
        return -1
