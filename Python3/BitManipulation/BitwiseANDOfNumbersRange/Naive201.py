class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        answer = n
        for i in reversed(range(m, n)):
            answer &= i
        return answer

# TLE
