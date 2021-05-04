from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        https://leetcode.com/problems/non-decreasing-array/solution/
        """

        # We have only one chance to fix
        chance = True

        for i in range(1, len(nums)):

            # Found a violation
            if nums[i - 1] > nums[i]:

                if not chance:
                    # Out of chance
                    return False

                # Make a greediest fix which consider the previous two numbers
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

                chance = False

        return True
