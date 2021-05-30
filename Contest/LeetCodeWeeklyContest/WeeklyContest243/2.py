class Solution:
    def maxValue(self, n: str, x: int) -> str:
        str_x = str(x)
        if n.startswith('-'):
            # negative
            for i in range(1, len(n)):
                if n[i] > str_x:
                    return n[:i] + str_x + n[i:]
        else:
            # positive
            for i in range(len(n)):
                if n[i] < str_x:
                    return n[:i] + str_x + n[i:]
        return n + str_x
