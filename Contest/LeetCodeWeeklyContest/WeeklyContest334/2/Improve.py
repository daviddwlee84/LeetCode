from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        answer = []
        left = 0
        for c in word:
            left += int(c)
            left %= m
            answer.append(1 if left == 0 else 0)
            left *= 10
        return answer

# WA (fixed)
# "4065582576255570359135118255554163128235573295923545700491253287387"
# 5
# output:   [0,1,0,1,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0]
# expected: [0,1,0,1,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0]
