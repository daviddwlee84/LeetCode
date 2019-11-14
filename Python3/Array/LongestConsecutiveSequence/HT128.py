from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums_set = set(nums)

        for num in nums:
            if num - 1 not in nums_set:
                # start new sequence
                current_num = num
                current_streak = 1

                while current_num + 1 in nums_set:
                    # this loop will only run when starting a new sequence
                    current_num += 1
                    current_streak += 1
                
                # update longest streak
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
