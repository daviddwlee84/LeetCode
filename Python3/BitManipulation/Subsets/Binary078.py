class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        """
        Binary Method
        3 numbers
        0 - 000
        1 - 001
        2 - 010
        3 - 011
        4 - 100
        5 - 101
        6 - 110
        7 - 111
        If 1 => pick that number
        """
        for i in range(2**len(nums)):
            answer.append([])
            ans_pos = i
            nums_pos = 0
            while i > 0:
                if i%2 == 1: # if that bit is 1
                    answer[ans_pos].append(nums[nums_pos])
                nums_pos += 1
                i //= 2 # shift right
        return answer