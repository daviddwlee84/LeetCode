class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lastTemp = None
        for i in range(len(nums)):
            if nums[i] == lastTemp:
                lastTemp = nums[i]
                nums[i] = None
            else:
                lastTemp = nums[i]
        
        while None in nums:
            nums.remove(None)

        return len(nums)
