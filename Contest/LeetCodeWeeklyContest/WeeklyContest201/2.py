class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        while n > 0:
            s = s + '1' + self.reverse(self.invert(s))
            n -= 1

        return s[k-1]

    def reverse(self, s):
        return ''.join(reversed(s))

    def invert(self, s):
        invert_s = []
        for c in s:
            if c == '0':
                invert_s.append('1')
            else:
                invert_s.append('0')
        return ''.join(invert_s)
