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

        return digits
