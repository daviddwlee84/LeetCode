class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        s = 0
        i = 1
        ans = []
        while i <= len(a) and i <= len(b):
            s = int(a[-i]) + int(b[-i]) + c
            c = s // 2
            s = s % 2
            ans.append(str(s))
            i += 1

        # or we can just padding the leading zeros
        while i <= len(a):
            s = int(a[-i]) + c
            c = s // 2
            s = s % 2
            ans.append(str(s))
            i += 1

        while i <= len(b):
            s = int(b[-i]) + c
            c = s // 2
            s = s % 2
            ans.append(str(s))
            i += 1

        if c:
            ans.append(str(c))

        return ''.join(reversed(ans))
