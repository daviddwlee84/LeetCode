from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        answer = 0
        double_nums = [num * 2 for num in nums]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # print(i, j, double_nums[i], nums[j])
                if double_nums[i] <= nums[j]:
                    answer += 1

        return answer * 2

# WA
# [1,78,27,48,14,86,79,68,77,20,57,21,18,67,5,51,70,85,47,56,22,79,41,8,39,81,59,74,14,45,49,15,10,28,16,77,22,65,8,36,79,94,44,80,72,8,96,78,39,92,69,55,9,44,26,76,40,77,16,69,40,64,12,48,66,7,59,10]
# output: 1184
# expected: 64
