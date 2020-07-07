from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        new_digits = []
        for digit in reversed(digits):
            carry, temp = self.fullAdder(digit, 0, carry)
            new_digits.append(temp)
        if carry:
            new_digits.append(1)
        
        return list(reversed(new_digits))
    
    def fullAdder(self, A: int, B: int, Cin: int) -> List[int]:
        S = A + B + Cin
        return S // 10, S % 10
    