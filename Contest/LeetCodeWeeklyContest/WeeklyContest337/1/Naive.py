from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        answer = [0, 0]
        for i, val in enumerate(reversed(bin(n)[2:])):
            if val == '1':
                if i % 2 == 0:
                    answer[0] += 1
                else:
                    answer[1] += 1

        return answer
