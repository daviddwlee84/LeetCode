from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        answer = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                target = nums[i] + nums[j]

                # find the leftest edge of target
                left = j + 1
                right = len(nums)
                while left < right:
                    mid = left + (right - left) // 2
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid

                length = left - j - 1

                answer += length

        return answer
