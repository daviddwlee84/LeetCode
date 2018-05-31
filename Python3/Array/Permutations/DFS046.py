class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(ans, [], nums)
        return ans
            
    def dfs(self, answer, path, nums):
        if not nums:
            # if no more num to add
            answer.append(path)
        
        for i in range(len(nums)):
            # each time add the ith num into path and remove from nums
            self.dfs(answer, path + [nums[i]], nums[:i] + nums[i+1:])

def main():
    print(Solution().permute([1, 2, 3]))

if __name__ == '__main__':
    main()