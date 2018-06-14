class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for _ in range(k):
            # Python version of swap
            nums[0], nums[1:length] = nums[length-1], nums[:length-1]
            
            # It doesn't work when call by reference
            # nums = [nums[length-1]] + nums[:length-1]

            # It will cause Time Limit Exceeded error
            # nums[:] = [nums[length-1]] + nums[:length-1]

