class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        newTail = 0
        for i in range(1, len(nums)):
            # Skip all the same number
            # Overwrite the next occur number to num[newTail]
            if nums[newTail] != nums[i]:
                newTail += 1
                nums[newTail] = nums[i]

        nums = nums[:newTail+1] # Optional: because it won't check the index larger than the return

        return newTail + 1
