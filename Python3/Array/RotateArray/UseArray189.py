class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        tempArray = [None] * length

        for i in range (length):
            tempArray[(i+k) % length] = nums[i]

        for i in range(len(nums)):
            nums[i] = tempArray[i]
