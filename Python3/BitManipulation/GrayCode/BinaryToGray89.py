from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        https://en.wikipedia.org/wiki/Gray_code#Constructing_an_n-bit_Gray_code
        https://zh.wikipedia.org/wiki/%E6%A0%BC%E9%9B%B7%E7%A0%81
        https://stackoverflow.com/questions/8928240/convert-base-2-binary-number-string-to-int
        """
        num = []
        for i in range(2 ** n):
            gray = ''
            binary = bin(i)[2:]
            # add a dummy 0 at the front
            binary = '0' * (n - len(binary) + 1) + binary
            for i in range(len(binary) - 1):
                gray = str(int(binary[len(binary) - 1 - i])
                           ^ int(binary[len(binary) - 2 - i])) + gray
            # print(binary)
            # print(gray)
            num.append(int(gray, 2))
        return num

# Runtime: 1136 ms, faster than 5.09% of Python3 online submissions for Gray Code.
# Memory Usage: 21.6 MB, less than 66.40% of Python3 online submissions for Gray Code.
