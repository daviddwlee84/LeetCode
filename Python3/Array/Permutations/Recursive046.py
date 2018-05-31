class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.permuteHelper(ans, 0, nums)
        return ans

    def swapListMember(self, lst, idx1, idx2):
        lst[idx1], lst[idx2] = lst[idx2], lst[idx1] 
    
    # permute num[begin..end]
    # finished num[0..begin-1]
    def permuteHelper(self, answer, begin, num):
        if begin >= len(num):
            answer.append(num.copy())
        else:
            for i in range(begin, len(num)):
                self.swapListMember(num, begin, i) # swap
                self.permuteHelper(answer, begin + 1, num)
                self.swapListMember(num, begin, i) # swap it back

def main():
    print(Solution().permute([1, 2, 3]))

if __name__ == '__main__':
    main()


        

