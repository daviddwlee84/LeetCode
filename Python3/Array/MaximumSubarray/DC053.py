class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.getMax(nums, 0, len(nums)-1)

    def getMax(self, nums, start, end):
        if start == end:
            return nums[start]
        
        middle = (start+end)//2

        leftMax = self.getMax(nums, start, middle)
        rightMax = self.getMax(nums, middle+1, end)
        crossMax = self.getCrossMax(nums, start, middle, end)

        return max(leftMax, rightMax, crossMax)

    def getCrossMax(self, nums, start, middle, end):
        leftMax = nums[middle]
        leftSum = 0
        rightMax = nums[middle + 1]
        rightSum = 0

        for i in range(middle, start-1, -1):
            leftSum += nums[i]
            leftMax = max(leftMax, leftSum)
        
        for i in range(middle+1, end+1):
            rightSum += nums[i]
            rightMax = max(rightMax, rightSum)

        return leftMax + rightMax
