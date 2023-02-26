from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()

        # print(nums)

        answer = 0
        left = 0
        right = 0
        while right < len(nums) and nums[left] * 2 > nums[right]:
            right += 1

        left_end = max(right, len(nums) // 2 + 1)
        while right < len(nums) and left < left_end:
            # print(left, right, nums[left], nums[right])
            if nums[left] * 2 <= nums[right]:
                answer += 1
                left += 1
                right += 1
            else:
                right += 1

        return answer


# WA
# [1,78,27,48,14,86,79,68,77,20,57,21,18,67,5,51,70,85,47,56,22,79,41,8,39,81,59,74,14,45,49,15,10,28,16,77,22,65,8,36,79,94,44,80,72,8,96,78,39,92,69,55,9,44,26,76,40,77,16,69,40,64,12,48,66,7,59,10]
# output: 35
# expected: 64
