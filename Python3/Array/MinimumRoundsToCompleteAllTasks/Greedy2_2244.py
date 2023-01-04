from typing import List
from collections import Counter


class Solution:

    # Keep update all seen cases
    # (but this solution is slower)
    base_cases = {
        0: 0,
        1: -1,
        2: 1,
        3: 1,
        4: 2,
        5: 2
    }

    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)

        answer = 0

        for count in counter.values():
            temp_count = [count]
            temp = 0
            while count not in self.base_cases:
                count -= 3
                temp_count.append(count)
                temp += 1

            if self.base_cases[count] < 0:
                return -1

            temp += self.base_cases[count]
            for i, c in enumerate(temp_count):
                self.base_cases[c] = temp - i
            answer += temp

        return answer

# class Solution:
#
#     base_cases = {
#         0: 0,
#         1: -1,
#         2: 1,
#         3: 1,
#         4: 2,
#         5: 2
#     }
#
#
#     def minimumRounds(self, tasks: List[int]) -> int:
#         counter = Counter(tasks)
#        
#         answer = 0
#        
#         for count in counter.values():
#             ori_count = count
#             temp = 0
#             while count not in self.base_cases:
#                 count -= 3
#                 temp += 1
#
#             if self.base_cases[count] < 0:
#                 return -1
#
#             temp += self.base_cases[count]
#             self.base_cases[ori_count] = temp
#             answer += temp
#
#         return answer