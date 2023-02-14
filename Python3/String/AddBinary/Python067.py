class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(eval(f'0b{a}') + eval(f'0b{b}'))[2:]
