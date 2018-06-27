class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        self.backtrack(answer, [], nums, 0)
        return answer

    def backtrack(self, answer, tempList, nums, start):
        answer.append(tempList.copy())
        for i in range(start, len(nums)):
            tempList.append(nums[i])
            self.backtrack(answer, tempList, nums, i + 1)
            tempList.remove(tempList[-1])