from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        answer = []
        for i, _ in sorted(sorted([(i, num) for i, num in enumerate(nums)], key=lambda x: x[1])[-k:], key=lambda x: x[0]):
            # print(i, nums[i])
            answer.append(nums[i])
        return answer
