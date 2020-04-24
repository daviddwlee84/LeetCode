from typing import List

# Might fail at this case
#
# [
#     short
#     short
#     short
#     loooooooooooooooooooooooooooooong
#     short
#     short
# ]


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        final_length = 0
        for arr in nums:
            final_length += len(arr)

        order = 1
        i = 0
        answer = [nums[0][0]]

        while len(answer) < final_length:

            if order - i < len(nums) and i < len(nums[order - i]):
                answer.append(nums[order - i][i])
            else:
                order += 1
                i = 0
                continue

            if i == order:
                order += 1
                i = 0
            else:
                i += 1

        return answer


# TLE
