class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            if i != len(nums):
                for j in range(i+1, len(nums)):
                    if nums[i]+nums[j] == target:
                        return [i, j]

def main():
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum((-3, 4, 3, 90), 0))

if __name__ == "__main__":
    main()
  