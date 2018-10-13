class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        #import sys
        #mindiff = sys.maxsize

        mindiff = float('inf')

        rtn = 0

        for i in range(len(nums)-2):
            fp = i+1; bp = len(nums)-1
            while fp < bp:
                currentSum = nums[fp]+nums[bp]+nums[i]
                if currentSum == target:
                    return target

                if abs(currentSum-target) < mindiff:
                    rtn = currentSum
                    mindiff = abs(currentSum - target)
                if currentSum > target:
                    bp -= 1
                else:
                    fp += 1
        
        return rtn
