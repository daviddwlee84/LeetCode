from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for i in range(len(nums) // 2):
            answer.append(nums[i])
            if i < len(nums):
                answer.append(nums[i + len(nums) // 2])

        return answer
