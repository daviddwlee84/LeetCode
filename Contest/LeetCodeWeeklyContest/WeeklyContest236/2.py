class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        line = [i + 1 for i in range(n)]

        i = -1

        while len(line) > 1:
            i += k
            if i >= len(line):
                i %= len(line)
            line.pop(i)
            i -= 1

        return line[0]
