class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashTable = {}

        for i, num in enumerate(nums):
            if target-num in hashTable:
                return [hashTable[target-num], i]
            else:
                # Initialize only when it can't find the number (i.e. the first time see the number)
                hashTable[num] = i

        # # Initialize Hash table
        # for num in nums:
        #     hashTable[num] = nums.index(num)
        
        # # Go through and find the corresponding value index
        # for i, num in enumerate(nums):
        #     toFind = target - num
        #     if toFind in hashTable:
        #         if hashTable[toFind] != i: # If the result isn't itself
        #             return [i, hashTable[toFind]]