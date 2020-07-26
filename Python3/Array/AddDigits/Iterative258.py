class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            temp = num
            new_num = 0
            while temp > 0:
                new_num += temp % 10
                temp //= 10
            num = new_num
        return num
