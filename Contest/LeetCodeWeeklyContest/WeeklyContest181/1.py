from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        answer = [-1] * len(nums)
        for num, idx in zip(nums, index):
            answer.insert(idx, num)

        return answer[:len(nums)]
