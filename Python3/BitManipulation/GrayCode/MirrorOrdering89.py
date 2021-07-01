from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        https://en.wikipedia.org/wiki/Gray_code#Constructing_an_n-bit_Gray_code
        https://zh.wikipedia.org/wiki/%E6%A0%BC%E9%9B%B7%E7%A0%81
        """
        num = [0, 1]
        if n == 1:
            return num

        for shift in range(1, n):
            num += list(reversed(num))
            for i in range(len(num)):
                if i >= len(num) // 2:
                    num[i] += 1 << shift

            # print(num)

        return num

# Runtime: 128 ms, faster than 45.02% of Python3 online submissions for Gray Code.
# Memory Usage: 21.5 MB, less than 66.40% of Python3 online submissions for Gray Code.
