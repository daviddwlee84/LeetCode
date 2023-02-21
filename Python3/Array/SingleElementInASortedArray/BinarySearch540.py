from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """ 
        https://leetcode.com/problems/single-element-in-a-sorted-array/solutions/627921/java-c-python3-easy-explanation-o-logn-o-1/?orderBy=most_votes

        Pattern: first element takes even position and second element takes odd position
        This pattern will be missed when single element is appeared in the array
        """

        start = 0
        end = len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2
            # Find pattern, the missed element should be at the right part
            #   Even condition                                   Odd condition
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid - 1] == nums[mid]):
                start = mid + 1
            # Pattern was break, the missed element should be at the left part
            else:
                end = mid

        return nums[start]
