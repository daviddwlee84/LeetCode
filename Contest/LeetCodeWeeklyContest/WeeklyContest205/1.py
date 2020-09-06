import random


class Solution:
    def modifyString(self, s: str) -> str:

        def is_consecutive_repeating(i: int, char: str, s: str):
            if char in set(s[max(i - 1, 0):min(i + 1, len(s)) + 1]):
                return True
            return False

        # eng_set = set(chr(i) for i in range(ord('a'), ord('z') + 1))
        answer = ''
        for i in range(len(s)):
            if s[i] == '?':
                rnd = ord(s[i])
                while is_consecutive_repeating(i, chr(rnd), s):
                    rnd = random.randint(ord('a'), ord('z'))
                answer += chr(rnd)
                s = s[:i] + chr(rnd) + s[i + 1:]
            else:
                answer += s[i]

        return answer


# "?f???sqmqt?ce"
