from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        https://en.wikipedia.org/wiki/Gray_code#Constructing_an_n-bit_Gray_code
        https://zh.wikipedia.org/wiki/%E6%A0%BC%E9%9B%B7%E7%A0%81
        https://stackoverflow.com/questions/8928240/convert-base-2-binary-number-string-to-int
        """
        i = 0
        num = [0] * n
        ans = []
        flip_right_most = True
        for _ in range(2**n):
            ans.append(int(''.join(str(bit) for bit in num), 2))

            if flip_right_most:
                i = 0
            else:
                i = (num.index(1) + 1) % len(num)

            # reverse bit i
            num[i] ^= 1
            flip_right_most ^= True

        return ans


# 3
# [0,1,3,2,6,7,5,4]
# 4
# [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8]
# Runtime: 432 ms, faster than 5.66% of Python3 online submissions for Gray Code.
# Memory Usage: 21.7 MB, less than 39.93% of Python3 online submissions for Gray Code.
