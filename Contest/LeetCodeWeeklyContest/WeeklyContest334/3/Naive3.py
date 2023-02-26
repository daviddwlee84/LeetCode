from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        answer = 0
        double_nums = [num * 2 for num in nums]
        marked = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i not in marked and j not in marked and double_nums[i] <= nums[j]:
                    marked.add(i)
                    marked.add(j)
                    answer += 1

        return answer

# WA
# [1,78,27,48,14,86,79,68,77,20,57,21,18,67,5,51,70,85,47,56,22,79,41,8,39,81,59,74,14,45,49,15,10,28,16,77,22,65,8,36,79,94,44,80,72,8,96,78,39,92,69,55,9,44,26,76,40,77,16,69,40,64,12,48,66,7,59,10]
# output: 30
# expected: 64
