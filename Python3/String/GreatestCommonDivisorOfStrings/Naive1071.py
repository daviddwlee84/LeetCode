import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = math.gcd(len(str1), len(str2))

        while gcd:
            if len(str1) % gcd != 0 or len(str2) % gcd != 0:
                gcd -= 1
                continue

            pattern = str1[:gcd]

            if pattern * (len(str1) // gcd) == str1 and pattern * (len(str2) // gcd) == str2:
                return pattern

            gcd -= 1

        return ''
