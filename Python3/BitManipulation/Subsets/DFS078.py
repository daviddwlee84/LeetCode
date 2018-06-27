class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.answer = []
        self.helper([], 0, len(nums), nums)
        return self.answer

    def helper(self, currentSet, start, end, nums):
        if start == end:
            self.answer.append(currentSet)
            return
        self.helper(currentSet + [nums[start]], start+1, end, nums) # With num[start]
        self.helper(currentSet, start+1, end, nums) # Without num[start]
        