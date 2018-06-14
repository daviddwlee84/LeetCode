class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Store (value, index)
        heshTable = [(value, index) for index, value in enumerate(nums)]
        heshTable.sort() # Sort it

        # Compare from the very beginning and the end
        begin, end = 0, len(nums) - 1
        while begin < end:
            # Sum up the value
            numSum = heshTable[begin][0] + heshTable[end][0]
            if numSum == target:
                # If sum equal target, return theirs index
                return [heshTable[begin][1], heshTable[end][1]]
            elif numSum < target:
                # Sum too small (move begin index)
                begin += 1
            else:
                # Sum too big (move end index)
                end -= 1
        