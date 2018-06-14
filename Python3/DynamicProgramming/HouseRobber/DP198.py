class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            houseRob = [nums[0], max(nums[:2])] # Initial status

            for i in range(2, len(nums)):
                houseRob.append(max(houseRob[i-2] + nums[i], houseRob[i-1]))
            
            return houseRob[-1]
