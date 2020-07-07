from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits)-1] += 1  # plus one
        # handle the carrys
        for i in range(len(digits)-1, -1, -1):
            if digits[i] > 9:
                digits[i] -= 10
                if i - 1 >= 0:
                    digits[i-1] += 1
                else:  # index = -1
                    digits.insert(0, 1)
            else:
                break

        return digits

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         digits[-1] += 1
#         i = len(digits) - 1
#         while i >= 0 and digits[i] == 10:
#             digits[i] = 0
#             if i == 0:
#                 digits = [1] + digits
#             else:
#                 digits[i-1] += 1
#             i -= 1
#         return digits