class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Sort the array first will reduce the time complexity of
        # searching element while to make sure they won't duplicate
        nums.sort()

        ans = []
        
        for i in range(len(nums)-2):
            # In case of duplicate list, if the number is duplicated, just move forward
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                # Maintain two pointers from the i+1, to prevent from adding same element
                fp = i+1; bp = len(nums)-1; target = 0-nums[i] # Front pointer, Back pointer, Target sum
                while fp < bp:
                    if nums[fp] + nums[bp] == target:
                        ans.append([nums[i], nums[fp], nums[bp]])
                        while fp < bp and nums[fp] == nums[fp+1]:
                            fp += 1
                        while fp < bp and nums[bp] == nums[bp-1]:
                            bp -= 1
                        fp += 1
                        bp -= 1
                    elif nums[fp] + nums[bp] < target:
                        fp += 1
                    else:
                        bp -= 1
        
        return ans