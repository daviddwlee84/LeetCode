# Digit Root
# congruence formula
# https://en.wikipedia.org/wiki/Digital_root#Congruence_formula


class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9
