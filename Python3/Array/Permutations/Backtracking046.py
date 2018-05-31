class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.permuteHelper(ans, [], nums)
        return ans

    # Backtracking
    def permuteHelper(self, answer, permuteTemp, nums):
        """
        :type answer: List[List[int]] 
        :type permuteTemp: List[int]
        :type nums: List[int]
        """
        if len(permuteTemp) == len(nums):
            # Use permuteTemp.copy() or python will copy the reference to the list
            # (or use permuteTemp[:], list(permuteTemp))
            answer.append(permuteTemp.copy()) 
        else:
            for i in nums:
                if i in permuteTemp:
                    continue # If the number exist in the list
                else:
                    permuteTemp.append(i) # Add new number in to the list
                    self.permuteHelper(answer, permuteTemp, nums)
                    permuteTemp.remove(permuteTemp[-1]) # Remove the last number


def main():
    print(Solution().permute([1, 2, 3]))

if __name__ == '__main__':
    main()